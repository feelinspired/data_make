"""
Field Mapping Engine for Data Whisperer
Provides intelligent field mapping suggestions based on name similarity
"""
import re
from difflib import SequenceMatcher
from typing import List, Dict, Any, Tuple


def normalize_field_name(field: str) -> str:
    """
    Normalize field names for better comparison:
    - Convert to lowercase
    - Replace common separators with underscores
    - Remove special characters
    """
    # Convert camelCase to snake_case
    field = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', field)
    field = re.sub('([a-z0-9])([A-Z])', r'\1_\2', field)
    
    # Convert to lowercase and replace separators
    field = field.lower()
    field = re.sub(r'[-.\s]+', '_', field)
    
    # Remove special characters
    field = re.sub(r'[^a-z0-9_]', '', field)
    
    return field


def calculate_similarity(source: str, target: str) -> float:
    """
    Calculate similarity score between two field names (0.0 to 1.0)
    Uses multiple heuristics for best matching
    """
    # Normalize both fields
    source_norm = normalize_field_name(source)
    target_norm = normalize_field_name(target)
    
    # Exact match after normalization
    if source_norm == target_norm:
        return 1.0
    
    # Sequence matcher for overall similarity
    base_similarity = SequenceMatcher(None, source_norm, target_norm).ratio()
    
    # Boost score if one contains the other
    if source_norm in target_norm or target_norm in source_norm:
        base_similarity = max(base_similarity, 0.85)
    
    # Common synonyms/abbreviations
    synonyms = {
        'id': ['identifier', 'uid', 'key', 'code'],
        'name': ['title', 'label', 'display_name'],
        'email': ['e_mail', 'mail', 'email_address'],
        'phone': ['telephone', 'tel', 'phone_number', 'mobile'],
        'address': ['addr', 'location', 'street'],
        'user': ['customer', 'client', 'contact'],
        'date': ['datetime', 'timestamp', 'time'],
        'created': ['create_date', 'created_at', 'creation_date'],
        'updated': ['update_date', 'updated_at', 'modification_date'],
    }
    
    # Check for synonym matches
    for key, values in synonyms.items():
        if (key in source_norm and any(v in target_norm for v in values)) or \
           (key in target_norm and any(v in source_norm for v in values)):
            base_similarity = max(base_similarity, 0.8)
    
    return round(base_similarity, 2)


def flatten_json(data: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Flatten nested JSON structure to dot-notation paths
    Example: {"user": {"name": "John"}} -> {"user.name": "John"}
    """
    items = []
    
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        
        if isinstance(value, dict):
            items.extend(flatten_json(value, new_key, sep=sep).items())
        elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
            # For arrays of objects, use first item as template
            items.extend(flatten_json(value[0], f"{new_key}[]", sep=sep).items())
        else:
            items.append((new_key, value))
    
    return dict(items)


def extract_fields(json_data: Dict[str, Any]) -> List[str]:
    """
    Extract all field paths from JSON structure
    """
    flattened = flatten_json(json_data)
    return sorted(flattened.keys())


def suggest_mappings(source_fields: List[str], target_fields: List[str], 
                     threshold: float = 0.3) -> List[Dict[str, Any]]:
    """
    Generate mapping suggestions between source and target fields
    
    Returns list of mappings with confidence scores:
    [
        {
            "source": "customer_id",
            "target": "userId",
            "confidence": 0.85,
            "transform": null
        },
        ...
    ]
    """
    mappings = []
    used_targets = set()
    
    # For each source field, find best target match
    for source_field in source_fields:
        best_match = None
        best_score = 0.0
        
        for target_field in target_fields:
            if target_field in used_targets:
                continue
                
            score = calculate_similarity(source_field, target_field)
            
            if score > best_score and score >= threshold:
                best_score = score
                best_match = target_field
        
        if best_match:
            mappings.append({
                "source": source_field,
                "target": best_match,
                "confidence": best_score,
                "transform": None
            })
            used_targets.add(best_match)
        else:
            # No good match found
            mappings.append({
                "source": source_field,
                "target": "",
                "confidence": 0.0,
                "transform": None
            })
    
    # Sort by confidence (highest first)
    mappings.sort(key=lambda x: x["confidence"], reverse=True)
    
    return mappings


def apply_transform(value: Any, transform: str) -> Any:
    """
    Apply a transformation to a value
    """
    if value is None:
        return None
    
    try:
        if transform == "lowercase":
            return str(value).lower()
        elif transform == "uppercase":
            return str(value).upper()
        elif transform == "trim":
            return str(value).strip()
        elif transform == "to_string":
            return str(value)
        elif transform == "to_int":
            # Try to extract first number from string
            if isinstance(value, (int, float)):
                return int(value)
            else:
                # Extract first number from string
                match = re.search(r'-?\d+', str(value))
                if match:
                    return int(match.group())
                return 0
        else:
            return value
    except Exception as e:
        # Return original value if transform fails
        return value


def transform_data(source_data: Dict[str, Any], mappings: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Apply mappings to transform source data to target structure
    """
    result = {}
    source_flat = flatten_json(source_data)
    
    for mapping in mappings:
        source_field = mapping.get("source")
        target_field = mapping.get("target")
        transform = mapping.get("transform")
        
        if not source_field or not target_field:
            continue
        
        # Get value from source
        value = source_flat.get(source_field)
        
        # Apply transformation
        if transform:
            value = apply_transform(value, transform)
        
        # Set in result (handling nested paths)
        if '.' in target_field:
            # Nested field - build structure
            parts = target_field.split('.')
            current = result
            
            for i, part in enumerate(parts[:-1]):
                # Remove array notation if present
                part = part.replace('[]', '')
                if part not in current:
                    current[part] = {}
                current = current[part]
            
            # Set final value
            final_key = parts[-1].replace('[]', '')
            current[final_key] = value
        else:
            result[target_field] = value
    
    return result

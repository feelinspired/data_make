"""
Data Whisperer - Flask Web Application
Map data fields between different JSON structures with AI-powered suggestions
"""
from flask import Flask, render_template, request, jsonify
import json
from mapper import extract_fields, suggest_mappings, transform_data

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    """Render main application page"""
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def analyze():
    """
    Analyze source and target JSON to suggest field mappings
    
    Expected input:
    {
        "source_json": {...},
        "target_json": {...}
    }
    
    Returns:
    {
        "source_fields": [...],
        "target_fields": [...],
        "mappings": [...]
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        source_json = data.get('source_json')
        target_json = data.get('target_json')
        
        if not source_json or not target_json:
            return jsonify({"error": "Both source_json and target_json are required"}), 400
        
        # Parse JSON if strings
        if isinstance(source_json, str):
            source_json = json.loads(source_json)
        if isinstance(target_json, str):
            target_json = json.loads(target_json)
        
        # Extract fields
        source_fields = extract_fields(source_json)
        target_fields = extract_fields(target_json)
        
        # Generate mapping suggestions
        mappings = suggest_mappings(source_fields, target_fields)
        
        return jsonify({
            "source_fields": source_fields,
            "target_fields": target_fields,
            "mappings": mappings,
            "success": True
        })
    
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Invalid JSON: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error analyzing data: {str(e)}"}), 500


@app.route('/api/preview', methods=['POST'])
def preview():
    """
    Preview transformed data based on current mappings
    
    Expected input:
    {
        "source_json": {...},
        "mappings": [...]
    }
    
    Returns:
    {
        "transformed": {...}
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        source_json = data.get('source_json')
        mappings = data.get('mappings', [])
        
        if not source_json:
            return jsonify({"error": "source_json is required"}), 400
        
        # Parse JSON if string
        if isinstance(source_json, str):
            source_json = json.loads(source_json)
        
        # Transform data
        transformed = transform_data(source_json, mappings)
        
        return jsonify({
            "transformed": transformed,
            "success": True
        })
    
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Invalid JSON: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error transforming data: {str(e)}"}), 500


@app.route('/api/export', methods=['POST'])
def export():
    """
    Export mapping configuration as JSON
    
    Expected input:
    {
        "mappings": [...]
    }
    
    Returns:
    {
        "config": {...}
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        mappings = data.get('mappings', [])
        
        # Filter out empty mappings
        valid_mappings = [
            {
                "source": m["source"],
                "target": m["target"],
                "transform": m.get("transform")
            }
            for m in mappings
            if m.get("source") and m.get("target")
        ]
        
        config = {
            "version": "1.0",
            "description": "Data Whisperer mapping configuration",
            "mappings": valid_mappings
        }
        
        return jsonify({
            "config": config,
            "success": True
        })
    
    except Exception as e:
        return jsonify({"error": f"Error exporting config: {str(e)}"}), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "app": "Data Whisperer"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

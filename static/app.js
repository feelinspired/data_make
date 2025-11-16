// Data Whisperer - Interactive Frontend Logic

// Global state
let currentMappings = [];
let currentSourceJson = null;
let currentTargetFields = [];

// Example data for demo
const exampleData = {
    source: {
        customer_id: "CUST-12345",
        full_name: "John Doe",
        email_address: "john.doe@example.com",
        phone_number: "+1-555-0123",
        created_date: "2024-01-15T10:30:00Z",
        account_status: "ACTIVE",
        billing_address: {
            street: "123 Main St",
            city: "San Francisco",
            state: "CA",
            zip_code: "94102"
        },
        total_purchases: 15,
        lifetime_value: "1250.50"
    },
    target: {
        userId: "",
        name: "",
        email: "",
        phone: "",
        registrationDate: "",
        status: "",
        address: {
            street: "",
            city: "",
            state: "",
            postalCode: ""
        },
        purchaseCount: 0,
        revenue: 0.0
    }
};

// Available transforms
const transforms = [
    { value: "", label: "None" },
    { value: "lowercase", label: "Lowercase" },
    { value: "uppercase", label: "Uppercase" },
    { value: "trim", label: "Trim whitespace" },
    { value: "to_string", label: "Convert to string" },
    { value: "to_int", label: "Convert to integer" }
];

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    // Attach event listeners
    document.getElementById('analyzeBtn').addEventListener('click', analyzeMappings);
    document.getElementById('loadExampleBtn').addEventListener('click', loadExample);
    document.getElementById('previewBtn').addEventListener('click', previewTransformation);
    document.getElementById('exportBtn').addEventListener('click', exportConfig);
    
    // Modal controls
    const modal = document.getElementById('exportModal');
    const closeBtn = document.querySelector('.close');
    closeBtn.addEventListener('click', () => modal.style.display = 'none');
    window.addEventListener('click', (e) => {
        if (e.target === modal) modal.style.display = 'none';
    });
    
    document.getElementById('copyConfigBtn').addEventListener('click', copyConfig);
    document.getElementById('downloadConfigBtn').addEventListener('click', downloadConfig);
});

// Load example data
function loadExample() {
    document.getElementById('sourceJson').value = JSON.stringify(exampleData.source, null, 2);
    document.getElementById('targetJson').value = JSON.stringify(exampleData.target, null, 2);
    showSuccess('Example data loaded! Click "Analyze & Suggest Mappings" to continue.');
}

// Analyze and suggest mappings
async function analyzeMappings() {
    const sourceText = document.getElementById('sourceJson').value.trim();
    const targetText = document.getElementById('targetJson').value.trim();
    
    if (!sourceText || !targetText) {
        showError('Please provide both source and target JSON.');
        return;
    }
    
    // Validate JSON
    let sourceJson, targetJson;
    try {
        sourceJson = JSON.parse(sourceText);
        targetJson = JSON.parse(targetText);
    } catch (e) {
        showError(`Invalid JSON: ${e.message}`);
        return;
    }
    
    // Show loading state
    const analyzeBtn = document.getElementById('analyzeBtn');
    analyzeBtn.classList.add('loading');
    hideMessages();
    
    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                source_json: sourceJson,
                target_json: targetJson
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Analysis failed');
        }
        
        // Store state
        currentSourceJson = sourceJson;
        currentTargetFields = data.target_fields;
        currentMappings = data.mappings;
        
        // Display mappings
        displayMappings(data.mappings, data.target_fields);
        document.getElementById('mappingSection').style.display = 'block';
        
        showSuccess(`Found ${data.mappings.length} field mappings! Review and adjust as needed.`);
        
        // Scroll to mappings
        document.getElementById('mappingSection').scrollIntoView({ behavior: 'smooth' });
        
    } catch (error) {
        showError(error.message);
    } finally {
        analyzeBtn.classList.remove('loading');
    }
}

// Display mappings in table
function displayMappings(mappings, targetFields) {
    const tbody = document.getElementById('mappingTableBody');
    tbody.innerHTML = '';
    
    mappings.forEach((mapping, index) => {
        const row = document.createElement('tr');
        
        // Source field
        const sourceCell = document.createElement('td');
        sourceCell.className = 'source-field';
        sourceCell.textContent = mapping.source;
        row.appendChild(sourceCell);
        
        // Arrow
        const arrowCell = document.createElement('td');
        arrowCell.className = 'arrow-cell';
        arrowCell.textContent = '→';
        row.appendChild(arrowCell);
        
        // Target field (dropdown)
        const targetCell = document.createElement('td');
        const targetSelect = document.createElement('select');
        targetSelect.dataset.index = index;
        targetSelect.addEventListener('change', (e) => updateMapping(index, 'target', e.target.value));
        
        // Add empty option
        const emptyOption = document.createElement('option');
        emptyOption.value = '';
        emptyOption.textContent = '-- Select target field --';
        targetSelect.appendChild(emptyOption);
        
        // Add all target fields
        targetFields.forEach(field => {
            const option = document.createElement('option');
            option.value = field;
            option.textContent = field;
            if (field === mapping.target) {
                option.selected = true;
            }
            targetSelect.appendChild(option);
        });
        
        targetCell.appendChild(targetSelect);
        row.appendChild(targetCell);
        
        // Transform (dropdown)
        const transformCell = document.createElement('td');
        const transformSelect = document.createElement('select');
        transformSelect.dataset.index = index;
        transformSelect.addEventListener('change', (e) => updateMapping(index, 'transform', e.target.value));
        
        transforms.forEach(transform => {
            const option = document.createElement('option');
            option.value = transform.value;
            option.textContent = transform.label;
            if (transform.value === mapping.transform) {
                option.selected = true;
            }
            transformSelect.appendChild(option);
        });
        
        transformCell.appendChild(transformSelect);
        row.appendChild(transformCell);
        
        // Confidence
        const confidenceCell = document.createElement('td');
        const badge = document.createElement('span');
        badge.className = `confidence-badge ${getConfidenceClass(mapping.confidence)}`;
        badge.textContent = mapping.confidence > 0 
            ? `${Math.round(mapping.confidence * 100)}%` 
            : 'No match';
        confidenceCell.appendChild(badge);
        row.appendChild(confidenceCell);
        
        tbody.appendChild(row);
    });
}

// Get confidence badge class
function getConfidenceClass(confidence) {
    if (confidence === 0) return 'confidence-none';
    if (confidence >= 0.7) return 'confidence-high';
    if (confidence >= 0.4) return 'confidence-medium';
    return 'confidence-low';
}

// Update mapping
function updateMapping(index, field, value) {
    if (field === 'target') {
        currentMappings[index].target = value;
    } else if (field === 'transform') {
        currentMappings[index].transform = value || null;
    }
    
    // Hide preview when mappings change
    document.getElementById('previewSection').style.display = 'none';
}

// Preview transformation
async function previewTransformation() {
    if (!currentSourceJson) {
        showError('Please analyze data first.');
        return;
    }
    
    const previewBtn = document.getElementById('previewBtn');
    previewBtn.classList.add('loading');
    hideMessages();
    
    try {
        const response = await fetch('/api/preview', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                source_json: currentSourceJson,
                mappings: currentMappings
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Preview failed');
        }
        
        // Display preview
        document.getElementById('originalPreview').textContent = 
            JSON.stringify(currentSourceJson, null, 2);
        document.getElementById('transformedPreview').textContent = 
            JSON.stringify(data.transformed, null, 2);
        
        document.getElementById('previewSection').style.display = 'block';
        document.getElementById('previewSection').scrollIntoView({ behavior: 'smooth' });
        
    } catch (error) {
        showError(error.message);
    } finally {
        previewBtn.classList.remove('loading');
    }
}

// Export configuration
async function exportConfig() {
    const exportBtn = document.getElementById('exportBtn');
    exportBtn.classList.add('loading');
    hideMessages();
    
    try {
        const response = await fetch('/api/export', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                mappings: currentMappings
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Export failed');
        }
        
        // Display in modal
        document.getElementById('exportedConfig').textContent = 
            JSON.stringify(data.config, null, 2);
        document.getElementById('exportModal').style.display = 'block';
        
    } catch (error) {
        showError(error.message);
    } finally {
        exportBtn.classList.remove('loading');
    }
}

// Copy config to clipboard
async function copyConfig() {
    const configText = document.getElementById('exportedConfig').textContent;
    
    try {
        await navigator.clipboard.writeText(configText);
        
        const btn = document.getElementById('copyConfigBtn');
        const originalText = btn.textContent;
        btn.textContent = '✅ Copied!';
        setTimeout(() => {
            btn.textContent = originalText;
        }, 2000);
    } catch (error) {
        alert('Failed to copy to clipboard. Please copy manually.');
    }
}

// Download config as JSON file
function downloadConfig() {
    const configText = document.getElementById('exportedConfig').textContent;
    const blob = new Blob([configText], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = 'data-whisperer-mapping-config.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    const btn = document.getElementById('downloadConfigBtn');
    const originalText = btn.textContent;
    btn.textContent = '✅ Downloaded!';
    setTimeout(() => {
        btn.textContent = originalText;
    }, 2000);
}

// Show error message
function showError(message) {
    const errorDiv = document.getElementById('errorMessage');
    errorDiv.textContent = '❌ ' + message;
    errorDiv.style.display = 'block';
    
    const successDiv = document.getElementById('successMessage');
    successDiv.style.display = 'none';
}

// Show success message
function showSuccess(message) {
    const successDiv = document.getElementById('successMessage');
    successDiv.textContent = '✅ ' + message;
    successDiv.style.display = 'block';
    
    const errorDiv = document.getElementById('errorMessage');
    errorDiv.style.display = 'none';
}

// Hide all messages
function hideMessages() {
    document.getElementById('errorMessage').style.display = 'none';
    document.getElementById('successMessage').style.display = 'none';
}

# 🔮 Data Whisperer

**Smart field mapping between JSON structures** - A beautiful, intelligent web application that helps you map data fields between different apps with AI-powered suggestions.

![Data Whisperer](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## ✨ Features

- 🤖 **Intelligent Field Matching** - Automatically suggests field mappings based on name similarity and smart heuristics
- 📊 **Confidence Scoring** - Each mapping comes with a confidence score to help you make decisions
- 🔄 **Data Transformations** - Apply common transforms like lowercase, uppercase, trim, type conversions
- 👁️ **Live Preview** - See exactly how your data will look after transformation
- 💾 **Export Configuration** - Generate reusable JSON mapping configs
- 🎨 **Beautiful UI** - Modern, dark-themed, responsive interface
- 📱 **Mobile Friendly** - Works great on all devices

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd /Users/chay/Documents/GitHub/KD
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   
   Navigate to: [http://localhost:5000](http://localhost:5000)

---

## 📖 How to Use

### Step 1: Input Your Data

1. **Paste Source JSON** - The data structure from your source application (App A)
2. **Paste Target JSON** - The expected data structure for your target application (App B)

Or click **"Load Example Data"** to see it in action!

### Step 2: Analyze & Map

Click **"Analyze & Suggest Mappings"** and watch the magic happen:
- Data Whisperer will analyze both structures
- Suggest field mappings based on intelligent matching
- Show confidence scores for each mapping

### Step 3: Customize Mappings

Review the suggested mappings:
- **Change target fields** using the dropdown menus
- **Add transformations** if needed (lowercase, uppercase, trim, type conversions)
- **Confidence badges** help you identify strong vs. weak matches:
  - 🟢 Green (70%+) - High confidence
  - 🟡 Yellow (40-69%) - Medium confidence
  - 🔴 Red (<40%) - Low confidence

### Step 4: Preview & Export

1. Click **"Preview Transformation"** to see your data transformed
2. Click **"Export Mapping Config"** to save your configuration
3. Copy to clipboard or download as JSON file

---

## 🧠 How It Works

### Smart Matching Algorithm

Data Whisperer uses multiple heuristics to suggest field mappings:

1. **Normalization**: Converts field names to a standard format (lowercase, snake_case)
2. **Exact Matching**: Finds exact matches after normalization
3. **Similarity Scoring**: Uses sequence matching for partial matches
4. **Substring Detection**: Identifies when one field name contains another
5. **Synonym Recognition**: Knows common field name patterns:
   - `id` ↔ `identifier`, `uid`, `key`
   - `email` ↔ `email_address`, `mail`
   - `user` ↔ `customer`, `client`, `contact`
   - And many more!

### Available Transformations

- **lowercase** - Convert text to lowercase
- **uppercase** - Convert text to UPPERCASE
- **trim** - Remove leading/trailing whitespace
- **to_string** - Convert any value to string
- **to_int** - Extract and convert to integer (handles errors gracefully)

---

## 🏗️ Project Structure

```
KD/
├── app.py              # Flask web server and API endpoints
├── mapper.py           # Core mapping algorithm and transforms
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main UI template
└── static/
    ├── style.css      # Modern, polished styling
    └── app.js         # Interactive frontend logic
```

---

## 🔧 API Endpoints

### POST `/api/analyze`
Analyze JSON structures and suggest mappings

**Request:**
```json
{
  "source_json": {...},
  "target_json": {...}
}
```

**Response:**
```json
{
  "source_fields": ["field1", "field2"],
  "target_fields": ["fieldA", "fieldB"],
  "mappings": [
    {
      "source": "field1",
      "target": "fieldA",
      "confidence": 0.85,
      "transform": null
    }
  ]
}
```

### POST `/api/preview`
Preview transformed data

**Request:**
```json
{
  "source_json": {...},
  "mappings": [...]
}
```

**Response:**
```json
{
  "transformed": {...}
}
```

### POST `/api/export`
Export mapping configuration

**Request:**
```json
{
  "mappings": [...]
}
```

**Response:**
```json
{
  "config": {
    "version": "1.0",
    "mappings": [...]
  }
}
```

---

## 💡 Example Use Case

**Scenario:** You're integrating a CRM system with a marketing platform.

**Source (CRM):**
```json
{
  "customer_id": "CUST-12345",
  "full_name": "John Doe",
  "email_address": "john@example.com",
  "phone_number": "+1-555-0123"
}
```

**Target (Marketing Platform):**
```json
{
  "userId": "",
  "name": "",
  "email": "",
  "phone": ""
}
```

**Result:** Data Whisperer will automatically suggest:
- `customer_id` → `userId` (85% confidence)
- `full_name` → `name` (92% confidence)
- `email_address` → `email` (95% confidence)
- `phone_number` → `phone` (88% confidence)

---

## 🛠️ Development

### Running in Development Mode

The app runs in debug mode by default:
```bash
python app.py
```

Server will auto-reload when you make changes to the code.

### Extending Transformations

Add new transformations in `mapper.py`:

```python
def apply_transform(value: Any, transform: str) -> Any:
    # ... existing transforms ...
    elif transform == "your_transform":
        return your_custom_logic(value)
```

Then update the transforms list in `static/app.js`.

---

## 🎨 Customization

### Change Color Scheme

Edit CSS variables in `static/style.css`:

```css
:root {
    --primary-color: #6366f1;  /* Your brand color */
    --background: #0f172a;      /* Background color */
    /* ... */
}
```

### Add More Synonyms

Edit the `synonyms` dictionary in `mapper.py`:

```python
synonyms = {
    'your_term': ['synonym1', 'synonym2'],
    # ...
}
```

---

## 🐛 Troubleshooting

**Issue:** Port 5000 already in use

**Solution:**
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Or change the port in app.py
app.run(debug=True, port=8080)
```

**Issue:** Module not found errors

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

---

## 📝 License

MIT License - feel free to use this for any purpose!

---

## 🙏 Acknowledgments

Built with:
- [Flask](https://flask.palletsprojects.com/) - Python web framework
- Modern CSS3 with beautiful gradients
- Vanilla JavaScript (no frameworks needed!)

---

## 🤝 Contributing

Found a bug? Have a feature idea? Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📧 Support

Questions? Issues? Feel free to open an issue or reach out!

---

**Made with ❤️ by Data Whisperer | Smart field mapping for seamless integrations**

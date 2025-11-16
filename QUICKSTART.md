# Quick Setup Guide for Data Whisperer

## 🚀 Get Started in 3 Steps

### Option 1: Using the Start Script (Easiest)

```bash
cd /Users/chay/Documents/GitHub/KD
./start.sh
```

The script will automatically:
- Create a virtual environment
- Install all dependencies
- Start the application

### Option 2: Manual Setup

```bash
# 1. Navigate to the project
cd /Users/chay/Documents/GitHub/KD

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python app.py
```

### Option 3: Quick Test (No Virtual Environment)

```bash
cd /Users/chay/Documents/GitHub/KD
pip3 install Flask
python3 app.py
```

---

## 🌐 Access the Application

Once running, open your browser and go to:
**http://localhost:5000**

---

## ✅ First-Time User Guide

1. Click **"Load Example Data"** button
2. Click **"Analyze & Suggest Mappings"**
3. Review the suggested field mappings
4. Click **"Preview Transformation"** to see the result
5. Click **"Export Mapping Config"** to save your configuration

---

## 🛑 Stopping the Server

Press `Ctrl+C` in the terminal where the app is running.

---

## 💡 Tips

- The app auto-detects nested JSON structures
- Use the confidence scores to validate mappings
- Try different transformations for data type conversions
- Export configs can be reused in your integrations

Enjoy mapping! 🔮

# 📥 Clone & Run Data Whisperer - Complete Guide

## 🎯 How to Get This Code Running on Your Computer

Follow these simple steps to clone and run the Data Whisperer application on your local machine.

---

## 📋 Prerequisites

Before you start, make sure you have:

- ✅ **Git** installed ([Download here](https://git-scm.com/downloads))
- ✅ **Python 3.8+** installed ([Download here](https://www.python.org/downloads/))
- ✅ A **terminal/command prompt**

---

## 🚀 Quick Start (5 Minutes)

### **Step 1: Clone the Repository**

Open your terminal and run:

```bash
# Clone the repository
git clone https://github.com/feelinspired/data_make.git

# Navigate into the project folder
cd data_make
```

**What this does:** Downloads all the code to your computer in a folder called `data_make`.

---

### **Step 2: Install Dependencies**

```bash
# Install Flask (the only required dependency)
pip3 install Flask
```

**Or if that doesn't work:**
```bash
pip install Flask
```

**Or on Windows:**
```bash
python -m pip install Flask
```

---

### **Step 3: Run the Application**

```bash
# Start the server
python3 app.py
```

**Or on Windows:**
```bash
python app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
```

---

### **Step 4: Open in Browser**

Open your web browser and go to:
```
http://localhost:5001
```

**🎉 That's it! The app is now running!**

---

## 🖥️ Detailed Instructions by Operating System

### **macOS**

```bash
# 1. Open Terminal (Command + Space, type "Terminal")

# 2. Clone the repository
git clone https://github.com/feelinspired/data_make.git
cd data_make

# 3. Install Flask
pip3 install Flask

# 4. Run the app
python3 app.py

# 5. Open http://localhost:5001 in your browser
```

---

### **Windows**

```cmd
# 1. Open Command Prompt or PowerShell

# 2. Clone the repository
git clone https://github.com/feelinspired/data_make.git
cd data_make

# 3. Install Flask
pip install Flask

# 4. Run the app
python app.py

# 5. Open http://localhost:5001 in your browser
```

---

### **Linux / Ubuntu**

```bash
# 1. Open Terminal

# 2. Clone the repository
git clone https://github.com/feelinspired/data_make.git
cd data_make

# 3. Install Flask
pip3 install Flask
# Or if pip3 doesn't exist:
sudo apt-get install python3-pip
pip3 install Flask

# 4. Run the app
python3 app.py

# 5. Open http://localhost:5001 in your browser
```

---

## 🔧 Alternative: Using Virtual Environment (Recommended)

For a cleaner installation that doesn't affect your system Python:

### **macOS / Linux**

```bash
# 1. Clone the repository
git clone https://github.com/feelinspired/data_make.git
cd data_make

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
python app.py

# When done, deactivate virtual environment
deactivate
```

---

### **Windows**

```cmd
# 1. Clone the repository
git clone https://github.com/feelinspired/data_make.git
cd data_make

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
python app.py

# When done, deactivate virtual environment
deactivate
```

---

## 📦 What Gets Downloaded

When you clone the repository, you'll get:

```
data_make/
├── app.py                    # Flask web server
├── mapper.py                 # Smart mapping algorithm
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html           # User interface
├── static/
│   ├── style.css            # Styling
│   └── app.js               # JavaScript functionality
├── README.md                # Documentation
├── QUICKSTART.md            # Quick start guide
├── examples.json            # Example data
└── test_installation.py     # Test suite
```

---

## ✅ Verify Installation

Test that everything works:

```bash
# Run the test suite
python3 test_installation.py
```

You should see:
```
🎉 All tests passed! Data Whisperer is ready to use.
```

---

## 🌐 Using the Application

Once the app is running at http://localhost:5001:

1. **Try the Demo:**
   - Click "📋 Load Example Data"
   - Click "✨ Analyze & Suggest Mappings"
   - Review the suggested field mappings
   - Click "👁️ Preview Transformation"
   - Click "💾 Export Mapping Config"

2. **Use Your Own Data:**
   - Paste your source JSON (from App A)
   - Paste your target JSON (for App B)
   - Click "Analyze & Suggest Mappings"
   - Adjust mappings and transforms as needed
   - Preview and export!

---

## 🛑 Stopping the Server

To stop the application:
- Press **Ctrl + C** in the terminal

---

## 🔄 Updating to Latest Version

To get the latest updates from GitHub:

```bash
# Navigate to the project folder
cd data_make

# Pull latest changes
git pull origin main

# Restart the app
python3 app.py
```

---

## 🐛 Troubleshooting

### **"Port 5001 is in use"**

**Solution:** The app will show which port is in use. You can either:
- Stop the program using that port
- Or edit `app.py` to use a different port (change `5001` to `5002`)

---

### **"Flask not found" or "No module named flask"**

**Solution:**
```bash
# Try installing with different methods:
pip3 install Flask
# or
pip install Flask
# or
python3 -m pip install Flask
# or
python -m pip install Flask
```

---

### **"python3: command not found" (Windows)**

**Solution:** Use `python` instead of `python3`:
```bash
python app.py
```

---

### **"git: command not found"**

**Solution:** 
1. Download Git from: https://git-scm.com/downloads
2. Install it
3. Restart your terminal
4. Try again

---

### **Can't access http://localhost:5001**

**Solutions:**
1. Make sure the server is running (look for "Running on..." message)
2. Try `http://127.0.0.1:5001` instead
3. Check your firewall settings
4. Make sure no other app is using port 5001

---

## 💡 Tips

1. **Keep it running:** The server needs to stay running in the terminal while you use the app
2. **Open in new terminal:** If you need to run other commands, open a new terminal window
3. **Save your work:** Export your mapping configs before closing the browser

---

## 📚 Additional Resources

- **Full Documentation:** See `README.md` in the project folder
- **Quick Start Guide:** See `QUICKSTART.md`
- **Troubleshooting:** See `TROUBLESHOOTING.md`
- **GitHub Issues:** https://github.com/feelinspired/data_make/issues

---

## 🆘 Still Need Help?

1. Check the documentation files in the repository
2. Open an issue on GitHub: https://github.com/feelinspired/data_make/issues
3. Make sure Python 3.8+ is installed: `python3 --version`

---

## 🎉 Success Checklist

- ✅ Cloned the repository
- ✅ Installed Flask
- ✅ Ran `python3 app.py`
- ✅ Opened http://localhost:5001 in browser
- ✅ Saw the Data Whisperer interface
- ✅ Loaded example data and tried it out

**Welcome to Data Whisperer! 🔮**

---

## 📝 Quick Command Reference

```bash
# Clone
git clone https://github.com/feelinspired/data_make.git

# Setup
cd data_make
pip3 install Flask

# Run
python3 app.py

# Update
git pull origin main

# Test
python3 test_installation.py
```

---

**Repository:** https://github.com/feelinspired/data_make

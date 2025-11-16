# Data Whisperer - Alternative Start Guide

## ⚠️ Xcode License Issue?

If you're seeing the Xcode license prompt, here are your options:

### Option 1: Accept Xcode License (Recommended)
```bash
sudo xcodebuild -license
```
- Enter your password
- Press space to scroll or 'q' to skip to end
- Type 'agree'
- Then run: `python3 app.py`

### Option 2: Use Homebrew Python (No Xcode needed)
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python via Homebrew
brew install python3

# Install Flask
brew install python3 && pip3 install Flask

# Run the app
python3 app.py
```

### Option 3: Use Docker (Cleanest)
```bash
# Create Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
EOF

# Build and run
docker build -t data-whisperer .
docker run -p 5000:5000 data-whisperer
```

### Option 4: Manual Flask Installation (macOS workaround)
```bash
# Download Flask and dependencies manually
curl -O https://files.pythonhosted.org/packages/source/F/Flask/Flask-3.0.0.tar.gz
tar -xzf Flask-3.0.0.tar.gz
cd Flask-3.0.0
sudo python3 setup.py install

# Go back and run
cd /Users/chay/Documents/GitHub/KD
python3 app.py
```

---

## ✅ Once Flask is Installed

Just run:
```bash
cd /Users/chay/Documents/GitHub/KD
python3 app.py
```

Then open: **http://localhost:5000**

---

## 💡 Quick Test

Check if Flask is already installed:
```bash
python3 -c "import flask; print('Flask is installed!'); print('Version:', flask.__version__)"
```

If you see "Flask is installed!", you're good to go! Just run `python3 app.py`.

---

## 🆘 Still Having Issues?

The simplest solution:
1. Accept the Xcode license once:  `sudo xcodebuild -license`
2. Install Flask: `pip3 install Flask`
3. Run the app: `python3 app.py`

That's it! 🎉

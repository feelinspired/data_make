# 🔧 How to Install Git on Your Computer

Git is required to clone and download code from GitHub. Follow the instructions for your operating system below.

---

## 🪟 Windows

### **Method 1: Git for Windows (Recommended)**

1. **Download Git:**
   - Go to: https://git-scm.com/download/win
   - The download should start automatically
   - Or click "Click here to download" if it doesn't

2. **Run the Installer:**
   - Double-click the downloaded `.exe` file
   - Click "Next" through the installation wizard
   - **Recommended settings:**
     - ✅ Use default installation location
     - ✅ Select "Git from the command line and also from 3rd-party software"
     - ✅ Use the default text editor (or choose VS Code if you have it)
     - ✅ Let Git decide the default branch name
     - ✅ Use Git Credential Manager

3. **Complete Installation:**
   - Click "Install"
   - Click "Finish" when done

4. **Verify Installation:**
   - Open **Command Prompt** or **PowerShell**
   - Type: `git --version`
   - You should see something like: `git version 2.42.0`

### **Method 2: Using Chocolatey (Package Manager)**

If you have Chocolatey installed:
```powershell
choco install git -y
```

### **Method 3: Using Winget (Windows 10/11)**

```powershell
winget install --id Git.Git -e --source winget
```

---

## 🍎 macOS

### **Method 1: Using Homebrew (Recommended)**

1. **Install Homebrew (if not installed):**
   - Open **Terminal** (Command + Space, type "Terminal")
   - Run:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Git:**
   ```bash
   brew install git
   ```

3. **Verify Installation:**
   ```bash
   git --version
   ```

### **Method 2: Install Xcode Command Line Tools**

1. **Open Terminal**
2. **Run:**
   ```bash
   xcode-select --install
   ```
3. **Click "Install"** in the popup window
4. **Accept the license agreement**
5. **Wait for installation** (may take 10-15 minutes)
6. **Verify:**
   ```bash
   git --version
   ```

### **Method 3: Download Official Installer**

1. Go to: https://git-scm.com/download/mac
2. Download the latest installer
3. Open the `.dmg` file
4. Run the `.pkg` installer
5. Follow the installation wizard
6. Verify in Terminal: `git --version`

---

## 🐧 Linux

### **Ubuntu / Debian**

```bash
# Update package list
sudo apt update

# Install Git
sudo apt install git -y

# Verify installation
git --version
```

### **Fedora**

```bash
# Install Git
sudo dnf install git -y

# Verify installation
git --version
```

### **CentOS / RHEL**

```bash
# Install Git
sudo yum install git -y

# Verify installation
git --version
```

### **Arch Linux**

```bash
# Install Git
sudo pacman -S git

# Verify installation
git --version
```

### **openSUSE**

```bash
# Install Git
sudo zypper install git

# Verify installation
git --version
```

---

## ✅ Verify Git Installation

After installation, open your terminal/command prompt and run:

```bash
git --version
```

You should see output like:
```
git version 2.42.0
```

If you see a version number, **Git is installed successfully!** ✨

---

## 🔧 Initial Git Configuration (First Time Setup)

After installing Git, configure your name and email (used for commits):

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"

# Verify settings
git config --list
```

**Example:**
```bash
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
```

---

## 🎯 Quick Test - Clone a Repository

Test that Git works by cloning the Data Whisperer repository:

```bash
# Clone the repository
git clone https://github.com/feelinspired/data_make.git

# Navigate into the folder
cd data_make

# List files
ls
```

If this works, you're all set! 🎉

---

## 🆘 Troubleshooting

### **"git: command not found" (After Installation)**

**Solution:**
1. Close and reopen your terminal/command prompt
2. Restart your computer
3. Verify the installation path is in your PATH environment variable

---

### **Windows: "git is not recognized as an internal or external command"**

**Solution:**
1. Reinstall Git and make sure to select "Add to PATH" during installation
2. Or manually add Git to PATH:
   - Right-click "This PC" → Properties
   - Advanced system settings → Environment Variables
   - Edit "Path" under System Variables
   - Add: `C:\Program Files\Git\cmd`
   - Click OK and restart terminal

---

### **macOS: "xcode-select: command line tools are already installed"**

**Solution:**
You already have Git! Just verify:
```bash
git --version
```

---

### **Linux: "Unable to locate package git"**

**Solution:**
Update your package list first:
```bash
sudo apt update
sudo apt install git
```

---

### **Slow Download Speed**

**Solution:**
- Use a wired internet connection if possible
- Disable VPN temporarily
- Try downloading during off-peak hours

---

## 📚 Next Steps

After installing Git:

1. ✅ **Configure Git** (name and email)
2. ✅ **Clone the Data Whisperer repository:**
   ```bash
   git clone https://github.com/feelinspired/data_make.git
   ```
3. ✅ **Follow INSTALLATION.md** to set up and run the app

---

## 🔗 Additional Resources

- **Official Git Documentation:** https://git-scm.com/doc
- **Git Basics Tutorial:** https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
- **GitHub Guides:** https://guides.github.com/
- **Interactive Git Tutorial:** https://learngitbranching.js.org/

---

## 📝 Quick Reference

### **Windows**
```powershell
# Download from: https://git-scm.com/download/win
# Then verify:
git --version
```

### **macOS**
```bash
# Install via Homebrew:
brew install git

# Or via Xcode:
xcode-select --install

# Then verify:
git --version
```

### **Linux (Ubuntu/Debian)**
```bash
sudo apt update && sudo apt install git -y
git --version
```

---

## 💡 Tips

1. **Git GUI Clients:** If you prefer a visual interface:
   - **GitHub Desktop:** https://desktop.github.com/
   - **GitKraken:** https://www.gitkraken.com/
   - **Sourcetree:** https://www.sourcetreeapp.com/

2. **VS Code Integration:** Visual Studio Code has built-in Git support

3. **Learn Git:** Take 15 minutes to learn basic Git commands - it's worth it!

---

**After installing Git, head over to INSTALLATION.md to clone and run Data Whisperer!** 🚀

---

## ❓ Still Having Issues?

1. Check the official Git documentation: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
2. Search for your specific error message online
3. Open an issue on GitHub: https://github.com/feelinspired/data_make/issues
4. Make sure you're using the latest version of your operating system

---

**Once Git is installed, you're ready to clone repositories and start coding!** ✨

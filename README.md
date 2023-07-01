# AutoSys Toolkit 🚀

AutoSys is a modular Python toolkit designed for Linux systems that monitors hardware usage, performs automated cleanup, and provides system administration utilities. Built with both CLI and Flask-based interfaces.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![AutoSys](https://img.shields.io/badge/Project-AutoSys-orange)

---

## ✨ Features

- ✅ CPU, memory, and disk usage monitoring
- 🧹 Automatic temp file cleanup
- 🔒 Open port scanner using `ss`
- 📦 System update & package manager
- 🌐 Optional Flask API dashboard
- 📧 Email alert template for system admins
- 🐳 Docker-ready

---

## 🔧 Setup

```bash
git clone https://github.com/Toshi-hub834/autosys.git
cd autosys
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python autosys.py
```

---

## 🧪 Web Dashboard

```bash
cd webapp
python app.py
```
Visit: `http://localhost:5000`

---

## 🐳 Run with Docker

```bash
docker build -t autosys .
docker run --rm autosys
```

---

## 🧠 Credits

Created by George Skhirtladze

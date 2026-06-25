# 📂 SORO: Smart Folder Organizer

**SORO** (Smart Organizer) is a lightweight, cross-platform Python tool designed to automate the painful process of organizing chaotic directories. With just one click, SORO scans your chosen folder and neatly categorizes files based on their extensions, sizes, or creation dates—all within seconds.

---

## 🎯 Project Purpose
Having a cluttered `Downloads` or `Desktop` folder is a universal headache. SORO was built to solve this problem efficiently. To guarantee **100% data safety**, the tool never alters your original files. Instead, it creates a secure backup copy with the suffix `_organized` and performs all sorting operations there, ensuring no data is ever lost or accidentally deleted.

---

## ✨ Key Features

* **🛡️ Ultra-Safe Backup:** Automatically replicates the source directory into a `_organized` folder before touching any file.
* **⚙️ Triple-Mode Smart Filtering:**
    * **By Extension:** Separates files into standard categories (Documents, Images, Videos, Archives, etc.).
    * **By Size:** Dynamically isolates heavy files (default > 10MB) to keep your main workspace clean.
    * **By Timeline:** Archives files into an elegant chronological tree folder structure (`Year/Month`).
* **🖥️ User-Friendly UI:** Modern Graphical User Interface (GUI) that launches automatically in your browser.
* **🚀 Multiple Launch Options:** Run it via Python, Windows Batch files, or a standalone `.exe`.
* **🌍 Cross-Platform:** Fully optimized to run seamlessly on **Windows, macOS, and Linux**.
* **🪶 Zero Dependencies:** Built entirely using Python's standard libraries. No heavy third-party installations required!

---

## 🗂️ How the Output Looks
After running SORO, your messy folder turns into this clean, professional structure:

```text
📁 YourFolder_organized
│
├── 📁 Images/          # All images (.png, .jpg, etc.)
├── 📁 Documents/       # All PDFs, Word Docs, Excels
├── 📁 Heavy_Files/     # Isolated files larger than 10MB
└── 📁 Timeline_Archive/
    └── 📁 2026/

```

🚀 Getting Started & Execution Guide
Prerequisites
Python 3.x or higher installed.

🪟 Windows Users (Choose one method)
Method 1 (Easiest): Double-click the App.exe file.

Method 2: Double-click the run.bat script file.

Method 3 (Developer Mode): Open the project folder in VS Code, open main.py, and hit Run.

🍏 🐧 macOS & Linux Users
Open the project folder in VS Code (or your favorite IDE).

Open the main.py file and click Run.

🕹️ How to Use (Step-by-Step)
💡 Tip for Testing: A built-in folder named Test is provided in the repository. We highly recommend testing the application using Filter 1 or Filter 3 on this folder first!

Launch the App: Once executed, the tool will automatically open a GUI panel in your default web browser.

Select Folder: Choose the target directory that you want to optimize.

Choose Filter: Enter the number corresponding to your preferred sorting rule:

Type 1 ➔ Filter and categorize by File Extension.

Type 2 ➔ Isolate Heavy Files (> 10MB).

Type 3 ➔ Archive chronologically by Year and Month.

🛠️ Built With
Python 3 - The core programming language.

Built-in Modules used: os, shutil, datetime, tkinter .
        ├── 📁 01-January/
        └── 📁 06-June/

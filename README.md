# Text-to-Speech from Word Document

This script reads text from a `.docx` file and converts it to speech using Microsoft Edge TTS.

## Requirements

```bash
pip install -r requirements.txt

Usage

Place your .docx file in the folder and name it input.docx.

Run the script:

bash
Copy
Edit
python ttmp3.py
The output will be saved as output.mp3.

yaml
Copy
Edit

---

#### Create a `requirements.txt` file

Paste the following into a file named `requirements.txt`:

python-docx
edge-tts

yaml
Copy
Edit

---

#### Create a `.gitignore` file

Paste the following into a file named `.gitignore`:

pycache/
*.mp3
*.docx

yaml
Copy
Edit

---

### ✅ Step 3: Initialize Git

1. In **Command Prompt** or **VS Code Terminal**, navigate to the folder:

```bash
cd path\to\tts-from-docx
Initialize Git:

bash
Copy
Edit
git init
Stage your files:

bash
Copy
Edit
git add .
Commit:

bash
Copy
Edit
git commit -m "Initial commit: DOCX to TTS converter"

# Text-to-Speech from Word Document

This Python script reads text from a `.docx` file and converts it into speech using Microsoft Edge TTS, saving the result as an `.mp3` file.

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your `.docx` file in the folder and name it `input.docx`.
2. Run the script:

```bash
python ttmp3.py
```

The output will be saved as `output.mp3` in the same folder.

## Notes

- You can change the voice used by editing the `voice` parameter in the script (default is `en-US-JennyNeural`).

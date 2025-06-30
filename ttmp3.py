import asyncio
import edge_tts
from docx import Document

def read_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

async def convert_text_to_speech(text, output_path, voice="en-US-JennyNeural"):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)
    print(f"Saved as {output_path}")

if __name__ == "__main__":
    input_file = "input.docx"
    output_file = "output.mp3"

    text = read_docx(input_file)
    if text.strip():
        asyncio.run(convert_text_to_speech(text, output_file))
    else:
        print("Document is empty.")

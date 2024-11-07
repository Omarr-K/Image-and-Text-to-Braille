from flask import Flask, render_template, request, redirect, url_for
import os
import pytesseract
from PIL import Image
from utils.ocr import extract_text_from_image
from utils.braille_converter import convert_text_to_braille
from utils.language_detection import detect_language

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Folder to temporarily store uploaded images

# Set up Tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata/'

# Ensure the uploads folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutp.html')

@app.route('/process_image_or_text', methods=['POST'])
def process_image_or_text():
    text_input = request.form.get('text')
    image_file = request.files.get('image')

    if image_file and image_file.filename != '':
        # Process the uploaded image
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(image_path)
        # Extract and detect language of the text
        extracted_text = extract_text_from_image(image_path)
        detected_language = detect_language(extracted_text)  # Detect the language
        # Clean up the image file after processing
        os.remove(image_path)
        # Pass `detected_language` to the template for conditional RTL rendering
        return render_template('text_review.html', extracted_text=extracted_text, detected_language=detected_language)
    else:
        # Handle text input directly
        if text_input:
            # Detect language from text input and Convert the input text to Braille based on detected language
            detected_language = detect_language(text_input)
            braille_text = convert_text_to_braille(text_input, detected_language)
            return render_template('result.html', braille=braille_text)
        else:
            # If no input is given, redirect or render an error message
            return render_template('index.html', error="Please enter text to convert.")

@app.route('/convert_to_braille', methods=['POST'])
def convert_to_braille():
    original_text = request.form.get('text')
    # Check if input is empty or just whitespace
    if not original_text.strip():
        return render_template('text_review.html', extracted_text='', error="Text cannot be empty. Please review and enter text before converting.")
    try:
        language = detect_language(original_text)
        braille_text = convert_text_to_braille(original_text, language)
        return render_template('result.html', braille=braille_text)
    except LangDetectException:
        # Handle the case where langdetect fails due to lack of text features
        return render_template('text_review.html', extracted_text=original_text, error="Language detection failed. Please provide more text.")


if __name__ == '__main__':
    app.run(debug=True)

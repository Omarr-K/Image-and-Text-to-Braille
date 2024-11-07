from flask import Flask, render_template, request, redirect, url_for
import os
import pytesseract
from PIL import Image
from utils.ocr import extract_text_from_image
from utils.braille_converter import convert_text_to_braille
from utils.language_detection import detect_language
from langdetect.lang_detect_exception import LangDetectException

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Folder to temporarily store uploaded images

# Set up Tesseract configuration
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Ensure the correct Tesseract path
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/5/tessdata/'  # Location of trained data

# Ensure the uploads folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Route: Home page
@app.route('/')
def index():
    return render_template('index.html')

# Route: About page
@app.route('/about')
def about():
    return render_template('aboutp.html')

# Route: Process uploaded image or entered text
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
        if not extracted_text.strip():
            os.remove(image_path)
            return render_template('text_review.html', error="No readable text detected in the image. Please try again with a clearer image.")

        try:
            detected_language = detect_language(extracted_text)  # Detect the language
        except LangDetectException:
            os.remove(image_path)
            return render_template('text_review.html', extracted_text=extracted_text, error="Language detection failed. Please provide more text.")

        os.remove(image_path)
        return render_template('text_review.html', extracted_text=extracted_text, detected_language=detected_language)

    elif text_input and text_input.strip():
        # Handle text input directly
        try:
            detected_language = detect_language(text_input)
            braille_text = convert_text_to_braille(text_input, detected_language)
            return render_template('result.html', braille=braille_text)
        except LangDetectException:
            return render_template('index.html', error="Language detection failed. Please provide more text.")
    else:
        # If no input is given
        return render_template('index.html', error="Please enter text or upload an image to convert.")

# Route: Convert entered text to Braille
@app.route('/convert_to_braille', methods=['POST'])
def convert_to_braille():
    original_text = request.form.get('text')

    if not original_text.strip():
        return render_template('text_review.html', extracted_text='', error="Text cannot be empty. Please review and enter text before converting.")
    
    try:
        language = detect_language(original_text)
        braille_text = convert_text_to_braille(original_text, language)
        return render_template('result.html', braille=braille_text)
    except LangDetectException:
        return render_template('text_review.html', extracted_text=original_text, error="Language detection failed. Please provide more text.")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

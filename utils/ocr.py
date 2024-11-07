import pytesseract
from PIL import Image
import os
from utils.language_detection import detect_language

# Set Tesseract path and tessdata directory
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
os.environ['TESSDATA_PREFIX'] = '/opt/homebrew/Cellar/tesseract/5.4.1_2/share/tessdata/'

def extract_text_from_image(image_path):
    try:
        # Initial OCR pass with all languages to detect the dominant language
        with Image.open(image_path) as img:
            initial_text = pytesseract.image_to_string(img, lang='eng+ita+ara')
        
        # Detect the dominant language using langdetect
        detected_language = detect_language(initial_text)
        
        # Map the detected language to the corresponding Tesseract language code
        lang_code = {
            'en': 'eng',
            'ita': 'ita',
            'ar': 'ara'
        }.get(detected_language, 'eng')  # Default to English if undetected

        # Re-run OCR using only the detected language for more accurate results
        with Image.open(image_path) as img:
            refined_text = pytesseract.image_to_string(img, lang=lang_code)
        
        return refined_text  # Return the refined text in the detected language
    except Exception as e:
        print(f"Error in OCR processing: {e}")
        return ""

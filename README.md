# Braille Converter - Omar's Image/Text to Braille Conversion Tool

---

## Overview

The Braille Converter is a powerful and efficient web application designed to convert text and images into Braille. This tool supports multiple languages, including English, Italian, and Arabic, ensuring accessibility for a wide range of users. It leverages Flask as the backend framework, Tesseract OCR for text extraction from images, and custom mappings for converting text into Braille.

---

## Project Motivation

I developed this program after seeing first-hand how slow and manual the process of translating textbooks into braille could be. Translating braille by hand takes too long, and I wanted to create a faster solution so visually impaired students could access their learning materials in a timely manner. My program automates much of the braille translation process, supporting Arabic, Italian, and English to ensure that more students in diverse language communities can benefit. By speeding up the production of braille resources, this tool helps visually impaired students keep pace with their peers, breaking down barriers to education and providing a more inclusive learning experience across multiple languages.


---

## Project Description

The Braille Converter offers the following features:

1. **Multi-Language Support**  
   - Converts text into Braille for English, Italian, and Arabic.
   - Each language has unique character mappings for accurate Braille representation.

2. **Image-to-Braille Conversion**  
   - Upload images containing text.
   - Uses Tesseract OCR to extract text from images for conversion.

3. **Text-to-Braille Conversion**  
   - Directly input text for instant Braille conversion.
   - Supports uppercase, lowercase, and special characters.

4. **Text Review and Editing**  
   - Users can review and modify the extracted text from images before conversion.

5. **Robust Error Handling**  
   - Alerts users when no text is provided or when an error occurs during language detection or OCR processing.

6. **Responsive Design**  
   - Built with HTML, CSS, and JavaScript for a clean and user-friendly interface.

---
## How It Works

1. **Flask Routing**  
   Flask manages the following HTTP routes:
   
   - **Home Route (`/`)**: Displays the main page for text or image input.
   - **About Route (`/about`)**: Provides information about the app and contact details.
   - **Processing Route (`/process_image_or_text`)**: Handles form submissions, processes uploaded images, and detects the language of extracted text.
   - **Conversion Route (`/convert_to_braille`)**: Converts text into Braille based on the detected language.

2. **Input Handling**  
   The application accepts two types of inputs:
   
   - **Text Input**: Users can directly enter text into a form.
   - **Image Input**: Users upload an image, and the app extracts text using an integrated OCR.

3. **Text Processing Pipeline**  
   - **Language Detection**: The `langdetect` library automatically detects the language (English, Italian, or Arabic).
   - **Braille Conversion**: Depending on the detected language, the app routes the text to the appropriate Braille conversion function:
     - Arabic: Uses Unicode-based mappings.
     - Italian: Handles accented characters.
     - English: Maps standard characters and punctuation.

4. **Frontend Interaction**  
   - **Form Submission**: Users submit text or images through a form, which is processed by the backend.
   - **Review and Edit**: Extracted text from images is displayed for review and can be edited before conversion.
   - **Braille Output**: The converted Braille is displayed, with options to copy the text or start a new conversion.

---

## Tech Stack

### Frontend

- **HTML5**: For structuring the application layout.
- **CSS3**: For styling and responsive design.
- **JavaScript**: For interactivity, form validation, and dynamic updates.

### Backend

- **Flask**: Python-based web framework for handling requests and rendering templates.

### Libraries and Tools

- **Tesseract OCR**: Extracts text from uploaded images.
- **Pillow**: Image processing and validation.
- **Langdetect**: Detects the language for accurate Braille conversion.

---

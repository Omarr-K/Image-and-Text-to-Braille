import unicodedata

capital_indicator = '⠠'

# Define Unicode-based Braille mappings for Arabic characters and character-based mappings for English and Italian
braille_mappings = {
    #Due to the program not being able to convert arabic to braille through a basic dictionary, it is now matched by Unicode
    'ar': {
        0x0627: '⠁',  # ا
        0x0628: '⠃',  # ب
        0x062A: '⠞',  # ت
        0x062B: '⠮',  # ث
        0x062C: '⠚',  # ج
        0x062D: '⠱',  # ح
        0x062E: '⠭',  # خ
        0x062F: '⠙',  # د
        0x0630: '⠹',  # ذ
        0x0631: '⠗',  # ر
        0x0632: '⠵',  # ز
        0x0633: '⠎',  # س
        0x0634: '⠱',  # ش
        0x0635: '⠨',  # ص
        0x0636: '⠹',  # ض
        0x0637: '⠞',  # ط
        0x0638: '⠮',  # ظ
        0x0639: '⠑',  # ع
        0x063A: '⠣',  # غ
        0x0641: '⠋',  # ف
        0x0642: '⠟',  # ق
        0x0643: '⠅',  # ك
        0x0644: '⠇',  # ل
        0x0645: '⠍',  # م
        0x0646: '⠝',  # ن
        0x0647: '⠓',  # ه
        0x0648: '⠺',  # و
        0x064A: '⠽',  # ي
        0x0621: '⠄',  # ء
        0x0626: '⠄',  # ئ
        0x0624: '⠲',  # ؤ
        0x0649: '⠊',  # ى
        0x0629: '⠞',  # ة
        0x0623: '⠁',  # أ
        0x0625: '⠊',  # إ
        0x0622: '⠁',  # آ
        0x061F: '⠦',  # ؟
        0x060C: '⠂',  # ،
        0x061B: '⠆',  # ؛
        0x0660: '⠼⠚',  # ٠
        0x0661: '⠼⠁',  # ١
        0x0662: '⠼⠃',  # ٢
        0x0663: '⠼⠉',  # ٣
        0x0664: '⠼⠙',  # ٤
        0x0665: '⠼⠑',  # ٥
        0x0666: '⠼⠋',  # ٦
        0x0667: '⠼⠛',  # ٧
        0x0668: '⠼⠓',  # ٨
        0x0669: '⠼⠊',  # ٩
        0x0020: ' ',     # Space
        0x0021: '⠮',    # Exclamation mark !
        0x002C: '⠂',    # Comma ,
        0x002E: '⠲',    # Period .
        0x003A: '⠒',    # Colon :
        0x003B: '⠆',    # Semicolon ;
        0x003F: '⠦',    # Question mark ?
        0x0028: '⠷',    # Left parenthesis (
        0x0029: '⠾',    # Right parenthesis )
        0x002D: '⠤',    # Hyphen -
        0x0022: '⠦',    # Quotation mark "
        0x002F: '⠌',    # Slash /
        0x0024: '⠈⠎',  # Dollar sign $
        0x0060: '⠹',
    },
    'en': {
        'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
        'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
        'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
        'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
        'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵',
        '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑',
        '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', '0': '⠼⠚',
        ' ': ' ', '!': '⠮', ',': '⠂', '.': '⠲', ':': '⠒', "'": '⠄',
        '"': '⠦', '/': '⠌', '?': '⠦', '-': '⠤', '(': '⠷', ')': '⠾', ';': '⠆', '$': '⠈⠎'
    },
    #Due to the program not being able to convert special italian letters intoto braille through a basic dictionary, it is now matched by Unicode
    'ita': {
        'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
        'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
        'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
        'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
        'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵',
        '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑',
        '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', '0': '⠼⠚',
        0x00E0: '⠷',  # à
        0x00E8: '⠮',  # è
        0x00EC: '⠤',  # ì
        0x00F2: '⠬',  # ò
        0x00F9: '⠜',  # ù
        ' ': ' ', '!': '⠮', ',': '⠂', '.': '⠲', ':': '⠒', "'": '⠄',
        '"': '⠦', '/': '⠌', '?': '⠦', '-': '⠤', '(': '⠷', ')': '⠾', ';': '⠆', '$': '⠈⠎'
    }
}

# Convert Arabic text to Braille using Unicode code points.
def convert_arabic_text_to_braille(text):
    braille_text = ''
    text = unicodedata.normalize('NFC', text)

    for char in text:
        if char == '\n':
            braille_text += '\n'
        else:
            unicode_val = ord(char)
            braille_char = braille_mappings['ar'].get(unicode_val, ' ')
            braille_text += braille_char      
    return braille_text

# Convert Italian text to Braille using Unicode code points.
def convert_italian_text_to_braille(text):
    braille_text = ''
    text = unicodedata.normalize('NFC', text)  # Normalize the text to handle accented characters

    for char in text:
        if char == '\n':
            braille_text += '\n'
        elif char.isupper():
            # Add capital indicator for uppercase letters
            braille_text += capital_indicator + braille_mappings['ita'].get(char.lower(), ' ')
        else:
            unicode_val = ord(char)
            braille_text += braille_mappings['ita'].get(unicode_val, ' ')
    return braille_text

# Convert English text to Braille
def convert_english_text_to_braille(text):
    braille_text = ''
    mapping = braille_mappings['en']  # Fixed to English

    for char in text:
        if char == '\n':
            braille_text += '\n'
        elif char.isupper():
            braille_text += capital_indicator + mapping.get(char.lower(), ' ')
        else:
            braille_text += mapping.get(char, ' ')
    return braille_text

# Determine which function to call based on the language.
def convert_text_to_braille(text, language):
    if language == 'ar':
        return convert_arabic_text_to_braille(text)
    elif language == 'ita':
        return convert_italian_text_to_braille(text)
    else:
        return convert_english_text_to_braille(text)
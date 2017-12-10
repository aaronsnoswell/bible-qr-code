"""Generate a QR code that opens the YouVersion Bible app on Android to any desired chapter and verse
"""

import pyqrcode
import argparse

"""
Returns an intent URI to load a book, chapter and verse from the Bible
@param book_name - Plaintext name of the desired bible book, e.g. 'Genesis' (required)
@param chapter - Integer chapter number (required)
@param verse_start - Integer verse number to start at (optional)
@param verse_end - Integer verse number to end at (optional)
@param version - Three leter version code, e.g. "KJV"
"""
def get_intent_url(book_name, chapter, verse_start=None, verse_end=None, version=None):

    # Sanity check - can't have verse end without verse start
    if verse_end is not None:
        if verse_start is None:
            verse_start = verse_end

    # URL template for www.bible.com
    url_template = "https://www.bible.com/en-GB/bible/{language_code}/{book_code}{chapter}{verse_start}{verse_end}{version}"

    # Book name mappings for www.bible.com
    book_mappings = {
        "Genesis": "GEN",
        "Exodus": "EXO",
        "Leviticus": "LEV",
        "Numbers": "NUM",
        "Deuteronomy": "DEU",
        "Joshua": "JOS",
        "Judges": "JDG",
        "Ruth": "RUT",
        "1 Samuel": "1SA",
        "2 Samuel": "2SA",
        "1 Kings": "1KI",
        "2 Kings": "2KI",
        "1 Chronicles": "1CH",
        "2 Chronicles": "2CH",
        "Ezra": "EZR",
        "Nehemiah": "NEH",
        "Esther": "EST",
        "Job": "JOB",
        "Psalms": "PSA",
        "Proverbs": "PRO",
        "Ecclesiastes": "ECC",
        "Song of Solomon": "SNG",
        "Isaiah": "ISA",
        "Jeremiah": "JER",
        "Lamentations": "LAM",
        "Ezekiel": "EZK",
        "Daniel": "DAN",
        "Hosea": "HOS",
        "Joel": "JOL",
        "Amos": "AMO",
        "Obadiah": "OBA",
        "Jonah": "JON",
        "Micah": "MIC",
        "Nahum": "NAM",
        "Habakkuk": "HAB",
        "Zephaniah": "ZEP",
        "Haggai": "HAG",
        "Zechariah": "ZEC",
        "Malachi": "MAL",
        "Matthew": "MAT",
        "Mark": "MRK",
        "Luke": "LUK",
        "John": "JHN",
        "Acts": "ACT",
        "Romans": "ROM",
        "1 Corinthians": "1CO",
        "2 Corinthians": "2CO",
        "Galatians": "GAL",
        "Ephesians": "EPH",
        "Philippians": "PHP",
        "Colossians": "COL",
        "1 Thessalonians": "1TH",
        "2 Thessalonians": "2TH",
        "1 Timothy": "1TI",
        "2 Timothy": "2TI",
        "Titus": "TIT",
        "Philemon": "PHM",
        "Hebrews": "HEB",
        "James": "JAS",
        "1 Peter": "1PE",
        "2 Peter": "2PE",
        "1 John": "1JN",
        "2 John": "2JN",
        "3 John": "3JN",
        "Jude": "JUD",
        "Revelation": "REV"
    }

    # TODO ajs 10/Dec/2017 Add lookup code for other languages
    # Language '1' is English on www.bible.com
    language_code = "1"

    # Look up the www.bible.com book code
    book_code = None
    if book_name in book_mappings:
        book_code = book_mappings[book_name]
    
    if book_code is None:
        raise ValueError("Unknown book name: '{0}'".format(book_name))

    url = url_template.format(
        language_code = language_code,
        book_code = book_code,
        chapter = "." + str(chapter),
        verse_start = "" if (verse_start == None) else ("." + str(verse_start)),
        verse_end = "" if (verse_end == None) else ("-" + str(verse_end)),
        version = "" if (version == None) else ("." + version)
    )

    return url


"""
Given a URI string and a filename, outputs a QR code that encodes the string
@param URI - String to encode in the QR barcode (required)
@param filename - Filename to save the QR code to (required)
@param scale - Integer scale to upsize the image (optional)
"""
def make_qr_code(URI, filename, scale=1):
    qr = pyqrcode.create(URI)
    qr.png(filename, scale=scale)


"""
Parse command line args and output help messages if needed
"""
def main():
    parser = argparse.ArgumentParser(description='Generates a QR code that opens a bible app to a specific location')
    parser.add_argument(
        '--output',
        '-o',
        dest='output',
        default='output.png',
        help='Output filename (with png extension)'
    )
    parser.add_argument(
        '--chapter',
        '-c',
        dest='chapter',
        default=1,
        help='Desired chapter'
    )
    parser.add_argument(
        '--start_verse',
        '-s',
        dest='start_verse',
        default=1,
        help='Starting verse'
    )
    parser.add_argument(
        '--end_verse',
        '-e',
        dest='end_verse',
        default=None,
        help='Ending verse'
    )
    parser.add_argument(
        '--version',
        '-v',
        dest='version',
        default="KJV",
        help='Three letter Bible version code (e.g. "KJV")'
    )
    parser.add_argument(
        '--zoom',
        '-z',
        dest='zoom',
        default=5,
        help='Scale factor to apply to the QR code'
    )
    parser.add_argument(
        'book',
        help='Desired book (e.g. "Genesis")'
    )

    args = parser.parse_args()

    intent_uri = get_intent_url(
        args.book,
        args.chapter,
        args.start_verse,
        args.end_verse,
        args.version
    )

    print("Generating QR code for intent URI:")
    print(intent_uri)
    make_qr_code(intent_uri, args.output, args.zoom)
    print("Saved {0}".format(args.output))


if __name__ == "__main__":
    main()


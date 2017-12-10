# bible-qr-code

Have you ever wanted to generate a QR code that opens a bible app to a specific spot?

This simple python script does just that - it uses a URI intent that the YouVersion
Bible app handles to launch the bible app to the desired locaiton.

## Installation

`pip install pyqrcode pypng argparse`

## Usage

`python bible-qr-code.py --output "test.png" --chapter 1 -start_verse 1 -end_verse 5 -version "ESV" "Genesis"`

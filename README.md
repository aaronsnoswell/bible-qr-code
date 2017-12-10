# bible-qr-code

Have you ever wanted to generate a QR code that opens a bible to a specific spot?

This simple python script does just that - it uses a [URI intent](https://developer.android.com/reference/android/content/Intent.html) that the
[YouVersion Bible app](https://www.youversion.com/) handles to launch the bible app to the desired location.

## Installation

`pip install pyqrcode pypng argparse`

## Usage

```
$> python bible-qr-code.py --output test.png --chapter 1 --start_verse 1 --end_verse 5 --version ESV Genesis
Generating QR code for intent URI:
https://www.bible.com/en-GB/bible/1/GEN.1.1-5.ESV
Saved test.png
```

![QR Code for above example](test.png)

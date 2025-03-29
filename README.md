# Regex Validator

A simple GUI tool to test regular expressions against input text, built with Python and Tkinter.

## Features

- Test regular expressions against any input text
- Instant feedback on matches
- Error handling for invalid regex patterns
- Clean, intuitive interface
- Supports multiline text input

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- re module (Python standard library)

## Usage

1. Run the script: `python regex_validator.py`
2. Enter your test text in the upper text box
3. Enter your regular expression in the lower input field
4. Click "Test Regex" button
5. View results in the output area:
   - Shows the first match found
   - Displays "No match found" if pattern doesn't match
   - Shows error messages for invalid regex patterns

## Examples

Try these regex patterns:

- Email addresses: `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`
- URLs: `https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+`
- Phone numbers: `(\+\d{1,3}\s?)?(\(\d{1,4}\)|\d{1,4})[\s.-]?\d{1,4}[\s.-]?\d{1,9}`

## Customization

You can modify:
- Default window size by changing `root.config(width=400, height=220)`
- Font by changing the `overall_font` variable
- Default placeholder text in the input fields
- Colors by adding configuration options to widgets

## Known Limitations

- Only shows the first match (not all matches)
- Basic interface without advanced regex options
- No regex explanation or breakdown

## License

This project is open-source and free to use.

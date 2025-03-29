# Regex Validator / Regex-Prüftool

## Description / Beschreibung  
`Python GUI for testing regular expressions / Python-GUI zum Testen von Regular Expressions`

## Features / Funktionen  
```text
- Test patterns in real-time / Muster in Echtzeit testen
- Highlight all matches / Alle Treffer markieren
- Validate regex syntax / Regex-Syntax prüfen
- Multi-line support / Mehrzeilen-Unterstützung
- Error diagnostics / Fehlerdiagnose
```

## Installation  
```bash
# Clone and run / Klonen und starten:
git clone https://github.com/Stephen-Scharmweber/Regex-Validator.git
cd regex-validator
python regex_validator.py
```

## Usage / Verwendung  
```text
1. Enter sample text / Beispieltext eingeben:
   "Test 123 - Beispiel 456"

2. Input regex pattern / Regex-Muster eingeben:
   "\d+"

3. Click "Test" / Auf "Testen" klicken

4. View results / Ergebnisse anzeigen:
   - "123", "456" (matches / Treffer)
```

## Examples / Beispiele  
```regex
# Email validation / E-Mail-Validierung:
\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b

# URL matching / URL-Erkennung:
https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+
```

## License / Lizenz  
`MIT License - Open source / Freie Nutzung`

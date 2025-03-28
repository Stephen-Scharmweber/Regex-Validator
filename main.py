from tkinter import *
import re

overall_font = "Righteous"
def test_regex():
    input_text = input_text_widget.get("1.0", "end-1c")  # Get text from the input Text widget
    regex_pattern = regex_entry.get()

    try:
        match = re.search(regex_pattern, input_text)
        if match:
            result_text.set(f"Regex Match gefunden: {match.group()}")
        else:
            result_text.set("Kein Match gefunden.")
    except re.error as e:
        result_text.set(f"Fehler beim Ausführen des Regex: {str(e)}")

# Erstelle das Hauptfenster
root = Tk()
root.title("Regex Validator")
root.config(width=400, height=220)


# Eingabetext
input_text_widget = Text(root, wrap="word", height=5, width=40, font=("Righteous", 12))
input_text_widget.insert("1.0", "Please Enter Text for Regex Test")
input_text_widget.place(x=10,y=10)

# Regex-Eingabe
regex_entry = Entry(root, width=40)
regex_entry.insert(0, "Enter Regex")
regex_entry.config(font=("Righteous", 12))
regex_entry.place(x=10,y=110)

# Test-Button
test_button = Button(root, text="Test Regex", command=test_regex, font=("Righteous", 12), width=10)
test_button.place(x=10,y=140)

# Ergebnis-Anzeige
result_text = StringVar()
result_label = Label(root, textvariable=result_text, wraplength=300, font=("Righteous", 12))
result_label.place(x=120,y=140)

# Starte die Tkinter-Schleife
root.mainloop()
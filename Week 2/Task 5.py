events = {
    "Brauchtum Karneval für alle!": "19.09.2026",
    "Keycabs – Kunst unter den Fingerspitzen": "19.09.2026",
    "Connected – Digitale Kultur im Ruhrgebiet": "19.09.2026",
    "Dinos, Ammos & Co": "19.09.2026",
    "Stille im Zero Raum": "19.09.2026"
}

museum_night_date = "19.09.2026"

print("Events during the Night of Museums in Dortmund:")

for event, date in events.items():
    if date == museum_night_date:
        print(event)

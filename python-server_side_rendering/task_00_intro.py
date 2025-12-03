import os

def generate_invitations(template, attendees):
    #
    # 1. TYPE CHECKS
    #
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Liste içindeki her eleman dictionary mi?
    for item in attendees:
        if not isinstance(item, dict):
            print("Error: All attendees must be dictionaries.")
            return

    #
    # 2. EMPTY CHECKS
    #
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    #
    # 3. PROCESS EACH ATTENDEE
    #
    for index, attendee in enumerate(attendees, start=1):

        # Her placeholder için "N/A" fallback
        name = attendee.get("name") or "N/A"
        title = attendee.get("event_title") or "N/A"
        date = attendee.get("event_date") or "N/A"
        location = attendee.get("event_location") or "N/A"

        # Template’i doldur
        filled = (
            template
            .replace("{name}", name)
            .replace("{event_title}", title)
            .replace("{event_date}", date)
            .replace("{event_location}", location)
        )

        # Dosya adı
        filename = f"output_{index}.txt"

        # Dosyaya yazma
        try:
            with open(filename, "w") as f:
                f.write(filled)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue  # diğer dosyalara devam

    print("Invitation files generated successfully.")

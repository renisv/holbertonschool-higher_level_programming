def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print(f"Error: attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Check if template is empty
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders, using "N/A" if key missing or value is None
        personalized_content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            personalized_content = personalized_content.replace(f"{{{key}}}", str(value))

        # Write to output file
        file_name = f"output_{index}.txt"
        try:
            with open(file_name, "w") as f:
                f.write(personalized_content)
        except Exception as e:
            print(f"Error writing file {file_name}: {e}")

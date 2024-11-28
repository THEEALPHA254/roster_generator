import random
import pandas as pd

# List of Producers
producers = [
    "Dennis Karuti", "Vickram Kimwere", "Kevin Kagema", 
    "Grace Muriithi", "Eliud Muiruri", "Patrick Collins", 
    "Austin Kagema", "Edward Kibugi"
]

# List of available roles
roles = {
    "Videography": ["Keel Kelvin", "David Kariuki", "Njoroge Waithaka", "David Gachuru", 
                    "Titus Maweu", "Eliud Muiruri", "Daniel Murigi", "Pacifique Birori", 
                    "Anthony Muriithi", "Dennis Mwangi", "Patrick Collins", "Austin Kagema"],

    "Projection": ["Grace Niyigena", "Grace Muriithi", "Patrick Collins", "Edward Kibugi", 
                   "Boniface Theuri", "Kevin Kagema", "Wangari Njuguna", "Sylvia Mumbi", 
                   "Cynthia Wanjiru", "Eliud Muiruri", "Dennis Karuti", "Austin Kagema"],

    "Streaming": ["Austin Kagema", "Timothy Karani", "Vickram Kimwere", "Edward Kibugi", 
                  "Dennis Karuti", "Grace Niyigena", "Sharlet Maithya"],

    "Photography": ["Austin Kagema", "Pacifique Birori", "David Gachuru", "Patrick Collins", 
                    "David Kariuki", "Vesh Kithuka", "Maureen Gachuru", "Mercy Makena", "Sharlet Maithya"],

    "Timer": ["Keel Kelvin", "David Kariuki", "Njoroge Waithaka", "David Gachuru", 
                "Titus Maweu", "Eliud Muiruri", "Daniel Murigi", "Pacifique Birori", 
                "Anthony Muriithi", "Dennis Mwangi", "Patrick Collins", "Austin Kagema",
                "Grace Niyigena", "Grace Muriithi", "Edward Kibugi", "Boniface Theuri", 
                "Kevin Kagema", "Wangari Njuguna", "Sylvia Mumbi", "Cynthia Wanjiru", 
                "Dennis Karuti", "Vickram Kimwere", "Maureen Gachuru", "Mercy Makena", 
                "Victor Rueben", "Mirriam Githinji", "Joy Wanjiku", "Faith Maina", "Hilda Nyakinyua", "Sharlet Maithya"],

    "Media Desk": ["Keel Kelvin", "David Kariuki", "Njoroge Waithaka", "David Gachuru", 
                "Titus Maweu", "Eliud Muiruri", "Daniel Murigi", "Pacifique Birori", 
                "Anthony Muriithi", "Dennis Mwangi", "Patrick Collins", "Austin Kagema",
                "Grace Niyigena", "Grace Muriithi", "Edward Kibugi", "Boniface Theuri", 
                "Kevin Kagema", "Wangari Njuguna", "Sylvia Mumbi", "Cynthia Wanjiru", 
                "Dennis Karuti", "Vickram Kimwere", "Maureen Gachuru", "Mercy Makena", 
                "Victor Rueben", "Mirriam Githinji", "Joy Wanjiku", "Faith Maina", "Hilda Nyakinyua", "Sharlet Maithya"],

    "Hospitality": ["Keel Kelvin", "David Kariuki", "Njoroge Waithaka", "David Gachuru", 
    "Titus Maweu", "Eliud Muiruri", "Daniel Murigi", "Pacifique Birori", 
    "Anthony Muriithi", "Dennis Mwangi", "Patrick Collins", "Austin Kagema",
    "Grace Niyigena", "Grace Muriithi", "Edward Kibugi", "Boniface Theuri", 
    "Kevin Kagema", "Wangari Njuguna", "Sylvia Mumbi", "Cynthia Wanjiru", 
    "Dennis Karuti", "Vickram Kimwere", "Maureen Gachuru", "Mercy Makena", 
    "Victor Rueben", "Mirriam Githinji", "Joy Wanjiku", "Faith Maina", "Hilda Nyakinyua", "Sharlet Maithya"],
    
    "Social Media": ["Victor Rueben"],
}

# Function to generate the roster for a single Sunday
def generate_roster(available_people, num_sundays, excluded_members):
    producer_index = 0
    all_sundays = []

    # Exclude missing members from the entire pool of available people
    available_people = [person for person in available_people if person not in excluded_members]

    # Exclude missing members from the roles as well
    for role in roles:
        roles[role] = [person for person in roles[role] if person not in excluded_members]

    for _ in range(num_sundays):
        sunday_roster = []
        random.shuffle(available_people)  # Shuffle the available people to ensure randomness

        # Select producer from available producers who are not excluded
        available_producers = [producer for producer in producers if producer not in excluded_members]
        if not available_producers:
            print("Error: No available producers!")
            return

        producer = available_producers[producer_index]
        producer_index = (producer_index + 1) % len(available_producers)  # Cycle through producers
        sunday_roster.append({"Name": producer, "Area of service": "Producer"})

        # Keep track of assigned people to avoid double assignment
        assigned_people = {producer}

        # Assign assistant producer (can serve in other roles as well)
        assistant = random.choice([member for member in available_people if member != producer and member not in assigned_people])
        sunday_roster.append({"Name": assistant, "Area of service": "Assistant Producer"})
        assigned_people.add(assistant)

        # Assign one Social Media
        social_media_member = random.choice([member for member in roles["Social Media"] if member not in assigned_people])
        sunday_roster.append({"Name": social_media_member, "Area of service": "Social Media"})
        assigned_people.add(social_media_member)

        # Assign two Hospitality roles
        hospitality_members = random.sample([member for member in roles["Hospitality"] if member not in assigned_people], 2)
        for member in hospitality_members:
            sunday_roster.append({"Name": member, "Area of service": "Hospitality"})
            assigned_people.add(member)

        # Now assign roles for each service (3 services)
        for service_num in range(1, 4):
            # Assign roles for each service
            service_roles = {
                "Videography": random.sample([member for member in roles["Videography"] if member not in assigned_people], 2),
                "Projection": random.sample([member for member in roles["Projection"] if member not in assigned_people], 2),
                "Streaming": random.sample([member for member in roles["Streaming"] if member not in assigned_people], 1),
                "Photography": random.sample([member for member in roles["Photography"] if member not in assigned_people], 1),
                "Timer": random.sample([member for member in roles["Timer"] if member not in assigned_people], 1),
                "Media Desk": random.sample([member for member in roles["Media Desk"] if member not in assigned_people], 1),
            }

            # Add the roles for the current service to the roster
            for role, members in service_roles.items():
                for member in members:
                    sunday_roster.append({"Name": member, "Area of service": f"{role} (Service {service_num})"})
                    assigned_people.add(member)

        all_sundays.append(sunday_roster)

    return all_sundays

# Function to display the rosters in a tabular format
def display_roster(all_sundays):
    for idx, sunday_roster in enumerate(all_sundays, 1):
        print(f"\nSunday {idx} Roster")
        df = pd.DataFrame(sunday_roster)
        print(df.to_string(index=False))

# Main program
def main():
    # Ask for input: number of Sundays and availability of people
    num_sundays = int(input("Enter the number of Sundays: "))
    
    # Ask for missing members
    missing_members_input = input("Enter the names of missing members (comma-separated): ")
    missing_members = [name.strip() for name in missing_members_input.split(",") if name.strip()]

    # Generate roster
    available_people = producers + [person for role_list in roles.values() for person in role_list]
    all_sundays = generate_roster(available_people, num_sundays, missing_members)

    # Display the roster
    display_roster(all_sundays)

    # Print missing members list
    print("\nMissing members for this month:", missing_members)

if __name__ == "__main__":
    main()

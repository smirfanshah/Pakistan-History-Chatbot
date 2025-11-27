import wikipediaapi
import json
import time

def fetch_wiki_page(title, wiki):
    for attempt in range(3):  # retry mechanism
        try:
            page = wiki.page(title)
            if page.exists():
                return page.text
            return None
        except Exception as e:
            print(f"[Retry {attempt+1}] Error fetching {title}: {e}")
            time.sleep(2)
    return None


def build_dataset(titles, output_file="pakistan_history_dataset.json"):
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent="PakistanHistoryRAG/1.0"
    )

    dataset = {}
    missing = []

    for idx, title in enumerate(titles):
        print(f"Fetching ({idx+1}/{len(titles)}): {title}")

        text = fetch_wiki_page(title, wiki)

        if text is None:
            print(f"Missing: {title}")
            missing.append(title)
        else:
            print(f"Fetched: {title} ({len(text)} chars)")
            dataset[title] = text

        time.sleep(1.5)  # rate limit control

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print("\nDataset built successfully!")
    print(f"Saved to: {output_file}")
    print(f"Missing pages: {missing}")


if __name__ == "__main__":
    titles = [
        # Core History
        "History_of_Pakistan",
        "Pakistan_Movement",
        "Partition_of_India",
        "Dominion_of_Pakistan",
        "Independence_of_Pakistan",
        "British_Raj",
        "Pakistan_Studies",

        # Ancient & Early History
        "Indus_Valley_Civilisation",
        "Mehrgarh",
        "Gandhara",
        "Achaemenid_Empire",
        "Maurya_Empire",
        "Indo-Greek_Kingdom",
        "Kushan_Empire",
        "Delhi_Sultanate",
        "Mughal_Empire",

        # Political Eras
        "Muhammad_Ali_Jinnah",
        "Liaquat_Ali_Khan",
        "Iskander_Mirza",
        "Ayub_Khan",
        "Yahya_Khan",
        "Zulfikar_Ali_Bhutto",
        "Muhammad_Zia-ul-Haq",
        "Benazir_Bhutto",
        "Nawaz_Sharif",
        "Pervez_Musharraf",
        "Asif_Ali_Zardari",
        "Mamnoon_Hussain",
        "Arif_Alvi",
        "Imran_Khan",
        "Shehbaz_Sharif",

        # Wars & Conflicts
        "Indo-Pakistani_War_of_1947–1948",
        "Indo-Pakistani_War_of_1965",
        "Indo-Pakistani_War_of_1971",
        "Bangladesh_Liberation_War",
        "Kargil_War",
        "War_in_North-West_Pakistan",
        "Afghan_War",
        "Siachen_conflict",

        # Major Events
        "Fall_of_Dhaka",
        "Operation_Searchlight",
        "Operation_Blue_Star",
        "1998_Pakistani_nuclear_tests",
        "Lahore_Resolution",
        "Objectives_Resolution",
        "Judicial_Crisis_of_2007",
        "2014_Peshawar_school_massacre",
        "2005_Kashmir_earthquake",

        # Constitutions
        "Constitution_of_Pakistan",
        "Constitution_of_Pakistan_of_1956",
        "Constitution_of_Pakistan_of_1962",
        "Constitution_of_1973",
        "Eighteenth_Amendment_to_the_Constitution_of_Pakistan",

        # Geography & Provinces
        "Punjab,_Pakistan",
        "Sindh",
        "Balochistan,_Pakistan",
        "Khyber_Pakhtunkhwa",
        "Gilgit-Baltistan",
        "Azad_Kashmir",
        "FATA",
        "Islamabad",

        # Movements & Ideologies
        "Two-nation_theory",
        "Pakistan_National_Movement",
        "All-India_Muslim_League",
        "Khilafat_Movement",
        "Tehreek-e-Nifaz-e-Shariat-e-Mohammadi",
        "Pakistan_Tehreek-e-Insaf",
        "Pakistan_Peoples_Party",
        "Pakistan_Muslim_League_(N) ",
        "Pakistan_Muslim_League_(Q)",

        # Foreign Relations
        "Foreign_relations_of_Pakistan",
        "Pakistan–United_States_relations",
        "Pakistan–China_relations",
        "Pakistan–India_relations",
        "Pakistan–Afghanistan_relations",

        # Military & Nuclear
        "Pakistan_Armed_Forces",
        "Inter-Services_Intelligence",
        "Pakistan_Atomic_Program",
        "Abdul_Qadeer_Khan",
        "Kahuta_Research_Laboratories",
        "Pakistan_Navy",
        "Pakistan_Air_Force",

        # Social & Cultural
        "Demographics_of_Pakistan",
        "Languages_of_Pakistan",
        "Ethnic_groups_in_Pakistan",
        "Religion_in_Pakistan",

        # Elections & Governance
        "Elections_in_Pakistan",
        "Federal_government_of_Pakistan",
        "Prime_Minister_of_Pakistan",
        "President_of_Pakistan",
        "Judiciary_of_Pakistan",
        "National_Assembly_of_Pakistan",

        # Pakistan Economy History
        "Economy_of_Pakistan",
        "Agriculture_in_Pakistan",
        "Industry_of_Pakistan",
        "China–Pakistan_Economic_Corridor",
        "Gwadar_Port",

        # Terrorism and Security Events
        "War_on_Terror",
        "Insurgency_in_Khyber_Pakhtunkhwa",
        "Tehrik-i-Taliban_Pakistan",
        "Operation_Zarb-e-Azb",
        "Operation_Radd-ul-Fasaad"
    ]


build_dataset(titles)


# Size logs
import os

file_path = "pakistan_history_dataset.json"
size_bytes = os.path.getsize(file_path)

print(f"Size: {size_bytes} bytes")
print(f"Size: {size_bytes / 1024:.2f} KB")
print(f"Size: {size_bytes / (1024**2):.2f} MB")

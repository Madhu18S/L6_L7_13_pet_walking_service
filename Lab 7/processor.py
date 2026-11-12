import math


def parse_walk_schedule(schedule_spec):
    if not isinstance(schedule_spec, str):
        return "Error: Schedule specification must be a non-empty string (e.g., '2-30-YES')."

    parts = [part.strip() for part in schedule_spec.strip().split('-')]
    if len(parts) != 3 or any(not p for p in parts):
        return "Error: Invalid schedule format. Expected '<pets>-<minutes>-<YES|NO>'."

    pets_str, mins_str, weekend_str = parts

    try:
        pets = int(pets_str)
        mins = int(mins_str)
    except ValueError:
        return "Error: Number of pets and minutes must be valid integers."

    if pets <= 0 or mins <= 0:
        return "Error: Number of pets and minutes must be greater than zero."

    weekend_map = {"YES": 15.0, "NO": 0.0}
    weekend_key = weekend_str.upper()
    if weekend_key not in weekend_map:
        return "Error: Weekend flag must be 'YES' or 'NO'."

    weekend_fee = weekend_map[weekend_key]
    base_fee = 20.0 if mins <= 30 else 35.0
    total = base_fee + (pets * 5.0) + weekend_fee
    return f"Walk: {pets} pets, {mins} mins - Total ${total:.2f}"


def compute_pace_per_pet(walk_metrics_str):
    if not isinstance(walk_metrics_str, str):
        return "Error: Walk metrics must be a string in '<minutes>/<pets>' format."

    parts = [part.strip() for part in walk_metrics_str.strip().split('/')]
    if len(parts) != 2 or any(not p for p in parts):
        return "Error: Invalid metrics format. Expected '<minutes>/<pets>'."

    mins_str, pets_str = parts

    try:
        mins = float(mins_str)
        pets = float(pets_str)
    except ValueError:
        return "Error: Minutes and pets must be valid numbers."

    if not (math.isfinite(mins) and math.isfinite(pets)):
        return "Error: Minutes and pets must be finite numbers."

    if mins < 0:
        return "Error: Minutes cannot be negative."

    if pets <= 0:
        return "Error: Number of pets must be greater than zero."

    pace = mins / pets
    return round(pace, 2)


def lookup_temperament_surcharge(temperament_code):
    if not isinstance(temperament_code, str):
        return "Error: Temperament code must be a string."

    cleaned = temperament_code.strip().upper()
    if len(cleaned) < 3:
        return "Error: Temperament code must be at least 3 characters (e.g., CALM, PLAYFUL)."

    prefix = cleaned[:3]
    surcharges = {
        "CAL": 0.0,
        "PLY": 5.0,
        "REA": 12.0,
        "AGG": 20.0,
    }

    if prefix not in surcharges:
        return f"Error: Unknown temperament code '{temperament_code.strip()}'."

    return surcharges[prefix]


def main():
    print("==== Running parse_walk_schedule ====")
    s_input = input("Enter schedule (e.g. 2-30-YES): ")
    print(parse_walk_schedule(s_input))

    print("\n==== Running compute_pace_per_pet ====")
    p_input = input("Enter minutes/pets (e.g. 45/3): ")
    print("Pace (min/pet):", compute_pace_per_pet(p_input))

    print("\n==== Running lookup_temperament_surcharge ====")
    t_input = input("Enter temperament code (e.g. CALM, PLAYFUL, AGGRESSIVE): ")
    print("Surcharge: $", lookup_temperament_surcharge(t_input))


if __name__ == "__main__":
    main()

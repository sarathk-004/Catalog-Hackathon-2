from tabulate import tabulate
def crop_selection():
    soil_type = input("Enter soil type (sandy, clay, loamy): ").lower()
    climate = input("Enter climate (tropical, temperate, arid): ").lower()
    season = input("Enter season (summer, winter, monsoon): ").lower()
    recommendations = []

    if soil_type == "loamy" and climate == "tropical" and season == "monsoon":
        recommendations.append(["Rice", "June - July", "High"])
    elif soil_type == "sandy" and climate == "arid" and season == "summer":
        recommendations.append(["Millets", "March - April", "Moderate"])
    elif soil_type == "clay" and climate == "temperate" and season == "winter":
        recommendations.append(["Wheat", "October - November", "High"])
    else:
        print("No exact match found. Let's gather more details.")
        water_availability = input("Enter water availability (high, medium, low): ").lower()
        market_demand = input("Is there high market demand for any specific crop? (yes/no): ").lower()

        if water_availability == "high" and market_demand == "yes":
            recommendations.append(["Sugarcane", "September - October", "High"])
            recommendations.append(["Banana", "Year-round", "High"])
        elif water_availability == "low":
            recommendations.append(["Millets", "March - April", "Moderate"])
            recommendations.append(["Pulses", "July - August", "Moderate"])
        else:
            recommendations.append(["Consider mixed farming for sustainability", "Varies", "Varies"])

    
    headers = ["Crop", "Planting Time", "Expected Yield"]
    print(tabulate(recommendations, headers, tablefmt="grid"))
    print()


def soil_management():
    soil_ph = float(input("Enter soil pH level: "))
    nutrient_level = input("Enter nutrient level (high, medium, low): ").lower()
    recommendations = []

    if soil_ph < 5.5:
        recommendations.append(["Add lime to increase pH", "Immediate"])
    elif soil_ph > 7.5:
        recommendations.append(["Add sulfur to decrease pH", "Immediate"])
    else:
        recommendations.append(["pH level is optimal", "No action needed"])

    
    if nutrient_level == "low":
        recommendations.append(["Use organic compost or NPK fertilizers", "Monthly"])
    elif nutrient_level == "medium":
        recommendations.append(["Maintain with balanced fertilizers", "As needed"])
    
    headers = ["Recommendation", "Timeframe"]
    print(tabulate(recommendations, headers, tablefmt="grid"))
    print()



def disease_identification():
    crops = ["1. Wheat", "2. Tomato", "3. Rice", "4. Corn"]
    print("Select a crop type:")
    for crop in crops:
        print(crop)

    choice = int(input("Enter the number corresponding to the crop: "))
    crop_type = crops[choice - 1].split(". ")[1].lower()
    symptoms = input("Enter observed symptoms: ").lower()
    diagnosis = []

    if crop_type == "wheat" and "yellow spots" in symptoms:
        diagnosis.append(["Yellow Rust", "Apply fungicides, use resistant varieties"])
    elif crop_type == "tomato" and "wilting" in symptoms:
        diagnosis.append(["Fusarium Wilt", "Crop rotation, soil solarization"])
    else:
        print("No exact match found. Let's gather more details.")
        spread_rate = input("How fast is the disease spreading? (fast, slow): ").lower()
        affected_parts = input("Which parts are affected? (leaves, stem, roots, all): ").lower()

        if spread_rate == "fast" and affected_parts == "all":
            diagnosis.append(["Suspected Viral Infection", "Isolate affected plants, apply appropriate treatment"])
        elif affected_parts == "leaves":
            diagnosis.append(["Possible fungal infection", "Apply fungicides, remove affected leaves"])
        else:
            diagnosis.append(["General crop health issue", "Improve soil and water management, monitor closely"])

    headers = ["Potential Disease", "Treatment"]
    print(tabulate(diagnosis, headers, tablefmt="grid"))
    print()

def main_menu():
    while True:
        print("Crop and Soil Management System")
        print("1. Crop Selection")
        print("2. Soil Management")
        print("3. Disease Identification")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            crop_selection()
        elif choice == '2':
            soil_management()
        elif choice == '3':
            disease_identification()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
        print()

main_menu()

devices = []  # le nom du branchement elec'

while True:
    device_name = input("Donne un nom a ton branchement (ou 'fin' pour finir): ")
    if device_name.lower() == "fin":
        break

    power = float(input("Entre la capacite du truc a brancher (en watts): "))
    duration = float(input("Entre la duree durant laquelle tu veux brancher le zinzin (En heures): "))
    hour_of_usage = int(input("Entre l'heure a laquelle tu le branches, pour connaitre le cout des heures creuses et pleines (0-23): "))

    device = {
        "name": device_name,
        "power": power,
        "duration": duration,
        "hour_of_usage": hour_of_usage,
    }
    devices.append(device)

# Defini le prix
daytime_price = 0.2228  
nighttime_price = 0.1615  

total_energy_consumption = 0
total_cost = 0

# Rendu dans un putain de tableauu useless
print("+" + "-" * 55 + "+")
print("|{:<20}|{:<15}|{:<15}|{:<15}|".format("Nom", "Conso'", "Cout", "Duree utilisation"))
print("|" + "-" * 55 + "|")

for device in devices:
    power = device["power"]
    duration = device["duration"]
    hour_of_usage = device["hour_of_usage"]

    # Determine the electricity price based on the hour of usage
    if 4 <= hour_of_usage < 22:
        price = daytime_price
    else:
        price = nighttime_price

    # Calculate energy consumption (in kilowatt-hours) and cost (in euros) for each device
    energy_consumption = (power * duration) / 1000  # Dividing by 1000 to convert watt-hours to kilowatt-hours
    cost = energy_consumption * price

    total_energy_consumption += energy_consumption
    total_cost += cost

    print("|{:<20}|{:<15.2f}|{:<15.2f}|{:<15}|".format(device["name"], energy_consumption, cost, hour_of_usage))

print("+" + "-" * 55 + "+")
print("|{:<20}|{:<15.2f}|{:<15.2f}|{:<15}|".format("Total", total_energy_consumption, total_cost, ""))
print("+" + "-" * 55 + "+")


# class Vehicle:
#     def __init__(self, registration_number, vehicle_type, owner):
#         self.registration_number = registration_number
#         self.type = vehicle_type
#         self.owner = owner
    
#     def update_owner(self, new_owner):
#         self.owner = new_owner




# vehicle1 = Vehicle("ABC123", "Sedan", "Keldon")
# vehicle2 = Vehicle("XYZ456", "SUV", "Chance")


# print("Initial Details:")
# print(f"Vehicle 1 - Registration Number: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
# print(f"Vehicle 2 - Registration Number: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")
# print()

# # Changing owner of vehicle1
# vehicle1.update_owner("Carter")
# vehicle2.update_owner("Cecilia")

# # Displaying updated details
# print("After Owner Update:")
# print(f"Vehicle 1 - Registration Number: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
# print(f"Vehicle 2 - Registration Number: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  
    
    def add_participant(self):
        self.participant_count += 1
    
    def get_participant_count(self):
        return self.participant_count
    
event = Event("Cook out", "07-04-2024")


event.add_participant()
event.add_participant()
event.add_participant()


participant_count = event.get_participant_count()


print(f"Event Name: {event.name}")
print(f"Event Date: {event.date}")
print(f"Participant Count: {participant_count}")


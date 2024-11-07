booking_records = {}
used_seats = set()

while True:
    record = input("Enter booking record (or type 'exit' to quit): ")
    if record.lower() == 'exit':
        break
    customer_name, movie_name, seat_number = record.split('-')
    seat_number = seat_number.strip()  
        
    if seat_number in used_seats:
        print(f"Error: Seat {seat_number} is already booked for another customer.")
        continue
        
    booking_records[customer_name] = (movie_name, seat_number)
    used_seats.add(seat_number)
    print(f"Booking successful: {customer_name} for {movie_name} at seat {seat_number}.")

print("\nAll Booking Records:")
for customer, (movie, seat) in booking_records.items():
    print(f"{customer} booked {movie} at seat {seat}")
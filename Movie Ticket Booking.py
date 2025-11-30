print(" Welcome to the Movie Ticket Booking System!")
print("---------------------------------------------")


movies = ["Krrish 44", "All of Us are Dead", "Superman", "Thor -Ragnarok🐱‍🐉"]


print("\nAvailable Movies:")
for i, movie in enumerate(movies, start=1):
    print(f"{i}. {movie}")


choice = int(input("\nEnter the movie number you want to watch: "))


if choice < 1 or choice > len(movies):
    print(" Invalid choice! Please restart the program.")
    exit()

selected_movie = movies[choice - 1]
print(f"\n You selected: {selected_movie}")


tickets = int(input("How many tickets do you want to book? "))


ticket_price = 150  
total_amount = tickets * ticket_price

print(f"\n Ticket Price: ₹{ticket_price} per ticket")
print(f" Total Amount: ₹{total_amount}")


confirm = input("\nDo you want to confirm the booking? (yes/no): ").lower()

if confirm == "yes":
    print("\n Booking Confirmed!")
    print(f"Enjoy your movie – {selected_movie}! 🍿🎬")
else:
    print("\n Booking Cancelled. Have a nice day!")

class Reservation:
    def __init__(self,room,name,days):
        self.room = room
        self.name = name
        self.days = days

class Hotel:
    def __init__(self):
        self.booked = []
        self.available = [f"Room{i}" for i in range(1, 21)]

    def Rooms(self):
        if not self.available:
            print("\nNo rooms are available at the moment")
            return
        else:
            print("\nHere are our available rooms for booking:\n")
            for i, room in enumerate(self.available, 1):
                print(f"{room:6}", end=" | ")
                if i % 4 == 0:
                    print()


    def Make_res(self):
        if not self.available:
            return
        else:
            book = input("\nWhich room would you like to book?: ")
            if book not in self.available:
                print(f"\nThere isn't a room by the name {book}.\n")
                return
            else:
                name = input("\nTell us your name: ")
                days = int(input("How many days will you be staying?: "))
                price = input(f"The price for that room for {days} days is ${days * 20}."
                              f"\nDoes that work for you?: ")
                if price.lower() == 'yes':
                    print(f"\nWonderful!A reservation under the name {name} is made.\n")
                    self.booked.append(Reservation(book,name,days))
                    self.available.remove(book)
                else:
                    print("I'm so sorry to hear that.")
                    return

    def check_out(self):
        if not self.booked:
            print("\nThere aren't any booked rooms to check out of.\n")
            return
        else:
            print()
            out = input("\nWhich room are you checking out of?: ")
            for res in self.booked:
                if res.room == out:
                    self.booked.remove(res)
                    self.available.append(out)
                    self.available.sort(key=lambda x: int(x[4:]))
                    print(f"\n{res.name} has checked out.{out} is now available.\n")
                    return
            print(f"\nNo reservation found for room {out}.")

    def see_reservations(self):
        if not self.booked:
            print("\nThere aren't any booked rooms.\n")
            return
        print("\nBooked rooms so far: ")
        print()
        for i in self.booked:
            print(f"Room:{i.room:6},Name: {i.name:12},Days: {i.days}")
        print()
    def start(self):
        while True:
            print("\n---------Hotel Beluga---------")
            print("---------Reservations---------")

            print("\nGood day everyone!")
            print("\nHere's a list of jobs we can do: ")
            print("\n1.Reservation")
            print("2.Check out")
            print("3.See reservations")
            print("4.See available rooms")
            what = input("\nWhat are we doing today?: ").split(",")

            for w in what:
                if w == '1':
                    self.Rooms()
                    self.Make_res()
                elif w == '2':
                    self.check_out()
                elif w == '3':
                    self.see_reservations()
                elif w == '4':
                    self.Rooms()

if __name__ == '__main__':
    hotel = Hotel()
    hotel.start()
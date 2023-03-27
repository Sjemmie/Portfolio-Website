import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """"Book a hotel and change its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """"Check if hotel is available"""
        available = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if available == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thanks for the reservation!
        Here are your booking data: 
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_security.loc[df_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


class SpaTicket(ReservationTicket):
    def ticket(self):
        content = f"""
                Thanks for your SPA reservation!
                Here are your booking data: 
                Name: {self.customer_name}
                Hotel: {self.hotel.name}
                """
        return content


print(df)
hotel_ID = input("enter the id of the hotel: ")
spa_hotel = Hotel(hotel_ID)

if spa_hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            spa_hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, spa_hotel)
            print(reservation_ticket.generate())
            spa_deal = input("Do you want to book a spa package? ")
            if spa_deal == "yes":
                spa_ticket = SpaTicket(name, spa_hotel)
                print(spa_ticket.ticket())
            else:
                print("You have decided to not use the spa package!")
        else:
            print("Credit card authentication failed")
    else:
        print("There was a problem with your card")
else:
    print("Hotel is not available")

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age 
        self.is_rewards_member = False 
        self.gold_card_points = 0 

    def display_info(self):
        print(self)

    def enroll(self, points):
        self.gold_card_points += points 
        if self.is_rewards_member is False :
            self.is_rewards_member = True 
            return True 
        else: 
            print("User already a member.")
            return False

    def spend_points(self, amount):
        if self.gold_card_points < amount :
            print("Not enough points for transaction.")
        else:
            balance = self.gold_card_points = self.gold_card_points - amount
            return balance

Alex = User("Alex", "Tate", "alex@123", 23)
Alex.display_info()
print(Alex.enroll(200))
print(Alex.gold_card_points)
print(Alex.spend_points(50))


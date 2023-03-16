from faker import Faker
from models import db, Player, Team

fake = Faker()


if __name__ == '__main__':
    teams = []
    for i in range(32):
        team = Team(name = fake.name(), location = fake.city())
        teams.append(team)
    print(teams)    
    




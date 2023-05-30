from faker import Faker
from faker.providers import company
from models import db, Player, Team
from app import app

fake = Faker()
fake.add_provider(company)


if __name__ == '__main__':
    with app.app_context():
        db.session.query(Team).delete()
        teams = []
        for i in range(32):
            team = Team(name = fake.name(), location = fake.company(industry = 'Sports'))
            teams.append(team)
        db.session.add_all(teams)
        db.session.commit()    

        # players = []
        # for x in range(960):
        #     player = Player(first_name = fake.first_name())
        #     players.append(player)
        # db.session.add_all(players)
        # db.session.commit()    
    




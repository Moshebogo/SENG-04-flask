from flask import Flask, render_template, jsonify, make_response, request
from models import db, Pet, Owner
from flask_migrate import Migrate

   
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route("/")
def root():
    return render_template("index.html")

      ###### pets  ###### 
@app.route("/api/pets", methods = ["GET", "POST"])
def get_all_pets():
    if request.method == "GET":
        pets = Pet.query.all()
        pets_dict = [pet.to_dict() for pet in pets]
        return make_response(jsonify(pets_dict), 200)   
    
    elif request.method == "POST":
        data = request.get_json()
        new_pet = Pet()
        for field in data:
            setattr(new_pet, field, data[field])
        db.session.add(new_pet)
        db.session.commit()
        return make_response(jsonify({"Status": "POST successful"}), 201)
             

@app.route("/api/pets/<int:id>", methods = ['GET', 'DELETE', 'PATCH'])
def get_pet_by_id(id):
    pet = Pet.query.get(id)
     
    if not pet:
        return make_response(jsonify({'Error': 'That pet does not exist'}), 404)
    
    elif request.method == "GET":
        return make_response(jsonify(pet.to_dict()), 200)

    elif request.method == "DELETE":
        db.session.delete(pet)
        db.session.commit()    
        return make_response(jsonify({"status": "DELETE successful"}), 200)

    elif request.method == "PATCH":
        data = request.get_json()
        for field in data:
            # pet.field = data[field] # why does this not work?
            setattr(pet, field, data[field])
        db.session.add(pet)
        db.session.commit()     
        return make_response(jsonify(pet.to_dict()), 200) 
       
    ###### owners  ###### 
@app.route("/api/owners", methods = ["GET", "POST"])
def get_all_owners():
    if request.method == "GET":
        owners = Owner.query.all()
        owners_to_dict = [owner.to_dict() for owner in owners]
        return make_response(jsonify(owners_to_dict), 200)
    
    elif request.method == "POST":
        data = request.get_json()
        new_owner = Owner()
        for key in data:
            setattr(new_owner, key, data[key])
        db.session.add(new_owner)
        db.session.commit()
        return make_response(jsonify(new_owner.to_dict()), 201)    

@app.route("/api/owners/<id>", methods= ["GET", "DELETE", "PATCH"])
def get_owner_id(id):
    owner = Owner.query.get(id)  

    if not owner:
        return make_response(jsonify({"error": "that owner does not exist"}), 404)  
    
    elif request.method == "GET":
        return make_response(jsonify(owner.to_dict()), 200) 
    
    elif request.method == "DELETE":
        db.session.delete(owner)
        db.session.commit()
        return make_response(jsonify({"status": "DELETE successful"}), 200)
    
    elif request.method == "PATCH":
        data = request.get_json()
        for key in data:
            setattr(owner, key, data[key])
        db.session.add(owner)
        db.session.commit()
        return make_response(jsonify(owner.to_dict()), 200)
           

@app.route('/message/<my_message>')
def message(my_message):
    return render_template('message.html', message=my_message)

if __name__ == '__main__':
    app.run(debug = True, port = 8000, host = '127.0.0.1')
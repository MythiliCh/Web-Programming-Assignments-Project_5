import json
from mongita import MongitaClientDisk
from werkzeug.security import generate_password_hash, check_password_hash

client = MongitaClientDisk()
user_db = client.user_db
user_collection = user_db.user_collection

def register_user(username, password):
    password_hash = generate_password_hash(password)
    user_data = {"username": username, "password_hash": password_hash}
    user_collection.insert_one(user_data)

def verify_user(username, password):
    user_data = user_collection.find_one({"username": username})
    if user_data:
        return check_password_hash(user_data["password_hash"], password)
    return False


# # Create a Mongita database with movie information
# import json
# from mongita import MongitaClientDisk
# from werkzeug.security import generate_password_hash

# # create a mongita client connection
# client = MongitaClientDisk()

# # create a database
# user_db = client.user_d

# #create a session collection
# user_collection = user_db.user_collection



# # empty the collection
# #user_collection.delete_many({})

# def create_user(username, password):
#     password_hash = generate_password_hash(password)
#     user_collection.insert_one({'user': username, 'password_hash': password_hash})

# # make sure the session are there
# print(user_collection.count_documents({}))
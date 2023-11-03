import pymongo

ph_numbers = ["+918386861394", "+919535242993", "+918151006864", "+918431264006", "+917483997061", "+919606833424", "+919738985383", "+916364673204", "+917676751856", "+918792381485", "+918336975741", "+917019390113"]

uri = "mongodb+srv://vivekdgrt:Pintu090703@cluster0.qxivjzg.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = pymongo.MongoClient(uri)
database = client["Tournament"]
table = database["Applicants"]
data = table.find()

def modify_number(number):
    if(len(number) == 10):
        modified_number = "+91" + number
        ph_numbers.append(modified_number)

for team in data:
    modify_number(team["player1_mob"])
    modify_number(team["player2_mob"])
    modify_number(team["player3_mob"])
    modify_number(team["player4_mob"])
    modify_number(team["player5_mob"])
    modify_number(team["player6_mob"])
    

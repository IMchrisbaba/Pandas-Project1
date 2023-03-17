import csv
import statistics
rows = []
all_vehicles = []
all_credit_card = []
all_address = []
all = []
with open("C:\\Users\\USER\\Data Science\\acw_user_data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
# print(header)
# print(rows[0][19])


def get_vehicle(person):
    vehicle = {}
    veh = {}
    listy = ['make', 'Model', 'Year', 'Type']
    list2 = []
    for i in range(19,23):
        list2.append(rows[person][i])
    for i in range(4):
        veh[f"{listy[i]}"] = list2[i]
    vehicle['vehicle'] = veh
    return vehicle

def get_credit_card(person):
    details = {}
    det = {}
    listy = ['start_date', 'end_date', 'number', 'ccv', 'iban']
    list2 = []
    list3 = [6, 7, 8, 9, 12]
    for i in list3:
        list2.append(rows[person][i])
    for i in range(5):
        det[f"{listy[i]}"] = list2[i]
    details['Credit Card'] = det
    return details

def get_address(person):
    address = {}
    add = {}
    listy = ['street', 'city', 'postcode']
    list2 = []
    for i in range(3):
        list2.append(rows[person][i])
    for i in range(3):
        add[f"{listy[i]}"] = list2[i]
    address['Address'] = add
    return address

def all_vehicle():
    for i in range(len(rows)):
        all_vehicles.append(get_vehicle(i))

def all_credit_cards():
    for i in range(len(rows)):
        all_credit_card.append(get_credit_card(i))

def all_addresses():
    for i in range(len(rows)):
        all_address.append(get_address(i))

# all_vehicle()
# all_credit_cards()
# all_addresses()
# print(all_vehicles)
# print(all_credit_card)
# print(all_address)

# def 

dependant = []
nan_dependant = []
def get_dependants():
    for i in range(len(rows)):
        if rows[i][10]!="":
            dependant.append(rows[i][10])
        else:
            continue


get_dependants()
mode = statistics.mode(dependant)
# print(dependant)
# print(nan_dependant)
# print(mode)




def get_person_detail(persons):
    # for persons in range(len(rows)):
    person = {}
    person[f"{header[11]}"] = rows[persons][11]
    person[f"{header[13]}"] = rows[persons][13]
    person[f"{header[3]}"] = rows[persons][3]
    person[f"{header[18]}"] = rows[persons][18]
    person[f"{header[16]}"] = rows[persons][16]
    person[f"{header[14]}"] = rows[persons][14]
    person[f"{header[10]}"] = rows[persons][10]
    if rows[persons][10] != "":
        person[f"{header[10]}"] = rows[persons][10]
    else:
        person[f"{header[10]}"] = mode
        nan_dependant.append(persons+1)
    person[f"{header[17]}"] = rows[persons][17]
    person[f"{header[15]}"] = rows[persons][15]
    person[f"{header[1]}"] = rows[persons][1]
    person[f"{header[0]}"] = rows[persons][0]

    
    # veh = {}
    # listy = ['make', 'Model', 'Year', 'Type']
    # list2 = []
    # for i in range(19,23):
    #     list2.append(rows[persons][i])
    # for i in range(4):
    #     veh[f"{listy[i]}"] = list2[i]
    # person['vehicle'] = veh
    person['vehicle'] = get_vehicle(persons)
    

    # details = {}
    # det = {}
    # listy = ['start_date', 'end_date', 'number', 'ccv', 'iban']
    # list2 = []
    # list3 = [6, 7, 8, 9, 12]
    # for i in list3:
    #     list2.append(rows[persons][i])
    # for i in range(5):
    #     det[f"{listy[i]}"] = list2[i]
    # person['Credit Card'] = det
    person['Credit Card'] = get_credit_card(persons)


    # address = {}
    # add = {}
    # listy = ['street', 'city', 'postcode']
    # list2 = []
    # for i in range(3):
    #     list2.append(rows[persons][i])
    # for i in range(3):
    #     add[f"{listy[i]}"] = list2[i]
    # person['Address'] = add

    person['Address'] = get_address(persons)
    return person



# get_person_detail()

def all_people():
    for i in range(len(rows)):
        all.append(get_person_detail(i))


all_people()
# for i in range(len(rows)):
#     print(all[i])
# print(f"The rows without dependants are {nan_dependant}")

print(rows[0][6])
# # print(range(len(rows)))
# print(all[21])
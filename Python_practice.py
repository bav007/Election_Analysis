name = "Bav"
print(name)
print(type(name))

counties_dict = {}
counties_dict["Arapahoe"]=422829
counties_dict["Jefferson"]=432438
counties_dict["third"]=433224
counties_dict.values()
len(counties_dict)

counties_dict.keys()
counties_dict
len(counties_dict)

counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.items()
counties_dict.get("third")

counties_dict['Arapahoe']


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
#print(voting_data[0]['county'], voting_data[2]['registered_voters'])

voting_data[1]['county'] = 'El Paso'
voting_data[1]['registered_voters'] = 461149
voting_data.pop[0]

del voting_data[0][0]
del voting_data[0][1]
voting_data

#voting_data[2]({"county":"El Paso","registered_voters": 45556})







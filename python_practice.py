print("Hello World")
counties = ['Arapahoe', 'Denver', 'Jefferson']
counties.insert(1, 'El Paso')
counties.pop(0)
counties[2] = 'Denver'
counties[1] = 'Jefferson'
counties.append('Arapahoe')
print(counties)



counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict.keys())

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(1, {"county":"El Paso", "registered_voter": 461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data[2] = {"county":"Denver", "registered_voters": 463353}
voting_data[1] = {"county":"Jefferson", "registered_voters": 432438}
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)


counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

for county in counties_dict.keys():
    print(county)

for county, voters in counties_dict.items():
    print(str(county) + " county has " + str(voters) + " registered voters.")
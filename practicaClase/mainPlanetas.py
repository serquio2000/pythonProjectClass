def main():
    #Variables
    name = list()
    weight = list()
    diameter = list()
    distance = list()
    header = ['name', 'weight', 'diameter', 'distance with Earth'] #header for table
    values = int(input("how many planets, would you like insert:")) # values for register
   #validation
    while values < 0:
        values = int(input("how many planets, would you like insert:"))
    #append in list
    for i in range(values):
        name.append(input("insert name of planet:"))
        weight.append(int(input("insert weight of planet:")))
        diameter.append(int(input("insert diameter of planet:")))
        distance.append(int(input("insert distance of planet with Earth:")))
    #dictionary
    val = {
        "name": name,
        "weight": weight,
        "diameter": diameter,
        "distance": distance

    }
    #print header
    for i in header:
        print(i, end="\t|")
    print()
    #print table
    for i in range(values):
        print(val['name'][i] + "\t" + str(val['weight'][i]) + "\t" + str(val['diameter'][i]) + "\t" + str(
        val['distance'][i]) + "\t")


if __name__ == "__main__":
    main()

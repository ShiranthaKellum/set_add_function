
countryList = []
countrySet = set (countryList)
noOfCountries = int (input ())
for i in range (noOfCountries):
    countrySet.add (input ())

print (len (countrySet))
#Dictionarys is Mutable

emptyDictionary = {}

dictCap = {"Bihar":"Patna","Uttar Pradesh":"Lucknow","Rajasthan":"Jaipur","Maharashtra":"Mumbai","Andhra Pradesh":"Amaravati","Karnataka":"Bangalore"}
dictMarks = {"Keshu":100,"Alok":70,"Shubham":80,"Vinit":90,"Mayank":30,"Rekha":40,"Jaya":50,"Nirma":60,"Sushma":20,"Hema":10,"Shivangi":0}


print(dictCap.get("Uttar Pradesh"))
print(dictCap["Uttar Pradesh"])
print(dictCap.get("Bihar"))
print(dictCap["Bihar"])
print(dictCap.get("Goa"))
print(dictCap["Goa"])
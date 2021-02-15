dinners={
    "D1":{
    "meal":"Spaghetti",
    "extras":"Meatballs",
    "prep":"2 hours",
    },

    "D2":{
    "meal":"Steak",
    "extras":"Sauteed mushrooms and onions",
    "prep":"4 hours",
    },
    "D3":{
    "meal":"Lasagna",
    "extras":"veggies",
    "prep":"3 hours",
    },
    
}

for D, info in dinners.items():
    
    extras =info["extras"]
    prep = info["prep"]
   
    print(f"\tExtras: {extras}")
    print(f"\tPrep: {prep}")
   


    
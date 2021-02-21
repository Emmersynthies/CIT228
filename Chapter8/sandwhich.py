def sandwich_meat(*meats):
   
   print("\n There are many meats you can choose from:")
   for food in meats:
       print(f"make  "+ food + "  in my sandwich.")
  


sandwich_meat("turkey")
sandwich_meat("Ham","steak", "tuna")
sandwich_meat("meatballs","provalone")
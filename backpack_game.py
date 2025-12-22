#🎒 Backpack Game To Practice Sets And Dictionaries
"""
This is just a sample game that i build for my understanding in list,sets and dictionaries and also to commit my fist push
in my git hub as a project this is not a game but still it represents something related to it this would give a start to my 
journey to my python learning for AI/ML
---13-12-2025
"""

#0️⃣Start Backpack Game.
#----------------------------------------------------
backpack=[]
print("0. 🙂Starting Journey With Empty Backpack.")
print("🎒",backpack)
print("-"*50)

#1️⃣ Pick Up Starter Kit Items.
#----------------------------------------------------
print("1. 📦Picking Up StarterKit(Armor,Sheild,Sword,Potion).")
backpack.append("Armor")
backpack.append("Sheild")
backpack.append("Sword")
backpack.append("Potion")
print("🎒",backpack)
print("-"*100)

#2️⃣ Loot a Tresure Chest.
#----------------------------------------------------
chest=["Map","Potion","Compass","Potion"]
print(f"Chest🧰:{chest}")
backpack.extend(chest)      #backpack+=chest
print("🎒",backpack)
print("-"*100)

#3️⃣ Visit Merchant.
#-----------------------------------------------------
print("3. 🧙‍♂️ Visiting Merchant")
print("- selling the sheild.")
print("- upgrading Sword -> Magic GreatSword")
backpack.remove("Sheild")
inx=backpack.index("Sword")
backpack[inx]="Magic-GreatSword"
print("🎒",backpack)
print("-"*100)

#4️⃣ Check Inventory.
#-----------------------------------------------------
print("4. 🔎Checking Backpack:")
print("🎒",backpack)
total_count=len(backpack)
unique_items=set(backpack)
unique_count=len(unique_items)
potion_count=backpack.count("Potion")
print(f"There are {total_count} Items in Total.")
print(f"There are {unique_count} Unique Items.")
print(f"There are {potion_count} Potions.")

#5️⃣ Dropped the Backpack.
#-----------------------------------------------------
print("5. 🙃Dropped the BackPack Upside-Down.")
backpack.reverse()
print("🎒",backpack)
print("-"*100)

#6️⃣ Sorting Items.
#-----------------------------------------------------
print("6. ➡️Sorting Items:")
backpack.sort()
print("🎒",backpack)
print("-"*100)

#7️⃣ 3 Items Stolen During Sleep
#-----------------------------------------------------
print("7. 💤Sleeping....")
a=backpack.pop()
b=backpack.pop(2)
c=backpack.pop()
stolen=[a,b,c]
print(f"Stolen Items:",stolen)
print("🎒",backpack)
print("-"*100)

#8️⃣ Found Magic-Ring
#-----------------------------------------------------
print("8. 💍Found Magic Ring And Coin Pouch")
ring="Magic Ring"
coin_pouch=["Gold Coin","Silver Coin"]
backpack.insert(0,ring)
backpack.append(coin_pouch)
print("🎒",backpack)
print("-"*100)

#9️⃣ Half Backpack Contents Have Teleported
#-----------------------------------------------------
print("9. 💥Half Items Magically Disappeared. Damn You Magic Ring....")
count=len(backpack)
half=int(count/2)
backpack=backpack[half:]
print("🎒",backpack)
print("-"*100)

#🔟 Bandits Stole Empty Backpack
#------------------------------------------------------
print("10. 🧌Bandits Attacked.")
print("Backpack Stolen.....")
backpack=None
print("🎒",backpack)
print("-"*100)

#-----------------  THE END ---------------------------
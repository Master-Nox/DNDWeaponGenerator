import random
import pandas as pd
import PySimpleGUI as sg
import textwrap

# Goals for this project
# Recreate all of the functionality found here: https://docs.google.com/spreadsheets/d/1HZmkBrDlUfBitvuw_Zmrnt1zZbXtOLFKNL8EQbGbxYE/edit#gid=831432008
# Add the ability for curses to be applied to weapons automatically
# Have AI-Generated images be populated for each generated weapon based on it's name most likely
# A decent looking UI to tie everything together
# Perhaps an options menu to mess with the settings more easily



# This code gathers data so that the csv files only need to be accessed once, it should be run first.

MaterialListData = pd.read_csv(r"C:\Users\FreeW\Documents\GitHub\Alyra-Obsidian\DNDWeaponGenerator/Materials.csv")

MaterialDescriptionDictionary = {}

index = 0
for MaterialName in MaterialListData.Name:
    MaterialDescriptionDictionary[MaterialName] = MaterialListData.Description[index]
    index +=1

MaterialWeaponMechanicDictionary = {}

index = 0
for MaterialName in MaterialListData.Name:
    MaterialWeaponMechanicDictionary[MaterialName] = MaterialListData.WeaponMechanic[index]
    index +=1

MaterialArmorMechanicDictionary = {}

index = 0
for MaterialName in MaterialListData.Name:
    MaterialArmorMechanicDictionary[MaterialName] = MaterialListData.ArmorMechanic[index]
    index +=1


index = 0
CommonMaterials = []

for MaterialName in MaterialListData.Name:
    if MaterialListData.Rarity[index] == "Common":
        CommonMaterials.append(MaterialName)
    index +=1

index = 0
UncommonMaterials = []

for MaterialName in MaterialListData.Name:
    if MaterialListData.Rarity[index] == "Uncommon":
        UncommonMaterials.append(MaterialName)
    index +=1
    
index = 0
RareMaterials = []

for MaterialName in MaterialListData.Name:
    if MaterialListData.Rarity[index] == "Rare":
        RareMaterials.append(MaterialName)
    index +=1
    
index = 0
VeryRareMaterials = []

for MaterialName in MaterialListData.Name:
    if MaterialListData.Rarity[index] == "Very Rare":
        VeryRareMaterials.append(MaterialName)
    index +=1
    
index = 0
LegendaryMaterials = []

for MaterialName in MaterialListData.Name:
    if MaterialListData.Rarity[index] == "Legendary":
        LegendaryMaterials.append(MaterialName)
    index +=1

WeaponListData = pd.read_csv(r"C:\Users\FreeW\Documents\GitHub\Alyra-Obsidian\DNDWeaponGenerator/Weapons.csv")

RangedWeapons = ["Crossbow, light", "Crossbow, hand", "Crossbow, heavy", "Shortbow", "Sling", "Blowgun", "Longbow"]
ThrownWeapons = ["Dagger", "Handaxe", "Javelin", "Spear", "Dart", "Net"]
Ammo = ["Arrows", "Crossbow Bolts", "Bullets", "Dart"]
MeleeWeapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War pick", "Warhammer", "Whip"]

WeaponEnchantmentData = pd.read_csv(r"C:\Users\FreeW\Documents\GitHub\Alyra-Obsidian\DNDWeaponGenerator/Weapon Enchantments.csv")

WeaponEnchantmentDescriptionDictionary = {}

index = 0
for EnchantmentName in WeaponEnchantmentData.Name:
    WeaponEnchantmentDescriptionDictionary[EnchantmentName] = WeaponEnchantmentData.Description[index]
    index +=1
WeaponEnchantmentDescriptionDictionary.pop("None")

ArmorListData = pd.read_csv(r"C:\Users\FreeW\Documents\GitHub\Alyra-Obsidian\DNDWeaponGenerator/Armor.csv")

ArmorEnchantmentData = pd.read_csv(r"C:\Users\FreeW\Documents\GitHub\Alyra-Obsidian\DNDWeaponGenerator/Armor Enchantments.csv")

ArmorEnchantmentDescriptionDictionary = {}

index = 0
for EnchantmentName in ArmorEnchantmentData.Name:
    ArmorEnchantmentDescriptionDictionary[EnchantmentName] = ArmorEnchantmentData.Description[index]
    index +=1
ArmorEnchantmentDescriptionDictionary.pop("None")

# Armor Enchantment Rarity Lists

index = 0
CommonArmorEnchantments = []

for EnchantmentName in ArmorEnchantmentData.Name:
    if ArmorEnchantmentData.Rarity[index] == "Common":
        CommonArmorEnchantments.append(EnchantmentName)
    index +=1

index = 0
UncommonArmorEnchantments = []

for EnchantmentName in ArmorEnchantmentData.Name:
    if ArmorEnchantmentData.Rarity[index] == "Uncommon":
        UncommonArmorEnchantments.append(EnchantmentName)
    index +=1

index = 0
RareArmorEnchantments = []

for EnchantmentName in ArmorEnchantmentData.Name:
    if ArmorEnchantmentData.Rarity[index] == "Rare":
        RareArmorEnchantments.append(EnchantmentName)
    index +=1

index = 0
VeryRareArmorEnchantments = []

for EnchantmentName in ArmorEnchantmentData.Name:
    if ArmorEnchantmentData.Rarity[index] == "Very Rare":
        VeryRareArmorEnchantments.append(EnchantmentName)
    index +=1

index = 0
LegendaryArmorEnchantments = []

for EnchantmentName in ArmorEnchantmentData.Name:
    if ArmorEnchantmentData.Rarity[index] == "Legendary":
        LegendaryArmorEnchantments.append(EnchantmentName)
    index +=1

# Weapon Enchantment Rarity Lists
index = 0
CommonWeaponEnchantmentsAny = []
CommonWeaponEnchantmentsAmmo = []
CommonWeaponEnchantmentsRanged = []
CommonWeaponEnchantmentsThrown = []
CommonWeaponEnchantmentsMelee = []

for EnchantmentName in WeaponEnchantmentData.Name:
    if WeaponEnchantmentData.Rarity[index] == "Common" and WeaponEnchantmentData.Requirements[index] == "Any":
        CommonWeaponEnchantmentsAny.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Common" and WeaponEnchantmentData.Requirements[index] == "Ammo":
        CommonWeaponEnchantmentsAmmo.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Common" and WeaponEnchantmentData.Requirements[index] == "Ranged":
        CommonWeaponEnchantmentsRanged.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Common" and WeaponEnchantmentData.Requirements[index] == "Thrown":
        CommonWeaponEnchantmentsThrown.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Common" and WeaponEnchantmentData.Requirements[index] == "Melee":
        CommonWeaponEnchantmentsMelee.append(EnchantmentName)
    index +=1
    
#print(CommonWeaponEnchantmentsAny)

index = 0
UncommonWeaponEnchantmentsAny = []
UncommonWeaponEnchantmentsAmmo = []
UncommonWeaponEnchantmentsRanged = []
UncommonWeaponEnchantmentsThrown = []
UncommonWeaponEnchantmentsMelee = []

for EnchantmentName in WeaponEnchantmentData.Name:
    if WeaponEnchantmentData.Rarity[index] == "Uncommon" and WeaponEnchantmentData.Requirements[index] == "Any":
        UncommonWeaponEnchantmentsAny.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Uncommon" and WeaponEnchantmentData.Requirements[index] == "Ammo":
        UncommonWeaponEnchantmentsAmmo.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Uncommon" and WeaponEnchantmentData.Requirements[index] == "Ranged":
        UncommonWeaponEnchantmentsRanged.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Uncommon" and WeaponEnchantmentData.Requirements[index] == "Thrown":
        UncommonWeaponEnchantmentsThrown.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Uncommon" and WeaponEnchantmentData.Requirements[index] == "Melee":
        UncommonWeaponEnchantmentsMelee.append(EnchantmentName)
    index +=1
    
#print(UncommonWeaponEnchantments)

index = 0
RareWeaponEnchantmentsAny = []
RareWeaponEnchantmentsAmmo = []
RareWeaponEnchantmentsRanged = []
RareWeaponEnchantmentsThrown = []
RareWeaponEnchantmentsMelee = []

for EnchantmentName in WeaponEnchantmentData.Name:
    if WeaponEnchantmentData.Rarity[index] == "Rare" and WeaponEnchantmentData.Requirements[index] == "Any":
        RareWeaponEnchantmentsAny.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Rare" and WeaponEnchantmentData.Requirements[index] == "Ammo":
        RareWeaponEnchantmentsAmmo.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Rare" and WeaponEnchantmentData.Requirements[index] == "Ranged":
        RareWeaponEnchantmentsRanged.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Rare" and WeaponEnchantmentData.Requirements[index] == "Thrown":
        RareWeaponEnchantmentsThrown.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Rare" and WeaponEnchantmentData.Requirements[index] == "Melee":
        RareWeaponEnchantmentsMelee.append(EnchantmentName)
    index +=1
    
#print(RareWeaponEnchantments)

index = 0
VeryRareWeaponEnchantmentsAny = []
VeryRareWeaponEnchantmentsAmmo = []
VeryRareWeaponEnchantmentsRanged = []
VeryRareWeaponEnchantmentsThrown = []
VeryRareWeaponEnchantmentsMelee = []

for EnchantmentName in WeaponEnchantmentData.Name:
    if WeaponEnchantmentData.Rarity[index] == "Very Rare" and WeaponEnchantmentData.Requirements[index] == "Any":
        VeryRareWeaponEnchantmentsAny.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Very Rare" and WeaponEnchantmentData.Requirements[index] == "Ammo":
        VeryRareWeaponEnchantmentsAmmo.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Very Rare" and WeaponEnchantmentData.Requirements[index] == "Ranged":
        VeryRareWeaponEnchantmentsRanged.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Very Rare" and WeaponEnchantmentData.Requirements[index] == "Thrown":
        VeryRareWeaponEnchantmentsThrown.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Very Rare" and WeaponEnchantmentData.Requirements[index] == "Melee":
        VeryRareWeaponEnchantmentsMelee.append(EnchantmentName)
    index +=1
    
#print(VeryRareWeaponEnchantments)

index = 0
LegendaryWeaponEnchantmentsAny = []
LegendaryWeaponEnchantmentsAmmo = []
LegendaryWeaponEnchantmentsRanged = []
LegendaryWeaponEnchantmentsThrown = []
LegendaryWeaponEnchantmentsMelee = []

for EnchantmentName in WeaponEnchantmentData.Name:
    if WeaponEnchantmentData.Rarity[index] == "Legendary" and WeaponEnchantmentData.Requirements[index] == "Any":
        LegendaryWeaponEnchantmentsAny.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Legendary" and WeaponEnchantmentData.Requirements[index] == "Ammo":
        LegendaryWeaponEnchantmentsAmmo.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Legendary" and WeaponEnchantmentData.Requirements[index] == "Ranged":
        LegendaryWeaponEnchantmentsRanged.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Legendary" and WeaponEnchantmentData.Requirements[index] == "Thrown":
        LegendaryWeaponEnchantmentsThrown.append(EnchantmentName)
    elif WeaponEnchantmentData.Rarity[index] == "Legendary" and WeaponEnchantmentData.Requirements[index] == "Melee":
        LegendaryWeaponEnchantmentsMelee.append(EnchantmentName)
    index +=1
    
#print(LegendaryWeaponEnchantments)





def GenerateItem():
    # Currently ignoring item type and just generating weaponry.
    
    

    # These three functions run the rng values and determine the rarity of an item's Enchantment, Material, and Refinement.
    def EnchantmentLevel():
        EnchantmentRNG = random.randint(1,100)
            
        if EnchantmentRNG < 30:
            EnchantmentLevel = "None"
        elif EnchantmentRNG >= 30 and EnchantmentRNG < 65:
            EnchantmentLevel = "Common"
        elif EnchantmentRNG >= 65 and EnchantmentRNG < 80:
            EnchantmentLevel = "Uncommon"
        elif EnchantmentRNG >= 80 and EnchantmentRNG < 98:
            EnchantmentLevel = "Rare"
        elif EnchantmentRNG >= 98 and EnchantmentRNG < 101:
            EnchantmentLevel = "Very Rare"
        else:
            EnchantmentLevel = "Legendary"
        
        return EnchantmentLevel
        
    def MaterialLevel():
        MaterialRNG = random.randint(1,100)
            
        if MaterialRNG < 65:
            MaterialLevel = "Common"
        elif MaterialRNG >= 65 and MaterialRNG < 80:
            MaterialLevel = "Uncommon"
        elif MaterialRNG >= 80 and MaterialRNG < 95:
            MaterialLevel = "Rare"
        elif MaterialRNG >= 95 and MaterialRNG < 101:
            MaterialLevel = "Very Rare"
        else:
            MaterialLevel = "Legendary"
        
        return MaterialLevel
        
    def RefinementLevel():
        RefinementRNG = random.randint(1,100)
            
        if RefinementRNG < 15:
            RefinementLevel = "Worn"
        elif RefinementRNG >= 15 and RefinementRNG < 70:
            RefinementLevel = "Average"
        elif RefinementRNG >= 70 and RefinementRNG < 98:
            RefinementLevel = "Honed"
        elif RefinementRNG >= 98 and RefinementRNG < 101:
            RefinementLevel = "Unique"
        else:
            RefinementLevel = "Masterwork"
        
        return RefinementLevel

    ELevel = EnchantmentLevel()
    MLevel = MaterialLevel()
    RLevel = RefinementLevel()
    
    if random.randint(0,1) == 0:
        ItemGenerated = "Weapon"
    else: 
        ItemGenerated = "Armor"

    if ItemGenerated == "Weapon":
    
        WeaponChoice = random.randint(0, len(WeaponListData.Weapon)-1)
        Item = WeaponListData.Weapon[WeaponChoice]
        WeaponCost = WeaponListData.Cost[WeaponChoice]

        if Item in RangedWeapons:
            WeaponType = "Ranged"
        elif Item in ThrownWeapons:
            WeaponType = "Thrown"
        elif Item in Ammo:
            WeaponType = "Ammo"
        elif Item in MeleeWeapons:
            WeaponType = "Melee"
        else:
            print("Weapon Type not found.")
            print(Item)

        Enchantment = ""
        EDescription = ""
        if ELevel == "None":
            pass
            # print("No Enchantment")
        elif ELevel == "Common":
            if WeaponType == "Ranged":
                EnchantmentList = CommonWeaponEnchantmentsAny + CommonWeaponEnchantmentsRanged
            elif WeaponType == "Thrown":
                EnchantmentList = CommonWeaponEnchantmentsAny + CommonWeaponEnchantmentsThrown
            elif WeaponType == "Ammo":
                EnchantmentList = CommonWeaponEnchantmentsAmmo
            elif WeaponType == "Melee":
                EnchantmentList = CommonWeaponEnchantmentsAny + CommonWeaponEnchantmentsMelee
            
            EnchantmentChoice = random.randint(0, len(EnchantmentList)-1)
            Enchantment = EnchantmentList[EnchantmentChoice]
            EDescription = WeaponEnchantmentDescriptionDictionary.get(Enchantment)
            
        elif ELevel == "Uncommon":
            if WeaponType == "Ranged":
                EnchantmentList = UncommonWeaponEnchantmentsAny + UncommonWeaponEnchantmentsRanged
            elif WeaponType == "Thrown":
                EnchantmentList = UncommonWeaponEnchantmentsAny + UncommonWeaponEnchantmentsThrown
            elif WeaponType == "Ammo":
                EnchantmentList = UncommonWeaponEnchantmentsAmmo
            elif WeaponType == "Melee":
                EnchantmentList = UncommonWeaponEnchantmentsAny + UncommonWeaponEnchantmentsMelee
            
            EnchantmentChoice = random.randint(0, len(EnchantmentList)-1)
            Enchantment = EnchantmentList[EnchantmentChoice]
            EDescription = WeaponEnchantmentDescriptionDictionary.get(Enchantment)
        elif ELevel == "Rare":
            if WeaponType == "Ranged":
                EnchantmentList = RareWeaponEnchantmentsAny + RareWeaponEnchantmentsRanged
            elif WeaponType == "Thrown":
                EnchantmentList = RareWeaponEnchantmentsAny + RareWeaponEnchantmentsThrown
            elif WeaponType == "Ammo":
                EnchantmentList = RareWeaponEnchantmentsAmmo
            elif WeaponType == "Melee":
                EnchantmentList = RareWeaponEnchantmentsAny + RareWeaponEnchantmentsMelee
            
            EnchantmentChoice = random.randint(0, len(EnchantmentList)-1)
            Enchantment = EnchantmentList[EnchantmentChoice]
            EDescription = WeaponEnchantmentDescriptionDictionary.get(Enchantment)
        elif ELevel == "Very Rare":
            if WeaponType == "Ranged":
                EnchantmentList = VeryRareWeaponEnchantmentsAny + VeryRareWeaponEnchantmentsRanged
            elif WeaponType == "Thrown":
                EnchantmentList = VeryRareWeaponEnchantmentsAny + VeryRareWeaponEnchantmentsThrown
            elif WeaponType == "Ammo":
                EnchantmentList = VeryRareWeaponEnchantmentsAmmo
            elif WeaponType == "Melee":
                EnchantmentList = VeryRareWeaponEnchantmentsAny + VeryRareWeaponEnchantmentsMelee
            
            EnchantmentChoice = random.randint(0, len(EnchantmentList)-1)
            Enchantment = EnchantmentList[EnchantmentChoice]
            EDescription = WeaponEnchantmentDescriptionDictionary.get(Enchantment)
        elif ELevel == "Legendary":
            if WeaponType == "Ranged":
                EnchantmentList = LegendaryWeaponEnchantmentsAny + LegendaryWeaponEnchantmentsRanged
            elif WeaponType == "Thrown":
                EnchantmentList = LegendaryWeaponEnchantmentsAny + LegendaryWeaponEnchantmentsThrown
            elif WeaponType == "Ammo":
                EnchantmentList = LegendaryWeaponEnchantmentsAmmo
            elif WeaponType == "Melee":
                EnchantmentList = LegendaryWeaponEnchantmentsAny + LegendaryWeaponEnchantmentsMelee
            
            EnchantmentChoice = random.randint(0, len(EnchantmentList)-1)
            Enchantment = EnchantmentList[EnchantmentChoice]
            EDescription = WeaponEnchantmentDescriptionDictionary.get(Enchantment)

        if MLevel == "Common":
            MaterialChoice = random.randint(0, len(CommonMaterials)-1)
            Material = CommonMaterials[MaterialChoice]
            MDescription = MaterialDescriptionDictionary.get(Material)
            MMechanic = MaterialWeaponMechanicDictionary.get(Material)
        elif MLevel == "Uncommon":
            MaterialChoice = random.randint(0, len(UncommonMaterials)-1)
            Material = UncommonMaterials[MaterialChoice]
            MDescription = MaterialDescriptionDictionary.get(Material)
            MMechanic = MaterialWeaponMechanicDictionary.get(Material)
        elif MLevel == "Rare":
            MaterialChoice = random.randint(0, len(RareMaterials)-1)
            Material = RareMaterials[MaterialChoice]
            MDescription = MaterialDescriptionDictionary.get(Material)
            MMechanic = MaterialWeaponMechanicDictionary.get(Material)
        elif MLevel == "Very Rare":
            MaterialChoice = random.randint(0, len(VeryRareMaterials)-1)
            Material = VeryRareMaterials[MaterialChoice]
            MDescription = MaterialDescriptionDictionary.get(Material)
            MMechanic = MaterialWeaponMechanicDictionary.get(Material)
        elif MLevel == "Legendary":
            MaterialChoice = random.randint(0, len(LegendaryMaterials)-1)
            Material = LegendaryMaterials[MaterialChoice]
            MDescription = MaterialDescriptionDictionary.get(Material)
            MMechanic = MaterialWeaponMechanicDictionary.get(Material)
    else:
        ArmorChoice = random.randint(0, len(ArmorListData.Armor)-1)
        Item = ArmorListData.Armor[ArmorChoice]
        ArmorCost = ArmorListData.Cost[ArmorChoice]
        
        Enchantment = ""
        EDescription = ""
        if ELevel == "None":
            pass
            # print("No Enchantment")
        elif ELevel == "Common":
            EnchantmentChoice = random.randint(0, len(CommonArmorEnchantments))
            Enchantment = CommonArmorEnchantments[EnchantmentChoice]
            EDescription = ArmorEnchantmentDescriptionDictionary.get(Enchantment)
        elif ELevel == "Uncommon":
            EnchantmentChoice = random.randint(0, len(UncommonArmorEnchantments))
            Enchantment = UncommonArmorEnchantments[EnchantmentChoice]
            EDescription = ArmorEnchantmentDescriptionDictionary.get(Enchantment)
        elif ELevel == "Rare":
            EnchantmentChoice = random.randint(0, len(RareArmorEnchantments))
            Enchantment = RareArmorEnchantments[EnchantmentChoice]
            EDescription = ArmorEnchantmentDescriptionDictionary.get(Enchantment)
        elif ELevel == "Very Rare":
            EnchantmentChoice = random.randint(0, len(VeryRareArmorEnchantments))
            Enchantment = VeryRareArmorEnchantments[EnchantmentChoice]
            EDescription = ArmorEnchantmentDescriptionDictionary.get(Enchantment)
        elif ELevel == "Legendary":
            EnchantmentChoice = random.randint(0, len(LegendaryArmorEnchantments))
            Enchantment = LegendaryArmorEnchantments[EnchantmentChoice]
            EDescription = ArmorEnchantmentDescriptionDictionary.get(Enchantment)
            
        if MLevel == "Common":
            MaterialChoice = random.randint(0, len(CommonMaterials)-1)
            Material = CommonMaterials[MaterialChoice]
            MDescription = MaterialDescriptionDictionary.get(Material)
            MMechanic = MaterialArmorMechanicDictionary.get(Material)
        elif MLevel == "Uncommon":
            MaterialChoice = random.randint(0, len(UncommonMaterials)-1)
            Material = UncommonMaterials[MaterialChoice]
            MDescription = MaterialDescriptionDictionary.get(Material)
            MMechanic = MaterialArmorMechanicDictionary.get(Material)
        elif MLevel == "Rare":
            MaterialChoice = random.randint(0, len(RareMaterials)-1)
            Material = RareMaterials[MaterialChoice]
            MDescription = MaterialDescriptionDictionary.get(Material)
            MMechanic = MaterialArmorMechanicDictionary.get(Material)
        elif MLevel == "Very Rare":
            MaterialChoice = random.randint(0, len(VeryRareMaterials)-1)
            Material = VeryRareMaterials[MaterialChoice]
            MDescription = MaterialDescriptionDictionary.get(Material)
            MMechanic = MaterialArmorMechanicDictionary.get(Material)
        elif MLevel == "Legendary":
            MaterialChoice = random.randint(0, len(LegendaryMaterials)-1)
            Material = LegendaryMaterials[MaterialChoice]
            MDescription = MaterialDescriptionDictionary.get(Material)
            MMechanic = MaterialArmorMechanicDictionary.get(Material)
    
    return Enchantment, EDescription, MLevel, ELevel, RLevel, Material, MDescription, MMechanic, Item


sg.theme('DarkTanBlue')

Enchantment, EDescription, MLevel, ELevel, RLevel, Material, MDescription, MMechanic, Item = GenerateItem()

TextWrapSize = 60

if Enchantment == "":
    ItemName = str(RLevel + " " + Material + " " + Item)
    Enchantment = ""
else:
    ItemName = str(RLevel + " " + Material + " " + Item + " (" + Enchantment + ")")
    Enchantment = "\n".join(textwrap.wrap(f"{Enchantment}: {EDescription}", TextWrapSize))

font=("Arial", 12)

col1 = [[sg.Text(text = f"Material Rarity: {MLevel}", font=font, key= '-MRarity-')],
          [sg.Text(text= f"Enchantment Rarity: {ELevel}", font=font, key= '-ERarity-')],
          [sg.Text(text= f"Refinement Level: {RLevel}", font=font, key= '-RRarity-')]]
col2 = [[sg.Text(text = ItemName, font=font, key='-ITEMNAME-')],
          [sg.Text(text = "\n".join(textwrap.wrap(f"{Material}: {MDescription}", TextWrapSize)), key = '-MATERIAL-')],
          [sg.Text(text = "\n".join(textwrap.wrap(f"{Material} Material Mechanic: {MMechanic}", TextWrapSize)), key="-MMECHANIC-")],
          [sg.Text(text= Enchantment, key="-ENCHANTMENT-")]]
Enchantment, EDescription, MLevel, ELevel, RLevel, Material, MDescription, MMechanic, Item = GenerateItem()
col3 = [[sg.Text(text = f"Material Rarity: {MLevel}", font=font, key= '-MRarity2-')],
          [sg.Text(text= f"Enchantment Rarity: {ELevel}", font=font, key= '-ERarity2-')],
          [sg.Text(text= f"Refinement Level: {RLevel}", font=font, key= '-RRarity2-')]]
col4 = [[sg.Text(text = ItemName, font=font, key='-ITEMNAME2-')],
          [sg.Text(text = "\n".join(textwrap.wrap(f"{Material}: {MDescription}", TextWrapSize)), key = '-MATERIAL2-')],
          [sg.Text(text = "\n".join(textwrap.wrap(f"{Material} Material Mechanic: {MMechanic}", TextWrapSize)), key="-MMECHANIC2-")],
          [sg.Text(text= Enchantment, key="-ENCHANTMENT2-")]]


layout = [[sg.Text("Welcome to Nox's Weapon and Armor Generator for 5e!", font=("Arial", 15))],
          [sg.Text('-'*150)],
          [sg.Column(col1, element_justification='l'), sg.Column(col2, element_justification='l')], 
          [sg.Column(col3, element_justification='l'), sg.Column(col4, element_justification='l')],
          [sg.Text('-'*150)],
          [sg.Button("Settings"), sg.Push(), sg.Button("Update"), sg.Push(), sg.Button('Exit')]
          ]

# Create the window
window = sg.Window("Nox's Weapon Generator", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    if event == "Update":
        Enchantment, EDescription, MLevel, ELevel, RLevel, Material, MDescription, MMechanic, Item = GenerateItem()
        
        if Enchantment == "":
            ItemName = str(RLevel + " " + Material + " " + Item)
            Enchantment = ""
        else:
            ItemName = str(RLevel + " " + Material + " " + Item + " (" + Enchantment + ")")
            Enchantment = "\n".join(textwrap.wrap(f"{Enchantment}: {EDescription}", TextWrapSize))
        
        window['-ITEMNAME-'].update(ItemName)
        window['-MATERIAL-'].update("\n".join(textwrap.wrap(f"{Material}: {MDescription}", TextWrapSize)))
        window['-MMECHANIC-'].update("\n".join(textwrap.wrap(f"{Material} Material Mechanic: {MMechanic}", TextWrapSize)))
        window['-ENCHANTMENT-'].update(Enchantment)
    
        Enchantment, EDescription, MLevel, ELevel, RLevel, Material, MDescription, MMechanic, Item = GenerateItem()
        
        if Enchantment == "":
            ItemName = str(RLevel + " " + Material + " " + Item)
            Enchantment = ""
        else:
            ItemName = str(RLevel + " " + Material + " " + Item + " (" + Enchantment + ")")
            Enchantment = "\n".join(textwrap.wrap(f"{Enchantment}: {EDescription}", TextWrapSize))
        
        window['-ITEMNAME2-'].update(ItemName)
        window['-MATERIAL2-'].update("\n".join(textwrap.wrap(f"{Material}: {MDescription}", TextWrapSize)))
        window['-MMECHANIC2-'].update("\n".join(textwrap.wrap(f"{Material} Material Mechanic: {MMechanic}", TextWrapSize)))
        window['-ENCHANTMENT2-'].update(Enchantment)
        
    if event == "Settings":
        layout2 = [[sg.Text("Settings")],
                   [sg.Text('-'*100)],
                   [sg.Checkbox(text="Option 1", default= True, key= "key1", enable_events=True)],
                   ]
        Settings = sg.Window("Settings Page", layout2)
        
        while True:
            event, values = Settings.read()
            
            if  event == sg.WIN_CLOSED:
                break
            if event == "Option 1":
                if values['key1'] == True:
                    print('Checkbox Checked.')
                elif values['key1'] == False:
                    print('Checkbox Unchecked.')
        

window.close()

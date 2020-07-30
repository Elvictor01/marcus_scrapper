
text = open("boots.csv", "r")
text = ''.join([i for i in text]) \
    .replace(", ,$", "; ")
text = ''.join([i for i in text]) \
    .replace(",$", ";")
text = ''.join([i for i in text]) \
    .replace(" ;", ",")
text = ''.join([i for i in text]) \
    .replace("$", "")
text = ''.join([i for i in text]) \
    .replace(", ", " ")
x = open("output.csv", "w")
x.writelines(text)
x.close()

'''
import csv
import pandas as pd
import numpy as np

data = pd.read_csv("output.csv", sep=',')

data.head()
'''
#print(data.iloc[[0], [0]])

#price = data.iloc[[1], [0]]

#print(data.iloc[[0], [0]].split(";"))

#split_data = price.str.split(", ")

# data.values.apply("".join)
#data = split_data.to_list()
#names = ["price", "shoeBrand", "shoeName", "shoeType"]
#new_df = pd.DataFrame(data, columns=names)
# new_df.values.tolist()
#new_df[[0], [1]].apply("".join)
# print(new_df)

#price = data['price']

# pd.concat([data, pd.DataFrame(data[price].str.split(
#    ';').tolist(), columns=['newPrice'])], axis=1)

'''
with open('boots.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
'''
'''
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {"shoeType": ["Boots"], "shoeBrand": ["Saint Laurent", "Hunter Boot", "Alexander McQueen", "Aquatalia", "Aquatalia", "Aquatalia", "Tod's", "Saint Laurent", "Aquatalia", "Balenciaga", "Balenciaga", "Magnanni", "Magnanni", "Magnanni", "Saint Laurent", "Amiri", "Fear of God", "UGG", "Salvatore Ferragamo", "Saint Laurent", "Maison Margiela", "Balenciaga", "Maison Margiela", "Versace", "Aquatalia", "Aquatalia", "Eastland 1955 Edition", "Prada", "Wolverine", "John Varvatos", "Loro Piana", "Giorgio Armani", "Saint Laurent", "UGG", "Berluti", "Eastland", "Eastland", "Eastland", "Stefano Ricci", "Frye", "Aquatalia", "Lucchese", "Lucchese", "Amiri", "Bruno Magli", "Christian Louboutin", "John Varvatos", "Frye", "John Varvatos", "John Varvatos", "John Varvatos", "Ermenegildo Zegna", "Balmain", "Brunello Cucinelli", "Brunello Cucinelli", "Frye", "Bally", "John Varvatos", "John Varvatos", "Bruno Magli", "Fendi", "Ike Behar", "Ike Behar", "Salvatore Ferragamo", "UGG", "Vince", "UGG", "Vince", "Burberry", "Ermenegildo Zegna", "Ermenegildo Zegna", "Ermenegildo Zegna", "Manolo Blahnik", "Manolo Blahnik", "Hari Mari", "Frye", "Vince", "Cole Haan", "Ermenegildo Zegna", "Ermenegildo Zegna", "Fendi", "Fendi", "Moncler", "Burberry", "Bruno Magli", "Magnanni", "Gucci", "Saint Laurent", "Tod's", "Swims", "Swims", "Badgley Mischka", "Versace", "Prada", "John Varvatos", "John Varvatos", "John Varvatos", "John Varvatos", "Bruno Magli", "Maison Margiela", "Eastland", "Bally", "Alexander McQueen", "Alexander McQueen", "TOM FORD", "Amiri", "John Varvatos", "Eastland 1955 Edition", "UGG", "Salvatore Ferragamo", "Salvatore Ferragamo", "Alexander McQueen", "Balenciaga", "Salvatore Ferragamo", "Giuseppe Zanotti", "TOM FORD", "Giorgio Armani", "Magnanni", "Giorgio Armani", "Frye"], "shoeName": ["Men's Jodhpur Leather Ankle-Wrap Boots", "Men's Original Refined Chelsea Boot", "Men's Studded Leather Moto Boot", "Men's Adrian  Leather Dress Chelsea Boots", "Men's Daniel Waterproof Suede Side-Zip Ankle Boots", "Men's Rinaldo Suede Lace-Up Chukka Boots", "Men's Polacco Suede Chukka Boots", "Men's Wyatt Leopard-Print Harness Boots", "Men's Adrian Weatherproof Suede Chelsea Boot", "Men's Suede Santiag Booties", "Men's Santiag Western Harness Suede Booties", "Men's Double-Zip Leather Ankle Boots", "Men's Side-Zip Leather Ankle Boots", "Men's Suede Chelsea Boots", "Men's Clementi 40 Buckle-Strap Patent Leather Boots", "Men's Jodhpur Conch Suede Boots", "Men's Santa Fe Suede Chelsea Boots", "Men's Classic Short Suede Front-Zip Boots", "Men's Sachie-2 Suede Chukka Boots", "Men's Wyatt Suede Chukka Boots", "Men's Cross Shiny Faux-Leather Combat Boots", "Men's Biker Bootie", "Men's Tank Metallic Split-Toe Ankle Boots", "Men's Leopard Calf Hair Ankle Boots", "Men's Corbin Weatherproof Suede Derby Shoes", "Men's Rinaldo Weatherproof Suede Chukka Boot", "Sherman 1955 Leather Boots, Oak ", "Saffiano Leather Chelsea Boots, Black", "1000 Mile Boot", "Morrison Sharpei Suede Boot", "Men's Open Walk Suede Chukka Boot", "Men's Vachetta Leather/Suede Chelsea Boots", "Men's Lukas Western Suede Boots", "Men's Harkley Waterproof Leather Boots", "Men's Scritto Leather Chelsea Boots", "Men's Edison 1955 Leather Chelsea Boots", "Men's Edison 1955 Suede Chelsea Boots", "Men's Sherman 1955 Suede Boots", "Men's Leather Mountain Boots", "Men's Bowery Leather Lace-Up Boots", "Men's Vladimir Leather Boots",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   "Men's Grayson Leather Chelsea Boots (Made to Order)", "Men's Hudson Full Quill Boots (Made to Order)", "Men's Bandana Buckle Ankle Boots", "Men's Sancho Leather Ankle Boots", "Men's Kicko Leopard-Print Red Sole Boots", "Eldridge Leather Harness Boot", "Men's Paul Lace-Up Leather Boots", "Men's Waverly Covered Chelsea Boots", "Men's Waverly Covered Chelsea Boots", "Men's NYC Leather Ankle Boots", "Men's Siena Flex Burnished Leather Chelsea Boots", "Men's Calf Suede Zip-Up Ankle Boots", "Men's Brogue Leather Derby Boots", "Men's Suede Mid-Top Desert Chukka Boots", "Men's Grady Jodhpur Ankle Boots", "Men's Nikora Leather Chelsea Boots ", "Men's Union Leather Combat Boots", "Men's Fleetwood Velvet Lace-Up Boots", "Men's Savino Suede/Leather Derby Boots", "Men's Embroidered FF Logo Leather Chelsea Boots", "Men's Octavian Patina Leather Double-Monk Boots", "Men's Edge Two-Tone Patina Leather Balmoral Boots", "Men's Sefton Gancini Leather Side-Zip Ankle Boots", "Men's Neumel Flex Suede Booties w/ Wool Lining", "Men's Colter Moc-Toe Chukka Boots", "Men's Neumel Waterproof Full-Grain Leather Chukka Boots", "Men's Carmine Valencia Leather Chelsea Boots", "Men's Vintage Check/Leather Hiking Boots", "Men's Trivero Suede Chukka Boots with Mud Guard, Black", "Men's Trivero Suede Chukka Boots with Mud Guard, Blue", "Men's Trivero Suede Chukka Boots with Mud Guard, Brown", "Men's Rodrigo Suede Chukka Boots", "Men's Bodolomite Shearling-Trim Hiking Boots", "Men's Nokona CanyonTrek Leather/Hemp Chukka Boots", "Men's Leather Harness Moto Boots", "Men's Colter Suede Moc-Toe Chukka Boots", "Men's 2.ZeroGrand Stretch-Knit Chukka Boots", "Men's Leather Chelsea Boots", "Men's Trivero Suede Chukka Boots", "Men's Faded FF Leather Chelsea Boots", "Men's Faded FF Moc-Toe Leather Combat Boots", "Hayden Chelsea Leather Boots", "Men's Allostock Vintage Check Leather Chelsea Boots", "Men's Octavio Brogue Leather Boots", "Men's Peyton II Burnished Leather Lace-Up Boots", "Men's Leon Chunky Leather Chelsea Boots", "Suede Chukka Boot Espadrille", "Men's Polacco Suede Chukka Boots", "Men's Motion Country Boots", "Men's Motion Chukka Boots", "Men's William Star-Print Leather Ankle Boots", "Men's Leather Medusa Combat Boots", "Men's Nylon-Inset Leather Boots", "Men's Morrison Sharpei Laser Boots", "Men's Lewis Leather Chelsea Boots", "Men's Lewis Leather Side-Zip Boots", "Men's Lewis Python-Print Side-Zip Boots", "Men's Riccardo Woven Leather Boots", "Men's Tabi Split-Toe Leather Ankle Boots", "Men's Kurt 1955 Waterproof Leather Hiking Boots", "Men's Lug-Sole Leather Derby Shoes", "Men's Leather Chelsea Boots", "Men's Brogue Lace-Up Boot Sneakers", "Men's Formal Leather Side-Zip Ankle Boots", "Men's Suede Point-Toe Chelsea Boots", "Men's Six O Six Convertible Leather Combat Boots", "Sherman 1955 Leather Boot, Black", "Men's x Ovadia Classic Mini Leather Boots", "Men's Rubly Leather Hiking Boots", "Men's Rhino Leather Chelsea Boots", "Men's Leather Glitter Ankle Boots", "Men's Combat Boot with Woven Lace Detail", "Men's Rosco Lug-Sole Combat Boots", "Men's Suede Chelsea Boots w/ Clear Heel", "Men's Kensington Double-Monk Boots", "Men's Lightweight Suede Chukka Boots", "Men's Durham Leather Desert Boots", "Men's Lightweight Suede Chukka Boots", "Men's Bowery Leather Lace-Up Boots"], "price": ["$995", "$154", "NOW ", "$75", " ", "$1,579", "NOW ", "$740", " ", "$449", "NOW ", "$210", " ", "$524", "NOW ", "$245", " ", "$449", "NOW ", "$210", " ", "$524", "NOW ", "$245", " ", "$1,594", "NOW ", "$747", " ", "$449", "NOW ", "$210", " ", "$1,089", "NOW ", "$510", " ", "$1,389", "NOW ", "$651", " ", "$484", "NOW ", "$237", " ", "$484", "NOW ", "$227", " ", "$484", "NOW ", "$227", " ", "$995", "NOW ", "$466", " ", "$1,589", "NOW ", "$745", " ", "$794", "NOW ", "$372", " ", "$189", "NOW ", "$88", " ", "$574", "NOW ", "$269", " ", "$994", "NOW ", "$466", " ", "$1,524", "NOW ", "$715", " ", "$1,189", "NOW ", "$557", " ", "$1,294", "NOW ", "$607", " ", "$1,474", "NOW ", "$691", " ", "$549", "NOW ", "$257", " ", "$449", "NOW ", "$210", " ", "$225", "$750", "$385", "$698", "$995", "$1,195", "$995", "$190", "$2,350", "$160", "$160", "$225", "$1,150", "$358", "$595", "$695", "$645", "$1,390", "$495", "NOW ", "$295", " ", "$1,695", "$698", "$328", "$298", "$298", "$298", "$750", "$995", "$1,095", "$895", "NOW ", "$626", " ", "$398", "$695", "$698", "$698", "$650", "$990", "$995", "$995", "$1,190", "$130", "$375", "NOW ", "$262", " ", "$180", "$395", "NOW ", "$276", " ", "$890", "$650", "$650", "$650", "$825", "$1,295", "$220", "$358", "$262.50", "$250", "$950", "$650", "$990", "$890", "$625", "$680", "$650", "$398", "$980", "$395", "$545", "$300", "$249", "NOW ", "$122", " ", "$295", "$1,650", "$890", "$698", "$798", "$798", "$898", "$650", "$1,280", "$200", "$675", "$650", "$780", "$1,990", "$990", "$748", "$225", "$300", "$1,150", "$895", "$890", "$1,290", "NOW ", "$658", " ", "$895", "$1,250", "$1,250", "$745", "$395", "$745", "$298"]},
)
lst_col = 'price'

r = pd.DataFrame({
    col: np.repeat(df[col].values, df[lst_col].str.len())
    for col in df.columns.drop(lst_col)}
).assign(**{lst_col: np.concatenate(df[lst_col].values)})[df.columns]
print(df[list_col)
'''

table = """
Airplane       & (10, 55)       & Apple          & (11, 28)       & Ball           & (25, 83)       \\
Banana         & (13, 156)      & Bat            & (13, 60)       & Bed            & (14, 95)       \\
Bee            & (13, 61)       & Beluga Whale   & (11, 27)       & Bicycle        & (11, 117)      \\
Bird           & (16, 115)      & Boat           & (18, 19)       & Book           & (12, 73)       \\
Bottle         & (11, 137)      & Camel          & (10, 109)      & Camera         & (12, 219)      \\
Car            & (25, 106)      & Cat            & (22, 142)      & Chair          & (12, 117)      \\
Clover         & (10, 23)       & Crab           & (10, 321)      & Cup            & (15, 380)      \\
Dinosaur       & (20, 184)      & Dog            & (21, 119)      & Door           & (13, 299)      \\
Duck           & (12, 399)      & Egg            & (17, 87)       & Elephant       & (20, 29)       \\
Fish           & (30, 130)      & Flower         & (13, 72)       & Fox            & (13, 163)      \\
Giraffe        & (12, 12)       & Glasses        & (12, 44)       & Guitar         & (18, 70)       \\
Hammer         & (19, 133)      & Hat            & (12, 73)       & Headphones     & (11, 53)       \\
Helicopter     & (102, 35)      & Horse          & (23, 93)       & Hut            & (10, 226)      \\
Iron           & (10, 110)      & Jellyfish      & (9, 21)        & Lamp           & (10, 38)       \\
Laptop         & (11, 153)      & Leaf           & (11, 127)      & Llama          & (10, 137)      \\
Motorcycle     & (14, 161)      & Pencil         & (19, 85)       & Penguin        & (12, 149)      \\
Planet         & (12, 36)       & Rabbit         & (10, 205)      & Ring           & (10, 17)       \\
Rocket         & (23, 84)       & Satellite      & (10, 49)       & School Backpack & (12, 24)      \\
Scooty         & (12, 46)       & Ship           & (13, 13)       & Shirt          & (21, 152)      \\
Shoe           & (18, 207)      & Snowflake      & (11, 56)       & Soda Cans      & (12, 35)       \\
Spoon          & (10, 25)       & Teddy Bear     & (16, 39)       & Train          & (18, 202)      \\
Tree           & (22, 107)      & Watch          & (11, 83)       & Umbrella       & (10, 25)       \\"""

rows = table.split("\\")

for row in rows:
    html_row = '<tr class="text-center border">'
    # Remove leading/trailing whitespace and backslashes
    cleaned_row = row.strip().replace("\\", "")
    
    # Split the row into columns
    columns = cleaned_row.split("&")
    
    # Clean each column and print it
    cleaned_columns = [col.strip() for col in columns]
    
    # Create HTML table cells
    for col in cleaned_columns:
        html_row += f"<td>{col}</td>"
    html_row += "</tr>"

    # Print the HTML row
    print(html_row)


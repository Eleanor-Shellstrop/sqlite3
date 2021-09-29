import csv
import pandas as pd
import sqlite3


# Connect to database file
connection = sqlite3.connect('inventory.db')


# Make the cursor
c = connection.cursor()


# Create a table
# c.execute("""CREATE TABLE yarns(
#     brand_name text, 
#     collection_name text,
#     color_name text,
#     dye_lot integer,
#     package_type text,
#     amount_in_inventory integer,
#     purchased_at text,
#     price integer,
#     length_yds integer,
#     yarn_weight integer,
#     weight_grams integer,
#     weight_oz integer,
#     gauge_needle_size text,
#     gauge_knit text,
#     gauge_hook_size text,
#     gauge_crochet text,
#     fiber_type text,
#     fiber_care text
#     )
# """)

# Insert info into table
# c.execute("""INSERT INTO yarns VALUES (
#     'Lion Brand',
#     'Wool Ease',
#     'Forest Green Heather',
#     634838,
#     'skein',
#     4,
#     'JOANN Fabric and Craft',
#     7, 
#     197,
#     4,
#     85,
#     3,
#     '8 (5mm)',
#     '18 s, 24 r',
#     'J-10 (6mm)',
#     '13.2 s, 16r',
#     '80% Acrylic, 20% Wool',
#     'Washine wash cold or warm, tumble dry, do not iron, do not use bleach, dry clean any'
# )""")

# cursor = c.execute("SELECT * FROM yarns")
# print(c.fetchall())

# colnames = cursor.description
# for row in colnames:
#     print(row[0])


#Import csv with pandas
new_yarn = pd.read_csv('yarn_data.csv')
new_yarn.to_sql('yarns', connection, if_exists='append', index=False)


# Test results
print(c.execute('''SELECT * FROM yarns''').fetchall())

connection.commit()


connection.close()
import sqlite3


# Write database file
connection = sqlite3.connect('inventory.db')


# Make the cursor
c = connection.cursor()


# Create a table
c.execute("""CREATE TABLE yarns(
    brand_name text, 
    collection_name text,
    color_name text,
    dye_lot integer,
    package_type text,
    amount_in_inventory integer,
    purchased_at text,
    price integer,
    length_yds integer,
    weight_grams integer,
    weight_oz integer,
    gauge_needle_size text,
    gauge_knit text,
    gauge_hook_size text
    gauge_crochet text,
    fiber_type text,
    fiber_care text
    )
""")


connection.commit()


connection.close()
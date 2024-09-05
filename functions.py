
#most valuble diamond
def highest_price(df):
    print(f"The most valuable diamond is priced at: {df['price'].max()}$")

#average of diamond price
def average_price(df):
    print(f"The average price of a diamond is: {df['price'].mean()}")

#count of ideal
def count_ideal(df):
    print(f"the number of ideal diamonds is {df[df['cut'] == 'Ideal'].shape[0]}")

# average price for diffrent colors
def color_counter(df):
    print(f"there are {len(df['color'].unique())} different colors, which are:")
    print(", ".join(df['color'].unique()))
    
# Median of diamond carat
def median_carat(df):
    print(f"The median carat of the diamonds is: {df['carat'].median()}")

#average price for color
def average_carat_per_cut(df): 
    print("avrage carat per each cut:")
    print(", ".join([f"{cut}: {carat:.2f}" for cut, carat in df.groupby('cut')['carat'].mean().items()]))


#avrage price for color
def average_price_per_color(df): 
    print("Average price per each color:")
    print(", ".join([f"{color}: ${price:.2f}" for color, price in df.groupby('color')['price'].mean().items()]))
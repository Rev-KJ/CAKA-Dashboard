import pandas as pd

# Read the data
data = pd.read_excel("sunday_data.xlsx")

# Drop rows with NaN values in the Basket column
data = data.dropna(subset=["Basket"])

def remove_punctuation(basket):
    basket = str(basket)
    basket = basket.replace("[", "")
    basket = basket.replace("]", "")
    basket = basket.replace("'", "")
    return basket

data["Basket"] = data["Basket"].apply(remove_punctuation)

def split_basket(basket_str):
    elements = basket_str.split(',')
    stripped_elements = [e.strip() for e in elements]
    return stripped_elements

data["Basket"] = data["Basket"].apply(split_basket)

data = data.explode("Basket", ignore_index=False)

# Count the occurrences of each item
item_counts = data["Basket"].value_counts()

print(item_counts)

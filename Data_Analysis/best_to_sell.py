import pandas as pd

organizations = pd.read_csv('Erste_Datasets/Organizations.csv')
receipts = pd.read_csv('Erste_Datasets/Receipts.csv')
products = pd.read_csv('Erste_Datasets/Products.csv')
product_categories = pd.read_csv('Erste_Datasets/ProductCategories.csv')
product_items = pd.read_csv('Erste_Datasets/ProductItems.csv')


# print(products['category'].unique())


def get_low_cost_best_sell(organization_name):
    # Get items under 3EUR
    organization_id = organizations.loc[organizations['name'] == organization_name, 'id'].iloc[0]

    # Filter products by price and the organization_id
    low_cost_items = products[(products['price'] < 3) & (products['organization_id'] == organization_id)]

    # Filter products to selected categories
    selected_categories = ['snacks/salty', 'snacks/sweet', 'pastry/basic', 'pastry/sweet', 'pastry/salty', 'drinks/non-alcoholic', 'drinks/juice', 'drinks/non-alcoholic-beer', 'health/medical-supplies', 'health/vitamins-ointments', 'seasonal', 'basic/tea-coffee-soups', 'drugstore/dental', 'fashion/accessories', 'dairy/yoghurts', 'frozen/sweet']

    return low_cost_items[low_cost_items['category'].isin(selected_categories)]


# print('Low cost best sell items for BILLA s.r.o.:')
# print(get_low_cost_best_sell('BILLA s.r.o.'))

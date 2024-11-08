import pandas as pd

organizations = pd.read_csv('Erste_Datasets/Organizations.csv')
receipts = pd.read_csv('Erste_Datasets/Receipts.csv')
products = pd.read_csv('Erste_Datasets/Products.csv')
product_categories = pd.read_csv('Erste_Datasets/ProductCategories.csv')
product_items = pd.read_csv('Erste_Datasets/ProductItems.csv')


def get_receipts_by_organization(organization_name):
    return receipts[receipts['org_name'] == organization_name]


def get_list_of_popular_products(organization_name):
    # Get receipts for the specified organization
    receipts_by_organization = get_receipts_by_organization(organization_name)

    # Filter product items for the organization’s receipts
    filtered_product_items = product_items[product_items['fs_receipt_id'].isin(receipts_by_organization['id'])]

    # Merge product_items with products to get product names and details
    merged_data = pd.merge(
        filtered_product_items,
        products,
        left_on='product_id',
        right_on='id',
        how='left'
    )

    # Merge all Z items
    merged_data = merged_data[~merged_data['item_type'].str.startswith('Z', na=False)]

    # Group by product name and calculate total quantity sold
    total_sales = merged_data.groupby(['name', 'category'])['quantity'].sum().reset_index()

    # Sort by total quantity sold in descending order
    total_sales = total_sales.sort_values(by='quantity', ascending=False).reset_index(drop=True)

    return total_sales


def get_popular_categories(organization_name):
    # Get list of popular items
    popular_items = get_list_of_popular_products(organization_name)

    # Group by category and calculate total quantity sold
    category_sales = popular_items.groupby('category')['quantity'].sum().reset_index()

    # Sort by quantity in descending order
    return category_sales.sort_values(by='quantity', ascending=False).reset_index(drop=True)


# print('Popular items sales for BILLA s.r.o.:')
# print(get_list_of_popular_products('Kaufland Slovenská republika v.o.s.'))
#
#
# print('Popular categories for BILLA s.r.o.:')
# print(get_popular_categories('BILLA s.r.o.'))


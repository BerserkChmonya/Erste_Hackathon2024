import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

organizations_df = pd.read_csv('Erste_Datasets/Organizations.csv')
product_items_df = pd.read_csv('Erste_Datasets/ProductItems.csv')
products_df = pd.read_csv('Erste_Datasets/Products.csv')
receipts_df = pd.read_csv('Erste_Datasets/Receipts.csv')

product_items_df = product_items_df.rename(columns={'fs_receipt_id': 'receipt_id'})
store_names_map = organizations_df.set_index('id')['name'].to_dict()
item_names_with_receipts = pd.merge(
    product_items_df[['receipt_id', 'product_id']],
    products_df[['id', 'name']],
    left_on='product_id',
    right_on='id',
    how='left'
).rename(columns={'name': 'item_name'})

item_names_with_receipts = pd.merge(
    item_names_with_receipts,
    receipts_df[['id', 'organization_id', 'created_date']],
    left_on='receipt_id',
    right_on='id',
    how='left'
)
item_names_with_receipts['organization_name'] = item_names_with_receipts['organization_id'].map(store_names_map)
lidl_sales_data = item_names_with_receipts[
    item_names_with_receipts['organization_name'] == "Lidl Slovenská republika, s.r.o."]
lidl_sales_data['created_date'] = pd.to_datetime(lidl_sales_data['created_date'])

monthly_sales = (lidl_sales_data
                 .groupby([lidl_sales_data['created_date'].dt.to_period("M"), 'item_name'])
                 .size()
                 .unstack(fill_value=0))

top_10_items = monthly_sales.sum().nlargest(10).index
monthly_sales = monthly_sales[top_10_items]
monthly_sales.index = monthly_sales.index.to_timestamp()

for item in top_10_items:
    df = monthly_sales[[item]].reset_index()
    df.columns = ['ds', 'y']

    model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    model.fit(df)

    future = model.make_future_dataframe(periods=12, freq='M')
    forecast = model.predict(future)

    forecast['yhat'] = forecast['yhat'].apply(lambda x: max(x, 0))
    forecast['yhat_lower'] = forecast['yhat_lower'].apply(lambda x: max(x, 0))
    forecast['yhat_upper'] = forecast['yhat_upper'].apply(lambda x: max(x, 0))

    plt.figure(figsize=(10, 6))

    plt.plot(df['ds'], df['y'], color='blue', label='Historical Sales')

    forecast_data = forecast[forecast['ds'] >= df['ds'].max()]
    plt.plot(forecast_data['ds'], forecast_data['yhat'], color='red', label='Forecasted Sales')
    plt.fill_between(forecast_data['ds'], forecast_data['yhat_lower'], forecast_data['yhat_upper'], color='red',
                     alpha=0.3)

    plt.axvline(x=df['ds'].max(), color='gray', linestyle='--')

    plt.title(f"Sales Forecast for {item} in 2025")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.show()

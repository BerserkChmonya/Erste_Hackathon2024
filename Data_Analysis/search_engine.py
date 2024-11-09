import pandas as pd

# Load the CSV file with company data
df = pd.read_csv('Erste_Datasets/Organizations.csv')

# Select only the 'name' column
df = df['name']


def search_companies(query):
    # Convert the query to lowercase for case-insensitive search
    query = query.lower()

    # Use str.contains to search for the query in the 'name' column
    result = df[df.str.contains(query, case=False, na=False)]

    # Return the result (filtered rows)
    return result


# Example: User input for search query
query = input("Enter search term: ")

# Perform the search
results = search_companies(query)

# Display the results
if not results.empty:
    print("Search Results:")
    print(results)
else:
    print("No results found.")


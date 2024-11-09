"""
Tento skript identifikuje 10 najčastejšie nakupovaných dvojíc položiek v predajni Lidl Slovenská republika, s.r.o.
Analýza je založená na údajoch z pokladničných blokov (receipts), pričom dáta z Lidlu sú použité, pretože z tohto obchodu
máme najviac dostupných blokov, čo poskytuje najreprezentatívnejšiu vzorku.

Postup:
1. Načíta údaje z CSV súborov vrátane informácií o organizáciách (obchodoch), položkách produktov, produktoch a pokladničných blokoch.
2. Spojí údaje o produktoch a pokladničných blokoch, aby každá položka obsahovala aj názov produktu a obchod, v ktorom bola zakúpená.
3. Filtrovanie transakcií na predajňu Lidl Slovenská republika, s.r.o.
4. Identifikácia dvojíc položiek zakúpených spoločne v každej transakcii (pokladničnom bloku).
5. Spočíta výskyt každej dvojice a poskytne výstup s 10 najčastejšie zakúpenými dvojicami.

Využitie:
Výsledky tejto analýzy môžu organizácii pomôcť pri vytváraní cielených zľavových kupónov na dvojice produktov, ktoré môžu zvýšiť predaj.
Analýza je navrhnutá na zvýšenie efektivity propagácie v obchodoch na Slovensku, na základe reálnych nákupných údajov.

Požiadavky:
- Pandas knižnica na spracovanie údajov
- Knižnica collections na počítanie dvojíc položiek

Použitie:
Skript spustite po aktualizovaní cesty k súborom CSV.

Autor: Andrii Kostiushko
Dátum: 08.11.2024
"""

import pandas as pd
from itertools import combinations
from collections import Counter
import matplotlib.pyplot as plt

# Load data
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
    receipts_df[['id', 'organization_id']],
    left_on='receipt_id',
    right_on='id',
    how='left'
)

item_names_with_receipts['organization_name'] = item_names_with_receipts['organization_id'].map(store_names_map)

lidl_data = item_names_with_receipts[item_names_with_receipts['organization_name'] == "Lidl Slovenská republika, s.r.o."]

pairs = []
for receipt_id, group in lidl_data.groupby('receipt_id'):
    items = group['item_name'].tolist()
    pairs.extend(combinations(sorted(items), 2))

pair_counts = Counter(pairs)
top_10_pairs = pair_counts.most_common(10)

total_lidl_receipts = lidl_data['receipt_id'].nunique()

items = [f"{item1.strip()} & {item2.strip()}" for (item1, item2), _ in top_10_pairs]
counts = [count for _, count in top_10_pairs]
percentages = [(count / total_lidl_receipts) * 100 for count in counts]

plt.figure(figsize=(12, 8))
bars = plt.barh(items, counts, color='skyblue')
plt.xlabel("Frequency")
plt.title("Top 10 Most Frequently Purchased Item Pairs in Lidl Slovenská republika, s.r.o.")
plt.gca().invert_yaxis()

for bar, percent in zip(bars, percentages):
    plt.text(
        bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
        f"{percent:.1f}%", va='center'
    )

plt.xticks(fontsize=10)
plt.yticks(fontsize=9)
plt.tight_layout()
plt.show()

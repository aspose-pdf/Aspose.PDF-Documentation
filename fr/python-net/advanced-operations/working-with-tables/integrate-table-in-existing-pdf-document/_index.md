---
title: Intégrer le tableau avec les sources de données PDF
linktitle: Intégrer le tableau
type: docs
weight: 30
url: /fr/python-net/integrate-table/
description: Cet article montre comment intégrer des tableaux PDF. Intégrer le tableau avec la base de données et déterminer si le tableau se scindera sur la page actuelle.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Créer un PDF à partir d'un DataFrame

La fonction 'create_pdf_from_dataframe' prend un DataFrame et le convertit en tableau dans un nouveau PDF. Elle crée un nouveau document PDF, ajoute une page, génère un tableau à partir du DataFrame (en utilisant une méthode d'assistance), et enregistre le résultat dans le chemin de fichier indiqué. Et ce n’est pas seulement possible, c’est très facile.

1. Initialise un document PDF vide avec 'ap.Document()'.
1. La fonction 'self.create_table_from_dataframe(df, max_rows)' transforme le DataFrame en un objet tableau Aspose.PDF.
1. Insère le tableau dans la page PDF. Ajoute le tableau généré au contenu de la première page (page.paragraphs.add(table)).
1. Enregistre le document PDF.

```python

from os import path
import pandas as pd
import aspose.pdf as ap

# Example DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
})

max_rows = 3  # Number of rows to include in the table
path_outfile = "output.pdf"

# Define the function to create a table from DataFrame
def create_table_from_dataframe(df, max_rows):
    table = ap.Table()
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )
    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray
    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))
    return table

# Load source PDF document
document = ap.Document()
page = document.pages.add()

table = create_table_from_dataframe(df, max_rows)

# Add table object to first page of input document
page.paragraphs.add(table)
document.save(path_outfile)
```

## Créer un tableau à partir d'un DataFrame

Ce code convertit le DataFrame en objet Table Aspose.PDF. Il configure les bordures du tableau, ajoute une ligne d’en-tête avec les noms de colonnes, et remplit le tableau avec les premières lignes max_rows du DataFrame. Le tableau résultant peut ensuite être ajouté à un document PDF.

1. Crée un objet 'ap.Table()' vide.
1. Définit les bordures du tableau.
1. Définit la bordure par défaut des cellules.
1. Ajoute une ligne d’en-tête.
1. Ajoute les lignes de données.
1. Retourne le tableau.

```python

    from os import path
    import pandas as pd
    import aspose.pdf as ap

    
    table = ap.Table()  # Initializes a new instance of the Table
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = (
        False  # Prevent header row from being split across pages
    )
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray

    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))

    return table
```

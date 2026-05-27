---
title: Intégrer des tables PDF avec des sources de données en Python
linktitle: Intégrer la table
type: docs
weight: 30
url: /fr/python-net/integrate-table/
description: Apprenez comment intégrer des tables PDF avec des sources de données telles que des bases de données et des pandas DataFrames en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Intégrer des tables PDF avec des bases de données et des DataFrames en utilisant Python
Abstract: Cet article explique comment intégrer des tables PDF avec des sources de données externes en utilisant Aspose.PDF for Python via .NET. Apprenez comment créer des tables PDF à partir de pandas DataFrames et d'autres sources structurées, les insérer dans des documents, et contrôler le flux des tables lors du rendu sur plusieurs pages PDF en Python.
---

## Créer un PDF à partir d'un DataFrame

Le `create_pdf_from_dataframe` La fonction crée un nouveau PDF et insère un tableau généré à partir d'un DataFrame pandas. Cette approche est utile pour les flux de travail de reporting où vos données existent déjà sous forme tabulaire.

La fonction effectue les étapes suivantes :

1. Créer un document PDF vide avec `ap.Document()`.
1. Ajoutez une page au document.
1. Convertir le DataFrame en tableau Aspose.PDF en appelant `create_table_from_dataframe(df, max_rows)`.
1. Ajouter le tableau à la page avec `page.paragraphs.add(table)`.
1. Enregistrez le PDF dans le chemin de sortie.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_pdf_from_dataframe(
    outfile: str, df: pd.DataFrame, max_rows: int = 20
) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    table = create_table_from_dataframe(df, max_rows)

    # Add table object to first page of input document
    page.paragraphs.add(table)
    document.save(outfile)
```

## Créer une Table à partir d'un DataFrame

Le `create_table_from_dataframe` fonction convertit un DataFrame en Aspose.PDF `Table` objet que vous pouvez ajouter à n'importe quelle page.

Il fait le suivant :

1. Créer un vide `ap.Table()` instance.
1. Définir les bordures de la table et des cellules pour un formatage cohérent.
1. Ajouter une ligne d’en-tête en utilisant les noms de colonnes du DataFrame.
1. Ajouter des lignes de données depuis `df.head(max_rows)`.
1. Retourner l’objet table rempli.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_table_from_dataframe(df: pd.DataFrame, max_rows: int = 20) -> ap.Table:
    """Create an Aspose.PDF table from a pandas DataFrame."""
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False  # Prevent header row from being split across pages
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

## Sujets liés à la table

- [Travailler avec des tableaux dans les PDF en Python](/pdf/fr/python-net/working-with-tables/)
- [Ajouter des tables au PDF avec Python](/pdf/fr/python-net/adding-tables/)
- [Extraire les tableaux des documents PDF](/pdf/fr/python-net/extracting-table/)
- [Manipuler les tableaux dans des PDF existants](/pdf/fr/python-net/manipulating-tables/)
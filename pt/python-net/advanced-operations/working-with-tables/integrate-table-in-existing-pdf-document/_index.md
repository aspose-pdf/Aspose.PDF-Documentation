---
title: Integrar Tabela com Fontes de Dados PDF
linktitle: Integrar Tabela
type: docs
weight: 30
url: /pt/python-net/integrate-table/
description: Este artigo mostra como integrar tabelas PDF. Integrar Tabela com Banco de Dados e determinar se a tabela será dividida na página atual.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Criar PDF a partir de DataFrame

A função 'create_pdf_from_dataframe' recebe um DataFrame e o converte em uma tabela dentro de um novo PDF. Ela cria um documento PDF novo, adiciona uma página, gera uma tabela a partir do DataFrame (usando um método auxiliar) e salva o resultado no caminho de arquivo fornecido. E não é apenas possível, mas muito fácil.

1. Inicializa um documento PDF vazio com 'ap.Document()'.
1. A função 'self.create_table_from_dataframe(df, max_rows)' transforma o DataFrame em um objeto de tabela Aspose.PDF.
1. Insere a tabela na página PDF. Adiciona a tabela gerada ao conteúdo da primeira página (page.paragraphs.add(table)).
1. Salva o documento PDF.

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

## Criar Tabela a partir de DataFrame

Este código converte o DataFrame em um objeto Table do Aspose.PDF. Ele configura as bordas da tabela, adiciona uma linha de cabeçalho com os nomes das colunas e preenche a tabela com as primeiras max_rows linhas do DataFrame. A Tabela resultante pode então ser adicionada a um documento PDF.

1. Cria um objeto 'ap.Table()' vazio.
1. Define a borda da tabela.
1. Define a borda padrão das células.
1. Adiciona a linha de cabeçalho.
1. Adiciona linhas de dados.
1. Retorna a tabela.

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

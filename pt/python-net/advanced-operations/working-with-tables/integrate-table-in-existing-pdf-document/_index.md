---
title: Integrar Tabelas PDF com Fontes de Dados em Python
linktitle: Integrar Tabela
type: docs
weight: 30
url: /pt/python-net/integrate-table/
description: Saiba como integrar tabelas PDF com fontes de dados, como bancos de dados e pandas DataFrames, em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Integrar tabelas PDF com bancos de dados e DataFrames usando Python
Abstract: Este artigo explica como integrar tabelas PDF com fontes de dados externas usando Aspose.PDF for Python via .NET. Aprenda a criar tabelas PDF a partir de pandas DataFrames e outras fontes estruturadas, inseri‑las em documentos e controlar o fluxo da tabela ao renderizar em várias páginas PDF em Python.
---

## Criar PDF a partir de DataFrame

O `create_pdf_from_dataframe` A função cria um novo PDF e insere uma tabela gerada a partir de um DataFrame do pandas. Essa abordagem é útil para fluxos de trabalho de relatórios onde seus dados já existem em formato tabular.

A função executa as seguintes etapas:

1. Crie um documento PDF vazio com `ap.Document()`.
1. Adicione uma página ao documento.
1. Converta o DataFrame em uma tabela Aspose.PDF chamando `create_table_from_dataframe(df, max_rows)`.
1. Adicionar a tabela à página com `page.paragraphs.add(table)`.
1. Salvar o PDF no caminho de saída.

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

## Criar Tabela a partir de DataFrame

O `create_table_from_dataframe` função converte um DataFrame em um Aspose.PDF `Table` objeto que você pode adicionar a qualquer página.

Ele faz o seguinte:

1. Criar um vazio `ap.Table()` instância.
1. Defina bordas de tabela e célula para formatação consistente.
1. Adicione uma linha de cabeçalho usando os nomes das colunas do DataFrame.
1. Adicionar linhas de dados de `df.head(max_rows)`.
1. Retorne o objeto de tabela preenchido.

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

## Tópicos Relacionados à Tabela

- [Trabalhe com tabelas em PDF usando Python](/pdf/pt/python-net/working-with-tables/)
- [Adicionar tabelas ao PDF usando Python](/pdf/pt/python-net/adding-tables/)
- [Extrair tabelas de documentos PDF](/pdf/pt/python-net/extracting-table/)
- [Manipular tabelas em PDFs existentes](/pdf/pt/python-net/manipulating-tables/)
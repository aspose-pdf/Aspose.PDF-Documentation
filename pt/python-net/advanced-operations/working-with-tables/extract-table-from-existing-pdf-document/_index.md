---
title: Extrair tabelas de PDF em Python
linktitle: Extrair tabela
type: docs
weight: 20
url: /pt/python-net/extracting-table/
description: Aprenda como extrair dados de tabela de documentos PDF existentes em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair dados de tabela de arquivos PDF com Python
Abstract: Este artigo explica como extrair tabelas de documentos PDF usando Aspose.PDF for Python via .NET. Ele mostra como usar `TableAbsorber` para detectar tabelas por página, iterar linhas e células e recuperar o texto das células para análise e processamento de dados a jusante.
---

## Extrair tabela de PDF

Extrair tabelas de PDFs é útil para geração de relatórios, migração de dados e fluxos de trabalho analíticos. Com Aspose.PDF for Python via .NET, você pode detectar e ler o conteúdo de tabelas de documentos PDF existentes de forma eficiente.

Este trecho de código abre um arquivo PDF existente, verifica cada página em busca de tabelas e extrai o conteúdo de texto das células. Ele usa `TableAbsorber` para detectar tabelas e então iterar pelas linhas e células para imprimir o texto extraído.

1. Carrega o PDF em um objeto ap.Document.
1. Itera pelas páginas.
1. Cria um objeto TableAbsorber.
1. Itera pelas tabelas.
1. Iterar através de linhas e células.
1. Extrair e imprimir texto das células.

Este exemplo lê um PDF, encontra todas as tabelas e imprime o conteúdo das células linha por linha.

```python
import aspose.pdf as ap
from os import path
import sys

def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)
```

## Tópicos Relacionados à Tabela

- [Trabalhar com tabelas em PDF usando Python](/pdf/pt/python-net/working-with-tables/)
- [Adicionar tabelas ao PDF usando Python](/pdf/pt/python-net/adding-tables/)
- [Integrar tabelas PDF com fontes de dados](/pdf/pt/python-net/integrate-table/)
- [Remover tabelas de PDFs existentes](/pdf/pt/python-net/removing-tables/)
---
title: Remover Tabelas de Documentos PDF Existentes
linktitle: Remover Tabelas
description: Aprenda como remover uma ou mais tabelas de documentos PDF existentes em Python.
lastmod: "2026-05-20"
type: docs
weight: 50
url: /pt/python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Excluir uma ou várias tabelas de arquivos PDF com Python
Abstract: Este artigo explica como remover tabelas de documentos PDF existentes usando Aspose.PDF for Python via .NET. Ele apresenta `TableAbsorber` para localizar tabelas e demonstra como excluir uma única tabela ou remover todas as tabelas detectadas de uma página.
---

## Remover Tabela de documento PDF

Aspose.PDF for Python permite que você remova uma tabela de um PDF. Ele abre um PDF existente, detecta a primeira tabela na primeira página com `TableAbsorber`, exclui essa tabela usando `remove()`, e salva o PDF atualizado em um novo arquivo.

Use esta página quando precisar limpar PDFs com muitas tabelas, remover conteúdo tabular desatualizado ou simplificar documentos antes da redistribuição.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## Remover todas as Tabelas do documento PDF

Com nossa biblioteca, você pode remover todas as tabelas de uma página específica em um PDF. O código abre um PDF existente, detecta todas as tabelas na segunda página com TableAbsorber, itera pelas tabelas detectadas, remove cada uma e, em seguida, salva o PDF modificado em um novo arquivo. É útil quando você precisa remover em massa tabelas de uma página enquanto mantém o restante do conteúdo do PDF intacto.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## Tópicos Relacionados à Tabela

- [Trabalhar com tabelas em PDF usando Python](/pdf/pt/python-net/working-with-tables/)
- [Adicionar tabelas ao PDF usando Python](/pdf/pt/python-net/adding-tables/)
- [Extrair tabelas de documentos PDF](/pdf/pt/python-net/extracting-table/)
- [Manipular tabelas em PDFs existentes](/pdf/pt/python-net/manipulating-tables/)
---
title: Manipular Tabelas em Documentos PDF Existentes
linktitle: Manipular Tabelas
type: docs
weight: 40
url: /pt/python-net/manipulating-tables/
description: Aprenda como inspecionar e modificar tabelas em documentos PDF existentes usando Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspecione e modifique tabelas PDF existentes com Python
Abstract: Este artigo explica como manipular tabelas já presentes em documentos PDF usando Aspose.PDF for Python via .NET. Aprenda como localizar tabelas com TableAbsorber, acessar linhas e células específicas, atualizar o conteúdo de texto da tabela e salvar o PDF modificado em Python.
---

## Manipular Tabelas em PDF Existente

Aspose.PDF for Python via .NET permite que você atualize tabelas que já existem em um documento PDF. Você pode usar o [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) classe para encontrar tabelas em uma página, acessar linhas e células, alterar o conteúdo de texto e salvar o arquivo atualizado.

Use esta página quando precisar atualizar o conteúdo de tabelas existentes em PDFs sem recriar o layout completo do documento.

## Localizar e Substituir Texto em Células de Tabela PDF

Este exemplo encontra a primeira tabela na página 1, acessa a primeira célula, substitui seu texto e salva o PDF de saída.

1. Abra o PDF de entrada.
1. Crie um TableAbsorber e visite a página 1.
1. Certifique‑se de que pelo menos uma tabela seja detectada.
1. Acesse a primeira célula na primeira linha da primeira tabela.
1. Certifique‑se de que a célula contenha fragmentos de texto e, em seguida, atualize o primeiro fragmento.
1. Salve o PDF modificado.

```python
import aspose.pdf as ap

def replace_cell_text(infile: str, outfile: str) -> None:
    """Replace text in the first cell of the first detected table."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    first_cell = absorber.table_list[0].row_list[0].cell_list[0]
    if len(first_cell.text_fragments) == 0:
        raise ValueError("The target cell has no text fragments.")

    # Change text of the first text fragment in the cell
    first_cell.text_fragments[0].text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## Substituir uma Tabela Existente por uma Nova Tabela

Você também pode substituir uma tabela detectada por uma recém-criada. Essa abordagem é útil quando tanto a estrutura quanto o conteúdo precisam ser alterados.

O código abaixo abre um PDF, encontra a primeira tabela na página 1, cria uma tabela de substituição, troca a tabela antiga pela nova e salva o resultado.

```python
import aspose.pdf as ap

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    # Get first table on the page
    old_table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the old table with the new one
    absorber.replace(document.pages[1], old_table, new_table)

    # Save PDF document
    document.save(outfile)
```

## Tópicos Relacionados à Tabela

- [Trabalhe com tabelas em PDF usando Python](/pdf/pt/python-net/working-with-tables/)
- [Adicionar tabelas ao PDF usando Python](/pdf/pt/python-net/adding-tables/)
- [Extrair tabelas de documentos PDF](/pdf/pt/python-net/extracting-table/)
- [Remover tabelas de PDFs existentes](/pdf/pt/python-net/removing-tables/)

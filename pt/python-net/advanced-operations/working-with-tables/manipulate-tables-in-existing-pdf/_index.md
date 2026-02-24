---
title: Manipular Tabelas em PDF existente
linktitle: Manipular Tabelas
type: docs
weight: 40
url: /pt/python-net/manipulating-tables/
description: Aprenda como trabalhar com tabelas em PDFs existentes usando Aspose.PDF para Python via .NET, oferecendo flexibilidade na modificação de documentos.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Manipular Tabelas em PDF existente

Aspose.PDF para Python demonstra como modificar o conteúdo de uma célula específica dentro de uma tabela em um documento PDF. Ele utiliza a classe TableAbsorber para localizar tabelas na primeira página, acessa um fragmento de texto específico dentro da primeira célula da primeira tabela, atualiza seu texto e salva o PDF modificado em um novo arquivo.

1. Abra o arquivo PDF usando 'ap.Document()'.
1. Crie um objeto TableAbsorber para detectar tabelas no PDF.
1. Chama absorber.visit() para encontrar todas as tabelas na primeira página.
1. Acesse um fragmento de texto específico:
- Recupera a primeira tabela.
- Obtém a primeira linha da tabela.
- Seleciona o segundo fragmento de texto na célula.
1. Modifique o texto.
1. Salve o PDF atualizado.
1. Imprime a confirmação do arquivo salvo.

```python

    import aspose.pdf as ap
    from os import path

    # Define file names and data directory
    data_dir = "."  # or specify your data directory
    infile = "input.pdf"   # replace with your input PDF file name
    outfile = "output.pdf" # replace with your desired output PDF file name

    # Open PDF document
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]

    # Change text of the first text fragment in the cell
    fragment.text = "hi world"

    # Save PDF document

    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

## Substituir Tabela antiga por uma nova em documento PDF

Aspose.PDF permite substituir uma tabela existente em um PDF por uma nova tabela. O trecho de código abre um PDF, identifica a primeira tabela na primeira página usando TableAbsorber, cria uma nova tabela com larguras de coluna personalizadas e conteúdo, e então substitui a tabela original pela nova. Por fim, salva o PDF atualizado em um novo arquivo.

Ele demonstra como modificar a estrutura e o conteúdo da tabela em um PDF sem alterar o restante do documento.

```python

    import aspose.pdf as ap
    from os import path

    # Open PDF document
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get first table on the page
    table = absorber.table_list[0]

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

    # Replace the table with new one
    absorber.replace(document.pages[1], table, new_table)

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

---
title: Extrair Dados de Tabela em PDF com Python
linktitle: Extrair Dados de Tabela
type: docs
weight: 40
url: /pt/python-net/extract-data-from-table-in-pdf/
description: Aprenda como extrair tabelas de PDF usando Aspose.PDF para Python
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Extrair Dados de Tabela em PDF via Python
Abstract: Este artigo fornece um guia abrangente sobre como extrair e processar programaticamente tabelas de documentos PDF usando Aspose.PDF, uma biblioteca Python. O artigo apresenta um script Python que abre um documento PDF, itera por cada página e extrai tabelas utilizando a classe `TableAbsorber`. Os dados das tabelas extraídas são então estruturados e impressos para análise adicional. Esta seção descreve como extrair tabelas de regiões marcadas específicas dentro de um PDF, como áreas delimitadas por anotações quadradas. O script identifica essas anotações, inicializa o `TableAbsorber` e verifica se as tabelas estão dentro das regiões anotadas antes de extrair e imprimir os dados. A seção final detalha um método para converter os dados tabulares extraídos de um PDF para o formato de arquivo CSV.
---

## Extrair Tabelas de PDF programaticamente

Este código extrai tabelas de PDF e converte os dados tabulares de um arquivo PDF em um formato legível e estruturado para posterior processamento ou análise.

1. Abrindo o Documento PDF
1. Iterando pelas Páginas do PDF
1. Extraindo Dados da Tabela

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Iterate through each page in the document
    for page in document.pages:
        absorber = apdf.text.TableAbsorber()
        absorber.visit(page)

        for table in absorber.table_list:
            print("Table")
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Extrair tabela em área específica da página PDF

Este trecho de código extrai dados tabulares de regiões marcadas específicas em um PDF, como dados dentro de uma caixa destacada ou uma anotação específica.

1. Abrir documento PDF
1. Obter a primeira página
1. Encontrar a primeira anotação quadrada
1. Inicializar o TableAbsorber
1. Iterar pelas tabelas na página
1. Verificar se a tabela está dentro da região da anotação

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Get the first page (index starts from 1 in Aspose.PDF)
    page = document.pages[1]

    # Find the first square annotation
    square_annotation = next(
        (
            ann
            for ann in page.annotations
            if ann.annotation_type == apdf.annotations.AnnotationType.SQUARE
        ),
        None,
    )

    if square_annotation is None:
        print("No square annotation found.")
        return

    # Initialize the TableAbsorber
    absorber = apdf.text.TableAbsorber()
    absorber.visit(page)

    # Iterate through tables on the page
    for table in absorber.table_list:
        table_rect = table.rectangle
        annotation_rect = square_annotation.rect

        # Check if the table is inside the annotation region
        is_in_region = (
            annotation_rect.llx < table_rect.llx
            and annotation_rect.lly < table_rect.lly
            and annotation_rect.urx > table_rect.urx
            and annotation_rect.ury > table_rect.ury
        )

        if is_in_region:
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Extrair Dados da Tabela de PDF e armazená-los em arquivo Excel

O seguinte trecho de código extrai dados tabulares de um PDF e os exporta como um arquivo CSV para posterior análise ou manipulação em aplicativos de planilha como Excel ou Google Sheets.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    excel_save = apdf.ExcelSaveOptions()
    excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, excel_save)
```


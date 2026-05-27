---
title: Extrair Dados de Tabela em PDF com Python
linktitle: Extrair Dados de Tabela
type: docs
weight: 40
url: /pt/python-net/extract-data-from-table-in-pdf/
description: Aprenda como extrair dados de tabela de arquivos PDF com Aspose.PDF for Python e exportar os resultados para processamento adicional.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Extrair Dados de Tabela em PDF via Python
Abstract: Este artigo explica como extrair e processar dados de tabelas de documentos PDF com Aspose.PDF for Python. Ele mostra como analisar cada página com TableAbsorber, ler linhas e células das tabelas detectadas, limitar a extração a uma região anotada específica e exportar o conteúdo PDF para o formato CSV para uso em ferramentas de planilha e processamento subsequente.
---

## Extrair Tabelas de PDF programaticamente

Usar [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) para detectar tabelas em cada página de um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Depois de visitar uma página, percorra `table_list`, então percorra cada linha e célula para reconstruir o conteúdo da tabela em um formato de texto legível.

1. Abra o PDF como um `Document`.
1. Iterar pelas páginas em `document.pages`.
1. Criar um `TableAbsorber` para cada página e chamar `visit(page)`.
1. Percorra as tabelas, linhas e células detectadas.
1. Leia fragmentos de texto de cada célula e monte a saída da linha extraída.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Extrair tabela em área específica da página PDF

Se precisar extrair apenas tabelas localizadas dentro de uma região marcada, combine [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) com um [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/). Neste exemplo, o retângulo da anotação é usado como limite, e somente tabelas totalmente contidas dentro dessa região são processadas.

1. Abra o PDF como um `Document`.
1. Selecione a página de destino.
1. Encontre a anotação quadrada que marca a região de interesse.
1. Criar um `TableAbsorber` e visite a página.
1. Compare cada retângulo de tabela detectado com o retângulo da anotação.
1. Processar apenas as tabelas que se situam completamente dentro da área marcada.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Exportar Dados da Tabela de PDF para CSV

Quando você precisar dos dados extraídos em um formato amigável a planilhas, salve o PDF usando [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) e defina o formato de saída como CSV. O arquivo resultante pode ser aberto no Excel, Google Sheets, ou importado em fluxos de trabalho analíticos.

1. Abra o PDF de origem como um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Criar um `ExcelSaveOptions` instância.
1. Conjunto `excel_save.format` para `ExcelSaveOptions.ExcelFormat.CSV`.
1. Salve o documento no caminho CSV de destino.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
excel_save = apdf.ExcelSaveOptions()
excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
document.save(path_outfile, excel_save)
```

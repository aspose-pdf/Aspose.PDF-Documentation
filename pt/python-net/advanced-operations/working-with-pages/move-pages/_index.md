---
title: Movendo páginas PDF programaticamente via Python
linktitle: Movendo páginas PDF
type: docs
weight: 100
url: /pt/python-net/move-pages/
description: Tente mover páginas para o local desejado ou para o final de um arquivo PDF usando Aspose.PDF para Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Movendo páginas entre documentos PDF usando Python
Abstract: O artigo fornece um guia abrangente sobre como mover páginas entre documentos PDF ou dentro de um único documento PDF usando Python, especificamente utilizando a biblioteca Aspose.PDF. Ele descreve processos passo a passo para três cenários – mover uma única página de um PDF para outro, transferir múltiplas páginas e realocar uma página dentro do mesmo documento. Cada cenário envolve a criação de objetos da classe `Document` para os PDFs de origem e destino, a manipulação de páginas através da classe `PageCollection`, e a utilização dos métodos `add`, `delete` e `save` para alcançar a reorganização de páginas desejada. Trechos de código são fornecidos para implementação prática, demonstrando como mover páginas de forma eficiente usando scripts Python.
---

## Movendo uma página de um documento PDF para outro

Aspose.PDF para Python permite mover uma página (não apenas copiá-la) de um PDF para outro. Ele remove a página selecionada do documento original e então a adiciona a um novo arquivo PDF.

Pense nisso como cortar uma página de um livro e colá-la em outro — a página deixa de existir no arquivo original após a movimentação.

1. Abra o documento PDF de origem usando a classe [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Selecione uma página específica para mover (neste caso, a página 2) — isso se refere a um [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Crie um novo documento PDF (instancie outro [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Adicione a página selecionada ao novo documento PDF usando a [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) do documento de destino (por exemplo, `another_document.pages.add(page)`).
1. Exclua a página do documento original através da sua [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (por exemplo, `document.pages.delete(index)`).
1. Salve ambos os documentos.

O trecho de código a seguir mostra como mover uma página.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a single page from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf","_new.pdf"))
    another_document.save(output_file_name)
```

## Movendo um conjunto de páginas de um documento PDF para outro

Ao contrário da cópia, esta operação transfere as páginas selecionadas — removendo-as do arquivo de origem e salvando-as em um novo PDF.

1. Crie um novo documento de destino vazio (`Document`).
1. Selecione múltiplas páginas (neste caso, as páginas 1 e 3) da [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) do documento de origem.
1. Percorra as páginas selecionadas e adicione cada uma à [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) do documento de destino.
1. Salve o documento de destino contendo as páginas movidas.
1. Exclua as páginas movidas do documento de origem usando sua [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o documento de origem modificado com um novo nome de arquivo para preservar ambas as versões.

O trecho de código a seguir mostra como inserir uma página vazia no final de um arquivo PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_bunch_pages_from_one_document_to_another(input_file_name, output_file_name):
    """
    Move a set of pages from one PDF document to another.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file where selected pages will be saved.
    """
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf","_new.pdf"))
```

## Movendo uma página para nova localização no documento PDF atual

Mostra como mover uma página específica para uma posição diferente dentro do mesmo documento — uma necessidade comum ao reorganizar ou editar layouts de PDF.

1. Carregue o documento PDF de entrada usando a classe [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Selecione a página que você deseja mover (página 2) — esta é uma [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Adicione-a ao final do documento usando a [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) do documento.
1. Exclua a página original de sua localização anterior via a [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o documento modificado como um novo arquivo.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def moving_page_in_new_location_in_same_document(input_file_name, output_file_name):
    """
    Move a page to a new location within the same PDF document.

    Parameters:
    - input_file_name (str): Path to the source PDF file.
    - output_file_name (str): Path to the destination PDF file after moving the page.
    """
    srcDocument = ap.Document(input_file_name)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Save output file
    srcDocument.save(output_file_name)
```



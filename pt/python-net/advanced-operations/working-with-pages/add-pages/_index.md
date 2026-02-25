---
title: Adicionando Páginas em PDF com Python
linktitle: Adicionando Páginas
type: docs
weight: 10
url: /pt/python-net/add-pages/
description: Descubra como adicionar páginas a um documento PDF em Python usando Aspose.PDF para criação e edição flexível de documentos.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar Páginas em PDF usando Python
Abstract: Este artigo fornece um guia sobre como usar o Aspose.PDF para Python via API .NET para manipular páginas em um documento PDF. Ele enfatiza a flexibilidade oferecida pela API, particularmente através da classe `PageCollection`, que gerencia todas as páginas dentro de um PDF. O documento detalha os procedimentos para adicionar ou inserir páginas em locais específicos em um arquivo PDF. Ele descreve duas operações principais – inserir uma página vazia no local desejado dentro do documento e adicionar uma página vazia ao final do documento. Para ambas as operações, o processo envolve criar um objeto `Document`, usar os métodos `insert` ou `add` da `PageCollection` e salvar o documento modificado. O artigo inclui trechos de código demonstrando essas tarefas, mostrando como é simples manipular documentos PDF usando Python com esta API.
---

Aspose.PDF para Python via API .NET oferece total flexibilidade para trabalhar com páginas em um documento PDF usando Python. Ele mantém todas as páginas de um documento PDF em [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) que pode ser usado para trabalhar com páginas PDF.
Aspose.PDF para Python via .NET permite inserir uma página em um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) em qualquer local do arquivo, bem como adicionar páginas ao final de um arquivo PDF. Esta seção mostra como adicionar páginas a um PDF usando Python.

## Adicionar ou Inserir Página em um Arquivo PDF

Aspose.PDF para Python via .NET permite inserir uma página em um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) em qualquer local do arquivo, bem como adicionar páginas ao final de um arquivo PDF.

### Inserir Página em Branco em um Arquivo PDF

Para inserir uma página em branco em um arquivo PDF:

1. Abra um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) existente usando os métodos apropriados.
1. Insira uma nova página em branco em um índice específico usando o método `insert()` da [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado no caminho de saída desejado.

Insira uma página em branco em um arquivo PDF existente em uma posição especificada:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def insert_empty_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Adicionar uma Página em Branco ao Final de um Arquivo PDF

Às vezes, você quer garantir que um documento termine em uma página em branco. Este tópico explica como inserir uma página em branco ao final do documento PDF.

Para inserir uma página em branco ao final de um arquivo PDF:

1. Abra um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) existente usando os métodos apropriados.
1. Adicione uma nova página em branco ao final do documento usando o método `add()` da [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) atualizado.

O trecho de código a seguir mostra como inserir uma página em branco ao final de um arquivo PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_empty_page_to_end(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Insert an empty page at the end of a PDF file
    document.pages.add()

    # Save output file
    document.save(output_file_name)
```

### Adicionar uma Página de Outro Documento PDF

Com a biblioteca Aspose.PDF para Python, você cria um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), adiciona uma página inicial e então importa uma página de outro PDF para ele.

1. Crie um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Adicione uma nova [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) em branco e escreva algum texto nela usando [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Abra outro [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) existente.
1. Copie uma [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) desse documento.
1. Cole a página copiada em seu documento principal usando a [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o arquivo combinado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_from_another_document(input_file_name, output_file_name):
    # Open document
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    # Save output file
    document.save(output_file_name)
```

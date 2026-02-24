---
title: Alterando o Tamanho da Página com Python
linktitle: Alterando o Tamanho da Página
type: docs
weight: 40
url: /pt/python-net/change-page-size/
description: Altere o tamanho da página do seu documento PDF usando o Aspose.PDF para Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Alterando o Tamanho da Página usando Python
Abstract: Este artigo demonstra como ler e modificar as dimensões das páginas de PDF usando o Aspose.PDF. O exemplo Obter Tamanho da Página recupera a largura e a altura de uma página PDF específica, permitindo que os usuários inspecionem o layout da página, validem a formatação ou analisem a estrutura do documento. O exemplo Definir Tamanho da Página mostra como alterar as dimensões de uma página — como converter a primeira página para o tamanho A4 — exibindo também as propriedades das caixas (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) antes e depois da modificação.
---

Aspose.PDF para Python via .NET permite que você altere o tamanho da página PDF com linhas simples de código. Este tópico mostra como atualizar as dimensões da página usando as APIs [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) e [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

{{% alert color="primary" %}}

Observe que as propriedades de altura e largura utilizam pontos como unidade básica, onde 1 polegada = 72 pontos e 1 cm = 1/2.54 polegada = 0.3937 polegada = 28.3 pontos.

{{% /alert %}}

### Definir o Tamanho da Página de um PDF para A4

O exemplo atualiza o tamanho da primeira página de um documento PDF para as dimensões padrão A4. Ele também exibe as dimensões das caixas da página (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) antes e depois do redimensionamento para que você possa verificar as alterações.

O trecho de código a seguir mostra como alterar as dimensões da página PDF para o tamanho A4:

1. Acesse a primeira [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) do [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Exiba os tamanhos das caixas da página antes da modificação (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Aplique as dimensões A4 (597.6 × 842.4 pontos) usando a API da página.
1. Exiba os tamanhos atualizados das caixas da página.
1. Salve o [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado no caminho de saída especificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    # Open the PDF document using the Document class
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in). In Aspose.PDF 1 inch = 72 points.
    # A4 dimensions in points are (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Use the Page API to set page size
    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## Obter Tamanho da Página PDF

Este trecho lê um PDF e recupera as dimensões (largura e altura) da primeira página. Ele usa a API [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para extrair o [`Retângulo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) delimitador da página e imprime seu tamanho no console. Isso é útil para inspecionar o layout da página, verificar formatos ou preparar documentos para processamento adicional.

1. Carregue o PDF como um [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Acesse a primeira [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Recupere o retângulo delimitador da página usando `get_page_rect()`.
1. Extraia os valores de largura e altura.
1. Imprima as dimensões da página.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)

    # Get particular page (Page API)
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Obter Tamanho da Página PDF Antes e Depois da Rotação

Recupere as dimensões de uma página PDF antes e depois de aplicar uma rotação de 90°. Isso demonstra como a rotação afeta a largura e a altura e como usar `get_page_rect()` com ou sem consideração de rotação.

1. Abra o PDF como um [`Documento`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Acesse a primeira [`Página`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Aplique uma rotação de 90° usando `page.rotate = ap.Rotation.ON90` (veja o enum [`Rotação`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/)).
1. Recupere o retângulo da página sem rotação usando `get_page_rect(False)` e imprima sua largura e altura.
1. Recupere o retângulo da página considerando a rotação usando `get_page_rect(True)` e imprima sua largura e altura.
1. Compare como as dimensões mudam devido à rotação.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_size_rotation(input_file_name, output_file_name):
    # Open document (Document API)
    document = ap.Document(input_file_name)
    # Get particular page (Page API)
    page = document.pages[1]
    # Apply rotation using Rotation enum
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

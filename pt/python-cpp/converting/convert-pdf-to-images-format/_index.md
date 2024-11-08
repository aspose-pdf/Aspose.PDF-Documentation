---
title: Converter PDF para Diferentes Formatos de Imagem em Python
linktitle: Converter PDF para Imagens
type: docs
weight: 70
url: /pt/python-cpp/convert-pdf-to-images-format/
lastmod: "2023-06-23"
description: Este tópico mostra como usar Aspose.PDF para Python para converter PDF em vários formatos de imagem, por exemplo, TIFF, BMP, EMF, JPEG, PNG, GIF, SVG com algumas linhas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Visão Geral

Este artigo explica como converter PDF para diferentes formatos de imagem usando Python. Ele cobre os seguintes tópicos.

## Python Converter PDF para Imagem

### Python Converter PDF para PNG

1. Importe o módulo AsposePdfPython, que fornece um wrapper em Python para a biblioteca Aspose.PDF.
1. Abra um documento PDF usando a função `document_open`, que leva o nome do arquivo como argumento e retorna um objeto Document.
1. Obtenha as páginas do documento usando a função `document_get_pages`, que leva um objeto Document como argumento e retorna um objeto PageCollection.

1. Obtenha a página desejada do documento usando a função `page_collection_get_page`, que recebe um objeto PageCollection e um índice como argumentos e retorna um objeto Page.
1. Crie um objeto PngDevice usando a função `png_device_create`, que não recebe argumentos. Este objeto pode converter páginas PDF em imagens PNG com parâmetros padrão.
1. Salve a página desejada do documento como uma imagem PNG usando a função `png_device_save_page_to_file`, que recebe um objeto PngDevice, um objeto Page e um nome de arquivo como argumentos.
1. Feche os manipuladores dos objetos PngDevice e Document usando a função close_handle, que recebe um objeto como argumento e libera seus recursos.

```python

from AsposePdfPython import *

doc = document_open("blank_pdf_document.pdf")
pages = document_get_pages(doc)
page = page_collection_get_page(pages,1)

pngDevice = png_device_create()
png_device_save_page_to_file(pngDevice,page,"test.png")

```

### Python Converter PDF para JPEG

1. Abra um documento PDF usando a função `document_open`, que recebe o nome do arquivo como argumento e retorna um objeto Document.
1. Obtenha as páginas do documento usando a função `document_get_pages`, que recebe um objeto Document como argumento e retorna um objeto PageCollection.
1. Obtenha a página desejada do documento usando a função `page_collection_get_page`, que recebe um objeto PageCollection e um índice como argumentos e retorna um objeto Page.
1. Crie um objeto Resolution usando a função `resolution_create`, que recebe o valor da resolução em pontos por polegada (DPI) como argumento.
1. Crie um objeto JpegDevice usando a função `jpeg_device_create_from_width_height_resolution`, que recebe os valores de largura, altura e resolução como argumentos. Este objeto pode converter páginas de PDF em imagens JPEG com os parâmetros especificados.

1. Salve a página desejada do documento como uma imagem JPEG usando a função `jpeg_device_save_page_to_file`, que recebe um objeto JpegDevice, um objeto Page e um nome de arquivo como argumentos.
1. Feche os handles dos objetos JpegDevice e Document usando a função `close_handle`, que recebe um objeto como argumento e libera seus recursos.

```python

    from AsposePdfPython import *

    doc = document_open("blank_pdf_document.pdf")
    pages = document_get_pages(doc)
    page = page_collection_get_page(pages,1)

    res = resolution_create(300)
    jpegDevice = jpeg_device_create_from_width_height_resolution(1239,1754,res)
    jpeg_device_save_page_to_file(jpegDevice,page,"test.jpeg")
```
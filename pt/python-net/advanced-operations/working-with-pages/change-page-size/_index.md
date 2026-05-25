---
title: Alterar o tamanho da página PDF em Python
linktitle: Alterando o tamanho da página
type: docs
weight: 40
url: /pt/python-net/change-page-size/
description: Aprenda como ler e alterar as dimensões da página PDF em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Alterando o tamanho da página usando Python
Abstract: Este artigo demonstra como ler e modificar as dimensões de páginas PDF usando Aspose.PDF. O exemplo Get Page Size recupera a largura e a altura de uma página PDF específica, permitindo que os usuários inspecionem o layout da página, validem a formatação ou analisem a estrutura do documento. O exemplo Set Page Size mostra como alterar as dimensões de uma página — como converter a primeira página para o tamanho A4 — exibindo também as propriedades das caixas (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) antes e depois da modificação.
---

Aspose.PDF for Python via .NET permite que você altere o tamanho da página PDF com linhas simples de código. Este tópico mostra como atualizar as dimensões da página usando o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) e [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) APIs.

Use este guia quando precisar redimensionar páginas PDF existentes, normalizar dimensões do documento ou inspecionar as configurações da caixa de página em Python.

{{% alert color="primary" %}}

Observe que as propriedades de altura e largura usam pontos como unidade básica, onde 1 polegada = 72 pontos e 1 cm = 1/2,54 polegada = 0,3937 polegada = 28,3 pontos.

{{% /alert %}}

## Defina o tamanho da página de um PDF para A4

O exemplo atualiza o tamanho da primeira página em um documento PDF para as dimensões padrão A4. Ele também imprime as dimensões das caixas da página (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) antes e depois do redimensionamento, para que você possa verificar as alterações.

O trecho de código a seguir mostra como alterar as dimensões da página PDF para o tamanho A4:

1. Acesse o primeiro [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) do [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Exiba os tamanhos das caixas da página antes da modificação (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Aplique as dimensões A4 (597.6 × 842.4 pontos) usando a API de página.
1. Exiba os tamanhos atualizados das caixas de página.
1. Salve o modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para o caminho de saída especificado.

```python
import aspose.pdf as ap

def set_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

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

## Obter tamanho da página PDF

Este trecho lê um PDF e recupera as dimensões (largura e altura) da primeira página. Ele usa o [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API para extrair o limite da página [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) e imprime seu tamanho no console. Isso é útil para inspecionar o layout da página, verificar formatos ou preparar documentos para processamento adicional.

1. Carregue o PDF como um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Acesse o primeiro [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Recupere o retângulo delimitador da página usando `get_page_rect()`.
1. Extraia os valores de largura e altura.
1. Imprima as dimensões da página.

```python
import aspose.pdf as ap

def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Obter tamanho da página PDF antes e depois da rotação

Recupere as dimensões de uma página PDF antes e depois de aplicar uma rotação de 90°. Isso demonstra como a rotação afeta a largura e a altura e como usar `get_page_rect()` com ou sem consideração de rotação.

1. Abra o PDF como um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Acesse o primeiro [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Aplicar uma rotação de 90° usando `page.rotate = ap.Rotation.ON90` (veja o [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) enum).
1. Recupere o retângulo da página sem rotação usando `get_page_rect(False)` e imprima sua largura e altura.
1. Recuperar o retângulo da página considerando a rotação usando `get_page_rect(True)` e imprima sua largura e altura.
1. Compare como as dimensões mudam devido à rotação.

```python
import aspose.pdf as ap

def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

## Tópicos Relacionados da Página

- [Trabalhar com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Recortar páginas PDF em Python](/pdf/pt/python-net/crop-pages/)
- [Obter e definir propriedades de página PDF em Python](/pdf/pt/python-net/get-and-set-page-properties/)
- [Rotacionar páginas PDF em Python](/pdf/pt/python-net/rotate-pages/)
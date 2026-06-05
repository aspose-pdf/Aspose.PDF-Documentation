---
title: Adicionar imagem a PDF existente em Python
linktitle: Adicionar imagem ao PDF
type: docs
weight: 10
url: /pt/python-net/add-image-to-existing-pdf-file/
description: Aprenda como adicionar uma imagem a um arquivo PDF existente em Python, posicioná‑la em coordenadas fixas, definir texto alternativo e usar compressão de imagem.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Adicionar imagens a arquivos PDF existentes usando Python
Abstract: Este artigo mostra como adicionar imagens a documentos PDF com Aspose.PDF for Python via .NET. Ele abrange a colocação de uma imagem em coordenadas fixas, desenhar imagens com operadores PDF de baixo nível, atribuir texto alternativo para acessibilidade e incorporar imagens com compressão Flate.
---

## Adicionar Imagem a um Arquivo PDF Existente em Python

Este exemplo mostra como posicionar uma imagem em um local fixo em uma página PDF existente usando Aspose.PDF for Python via .NET.

Use estes exemplos quando precisar adicionar um logotipo, foto, carimbo, gráfico ou outro elemento visual a um layout PDF existente. Você pode posicionar a imagem com coordenadas de página, desenhá‑la com operadores, adicionar texto de acessibilidade ou controlar a compressão da imagem.

1. Carregue um PDF existente com `ap.Document(infile)`.
1. Selecione a página de destino (`document.pages[1]` para a primeira página).
1. Chamar `page.add_image()` com:
    - O caminho do arquivo de imagem.
    - A `Rectangle` definindo coordenadas de posicionamento.
1. Salve o PDF atualizado.

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## Adicionar uma imagem ao PDF usando operadores

Esta abordagem adiciona uma imagem com operadores PDF de baixo nível em vez dos de alto nível `add_image()` ajudante.

1. Crie um novo `Document` e adicione uma página.
1. Adicionar a imagem aos recursos da página (`page.resources.images`).
1. Criar operadores de transformação (`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. Adicione operadores ao conteúdo da página.
1. Salve o PDF resultante.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## Adicionar imagem ao PDF com texto alternativo

Este exemplo adiciona uma imagem e atribui texto alternativo para acessibilidade.

1. Crie um novo `Document` e adicione uma página.
1. Adicione a imagem à página com `page.add_image()`.
1. Obter recursos de imagem de `page.resources.images`.
1. Definir texto alternativo usando `try_set_alternative_text()`.
1. Salve o PDF resultante.

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## Adicionar uma imagem a um PDF com compactação Flate

Este exemplo incorpora uma imagem usando `ImageFilterType.FLATE` compressão.

1. Crie um novo `Document` e adicione uma página.
1. Adicionar a imagem aos recursos da página com compactação Flate.
1. Usar operadores de matriz para posicionar e desenhar a imagem.
1. Salve o documento.

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## Tópicos Relacionados a Imagens

- [Trabalhe com imagens em PDF usando Python](/pdf/pt/python-net/working-with-images/)
- [Substituir imagens em arquivos PDF existentes](/pdf/pt/python-net/replace-image-in-existing-pdf-file/)
- [Excluir imagens de arquivos PDF](/pdf/pt/python-net/delete-images-from-pdf-file/)
- [Extrair imagens de arquivos PDF](/pdf/pt/python-net/extract-images-from-pdf-file/)

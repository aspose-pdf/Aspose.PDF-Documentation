---
title: Adicionar imagem ao PDF usando Python
linktitle: Adicionar imagem
type: docs
weight: 10
url: /pt/python-net/add-image-to-existing-pdf-file/
description: Saiba como adicionar imagens a arquivos PDF existentes em Python.
lastmod: "2026-05-20"
TechArticle: true
AlternativeHeadline: Adicionar imagens a arquivos PDF existentes com Python
Abstract: Este artigo mostra como adicionar imagens a documentos PDF com Aspose.PDF for Python via .NET. Ele aborda a adição de uma imagem em coordenadas fixas, a inserção de imagens com operadores de baixo nível, a atribuição de texto alternativo para acessibilidade e a incorporação de imagens com compressão Flate.
---

## Adicionar imagem em um arquivo PDF existente

Este exemplo mostra como posicionar uma imagem em um local fixo em uma página PDF existente usando Aspose.PDF for Python via .NET.

Use esses exemplos desta página quando precisar posicionar logotipos, fotos ou outras imagens em coordenadas fixas dentro de um layout PDF existente.

1. Carregue um PDF existente com `ap.Document(infile)`.
1. Selecione a página de destino (`document.pages[1]` para a primeira página).
1. Chamada `page.add_image()` com:
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

## Adicionar uma Imagem Usando Operadores

Esta abordagem adiciona uma imagem com operadores PDF de baixo nível em vez dos de alto nível. `add_image()` ajudante.

1. Criar um novo `Document` e adicione uma página.
1. Adicione a imagem aos recursos da página (`page.resources.images`).
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

## Adicionar Imagem com Texto Alternativo

Este exemplo adiciona uma imagem e atribui texto alternativo para acessibilidade.

1. Criar um novo `Document` e adicione uma página.
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

## Adicionar uma imagem a um PDF com compressão Flate

Este exemplo incorpora uma imagem usando `ImageFilterType.FLATE` compressão.

1. Criar um novo `Document` e adicione uma página.
1. Adicionar a imagem aos recursos da página com compressão Flate
1. Use operadores de matriz para posicionar e desenhar a imagem.
1. Salvar o documento.

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

## Tópicos Relacionados à Imagem

- [Trabalhe com imagens em PDF usando Python](/pdf/pt/python-net/working-with-images/)
- [Substitua imagens em arquivos PDF existentes](/pdf/pt/python-net/replace-image-in-existing-pdf-file/)
- [Excluir imagens de arquivos PDF](/pdf/pt/python-net/delete-images-from-pdf-file/)
- [Extrair imagens de arquivos PDF](/pdf/pt/python-net/extract-images-from-pdf-file/)

---
title: Obter e Pesquisar Imagens em PDF
linktitle: Obter e Pesquisar Imagens
type: docs
weight: 40
url: /pt/python-net/search-and-get-images-from-pdf-document/
description: Aprenda como pesquisar e inspecionar imagens em documentos PDF em Python.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Pesquise e inspecione imagens em arquivos PDF com Python
Abstract: Este artigo mostra como pesquisar e inspecionar imagens em documentos PDF com Aspose.PDF for Python via .NET. Ele aborda o uso de ImagePlacementAbsorber para analisar a posição da imagem, tamanho, resolução e texto alternativo.
---

## Inspecionar propriedades de posicionamento de imagem em uma página PDF

Este exemplo demonstra como analisar e exibir as propriedades de todas as imagens em uma página PDF específica usando Aspose.PDF for Python via .NET.

Use esta página quando precisar auditar o posicionamento de imagens, inspecionar a resolução da imagem ou identificar objetos de imagem incorporados em várias páginas PDF.

1. Crie um 'ImagePlacementAbsorber' para coletar todas as imagens na página.
1. Chame 'document.pages[1].accept(absorber)' para analisar as posições das imagens na primeira página.
1. Itere através de 'absorber.image_placements' e exiba as principais propriedades de cada imagem:
    - Largura e Altura (pontos).
    - Coordenadas X (LLX) e Y (LLY) do canto inferior esquerdo.
    - Resolução horizontal (X) e vertical (Y) (DPI).

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_params(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Extrair e Contar Tipos de Imagem em um PDF

Esta função analisa todas as imagens na primeira página de um PDF e conta quantas são imagens em escala de cinza e RGB.

1. Crie um 'ImagePlacementAbsorber' para coletar todas as imagens na página.
1. Inicializar contadores para imagens em escala de cinza e RGB.
1. Chame 'document.pages[1].accept(absorber)' para analisar a colocação de imagens.
1. Imprima o número total de imagens encontradas.
1. Itere por cada imagem em 'absorber.image_placements':
    - Obtenha o tipo de cor da imagem usando 'image_placement.image.get_color_type()'.
    - Incrementar o contador correspondente (escala de cinza ou rgb).
    - Imprimir uma mensagem para cada imagem indicando se ela é em escala de cinza ou RGB.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.
    """

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1

    print("--------------------------------")
    print("Grayscale Images = " + str(grayscaled))
    print("RGB Images = " + str(rgb))
```

## Extrair informações detalhadas da imagem de um PDF

Esta função analisa todas as imagens na primeira página de um PDF e calcula suas dimensões escalonadas e resolução efetiva com base nas transformações gráficas da página.

1. Carregar PDF e inicializar variáveis
1. Coletar recursos de imagem
1. Processar operadores de conteúdo da página:
    - 'GSave' - empurrar a CTM atual para a pilha.
    - 'GRestore' - retirar a última CTM da pilha.
    - 'ConcatenateMatrix' - atualize a CTM atual multiplicando‑a pela matriz do operador.
1. Imprima o nome da imagem, dimensões escaladas e resolução calculada.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_information_from_pdf(infile):
    with ap.Document(infile) as document:
        default_resolution = 72
        graphics_state = []

        image_names = list(document.pages[1].resources.images.names)

        graphics_state.append(
            drawing.drawing2d.Matrix(
                float(1), float(0), float(0), float(1), float(0), float(0)
            )
        )

        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                op_cm = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(op_cm.matrix.a),
                    float(op_cm.matrix.b),
                    float(op_cm.matrix.c),
                    float(op_cm.matrix.d),
                    float(op_cm.matrix.e),
                    float(op_cm.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                op_do = cast(ap.operators.Do, op)
                if op_do.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(op_do.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = (
                        original_width * default_resolution / scaled_width
                    )
                    res_vertical = (
                        original_height * default_resolution / scaled_height
                    )

                    info = (
                        f"{infile} image {op_do.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
```

## Extrair Texto Alternativo de Imagens em um PDF

Esta função recupera o texto alternativo (alt text) de todas as imagens na primeira página de um PDF, útil para verificações de acessibilidade e conformidade com PDF/UA.

1. Carregue o documento PDF usando 'ap.Document()'.
1. Crie um 'ImagePlacementAbsorber' para coletar todas as imagens na página.
1. Aceite o absorvedor na primeira página (page.accept(absorber)).
1. Itere por cada imagem em 'absorber.image_placements':
    - Imprima o nome da imagem na coleção de recursos da página (get_name_in_collection()).
    - Recupere o texto alternativo usando 'get_alternative_text(page)'.
    - Imprima a primeira linha do texto alternativo.

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_alt_text(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

## Tópicos Relacionados a Imagens

- [Trabalhe com imagens em PDF usando Python](/pdf/pt/python-net/working-with-images/)
- [Extrair imagens de arquivos PDF](/pdf/pt/python-net/extract-images-from-pdf-file/)
- [Substituir imagens em arquivos PDF existentes](/pdf/pt/python-net/replace-image-in-existing-pdf-file/)
- [Adicionar imagens a arquivos PDF existentes](/pdf/pt/python-net/add-image-to-existing-pdf-file/)

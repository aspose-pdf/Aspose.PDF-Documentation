---
title: Obter e Pesquisar Imagens em PDF
linktitle: Obter e Pesquisar Imagens
type: docs
weight: 40
url: /pt/python-net/search-and-get-images-from-pdf-document/
description: Aprenda como pesquisar e obter imagens de um documento PDF em Python usando Aspose.PDF.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Pesquisando e Extraindo Imagens de PDF
Abstract: A biblioteca Aspose.PDF for Python via .NET oferece recursos robustos para pesquisar e extrair imagens de documentos PDF. Utilizando a classe 'ImagePlacementAbsorber', os desenvolvedores podem localizar e acessar eficientemente imagens incorporadas em todas as páginas de um PDF.
---

## Inspecionar Propriedades de Posicionamento de Imagem em uma Página PDF

Este exemplo demonstra como analisar e exibir as propriedades de todas as imagens em uma página PDF específica usando Aspose.PDF for Python via .NET.

1. Crie um 'ImagePlacementAbsorber' para coletar todas as imagens na página.
1. Chame 'document.pages[1].accept(absorber)' para analisar os posicionamentos de imagens na primeira página.
1. Itere através de 'absorber.image_placements' e exiba as principais propriedades de cada imagem:
- Largura e Altura (pontos).
- Coordenadas X (LLX) e Y (LLY) do canto inferior esquerdo.
- Resolução Horizontal (X) e Vertical (Y) (DPI).

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        # Display image placement properties for all placements
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Extrair e Contar Tipos de Imagem em um PDF

Esta função analisa todas as imagens na primeira página de um PDF e conta quantas são em escala de cinza e RGB.

1. Crie um 'ImagePlacementAbsorber' para coletar todas as imagens na página.
1. Inicialize contadores para imagens em escala de cinza e RGB.
1. Chame 'document.pages[1].accept(absorber)' para analisar os posicionamentos de imagens.
1. Imprima o número total de imagens encontradas.
1. Itere através de cada imagem em 'absorber.image_placements':
- Obtenha o tipo de cor da imagem usando 'image_placement.image.get_color_type()'.
- Incrementar o contador correspondente (escala de cinza ou rgb).
- Imprima uma mensagem para cada imagem indicando se é em escala de cinza ou RGB.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
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
```

## Extrair Informações Detalhadas da Imagem de um PDF

Esta função analisa todas as imagens na primeira página de um PDF e calcula suas dimensões escaladas e resolução efetiva com base nas transformações gráficas da página.

1. Carregue o PDF e inicialize variáveis
1. Colete recursos de imagem
1. Processar operadores de conteúdo da página:
- 'GSave' - empurra o CTM atual para a pilha.
- 'GRestore' - remove o último CTM da pilha.
- 'ConcatenateMatrix' - atualiza o CTM atual multiplicando-o pela matriz do operador.
1. Imprima o nome da imagem, as dimensões escaladas e a resolução calculada.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(drawing.drawing2d.Matrix(float(1), float(0), float(0), float(1), float(0), float(0)))

    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone())

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = drawing.drawing2d.Matrix(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1].multiply(cm)
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                scaled_width = math.sqrt(last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2)
                scaled_height = math.sqrt(last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2)

                original_width = image.width
                original_height = image.height

                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```

## Extrair Texto Alternativo de Imagens em um PDF

Esta função recupera o texto alternativo (alt text) de todas as imagens na primeira página de um PDF, útil para verificações de acessibilidade e conformidade PDF/UA.

1. Carregue o documento PDF usando 'ap.Document()'.
1. Crie um 'ImagePlacementAbsorber' para coletar todas as imagens na página.
1. Aceite o absorvedor na primeira página (page.accept(absorber)).
1. Itere através de cada imagem em 'absorber.image_placements':
- Imprima o nome da imagem na coleção de recursos da página (get_name_in_collection()).
- Recupere o texto alternativo usando 'get_alternative_text(page)'.
- Imprima a primeira linha do texto alternativo.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: "
            + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

---
title: Extrair Imagens de Arquivo PDF usando Python
linktitle: Extrair Imagens
type: docs
weight: 30
url: /pt/python-net/extract-images-from-pdf-file/
description: Esta seção mostra como extrair imagens de um arquivo PDF usando a biblioteca Python.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Extrair imagens de PDF com Python
Abstract: Este artigo discute o processo de extração de imagens de arquivos PDF usando Aspose.PDF para Python. Destaca a utilidade de separar imagens para fins como gerenciamento, arquivamento, análise ou compartilhamento. O artigo explica que as imagens dentro de um PDF são armazenadas na coleção de recursos de cada página, especificamente na coleção XImage. Para extrair uma imagem, os usuários podem acessar uma página específica e recuperar a imagem usando seu índice na coleção Images. O objeto XImage retornado pelo índice fornece um método `save()` para salvar a imagem extraída. Um trecho de código é fornecido para demonstrar os passos necessários para abrir um documento PDF, extrair uma imagem específica da segunda página usando seu índice e salvá‑la em um arquivo.
---

Precisa separar imagens dos seus arquivos PDF? Para gerenciamento simplificado, arquivamento, análise ou compartilhamento de imagens dos seus documentos, use **Aspose.PDF for Python** e extraia imagens de arquivos PDF.

1. Carregue o documento PDF com 'ap.Document()'.
1. Acesse a página desejada do documento (document.pages[1]).
1. Selecione a imagem dos recursos da página (por exemplo, resources.images[1]).
1. Crie um fluxo de saída (FileIO) para o arquivo de destino.
1. Salve a imagem extraída usando 'xImage.save(output_image)'.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## Extrair Imagens de Região Específica em PDF

Este exemplo extrai imagens localizadas dentro de uma região retangular especificada em uma página PDF e as salva como arquivos separados.

1. Carregue o documento PDF usando 'ap.Document'.
1. Crie um 'ImagePlacementAbsorber' para coletar todas as imagens na primeira página.
1. Chame 'document.pages[1].accept(absorber)' para analisar a colocação das imagens.
1. Itere por todas as imagens em 'absorber.image_placements':
- Obtenha a caixa delimitadora da imagem (llx, lly, urx, ury).
- Verifique se ambos os cantos do retângulo da imagem estão dentro do retângulo alvo (rectangle.contains()).
- Se verdadeiro, salve a imagem em um arquivo usando FileIO, substituindo 'index' no nome do arquivo por um número sequencial.
1. Incrementar o índice para cada imagem salva.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## Extrair Informações da Imagem do PDF

O exemplo abaixo demonstra como analisar imagens incorporadas em uma página PDF e calcular sua resolução efetiva.

1. Abra o PDF com 'ap.Document'.
1. Acompanhe o estado gráfico ao ler o conteúdo da página.
1. Manipule operadores:
- 'GSave'/'GRestore' - empilhar/desempilhar matriz.
- 'ConcatenateMatrix' - atualizar transformação.
- 'Do' - se for uma imagem, obter tamanho e aplicar transformação.
1. Calcule o DPI efetivo.
1. Imprima o nome da imagem, tamanho escalado e DPI.

```python

    import aspose.pdf as ap
    from io import FileIO
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

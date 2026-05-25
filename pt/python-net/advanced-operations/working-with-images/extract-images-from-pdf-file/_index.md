---
title: Extrair imagens de arquivo PDF usando Python
linktitle: Extrair imagens
type: docs
weight: 30
url: /pt/python-net/extract-images-from-pdf-file/
description: Aprenda como extrair imagens incorporadas de arquivos PDF em Python.
lastmod: "2026-05-20"
TechArticle: true
AlternativeHeadline: Extrair imagens de arquivos PDF com Python
Abstract: Este artigo mostra como extrair imagens de documentos PDF com Aspose.PDF for Python via .NET. Ele cobre a extração de uma única imagem incorporada e a exportação de imagens encontradas dentro de uma região retangular específica em uma página.
---

Use esta página quando precisar reutilizar gráficos incorporados, arquivar ativos de imagem ou processar conteúdo de imagem fora do PDF.

1. Carregue o PDF de origem com `ap.Document(infile)`.
1. Selecione a página de destino e o índice do recurso de imagem.
1. Salve o objeto de imagem em um fluxo de saída.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## Extrair imagens de região específica em PDF

Este exemplo extrai imagens localizadas dentro de uma região retangular especificada em uma página PDF e as salva como arquivos separados.

1. Carregue o PDF de origem.
1. Criar `ImagePlacementAbsorber` e aceite-o na página de destino.
1. Defina o retângulo de destino.
1. Itere pelas colocações de imagens e verifique se os limites de cada imagem se encaixam na região.
1. Salve as imagens correspondentes em arquivos de saída.

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## Tópicos Relacionados à Imagem

- [Trabalhar com imagens em PDF usando Python](/pdf/pt/python-net/working-with-images/)
- [Substituir imagens em arquivos PDF existentes](/pdf/pt/python-net/replace-image-in-existing-pdf-file/)
- [Excluir imagens de arquivos PDF](/pdf/pt/python-net/delete-images-from-pdf-file/)
- [Adicionar imagens a arquivos PDF existentes](/pdf/pt/python-net/add-image-to-existing-pdf-file/)

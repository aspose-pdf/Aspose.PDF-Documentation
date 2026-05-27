---
title: Substituir imagem em arquivo PDF existente usando Python
linktitle: Substituir imagem
type: docs
weight: 70
url: /pt/python-net/replace-image-in-existing-pdf-file/
description: Aprenda como substituir imagens incorporadas em arquivos PDF existentes em Python.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Substitua imagens em arquivos PDF existentes com Python
Abstract: Este artigo mostra como substituir imagens em documentos PDF com Aspose.PDF for Python via .NET. Ele cobre a substituição de uma imagem por índice de recurso e a substituição de uma imagem específica encontrada com ImagePlacementAbsorber.
---

## Substituir uma imagem em PDF

Use esta página quando precisar atualizar logotipos, diagramas ou outras imagens incorporadas em um PDF sem recriar o layout do documento.

1. Carregue o PDF de origem com `ap.Document(infile)`.
1. Abra a imagem de substituição como um fluxo binário.
1. Substitua um recurso de imagem por índice em uma página.
1. Salve o PDF atualizado.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## Substituir uma Imagem Específica

Este exemplo substitui um posicionamento de imagem específico encontrado por `ImagePlacementAbsorber`.

1. Carregar o PDF de origem.
1. Criar `ImagePlacementAbsorber` e coletar posicionamentos de imagens na página.
1. Verificar se existem posicionamentos de imagem na página.
1. Substitua a posição selecionada por um novo fluxo de imagem.
1. Salve o PDF atualizado.

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## Tópicos Relacionados a Imagens

- [Trabalhe com imagens em PDF usando Python](/pdf/pt/python-net/working-with-images/)
- [Excluir imagens de arquivos PDF](/pdf/pt/python-net/delete-images-from-pdf-file/)
- [Extrair imagens de arquivos PDF](/pdf/pt/python-net/extract-images-from-pdf-file/)
- [Adicionar imagens a arquivos PDF existentes](/pdf/pt/python-net/add-image-to-existing-pdf-file/)

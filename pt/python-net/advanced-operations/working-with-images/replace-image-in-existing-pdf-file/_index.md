---
title: Substituir Imagem em Arquivo PDF Existente usando Python
linktitle: Substituir Imagem
type: docs
weight: 70
url: /pt/python-net/replace-image-in-existing-pdf-file/
description: Esta seção descreve a substituição de imagem em arquivo PDF existente usando a biblioteca Python.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Substituir uma Imagem em PDF
Abstract: A documentação do Aspose.PDF para Python via .NET fornece um guia abrangente sobre como substituir imagens em arquivos PDF existentes. Essa funcionalidade é essencial para tarefas como atualizar logotipos, gráficos ou outros elementos visuais em um documento PDF sem alterar seu conteúdo textual.
---

## Substituir uma Imagem em PDF

Como substituir uma imagem existente em uma página PDF por uma nova imagem? Implemente isso usando Aspose.PDF para Python via .NET.

1. Importar módulos necessários (aspose.pdf, os.path, FileIO).
1. Definir caminhos para:
- PDF de entrada (infile)
- Novo arquivo de imagem (image_file)
- PDF de saída (outfile)
1. Carregar o documento PDF usando 'apdf.Document(path_infile)'.
1. Abrir o novo arquivo de imagem em modo de leitura binária.
1. Substituir a primeira imagem na primeira página:
- 'document.pages[1].resources.images.replace(1, image_stream)'
1. Salvar o PDF atualizado em 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    with FileIO(path_image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(path_outfile)
```

## Substituir Imagem Específica

Este exemplo demonstra como substituir uma imagem específica em uma página PDF localizando-a via detecção de posicionamento de imagem.

1. Carregar o PDF usando 'apdf.Document()'.
1. Criar um 'ImagePlacementAbsorber' para coletar todos os posicionamentos de imagem na página.
1. Aceitar o absorvedor na primeira página ('document.pages[1].accept(absorber)').
1. Verificar se existem posicionamentos de imagem na página.
1. Selecionar o primeiro posicionamento de imagem (absorber.image_placements[1]) e substituí-lo.
1. Salvar o PDF modificado em 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = apdf.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(path_image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(path_outfile)
```

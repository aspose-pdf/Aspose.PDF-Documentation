---
title: Adicionar fundos de PDF em Python
linktitle: Adicionando fundos
type: docs
weight: 20
url: /pt/python-net/add-backgrounds/
description: Aprenda como adicionar uma imagem de fundo às páginas PDF em Python usando a classe BackgroundArtifact no Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar fundo a PDF com Python
Abstract: Este artigo discute o uso de imagens de fundo em documentos PDF usando Aspose.PDF for Python via .NET. Ele destaca a capacidade de adicionar marcas d'água ou designs sutis aos documentos ao utilizar a classe `BackgroundArtifact`, que permite a incorporação de imagens de fundo em objetos de página individuais. O artigo fornece um exemplo de código prático que demonstra como implementar esse recurso. O processo envolve criar um novo documento PDF, adicionar uma página, criar um objeto `BackgroundArtifact`, definir uma imagem de fundo e anexar o artefato de fundo à coleção de artefatos da página. Finalmente, o documento modificado é salvo como um arquivo PDF. Essa técnica permite uma apresentação visual aprimorada dos documentos PDF.
---

## Adicionar uma Imagem de Fundo a um PDF

Imagens de plano de fundo podem ser usadas para adicionar uma marca d'água ou outro design sutil a documentos. No Aspose.PDF for Python via .NET, cada documento PDF é uma coleção de páginas e cada página contém uma coleção de artefatos. O [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) classe pode ser usada para adicionar uma imagem de fundo a um objeto de página.

Essa abordagem é útil quando você precisa colocar uma imagem decorativa atrás do conteúdo principal do PDF sem transformá-la em texto pesquisável no documento.

O seguinte trecho de código mostra como adicionar uma imagem de fundo às páginas PDF usando o objeto BackgroundArtifact com Python.

1. Carregue o documento PDF.
1. Crie um BackgroundArtifact.
1. Carregue o arquivo de imagem.
1. Anexe o artefato a uma página.
1. Salve o documento atualizado.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Adicionar uma Imagem de Fundo com Opacidade a um PDF

Adicionar uma imagem de fundo semitransparente a uma página PDF usando Aspose.PDF for Python.

Ao aplicar opacidade, a imagem de fundo torna‑se parcialmente transparente, permitindo que o conteúdo original da página (texto, imagens, etc.) permaneça claramente visível. Isso é especialmente útil para:

- Marcas d'água
- Sobreposições de branding
- Aprimoramentos sutis de design

O plano de fundo é adicionado como um artefato, garantindo que permaneça atrás de todo o conteúdo da página.

1. Carregue o documento PDF.
1. Crie um BackgroundArtifact.
1. Carregue o arquivo de imagem.
1. Defina o nível de opacidade.
1. Anexe o artefato a uma página.
1. Salve o documento atualizado.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Adicionar uma Cor de Fundo a um PDF

Aplicar uma cor de fundo sólida a uma página PDF usando Aspose.PDF for Python.

1. Carregue o documento PDF.
1. Crie um BackgroundArtifact.
1. Definir a cor de fundo.
1. Anexe o artefato a uma página.
1. Salve o documento atualizado.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Remover plano de fundo de um PDF

Remover artefatos de plano de fundo de uma página PDF usando Aspose.PDF for Python.
Os planos de fundo em PDFs costumam ser armazenados como artefatos, e este método identifica seletivamente e remove apenas aqueles artefatos que são classificados como elementos de plano de fundo.

1. Carregue o documento PDF.
1. Acessar artefatos de página.
1. Filtrar artefatos de plano de fundo.
1. Coletar elementos de plano de fundo.
1. Excluir artefatos de plano de fundo.
1. Salve o documento atualizado.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## Tópicos de Artefatos Relacionados

- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)
- [Adicionar marcas d'água ao PDF em Python](/pdf/pt/python-net/add-watermarks/)
- [Adicionar numeração Bates ao PDF em Python](/pdf/pt/python-net/add-bates-numbering/)
- [Contar tipos de artefato em arquivos PDF](/pdf/pt/python-net/counting-artifacts/)
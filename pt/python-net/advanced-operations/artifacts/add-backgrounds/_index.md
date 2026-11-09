---
title: Adicionar fundos de PDF em Python
linktitle: Adicionar fundos
type: docs
weight: 20
url: /pt/python-net/add-backgrounds/
description: Adicionar fundos de imagem e de cor sólida às páginas PDF em Python e ajustar a opacidade da imagem de fundo.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar fundos em um PDF com Python
Abstract: Adicionar fundos de imagem e de cor sólida às páginas PDF em Python e ajustar a opacidade da imagem de fundo.
---

Usar `BackgroundArtifact` para colocar uma imagem ou cor sólida atrás do conteúdo de uma página PDF. Estes exemplos modificam a primeira página.

## Adicionar uma imagem de fundo ao PDF

Defina `background_image` com um fluxo de imagem e adicione o artefato à página.

```python
from io import FileIO
import aspose.pdf as ap

def add_background_image_to_pdf(infile, imagefile, outfile, opacity=1.0):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = opacity
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Adicionar uma imagem de fundo com opacidade a um PDF

Passe um valor de opacidade entre 0 e 1 para a mesma função. Use `0.5` para obter uma imagem semitransparente.

```python
add_background_image_to_pdf("input.pdf", "background.png", "output.pdf", opacity=0.5)
```

## Adicionar uma cor de fundo a um PDF

Defina `background_color` no artefato para aplicar uma cor sólida.

```python
import aspose.pdf as ap

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Tópicos relacionados

- [Remover Fundos](/pdf/pt/python-net/remove-backgrounds/)
- [Trabalhe com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)

---
title: Remover fundos de PDF em Python
linktitle: Remover fundos
type: docs
weight: 80
url: /pt/python-net/remove-backgrounds/
description: Remover artefatos de fundo da primeira página de um PDF em Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover fundos de um PDF com Python
Abstract: Remover artefatos de fundo da primeira página de um PDF em Python.
---

Remover artefatos de fundo da primeira página de um PDF em Python.

## Remover artefatos de fundo

Reúna os artefatos de paginação do subtipo `BACKGROUND` antes de excluí-los.

```python
import aspose.pdf as ap

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

## Tópicos relacionados

- [Adicionar Fundos](/pdf/pt/python-net/add-backgrounds/)
- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)

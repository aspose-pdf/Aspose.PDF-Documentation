---
title: Remover marcas d'água de PDF em Python
linktitle: Remover marcas d'água
type: docs
weight: 90
url: /pt/python-net/remove-watermarks/
description: Remover artefatos de marca d'água da primeira página de um PDF em Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover marcas d'água de um PDF com Python
Abstract: Remover artefatos de marca d'água da primeira página de um PDF em Python.
---

Remover artefatos de marca d'água da primeira página de um PDF em Python.

## Remover artefatos de marca d'água

O exemplo remove da primeira página apenas os artefatos do tipo `PAGINATION` e do subtipo `WATERMARK`. As marcas d’água visíveis armazenadas como texto comum da página, imagens ou anotações permanecem no PDF.

```python
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## Tópicos relacionados

- [Adicionar Marcas d'Água](/pdf/pt/python-net/add-watermarks/)
- [Extrair Detalhes da Marca d'Água](/pdf/pt/python-net/extract-watermarks/)
- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)

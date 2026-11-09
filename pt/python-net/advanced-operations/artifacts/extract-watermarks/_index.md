---
title: Extrair detalhes da marca d'água PDF em Python
linktitle: Extrair detalhes da marca d'água
type: docs
weight: 50
url: /pt/python-net/extract-watermarks/
description: Ler o texto e o retângulo delimitador dos artefatos de marca d'água na primeira página de um PDF em Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair detalhes da marca d'água em um PDF com Python
Abstract: Ler o texto e o retângulo delimitador dos artefatos de marca d'água na primeira página de um PDF em Python.
---

Ler o texto e o retângulo delimitador dos artefatos de marca d'água na primeira página de um PDF em Python.

## Ler texto e limites da marca d'água

Exiba o texto e o retângulo delimitador de cada artefato de paginação do subtipo `WATERMARK`.

```python
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## Tópicos relacionados

- [Adicionar marcas d'água](/pdf/pt/python-net/add-watermarks/)
- [Remover marcas d'água](/pdf/pt/python-net/remove-watermarks/)
- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)

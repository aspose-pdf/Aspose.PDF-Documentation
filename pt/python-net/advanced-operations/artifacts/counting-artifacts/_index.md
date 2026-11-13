---
title: Contar Artefatos PDF em Python
linktitle: Contando Artefatos
type: docs
weight: 40
url: /pt/python-net/counting-artifacts/
description: Contar marcas d'água, fundos, cabeçalhos e rodapés por subtipo de artefato de paginação em uma página PDF em Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Contando Artefatos em PDF usando Python
Abstract: Contar artefatos de paginação em uma página PDF para verificar marcas d'água, fundos, cabeçalhos e rodapés.
---

Contar artefatos de paginação em uma página PDF para verificar marcas d'água, fundos, cabeçalhos e rodapés.

## Contar artefatos por subtipo

Filtre a coleção `artifacts` da primeira página pelo tipo `PAGINATION` e conte os artefatos por subtipo. O exemplo exibe zero quando um subtipo está ausente.

```python
from collections import Counter
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## Tópicos relacionados

- [Trabalhe com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)
- [Extrair detalhes da marca d'água](/pdf/pt/python-net/extract-watermarks/)
- [Remover marcas d'água](/pdf/pt/python-net/remove-watermarks/)
- [Remover fundos](/pdf/pt/python-net/remove-backgrounds/)
- [Remover cabeçalhos e rodapés](/pdf/pt/python-net/remove-headers-footers/)

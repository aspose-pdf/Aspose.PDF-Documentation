---
title: Remover cabeçalhos e rodapés de PDF em Python
linktitle: Remover cabeçalhos e rodapés
type: docs
weight: 110
url: /pt/python-net/remove-headers-footers/
description: Remover artefatos de cabeçalho e rodapé da primeira página de um PDF em Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover cabeçalhos e rodapés em um PDF com Python
Abstract: Remover artefatos de cabeçalho e rodapé da primeira página de um PDF em Python.
---

Remover artefatos de cabeçalho e rodapé da primeira página de um PDF em Python.

## Remover artefatos de cabeçalho e rodapé

Reúna os artefatos de paginação dos subtipos `HEADER` ou `FOOTER` antes de excluí-los.

```python
import aspose.pdf as ap

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## Tópicos relacionados

- [Adicionar Cabeçalhos e Rodapés](/pdf/pt/python-net/artifacts-header-footer/)
- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)

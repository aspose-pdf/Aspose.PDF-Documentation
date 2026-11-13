---
title: Adicionar numeração Bates a PDF em Python
linktitle: Adicionar numeração Bates
type: docs
weight: 10
url: /pt/python-net/add-bates-numbering/
description: Adicionar identificadores sequenciais Bates às páginas de PDF em Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar numeração Bates em um PDF com Python
Abstract: Adicionar identificadores sequenciais Bates às páginas de PDF em Python.
---

A numeração Bates atribui identificadores sequenciais às páginas de um conjunto de documentos. Configure um `BatesNArtifact` para controlar o intervalo de páginas, número inicial, contagem de dígitos, prefixo, sufixo e posicionamento.

## Adicionar um artefato de numeração Bates

Passe o artefato configurado e as páginas do documento para `PageCollectionExtensions.add_bates_numbering`. O exemplo atribui às páginas existentes identificadores de seis dígitos a partir de `000001`.

```python
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact


def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Adicionar numeração Bates usando artefatos de paginação

Para aplicar a numeração Bates pela API de paginação, reutilize `_create_bates_artifact` do exemplo anterior e passe uma lista com o artefato para `PageCollectionExtensions.add_pagination`.

```python
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Tópicos relacionados

- [Remover Numeração Bates](/pdf/pt/python-net/remove-bates-numbering/)
- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)

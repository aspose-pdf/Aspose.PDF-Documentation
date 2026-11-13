---
title: Remover numeração Bates de PDF em Python
linktitle: Remover numeração Bates
type: docs
weight: 100
url: /pt/python-net/remove-bates-numbering/
description: Remover a numeração Bates de todas as páginas de um PDF em Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover a numeração Bates de um PDF com Python
Abstract: Remover a numeração Bates de todas as páginas de um PDF em Python.
---

Remover a numeração Bates de todas as páginas de um PDF em Python.

## Excluir numeração Bates

Passe as páginas do documento para `PageCollectionExtensions.delete_bates_numbering` e salve o PDF.

```python
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Tópicos relacionados

- [Adicionar Numeração Bates](/pdf/pt/python-net/add-bates-numbering/)
- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)

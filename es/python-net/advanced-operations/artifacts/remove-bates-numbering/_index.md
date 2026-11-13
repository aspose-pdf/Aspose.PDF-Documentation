---
title: Eliminar la numeración Bates de PDF en Python
linktitle: Eliminar numeración Bates
type: docs
weight: 100
url: /es/python-net/remove-bates-numbering/
description: Eliminar la numeración Bates de todas las páginas de un PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar la numeración Bates en un PDF con Python
Abstract: Eliminar la numeración Bates de todas las páginas de un PDF en Python.
---

Eliminar la numeración Bates de todas las páginas de un PDF en Python.

## Eliminar la numeración Bates

Pase las páginas del documento a `PageCollectionExtensions.delete_bates_numbering` y guarde el PDF.

```python
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Temas relacionados

- [Agregar numeración Bates](/pdf/es/python-net/add-bates-numbering/)
- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)

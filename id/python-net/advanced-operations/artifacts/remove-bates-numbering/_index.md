---
title: Menghapus penomoran Bates dari PDF dengan Python
linktitle: Menghapus penomoran Bates
type: docs
weight: 100
url: /id/python-net/remove-bates-numbering/
description: Hapus penomoran Bates dari semua halaman PDF menggunakan Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghapus penomoran Bates dari PDF dengan Python
Abstract: Hapus penomoran Bates dari semua halaman PDF menggunakan Python.
---

Hapus penomoran Bates dari semua halaman PDF menggunakan Python.

## Menghapus penomoran Bates

Teruskan halaman dokumen ke `PageCollectionExtensions.delete_bates_numbering`, lalu simpan PDF.

```python
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Topik terkait

- [Menambahkan penomoran Bates](/pdf/id/python-net/add-bates-numbering/)
- [Artefak PDF](/pdf/id/python-net/artifacts/)

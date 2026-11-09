---
title: Menambahkan penomoran Bates pada PDF dengan Python
linktitle: Menambahkan penomoran Bates
type: docs
weight: 10
url: /id/python-net/add-bates-numbering/
description: Tambahkan pengidentifikasi Bates berurutan ke halaman PDF dengan Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan penomoran Bates pada PDF dengan Python
Abstract: Tambahkan pengidentifikasi Bates berurutan ke halaman PDF dengan Python.
---

Penomoran Bates memberikan identifikasi berurutan pada halaman dalam sekumpulan dokumen. Konfigurasikan a `BatesNArtifact` untuk mengontrol rentang halaman, nomor mulai, jumlah digit, awalan, akhiran, dan penempatan.

## Menambahkan artefak penomoran Bates

Teruskan artefak yang telah dikonfigurasi beserta halaman dokumen ke `PageCollectionExtensions.add_bates_numbering`. Contoh ini memberi halaman yang ada pengenal enam digit mulai dari `000001`.

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

## Menambahkan penomoran Bates melalui artefak paginasi

Untuk menerapkan penomoran Bates melalui API paginasi, gunakan kembali `_create_bates_artifact` dari contoh sebelumnya. Teruskan daftar yang memuat artefak tersebut ke `PageCollectionExtensions.add_pagination`.

```python
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Topik terkait

- [Menghapus penomoran Bates](/pdf/id/python-net/remove-bates-numbering/)
- [Artefak PDF](/pdf/id/python-net/artifacts/)

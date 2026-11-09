---
title: Menghapus latar belakang dari PDF dengan Python
linktitle: Menghapus latar belakang
type: docs
weight: 80
url: /id/python-net/remove-backgrounds/
description: Hapus artefak latar belakang dari halaman pertama PDF menggunakan Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghapus latar belakang dari PDF dengan Python
Abstract: Hapus artefak latar belakang dari halaman pertama PDF menggunakan Python.
---

Hapus artefak latar belakang dari halaman pertama PDF menggunakan Python.

## Menghapus artefak latar belakang

Kumpulkan artefak paginasi dengan subtipe `BACKGROUND` sebelum menghapusnya.

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

## Topik terkait

- [Menambahkan latar belakang](/pdf/id/python-net/add-backgrounds/)
- [Artefak PDF](/pdf/id/python-net/artifacts/)

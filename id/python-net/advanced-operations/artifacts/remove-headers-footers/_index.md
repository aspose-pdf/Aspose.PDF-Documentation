---
title: Menghapus header dan footer dari PDF dengan Python
linktitle: Menghapus header dan footer
type: docs
weight: 110
url: /id/python-net/remove-headers-footers/
description: Hapus artefak header dan footer dari halaman pertama PDF dengan Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghapus header dan footer dari PDF dengan Python
Abstract: Hapus artefak header dan footer dari halaman pertama PDF dengan Python.
---

Hapus artefak header dan footer dari halaman pertama PDF dengan Python.

## Menghapus artefak header dan footer

Kumpulkan artefak paginasi dengan subtipe `HEADER` atau `FOOTER` sebelum menghapusnya.

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

## Topik terkait

- [Menambahkan header dan footer](/pdf/id/python-net/artifacts-header-footer/)
- [Artefak PDF](/pdf/id/python-net/artifacts/)

---
title: Remove PDF Headers and Footers in Python
linktitle: Remove Headers and Footers
type: docs
weight: 110
url: /python-net/remove-headers-footers/
description: Remove header and footer artifacts from the first page of a PDF in Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Headers and Footers in a PDF with Python
Abstract: Remove header and footer artifacts from the first page of a PDF in Python.
---

Remove header and footer artifacts from the first page of a PDF in Python.

## Remove header and footer artifacts

Collect pagination artifacts with the `HEADER` or `FOOTER` subtype before deleting them.

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

## Related Artifact Topics

- [Add Headers and Footers](/pdf/python-net/artifacts-header-footer/)
- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)

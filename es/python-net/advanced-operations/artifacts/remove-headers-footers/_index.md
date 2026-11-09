---
title: Eliminar encabezados y pies de página de PDF en Python
linktitle: Eliminar encabezados y pies de página
type: docs
weight: 110
url: /es/python-net/remove-headers-footers/
description: Eliminar artefactos de encabezado y pie de página de la primera página de un PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar encabezados y pies de página en un PDF con Python
Abstract: Eliminar artefactos de encabezado y pie de página de la primera página de un PDF en Python.
---

Eliminar artefactos de encabezado y pie de página de la primera página de un PDF en Python.

## Eliminar artefactos de encabezado y pie de página

Recopile los artefactos de paginación de los subtipos `HEADER` o `FOOTER` antes de eliminarlos.

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

## Temas relacionados

- [Agregar encabezados y pies de página](/pdf/es/python-net/artifacts-header-footer/)
- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)

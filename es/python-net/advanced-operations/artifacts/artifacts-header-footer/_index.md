---
title: Agregar encabezados y pies de página PDF en Python
linktitle: Agregar encabezados y pies de página
type: docs
weight: 70
url: /es/python-net/artifacts-header-footer/
description: Agregar artefactos de encabezado y pie de página con estilo a páginas PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar encabezados y pies de página en un PDF con Python
Abstract: Agregar artefactos de encabezado y pie de página con estilo a páginas PDF en Python.
---

Usar `HeaderArtifact` y `FooterArtifact` para agregar texto en movimiento a las páginas PDF. Estos ejemplos añaden artefactos a la primera página.

## Crear artefactos de texto con estilo

Defina la función auxiliar antes de ejecutar cualquiera de los ejemplos de adición. Aplica la misma fuente, tamaño, color y alineación a los encabezados y pies de página.

```python
import aspose.pdf as ap

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact
```

## Agregar encabezado al PDF

Pase `HeaderArtifact` a la función auxiliar y agregue el artefacto resultante a la página.

```python
import aspose.pdf as ap

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Agregar pie de página al PDF

Pase `FooterArtifact` a la función auxiliar y agregue el artefacto resultante a la página.

```python
import aspose.pdf as ap

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Temas relacionados

- [Eliminar encabezados y pies de página](/pdf/es/python-net/remove-headers-footers/)
- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)

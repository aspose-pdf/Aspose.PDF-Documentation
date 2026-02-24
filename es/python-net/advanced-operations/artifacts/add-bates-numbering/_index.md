---
title: Agregar artefacto de numeración Bates en Python mediante .NET
linktitle: Agregar numeración Bates
type: docs
weight: 10
url: /es/python-net/add-bates-numbering/
description: Aspose.PDF para Python a través de .NET le permite agregar numeración Bates a PDF.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar numeración Bates mediante Python
Abstract: La numeración Bates es una característica crítica en los flujos de trabajo de documentos legales, médicos y empresariales, garantizando que cada página de un conjunto reciba un identificador único y secuencial para una referencia fiable. Este artículo muestra cómo Aspose.PDF para Python a través de .NET simplifica la automatización de la numeración Bates mediante su API flexible. Usando la clase BatesNArtifact, los desarrolladores pueden configurar el comportamiento de la numeración, incluyendo la cantidad de dígitos, prefijos, sufijos, alineación y márgenes, y aplicarla programáticamente a lo largo de documentos completos. Se presentan múltiples enfoques, desde la aplicación directa del artefacto hasta la configuración basada en delegados, ofreciendo control tanto estático como dinámico. Además, la API soporta la eliminación completa de los números Bates con una única llamada a método, permitiendo la gestión completa del ciclo de vida de los artefactos de paginación. Ejemplos de código claros y paso a paso ilustran cómo agregar, personalizar y eliminar la numeración Bates, convirtiendo esta guía en un recurso práctico para desarrolladores que buscan optimizar los flujos de trabajo de procesamiento de documentos.
---

La numeración Bates se usa ampliamente en flujos de trabajo legales, médicos y empresariales para asignar identificadores únicos y secuenciales a las páginas dentro de un conjunto de documentos. Aspose.PDF para Python a través de .NET ofrece una API sencilla y flexible para automatizar este proceso, permitiéndole aplicar números Bates estandarizados programáticamente en cualquier PDF.

Usando la clase [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/), los desarrolladores pueden personalizar completamente el comportamiento de la numeración, incluyendo el número inicial, la cantidad de dígitos, los prefijos y sufijos, la alineación y los márgenes. Una vez configurado, el artefacto puede aplicarse al [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) mediante el método `add_bates_numbering` en la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) o añadirse como parte de una lista de objetos [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/). Aspose.PDF también admite un estilo de configuración basado en delegados, lo que permite un control dinámico de los ajustes del artefacto en tiempo de ejecución.

Además de crear números Bates, la API proporciona una manera fácil de eliminarlos usando `delete_bates_numbering`, ofreciendo una flexibilidad total en los flujos de trabajo de procesamiento de documentos.

Este artículo muestra múltiples métodos para agregar y eliminar la numeración Bates en un PDF usando Aspose.PDF para Python a través de .NET, con ejemplos claros de configuración, aplicación y eliminación del artefacto.

## Agregar artefacto de numeración Bates

Este ejemplo muestra cómo agregar programáticamente numeración Bates a un documento PDF usando Aspose.PDF para Python a través de .NET. Configurando un [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) con los ajustes deseados y aplicándolo a las páginas del documento, puede automatizar el proceso de agregar identificadores estandarizados a cada página.

Para agregar un artefacto de numeración Bates a un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), llame al método de extensión `AddBatesNumbering(BatesNArtifact)` en la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), pasando una instancia de [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) como parámetro:

```python

import aspose.pdf as ap

def add_bates_numbering(path_outfile):
    # Create a new or empty PDF document
    with ap.Document() as document:

        # Add 10 blank pages
        for _ in range(10):
            document.pages.add()

        # Create Bates numbering artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,  # 0 = apply until last page
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(bates)

        # Save the resulting PDF
        document.save(path_outfile)
```

O, puede pasar una colección de objetos [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/):

```python

import aspose.pdf as ap

def add_bates_numbering_collection(path_outfile):
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Create Bates artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add as a pagination artifact list
        document.pages.add_pagination([bates])

        # Save document
        document.save(path_outfile)
```

Agregar un artefacto de numeración Bates usando un delegado de acción:

```python

import aspose.pdf as ap

def add_bates_numbering_delegate(path_outfile):
    def configure_bates(b):
        """Configure Bates numbering artifact with desired settings."""
        b.start_page = 1
        b.end_page = 0
        b.subset = ap.Subset.ALL
        b.number_of_digits = 6
        b.start_number = 1
        b.prefix = ""
        b.suffix = ""
        b.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
        b.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
        b.right_margin = 72
        b.left_margin = 72
        b.top_margin = 36
        b.bottom_margin = 36
        b.text_state.font_size = 10
    
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Use delegate function to configure Bates artifact
        document.pages.add_bates_numbering(configure_bates)

        # Save output PDF
        document.save(path_outfile)
```

## Eliminar numeración Bates

Para eliminar la numeración Bates de un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), use el método `delete_bates_numbering()` en la [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python

import aspose.pdf as ap

def delete_bates_numbering(path_infile, path_outfile):
    with ap.Document(path_infile) as document:

        # Remove Bates numbering from all pages
        document.pages.delete_bates_numbering()

        # Save updated document
        document.save(path_outfile)
```

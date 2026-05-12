---
title: Agregar numeración Bates a PDF en Python
linktitle: Agregar numeración Bates
type: docs
weight: 10
url: /es/python-net/add-bates-numbering/
description: Aprenda cómo agregar y eliminar la numeración Bates en documentos PDF usando Python con Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar numeración Bates vía Python
Abstract: La numeración Bates es una característica crítica en los flujos de trabajo de documentos legales, médicos y empresariales, garantizando que cada página de un conjunto reciba un identificador único y secuencial para una referencia fiable. Este artículo muestra cómo Aspose.PDF for Python via .NET simplifica la automatización de la numeración Bates a través de su API flexible. Usando la clase BatesNArtifact, los desarrolladores pueden configurar el comportamiento de la numeración —incluyendo el recuento de dígitos, prefijos, sufijos, alineación y márgenes— y aplicarlo programáticamente en documentos completos. Se presentan varios enfoques, desde la aplicación directa del artefacto hasta la configuración basada en delegados, ofreciendo control tanto estático como dinámico. Además, la API admite la eliminación completa de los números Bates con una única llamada al método, lo que permite una gestión de ciclo de vida completa de los artefactos de paginación. Ejemplos de código claros y paso a paso ilustran cómo añadir, personalizar y eliminar la numeración Bates, convirtiendo esta guía en un recurso práctico para desarrolladores que buscan optimizar los flujos de trabajo de procesamiento de documentos.
---

La numeración Bates se usa ampliamente en flujos de trabajo legales, médicos y empresariales para asignar identificadores únicos y secuenciales a las páginas dentro de un conjunto de documentos. Aspose.PDF for Python via .NET ofrece una API simple y flexible para automatizar este proceso, permitiéndote aplicar números Bates estandarizados de forma programática en cualquier PDF.

Usando el [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) clase, los desarrolladores pueden personalizar completamente el comportamiento de la numeración—incluyendo el número inicial, la cantidad de dígitos, los prefijos y sufijos, la alineación y los márgenes. Una vez configurado, el artefacto puede aplicarse al [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) a través del `add_bates_numbering` método en el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) o añadido como parte de una lista de [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) objetos. Aspose.PDF también admite un estilo de configuración basado en delegados, que permite el control dinámico de la configuración de artefactos en tiempo de ejecución.

Además de crear números Bates, la API proporciona una forma fácil de eliminarlos usando `delete_bates_numbering`, ofreciendo una flexibilidad completa en los flujos de trabajo de procesamiento de documentos.

Este artículo muestra varios métodos para agregar y eliminar la numeración Bates en un PDF usando Aspose.PDF for Python via .NET, con ejemplos claros de configuración, aplicación y eliminación de artefactos.

## Agregar artefacto de numeración Bates

Este ejemplo muestra cómo agregar programáticamente la numeración Bates a un documento PDF usando Aspose.PDF for Python via .NET. Configurando un [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) con los ajustes deseados y aplicándolo a las páginas del documento, puede automatizar el proceso de añadir identificadores estandarizados a cada página.

Para agregar un artefacto de numeración Bates a un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), llama al `AddBatesNumbering(BatesNArtifact)` método de extensión en el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), pasando un [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) instancia como el parámetro:

```python
import sys
from os import path
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
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Agregar numeración Bates usando artefactos de paginación

Agregar numeración Bates a un PDF usando la colección de artefactos de paginación en Aspose.PDF for Python:

1. Cargue el documento PDF.
1. Inserte páginas extra si es necesario antes de aplicar la numeración.
1. Cree un artefacto Bates.
1. Configure las propiedades del artefacto.
1. Añada el artefacto a la colección de paginación.
1. Aplicar paginación a las páginas.
1. Guarde el documento actualizado.

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Eliminar numeración Bates

Para eliminar la numeración Bates de un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), use el `delete_bates_numbering()` método en el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Temas relacionados con artefactos

- [Trabajar con artefactos PDF en Python](/pdf/es/python-net/artifacts/)
- [Agregar marcas de agua a PDF en Python](/pdf/es/python-net/add-watermarks/)
- [Agregar fondos PDF en Python](/pdf/es/python-net/add-backgrounds/)
- [Contar tipos de artefactos en archivos PDF](/pdf/es/python-net/counting-artifacts/)
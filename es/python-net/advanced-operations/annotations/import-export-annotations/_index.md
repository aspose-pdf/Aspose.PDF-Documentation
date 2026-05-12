---
title: Importar y exportar anotaciones usando Python
linktitle: Importar y exportar anotaciones
type: docs
weight: 80
url: /es/python-net/import-export-annotations/
description: Aprenda cómo importar anotaciones de un PDF y exportarlas a un nuevo documento PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transfiera anotaciones PDF entre documentos en Python.
Abstract: Este artículo explica cómo copiar anotaciones de un PDF de origen y exportarlas a un nuevo documento PDF utilizando Aspose.PDF for Python via .NET. La guía divide el proceso en pasos pequeños, incluyendo la carga del archivo de origen, la creación del documento de destino, la adición de una página, la copia de anotaciones de la primera página y el guardado del resultado.
---

Este artículo muestra cómo importar anotaciones de un PDF existente y exportarlas a un nuevo documento PDF usando Aspose.PDF for Python via .NET.

El ejemplo lee anotaciones de la primera página de un archivo de origen, crea un nuevo PDF, añade una página en blanco y copia cada anotación a esa nueva página. Este enfoque es útil cuando necesitas mover comentarios, marcas o notas de revisión a un documento de salida separado.

## Cargar el PDF de origen

Crear una `Document` objeto para el archivo de entrada que ya contiene anotaciones. Este objeto brinda acceso a la colección de páginas y a las anotaciones almacenadas en cada página.

```python
source_document = ap.Document(infile)
```

## Crear el PDF de destino

A continuación, cree un documento PDF vacío que recibirá las anotaciones importadas. En esta etapa, el documento de destino no contiene ninguna página.

```python
destination_document = ap.Document()
```

## Agregar una página para anotaciones exportadas

Dado que las anotaciones deben pertenecer a una página, añada una nueva página al documento de destino antes de copiar cualquier cosa.

```python
page = destination_document.pages.add()
```

## Copiar anotaciones de la página de origen

Iterar a través de la colección de anotaciones en la primera página del PDF de origen y agregar cada anotación a la nueva página en el documento de destino.

El segundo argumento en `page.annotations.add(annot, True)` indica a Aspose.PDF que copie la anotación en la página de destino en lugar de solo reutilizar la referencia de objeto existente.

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## Guarda el documento de salida

Después de que se hayan copiado todas las anotaciones, guarde el documento de destino para crear el archivo PDF final.

```python
destination_document.save(outfile)
```

## Ejemplo completo

El siguiente código combina todos los pasos en una función reutilizable:

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## Temas relacionados

- [Anotaciones interactivas](/python-net/interactive-annotations/)
- [Anotaciones de marcado](/python-net/markup-annotations/)
- [Anotaciones de medios](/python-net/media-annotations/)
- [Anotaciones de Seguridad](/python-net/security-annotations/)
- [Anotaciones de forma](/python-net/shape-annotations/)
- [Anotaciones basadas en texto](/python-net/text-based-Annotations/)
- [Anotaciones de Marca de Agua](/python-net/watermark-annotations/)

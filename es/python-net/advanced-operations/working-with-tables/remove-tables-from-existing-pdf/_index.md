---
title: Eliminar tablas de documentos PDF existentes
linktitle: Eliminar tablas
description: Aprenda cómo eliminar una o más tablas de documentos PDF existentes en Python.
lastmod: "2026-05-05"
type: docs
weight: 50
url: /es/python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar una o varias tablas de archivos PDF con Python
Abstract: Este artículo explica cómo eliminar tablas de documentos PDF existentes usando Aspose.PDF for Python via .NET. Introduce `TableAbsorber` para localizar tablas y muestra cómo eliminar una sola tabla o eliminar todas las tablas detectadas de una página.
---

## Eliminar tabla de documento PDF

Aspose.PDF for Python le permite eliminar una tabla de un PDF. Abre un PDF existente, detecta la primera tabla en la primera página con `TableAbsorber`, elimina esa tabla usando `remove()`, y guarda el PDF actualizado en un nuevo archivo.

Utilice esta página cuando necesite limpiar PDFs con muchas tablas, eliminar contenido tabular desactualizado o simplificar documentos antes de redistribuirlos.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## Eliminar todas las tablas del documento PDF

Con nuestra biblioteca, puedes eliminar todas las tablas de una página específica en un PDF. El código abre un PDF existente, detecta todas las tablas en la segunda página con TableAbsorber, recorre las tablas detectadas, elimina cada una y luego guarda el PDF modificado en un nuevo archivo. Es útil cuando necesitas eliminar en bloque las tablas de una página mientras dejas intacto el resto del contenido del PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## Temas relacionados de la tabla

- [Trabajar con tablas en PDF usando Python](/pdf/es/python-net/working-with-tables/)
- [Agregar tablas al PDF usando Python](/pdf/es/python-net/adding-tables/)
- [Extraer tablas de documentos PDF](/pdf/es/python-net/extracting-table/)
- [Manipular tablas en PDFs existentes](/pdf/es/python-net/manipulating-tables/)
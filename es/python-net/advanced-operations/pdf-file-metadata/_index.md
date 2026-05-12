---
title: Trabajar con metadatos de archivos PDF en Python
linktitle: Metadatos de archivos PDF
type: docs
weight: 200
url: /es/python-net/pdf-file-metadata/
description: Aprenda cómo extraer, actualizar y administrar los metadatos de archivos PDF y las propiedades XMP en Python usando Aspose.PDF.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenga y establezca la información del documento PDF y los metadatos XMP en Python
Abstract: Este artículo explica cómo trabajar con los metadatos de PDF en Aspose.PDF for Python via .NET. Aprenda cómo leer la información del documento, como autor, título y palabras clave, actualizar las propiedades del archivo, establecer campos de metadatos XMP y registrar prefijos de metadatos personalizados para archivos PDF en Python.
---

Utilice esta guía cuando necesite inspeccionar las propiedades del documento, actualizar la información del archivo PDF para búsqueda o catalogación, o gestionar los metadatos XMP programáticamente en Python.

## Obtener información del archivo PDF

Este fragmento de código muestra cómo extraer metadatos de un documento PDF usando Aspose.PDF for Python via .NET. Al acceder a la propiedad info del objeto Document, recupera información clave como el autor, la fecha de creación, las palabras clave, la fecha de modificación, el asunto y el título. Esta funcionalidad es esencial para aplicaciones que requieren catalogación de documentos, optimización de búsquedas o validación de las propiedades del documento.

1. Abra el archivo PDF usando la clase Document
1. Recupera los metadatos del documento a través de la propiedad info
1. Muestre la información de los metadatos. Imprima los campos de metadatos deseados

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## Establecer información del archivo PDF

Aspose.PDF for Python via .NET le permite establecer información específica del archivo para un PDF, información como autor, fecha de creación, tema y título. Para establecer esta información:

1. Abra el archivo PDF usando la clase Document.
1. Cree un [DocumentInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) objeto y establezca las propiedades de metadatos deseadas.
1. Guarde los cambios en un nuevo archivo PDF usando el método save.

El siguiente fragmento de código le muestra cómo establecer la información del archivo PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## Establecer metadatos XMP en un archivo PDF

Este fragmento de código demuestra cómo establecer o actualizar programáticamente los metadatos XMP en un documento PDF usando Aspose.PDF for Python via .NET. Al modificar propiedades como xmp:CreateDate, xmp:Nickname y campos definidos por el usuario, puedes incrustar metadatos estandarizados en tus archivos PDF. Este enfoque es particularmente útil para mejorar la organización de documentos, facilitar la búsqueda e incrustar información esencial directamente en el archivo.

Aspose.PDF le permite establecer metadatos en un archivo PDF. Para establecer metadatos:

1. Abra el archivo PDF usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.
1. Modifique los metadatos XMP asignando valores a claves específicas.
1. Guarde el documento PDF actualizado.

El siguiente fragmento de código le muestra cómo establecer metadatos en un archivo PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## Insertar metadatos con prefijo

Algunos desarrolladores necesitan crear un nuevo espacio de nombres de metadatos con un prefijo. El siguiente fragmento de código muestra cómo insertar metadatos con prefijo.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## Temas relacionados

- [Operaciones avanzadas de PDF en Python](/pdf/es/python-net/advanced-operations/)
- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Trabajar con archivos adjuntos PDF en Python](/pdf/es/python-net/attachments/)
- [Comparar documentos PDF en Python](/pdf/es/python-net/compare-pdf-documents/)

---
title: Trabajar con metadatos de archivos PDF en Python
linktitle: Metadatos de archivos PDF
type: docs
weight: 200
url: /es/python-net/pdf-file-metadata/
description: Aprenda cómo extraer, actualizar y gestionar los metadatos de archivos PDF y las propiedades XMP en Python usando Aspose.PDF.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenga y establezca la información del documento PDF y los metadatos XMP en Python
Abstract: Este articulo explica como trabajar con los metadatos PDF en Aspose.PDF para Python a traves de .NET. Aprenda como leer la informacion del documento, como autor, titulo y palabras clave, actualizar propiedades del archivo, establecer campos de metadatos XMP y registrar prefijos de metadatos personalizados para archivos PDF en Python.
---

Utilice esta guía cuando necesite inspeccionar las propiedades del documento, actualizar la información del archivo PDF para búsqueda o catalogación, o gestionar los metadatos XMP programáticamente en Python.

## Obtener información del archivo PDF

Este fragmento de codigo demuestra como extraer metadatos de un documento PDF usando Aspose.PDF para Python a traves de .NET. Al acceder a la propiedad `info` del objeto `Document`, recupera informacion clave como el autor, la fecha de creacion, las palabras clave, la fecha de modificacion, el asunto y el titulo. Esta funcionalidad es esencial para aplicaciones que requieren catalogacion de documentos, optimizacion de busquedas o validacion de propiedades del documento.

1. Abra el archivo PDF usando la clase Document
1. Recupera los metadatos del documento mediante la propiedad info
1. Muestra la información de los metadatos. Imprime los campos de metadatos deseados

```python
import aspose.pdf as ap


def get_pdf_file_information():
    # The path to the documents directory
    data_dir = RunExamples.get_data_dir_asposepdf()

    # Open PDF document
    document = ap.Document(data_dir + "GetFileInfo.pdf")

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

Aspose.PDF para Python a traves de .NET le permite establecer informacion especifica del archivo para un PDF, como autor, fecha de creacion, asunto y titulo. Para establecer esta informacion:

1. Abra el archivo PDF usando la clase Document.
1. Cree un objeto [DocumentInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) y establezca las propiedades de metadatos deseadas.
1. Guarde los cambios en un nuevo archivo PDF utilizando el método save.

El siguiente fragmento de código le muestra cómo establecer la información del archivo PDF.

```python
import aspose.pdf as ap
import datetime


def set_file_information():
    # The path to the documents directory
    data_dir = RunExamples.get_data_dir_asposepdf_workingdocuments()

    # Open PDF document
    document = ap.Document(data_dir + "SetFileInfo.pdf")

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
    document.save(data_dir + "SetFileInfo_out.pdf")
```

## Establecer metadatos XMP en un archivo PDF

Este fragmento de codigo demuestra como establecer o actualizar programaticamente los metadatos XMP en un documento PDF usando Aspose.PDF para Python a traves de .NET. Al modificar propiedades como `xmp:CreateDate`, `xmp:Nickname` y campos definidos a medida, puede incrustar metadatos estandarizados en sus archivos PDF. Este enfoque es especialmente util para mejorar la organizacion de documentos, facilitar la capacidad de busqueda y añadir informacion esencial directamente al archivo.

Aspose.PDF le permite establecer metadatos en un archivo PDF. Para establecer metadatos:

1. Abra el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Modifique los metadatos XMP asignando valores a claves específicas.
1. Guarde el Documento PDF actualizado.

El siguiente fragmento de código le muestra cómo establecer metadatos en un archivo PDF.

```python
import aspose.pdf as ap
import datetime


def set_xmp_metadata():
    # The path to the documents directory
    data_dir = RunExamples.get_data_dir_asposepdf()

    # Open PDF document
    document = ap.Document(data_dir + "SetXMPMetadata.pdf")

    # Set XMP metadata properties
    document.metadata["xmp:CreateDate"] = datetime.datetime.now().isoformat()
    document.metadata["xmp:Nickname"] = "Nickname"
    document.metadata["xmp:CustomProperty"] = "Custom Value"

    # Save the updated PDF document
    document.save(data_dir + "SetXMPMetadata_out.pdf")
```

## Insertar metadatos con prefijo

Algunos desarrolladores necesitan crear un nuevo espacio de nombres de metadatos con un prefijo. El siguiente fragmento de código muestra cómo insertar metadatos con prefijo.

```python
import aspose.pdf as ap
import datetime


def set_prefix_metadata():
    # The path to the documents directory
    data_dir = RunExamples.get_data_dir_asposepdf()

    # Open PDF document
    document = ap.Document(data_dir + "SetXMPMetadata.pdf")

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata[
        "xmp:ModifyDate"
    ] = datetime.datetime.now().isoformat()  # ISO 8601 format

    # Save the updated PDF document
    document.save(data_dir + "SetPrefixMetadata_out.pdf")
```

## Temas Relacionados

- [Operaciones avanzadas de PDF en Python](/pdf/es/python-net/advanced-operations/)
- [Trabaja con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Trabajar con archivos adjuntos PDF en Python](/pdf/es/python-net/attachments/)
- [Comparar documentos PDF en Python](/pdf/es/python-net/compare-pdf-documents/)

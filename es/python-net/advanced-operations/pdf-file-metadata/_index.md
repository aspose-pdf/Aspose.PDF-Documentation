---
title: Trabajar con metadatos de archivos PDF en Python
linktitle: Metadatos de archivos PDF
type: docs
weight: 200
url: /es/python-net/pdf-file-metadata/
description: Explora cómo extraer y gestionar los metadatos de PDF, como el autor y el título, en Python usando Aspose.PDF.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtener y establecer metadatos en PDF usando Python
Abstract: El artículo ofrece una guía completa sobre la manipulación de los metadatos de PDF utilizando Aspose.PDF para Python a través de .NET. Describe métodos para extraer y establecer propiedades de metadatos, incluyendo autor, fecha de creación, palabras clave y más, que son cruciales para la catalogación de documentos, la optimización de búsquedas o la validación. Los fragmentos de código demuestran cómo recuperar los metadatos de un PDF usando la clase `Document` y la propiedad `info`, establecer nuevos metadatos mediante el objeto `DocumentInfo` y guardar los cambios. Además, muestra cómo actualizar programáticamente los metadatos XMP, lo que mejora la organización y la capacidad de búsqueda de los documentos. El artículo también explica cómo insertar metadatos con un prefijo personalizado registrando un URI de espacio de nombres. Estas funcionalidades son esenciales para los desarrolladores que buscan gestionar la información de documentos PDF de manera eficaz dentro de aplicaciones.
---

## Obtener información del archivo PDF

Este fragmento de código muestra cómo extraer metadatos de un documento PDF usando Aspose.PDF para Python a través de .NET. Al acceder a la propiedad info del objeto Document, recupera información clave como el autor, la fecha de creación, palabras clave, fecha de modificación, asunto y título. Esta funcionalidad es esencial para aplicaciones que requieren catalogar documentos, optimizar búsquedas o validar las propiedades del documento.

1. Abrir el archivo PDF usando la clase Document
1. Recuperar los metadatos del documento a través de la propiedad info
1. Mostrar información de metadatos. Imprimir los campos de metadatos deseados

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

Aspose.PDF para Python a través de .NET le permite establecer información específica de archivo para un PDF, información como autor, fecha de creación, asunto y título. Para establecer esta información:

1. Abrir el archivo PDF usando la clase Document.
1. Crear un objeto [DocumentInfo]() y establecer las propiedades de metadatos deseadas.
1. Guardar los cambios en un nuevo archivo PDF usando el método save.

El siguiente fragmento de código muestra cómo establecer la información del archivo PDF.

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

Este fragmento de código muestra cómo establecer o actualizar programáticamente los metadatos XMP en un documento PDF usando Aspose.PDF para Python a través de .NET. Al modificar propiedades como xmp:CreateDate, xmp:Nickname y campos definidos por el usuario, puedes incrustar metadatos estandarizados en tus archivos PDF. Este enfoque es especialmente útil para mejorar la organización de documentos, facilitar la búsqueda y agregar información esencial directamente al archivo.

Aspose.PDF le permite establecer metadatos en un archivo PDF. Para establecer metadatos:

1. Abrir el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Modificar los metadatos XMP asignando valores a claves específicas.
1. Guardar el documento PDF actualizado.

El siguiente fragmento de código muestra cómo establecer metadatos en un archivo PDF.

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
        document.metadata["xmp:ModifyDate"] = datetime.datetime.now().isoformat()  # ISO 8601 format

        # Save the updated PDF document
        document.save(data_dir + "SetPrefixMetadata_out.pdf")
```

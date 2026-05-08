---
title: Crear PDF compatible con PDF/3-A y adjuntar factura ZUGFeRD en Python
linktitle: Adjuntar ZUGFeRD a PDF
type: docs
weight: 10
url: /es/python-net/attach-zugferd/
description: Aprenda cómo generar un documento PDF con ZUGFeRD en Aspose.PDF para Python a través de .NET
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo adjuntar ZUGFeRD a un documento PDF
Abstract: El artículo ofrece una guía paso a paso sobre cómo adjuntar ZUGFeRD (un formato de facturas electrónicas) a un documento PDF utilizando la biblioteca Aspose.PDF. El procedimiento comienza importando la biblioteca necesaria y configurando las rutas de directorio para los archivos de entrada y salida. Implica cargar el archivo PDF objetivo en un objeto Document y crear un objeto FileSpecification para el archivo XML de metadatos de la factura. Propiedades clave como `mime_type` y `af_relationship` se establecen para garantizar una integración adecuada de los metadatos. Luego, el archivo XML se agrega a la colección de archivos incrustados del PDF, adjuntándolo efectivamente como metadatos. Posteriormente, el documento PDF se convierte al formato PDF/A-3A, que es adecuado para archivar documentos electrónicos, antes de guardar el PDF final con el ZUGFeRD incrustado. El artículo concluye con un fragmento de código Python que demuestra la implementación de estos pasos, mostrando la integración de ZUGFeRD con un PDF para una mejor gestión documental.
---

## Adjuntar ZUGFeRD a PDF

Recomendamos los siguientes pasos para adjuntar ZUGFeRD al PDF:

1. Importe la biblioteca Aspose.PDF y asígnele el alias ap para mayor comodidad.
1. Defina la ruta al directorio donde se encuentran los archivos PDF de entrada y salida.
1. Defina la ruta al archivo PDF que será procesado.
1. Cargue el archivo PDF desde la variable de ruta y cree un objeto Document.
1. Cree un objeto FileSpecification para el archivo XML que contiene los metadatos de la factura. Use la variable de ruta y una cadena de descripción para crear el objeto FileSpecification.
1. Establecer el `mime_type` y el `af_relationship` propiedades del objeto FileSpecification a `text/xml` y `ALTERNATIVE`, respectivamente.
1. Añada el objeto fileSpecification a la colección de archivos incrustados del objeto document. Esto adjunta el archivo XML al documento PDF como un archivo de metadatos de factura.
1. Convertir el documento PDF al formato PDF/A-3A. Utilice la ruta al archivo de registro, el `PdfFormat.PDF_A_3A` enumeración, y el `ConvertErrorAction.DELETE` enumeración para convertir el objeto del documento.
1. Guarde el documento PDF con el ZUGFeRD adjunto.

```python
import sys
import os
import aspose.pdf as ap

def attach_invoice_zugferd_format(infile, invoice, outfile):
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

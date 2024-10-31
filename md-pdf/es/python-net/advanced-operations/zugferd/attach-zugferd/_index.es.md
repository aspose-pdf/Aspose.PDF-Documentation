---
title: Creación de PDF compatible con PDF/3-A y adjuntar factura ZUGFeRD en Python
linktitle: Adjuntar ZUGFeRD al PDF
type: docs
weight: 10
url: /python-net/attach-zugferd/
description: Aprenda a generar un documento PDF con ZUGFeRD en Aspose.PDF para Python a través de .NET
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adjuntar ZUGFeRD al PDF

Recomendamos seguir los siguientes pasos para adjuntar ZUGFeRD al PDF:

1. Importe la biblioteca Aspose.PDF y asígnele un alias de ap para mayor comodidad.
1. Defina la ruta al directorio donde se encuentran los archivos PDF de entrada y salida.
1. Defina la ruta al archivo PDF que se procesará.
1. Cargue el archivo PDF desde la variable de ruta y cree un objeto Document.
1. Cree un objeto FileSpecification para el archivo XML que contiene los metadatos de la factura. Use la variable de ruta y una cadena de descripción para crear el objeto FileSpecification.

1. Establece las propiedades `mime_type` y `af_relationship` del objeto FileSpecification a `text/xml` y `ALTERNATIVE`, respectivamente.
1. Agrega el objeto fileSpecification a la colección de archivos incrustados del objeto documento. Esto adjunta el archivo XML al documento PDF como un archivo de metadatos de factura.
1. Convierte el documento PDF al formato PDF/A-3A. Usa la ruta al archivo de registro, la enumeración `PdfFormat.PDF_A_3A` y la enumeración `ConvertErrorAction.DELETE` para convertir el objeto documento.
1. Guarda el documento PDF con el ZUGFeRD adjunto.

```python
import aspose.pdf as ap

# Define la ruta al directorio donde se encuentran los archivos PDF de entrada y salida
_dataDir = "./"

# Carga el archivo PDF que será procesado
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Crea un objeto FileSpecification para el archivo XML que contiene los metadatos de la factura
description = "Metadatos de factura conformes al estándar ZUGFeRD"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Establece el tipo MIME y las propiedades AFRelationship del archivo incrustado
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Agrega el archivo incrustado a la colección de archivos incrustados del documento PDF
document.embedded_files.add("factur",fileSpecification)

# Convierte el documento PDF al formato PDF/A-3A
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Guarda el documento PDF con el ZUGFeRD adjunto
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```
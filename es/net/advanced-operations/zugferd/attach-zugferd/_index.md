---
title: Creando PDF/3-A conforme a PDF y adjuntando factura ZUGFeRD en C#
linktitle: Adjuntar ZUGFeRD a PDF
type: docs
weight: 10
url: /es/net/attach-zugferd/
description: Aprende cómo generar un documento PDF con ZUGFeRD en Aspose.PDF para .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adjuntar ZUGFeRD a PDF

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

Recomendamos seguir los siguientes pasos para adjuntar ZUGFeRD a PDF:

* Definir una variable de ruta que apunte a una carpeta donde se encuentren los archivos PDF de entrada y salida.
* Crear un objeto de documento cargando un archivo PDF existente (por ejemplo, "ZUGFeRD-test.pdf") desde la ruta.
* Crear un objeto [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) proporcionando la ruta y descripción de otro archivo llamado "factur-x.xml", que contiene metadatos de factura conforme al estándar ZUGFeRD.
* Añadir propiedades al objeto de especificación de archivo, tales como la descripción, tipo MIME y relación AF.
* Agregar propiedades al objeto de especificación de archivo, como la descripción, el tipo MIME y la relación AF.
* Agregar el objeto de especificación de archivo a la colección de archivos incrustados del documento. El nombre del archivo debe especificarse según el estándar ZUGFeRD, por ejemplo, "factur-x.xml".
* Convertir el documento al formato PDF/A-3U, un subconjunto de PDF que garantiza la preservación a largo plazo de los documentos electrónicos. PDF/A-3U permite incrustar archivos de cualquier formato en documentos PDF.
* Guardar el documento convertido como un nuevo archivo PDF (por ejemplo, "ZUGFeRD-res.pdf").

```cs
var path = @"C:\Samples\ZUGFeRD\";

var document = new Aspose.Pdf.Document(Path.Combine(path,"ZUGFeRD-test.pdf"));
// Configurar nuevo archivo para ser añadido como adjunto
var description = "Metadatos de factura conforme al estándar ZUGFeRD";
var fileSpecification = new Aspose.Pdf.FileSpecification(Path.Combine(path, "factur-x.xml"), description)
{
    Description = "Zugferd",
    MIMEType = "text/xml",
    AFRelationship = Aspose.Pdf.AFRelationship.Alternative
};
// Añadir adjunto a la colección de archivos incrustados del documento
document.EmbeddedFiles.Add(fileSpecification);
document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.PDF_A_3U, Aspose.Pdf.ConvertErrorAction.Delete);
document.Save(Path.Combine(path, "ZUGFeRD-res.pdf"));
```
El método convert toma un flujo, un formato PDF y una acción de error de conversión como parámetros. El parámetro de flujo se puede utilizar para guardar el registro de conversión. El parámetro de acción de error de conversión especifica qué hacer si ocurren errores durante la conversión. En este caso, está configurado en "Eliminar", lo que significa que cualquier elemento que no cumpla con el formato PDF/A-3U será eliminado del documento.

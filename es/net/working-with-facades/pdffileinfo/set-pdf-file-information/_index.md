---
title: Establecer Información del Archivo PDF
type: docs
weight: 40
url: es/net/set-pdf-file-information/
description: Esta sección explica cómo establecer la Información del Archivo PDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

La clase [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) permite establecer información específica del archivo de un archivo PDF. Necesitas crear un objeto de la clase [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) y luego establecer diferentes propiedades específicas del archivo como Autor, Título, Palabra clave y Creador, etc. Finalmente, guarda el archivo PDF actualizado usando el método [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) del objeto [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo).

El siguiente fragmento de código te muestra cómo establecer la información del archivo PDF.

```csharp
 public static void SetPdfInfo()
        {
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf")
            {
                // Establecer información del PDF
                Author = "Aspose",
                Title = "Hello World!",
                Keywords = "Peace and Development",
                Creator = "Aspose"
            };
            // Guardar archivo actualizado
            fileInfo.SaveNewInfo(_dataDir + "SetFileInfo_out.pdf");
        }
```

## Set Meta Info

[SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) método te permite agregar cualquier información. En nuestro ejemplo, agregamos un campo. Consulta el siguiente fragmento de código:

```csharp
 public static void SetMetaInfo()
        {
            // Crear instancia del objeto PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "sample.pdf");

            // Establecer nuevo atributo de cliente como metainformación
            fInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

            // Guardar archivo actualizado
            fInfo.SaveNewInfo(_dataDir + "SetMetaInfo_out.pdf");
```
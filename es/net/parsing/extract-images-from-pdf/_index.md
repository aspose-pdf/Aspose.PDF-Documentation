---
title: Extraer imágenes de PDF C#
linktitle: Extraer imágenes de PDF
type: docs
weight: 20
url: /es/net/extract-images-from-the-pdf-file/
description: Cómo extraer una parte de la imagen de un PDF usando Aspose.PDF para .NET en C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Las imágenes se encuentran en la colección [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) de cada página, dentro de la colección [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images). Para extraer una página en particular, luego obtén la imagen de la colección Images utilizando el índice específico de la imagen.

El índice de la imagen devuelve un objeto [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage). Este objeto proporciona un método Save que se puede usar para guardar la imagen extraída. El siguiente fragmento de código muestra cómo extraer imágenes de un archivo PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

 ```csharp
 // Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
```

// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractImages.pdf");

// Extraer una imagen en particular
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// Guardar la imagen de salida
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// Guardar el archivo PDF actualizado
pdfDocument.Save(dataDir);
```

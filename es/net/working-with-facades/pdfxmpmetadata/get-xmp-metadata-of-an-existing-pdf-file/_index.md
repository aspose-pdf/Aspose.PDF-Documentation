---
title: Obtener Metadatos XMP de un Archivo PDF
type: docs
weight: 30
url: /es/net/get-xmp-metadata-of-an-existing-pdf-file/
description: Esta sección explica cómo obtener metadatos XMP de un PDF existente con Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Para obtener metadatos XMP de un archivo PDF, necesitas crear un objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) y vincular el archivo PDF usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Puedes pasar propiedades específicas de metadatos XMP al objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) para obtener sus valores. El siguiente fragmento de código muestra cómo obtener metadatos XMP de un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Crear objeto PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Vincular archivo pdf al objeto
xmpMetaData.BindPdf( dataDir + "input.pdf");

// Obtener propiedades de Metadatos XMP
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreateDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.MetadataDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreatorTool].ToString());
Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

Console.ReadLine();
```
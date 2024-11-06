---
title: Dapatkan Metadata XMP dari File PDF
type: docs
weight: 30
url: id/net/get-xmp-metadata-of-an-existing-pdf-file/
description: Bagian ini menjelaskan cara mendapatkan Metadata XMP dari PDF yang ada dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Untuk mendapatkan metadata XMP dari file PDF, Anda perlu membuat objek [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Anda dapat meneruskan properti metadata XMP tertentu ke objek [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) untuk mendapatkan nilai mereka. Cuplikan kode berikut menunjukkan cara mendapatkan metadata XMP dari file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan pergi ke https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Buat objek PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Mengikat file pdf ke objek
xmpMetaData.BindPdf( dataDir + "input.pdf");

// Dapatkan properti Data Meta XMP
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreateDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.MetadataDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreatorTool].ToString());
Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

Console.ReadLine();
```
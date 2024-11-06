---
title: Получение XMP метаданных PDF файла
type: docs
weight: 30
url: ru/net/get-xmp-metadata-of-an-existing-pdf-file/
description: Этот раздел объясняет, как получить XMP метаданные существующего PDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Чтобы получить XMP метаданные из PDF файла, необходимо создать объект [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) и связать PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Вы можете передать определенные свойства XMP метаданных объекту [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata), чтобы получить их значения. Следующий фрагмент кода показывает, как получить XMP метаданные из PDF файла.

```csharp
// Для получения полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Создать объект PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Связать PDF файл с объектом
xmpMetaData.BindPdf( dataDir + "input.pdf");

// Получить свойства XMP метаданных
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreateDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.MetadataDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreatorTool].ToString());
Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

Console.ReadLine();
```
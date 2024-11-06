---
title: احصل على بيانات XMP الوصفية لملف PDF
type: docs
weight: 30
url: ar/net/get-xmp-metadata-of-an-existing-pdf-file/
description: يشرح هذا القسم كيفية الحصول على بيانات XMP الوصفية لملف PDF موجود باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

من أجل الحصول على بيانات XMP الوصفية من ملف PDF، تحتاج إلى إنشاء كائن [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) وربط ملف PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). يمكنك تمرير خصائص محددة من بيانات XMP الوصفية إلى كائن [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) للحصول على قيمها. يوضح لك الجزء التالي من الكود كيفية الحصول على بيانات XMP الوصفية من ملف PDF.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// إنشاء كائن PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// ربط ملف pdf بالكائن
xmpMetaData.BindPdf( dataDir + "input.pdf");

// الحصول على خصائص بيانات XMP الوصفية
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreateDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.MetadataDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreatorTool].ToString());
Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

Console.ReadLine();
```
```
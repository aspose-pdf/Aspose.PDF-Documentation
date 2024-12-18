---
title: تعيين بيانات XMP الوصفية لملف PDF موجود
type: docs
weight: 20
url: /ar/net/set-xmp-metadata-of-an-existing-pdf/
description: يوضح هذا القسم كيفية تعيين بيانات XMP الوصفية لملف PDF موجود باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

من أجل تعيين بيانات XMP الوصفية في ملف PDF، تحتاج إلى إنشاء كائن [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) وربط ملف PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). يمكنك استخدام [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) طريقة [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) فئة لإضافة خصائص مختلفة. أخيرًا، قم باستدعاء [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) طريقة [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) فئة. يوضح لك مقتطف الكود التالي كيفية إضافة بيانات تعريف XMP في ملف PDF.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// إنشاء كائن PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// ربط ملف pdf بالكائن
xmpMetaData.BindPdf(dataDir+ "SetXMPMetadata.pdf");

// إضافة تاريخ الإنشاء
xmpMetaData.Add(DefaultMetadataProperties.CreateDate, System.DateTime.Now.ToString());

// تغيير تاريخ بيانات التعريف
xmpMetaData[DefaultMetadataProperties.MetadataDate] = System.DateTime.Now.ToString();

// إضافة أداة الإنشاء
xmpMetaData.Add(DefaultMetadataProperties.CreatorTool, "Creator tool name");

// إزالة تاريخ التعديل
xmpMetaData.Remove(DefaultMetadataProperties.ModifyDate);

// إضافة خاصية مخصصة من قبل المستخدم
// الخطوة #1: تسجيل بادئة النطاق وURI
xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");
// الخطوة #2: إضافة خاصية المستخدم مع البادئة
xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

// تغيير الخاصية المخصصة من قبل المستخدم
xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

// حفظ بيانات التعريف xmp في ملف pdf
xmpMetaData.Save(dataDir+ "SetXMPMetadata_out.pdf");

// إغلاق الكائن
xmpMetaData.Close();
```
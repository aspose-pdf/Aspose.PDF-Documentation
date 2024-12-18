---
title: إزالة المرفقات من ملف PDF
linktitle: إزالة المرفقات من ملف PDF موجود
type: docs
weight: 30
url: /ar/cpp/removing-attachment-from-an-existing-pdf/
description: يمكن لـ Aspose.PDF إزالة المرفقات من مستندات PDF الخاصة بك. استخدم C++ PDF API لإزالة المرفقات في ملفات PDF باستخدام مكتبة Aspose.PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكن لـ Aspose.PDF إزالة المرفقات من ملفات PDF. يتم الاحتفاظ بمرفقات مستند PDF في مجموعة EmbeddedFiles الخاصة بكائن Document.

لحذف جميع المرفقات المرتبطة بملف PDF:

1. قم باستدعاء طريقة [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection#afff8b235b554a66c203464b61204b843) لمجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection).
2. احفظ الملف المحدث باستخدام طريقة Save الخاصة بكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

يوضح مقتطف الشيفرة التالي كيفية إزالة المرفقات من مستند PDF.

```cpp
void WorkingWithAttachments::RemovingAttachment() {

 String _dataDir("C:\\Samples\\");

 // فتح المستند
 auto pdfDocument = new Document(_dataDir + u"DeleteAllAttachments.pdf");

 // حذف جميع المرفقات
 pdfDocument->get_EmbeddedFiles()->Delete();

 // حفظ الملف المحدث
 pdfDocument->Save(_dataDir + u"DeleteAllAttachments_out.pdf");
}
```
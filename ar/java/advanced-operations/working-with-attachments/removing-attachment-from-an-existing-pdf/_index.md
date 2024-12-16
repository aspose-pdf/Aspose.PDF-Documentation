---
title: إزالة المرفقات من ملف PDF موجود
linktitle: إزالة المرفقات من ملف PDF موجود
type: docs
weight: 30
url: /ar/java/removing-attachment-from-an-existing-pdf/
description: يمكن لـ Aspose.PDF إزالة المرفقات من مستندات PDF الخاصة بك. استخدم Java PDF API لإزالة المرفقات في ملفات PDF باستخدام مكتبة Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكن لـ Aspose.PDF إزالة المرفقات من ملفات PDF. يتم الاحتفاظ بمرفقات مستند PDF في مجموعة EmbeddedFiles الخاصة بكائن المستند.

يتم الاحتفاظ بمرفقات مستند PDF في مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

لحذف جميع المرفقات المرتبطة بملف PDF:

1. قم باستدعاء طريقة الحذف(..) الخاصة بمجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection).

1. احفظ الملف المحدث باستخدام طريقة الحفظ الخاصة بـ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يظهر جزء الشيفرة التالي كيفية حذف جميع المرفقات من مستند PDF.

```java
   public static void DeleteAllAttachmentsFromPDF(){
  // افتح مستندًا
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // احذف جميع المرفقات
  pdfDocument.getEmbeddedFiles().delete();
  // احفظ الملف المحدث
  pdfDocument.save("output.pdf");

    }
```
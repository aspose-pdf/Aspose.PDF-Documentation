---
title: إضافة مرفق إلى مستند PDF 
linktitle: إضافة مرفق إلى مستند PDF 
type: docs
weight: 10
url: /ar/java/add-attachment-to-pdf-document/
description: تصف هذه الصفحة كيفية إضافة مرفق إلى ملف PDF باستخدام Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكن أن تحتوي المرفقات على مجموعة واسعة من المعلومات ويمكن أن تكون من أنواع ملفات متنوعة. يشرح هذا المقال كيفية إضافة مرفق إلى ملف PDF.

1. قم بإنشاء كائن [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) يحتوي على الملف الذي تريد إرفاقه ووصف الملف.

1. أضف كائن [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) إلى مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) باستخدام الطريقة [add(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). تحتوي مجموعة [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) على كافة المرفقات المضافة إلى ملف PDF.

يوضح لك مقطع الشيفرة البرمجية التالي كيفية إضافة مرفق في مستند PDF.

```java
public class ExampleAttachments {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Attachments/";

    public static void AddingAttachment() {
        // افتح مستند
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // إعداد ملف جديد ليتم إضافته كمرفق
  FileSpecification fileSpecification = new FileSpecification("sample.txt", "ملف نصي تجريبي");
  // أضف مرفقًا إلى مجموعة مرفقات المستند
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // احفظ المستند المحدث
  pdfDocument.save("output.pdf");
    }
}
```
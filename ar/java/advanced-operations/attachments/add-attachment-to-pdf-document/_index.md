---
title: إضافة مرفقات إلى PDF في جافا
linktitle: إضافة مرفق إلى وثيقة PDF
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: تعرف على كيفية إضافة مرفقات الملفات إلى مستندات PDF في Java باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف الملفات المضمنة إلى مستندات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إرفاق ملف خارجي بمستند PDF باستخدام Aspose.PDF لـ Java. يفتح المثال ملف PDF موجود، وينشئ مواصفات الملف للمرفق، ويضيفه إلى مجموعة EmbeddedFiles الخاصة بالمستند، ويحفظ الملف المحدث.
---
لإرفاق ملف بملف PDF، قم بتحميل المستند المصدر، وأنشئ `FileSpecification`، وأضفه إلى مجموعة الملفات المضمنة، واحفظ النتيجة.

## إضافة مرفق إلى وثيقة PDF

استخدم هذا المثال عندما يجب تضمين ملف خارجي في ملف PDF موجود.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) للملف الذي تريد تضمينه.
1. أضف مواصفات الملف إلى مجموعة `EmbeddedFiles` واحفظ المستند المحدث.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```

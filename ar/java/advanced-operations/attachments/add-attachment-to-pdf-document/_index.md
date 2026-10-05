---
title: إضافة مرفقات إلى PDF في Java
linktitle: إضافة مرفق إلى مستند PDF
type: docs
weight: 10
url: /ar/java/add-attachment-to-pdf-document/
description: تعرف على كيفية إضافة مرفقات ملفات إلى مستندات PDF في Java باستخدام Aspose.PDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة ملفات مضمنة إلى مستندات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إرفاق ملف خارجي إلى مستند PDF باستخدام Aspose.PDF for Java. يفتح المثال ملف PDF موجود، وينشئ FileSpecification للمرفق، ويضيفه إلى مجموعة EmbeddedFiles الخاصة بالمستند، ثم يحفظ الملف المحدث.
---
لإرفاق ملف إلى PDF، قم بتحميل المستند المصدر، أنشئ `FileSpecification`، أضفها إلى مجموعة الملفات المضمنة، واحفظ النتيجة.

## إضافة مرفق إلى مستند PDF

استخدم هذا المثال عندما يجب تضمين ملف خارجي في PDF موجود.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) بالنسبة للملف الذي تريد تضمينه.
1. أضف مواصفات الملف إلى `EmbeddedFiles` اجمع واحفظ المستند المحدث.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```

---
title: إزالة المرفقات من PDF في جافا
linktitle: إزالة المرفق من ملف PDF موجود
type: docs
weight: 30
url: /java/removing-attachment-from-an-existing-pdf/
description: تعرف على كيفية إزالة أحد المرفقات المضمنة أو جميعها من مستندات PDF في Java باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حذف مرفقات PDF برمجياً باستخدام Java
Abstract: توضح هذه المقالة كيفية إزالة المرفقات من ملفات PDF باستخدام Aspose.PDF لـ Java. توضح الأمثلة حذف ملف مضمن واحد عن طريق المفتاح ومسح مجموعة EmbeddedFiles بالكامل قبل حفظ المستند المحدث.
---
يمكن إزالة المرفقات المخزنة في مستند PDF إما بشكل فردي أو مرة واحدة من خلال مجموعة `EmbeddedFiles`.

## إزالة مرفق واحد

استخدم هذا المثال عندما يجب حذف ملف مضمن مسمى من ملف PDF.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احذف المرفق بالمفتاح الخاص به من مجموعة الملفات المضمنة.
1. احفظ مستند الإخراج المحدث.

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## قم بإزالة كافة المرفقات

استخدم هذا الأسلوب عندما يجب مسح مجموعة الملفات المضمنة بالكامل.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احذف كافة العناصر من مجموعة الملفات المضمنة.
1. احفظ مستند الإخراج الذي تم تنظيفه.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```

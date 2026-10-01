---
title: إزالة المرفقات من PDF في Java
linktitle: إزالة المرفق من PDF موجود
type: docs
weight: 30
url: /ar/java/removing-attachment-from-an-existing-pdf/
description: تعلم كيفية إزالة مرفق واحد أو جميع المرفقات المدمجة من مستندات PDF في Java باستخدام Aspose.PDF.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حذف مرفقات PDF برمجياً باستخدام Java
Abstract: توضح هذه المقالة كيفية إزالة المرفقات من ملفات PDF باستخدام Aspose.PDF for Java. تُظهر الأمثلة حذف ملف مدمج واحد بواسطة المفتاح ومسح مجموعة `EmbeddedFiles` بالكامل قبل حفظ المستند المحدث.
---
يمكن إزالة المرفقات المخزنة في مستند PDF إما بشكل فردي أو جميعها مرة واحدة من خلال `EmbeddedFiles` مجموعة.

## إزالة مرفق واحد

استخدم هذا المثال عندما يجب حذف ملف مدمج مسمى واحد من ملف PDF.

1. فتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احذف المرفق بواسطة مفتاحه من مجموعة الملفات المدمجة.
1. احفظ المستند الناتج المحدث.

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## إزالة جميع المرفقات

استخدم هذا الأسلوب عندما يجب مسح مجموعة الملفات المضمنة بالكامل.

1. فتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احذف جميع العناصر من مجموعة الملفات المضمنة.
1. احفظ مستند الإخراج المنقى.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```

---
title: إضافة صفحات PDF في جافا
linktitle: إضافة صفحات
type: docs
weight: 10
url: /ar/java/add-pages/
description: تعلم كيفية إضافة أو إدراج صفحات في مستندات PDF باستخدام جافا.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة أو إدراج صفحات PDF باستخدام جافا
Abstract: تشرح هذه المقالة كيفية إضافة صفحات إلى ملفات PDF باستخدام Aspose.PDF for Java. تغطي إدراج صفحة فارغة في موضع محدد، وإضافة صفحة في نهاية المستند، واستيراد صفحة من ملف PDF آخر.
---
يتيح لك Aspose.PDF for Java إدراج صفحات فارغة أو استيراد صفحات من مستند آخر.

## إدراج صفحة فارغة في موضع محدد

استخدم هذا المثال عندما تحتاج إلى إضافة صفحة فارغة في وسط ملف PDF موجود.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أدرج صفحة جديدة في الموضع المستهدف في مجموعة الصفحات.
1. احفظ المستند المحدث.

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## إلحاق صفحة فارغة في النهاية

استخدم هذا المثال عندما تحتاج إلى توسيع المستند بصفحة فارغة جديدة في النهاية.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إضافة صفحة جديدة إلى نهاية مجموعة الصفحات.
1. احفظ ملف PDF المعدل.

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## أضف صفحة من مستند آخر

استخدم هذا المثال عندما تريد استيراد صفحة من ملف PDF إلى ملف PDF آخر.

1. إنشاء الوجهة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح المستند المصدر.
1. أضف أي محتوى مطلوب للوجهة واستورد الصفحة المستهدفة من ملف PDF المصدر.
1. احفظ المستند الناتج.

```java
public static void addPageFromAnotherDocument(Path inputFile, Path outputFile) {
    try (Document document = new Document();
         Document anotherDocument = new Document(inputFile.toString())) {
        document.getPages().add().getParagraphs().add(new TextFragment("This is first page!"));
        document.getPages().add(anotherDocument.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

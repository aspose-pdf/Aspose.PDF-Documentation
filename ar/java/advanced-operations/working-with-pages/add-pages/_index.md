---
title: إضافة صفحات PDF في جافا
linktitle: إضافة الصفحات
type: docs
weight: 10
url: /java/add-pages/
description: تعرف على كيفية إضافة أو إدراج صفحات في مستندات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة أو إدراج صفحات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إضافة صفحات إلى ملفات PDF باستخدام Aspose.PDF لـ Java. وهو يغطي إدراج صفحة فارغة في موضع محدد، وإلحاق صفحة في نهاية المستند، واستيراد صفحة من ملف PDF آخر.
---
يتيح لك Aspose.PDF for Java إدراج صفحات فارغة أو استيراد صفحات من مستند آخر.

## أدخل صفحة فارغة في موضع محدد

استخدم هذا المثال عندما تحتاج إلى إضافة صفحة فارغة في منتصف ملف PDF موجود.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإدراج صفحة جديدة في الموضع المستهدف في مجموعة الصفحات.
1. احفظ المستند المحدث.

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## إلحاق صفحة فارغة بالنهاية

استخدم هذا المثال عندما تحتاج إلى توسيع المستند بصفحة أخيرة فارغة جديدة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف صفحة جديدة إلى نهاية مجموعة الصفحات.
1. احفظ ملف PDF المعدل.

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## إضافة صفحة من مستند آخر

استخدم هذا المثال عندما تريد استيراد صفحة من ملف PDF إلى ملف PDF آخر.

1. قم بإنشاء الوجهة [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح المستند المصدر.
1. أضف أي محتوى وجهة مطلوب واستورد الصفحة المستهدفة من ملف PDF المصدر.
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

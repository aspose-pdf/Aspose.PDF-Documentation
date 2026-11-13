---
title: إزالة ترقيم Bates من PDF باستخدام Java
linktitle: إزالة ترقيم Bates
type: docs
weight: 100
url: /ar/java/remove-bates-numbering/
description: إزالة ترقيم Bates من جميع صفحات ملف PDF باستخدام Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة ترقيم Bates من PDF في Java
Abstract: إزالة ترقيم Bates من جميع صفحات ملف PDF.
---

إزالة ترقيم Bates من جميع صفحات ملف PDF.

## حذف ترقيم Bates

يحذف المثال ترقيم Bates من مجموعة صفحات المستند.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. استدعِ الطريقة المساعدة لحذف ترقيم Bates من مجموعة الصفحات.
1. احفظ ملف PDF الناتج.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

## مواضيع ذات صلة

- [إضافة ترقيم Bates](/pdf/ar/java/add-bates-numbering/)
- [العمل مع عناصر PDF](/pdf/ar/java/artifacts/)

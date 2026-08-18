---
title: إنشاء حزم PDF في جافا
linktitle: مَلَفّ
type: docs
weight: 20
url: /java/portfolio/
description: تعرف على كيفية إنشاء وإدارة ملفات PDF في Java باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء وتحرير ملفات PDF باستخدام الملفات المضمنة في Java
Abstract: يشرح هذا المقال كيفية إنشاء وإدارة ملفات PDF باستخدام Aspose.PDF لـ Java. تعرف على كيفية تمكين مجموعة في مستند، وإضافة أنواع ملفات متعددة إلى المحفظة، وإزالة جميع عناصر المجموعة من محفظة PDF موجودة.
---
يمكن لمحفظة PDF تجميع ملفات متعددة داخل حاوية PDF واحدة مع الحفاظ على كل ملف بتنسيقه الأصلي.

## إنشاء محفظة PDF

استخدم هذا المثال عندما تحتاج إلى تجميع عدة ملفات في مجموعة ملفات PDF.

1. قم بإنشاء [مستند] PDF جديد (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بتمكين [المجموعة] (https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/) الخاصة به.
1. قم بإنشاء كائنات [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) لكل ملف إدخال وقم بتعيين أوصافها.
1. أضف الملفات إلى مجموعة المحفظة واحفظ مستند الإخراج.

```java
public static void createPdfPortfolio(Path[] inputFiles, Path outputFile) {
    try (Document document = new Document()) {
        document.setCollection(new Collection());

        FileSpecification excel = new FileSpecification(inputFiles[0].toString());
        FileSpecification word = new FileSpecification(inputFiles[1].toString());
        FileSpecification image = new FileSpecification(inputFiles[2].toString());

        excel.setDescription("Excel File");
        word.setDescription("Word File");
        image.setDescription("Image File");

        document.getCollection().add(excel);
        document.getCollection().add(word);
        document.getCollection().add(image);

        document.save(outputFile.toString());
    }
}
```

## إزالة الملفات من محفظة PDF

استخدم هذا المثال عندما يجب مسح مجموعة محفظة PDF موجودة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حذف إدخالات مجموعة المستندات.
1. احفظ مستند الإخراج الذي تم تنظيفه.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```

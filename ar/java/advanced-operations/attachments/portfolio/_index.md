---
title: إنشاء حافظات PDF في Java
linktitle: حافظة
type: docs
weight: 20
url: /ar/java/portfolio/
description: تعلّم كيفية إنشاء وإدارة حافظات PDF في Java باستخدام Aspose.PDF.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء وتحرير حافظات PDF مع ملفات مدمجة في Java
Abstract: تشرح هذه المقالة كيفية إنشاء وإدارة حافظات PDF باستخدام Aspose.PDF for Java. تعلّم كيفية تمكين مجموعة على مستند، إضافة أنواع ملفات متعددة إلى الحافظة، وإزالة جميع عناصر المجموعة من حافظة PDF موجودة.
---
يمكن لحافظة PDF تجميع ملفات متعددة داخل حاوية PDF واحدة مع الحفاظ على كل ملف بصيغته الأصلية.

## إنشاء محفظة PDF

استخدم هذا المثال عندما تحتاج إلى تجميع عدة ملفات في مجموعة محفظة PDF.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتمكينها [Collection](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/).
1. إنشاء [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) كائنات لكل ملف إدخال وتعيين أوصافها.
1. أضف الملفات إلى مجموعة الحافظة واحفظ مستند الإخراج.

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

استخدم هذا المثال عندما يجب مسح مجموعة محفظة PDF الموجودة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احذف إدخالات مجموعة المستندات.
1. احفظ المستند الناتج المنظف.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```

---
title: إضافة Bates Numbering إلى PDF في Java
linktitle: إضافة Bates Numbering
type: docs
weight: 10
url: /ar/java/add-bates-numbering/
description: تعلم كيفية إضافة وإزالة Bates Numbering في مستندات PDF باستخدام Java مع Aspose.PDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة Bates Numbering عبر Java
Abstract: تشرح هذه المقالة كيفية إنشاء وإزالة ملحقات ترقيم Bates في مستندات PDF باستخدام Aspose.PDF for Java. تغطي تكوين `BatesNArtifact`، وتطبيقه عبر مساعدي ترقيم Bates أو مساعدي ترقيم الصفحات العامة، وإزالة ترقيم Bates من المستند.
---
تُعد ملحقات ترقيم Bates مفيدة في عمليات العمل القانونية والأرشيفية ومراقبة المستندات حيث تحتاج كل صفحة إلى معرف ثابت على مستوى الصفحة.

## إضافة ترقيم Bates باستخدام المساعد المخصص

استخدم هذا المثال عندما تريد تطبيق ترقيم Bates عبر المساعد المخصص لتجميع الصفحات.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف أي صفحات إضافية مطلوبة في العينة.
1. أنشئ كائنًا من الفئة [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) التكوين.
1. طبّق ترقيم Bates على مجموعة الصفحات واحفظ ملف الإخراج.

```java
public static void addBatesNArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        PageCollectionExtensions.addBatesNumbering(document.getPages(), batesArtifact);
        document.save(outputFile.toString());
    }
}
```

## إضافة ترقيم Bates عبر قطع ترقيم الصفحات

يطبق هذا المثال ترقيم باتس بتمرير قطعة باتس عبر واجهة برمجة تطبيقات الترقيم العامة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف الصفحات المطلوبة.
1. أنشئ كائنًا من الفئة [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) وإضافتها إلى قائمة قطع الترقيم.
1. طبّق قطع الترقيم على مجموعة الصفحات واحفظ المستند.

```java
public static void addBatesNArtifactPagination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        List<PaginationArtifact> paginationArtifacts = new ArrayList<>();
        paginationArtifacts.add(batesArtifact);
        PageCollectionExtensions.addPagination(document.getPages(), paginationArtifacts);
        document.save(outputFile.toString());
    }
}
```

## حذف ترقيم Bates

استخدم هذا النهج عندما يجب إزالة عناصر ترقيم Bates الموجودة من المستند.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. استدعِ أداة مساعدة تجميع الصفحات التي تحذف ترقيم Bates..
1. احفظ ملف الإخراج المنقّح.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

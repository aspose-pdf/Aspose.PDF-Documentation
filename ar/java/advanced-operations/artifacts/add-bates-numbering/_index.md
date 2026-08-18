---
title: إضافة ترقيم بيتس إلى PDF في جافا
linktitle: إضافة ترقيم بيتس
type: docs
weight: 10
url: /java/add-bates-numbering/
description: تعرف على كيفية إضافة وإزالة ترقيم Bates في مستندات PDF باستخدام Java مع Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة ترقيم بيتس عبر جافا
Abstract: يشرح هذا المقال كيفية إنشاء وإزالة عناصر ترقيم Bates في مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي تكوين `BatesNArtifact`، وتطبيقه من خلال مساعدي ترقيم Bates أو مساعدي ترقيم الصفحات العامين، وإزالة ترقيم Bates من المستند.
---
تعد عناصر ترقيم Bates مفيدة في سير العمل القانوني والأرشفي ومراقبة المستندات حيث تحتاج كل صفحة إلى معرف ثابت على مستوى الصفحة.

## إضافة ترقيم بيتس مع المساعد المخصص

استخدم هذا المثال عندما تريد تطبيق ترقيم Bates من خلال مساعد مجموعة الصفحات المخصص.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف أي صفحات إضافية تتطلبها العينة.
1. قم بإنشاء تكوين [BatesNRifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
1. قم بتطبيق ترقيم بيتس على مجموعة الصفحات واحفظ ملف الإخراج.

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

## إضافة ترقيم بيتس من خلال التحف ترقيم الصفحات

يطبق هذا المثال ترقيم Bates عن طريق تمرير قطعة Bates من خلال واجهة برمجة تطبيقات ترقيم الصفحات العامة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف الصفحات المطلوبة.
1. قم بإنشاء [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) وأضفه إلى قائمة عناصر ترقيم الصفحات.
1. قم بتطبيق عناصر ترقيم الصفحات على مجموعة الصفحات واحفظ المستند.

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

## حذف ترقيم بيتس

استخدم هذا الأسلوب عندما يجب إزالة عناصر ترقيم Bates الموجودة من المستند.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اتصل بمساعد مجموعة الصفحات الذي يقوم بحذف ترقيم Bates.
1. احفظ ملف الإخراج الذي تم تنظيفه.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

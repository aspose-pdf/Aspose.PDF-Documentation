---
title: إضافة ترقيم Bates إلى PDF باستخدام Java
linktitle: إضافة ترقيم Bates
type: docs
weight: 10
url: /ar/java/add-bates-numbering/
description: إضافة معرّفات Bates متسلسلة إلى صفحات PDF باستخدام Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة ترقيم Bates إلى PDF في Java
Abstract: إضافة معرّفات Bates متسلسلة إلى صفحات PDF.
---

يمنح ترقيم Bates كل صفحة معرّفًا ثابتًا يُستخدم في الأعمال القانونية والأرشفة وإدارة المستندات.

## إضافة ترقيم Bates بالطريقة المخصّصة

يطبّق المثال ترقيم Bates على مجموعة الصفحات.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف الصفحات الإضافية التي يتطلبها المثال.
1. أنشئ كائنًا من الفئة [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) لإعداد الترقيم.
1. طبّق ترقيم Bates على مجموعة الصفحات واحفظ ملف PDF الناتج.

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

## إضافة ترقيم Bates عبر عناصر الترقيم

يمرّر المثال عنصر ترقيم Bates إلى واجهة برمجة التطبيقات العامة للترقيم.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف الصفحات المطلوبة.
1. أنشئ كائنًا من الفئة [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) وأضفه إلى قائمة عناصر الترقيم.
1. طبّق عناصر الترقيم على مجموعة الصفحات واحفظ المستند.

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

## مواضيع ذات صلة

- [إزالة ترقيم Bates](/pdf/ar/java/remove-bates-numbering/)
- [العمل مع عناصر PDF](/pdf/ar/java/artifacts/)

---
title: إضافة خلفيات إلى PDF باستخدام Java
linktitle: إضافة الخلفيات
type: docs
weight: 20
url: /ar/java/add-backgrounds/
description: إضافة صورة أو لون موحّد إلى خلفية صفحة PDF وضبط عتامة صورة الخلفية باستخدام Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة خلفيات إلى PDF في Java
Abstract: إضافة صورة أو لون موحّد إلى خلفية صفحة PDF وضبط عتامة صورة الخلفية.
---

تضع عناصر الخلفية صورة أو لونًا خلف محتوى الصفحة الرئيسي مع الحفاظ على النص المنطقي للمستند.

## إضافة صورة خلفية إلى ملف PDF

يضع المثال صورة خلف محتوى الصفحة الأولى.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح دفق إدخال الصورة.
1. أنشئ كائنًا من الفئة [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) وأسند إليه دفق الصورة.
1. أضف العنصر إلى الصفحة واحفظ ملف PDF الناتج.

```java
public static void addBackgroundImageToPdf(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## إضافة صورة خلفية شبه شفافة

يضبط المثال عتامة صورة الخلفية على 0.5.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح دفق إدخال الصورة.
1. أنشئ كائنًا من الفئة [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) واضبط صورته وعتامته.
1. أضف العنصر إلى الصفحة واحفظ ملف PDF الناتج.

```java
public static void addBackgroundImageWithOpacityToPdf(Path inputFile, Path imageFile, Path outputFile)
        throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        artifact.setOpacity(0.5);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## إضافة لون خلفية إلى ملف PDF

يستخدم المثال لونًا موحّدًا لخلفية الصفحة.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) وحدّد لون الخلفية.
1. أضف العنصر إلى الصفحة واحفظ ملف PDF الناتج.

```java
public static void addBackgroundColorToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundColor(Color.getDarkKhaki().toRgb());
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## مواضيع ذات صلة

- [إزالة الخلفيات](/pdf/ar/java/remove-backgrounds/)
- [العمل مع عناصر PDF](/pdf/ar/java/artifacts/)

---
title: إضافة خلفيات PDF في جافا
linktitle: إضافة الخلفيات
type: docs
weight: 20
url: /java/add-backgrounds/
description: تعرف على كيفية إضافة صورة خلفية أو لون خلفية إلى صفحات PDF في Java باستخدام `BackgroundArtifact` مع Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة خلفية إلى ملف PDF باستخدام جافا
Abstract: تشرح هذه المقالة كيفية إضافة خلفيات صفحات PDF أو إزالتها في Java باستخدام Aspose.PDF. ويغطي إضافة صورة خلفية، وضبط عتامة الصورة، وتطبيق لون الخلفية، وإزالة عناصر الخلفية من الصفحة.
---
تتيح لك عناصر الخلفية إمكانية وضع عناصر مرئية غير متعلقة بالمحتوى خلف محتوى الصفحة الرئيسية دون تغيير نص المستند المنطقي.

## إضافة صورة خلفية إلى ملف PDF

استخدم هذا المثال عندما يجب أن تعرض الصفحة صورة كقطعة أثرية في الخلفية.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ودفق إدخال الصورة.
1. قم بإنشاء [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) وقم بتعيين دفق الصورة.
1. أضف القطعة الأثرية إلى الصفحة المستهدفة واحفظ ملف PDF الناتج.

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

## إضافة صورة خلفية مع العتامة

يضع هذا المثال صورة خلفية شبه شفافة خلف محتوى الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ودفق الصور.
1. أنشئ [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/)، وقم بتعيين الصورة، واضبط العتامة.
1. أضف القطعة الأثرية إلى الصفحة واحفظ المستند.

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

## إضافة لون الخلفية إلى ملف PDF

استخدم هذا المثال عندما يجب أن تستخدم الصفحة لون خلفية خالصًا بدلاً من الصورة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) وقم بتعيين لون الخلفية.
1. أضف القطعة الأثرية إلى الصفحة واحفظ ملف الإخراج.

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

## إزالة التحف الخلفية

استخدم هذا الأسلوب عندما يجب حذف عناصر الخلفية الموجودة من الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار عبر مجموعة عناصر الصفحة بترتيب عكسي.
1. احذف العناصر التي يكون نوعها هو ترقيم الصفحات والنوع الفرعي هو الخلفية، ثم احفظ المستند.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

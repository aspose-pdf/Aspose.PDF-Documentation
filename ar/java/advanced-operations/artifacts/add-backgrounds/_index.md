---
title: إضافة خلفيات PDF في Java
linktitle: إضافة الخلفيات
type: docs
weight: 20
url: /ar/java/add-backgrounds/
description: تعلم كيفية إضافة صورة خلفية أو لون خلفية إلى صفحات PDF في Java باستخدام `BackgroundArtifact` مع Aspose.PDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة خلفية إلى PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إضافة أو إزالة خلفيات صفحات PDF في Java باستخدام Aspose.PDF. وتغطي إضافة صورة خلفية، تعديل شفافية الصورة، تطبيق لون خلفية، وإزالة العناصر الخلفية من صفحة.
---
تسمح لك العناصر الخلفية بوضع عناصر بصرية ليست جزءًا من المحتوى خلف محتوى الصفحة الرئيسي دون تغيير نص الوثيقة المنطقي.

## إضافة صورة خلفية إلى PDF

استخدم هذا المثال عندما يجب أن تعرض الصفحة صورة كعنصر خلفية.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتيار إدخال الصورة.
1. أنشئ كائنًا من الفئة [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) وأسند تدفق الصورة.
1. أضف القطعة إلى الصفحة المستهدفة واحفظ ملف PDF الناتج.

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

## إضافة صورة خلفية مع الشفافية

هذا المثال يضع صورة خلفية شبه شفافة خلف محتوى الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتدفق الصورة.
1. أنشئ كائنًا من الفئة [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/)، عيّن الصورة، واضبط الشفافية.
1. أضف العنصر إلى الصفحة واحفظ المستند.

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

## إضافة لون خلفية إلى PDF

استخدم هذا المثال عندما يجب أن تستخدم الصفحة لون خلفية صلب بدلاً من صورة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) وعيّن لون الخلفية.
1. أضف العنصر إلى الصفحة واحفظ ملف الإخراج.

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

## إزالة العناصر الخلفية

استخدم هذه الطريقة عندما يجب حذف العناصر الخلفية الموجودة من الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على مجموعة عناصر الصفحة بترتيب عكسي.
1. احذف العناصر التي نوعها pagination والفرعية هي background، ثم حفظ المستند.

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

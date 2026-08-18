---
title: قص صفحات PDF في جافا
linktitle: قص صفحات PDF
type: docs
weight: 70
url: /java/crop-pages/
description: تعرف على كيفية قص صفحات PDF وضبط مربعات القص والقص والتسييل والوسائط في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بقص الصفحات وضبط مربعات الصفحات في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية اقتصاص صفحات PDF باستخدام Aspose.PDF لـ Java. وهو يغطي تعيين مستطيل اقتصاص جديد لمربعات الاقتصاص والقص والفن والتسييل واقتصاص الصفحة تلقائيًا بناءً على محتوى الصورة المكتشفة.
---
يتيح لك Aspose.PDF for Java اقتصاص الصفحات إما عن طريق إحداثيات مربع واضحة أو بناءً على المحتوى المكتشف.

## قص الصفحة عن طريق وضع مربعات الصفحة

استخدم هذا المثال عندما تحتاج إلى تطبيق نفس مساحة الاقتصاص على مربعات الصفحة الرئيسية.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء الاقتصاص الجديد [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. قم بتطبيق المستطيل على مربعات الصفحة ذات الصلة بالاقتصاص واحفظ المستند.

```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## قص الصفحة حسب المحتوى المكتشف

استخدم هذا المثال عندما يجب أن يتم اشتقاق منطقة الاقتصاص من أول صورة تم اكتشافها على الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. استخدم [ImagePlacementAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) لاكتشاف مواضع الصور.
1. قم بتعيين مربع الاقتصاص على مستطيل الصورة إذا تم العثور عليه، ثم احفظ المستند.

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```

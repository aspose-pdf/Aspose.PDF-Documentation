---
title: إضافة طوابع الصور إلى PDF في Java
linktitle: طوابع الصور في ملف PDF
type: docs
weight: 10
url: /ar/java/image-stamps-in-pdf-page/
description: تعلم كيفية إضافة طوابع الصور إلى صفحات PDF في Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة طوابع الصور وخلفيات الصور إلى صفحات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إضافة طوابع الصور إلى ملفات PDF باستخدام Aspose.PDF for Java. تغطي طوابع الصور مع التموضع، والدوران، والشفافية، والتحكم في الجودة، واستخدام صورة كخلفية لصندوق عائم.
---
يدعم Aspose.PDF for Java طوابع الصور كطبقات تغطية وعناصر تخطيط مدعومة بالصور.

## إضافة طابع صورة

استخدم هذا المثال عندما يجب على الصفحة عرض طابع صورة مع وضع مخصص وشفافية.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) وتهيئة مظهره.
1. أضف الختم إلى الصفحة واحفظ المستند.

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## أضف ختم صورة مع التحكم في الجودة

استخدم هذا المثال عندما تحتاج إلى ضبط جودة عرض ختم الصورة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) وحدد قيمة الجودة.
1. أضف الختم إلى الصفحة واحفظ النتيجة.

```java
public static void addImageStampWithQualityControl(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setQuality(10);
        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## استخدم صورة كخلفية لمربع عائم

استخدم هذا المثال عندما يجب أن تكون الصورة خلفية لحاوية تخطيط مُصمَّمة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) والوصول إلى الصفحة المستهدفة.
1. إنشاء [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) مع إعدادات النص والحدود.
1. اضبط صورة الخلفية، أضف الصندوق إلى الصفحة، واحفظ المستند.

```java
public static void addImageAsBackgroundInFloatingBox(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        FloatingBox box = new FloatingBox(200.0f, 100.0f);
        box.setLeft(40);
        box.setTop(80);
        box.setHorizontalAlignment(HorizontalAlignment.Center);
        box.getParagraphs().add(new TextFragment("Text in Floating Box"));
        box.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Image image = new Image();
        image.setFile(imageFile.toString());
        box.setBackgroundImage(image);
        box.setBackgroundColor(Color.getYellow());
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```

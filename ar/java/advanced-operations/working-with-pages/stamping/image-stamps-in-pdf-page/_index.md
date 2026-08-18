---
title: إضافة طوابع الصور إلى PDF في Java
linktitle: طوابع الصور في ملف PDF
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: تعرف على كيفية إضافة طوابع الصور إلى صفحات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف طوابع الصور وخلفيات الصور إلى صفحات PDF باستخدام Java
Abstract: يشرح هذا المقال كيفية إضافة طوابع الصور إلى ملفات PDF باستخدام Aspose.PDF لـ Java. ويغطي طوابع الصور مع تحديد الموضع والتدوير والعتامة ومراقبة الجودة واستخدام الصورة كخلفية لمربع عائم.
---
يدعم Aspose.PDF for Java طوابع الصور كتراكبات وعناصر تخطيط مدعومة بالصور.

## أضف ختم الصورة

استخدم هذا المثال عندما يجب أن تعرض الصفحة طابع صورة بموضع وعتامة مخصصين.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) وقم بتكوين مظهره.
1. أضف الطابع إلى الصفحة واحفظ المستند.

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

## إضافة ختم الصورة مع مراقبة الجودة

استخدم هذا المثال عندما تحتاج إلى ضبط جودة عرض ختم الصورة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) وقم بتعيين قيمة الجودة.
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

## استخدم صورة كخلفية مربع عائم

استخدم هذا المثال عندما يجب أن تكون الصورة بمثابة خلفية لحاوية تخطيط ذات نمط.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بالوصول إلى الصفحة المستهدفة.
1. أنشئ [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) بإعدادات النص والحدود.
1. قم بتعيين صورة الخلفية، وأضف المربع إلى الصفحة، واحفظ المستند.

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

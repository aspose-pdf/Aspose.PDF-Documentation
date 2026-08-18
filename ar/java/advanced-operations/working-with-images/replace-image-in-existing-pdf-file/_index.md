---
title: استبدال الصورة في ملف PDF الموجود باستخدام Java
linktitle: استبدال الصورة
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: تعرف على كيفية استبدال الصور المضمنة في ملفات PDF الموجودة في Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: استبدل الصور الموجودة في ملفات PDF الموجودة بـ Java
Abstract: توضح هذه المقالة كيفية استبدال الصور في مستندات PDF باستخدام Aspose.PDF لـ Java. وهو يغطي استبدال الصورة بفهرس الموارد الخاص بها واستبدال أول موضع صورة مطابق تم العثور عليه باستخدام ImagePlacementAbsorter.
---
استخدم إما مجموعة صور الصفحة أو البحث المستند إلى الموضع اعتمادًا على مدى الدقة التي تحتاجها لاستهداف الصورة.

## استبدال الصورة بفهرس الموارد

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. الوصول إلى موارد الصورة على الهدف [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. استبدل مصدر الصورة الهدف بملف الصورة الجديد.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## استبدال صورة باستخدام `ImagePlacementAbsorber`

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [ImagePlacementAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) وقم بزيارة [الصفحة] المستهدفة (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احصل على الهدف [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) واستبدله بتدفق الصور الجديد.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImageWithAbsorber(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        if (absorber.getImagePlacements().size() > 0) {
            ImagePlacement imagePlacement = absorber.getImagePlacements().get_Item(1);
            try (InputStream imageStream = Files.newInputStream(imageFile)) {
                imagePlacement.replace(imageStream);
            }
        }

        document.save(outputFile.toString());
    }
}
```

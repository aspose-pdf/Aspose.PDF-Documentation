---
title: استبدال صورة في ملف PDF موجود باستخدام Java
linktitle: استبدال صورة
type: docs
weight: 70
url: /ar/java/replace-image-in-existing-pdf-file/
description: تعرّف على كيفية استبدال الصور المضمّنة في ملفات PDF الموجودة باستخدام Java.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: استبدال الصور في ملفات PDF الموجودة باستخدام Java
Abstract: توضح هذه المقالة كيفية استبدال الصور في مستندات PDF باستخدام Aspose.PDF for Java. وتتناول استبدال صورة بحسب فهرس المورد واستبدال أول موضع صورة مطابق يتم العثور عليه باستخدام ImagePlacementAbsorber.
---
استخدم إما مجموعة صور الصفحة أو البحث القائم على الموضع وفقًا لدقة الاستهداف التي تحتاجها للصورة.

## استبدال صورة وفقًا لمؤشر المورد

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. انتقل إلى موارد الصورة على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. استبدل مورد الصورة الهدف بملف الصورة الجديد.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) وزر الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احصل على الهدف [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) واستبدله بتدفق الصورة الجديد.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

---
title: استخراج الصور من ملف PDF باستخدام جافا
linktitle: استخراج الصور
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: تعرف على كيفية استخراج الصور المضمنة من ملفات PDF في Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: استخراج الصور من ملفات PDF مع جافا
Abstract: توضح هذه المقالة كيفية استخراج الصور من مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي حفظ مورد صورة محدد من الصفحة وتصدير الصور التي تقع داخل منطقة مستطيلة محددة.
---
يدعم Aspose.PDF for Java الاستخراج المباشر لموارد الصور والتصفية المستندة إلى الموضع.

## استخراج صورة مضمنة عن طريق الفهرس

استخدم هذا المثال عندما تحتاج إلى حفظ مصدر صورة محدد من صفحة PDF.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى الهدف [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) من موارد الصفحة.
1. حفظ دفق الصورة إلى ملف الإخراج.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## استخراج الصور من منطقة صفحة معينة

استخدم هذا المثال عندما يجب تصدير الصور الموضوعة داخل المستطيل المحدد فقط.

1. حدد الهدف [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) وافتح ملف PDF المصدر.
1. استخدم [ImagePlacementAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) لفحص مواضع الصور على الصفحة.
1. احفظ فقط الصور التي يتناسب موضعها داخل المنطقة المحددة.

```java
public static void extractImageFromSpecificRegion(Path inputFile, Path outputFile) throws Exception {
    Rectangle rectangle = new Rectangle(0, 0, 590, 590, true);

    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        int index = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            Point point1 = new Point(imagePlacement.getRectangle().getLLX(), imagePlacement.getRectangle().getLLY());
            Point point2 = new Point(imagePlacement.getRectangle().getURX(), imagePlacement.getRectangle().getURX());
            if (rectangle.contains(point1, true) && rectangle.contains(point2, true)) {
                Path indexedOutputFile = Path.of(outputFile.toString().replace("index", String.valueOf(index)));
                try (OutputStream outputImage = Files.newOutputStream(indexedOutputFile)) {
                    imagePlacement.getImage().save(outputImage);
                }
                index++;
            }
        }
    }
}
```

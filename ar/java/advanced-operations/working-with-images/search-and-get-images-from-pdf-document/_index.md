---
title: الحصول على الصور والبحث عنها في PDF
linktitle: الحصول على الصور والبحث فيها
type: docs
weight: 40
url: /java/search-and-get-images-from-pdf-document/
description: تعرف على كيفية البحث عن الصور وفحصها في مستندات PDF في Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: البحث عن الصور وفحصها في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية البحث عن الصور وفحصها في مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي قراءة هندسة موضع الصورة، واكتشاف نوع اللون، واستخراج النص البديل، وحساب دقة الصورة الفعالة من مشغلي الصفحة.
---
يمكن لـ Aspose.PDF لـ Java فحص معلومات موضع الصورة بالإضافة إلى بيانات الرسم ذات المستوى الأدنى.

## الحصول على معلمات موضع الصورة

استخدم هذا المثال عندما تحتاج إلى فحص هندسة الصورة والدقة الفعالة على الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. استخدم [ImagePlacementAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) لجمع مواضع الصور.
1. قم بإخراج الحجم والإحداثيات والدقة لكل صورة موضوعة.

```java
public static void extractImageParams(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("image width: " + imagePlacement.getRectangle().getWidth());
            System.out.println("image height: " + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX: " + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY: " + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution: " + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution: " + imagePlacement.getResolution().getY());
        }
    }
}
```

## كشف أنواع ألوان الصورة

استخدم هذا المثال عندما تحتاج إلى حساب صور ذات تدرج رمادي وRGB في صفحة PDF.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. استخدم [ImagePlacementAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) للتكرار على صور الصفحة.
1. اقرأ [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/) لكل صورة وأخرج الإجماليات.

```java
public static void extractImageTypesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        int grayscaled = 0;
        int rgb = 0;

        document.getPages().get_Item(1).accept(absorber);

        System.out.println("--------------------------------");
        System.out.println("Total Images = " + absorber.getImagePlacements().size());

        int imageCounter = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            ColorType colorType = imagePlacement.getImage().getColorType();
            if (colorType == ColorType.Grayscale) {
                grayscaled++;
                System.out.println("Image " + imageCounter + " is Grayscale...");
            } else if (colorType == ColorType.Rgb) {
                rgb++;
                System.out.println("Image " + imageCounter + " is RGB...");
            }
            imageCounter++;
        }

        System.out.println("--------------------------------");
        System.out.println("Grayscale Images = " + grayscaled);
        System.out.println("RGB Images = " + rgb);
    }
}
```

## استخراج النص البديل للصورة

استخدم هذا المثال عندما تحتاج إلى فحص نص إمكانية الوصول المرتبط بصور الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. استخدم [ImagePlacementAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) لجمع مواضع الصور.
1. اقرأ النص البديل لكل صورة وأخرج النتيجة.

```java
public static void extractImageAltText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("Name in collection: " + imagePlacement.getImage().getNameInCollection());
            List<String> lines = imagePlacement.getImage().getAlternativeText(document.getPages().get_Item(1));
            if (!lines.isEmpty()) {
                System.out.println("Alt Text: " + lines.get(0));
            } else {
                System.out.println("Alt Text: ");
            }
        }
    }
}
```

## حساب معلومات الصورة من مشغلي الصفحة

استخدم هذا المثال عندما تحتاج إلى استخلاص حجم الصورة ودقة الوضوح الفعالين من عوامل تشغيل محتوى الصفحة ذات المستوى المنخفض.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) واجمع أسماء موارد الصور.
1. تتبع حالة الرسومات أثناء التكرار من خلال عوامل تشغيل الصفحة.
1. حل كل عملية رسم صورة وحساب أبعادها الفعالة ودقة الوضوح.

```java
public static void extractImageInformationFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int defaultResolution = 72;
        List<Matrix> graphicsState = new ArrayList<>();
        List<String> imageNames = Arrays.asList(document.getPages().get_Item(1).getResources().getImages().getNames());

        graphicsState.add(new Matrix(1, 0, 0, 1, 0, 0));

        for (Operator operator : document.getPages().get_Item(1).getContents()) {
            if (operator instanceof GSave) {
                graphicsState.add(new Matrix(graphicsState.get(graphicsState.size() - 1)));
            } else if (operator instanceof GRestore) {
                graphicsState.remove(graphicsState.size() - 1);
            } else if (operator instanceof ConcatenateMatrix concatenateMatrix) {
                Matrix current = graphicsState.get(graphicsState.size() - 1);
                graphicsState.set(graphicsState.size() - 1, current.multiply(concatenateMatrix.getMatrix()));
            } else if (operator instanceof Do doOperator) {
                if (imageNames.contains(doOperator.getName())) {
                    Matrix lastCtm = graphicsState.get(graphicsState.size() - 1);
                    int index = imageNames.indexOf(doOperator.getName()) + 1;
                    XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(index);

                    double scaledWidth = Math.sqrt(Math.pow(lastCtm.getA(), 2) + Math.pow(lastCtm.getB(), 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCtm.getC(), 2) + Math.pow(lastCtm.getD(), 2));

                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    String info = String.format(
                            "%s image %s (%.2f:%.2f): res %.2f x %.2f",
                            inputFile,
                            doOperator.getName(),
                            scaledWidth,
                            scaledHeight,
                            resHorizontal,
                            resVertical);
                    System.out.println(info);
                }
            }
        }
    }
}
```

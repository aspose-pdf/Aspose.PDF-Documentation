---
title: تحويل تنسيقات الصور إلى PDF في جافا
linktitle: تحويل الصور إلى PDF
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2026-06-16"
description: تعرف على كيفية تحويل BMP وCGM وDICOM وPNG وTIFF وEMF وSVG وCDR وتنسيقات الصور الأخرى إلى PDF في Java باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: كيفية تحويل الصور إلى PDF في جافا
Abstract: تشرح هذه المقالة كيفية تحويل تنسيقات صور متعددة إلى PDF باستخدام Aspose.PDF لـ Java. وهو يغطي وضع الصورة مباشرة في صفحة PDF جديدة بالإضافة إلى خيارات التحميل الخاصة بنوع الملف لمدخلات CGM وSVG وCDR.
---
يمكن لـ Aspose.PDF for Java تحويل العديد من تنسيقات الصور النقطية والمتجهة إلى مستندات PDF.

## تحويل BMP إلى PDF

استخدم هذا المثال عندما يجب وضع صورة BMP في مستند PDF.

1. قم بإنشاء [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغًا للاحتفاظ بملف PDF الناتج.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ثم ضع BMP مع `page.addImage(...)`.
1. حدد مستطيل الصورة المستهدفة باستخدام [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) بحيث يملأ المحتوى النقطي منطقة صفحة PDF.
1. احفظ ملف PDF الناتج.

```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
        try (Document document = new Document()) {
            try (Page page = document.getPages().add()) {
                page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
            }
            document.save(outputFile.toString());
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## تحويل CGM إلى PDF

استخدم هذا المثال عندما يجب تحويل ملف رسومات CGM إلى PDF.

1. افتح مصدر CGM عن طريق تمرير مسار الملف و[`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بتفسير تدفق رسومات CGM أثناء تحميل المستند.
1. احفظ ملف PDF المحول إلى مسار الإخراج المستهدف.

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل DICOM إلى PDF

استخدم هذا المثال عندما يجب تغليف صورة DICOM الطبية في مستند PDF.

1. قم بإنشاء [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغًا لمخرجات PDF.
1. قم بإنشاء كائن [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/)، وقم بتعيين [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) إلى `Dicom`، وقم بتعيين مسار الملف المصدر.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وألحق صورة DICOM بمجموعة فقرات الصفحة.
1. احفظ النتيجة بصيغة PDF.

```java
public static void convertDicomToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setFile(inputFile.toString());

        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل EMF إلى PDF مع التحميل المباشر للمستندات

استخدم هذا المثال عندما يجب تحويل ملف EMF إلى PDF من خلال مسار تحميل EMF الأساسي.

1. قم بإنشاء [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغًا وافتح مصدر EMF كتدفق ثنائي.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وامسح هوامشها حتى يتمكن العمل الفني EMF من شغل مساحة الصفحة بأكملها.
1. أنشئ [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/)، واربط تدفق EMF به، وأضفه إلى مجموعة فقرات الصفحة.
1. احفظ ملف PDF الناتج.

```java
public static void convertEmfToPdf01(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         FileInputStream imageStream = new FileInputStream(inputFile.toFile())) {
        try (Page page = document.getPages().add()) {
            page.getPageInfo().getMargin().setBottom(0);
            page.getPageInfo().getMargin().setTop(0);
            page.getPageInfo().getMargin().setLeft(0);
            page.getPageInfo().getMargin().setRight(0);

            Image image = new Image();
            image.setFileType(ImageFileType.Unknown);
            image.setImageStream(imageStream);
            page.getParagraphs().add(image);
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## قم بتحويل EMF إلى PDF باستخدام سير عمل بديل

استخدم هذا المثال عندما يجب تحويل محتوى EMF باستخدام إعداد بديل أو تدفق تكوين الصفحة.

1. قم بتحميل مصدر EMF باستخدام Aspose.Imaging وقم بتحويله إلى تدفق PNG في الذاكرة قبل وضع PDF.
1. أنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغًا وأضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. أنشئ [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) من دفق البايت المتوسط ​​وأضفه إلى الصفحة.
1. احفظ ملف PDF المحول.

```java
public static void convertEmfToPdf02(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         com.aspose.imaging.Image emfImage = com.aspose.imaging.Image.load(inputFile.toString());
         ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {
        emfImage.save(byteArrayOutputStream, new PngOptions());

        try (Page page = document.getPages().add()) {
            Image image = new Image();
            image.setImageStream(new ByteArrayInputStream(byteArrayOutputStream.toByteArray()));
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل GIF إلى PDF

استخدم هذا المثال عندما يجب إضافة صورة GIF إلى صفحة PDF.

1. قم بإنشاء [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغًا لمخرجات PDF.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ثم ضع ملف GIF مع `page.addImage(...)`.
1. حدد حدود الموضع باستخدام [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) بحيث تملأ الصورة مساحة الصفحة.
1. احفظ ملف PDF الناتج.

```java
public static void convertGifToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل JPEG إلى PDF

استخدم هذا المثال عندما يجب تحويل صورة JPEG إلى ملف PDF من صفحة واحدة.

1. قم بإنشاء [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغًا لملف PDF الناتج.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وأدخل صورة JPEG باستخدام `page.addImage(...)`.
1. استخدم [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) للتحكم في كيفية تعيين الصورة النقطية لإحداثيات الصفحة.
1. احفظ ملف PDF الذي تم إنشاؤه.

```java
public static void convertJpegToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PNG إلى PDF

استخدم هذا المثال عندما يجب أن يتم تغليف صورة PNG في مستند PDF.

1. قم بإنشاء [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغًا لمخرجات التحويل.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ثم ضع صورة PNG عليها باستخدام `page.addImage(...)`.
1. استخدم [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) لتغيير حجم الصورة مقابل لوحة الصفحة.
1. احفظ ملف الإخراج.

```java
public static void convertPngToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل SVG إلى PDF

استخدم هذا المثال عندما يجب عرض عمل فني SVG داخل مستند PDF.

1. افتح مصدر SVG عن طريق تمرير مسار الملف و[`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بتحليل علامة SVG وإنشاء نموذج رسومات PDF المقابل أثناء التحميل.
1. احفظ مخرجات PDF في مسار الملف الهدف.

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل TIFF إلى PDF

استخدم هذا المثال عندما يجب تحويل صورة TIFF إلى PDF.

1. قم بإنشاء [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغًا لمخرجات PDF.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ثم ضع صورة TIFF مع `page.addImage(...)`.
1. حدد منطقة الموضع باستخدام [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) بحيث يتم تعيين محتوى TIFF إلى إحداثيات الصفحة.
1. احفظ النتيجة بصيغة PDF.

```java
public static void convertTiffToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل CDR إلى PDF

استخدم هذا المثال عندما يجب تحويل ملف CorelDRAW CDR إلى PDF.

1. افتح مصدر CDR عن طريق تمرير مسار الملف و[`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) إلى المُنشئ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اسمح لـ Aspose.PDF بتحميل محتوى CorelDRAW في نموذج مستند PDF.
1. احفظ ملف PDF المحول إلى مسار الإخراج المطلوب.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

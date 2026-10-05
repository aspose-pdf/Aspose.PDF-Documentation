---
title: تحويل صيغ الصور إلى PDF في Java
linktitle: تحويل الصور إلى PDF
type: docs
weight: 60
url: /ar/java/convert-images-format-to-pdf/
lastmod: "2026-10-05"
description: تعلم كيفية تحويل صيغ BMP و CGM و DICOM و PNG و TIFF و EMF و SVG و CDR وغيرها من صيغ الصور إلى PDF في Java باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: كيفية تحويل الصور إلى PDF في Java
Abstract: تشرح هذه المقالة كيفية تحويل صيغ صور متعددة إلى PDF باستخدام Aspose.PDF for Java. تغطي وضع الصورة مباشرةً في صفحة PDF جديدة بالإضافة إلى خيارات التحميل الخاصة بنوع الملف لمدخلات CGM و SVG و CDR.
---
يمكن لـ Aspose.PDF for Java تحويل العديد من تنسيقات الصور النقطية والمتجهة إلى مستندات PDF.

## تحويل BMP إلى PDF

استخدم هذا المثال عندما يجب وضع صورة BMP في مستند PDF.

1. أنشئ كائنًا فارغًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) للاحتفاظ بملف PDF الناتج.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وضع BMP مع `page.addImage(...)`.
1. حدّد مستطيل الصورة الهدف بـ [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) لذا يملأ محتوى الراستر منطقة صفحة PDF..
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

1. افتح مصدر CGM بتمرير مسار الملف و [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المُنشئ.
1. دع Aspose.PDF يفسر تدفق الرسومات CGM أثناء تحميل المستند.
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

1. أنشئ كائنًا فارغًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) لإخراج PDF..
1. أنشئ كائنًا من الفئة [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/)، اضبطه [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) إلى `Dicom`، وعيّن مسار ملف المصدر.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وإلحاق صورة DICOM إلى مجموعة فقرات الصفحة.
1. احفظ النتيجة بصيغة PDF..

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

## تحويل EMF إلى PDF مع تحميل المستند مباشرة

استخدم هذا المثال عندما يجب تحويل ملف EMF إلى PDF عبر مسار التحميل الأساسي لـ EMF.

1. أنشئ كائنًا فارغًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وفتح مصدر EMF كسلسلة ثنائية.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وأزل هوامشها بحيث يمكن لعمل فن EMF أن يملأ مساحة الصفحة بالكامل.
1. أنشئ كائنًا من الفئة [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/)، اربط تدفق EMF به، وأضفه إلى مجموعة فقرات الصفحة.
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

## تحويل EMF إلى PDF مع سير عمل بديل

استخدم هذا المثال عندما يجب تحويل محتوى EMF باستخدام إعداد بديل أو تدفق تكوين الصفحة.

1. حمّل مصدر EMF باستخدام Aspose.Imaging وقم بتحويله إلى تدفق PNG في الذاكرة قبل وضعه في PDF..
1. أنشئ كائنًا فارغًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. أنشئ كائنًا من الفئة [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) من تدفق البايت الوسيط وأضفه إلى الصفحة.
1. احفظ ملف PDF المحوَّل.

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

1. أنشئ كائنًا فارغًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) لإخراج PDF..
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وضع GIF مع `page.addImage(...)`.
1. حدّد حدود الموضع باستخدام [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) لذلك الصورة تملأ مساحة الصفحة.
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

1. أنشئ كائنًا فارغًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) للـ PDF الناتج.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وأدرج صورة JPEG مع `page.addImage(...)`.
1. استخدم [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) للتحكم في كيفية تعيين صورة الرستر إلى إحداثيات الصفحة.
1. احفظ ملف PDF المُولد.

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

استخدم هذا المثال عندما يجب تضمين صورة PNG في مستند PDF.

1. أنشئ كائنًا فارغًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) لإخراج التحويل.
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وضع صورة PNG عليها باستخدام `page.addImage(...)`.
1. استخدم [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) لتحجيم الصورة بالنسبة إلى لوحة الصفحة.
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

استخدم هذا المثال عندما يجب عرض رسومات SVG داخل مستند PDF.

1. افتح مصدر SVG بتمرير مسار الملف و [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المُنشئ.
1. دع Aspose.PDF يحلل ترميز SVG وينشئ نموذج رسومات PDF المقابل أثناء التحميل.
1. احفظ ناتج PDF إلى مسار الملف المستهدف.

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

1. أنشئ كائنًا فارغًا من الفئة [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) لإخراج PDF..
1. أضف [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وضع صورة TIFF مع `page.addImage(...)`.
1. حدّد منطقة التحديد باستخدام [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) لذا يتم تعيين محتوى TIFF إلى إحداثيات الصفحة.
1. احفظ النتيجة بصيغة PDF..

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

1. افتح مصدر CDR بتمرير مسار الملف و [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) إلى [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المُنشئ.
1. دع Aspose.PDF يحمل محتوى CorelDRAW إلى نموذج مستند PDF..
1. احفظ ملف PDF المحول إلى مسار الإخراج المطلوب.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

---
title: تحويل PDF إلى صيغ صور في Java
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /ar/java/convert-pdf-to-images-format/
lastmod: "2026-10-01"
description: تعلم كيفية تحويل صفحات PDF إلى ملفات TIFF و BMP و EMF و JPEG و PNG و GIF و SVG في Java باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: تحويل صفحات PDF إلى TIFF و PNG و JPEG و GIF و BMP و EMF و SVG في Java
Abstract: تشرح هذه المقالة كيفية تحويل ملفات PDF إلى صيغ الصور الشائعة باستخدام Aspose.PDF for Java. وتغطي تصدير TIFF على مستوى المستند بالكامل، وإنشاء الرسوم النقطية لكل صفحة باستخدام أجهزة الصور، واستبدال الخطوط الاختياري أثناء تصدير PNG، وإخراج SVG باستخدام `SvgSaveOptions`.
---
يمكن لـ Aspose.PDF for Java تحويل صفحات PDF إلى تنسيقات صور نقطية ومتجهة مع خيارات جهاز محددة لكل تنسيق.

## تحويل PDF إلى BMP

استخدم هذا المثال عندما يجب عرض صفحات PDF كصور BMP.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) مع [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 DPI.
1. التكرار عبر `document.getPages()` و استدع `device.process(...)` لكل صفحة.
1. احفظ صور BMP التي تم إنشاؤها إلى مسارات إخراج مرقمة.

```java
public static void convertPdfToBmp(Path inputFile, Path outputPrefix) {
       try (Document document = new Document(inputFile.toString())) {
           BmpDevice device = new BmpDevice(new Resolution(300));
           for (int page = 1; page <= document.getPages().size(); page++) {
               device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "bmp"));
           }
       }
       System.out.println(inputFile + " converted into " + outputPrefix);
   }
```

## تحويل PDF إلى EMF

استخدم هذا المثال عندما يجب تصدير صفحات PDF كصور متجهة بصيغة EMF.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) مع [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 DPI.
1. التكرار عبر الصفحات واستدعاء `device.process(...)` لكل صفحة.
1. احفظ مخرجات EMF إلى مسارات ملفات مرقمة.

```java
public static void convertPdfToEmf(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        EmfDevice device = new EmfDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "emf"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## تحويل PDF إلى GIF

استخدم هذا المثال عندما يجب تحويل صفحات PDF إلى صور GIF.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) مع [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 DPI.
1. التكرار عبر الصفحات واستدعاء `device.process(...)` لعرض كل صفحة.
1. احفظ ملفات GIF إلى مسارات إخراج مرقمة.

```java
public static void convertPdfToGif(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        GifDevice device = new GifDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "gif"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## تحويل PDF إلى JPEG

استخدم هذا المثال عندما يجب تصدير صفحات PDF كصور JPEG.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) مع [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 DPI.
1. التكرار عبر الصفحات واستدعاء `device.process(...)` لتحويل كل صفحة إلى JPEG.
1. احفظ ملفات JPEG الناتجة إلى مسارات مرقمة.

```java
public static void convertPdfToJpeg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        JpegDevice device = new JpegDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "jpeg"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## تحويل PDF إلى PNG

استخدم هذا المثال عندما يجب تحويل صفحات PDF إلى صور PNG.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) مع [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 DPI.
1. التكرار عبر الصفحات واستدعاء `device.process(...)` لكل صفحة PDF.
1. احفظ مخرجات PNG إلى مسارات ملفات مرقمة.

```java
public static void convertPdfToPng(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## تحويل PDF إلى PNG مع احتياطي للخط الافتراضي

استخدم هذا المثال عندما يجب أن يستخدم العرض خطًا احتياطيًا للرموز المفقودة.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) مع [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 DPI.
1. تمكين `document.setAbsentFontTryToSubstitute(true)` حتى يتمكن الحروف المفقودة من الرجوع إلى خطوط بديلة أثناء العرض.
1. قم بتصوير الصفحات وحفظ ملفات PNG.

```java
public static void convertPdfToPngWithDefaultFont(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        document.setAbsentFontTryToSubstitute(true);
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## تحويل PDF إلى SVG

استخدم هذا المثال عندما يجب تصدير صفحات PDF كرسومات SVG.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) وإيقاف ضغط ZIP عند RAW `.svg` مطلوب الإخراج.
1. تمكين `setTreatTargetFileNameAsDirectory(true)` لذلك يمكن تنظيم مخرجات SVG لكل صفحة تحت مسار الهدف.
1. احفظ مخرجات SVG.

```java
public static void convertPdfToSvg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        SvgSaveOptions saveOptions = new SvgSaveOptions();
        saveOptions.setCompressOutputToZipArchive(false);
        saveOptions.setTreatTargetFileNameAsDirectory(true);
        document.save(outputPrefix + ".svg", saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## تحويل PDF إلى TIFF

استخدم هذا المثال عندما يجب تصدير صفحة أو أكثر من صفحات PDF إلى TIFF.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) وتكوين الضغط، عمق اللون، وسلوك الصفحات الفارغة.
1. إنشاء [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) مع [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 نقطة في البوصة وإعدادات TIFF المُحضرة.
1. قم بتصيير الصفحات واحفظ إخراج TIFF.

```java
public static void convertPdfToTiff(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.LZW);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setSkipBlankPages(false);

        TiffDevice tiffDevice = new TiffDevice(new Resolution(300), tiffSettings);
        tiffDevice.process(document, outputPrefix + ".tiff");
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

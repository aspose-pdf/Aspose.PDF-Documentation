---
title: تحويل PDF إلى تنسيقات الصور في جافا
linktitle: تحويل قوات الدفاع الشعبي إلى الصور
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2026-06-16"
description: تعرف على كيفية عرض صفحات PDF كملفات TIFF، وBMP، وEMF، وJPEG، وPNG، وGIF، وSVG في Java باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: تحويل صفحات PDF إلى TIFF، PNG، JPEG، GIF، BMP، EMF، وSVG في Java
Abstract: يشرح هذا المقال كيفية تحويل ملفات PDF إلى تنسيقات صور شائعة باستخدام Aspose.PDF لـ Java. ويغطي تصدير TIFF على مستوى المستند، وإنشاء البيانات النقطية لكل صفحة باستخدام أجهزة الصور، واستبدال الخط الاختياري أثناء تصدير PNG، وإخراج SVG باستخدام `SvgSaveOptions`.
---
يمكن لـ Aspose.PDF for Java عرض صفحات PDF بتنسيقات صور نقطية ومتجهة مع خيارات جهاز خاصة بالتنسيق.

## تحويل قوات الدفاع الشعبي إلى BMP

استخدم هذا المثال عندما يجب عرض صفحات PDF كصور BMP.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) باستخدام [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 نقطة في البوصة.
1. قم بالتكرار عبر `document.getPages()` واتصل بـ`device.process(...)` لكل صفحة.
1. حفظ صور BMP التي تم إنشاؤها إلى مسارات الإخراج المرقمة.

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

## تحويل قوات الدفاع الشعبي إلى EMF

استخدم هذا المثال عندما يجب تصدير صفحات PDF كصور متجهة لـ EMF.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) باستخدام [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 نقطة لكل بوصة.
1. كرر الصفحات واتصل بـ `device.process(...)` لكل صفحة.
1. احفظ مخرجات EMF في مسارات الملفات المرقمة.

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

## تحويل قوات الدفاع الشعبي إلى GIF

استخدم هذا المثال عندما يجب تحويل صفحات PDF إلى صور GIF.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) باستخدام [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 نقطة في البوصة.
1. كرر الصفحات واتصل بـ `device.process(...)` لعرض كل صفحة.
1. احفظ ملفات GIF في مسارات الإخراج المرقمة.

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

## تحويل قوات الدفاع الشعبي إلى JPEG

استخدم هذا المثال عندما يجب تصدير صفحات PDF كصور JPEG.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) باستخدام [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 نقطة في البوصة.
1. قم بالتكرار عبر الصفحات واتصل بـ `device.process(...)` لتنقيط كل صفحة إلى JPEG.
1. احفظ ملفات إخراج JPEG في مسارات مرقمة.

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

## تحويل قوات الدفاع الشعبي إلى PNG

استخدم هذا المثال عندما يجب تحويل صفحات PDF إلى صور PNG.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) باستخدام [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 نقطة في البوصة.
1. كرر الصفحات واتصل بـ `device.process(...)` لكل صفحة PDF.
1. احفظ مخرجات PNG في مسارات الملفات المرقمة.

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

## قم بتحويل PDF إلى PNG باستخدام خط احتياطي افتراضي

استخدم هذا المثال عندما يجب أن يستخدم العرض خطًا احتياطيًا للحروف الرسومية المفقودة.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) باستخدام [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 نقطة في البوصة.
1. قم بتمكين `document.setAbsentFontTryToSubstitute(true)` حتى تتمكن الحروف الرسومية المفقودة من الرجوع إلى الخطوط البديلة أثناء العرض.
1. قم بعرض الصفحات وحفظ ملفات PNG.

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

## تحويل قوات الدفاع الشعبي إلى SVG

استخدم هذا المثال عندما يجب تصدير صفحات PDF كرسومات SVG.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) وقم بتعطيل ضغط ZIP عندما يكون الإخراج الأولي `.svg` مطلوبًا.
1. قم بتمكين `setTreatTargetFileNameAsDirectory(true)` بحيث يمكن تنظيم إخراج SVG لكل صفحة ضمن المسار المستهدف.
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

## تحويل قوات الدفاع الشعبي إلى TIFF

استخدم هذا المثال عندما يجب تصدير صفحة PDF واحدة أو أكثر إلى TIFF.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) وقم بتكوين الضغط وعمق الألوان وسلوك الصفحة الفارغة.
1. قم بإنشاء [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) باستخدام [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 300 نقطة في البوصة وإعدادات TIFF المعدة.
1. قم بعرض الصفحات وحفظ مخرجات TIFF.

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

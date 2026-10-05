---
title: تحويل PDF إلى EPUB، Text، XPS، وأكثر في Java
linktitle: تحويل PDF إلى صيغ أخرى
type: docs
weight: 90
url: /ar/java/convert-pdf-to-other-files/
lastmod: "2026-10-05"
description: تعلم كيفية تحويل ملفات PDF إلى EPUB و LaTeX و Markdown ونص و XPS و MobiXML باستخدام Java و Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى صيغ أخرى باستخدام Java
Abstract: تشرح هذه المقالة كيفية تحويل ملفات PDF إلى صيغ EPUB و TeX و Markdown والنص و XPS و MobiXML باستخدام Aspose.PDF for Java، مع خيارات حفظ مخصصة لكل صيغة عند الحاجة.
---
يمكن لـ Aspose.PDF for Java تصدير مستندات PDF إلى صيغ نصية، وصيغ كتب إلكترونية، وصيغ للطباعة، وصيغ مخرجات موجهة للترميز.

## تحويل PDF إلى EPUB

استخدم هذا المثال عندما يجب تصدير مستند PDF إلى تنسيق الكتاب الإلكتروني EPUB.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. أنشئ كائنًا من الفئة [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) واضبط وضع التعرف إلى `Flow`.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذا يتم تصدير محتوى PDF على هيئة ترميز EPUB قابل لإعادة التدفق.
1. احفظ ملف EPUB المحوّل.

```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            EpubSaveOptions saveOptions = new EpubSaveOptions();
            saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
            document.save(outputFile.toString(), saveOptions);
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## تحويل PDF إلى TeX

استخدم هذا المثال عندما يجب تصدير محتوى PDF إلى تنسيق TeX.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. أنشئ كائنًا من الفئة [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) للتسلسل في TeX..
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذلك يتم إصدار محتوى PDF على شكل تنسيق TeX..
1. احفظ ملف TeX الناتج.

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى نص عادي

استخدم هذا المثال عندما يجب تصدير مستند PDF كملف نصي.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. أنشئ كائنًا من الفئة [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) استخراج المحتوى النصي من صفحات PDF..
1. استدعِ `device.process(document.getPages().get_Item(1), outputFile.toString())` لِكتابة الصفّحة الأولى كنص عادي.
1. احفظ ملف النص الناتج.

```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى XPS

استخدم هذا المثال عندما يجب تحويل مستند PDF إلى تنسيق XPS.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. أنشئ كائنًا من الفئة [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) وفعّل الخطوط TrueType المدمجة.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذا يتم تسلسل PDF كـ XPS مع موارد الخط المدمجة.
1. احفظ ملف XPS المحوَّل.

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى Markdown

استخدم هذا المثال عندما يجب تصدير محتوى PDF كـ Markdown.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. أنشئ كائنًا من الفئة [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) وتهيئة دليل موارد الصورة بالإضافة إلى مخرجات وسم صورة HTML.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذا يتم إصدار محتوى PDF كـ Markdown مع موارد صور خارجية.
1. احفظ ملف Markdown المُولّد.

```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى Mobi XML

استخدم هذا المثال عندما يجب تصدير محتوى PDF إلى XML متوافق مع Mobi.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. اختر [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` كصيغة التسلسل المستهدفة.
1. استدعِ `document.save(outputFile.toString(), SaveFormat.MobiXml)` لذا يتم تصدير ملف PDF كملف XML متوافق مع Mobi..
1. احفظ الملف المحول.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

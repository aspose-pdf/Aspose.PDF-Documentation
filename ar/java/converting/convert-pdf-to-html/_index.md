---
title: تحويل PDF إلى HTML في Java
linktitle: تحويل PDF إلى تنسيق HTML
type: docs
weight: 50
url: /ar/java/convert-pdf-to-html/
lastmod: "2026-10-05"
description: تعلم كيفية تحويل PDF إلى HTML في Java باستخدام Aspose.PDF، بما في ذلك الإخراج متعدد الصفحات، مجلدات الصور الخارجية، معالجة SVG، وتصيير HTML متعدد الطبقات.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى HTML في Java
Abstract: تشرح هذه المقالة كيفية تحويل ملفات PDF إلى HTML باستخدام Aspose.PDF for Java. وتغطي تصدير HTML الأساسي بالإضافة إلى خيارات مجلدات الصور، تقسيم الصفحات، مخرجات SVG، رسومات SVG مضغوطة، خلفيات الصفحات PNG، ترميز الجسم فقط، عرض النص الشفاف، وتحويل طبقة المستند.
---
يدعم Aspose.PDF for Java تصدير HTML مع خيارات للصور، وSVG، وتقسيم الصفحات، والشفافية، وعرض الطبقات. استخدم [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) للتحكم في كيفية كتابة صفحات PDF والموارد والترميز إلى إخراج HTML.

## تحويل PDF إلى HTML

استخدم هذا المثال عندما يجب تصدير ملف PDF إلى مستند HTML قياسي.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ الإعداد الافتراضي [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) للتسلسل القياسي لـ HTML..
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذا يتم تصدير محتوى صفحة PDF كعلامات HTML..
1. احفظ مخرجات HTML التي تم إنشاؤها.

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى HTML وتخزين الصور بشكل منفصل

استخدم هذا المثال عندما يجب كتابة الصور المستخرجة كملفات منفصلة أثناء تصدير HTML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وضع `setSpecialFolderForAllImages(...)` إلى دليل إخراج صور مخصص.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذا يتم إصدار صور النقطية كملفات موارد منفصلة بدلاً من الإخراج داخل السطر فقط.
1. احفظ مخرجات HTML إلى جانب الأصول المتولدة للصور.

```java
public static void convertPdfToHtmlStoringImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForAllImages(inputFile.getParent().resolve("images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى HTML متعدد الصفحات

استخدم هذا المثال عندما يجب تمثيل كل صفحة PDF بشكل منفصل في مخرجات HTML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وفعّل `setSplitIntoPages(true)`.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذلك يتم كتابة كل صفحة PDF كمخرج HTML منفصل.
1. احفظ ملفات HTML التي تم إنشاؤها.

```java
public static void convertPdfToHtmlMultiPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى HTML وتخزين SVG بشكل منفصل

استخدم هذا المثال عندما يجب إصدار محتوى المتجهات كموارد SVG منفصلة.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وضع `setSpecialFolderForSvgImages(...)` إلى دليل موارد SVG خارجي.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذا تُخزن الرسومات المتجهية خارج ملف HTML الرئيسي.
1. احفظ مخرجات HTML وأصول SVG.

```java
public static void convertPdfToHtmlStoringSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى HTML مع SVG مضغوط

استخدم هذا المثال عندما يجب تحسين إخراج SVG أثناء تصدير HTML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وتهيئة مجلد مخصص لموارد SVG..
1. فعّل `setCompressSvgGraphicsIfAny(true)` لذلك يتم ضغط ملفات SVG أثناء التصدير.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` واحفظ ملفات HTML المحوَّلة.

```java
public static void convertPdfToHtmlCompressSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        saveOptions.setCompressSvgGraphicsIfAny(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى HTML مع خلفيات صفحات PNG

استخدم هذا المثال عندما يجب عرض خلفيات الصفحات كصور PNG في مخرجات HTML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وعيّن وضع حفظ الصورة النقطية إلى خلفيات الصفحات بصيغة PNG..
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذلك يتم إصدار محتوى خلفية الصفحة كطبقات HTML مدعومة بـ PNG..
1. احفظ مخرجات HTML المحولة.

```java
public static void convertPdfToHtmlPngBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setRasterImagesSavingMode(
                HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى محتوى جسم HTML فقط

استخدم هذا المثال عندما تكون الحاجة فقط إلى ترميز الجسم بدلاً من هيكل مستند HTML كامل.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) واضبط وضع إنشاء العلامات إلى `WriteOnlyBodyContent`.
1. احتفظ `setSplitIntoPages(true)` مفعَّل عندما يجب أن يظل الإخراج الذي يقتصر على النص مفصولًا إلى صفحات.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` واحفظ مخرجات HTML..

```java
public static void convertPdfToHtmlBodyContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setHtmlMarkupGenerationMode(
                HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى HTML مع عرض النص الشفاف

استخدم هذا المثال عندما يجب الحفاظ على النص الشفاف في تصدير HTML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وفعّل حفظ النص الشفاف والمظلل.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذلك يتم الاحتفاظ بمظهر النص المتعلق بالشفافية في نتيجة HTML..
1. احفظ مخرجات HTML المحولة.

```java
public static void convertPdfToHtmlTransparentTextRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSaveTransparentTexts(true);
        saveOptions.setSaveShadowedTextsAsTransparentTexts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى HTML مع عرض طبقة المستند

استخدم هذا المثال عندما يجب عكس رؤية طبقة PDF في نتيجة HTML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وفعّل `setConvertMarkedContentToLayers(true)`.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` يتم تعيين محتوى PDF المحدد إلى طبقات HTML..
1. احفظ ملفات HTML المصدرة.

```java
public static void convertPdfToHtmlDocumentLayersRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setConvertMarkedContentToLayers(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

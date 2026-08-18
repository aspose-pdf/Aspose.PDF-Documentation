---
title: تحويل PDF إلى HTML في جافا
linktitle: تحويل PDF إلى تنسيق HTML
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2026-06-16"
description: تعرف على كيفية تحويل PDF إلى HTML في Java باستخدام Aspose.PDF، بما في ذلك الإخراج متعدد الصفحات، ومجلدات الصور الخارجية، ومعالجة SVG، وعرض HTML متعدد الطبقات.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى HTML في جافا
Abstract: يشرح هذا المقال كيفية تحويل ملفات PDF إلى HTML باستخدام Aspose.PDF لـ Java. وهو يغطي تصدير HTML الأساسي مع خيارات لمجلدات الصور، وتقسيم الصفحات، ومخرجات SVG، ورسومات SVG المضغوطة، وخلفيات صفحات PNG، وترميز النص الأساسي فقط، وعرض النص الشفاف، وتحويل طبقة المستندات.
---
يدعم Aspose.PDF for Java تصدير HTML مع خيارات للصور وSVG وتقسيم الصفحة والشفافية وعرض الطبقة. استخدم [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) للتحكم في كيفية كتابة صفحات PDF والموارد والعلامات إلى مخرجات HTML.

## تحويل قوات الدفاع الشعبي إلى HTML

استخدم هذا المثال عندما يجب تصدير ملف PDF إلى مستند HTML قياسي.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) الافتراضي لتسلسل HTML القياسي.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم تصدير محتوى صفحة PDF كعلامة HTML.
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
1. قم بإنشاء [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وقم بتعيين `setSpecialFolderForAllImages(...)` على دليل إخراج صورة مخصص.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم إصدار الصور النقطية كملفات موارد منفصلة بدلاً من الإخراج المضمن فقط.
1. احفظ مخرجات HTML مع أصول الصورة التي تم إنشاؤها.

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
1. أنشئ [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وقم بتمكين `setSplitIntoPages(true)`.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى تتم كتابة كل صفحة PDF كمخرجات HTML منفصلة.
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

استخدم هذا المثال عندما يجب أن يتم إصدار محتوى متجه كموارد SVG منفصلة.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وقم بتعيين `setSpecialFolderForSvgImages(...)` على دليل موارد SVG خارجي.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم تخزين الرسومات المتجهة خارج ملف HTML الرئيسي.
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

## تحويل PDF إلى HTML باستخدام SVG المضغوط

استخدم هذا المثال عندما يجب تحسين إخراج SVG أثناء تصدير HTML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وقم بتكوين مجلد مخصص لموارد SVG.
1. قم بتمكين `setCompressSvgGraphicsIfAny(true)` حتى يتم ضغط أصول SVG أثناء التصدير.
1. اتصل `document.save(outputFile.toString(), saveOptions)` واحفظ ملفات HTML المحولة.

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

## تحويل PDF إلى HTML مع خلفيات صفحة PNG

استخدم هذا المثال عندما يجب عرض خلفيات الصفحة كصور PNG في مخرجات HTML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وقم بتعيين وضع حفظ الصور النقطية على خلفيات صفحة PNG.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم إصدار محتوى خلفية الصفحة كطبقات HTML مدعومة بـ PNG.
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

## تحويل PDF إلى محتوى نص HTML فقط

استخدم هذا المثال عندما تكون هناك حاجة إلى ترميز النص فقط بدلاً من غلاف مستند HTML الكامل.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وقم بتعيين وضع إنشاء العلامات على `WriteOnlyBodyContent`.
1. احتفظ بتمكين `setSplitIntoPages(true)` عندما يكون الإخراج الأساسي فقط مفصولاً بالصفحة.
1. اتصل بـ`document.save(outputFile.toString(), saveOptions)` واحفظ مخرجات HTML.

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

## تحويل PDF إلى HTML مع عرض نص شفاف

استخدم هذا المثال عندما يجب الحفاظ على النص الشفاف في تصدير HTML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وقم بتمكين الاحتفاظ بالنص الشفاف والمظلل.
1. اتصل بـ`document.save(outputFile.toString(), saveOptions)` حتى يتم الاحتفاظ بمظهر النص المتعلق بالشفافية في نتيجة HTML.
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

## تحويل PDF إلى HTML مع عرض طبقة الوثيقة

استخدم هذا المثال عندما يجب أن تنعكس رؤية طبقة PDF في نتيجة HTML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) وقم بتمكين `setConvertMarkedContentToLayers(true)`.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم تعيين محتوى PDF المميز إلى طبقات HTML.
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

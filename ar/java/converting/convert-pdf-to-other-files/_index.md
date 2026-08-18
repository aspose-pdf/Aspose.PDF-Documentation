---
title: تحويل PDF إلى EPUB، والنص، وXPS، والمزيد في Java
linktitle: تحويل PDF إلى صيغ أخرى
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2026-06-16"
description: تعرف على كيفية تحويل ملفات PDF إلى EPUB، وLaTeX، وMarkdown، وtext، وXPS، وMobiXML في Java باستخدام Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى تنسيقات أخرى في جافا
Abstract: تشرح هذه المقالة كيفية تحويل ملفات PDF إلى تنسيقات EPUB، وTeX، وMarkdown، وtext، وXPS، وMobiXML باستخدام Aspose.PDF لـ Java، مع خيارات حفظ خاصة بالتنسيق عند الحاجة.
---
يمكن لـ Aspose.PDF for Java تصدير مستندات PDF إلى تنسيقات نصية وكتب إلكترونية وطباعة وتنسيقات موجهة نحو العلامات.

## تحويل قوات الدفاع الشعبي إلى EPUB

استخدم هذا المثال عندما يجب تصدير مستند PDF إلى تنسيق الكتاب الإلكتروني EPUB.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) وقم بتعيين وضع التعرف على `Flow`.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم تصدير محتوى PDF كعلامة EPUB قابلة لإعادة التدفق.
1. احفظ ملف EPUB المحول.

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

## تحويل قوات الدفاع الشعبي إلى تكس

استخدم هذا المثال عندما يجب تصدير محتوى PDF إلى علامة TeX.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) لتسلسل TeX.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم إصدار محتوى PDF كعلامة TeX.
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

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) لاستخراج المحتوى النصي من صفحات PDF.
1. اتصل بـ `device.process(document.getPages().get_Item(1), outputFile.toString())` لكتابة الصفحة الأولى كنص عادي.
1. احفظ ملف إخراج النص.

```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل قوات الدفاع الشعبي إلى XPS

استخدم هذا المثال عندما يجب تحويل مستند PDF إلى تنسيق XPS.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) وقم بتمكين خطوط TrueType المضمنة.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم إجراء تسلسل لملف PDF بتنسيق XPS مع موارد الخطوط المضمنة.
1. احفظ ملف XPS المحول.

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

## تحويل قوات الدفاع الشعبي إلى تخفيض السعر

استخدم هذا المثال عندما يجب تصدير محتوى PDF كـ Markdown.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) وقم بتكوين دليل موارد الصورة بالإضافة إلى إخراج علامة صورة HTML.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم إصدار محتوى PDF كـ Markdown مع موارد الصور الخارجية.
1. احفظ ملف Markdown الذي تم إنشاؤه.

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

## تحويل PDF إلى موبي XML

استخدم هذا المثال عندما يجب تصدير محتوى PDF إلى XML المتوافق مع Mobi.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حدد [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` كتنسيق التسلسل المستهدف.
1. اتصل بـ `document.save(outputFile.toString(), SaveFormat.MobiXml)` حتى يتم تصدير ملف PDF بتنسيق XML متوافق مع Mobi.
1. احفظ الملف المحول.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

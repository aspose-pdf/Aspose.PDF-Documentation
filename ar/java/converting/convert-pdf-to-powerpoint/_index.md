---
title: تحويل PDF إلى PowerPoint في Java
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /ar/java/convert-pdf-to-powerpoint/
description: تعرّف على كيفية تحويل ملفات PDF إلى PowerPoint في Java باستخدام Aspose.PDF، بما في ذلك الشرائح القابلة للتحرير بصيغة PPTX، والشرائح المعتمدة على الصور، ودقة الصورة المخصصة.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى PowerPoint في Java
Abstract: تشرح هذه المقالة كيفية تحويل ملفات PDF إلى عروض PowerPoint باستخدام Aspose.PDF for Java. تغطي التحويل القياسي إلى PPTX، وإخراج الشريحة كصورة، والتحكم في دقة الصورة عبر `PptxSaveOptions`.
---
يدعم Aspose.PDF for Java تصدير صفحات PDF إلى عروض PowerPoint قابلة للتحرير مع خيارات عرض الشرائح. استخدم [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) للتحكم في كيفية تعيين صفحات PDF إلى شرائح PowerPoint.

## تحويل PDF إلى PPTX

استخدم هذا المثال عندما ينبغي تصدير مستند PDF كعرض PowerPoint قياسي.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ الافتراضي [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) لتصدير PowerPoint قابل للتحرير.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذلك يتم تسلسل صفحات PDF كـ `.pptx` عرض.
1. احفظ ملف PPTX المحول.

```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى PPTX مع الشرائح كصور

استخدم هذا المثال عندما يجب أن تتحول كل صفحة PDF إلى شريحة PowerPoint مستندة إلى صورة.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) وفعّل `setSlidesAsImages(true)`.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذا يتم عرض كل صفحة PDF كشريحة مدعومة بصورة في العرض التقديمي.
1. احفظ ملف PPTX الذي تم إنشاؤه.

```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setSlidesAsImages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى PPTX بدقة صورة مخصصة

استخدم هذا المثال عندما يجب التحكم في جودة صورة الشريحة أثناء تصدير PDF إلى PPTX.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) واضبط `setImageResolution(300)` لتحقيق دقة أعلى لصورة الشريحة.
1. استدعِ `document.save(outputFile.toString(), saveOptions)` لذلك يتم إنشاء محتوى الشريحة المتراكم بتقنية النقطية بالدقة المطلوبة.
1. احفظ العرض التقديمي الناتج.

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setImageResolution(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

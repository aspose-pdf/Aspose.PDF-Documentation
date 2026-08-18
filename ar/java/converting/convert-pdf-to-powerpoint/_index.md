---
title: تحويل PDF إلى PowerPoint في جافا
linktitle: تحويل قوات الدفاع الشعبي إلى PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
description: تعرف على كيفية تحويل ملفات PDF إلى PowerPoint في Java باستخدام Aspose.PDF، بما في ذلك شرائح PPTX القابلة للتحرير، والشرائح المستندة إلى الصور، ودقة الصورة المخصصة.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى PowerPoint في جافا
Abstract: تشرح هذه المقالة كيفية تحويل ملفات PDF إلى عروض PowerPoint التقديمية باستخدام Aspose.PDF لـ Java. ويغطي تحويل PPTX القياسي، وإخراج الشريحة كصورة، والتحكم في دقة الصورة من خلال `PptxSaveOptions`.
---
يدعم Aspose.PDF for Java تصدير صفحات PDF إلى عروض PowerPoint التقديمية القابلة للتحرير مع خيارات عرض الشرائح. استخدم [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) للتحكم في كيفية تعيين صفحات PDF في شرائح PowerPoint.

## تحويل قوات الدفاع الشعبي إلى PPTX

استخدم هذا المثال عندما يجب تصدير مستند PDF كعرض تقديمي قياسي لـ PowerPoint.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) الافتراضي لتصدير PowerPoint القابل للتحرير.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم إجراء تسلسل لصفحات PDF كعرض تقديمي `.pptx`.
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

استخدم هذا المثال عندما تصبح كل صفحة PDF شريحة PowerPoint مبنية على صورة.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) وقم بتمكين `setSlidesAsImages(true)`.
1. اتصل بـ`document.save(outputFile.toString(), saveOptions)` حتى يتم عرض كل صفحة PDF كشريحة مدعومة بالصورة في العرض التقديمي.
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
1. قم بإنشاء [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) وقم بتعيين `setImageResolution(300)` للحصول على دقة أعلى لصورة الشريحة.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم إنشاء محتوى الشريحة النقطية بالدقة المطلوبة.
1. حفظ العرض التقديمي الناتج.

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

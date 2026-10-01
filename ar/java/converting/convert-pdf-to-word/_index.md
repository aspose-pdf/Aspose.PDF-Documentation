---
title: تحويل PDF إلى Word في Java
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /ar/java/convert-pdf-to-word/
lastmod: "2026-10-01"
description: تعلم كيفية تحويل ملفات PDF إلى DOC و DOCX في Java باستخدام Aspose.PDF لتسهيل تحرير المستندات وإعادة استخدامها.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى Word في Java
Abstract: تشرح هذه المقالة كيفية تحويل ملفات PDF إلى صيغ Microsoft Word باستخدام Aspose.PDF for Java. وتغطي مخرجات DOC، مخرجات DOCX، تحويل DOCX بتدفق محسّن، الحفاظ على فواصل السطر، التعرف على الرصاصات، والتحكم في دقة الصورة من خلال `DocSaveOptions`.
---
Aspose.PDF for Java يمكنه تصدير مستندات PDF إلى صيغ Microsoft Word مع خيارات مختلفة للتعرف والتخطيط. Use [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) للتحكم في كيفية تحويل نص PDF والقوائم والصور إلى مخرجات Word.

## تحويل PDF إلى DOC

استخدم هذا المثال عندما يجب تصدير مستند PDF إلى تنسيق DOC القديم. يقوم الكود بإنشاء `DocSaveOptions`، يضبط الصيغة إلى `Doc`, ويمرّر الخيارات إلى طريقة حفظ مشتركة.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) وقم بتعيين التنسيق إلى `Doc`.
1. اتصال `document.save(outputFile.toString(), saveOptions)` لذلك يتم تصدير ملف PDF إلى تنسيق مستند مايكروسوفت وورد الثنائي.
1. احفظ ملف DOC المحول.

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى DOCX

استخدم هذا المثال عندما يجب تصدير مستند PDF كملف DOCX. DOCX هو التنسيق المفضل لمعظم سير عمل معالجة النصوص الحديثة لأنه مدعوم على نطاق واسع وأسهل في التحرير.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) وقم بتعيين التنسيق إلى `DocX`.
1. اتصال `document.save(outputFile.toString(), saveOptions)` لذلك يتم تصدير محتوى PDF كوثيقة Word بصيغة Office Open XML.
1. احفظ ملف DOCX الناتج.

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى DOCX مع تحسين التعرف على التدفق

استخدم هذا المثال عندما يجب أن يفضّل تصدير Word المحتوى القابل للتحرير المتدفّق بدلاً من التخطيط البصري الثابت.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) لـ `DocX` الإخراج.
1. تفعيل `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` لذلك يستخدم المحول التعرف المحسن على التدفق أثناء إنشاء DOCX.
1. اتصال `document.save(outputFile.toString(), saveOptions)` واحفظ ناتج DOCX المحول.

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى DOCX مع الحفاظ على فواصل الأسطر

استخدم هذا المثال عندما يجب الاحتفاظ بنهايات الأسطر من ملف PDF الأصلي في مخرجات Word.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) لـ `DocX` تصدير.
1. تفعيل `setAddReturnToLineEnd(true)` لذا يتم الحفاظ على فواصل الأسطر الصريحة أثناء التحويل.
1. اتصال `document.save(outputFile.toString(), saveOptions)` وحفظ ملف DOCX.

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى DOCX مع التعرف على القوائم النقطية

استخدم هذا المثال عندما يجب التعرف على نقط القوائم من ملف PDF المصدر والحفاظ عليها كهيكليات قوائم في Word.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) لـ `DocX` تصدير.
1. تفعيل `setRecognizeBullets(true)` لذلك يتم التعرف على محتوى PDF الشبيه بالقوائم كقوائم نقطية أثناء التحويل.
1. اتصال `document.save(outputFile.toString(), saveOptions)` وحفظ ملف DOCX.

```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى DOCX مع دقة صورة مخصصة

استخدم هذا المثال عندما يجب التحكم في جودة الصورة داخل ملف DOCX الذي تم إنشاؤه أثناء التحويل.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) لـ `DocX` تصدير.
1. مجموعة `setImageResolutionX(300)` و `setImageResolutionY(300)` لذلك يتم إنشاء محتوى النقطية بالدقة المطلوبة.
1. اتصال `document.save(outputFile.toString(), saveOptions)` وحفظ مخرجات DOCX.

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

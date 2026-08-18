---
title: تحويل PDF إلى Word في جافا
linktitle: تحويل قوات الدفاع الشعبي إلى كلمة
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2026-06-16"
description: تعرف على كيفية تحويل ملفات PDF إلى DOC وDOCX في Java باستخدام Aspose.PDF لتسهيل تحرير المستندات وإعادة استخدامها.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى Word في جافا
Abstract: يشرح هذا المقال كيفية تحويل ملفات PDF إلى تنسيقات Microsoft Word باستخدام Aspose.PDF لـ Java. وهو يغطي إخراج DOC، وإخراج DOCX، وتحويل DOCX المحسّن، وفواصل الأسطر المحفوظة، والتعرف على التعداد النقطي، والتحكم في دقة الصورة من خلال `DocSaveOptions`.
---
يمكن لـ Aspose.PDF for Java تصدير مستندات PDF إلى تنسيقات Microsoft Word مع خيارات التعرف والتخطيط المختلفة. استخدم [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) للتحكم في كيفية تعيين نص PDF والقوائم والصور في مخرجات Word.

## تحويل قوات الدفاع الشعبي إلى DOC

استخدم هذا المثال عندما يجب تصدير مستند PDF إلى تنسيق DOC القديم. يقوم الكود بإنشاء `DocSaveOptions`، ويضبط التنسيق على `Doc`، ويمرر الخيارات إلى طريقة حفظ مشتركة.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) وقم بتعيين التنسيق على `Doc`.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم تصدير ملف PDF إلى تنسيق مستند Microsoft Word الثنائي.
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

استخدم هذا المثال عندما يجب تصدير مستند PDF كملف DOCX. DOCX هو التنسيق المفضل لمعظم عمليات سير عمل معالجة النصوص الجديدة لأنه مدعوم على نطاق واسع وأسهل في التحرير.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) وقم بتعيين التنسيق على `DocX`.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم تصدير محتوى PDF كمستند Office Open XML Word.
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

## تحويل PDF إلى DOCX مع التعرف على التدفق المحسن

استخدم هذا المثال عندما يفضل تصدير Word المحتوى المتدفق القابل للتحرير بدلاً من التخطيط المرئي الثابت.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) للإخراج `DocX`.
1. قم بتمكين `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` بحيث يستخدم المحول التعرف المحسن على التدفق أثناء إنشاء DOCX.
1. اتصل `document.save(outputFile.toString(), saveOptions)` واحفظ مخرجات DOCX المحولة.

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

## قم بتحويل PDF إلى DOCX مع فواصل الأسطر المحفوظة

استخدم هذا المثال عندما يجب الاحتفاظ بنهايات الأسطر من ملف PDF المصدر في مخرجات Word.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) للتصدير `DocX`.
1. قم بتمكين `setAddReturnToLineEnd(true)` بحيث يتم الاحتفاظ بفواصل الأسطر الصريحة أثناء التحويل.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` واحفظ ملف DOCX.

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

## تحويل PDF إلى DOCX مع التعرف على التعداد النقطي

استخدم هذا المثال عندما يجب التعرف على التعداد النقطي من ملف PDF المصدر وحفظه كبنيات قائمة في Word.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) للتصدير `DocX`.
1. قم بتمكين `setRecognizeBullets(true)` حتى يتم التعرف على محتوى PDF الذي يشبه القائمة كقوائم نقطية أثناء التحويل.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` واحفظ ملف DOCX.

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

## قم بتحويل PDF إلى DOCX بدقة صورة مخصصة

استخدم هذا المثال عندما يجب التحكم في دقة الصورة داخل DOCX الذي تم إنشاؤه أثناء التحويل.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) للتصدير `DocX`.
1. قم بتعيين `setImageResolutionX(300)` و`setImageResolutionY(300)` بحيث يتم إنشاء المحتوى النقطي بالدقة المطلوبة.
1. اتصل `document.save(outputFile.toString(), saveOptions)` واحفظ مخرجات DOCX.

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

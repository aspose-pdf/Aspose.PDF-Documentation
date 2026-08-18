---
title: فئة الطوابع
linktitle: فئة الطوابع
type: docs
weight: 150
url: /java/stamp-class/
description: تعرف على كيفية العمل مع فئة Stamp في Java لإضافة صورة وPDF وطوابع نصية إلى مستندات PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف الصور وPDF والطوابع النصية إلى مستندات PDF في Java
Abstract: يشرح هذا القسم كيفية استخدام فئة Stamp مع PdfFileStamp في Aspose.PDF لـ Java لإضافة محتوى ختم قابل لإعادة الاستخدام إلى مستندات PDF. تغطي أمثلة Java الحالية طوابع الصور، وطوابع صفحات PDF، وطوابع النص مع حالة نصية مخصصة، وطوابع خاصة بالصفحة، وطوابع صور الخلفية مع إعدادات العتامة والحجم والتدوير.
---
توضح فئة Java `StampExamples` سير العمل الرئيسي لبناء الطوابع المتاحة من خلال واجهة برمجة التطبيقات Facades.

## أضف ختم الصورة

استخدم سير العمل هذا عندما يجب وضع ملف صورة على ملف PDF كختم.

### خطوات

1. قم بإنشاء مثيل `PdfFileStamp` واربط ملف PDF المصدر.
2. قم بإنشاء كائن `Stamp` واربطه بملف الصورة.
3. قم بتعيين معرف الختم وأصل الموضع.
4. أضف الختم إلى المستند.
5. احفظ النتيجة وأغلق كائن الواجهة.

### مثال جافا

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setStampId(1);
        stamp.setOrigin(36, 520);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## أضف صفحة PDF كختم

استخدم سير العمل هذا عندما يجب إعادة استخدام المحتوى من صفحة PDF أخرى كمحتوى ختم.

### خطوات

1. قم بإنشاء مثيل `PdfFileStamp` واربط ملف PDF المستهدف.
2. قم بإنشاء كائن `Stamp`.
3. ربط الختم بصفحة معينة من ملف PDF آخر.
4. قم بتعيين رقم الصفحة المستهدفة وأصل الموضع.
5. أضف الختم، واحفظ المخرجات، وأغلق كائن الواجهة.

### مثال جافا

```java
public static void addPdfPageAsStamp(Path inputFile, Path stampPdf, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindPdf(stampPdf.toString(), 1);
        stamp.setPageNumber(1);
        stamp.setOrigin(36, 250);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## أضف ختمًا نصيًا باستخدام TextState

استخدم سير العمل هذا عندما يجب أن يحتوي الختم على نص منمق بدلاً من صورة.

### خطوات

1. قم بإنشاء مثيل `PdfFileStamp` واربط ملف PDF المصدر.
2. قم بإنشاء كائن `Stamp`.
3. قم بربط شعار `FormattedText` و`TextState` المخصص بالختم.
4. تعيين أصل الختم والتناوب.
5. أضف الختم، واحفظ المخرجات، وأغلق كائن الواجهة.

### مثال جافا

```java
public static void addTextStampWithTextState(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindLogo(createTextLogo("Approved by signing workflow"));
        stamp.bindTextState(createTextState());
        stamp.setOrigin(36, 700);
        stamp.setRotation(15.0f);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## إضافة طابع إلى صفحات محددة

استخدم سير العمل هذا عندما يظهر الطابع على الصفحات المحددة فقط بدلاً من المستند بأكمله.

### خطوات

1. قم بإنشاء مثيل `PdfFileStamp` واربط ملف PDF المصدر.
2. قم بإنشاء كائن `Stamp` واربطه بملف صورة.
3. قم بتعيين قائمة الصفحات المستهدفة والأصل وحجم الصورة.
4. أضف الختم إلى المستند.
5. احفظ النتيجة وأغلق كائن الواجهة.

### مثال جافا

```java
public static void addStampToSpecificPages(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setPages(new int[] {1});
        stamp.setOrigin(400, 40);
        stamp.setImageSize(120, 60);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## إضافة ختم صورة الخلفية

استخدم سير العمل هذا عندما يظهر الختم خلف محتوى الصفحة مع عتامة وتدوير يمكن التحكم فيهما.

### خطوات

1. قم بإنشاء مثيل `PdfFileStamp` واربط ملف PDF المصدر.
2. قم بإنشاء كائن `Stamp` واربطه بملف الصورة.
3. ضع علامة على الختم كمحتوى خلفية.
4. تكوين العتامة والجودة والتدوير والحجم والأصل.
5. أضف الختم، واحفظ المخرجات، وأغلق كائن الواجهة.

### مثال جافا

```java
public static void addBackgroundImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setBackground(true);
        stamp.setOpacity(0.35f);
        stamp.setQuality(90);
        stamp.setRotation(45.0f);
        stamp.setImageSize(160, 80);
        stamp.setOrigin(200, 300);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

---
title: فئة Stamp
linktitle: فئة Stamp
type: docs
weight: 150
url: /ar/java/stamp-class/
description: تعرّف على كيفية العمل مع فئة Stamp في Java لإضافة طوابع صورة، PDF، وطوابع نصية إلى مستندات PDF.
lastmod: "2026-10-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف طوابع صورة، PDF، وطوابع نصية إلى مستندات PDF في Java
Abstract: يشرح هذا القسم كيفية استخدام فئة Stamp مع PdfFileStamp في Aspose.PDF for Java لإضافة محتوى طوابع قابل لإعادة الاستخدام إلى مستندات PDF. تغطي أمثلة Java الحالية طوابع الصورة، وطوابع صفحات PDF، وطوابع النص مع TextState مخصص، وطوابع خاصة بالصفحات، وطوابع صورة الخلفية مع إعدادات الشفافية، والحجم، والدوران.
---
الجافا `StampExamples` الفئة توضح سير عمل بناء الطوابع الرئيسي المتاح عبر Facades API.

## إضافة طابع صورة

استخدم هذا سير العمل عندما يجب وضع ملف صورة على ملف PDF كطابع.

### الخطوات

1. إنشاء `PdfFileStamp` إنشاء نسخة وربط ملف PDF المصدر.
2. إنشاء `Stamp` الكائن وربطه بملف الصورة.
3. عيّن معرف الختم ونقطة أصل الموضع.
4. أضف الختم إلى المستند.
5. احفظ النتيجة وأغلق كائن الواجهة.

### مثال Java

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

## إضافة صفحة PDF كختم

استخدم سير العمل هذا عندما يجب إعادة استخدام المحتوى من صفحة PDF أخرى كمحتوى طابع.

### الخطوات

1. إنشاء `PdfFileStamp` إنشاء نسخة وربط ملف PDF الهدف.
2. إنشاء `Stamp` كائن.
3. اربط الطابع بصفحة محددة من ملف PDF آخر.
4. قم بتعيين رقم الصفحة المستهدفة والنقطة الأصلية للمكان.
5. أضف الختم، احفظ الإخراج، وأغلق كائن الواجهة.

### مثال Java

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

## أضف ختم نصي باستخدام TextState

استخدم هذا سير العمل عندما يجب أن يحتوي الختم على نص منسق بدلاً من صورة.

### الخطوات

1. إنشاء `PdfFileStamp` إنشاء نسخة وربط ملف PDF المصدر.
2. إنشاء `Stamp` كائن.
3. ربط `FormattedText` شعار ومخصص `TextState` إلى الختم.
4. تعيين أصل الطابع والدوران.
5. أضف الختم، احفظ الإخراج، وأغلق كائن الواجهة.

### مثال Java

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

## أضف ختمًا إلى صفحات محددة

استخدم سير العمل هذا عندما يجب أن يظهر الطبع فقط على الصفحات المحددة بدلاً من المستند كله.

### الخطوات

1. إنشاء `PdfFileStamp` إنشاء نسخة وربط ملف PDF المصدر.
2. إنشاء `Stamp` كائن وربطه بملف صورة.
3. حدد قائمة الصفحات المستهدفة، الأصل، وحجم الصورة.
4. أضف الختم إلى المستند.
5. احفظ النتيجة وأغلق كائن الواجهة.

### مثال Java

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

## إضافة ختم صورة خلفية

استخدم سير العمل هذا عندما يجب أن يظهر الختم خلف محتوى الصفحة مع شفافية مدارة وتدوير.

### الخطوات

1. إنشاء `PdfFileStamp` إنشاء نسخة وربط ملف PDF المصدر.
2. إنشاء `Stamp` الكائن وربطه بملف الصورة.
3. ضع علامة على الختم كمحتوى خلفية.
4. قم بتكوين الشفافية والجودة والتدوير والحجم والنقطة الأصلية.
5. أضف الختم، احفظ الإخراج، وأغلق كائن الواجهة.

### مثال Java

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

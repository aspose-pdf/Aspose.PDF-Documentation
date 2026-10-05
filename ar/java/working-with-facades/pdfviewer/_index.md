---
title: فئة PdfViewer
linktitle: فئة PdfViewer
type: docs
weight: 135
url: /ar/java/pdfviewer-class/
description: تعلم كيفية استخدام الواجهة PdfViewer في Java لفك تشفير صفحات PDF وفحص إعدادات العارض المتعلقة بها.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فك تشفير صفحات PDF وفحص بيانات العارض في Java باستخدام PdfViewer
Abstract: يشرح هذا القسم كيفية استخدام الواجهة PdfViewer في Aspose.PDF for Java لتشفير الصفحات ومهام فحص العارض المتعلق بها. تغطي أمثلة Java الحالية تحويل جميع الصفحات إلى صور، وفك تشفير صفحة محددة، وفحص عدد الصفحات، ونوع الإحداثيات، والدقة، وإعدادات العارض المرتبطة.
---
الجافا الفئة `PdfViewerExamples` توضح سير عمل العارض الرئيسي المتاح عبر Facades API.

## فك تشفير جميع صفحات PDF

استخدم هذا سير العمل عندما يجب عرض كل صفحة من PDF المصدر كصورة.

### الخطوات

1. أنشئ واضبط مثيلًا من `PdfViewer`.
2. اربط ملف PDF المصدر بـ `bindPdf`.
3. استدعِ `decodeAllPages()` لعرض المستند في `BufferedImage` مصفوفة.
4. احفظ كل صفحة مُفكّكة في ملف صورة إخراج.
5. أغلق ملف PDF المرتبط.

### مثال Java

```java
public static void decodeAllPages(Path inputFile, Path outputDir) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        BufferedImage[] pages = viewer.decodeAllPages();
        for (int index = 0; index < pages.length; index++) {
            ImageIO.write(pages[index], "png", outputDir.resolve("decode_all_pages_" + (index + 1) + ".png").toFile());
        }
    } finally {
        viewer.closePdfFile();
    }
}
```

## فك تشفير صفحة PDF محددة

استخدم سير العمل هذا عندما تحتاج صفحة واحدة فقط إلى تحويلها إلى صورة.

### الخطوات

1. أنشئ واضبط مثيلًا من `PdfViewer`.
2. اربط ملف PDF المصدر.
3. استدعِ `decodePage()` للصفحة التي تريد عرضها.
4. احفظ الصفحة المفكوكة في ملف صورة إخراج.
5. أغلق العارض.

### مثال Java

```java
public static void decodeSpecificPage(Path inputFile, Path outputFile) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        ImageIO.write(viewer.decodePage(1), "png", outputFile.toFile());
    } finally {
        viewer.close();
    }
}
```

## فحص بيانات تعريف PDF

استخدم هذا سير العمل عندما تحتاج إلى معلومات مستند متعلقة بالمشاهد قبل الرسم أو الطباعة.

### الخطوات

1. أنشئ واضبط مثيلًا من `PdfViewer`.
2. اربط ملف PDF المصدر.
3. اقرأ عدد الصفحات، نوع الإحداثيات، ودقة العرض.
4. استخدم أو اطبع القيم المسترجعة.
5. أغلق ملف PDF المرتبط.

### مثال Java

```java
public static void inspectPdfMetadata(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Coordinate type: " + viewer.getCoordinateType());
        System.out.println("Resolution: " + viewer.getResolution());
    } finally {
        viewer.closePdfFile();
    }
}
```

## فحص إعدادات العارض المرتبط

استخدم سير العمل هذا عندما تحتاج إلى تأكيد أو تعديل سلوك العارض بعد ربط ملف PDF.

### الخطوات

1. أنشئ واضبط مثيلًا من `PdfViewer`.
2. اربط ملف PDF المصدر.
3. حدّد خيارات العارض مثل إعادة التحجيم التلقائي، الدوران التلقائي، ورؤية نافذة حوار الطباعة.
4. اقرأ إعدادات العارض النشطة وعدد الصفحات.
5. أغلق العارض.

### مثال Java

```java
public static void inspectBoundViewerSettings(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        viewer.setAutoResize(true);
        viewer.setAutoRotate(true);
        viewer.setPrintPageDialog(false);
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Print as image: " + viewer.getPrintAsImage());
        System.out.println("Auto resize: " + viewer.getAutoResize());
        System.out.println("Auto rotate: " + viewer.getAutoRotate());
    } finally {
        viewer.close();
    }
}
```

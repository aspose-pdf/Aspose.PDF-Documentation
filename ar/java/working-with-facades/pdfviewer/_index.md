---
title: فئة عارض PDF
linktitle: فئة عارض PDF
type: docs
weight: 135
url: /java/pdfviewer-class/
description: تعرف على كيفية استخدام واجهة PdfViewer في Java لفك تشفير صفحات PDF وفحص الإعدادات المتعلقة بالعارض.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بفك تشفير صفحات PDF وفحص بيانات العارض في Java باستخدام PdfViewer
Abstract: يشرح هذا القسم كيفية استخدام واجهة PdfViewer في Aspose.PDF لـ Java لفك تشفير الصفحة ومهام الفحص المتعلقة بالعارض. تغطي أمثلة Java الحالية عرض جميع الصفحات على صور، وفك تشفير صفحة معينة، وفحص عدد الصفحات، ونوع الإحداثيات، والدقة، وإعدادات العارض المرتبطة.
---
توضح فئة Java `PdfViewerExamples` سير عمل العارض الرئيسي المتاح من خلال واجهة برمجة التطبيقات للواجهات.

## فك تشفير كافة صفحات PDF

استخدم سير العمل هذا عندما يجب عرض كل صفحة من ملف PDF المصدر كصورة.

### خطوات

1. قم بإنشاء وتكوين مثيل `PdfViewer`.
2. قم بربط ملف PDF المصدر بـ `bindPdf`.
3. اتصل بـ `decodeAllPages()` لعرض المستند في مصفوفة `BufferedImage`.
4. احفظ كل صفحة تم فك تشفيرها في ملف صورة الإخراج.
5. أغلق ملف PDF المقيد.

### مثال جافا

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

استخدم سير العمل هذا عندما يلزم عرض صفحة واحدة فقط على الصورة.

### خطوات

1. قم بإنشاء وتكوين مثيل `PdfViewer`.
2. ربط ملف PDF المصدر.
3. اتصل بـ `decodePage()` للصفحة التي تريد عرضها.
4. احفظ الصفحة التي تم فك ترميزها في ملف صورة الإخراج.
5. أغلق العارض.

### مثال جافا

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

## فحص البيانات التعريفية لملف PDF

استخدم سير العمل هذا عندما تحتاج إلى معلومات وثيقة متعلقة بالعارض قبل العرض أو الطباعة.

### خطوات

1. قم بإنشاء وتكوين مثيل `PdfViewer`.
2. ربط ملف PDF المصدر.
3. اقرأ عدد الصفحات ونوع الإحداثيات ودقة العرض.
4. استخدم أو اطبع القيم المستردة.
5. أغلق ملف PDF المقيد.

### مثال جافا

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

## فحص إعدادات العارض المنضمة

استخدم سير العمل هذا عندما تحتاج إلى تأكيد أو ضبط سلوك العارض بعد ربط ملف PDF.

### خطوات

1. قم بإنشاء وتكوين مثيل `PdfViewer`.
2. ربط ملف PDF المصدر.
3. قم بتعيين خيارات العارض مثل تغيير الحجم التلقائي، والتدوير التلقائي، ورؤية مربع حوار الطباعة.
4. اقرأ إعدادات العارض النشط وعدد الصفحات.
5. أغلق العارض.

### مثال جافا

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

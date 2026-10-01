---
title: إنشاء ملفات PDF في Java
linktitle: إنشاء مستند PDF
type: docs
weight: 10
url: /ar/java/create-pdf-document/
description: تعلم كيفية إنشاء ملفات PDF وبناء ملفات PDF قابلة للبحث في Java باستخدام Aspose.PDF.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء ملفات PDF ووثائق PDF قابلة للبحث باستخدام Java
Abstract: توضح هذه المقالة كيفية إنشاء مستندات PDF باستخدام Aspose.PDF for Java. وتغطي إنشاء PDF جديد من الصفر وتحويل مستند مبني على صورة إلى PDF قابل للبحث عن طريق تزويد ناتج HOCR من محرك OCR خارجي.
---
Aspose.PDF for Java يدعم كل من إنشاء المستندات البسيطة وتدفقات عمل PDF القابلة للبحث المدعومة بتقنية OCR.

## إنشاء مستند PDF جديد

استخدم هذا النهج عندما تحتاج إلى إنشاء ملف PDF بسيط من الصفر.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) وإضافة ذلك إلى الصفحة.
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## إنشاء PDF قابل للبحث

ال `createSearchablePdf` أمثلة الاستخدام `Document.convert(...)` مع `CallBackGetHocr` التنفيذ. تقوم الدالة الراجعة بكتابة صورة المصدر إلى ملف مؤقت، وتستدعي Tesseract مع `hocr` الخيار، يقرأ ترميز HOCR الذي تم إنشاؤه، ويعيده إلى Aspose.PDF.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء `CallBackGetHocr` استدعاء وتحويل المستند المصدر إلى محتوى PDF قابل للبحث.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createSearchablePdf(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.getParent().resolve("ocr-temp");
    CallBackGetHocr cbgh = new CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            // save the image, run Tesseract with "hocr", and return the HOCR text
            return fileContents.toString();
        }
    };
    try (Document document = new Document(inputFile.toString())) {
        document.convert(cbgh);
        document.save(outputFile.toString());
    }
}
```

## احصل على إعدادات نافذة المستند

استخدم هذا المثال لتفقد تفضيلات المشاهد الحالية المخزنة في مستند PDF موجود.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قراءة خصائص النافذة والعرض المطلوبة من المستند.
1. قم بإخراج الإعدادات الحالية للفحص أو التصحيح.

```java
public static void getDocumentWindow(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("CenterWindow: " + document.isCenterWindow());
        System.out.println("Direction: " + document.getDirection());
        System.out.println("DisplayDocTitle: " + document.isDisplayDocTitle());
        System.out.println("FitWindow: " + document.isFitWindow());
        System.out.println("HideMenuBar: " + document.isHideMenubar());
        System.out.println("HideToolBar: " + document.isHideToolBar());
        System.out.println("HideWindowUI: " + document.isHideWindowUI());
        System.out.println("NonFullScreenPageMode: " + document.getNonFullScreenPageMode());
        System.out.println("PageLayout: " + document.getPageLayout());
        System.out.println("PageMode: " + document.getPageMode());
    }
}
```

## تعيين تفضيلات نافذة المستند

يحدّث هذا المثال كيفية عرض ملف PDF عندما يتم فتحه في عارض متوافق.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتعيين تفضيلات النافذة والتخطيط ووضع الصفحة المطلوبة.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void setDocumentWindow(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setCenterWindow(true);
        document.setDirection(Direction.R2L);
        document.setDisplayDocTitle(true);
        document.setFitWindow(true);
        document.setHideMenubar(true);
        document.setHideToolBar(true);
        document.setHideWindowUI(true);
        document.setNonFullScreenPageMode(PageMode.UseOC);
        document.setPageLayout(PageLayout.TwoColumnLeft);
        document.setPageMode(PageMode.UseThumbs);
        document.save(outputFile.toString());
    }
}
```

## تضمين الخطوط في ملف PDF موجود

استخدم هذا الأسلوب عندما يجب أن يحتوي المستند على الخطوط المطلوبة لضمان عرض أكثر موثوقية على الأنظمة الأخرى.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتمكين تضمين الخطوط القياسية وتكرار الخطوط المستخدمة في كل منها [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. علّم أي غير مضمّن [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) كائنات للتضمين.
1. احفظ المستند المحدث.

```java
public static void embeddedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setEmbedStandardFonts(true);
        for (Page page : document.getPages()) {
            for (Font pageFont : page.getResources().getFonts()) {
                if (!pageFont.isEmbedded()) {
                    pageFont.setEmbedded(true);
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## تضمين الخطوط عند إنشاء ملف PDF جديد

هذا المثال ينشئ ملف PDF جديد ويُعيّن خطًا مضمّنًا إلى محتوى النص منذ البداية.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. إنشاء المطلوب [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/), و [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. حل الهدف [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) من المستودع وعلمها بأنها مدمجة.
1. أضف محتوى النص إلى الصفحة واحفظ مستند الإخراج.

```java
public static void embeddedFontsInNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            TextFragment fragment = new TextFragment("");
            TextSegment segment = new TextSegment(" This is a sample text using Custom font.");
            TextState textState = new TextState();
            Font font = FontRepository.findFont("Arial");
            font.setEmbedded(true);
            textState.setFont(font);
            segment.setTextState(textState);
            fragment.getSegments().add(segment);
            page.getParagraphs().add(fragment);
        }
        document.save(outputFile.toString());
    }
}
```

## ضبط خط افتراضي لإخراج PDF

استخدم هذا النمط عندما يجب أن يعود المستند المحفوظ إلى خط محدد أثناء توليد الإخراج.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) وحدد اسم الخط الافتراضي.
1. احفظ المستند باستخدام خيارات الحفظ المُكوَّنة.

```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## احصل على جميع الخطوط المستخدمة في ملف PDF

يسرد هذا المثال كل الخطوط المكتشفة في المستند حتى تتمكن من تدقيق استخدام الخطوط قبل التصدير أو تحديث الملف.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. عد الـ Fonts التي تُرجعها أدوات Font للمستند.
1. إخراج اسم كل ما تم اكتشافه [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## تحسين تضمين الخطوط عن طريق تقسيم الخطوط إلى مجموعات فرعية

استخدم هذا النهج عندما تريد تقليل حجم تحميل الخط مع الحفاظ على توافق بيانات الخط المضمنة مع استخدام المستند.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. شغّل تقليل الخط من خلال أدوات خطوط المستند المطلوبة [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) قيم.
1. احفظ المستند المحسّن.

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## ضبط معامل تكبير فتح المستند

يقوم هذا المثال بتكوين مستوى التكبير الأولي الذي يجب تطبيقه عند فتح ملف PDF.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) مع [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. عيّن الإجراء كإجراء فتح المستند واحفظ النتيجة.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## احصل على معامل تقريب فتح المستند

استخدم هذا المثال لفحص ما إذا كان ملف PDF يحدد مسبقًا مستوى تقريب صريح لإجراء الفتح.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تحقق مما إذا كان إجراء الفتح هو [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) مع [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. أخرج قيمة التكبير المُكوَّنة أو أبلغ بأنه لا يوجد تكبير مُحدد.

```java
public static void getZoomFactor(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getOpenAction() instanceof GoToAction action
                && action.getDestination() instanceof XYZExplicitDestination destination) {
            System.out.println("Zoom: " + destination.getZoom());
        } else {
            System.out.println("Zoom: not set");
        }
    }
}
```

---
title: تنسيق مستندات PDF في Java
linktitle: تنسيق مستند PDF
type: docs
weight: 11
url: /ar/java/formatting-pdf-document/
description: تعلم كيفية تنسيق مستندات PDF، تضمين Font، التحكم في إعدادات عارض PDF، وضبط خيارات العرض في Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تنسيق نافذة المستند، Font، وسلوك التكبير/التصغير في ملفات PDF باستخدام Java.
Abstract: توضح هذه المقالة كيفية تنسيق مستندات PDF باستخدام Aspose.PDF for Java. تغطي القراءة وتحديث إعدادات نافذة المستند، وتضمين الخطوط، وتعيين خط افتراضي، وسرد الخطوط، وتقليص الخطوط المضمنة، والتحكم في عامل التكبير الأولي.
---
يتضمن التنسيق في Aspose.PDF for Java سلوك عارض المستندات، وتضمين الخط، وإعدادات العرض.

## احصل على إعدادات نافذة المستند

استخدم هذا المثال لتفحص تفضيلات المشاهد الحالية المخزنة في مستند PDF موجود.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اقرأ خصائص النافذة والعرض المطلوبة من المستند.
1. اعرض الإعدادات الحالية للفحص أو التصحيح.

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

## ضبط تفضيلات نافذة المستند

يقوم هذا المثال بتحديث طريقة عرض ملف PDF عندما يتم فتحه في عارض متوافق.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. عيّن التفضيلات المطلوبة للنافذة والتخطيط ووضع الصفحة.
1. احفظ ملف PDF المحدّث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

استخدم هذا النهج عندما يجب أن يحمل المستند الخطوط المطلوبة لضمان عرض أكثر موثوقية على الأنظمة الأخرى.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. فعّل تضمين الخطوط القياسية وتكرار عبر الخطوط المستخدمة في كلٍ [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. علِّم أي غير مضمّن الكائنات [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) للتضمين.
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

هذا المثال ينشئ ملف PDF جديد ويُعيّن خطًا مدمجًا لمحتوى النص من البداية.

1. أنشئ مستند PDF جديدًا باستخدام [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. أنشئ المطلوب [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/)، و [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. استرجع الخط المستهدف [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) من المستودع وضع علامة عليه لتضمينه.
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

## تعيين Font افتراضي لإخراج PDF

استخدم هذا النمط عندما ينبغي أن يعود المستند المحفوظ إلى خطٍ محدد أثناء توليد الإخراج.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) وحدد اسم الخط الافتراضي.
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

## احصل على جميع الخطوط المستخدمة في PDF

يعرض هذا المثال كل الخطوط المكتشفة في المستند حتى تتمكن من تدقيق استخدام الخطوط قبل تصدير الملف أو تحديثه.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. عدّ الخطوط التي تُرجعها أدوات خطوط المستند.
1. اعرض اسم كل ما تم اكتشافه [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## تحسين تضمين الخطوط عن طريق تقليص الخطوط

استخدم هذا النهج عندما تريد تقليل حجم الخط المضمن مع الحفاظ على توافق بيانات الخط المدمج مع استخدام المستند.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. شغّل تقليل الخط من خلال أدوات خطوط المستند المطلوبة [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) القيم.
1. احفظ المستند المُحسّن.

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## تعيين عامل تكبير فتح المستند

هذا المثال يضبط مستوى التكبير الأولي الذي يجب تطبيقه عند فتح ملف PDF.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) مع [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
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

## احصل على معامل تكبير المستند عند الفتح

استخدم هذا المثال للتحقق مما إذا كان ملف PDF يحدد بالفعل مستوى تكبير صريح لإجراء الفتح الخاص به.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تحقّق مما إذا كان إجراء الفتح هو [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) مع [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. أخرج قيمة التكبير المُكوَّنة أو أبلغ بأنه لا يوجد تكبير محدد.

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

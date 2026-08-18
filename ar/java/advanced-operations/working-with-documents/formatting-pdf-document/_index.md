---
title: تنسيق مستندات PDF في جافا
linktitle: تنسيق وثيقة PDF
type: docs
weight: 11
url: /java/formatting-pdf-document/
description: تعرف على كيفية تنسيق مستندات PDF وتضمين الخطوط والتحكم في إعدادات العارض وضبط خيارات العرض في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتنسيق نافذة المستند والخطوط وسلوك التكبير/التصغير في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية تنسيق مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي قراءة وتحديث إعدادات نافذة المستند، وتضمين الخطوط، وتعيين خط افتراضي، وإدراج الخطوط، وتعيين الخطوط المضمنة فرعيًا، والتحكم في عامل التكبير/التصغير الأولي.
---
يتضمن التنسيق في Aspose.PDF لـ Java سلوك المشاهد وتضمين الخط وإعدادات العرض.

## الحصول على إعدادات نافذة المستند

استخدم هذا المثال لفحص تفضيلات العارض الحالية المخزنة في مستند PDF موجود.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اقرأ النافذة المطلوبة واعرض الخصائص من المستند.
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

## ضبط تفضيلات نافذة الوثيقة

يقوم هذا المثال بتحديث كيفية عرض ملف PDF عند فتحه في عارض متوافق.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتعيين تفضيلات النافذة والتخطيط ووضع الصفحة المطلوبة.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

استخدم هذا الأسلوب عندما يجب أن يحمل المستند الخطوط المطلوبة للحصول على عرض أكثر موثوقية على الأنظمة الأخرى.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتمكين تضمين الخط القياسي وكرر الخطوط المستخدمة بواسطة كل [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. قم بوضع علامة على أي كائنات [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) غير مضمنة للتضمين.
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

يقوم هذا المثال بإنشاء ملف PDF جديد وتعيين خط مضمن لمحتوى النص من البداية.

1. أنشئ [مستند] PDF جديدًا (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. قم بإنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) و[TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/) و[TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/) المطلوبة.
1. قم بحل الهدف [الخط](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) من المستودع ووضع علامة عليه كمضمن.
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

## قم بتعيين الخط الافتراضي لإخراج PDF

استخدم هذا النمط عندما يجب أن يعود المستند المحفوظ إلى خط معين أثناء إنشاء الإخراج.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) وقم بتعيين اسم الخط الافتراضي.
1. احفظ المستند باستخدام خيارات الحفظ التي تم تكوينها.

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

يسرد هذا المثال كل خط تم اكتشافه في المستند حتى تتمكن من تدقيق استخدام الخط قبل تصدير الملف أو تحديثه.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تعداد الخطوط التي يتم إرجاعها بواسطة الأدوات المساعدة لخطوط المستند.
1. قم بإخراج اسم كل [خط] تم اكتشافه (https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## تحسين تضمين الخط عن طريق تعيين الخطوط الفرعية

استخدم هذا الأسلوب عندما تريد تقليل حمولة الخط مع الحفاظ على توافق بيانات الخط المضمنة مع استخدام المستند.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتشغيل الإعداد الفرعي للخط من خلال الأدوات المساعدة لخطوط المستند باستخدام قيم [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) المطلوبة.
1. احفظ المستند الأمثل.

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## اضبط عامل تكبير/تصغير المستند المفتوح

يقوم هذا المثال بتكوين مستوى التكبير/التصغير الأولي الذي يجب تطبيقه عند فتح ملف PDF.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) باستخدام [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. قم بتعيين الإجراء كإجراء فتح المستند واحفظ النتيجة.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## احصل على عامل التكبير/التصغير المفتوح للمستند

استخدم هذا المثال لفحص ما إذا كان ملف PDF قد قام بالفعل بتعريف مستوى تكبير واضح للإجراء المفتوح الخاص به.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تحقق مما إذا كان الإجراء المفتوح هو [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) مع [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. قم بإخراج قيمة التكبير/التصغير التي تم تكوينها أو الإبلاغ عن عدم تعيين أي تكبير/تصغير.

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

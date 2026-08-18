---
title: التعامل مع مستندات PDF في جافا
linktitle: التعامل مع وثيقة PDF
type: docs
weight: 20
url: /java/manipulate-pdf-document/
description: تعرف على كيفية التحقق من صحة مستندات PDF وتنظيمها وتعديلها في Java، بما في ذلك إدارة جدول المحتويات (TOC) والتحقق من PDF/A.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: التحقق من صحة مستندات PDF وإعادة هيكلتها وتسويتها باستخدام Java
Abstract: تشرح هذه المقالة كيفية التعامل مع مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي التحقق من صحة التوافق مع PDF/A، وإضافة جدول محتويات وتخصيصه، وإخفاء أو تخصيص أرقام صفحات جدول المحتويات، وتعيين نص انتهاء الصلاحية، وتسوية حقول النماذج التفاعلية.
---
يتضمن Aspose.PDF for Java عمليات بنية المستند التي تتجاوز مجرد تحرير الصفحة البسيطة.

## التحقق من صحة التوافق مع PDF/A-1a

استخدم هذا المثال عندما تحتاج إلى التحقق مما إذا كان المستند يتوافق مع معيار الأرشفة PDF/A-1a.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإجراء التحقق من الصحة مقابل الهدف [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) المطلوب.
1. احفظ تقرير التحقق من الصحة في مسار الإخراج المحدد.

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## التحقق من صحة التوافق مع PDF/A-1b

يتحقق هذا الاختلاف من صحة نفس المستند المصدر مقابل مستوى التوافق PDF/A-1b.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم باستدعاء طريقة التحقق من الصحة باستخدام قيمة [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) لـ PDF/A-1b.
1. اكتب نتيجة التحقق من الصحة إلى ملف تقرير الإخراج.

```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## إضافة جدول محتويات

استخدم هذا الأسلوب عندما يجب أن يتضمن المستند صفحة جدول المحتويات التي تم إنشاؤها مع روابط لصفحات المحتوى.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أدخل جدول محتويات [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) جديدًا وقم بتكوين [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. قم بإنشاء إدخالات [العناوين](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) التي تشير إلى الصفحات الوجهة.
1. احفظ المستند المحدث.

```java
public static void addTableOfContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        String[] titles = {"First page", "Second page"};
        for (int index = 0; index < titles.length && index + 2 <= document.getPages().size(); index++) {
            Heading heading = new Heading(1);
            TextSegment segment = new TextSegment(titles[index]);
            heading.setTocPage(tocPage);
            heading.getSegments().add(segment);
            Page destinationPage = document.getPages().get_Item(index + 2);
            heading.setDestinationPage(destinationPage);
            heading.setTop(destinationPage.getRect().getHeight());
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## تخصيص مستويات جدول المحتويات والتنسيق

يوضح هذا المثال كيفية تعيين إعدادات مرئية مختلفة لمستويات جدول المحتويات المتعددة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف جدول محتويات [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وقم بتكوين صفيف تنسيق [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. قم بإنشاء نموذج لإدخالات [العنوان](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) بمستويات مختلفة.
1. احفظ المستند باستخدام جدول المحتويات المنسق.

```java
public static void setTocLevels(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().add();
        TocInfo tocInfo = new TocInfo();
        tocInfo.setLineDash(TabLeaderType.Solid);
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(30);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        tocInfo.setFormatArrayLength(4);
        tocInfo.getFormatArray()[0].getMargin().setLeft(0);
        tocInfo.getFormatArray()[0].getMargin().setRight(30);
        tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
        tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        tocInfo.getFormatArray()[1].getMargin().setLeft(10);
        tocInfo.getFormatArray()[1].getMargin().setRight(30);
        tocInfo.getFormatArray()[1].setLineDash(3);
        tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
        tocInfo.getFormatArray()[2].getMargin().setLeft(20);
        tocInfo.getFormatArray()[2].getMargin().setRight(30);
        tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
        tocInfo.getFormatArray()[3].getMargin().setLeft(30);
        tocInfo.getFormatArray()[3].getMargin().setRight(30);
        tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

        try (Page page = document.getPages().add()) {
            for (int level = 1; level < 5; level++) {
                Heading heading = new Heading(level);
                heading.setAutoSequence(true);
                heading.setTocPage(tocPage);
                heading.getTextState().setFont(FontRepository.findFont("Arial"));
                heading.getSegments().add(new TextSegment("Sample Heading" + level));
                heading.setInList(true);
                page.getParagraphs().add(heading);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## إخفاء أرقام الصفحات في جدول المحتويات

استخدم هذا المثال عندما يُظهر جدول المحتويات عناوين الإدخال بدون أرقام الصفحات.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف جدول المحتويات [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وقم بتعطيل أرقام الصفحات في [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. أنشئ إدخال [العنوان](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) المطلوب وأضفه إلى صفحة المحتوى.
1. احفظ المستند المحدث.

```java
public static void hidePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page;
        Heading heading;
        try (Page tocPage = document.getPages().add()) {
            TocInfo tocInfo = new TocInfo();
            TextFragment title = new TextFragment("Table Of Contents");
            title.getTextState().setFontSize(20);
            title.getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.setTitle(title);
            tocInfo.setShowPageNumbers(false);
            tocPage.setTocInfo(tocInfo);

            tocInfo.setFormatArrayLength(4);
            tocInfo.getFormatArray()[0].getMargin().setRight(0);
            tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
            tocInfo.getFormatArray()[1].getMargin().setLeft(30);
            tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
            tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
            tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

            page = document.getPages().add();
            heading = new Heading(1);
            heading.setTocPage(tocPage);
        }
        heading.setAutoSequence(true);
        heading.setInList(true);
        heading.getSegments().add(new TextSegment("this is heading of level 1"));
        page.getParagraphs().add(heading);

        document.save(outputFile.toString());
    }
}
```

## تخصيص بادئات رقم صفحة جدول المحتويات

يضيف هذا المثال بادئة مخصصة إلى أرقام الصفحات المعروضة في جدول المحتويات الذي تم إنشاؤه.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أدخل جدول المحتويات [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وقم بتعيين بادئة رقم الصفحة المطلوبة في [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. قم بإنشاء إدخالات [العنوان](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) التي تشير إلى كل صفحة.
1. احفظ المستند المحدث.

```java
public static void customizePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocInfo.setPageNumbersPrefix("P");
        tocPage.setTocInfo(tocInfo);

        for (int index = 1; index <= document.getPages().size(); index++) {
            Page page = document.getPages().get_Item(index);
            Heading heading = new Heading(1);
            heading.setTocPage(tocPage);
            heading.setDestinationPage(page);
            heading.setTop(page.getRect().getHeight());
            heading.getSegments().add(new TextSegment("Page " + index));
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## أضف نصًا لانتهاء صلاحية PDF

استخدم هذا الأسلوب عندما يجب على المستند تشغيل JavaScript عند فتحه وإظهار تحذير انتهاء الصلاحية بعد تاريخ محدد.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف أي محتوى مطلوب.
1. قم بإنشاء [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) باستخدام منطق انتهاء الصلاحية.
1. قم بتعيين البرنامج النصي كإجراء فتح المستند وحفظ ملف الإخراج.

```java
public static void setPdfExpiryDate(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(new TextFragment("Hello World..."));
        }
        JavascriptAction script = new JavascriptAction(
                "var year=2017;"
                        + "var month=5;"
                        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
                        + "expiry = new Date(year, month);"
                        + "if (today.getTime() > expiry.getTime())"
                        + "app.alert('The file is expired. You need a new one.');");
        document.setOpenAction(script);
        document.save(outputFile.toString());
    }
}
```

## قم بتسوية نموذج PDF قابل للتعبئة

يقوم هذا المثال بتحويل حقول النموذج التفاعلية إلى محتوى صفحة ثابت بحيث لا يعد المستند الناتج قابلاً للتحرير كنموذج.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تحقق مما إذا كانت الوثيقة تحتوي على عناصر واجهة مستخدم النموذج.
1. قم بتسوية كل [حقل](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) الذي يمثله [تعليق القطعة](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. احفظ المستند الذي تم تسويته.

```java
public static void flattenFillablePdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

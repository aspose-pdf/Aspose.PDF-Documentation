---
title: معالجة ملفات PDF في Java
linktitle: معالجة مستند PDF
type: docs
weight: 20
url: /ar/java/manipulate-pdf-document/
description: تعرّف على كيفية التحقق من صحة وثائق PDF وتنسيقها وتعديلها في Java، بما في ذلك إدارة TOC وفحوصات PDF/A.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحقق من صحة وثائق PDF وأعد هيكلتها وتسطيحها باستخدام Java
Abstract: تشرح هذه المقالة كيفية معالجة مستندات PDF باستخدام Aspose.PDF for Java. تغطي التحقق من توافق PDF/A، إضافة وتخصيص جدول المحتويات، إخفاء أو تخصيص أرقام صفحات TOC، تعيين نص انتهاء الصلاحية، وتسطيح حقول النموذج التفاعلية.
---
يتضمن Aspose.PDF for Java عمليات هيكل الوثيقة التي تتجاوز تحرير الصفحات البسيط.

## تحقق من امتثال PDF/A-1a

استخدم هذا المثال عندما تحتاج إلى التحقق مما إذا كان المستند يلتزم بمعيار الأرشفة PDF/A-1a.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تشغيل التحقق من الصحة مقابل المطلوب [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) الهدف.
1. احفظ تقرير التحقق إلى مسار الإخراج المحدد.

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## تحقق من امتثال PDF/A-1b

يقوم هذا الاختلاف بالتحقق من صحة نفس مستند المصدر مقابل مستوى التوافق PDF/A-1b.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. استدع طريقة التحقق مع [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) قيمة لـ PDF/A-1b.
1. اكتب نتيجة التحقق إلى ملف تقرير الإخراج.

```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## إضافة جدول محتويات

استخدم هذا النهج عندما يجب أن يتضمن المستند صفحة TOC مُولَّدة مع روابط إلى صفحات المحتوى.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إدراج TOC جديد [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وتهيئتها [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. إنشاء [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) الإدخالات التي تشير إلى صفحات الوجهة.
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

## تخصيص مستويات TOC والتنسيق

يوضح هذا المثال كيفية تعيين إعدادات بصرية مختلفة لمستويات جدول المحتويات المتعددة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف TOC إلى [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) و تكوين [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) تنسيق المصفوفة.
1. إنشاء نموذج [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) إدخالات بمستويات مختلفة.
1. احفظ المستند مع TOC المنسق.

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

## إخفاء أرقام الصفحات في TOC

استخدم هذا المثال عندما يجب أن يُظهر جدول المحتويات عناوين الإدخالات دون أرقام الصفحات.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف TOC إلى [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وإلغاء أرقام الصفحات في [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. أنشئ المطلوب [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) إدخال وإضافتها إلى صفحة المحتوى.
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

## تخصيص بادئات أرقام صفحات TOC

يضيف هذا المثال بادئة مخصصة لأرقام الصفحات المعروضة في جدول المحتويات المُنشأ.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أدرج TOC في [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وحدد بادئة رقم الصفحة المطلوبة في [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. إنشاء [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) مدخلات تشير إلى كل صفحة.
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

## إضافة سكريبت انتهاء صلاحية PDF

استخدم هذا النهج عندما يجب على المستند تشغيل جافا سكريبت عند الفتح وإظهار تحذير انتهاء الصلاحية بعد تاريخ محدد.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف أي محتوى مطلوب.
1. إنشاء [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) مع منطق انتهاء الصلاحية.
1. عيّن البرنامج النصي كإجراء فتح المستند واحفظ ملف الإخراج.

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

## تسطيح نموذج PDF القابل للملء

يقوم هذا المثال بتحويل حقول النموذج التفاعلية إلى محتوى صفحة ثابت بحيث يصبح المستند الناتج غير قابل للتعديل كنموذج.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تحقق مما إذا كان المستند يحتوي على عناصر النموذج.
1. تسوية كل [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) ممثلة بـ [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. احفظ المستند المسطح.

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

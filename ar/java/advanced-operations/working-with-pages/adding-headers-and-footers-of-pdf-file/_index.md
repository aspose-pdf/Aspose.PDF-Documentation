---
title: إضافة رؤوس وتذييلات PDF في Java
linktitle: إضافة رأس وتذييل إلى PDF
type: docs
weight: 50
url: /ar/java/add-headers-and-footers-of-pdf-file/
description: تعرّف على كيفية إضافة رؤوس وتذييلات إلى ملفات PDF في Java باستخدام النصوص والصور والمحتوى المهيكل.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف رؤوس وتذييلات إلى ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة رؤوس وتذييلات إلى مستندات PDF باستخدام Aspose.PDF for Java. وتغطي النص، وترقيم الصفحات، وHTML، والصورة، والجدول، ومحتوى الرأس والتذييل المستند إلى LaTeX.
---
Aspose.PDF for Java يتيح لك تعيين الكائنات `HeaderFooter` إلى كل صفحة وملئها بأنواع محتوى مختلفة.

## إضافة رؤوس وتذييلات النص

استخدم هذا المثال عندما تحتاج إلى محتوى نصي بسيط في أعلى وأسفل كل صفحة.

1. أنشئ الكائنات [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) وأضف مقاطع نصية.
1. اضبط الهوامش للرأس والتذييل.
1. طبقها على كل صفحة من ملف PDF المصدر واحفظ النتيجة.

```java
public static void addHeaderAndFooterAsText(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Demo header"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Demo footer"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## إضافة رؤوس وتذييلات مع ترقيم الصفحات

استخدم هذا المثال عندما يجب أن يُظهر الرأس أو التذييل رقم الصفحة الحالية وإجمالي عدد الصفحات.

1. أنشئ الكائنات [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) ذات عناصر نائبة لترقيم الصفحات.
1. اضبط الهوامش لكلا الكائنين.
1. طبقها على كل صفحة واحفظ ملف PDF المحدث.

```java
public static void usingHeaderAndFooterForPageNumbering(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Page $p from $P"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Page $p / $P"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## إضافة رؤوس وتذييلات HTML

استخدم هذا المثال عندما ينبغي أن يتضمن محتوى الرأس والتذييل تنسيق HTML مضمن.

1. أنشئ الكائنات [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) وأضف [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) المحتوى.
1. اضبط الهوامش للموضع.
1. عيّن الرأس والتذييل لكل صفحة واحفظ المستند.

```java
public static void addHeaderAndFooterAsHtml(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new HtmlFragment("This is an HTML <strong>Header</strong>"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new HtmlFragment("Powered by <i>Aspose.PDF</i>"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## إضافة رؤوس وتذييلات الصور

استخدم هذا المثال عندما يجب أن يعرض الرأس والتذييل صورة في كل صفحة.

1. أنشئ الكائنات [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) وإضافتها إلى حاويات الرأس والتذييل.
1. اضبط الهوامش وعيّن الحاويات لكل صفحة.
1. احفظ ملف PDF المحدث.

```java
public static void addHeaderAndFooterAsImage(Path inputFile, Path imageFile, Path outputFile) {
    Image headerImage = new Image();
    headerImage.setFile(imageFile.toString());
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(headerImage);

    Image footerImage = new Image();
    footerImage.setFile(imageFile.toString());
    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(footerImage);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            MarginInfo margin = new MarginInfo();
            margin.setLeft(50);
            header.setMargin(margin);
            footer.setMargin(margin);
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## إضافة رؤوس وتذييلات مبنية على الجداول

استخدم هذا المثال عندما يجب أن يستخدم محتوى الرأس والتذييل تخطيط الجدول وتنسيق النص.

1. أنشئ أنماط النص المطلوبة وكائنات الجدول.
1. أضف الجداول إلى [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) حاويات.
1. طبّق الترويسة والتذييل على كل صفحة واحفظ المستند.

```java
public static void addHeaderAndFooterAsTable(Path inputFile, Path outputFile) {
    TextState textStateHeader = new TextState();
    textStateHeader.setFont(FontRepository.findFont("Arial"));
    textStateHeader.setFontSize(12);
    textStateHeader.setHorizontalAlignment(HorizontalAlignment.Center);

    TextState textStateFooter = new TextState();
    textStateFooter.setFont(FontRepository.findFont("Arial"));
    textStateFooter.setFontSize(12);
    textStateFooter.setHorizontalAlignment(HorizontalAlignment.Left);

    HeaderFooter header = new HeaderFooter();
    HeaderFooter footer = new HeaderFooter();

    Table tableHeader = new Table();
    tableHeader.setColumnWidths(String.valueOf(594 - header.getMargin().getLeft() - header.getMargin().getRight()));
    tableHeader.getRows().add().getCells().add("This is a Table Header", textStateHeader);

    Table table = new Table();
    table.setColumnWidths(String.valueOf(594 - footer.getMargin().getLeft() - footer.getMargin().getRight()));
    table.getRows().add().getCells().add("Powered by Aspose.PDF", textStateFooter);

    header.getParagraphs().add(tableHeader);
    footer.getParagraphs().add(table);
    footer.getMargin().setLeft(150);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## إضافة رؤوس وتذييلات LaTeX

استخدم هذا المثال عندما يجب على الرأس والتذييل أن يعرضا محتوى TeX أو LaTeX.

1. افتح ملف PDF المصدر وحدد إجمالي عدد الصفحات.
1. أنشئ كائنًا من الفئة [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) المحتوى لترويسة وتذييل كل صفحة.
1. عيّن المحتوى واحفظ المستند.

```java
public static void addHeaderAndFooterAsLatex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int pageCount = document.getPages().size();
        for (int i = 1; i <= pageCount; i++) {
            HeaderFooter header = new HeaderFooter();
            header.getParagraphs().add(new TeXFragment("This is a LaTeX Header. \\today\\", true));

            HeaderFooter footer = new HeaderFooter();
            footer.getParagraphs().add(new TeXFragment("\\copyright\\ 2025 My Company -- Page \\thepage\\ is " + pageCount, true));

            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

---
title: إضافة رؤوس وتذييلات PDF في Java
linktitle: إضافة رأس وتذييل إلى ملف PDF
type: docs
weight: 50
url: /java/add-headers-and-footers-of-pdf-file/
description: تعرف على كيفية إضافة الرؤوس والتذييلات إلى ملفات PDF في Java باستخدام النص والصور والمحتوى المنظم.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف الرؤوس والتذييلات إلى ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة الرؤوس والتذييلات إلى مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي النص وترقيم الصفحات وHTML والصورة والجدول ومحتوى الرأس والتذييل المستند إلى LaTeX.
---
يتيح لك Aspose.PDF for Java تعيين كائنات `HeaderFooter` لكل صفحة وتعبئتها بأنواع محتوى مختلفة.

## إضافة رؤوس وتذييلات النص

استخدم هذا المثال عندما تحتاج إلى محتوى نصي بسيط في أعلى وأسفل كل صفحة.

1. قم بإنشاء كائنات [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) وأضف أجزاء نصية.
1. تكوين الهوامش للرأس والتذييل.
1. قم بتطبيقها على كل صفحة من ملف PDF المصدر واحفظ النتيجة.

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

## أضف الرؤوس والتذييلات مع ترقيم الصفحات

استخدم هذا المثال عندما يُظهر الرأس أو التذييل رقم الصفحة الحالية وإجمالي عدد الصفحات.

1. قم بإنشاء كائنات [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) باستخدام العناصر النائبة لترقيم الصفحات.
1. قم بتكوين الهوامش لكلا الكائنين.
1. قم بتطبيقها على كل صفحة واحفظ ملف PDF المحدث.

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

## أضف رؤوس وتذييلات HTML

استخدم هذا المثال عندما يجب أن يتضمن محتوى الرأس والتذييل تنسيق HTML المضمن.

1. قم بإنشاء كائنات [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) وأضف محتوى [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/).
1. تكوين الهوامش للموضع.
1. قم بتعيين الرأس والتذييل لكل صفحة واحفظ المستند.

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

1. قم بإنشاء كائنات [صورة](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) وأضفها إلى حاويات الرأس والتذييل.
1. تكوين الهوامش وتعيين الحاويات لكل صفحة.
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

## أضف الرؤوس والتذييلات المستندة إلى الجدول

استخدم هذا المثال عندما يجب أن يستخدم محتوى الرأس والتذييل تخطيط الجدول وتصميم النص.

1. قم بإنشاء أنماط النص وكائنات الجدول المطلوبة.
1. أضف الجداول إلى حاويات [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/).
1. قم بتطبيق الرأس والتذييل على كل صفحة واحفظ المستند.

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

## أضف رؤوس وتذييلات LaTeX

استخدم هذا المثال عندما يجب أن يعرض الرأس والتذييل محتوى TeX أو LaTeX.

1. افتح ملف PDF المصدر وحدد إجمالي عدد الصفحات.
1. قم بإنشاء محتوى [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) لرأس وتذييل كل صفحة.
1. قم بتعيين المحتوى وحفظ المستند.

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

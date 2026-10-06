---
title: 在 Java 中添加 PDF 页眉和页脚
linktitle: 向 PDF 添加页眉和页脚
type: docs
weight: 50
url: /zh/java/add-headers-and-footers-of-pdf-file/
description: 了解如何使用文本、图像和结构化内容在 Java 中向 PDF 文件添加页眉和页脚。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 为 PDF 文件添加页眉和页脚。
Abstract: 本文展示了如何使用 Aspose.PDF for Java 为 PDF 文档添加页眉和页脚。它涵盖了文字、页码、HTML、图像、表格以及基于 LaTeX 的页眉和页脚内容。
---
Aspose.PDF for Java 让您分配 `HeaderFooter` 将对象添加到每页并用不同的内容类型填充它们。

## 添加文本页眉和页脚

当您需要在每页的顶部和底部放置简单文本内容时，请使用此示例。

1. 创建 [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) 对象并添加文本片段。
1. 配置页眉和页脚的边距。
1. 将它们应用于源 PDF 的每一页并保存结果。

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

## 添加带页码的页眉和页脚

在标题或页脚应显示当前页码和总页数时使用此示例。

1. 创建 [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) 带有页码占位符的对象。
1. 为两个对象配置边距。
1. 将它们应用于每一页并保存更新后的 PDF。

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

## 添加 HTML 页眉和页脚

当页眉和页脚内容需要包含内联 HTML 格式时，请使用此示例。

1. 创建 [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) 对象和添加 [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) 内容。
1. 配置放置的边距。
1. 将页眉和页脚分配给每一页并保存文档。

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

## 添加图像页眉和页脚

当页眉和页脚需要在每页显示图像时，请使用此示例。

1. 创建 [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) 对象并将它们添加到页眉和页脚容器中。
1. 配置页边距并将容器分配到每一页。
1. 保存已更新的 PDF。

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

## 添加基于表格的页眉和页脚

当页眉和页脚内容应使用表格布局和文本样式时，请使用此示例。

1. 创建所需的文本样式和表对象。
1. 将表添加到 [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) 容器。
1. 将页眉和页脚应用于每一页并保存文档。

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

## 添加 LaTeX 页眉和页脚

当页眉和页脚应渲染 TeX 或 LaTeX 内容时，请使用此示例。

1. 打开源 PDF 并确定总页数。
1. 创建 [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) 每页的页眉和页脚内容。
1. 分配内容并保存文档。

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

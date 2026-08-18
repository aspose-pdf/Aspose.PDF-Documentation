---
title: 在 Java 中将其他文件格式转换为 PDF
linktitle: 将其他文件格式转换为 PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2026-06-16"
description: 了解如何使用 Aspose.PDF 将 EPUB、Markdown、PCL、XPS、PostScript、XML、XSL-FO、OFD 和 TeX 文件转换为 Java 中的 PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 如何在Java中将其他文件格式转换为PDF
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将多种源文件格式转换为 PDF。它涵盖 EPUB、Markdown、OFD、PCL、PostScript、EPS、TeX、文本、XML、XPS 和 XSL-FO 转换工作流程，在需要时使用特定于格式的加载选项和预处理步骤。
---
Aspose.PDF for Java 支持从文档、标记和页面描述格式到 PDF 的转换。

## 将 OFD 转换为 PDF

当要将 OFD 文档转换为 PDF 时，请使用此示例。

1. 通过将文件路径和 [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) 传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数来打开 OFD 源。
1. 让Aspose.PDF将OFD包解析为PDF文档模型。
1. 将生成的 PDF 保存到目标输出路径。

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## 将 TeX 转换为 PDF

当 TeX 内容应直接呈现为 PDF 时，请使用此示例。

1. 通过将文件路径和 [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) 传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数来打开 TeX 源代码。
1. 让 Aspose.PDF 解释 TeX 标记并在加载期间构建 PDF 布局。
1. 保存生成的 PDF。

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PostScript 转换为 PDF

当需要将 PostScript 文件转换为 PDF 文档时，请使用此示例。

1. 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数中使用 [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) 打开 PostScript 源代码。
1. 让 Aspose.PDF 将 PostScript 页面描述流转换为 PDF 文档模型。
1. 保存转换后的 PDF 文件。

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 EPS 转换为 PDF

当应将 Encapsulated PostScript 文件转换为 PDF 时，请使用此示例。

1. 使用 [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) 打开 EPS 源，因为 EPS 遵循相同的基于 PostScript 的加载路径。
1. 将文件加载到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 中，以便在导入期间转换页面描述内容。
1. Save the output PDF.

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 EPUB 转换为 PDF

当 EPUB 电子书应转换为 PDF 时，请使用此示例。

1. 将文件路径和 [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) 传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数中，打开 EPUB 源代码。
1. 让 Aspose.PDF 加载电子书结构并将其转换为 PDF 页面。
1. 保存转换后的 PDF。

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 Markdown 转换为 PDF

当 Markdown 内容应呈现并保存为 PDF 时，请使用此示例。

1. 通过将文件路径和 [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) 传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数来打开 Markdown 源代码。
1. 让Aspose.PDF解释Markdown内容并将其渲染为PDF页面内容。
1. 保存输出的 PDF 文件。

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 通过简单的工作流程将文本转换为 PDF

当需要将纯文本文件快速转换为 PDF 时，请使用此示例。

1. 使用 UTF-8 解码读取纯文本源，以便文本内容可作为 Java 字符串使用。
1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 将文本包装在 [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 中并将其添加到页面段落集合中。
1. 保存生成的 PDF。

```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 使用高级选项将文本转换为 PDF

当应使用其他布局或编码选项转换纯文本时，请使用此示例。

1. 从输入文件中读取所有文本行，以便在转换过程中检查分页标记。
1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并为每个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 配置边距和默认文本状态。
1. 通过 [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) 解析等宽字体，并将每一行添加为 [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)。
1. 页面构建循环完成后保存输出文件。

```java
public static void convertTxtToPdf(Path inputFile, Path outputFile) throws Exception {
    List<String> lines = Files.readAllLines(inputFile);
    try (Document document = new Document()) {
        com.aspose.pdf.Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        int pageCount = 1;
        for (String line : lines) {
            if (!line.isEmpty() && line.charAt(0) == '\f') {
                page = document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
                pageCount++;
                if (pageCount == 4) {
                    break;
                }
            } else {
                page.getParagraphs().add(new TextFragment(line));
            }
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 PCL 转换为PDF

当 PCL 打印流应转换为 PDF 时，请使用此示例。

1. 创建 [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) 并在需要宽松的导入行为时启用抑制解析错误。
1. 通过将文件路径和加载选项传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数来打开 PCL 源。
1. 将结果另存为 PDF。

```java
public static void convertPclToPdf(Path inputFile, Path outputFile) {
    PclLoadOptions loadOptions = new PclLoadOptions();
    loadOptions.setSupressErrors(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 通过 XSLT 和 HTML 将 XML 转换为 PDF

当应在最终 PDF 生成之前转换 XML 数据时，请使用此示例。

1. 通过调用专用转换方法，将带有 XSLT 文件的 XML 源转换为临时 HTML 文件。
1. 将生成的 HTML 文件传递​​到现有的 HTML 到 PDF 转换函数中，以便最终的 PDF 使用标准的 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 工作流程。
1. 转换完成后删除`finally`块中的临时HTML文件。
1. 保存生成的 PDF 文件。

```java
public static void convertXmlToPdf(Path xsltFile, Path xmlFile, Path outputFile) throws Exception {
    Path htmlFile = Files.createTempFile("aspose-pdf-xml-", ".html");
    try {
        transformXmlToHtml(xmlFile, xsltFile, htmlFile);
        HtmlToPdfExamples.convertHtmlToPdf(htmlFile, outputFile);
    } finally {
        Files.deleteIfExists(htmlFile);
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## 将 XPS 转换为 PDF

当需要将 XPS 文档转换为 PDF 时，请使用此示例。

1. 通过将文件路径和 [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) 传递到 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数来打开 XPS 源。
1. 让 Aspose.PDF 在文档加载期间解释 XPS 页面描述。
1. 保存转换后的 PDF。

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 XSL-FO 转换为 PDF

当 XSL-FO 内容应呈现为 PDF 时，请使用此示例。

1. 使用 XSLT 路径创建 [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/)，以便可以在加载期间转换 XML 源。
1. 将解析错误处理模式配置为在遇到无效的 XSL-FO 时立即抛出。
1. 使用这些加载选项在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 中打开 XML 源。
1. 保存生成的 PDF 文档。

```java
public static void convertXslFoToPdf(Path xsltFile, Path xmlFile, Path outputFile) {
    XslFoLoadOptions loadOptions = new XslFoLoadOptions(xsltFile.toString());
    loadOptions.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);
    try (Document document = new Document(xmlFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## 将 XML 转换为中间 HTML

当必须在最终 PDF 转换步骤之前将 XML 数据转换为 HTML 时，请使用此方法。

1. 打开 XML 和 XSLT 输入文件作为转换源。
1. 从 XSLT 样式表创建 `Transformer` 并针对 XML 源运行它。
1. 将转换后的 HTML 文件写入磁盘，以便下游 PDF 转换功能可以加载它。

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```

---
title: 在 Java 中将其他文件格式转换为 PDF
linktitle: 将其他文件格式转换为 PDF
type: docs
weight: 80
url: /zh/java/convert-other-files-to-pdf/
lastmod: "2026-10-06"
description: 了解如何在 Java 中使用 Aspose.PDF 将 EPUB、Markdown、PCL、XPS、PostScript、XML、XSL-FO、OFD 和 TeX 文件转换为 PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 如何在 Java 中将其他文件格式转换为 PDF
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 将多种源文件格式转换为 PDF。它涵盖了 EPUB、Markdown、OFD、PCL、PostScript、EPS、TeX、文本、XML、XPS 和 XSL-FO 的转换工作流，在需要时使用特定格式的加载选项和预处理步骤。
---
Aspose.PDF for Java 支持将文档、标记和页面描述格式转换为 PDF。

## 将 OFD 转换为 PDF

当需要将 OFD 文档转换为 PDF 时，请使用此示例。

1. 通过传递文件路径并打开 OFD 源 [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) 进入 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 让 Aspose.PDF 将 OFD 包解析为 PDF 文档模型。
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

当 TeX 内容应直接渲染为 PDF 时，请使用此示例。

1. 通过传递文件路径打开 TeX 源文件并 [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) 进入 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
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

在需要将 PostScript 文件转换为 PDF 文档时使用此示例。

1. 使用以下方式打开 PostScript 源文件 [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) 在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 让 Aspose.PDF 将 PostScript 页面描述流转换为 PDF 文档模型。
1. 保存已转换的 PDF 文件。

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 EPS 转换为 PDF

当需要将 Encapsulated PostScript 文件转换为 PDF 时，请使用此示例。

1. 使用以下方式打开 EPS 源 [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) 因为 EPS 遵循相同的基于 PostScript 的加载路径。
1. 将文件加载到 a [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 因此，页面描述内容在导入期间会被转换。
1. 保存输出 PDF。

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 EPUB 转换为 PDF

当需要将 EPUB 电子书转换为 PDF 时，请使用此示例。

1. 通过传递文件路径并打开 EPUB 源 [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) 进入 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 让 Aspose.PDF 加载电子书结构并将其转换为 PDF 页面。
1. 保存已转换的 PDF。

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 Markdown 转换为 PDF

当需要将 Markdown 内容渲染并保存为 PDF 时，请使用此示例。

1. 通过传递文件路径打开 Markdown 源并 [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) 进入 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 让 Aspose.PDF 解析 Markdown 内容并将其渲染为 PDF 页面内容。
1. 保存输出的 PDF 文件。

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 使用简单工作流将文本转换为 PDF

在需要快速将纯文本文件转换为 PDF 时，请使用此示例。

1. 使用 UTF-8 解码读取纯文本源，以便文本内容可作为 Java 字符串使用。
1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 将文本包装在一个 [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 并将其添加到页面段落集合中。
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

## 将文本转换为 PDF，使用高级选项

当需要将纯文本转换为带有额外布局或编码选项的内容时，请使用此示例。

1. 读取输入文件的所有文本行，以便在转换过程中检查分页标记。
1. 创建一个空的 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)，并为每个 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 配置边距和默认文本状态。
1. 通过解析等宽字体 [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) 并将每行添加为 [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)。
1. 在页面构建循环完成后保存输出文件。

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

## 将 PCL 转换为 PDF

当需要将 PCL 打印流转换为 PDF 时，请使用此示例。

1. 创建 [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) 并在需要宽松导入行为时启用已抑制的解析错误。
1. 打开 PCL 源，通过将文件路径和加载选项传递给 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 将结果保存为 PDF。

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

当需要在最终 PDF 生成之前转换 XML 数据时，请使用此示例。

1. 通过调用专用的转换方法，将 XML 源与 XSLT 文件转换为临时 HTML 文件。
1. 将生成的 HTML 文件传递给现有的 HTML 转 PDF 转换函数，以便最终的 PDF 使用标准 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 工作流。
1. 删除临时 HTML 文件 `finally` 在转换完成后阻塞。
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

1. 通过传递文件路径打开 XPS 源并 [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) 进入 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 构造函数。
1. 在文档加载期间，让 Aspose.PDF 解释 XPS 页面描述。
1. 保存已转换的 PDF。

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 将 XSL-FO 转换为 PDF

当需要将 XSL-FO 内容渲染为 PDF 时，请使用此示例。

1. 创建 [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) 使用 XSLT 路径，以便在加载期间可以转换 XML 源。
1. 配置解析错误处理模式，使在遇到无效 XSL-FO 时立即抛出异常。
1. 使用这些加载选项，在 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 中打开 XML 源文件。
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

当 XML 数据必须在最终 PDF 转换步骤之前转换为 HTML 时，请使用此方法。

1. 打开 XML 和 XSLT 输入文件作为转换源。
1. 创建一个 `Transformer` 从 XSLT 样式表获取并在 XML 源上运行它。
1. 将转换后的 HTML 文件写入磁盘，以便下游的 PDF 转换函数能够加载它。

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```

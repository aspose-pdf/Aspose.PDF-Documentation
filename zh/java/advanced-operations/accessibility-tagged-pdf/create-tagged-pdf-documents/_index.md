---
title: 在 Java 中创建带标签的 PDF
linktitle: 创建带标签的 PDF
type: docs
weight: 10
url: /java/create-tagged-pdf/
description: 了解如何使用 Aspose.PDF 在 Java 中创建带标签的 PDF 文档，包括 PDF/UA 结构元素、可访问的表单字段、TOC 页面和自动标记。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
创建带标签的 PDF 意味着添加结构元素，使文档更容易根据 PDF/UA 可访问性要求进行验证，并且更易于辅助技术解释。

## 创建一个简单的带标签的 PDF 文档

当您需要在逻辑结构树中包含标题和段落的最小标记 PDF 时，请使用此示例。

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并获取其 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/)。
1. 设置文档标题和语言，然后创建所需的标题和段落元素。
1. 将结构元素附加到根元素并保存文档。

```java
public static void createTaggedPdfDocumentSimple(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        StructureElement rootElement = taggedContent.getRootElement();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        HeaderElement mainHeader = taggedContent.createHeaderElement();
        mainHeader.setText("Main Header");

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                + "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. "
                + "Cras pellentesque libero semper, gravida magna sed, luctus leo.");

        rootElement.appendChild(mainHeader, true);
        rootElement.appendChild(paragraphElement, true);
        document.save(outputFile.toString());
    }
}
```

## 创建高级标记 PDF 文档

此示例通过混合标题、段落、跨度、引号和显式布局设置来构建更丰富的结构。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并初始化标记的内容元数据。
1. 构建标题和段落结构，然后在段落内添加跨度和引用元素。
1. 调整段落位置，将元素附加到根结构，然后保存文档。

```java
public static void createTaggedPdfDocumentAdv(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        StructureElement rootElement = taggedContent.getRootElement();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        HeaderElement header1 = taggedContent.createHeaderElement(1);
        header1.setText("Header Level 1");

        ParagraphElement paragraphWithQuotes = taggedContent.createParagraphElement();
        paragraphWithQuotes.getStructureTextState().setFont(FontRepository.findFont("Arial"));

        PositionSettings positionSettings = new PositionSettings();
        positionSettings.setMargin(new MarginInfo(10, 5, 10, 5));
        paragraphWithQuotes.adjustPosition(positionSettings);

        SpanElement spanElement1 = taggedContent.createSpanElement();
        spanElement1.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                + "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. ");

        QuoteElement quoteElement = taggedContent.createQuoteElement();
        quoteElement.setText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus.");
        quoteElement.getStructureTextState().setFontStyle(Nullable.of(FontStyles.Bold | FontStyles.Italic));

        SpanElement spanElement2 = taggedContent.createSpanElement();
        spanElement2.setText(" Sed non consectetur elit.");

        paragraphWithQuotes.appendChild(spanElement1, true);
        paragraphWithQuotes.appendChild(quoteElement, true);
        paragraphWithQuotes.appendChild(spanElement2, true);

        rootElement.appendChild(header1, true);
        rootElement.appendChild(paragraphWithQuotes, true);
        document.save(outputFile.toString());
    }
}
```

## 为标记内容添加文本样式

当标记的段落内容应包含明确的字体、颜色和样式信息时，请使用此示例。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建段落元素并配置其结构文本状态。
1. 设置段落文本并保存文档。

```java
public static void addStyle(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        paragraphElement.getStructureTextState().setFontSize(Nullable.of(18.0f));
        paragraphElement.getStructureTextState().setForegroundColor(Color.getRed());
        paragraphElement.getStructureTextState().setFontStyle(Nullable.of(FontStyles.Italic));
        paragraphElement.setText("Red italic text.");

        document.save(outputFile.toString());
    }
}
```

## 添加图形结构元素

此示例演示如何使用替代文本、标题、自定义标签、图像内容和位置创建带标签的图形。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [FigureElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/figureelement/)，设置其可访问的元数据，并分配图像。
1. 调整图形位置并保存文档。

```java
public static void illustrateStructureElements(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        FigureElement figure1 = taggedContent.createFigureElement();
        taggedContent.getRootElement().appendChild(figure1, true);
        figure1.setAlternativeText("Figure One");
        figure1.setTitle("Image 1");
        figure1.setTag("Fig1");
        figure1.setImage(imageFile.toString(), 300);

        PositionSettings positionSettings = new PositionSettings();
        MarginInfo marginInfo = new MarginInfo();
        marginInfo.setLeft(50);
        marginInfo.setTop(20);
        positionSettings.setMargin(marginInfo);
        figure1.adjustPosition(positionSettings);

        document.save(outputFile.toString());
    }
}
```

## 验证带标签的 PDF 是否为 PDF/UA

当您需要检查带标签的 PDF 是否满足 PDF/UA 验证规则时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 针对 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).`PDF_UA_1` 运行验证。
1. 写入验证日志并打印验证结果。

```java
public static void validateTaggedPdf(Path inputFile, Path logFile) {
    try (Document document = new Document(inputFile.toString())) {
        boolean isValid = document.validate(logFile.toString(), PdfFormat.PDF_UA_1);
        System.out.println("Is Valid: " + isValid);
    }
}
```

## 调整结构元素位置

此示例将显式边距和对齐设置应用于标记的段落。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 添加段落结构元素并准备 [PositionSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/)。
1. 将位置设置应用到段落并保存文档。

```java
public static void adjustPosition(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();

        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);
        paragraph.setText("Text.");

        PositionSettings positionSettings = new PositionSettings();
        MarginInfo marginInfo = new MarginInfo();
        marginInfo.setLeft(300);
        marginInfo.setTop(20);
        marginInfo.setRight(0);
        marginInfo.setBottom(0);
        positionSettings.setMargin(marginInfo);
        positionSettings.setHorizontalAlignment(HorizontalAlignment.None);
        positionSettings.setVerticalAlignment(VerticalAlignment.None);
        positionSettings.setFirstParagraphInColumn(false);
        positionSettings.setKeptWithNext(false);
        positionSettings.setInNewPage(false);
        positionSettings.setInLineParagraph(false);
        paragraph.adjustPosition(positionSettings);

        document.save(outputFile.toString());
    }
}
```

## 使用自动标记将现有 PDF 转换为 PDF/UA

当现有 PDF 需要转换为 PDF/UA 并在转换过程中自动标记时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) 并启用自动标记。
1. 运行转换并保存输出文档。

```java
public static void convertToPdfUaWithAutomaticTagging(Path inputFile, Path outputFile, Path logFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfFormatConversionOptions options = new PdfFormatConversionOptions(
                logFile.toString(), PdfFormat.PDF_UA_1, ConvertErrorAction.Delete);

        AutoTaggingSettings autoTaggingSettings = new AutoTaggingSettings();
        autoTaggingSettings.setEnableAutoTagging(true);
        autoTaggingSettings.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Auto);
        options.setAutoTaggingSettings(autoTaggingSettings);

        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## 创建带有可访问表单字段的带标签的 PDF

此示例标记签名表单字段，使其成为逻辑结构树的一部分。

1. 创建一个新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加带有表单字段的页面。
1. 将表单字段添加到文档表单集合中。
1. 创建带标记的表单结构元素，将其与字段关联，然后保存文档。

```java
public static void createPdfWithTaggedFormField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        ITaggedContent taggedContent = document.getTaggedContent();
        StructureElement rootElement = taggedContent.getRootElement();

        SignatureField signatureField = new SignatureField(page, new Rectangle(50, 50, 100, 100, true));
        signatureField.setPartialName("Signature1");
        signatureField.setAlternateName("signature 1");

        Form formFields = document.getForm();
        formFields.add(signatureField);

        FormElement form = taggedContent.createFormElement();
        form.setAlternativeText("form 1");
        form.tag(signatureField);
        rootElement.appendChild(form, true);

        document.save(outputFile.toString());
    }
}
```

## 创建带有目录页的带标签的 PDF

当带标签的 PDF 应包含链接到文档标题的基本目录页面时，请使用此示例。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加目录页面。
1. 创建 [TOCElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tocelement/) 和应出现在 TOC 中的标头。
1. 将目录条目链接到标题并保存文档。

```java
public static void createPdfWithTocPage(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent content = document.getTaggedContent();
        StructureElement rootElement = content.getRootElement();
        content.setLanguage("en-US");

        Page tocPage = document.getPages().add();
        tocPage.setTocInfo(new TocInfo());

        TOCElement tocElement = content.createTOCElement();
        rootElement.appendChild(tocElement, true);

        document.getPages().add();

        HeaderElement header = content.createHeaderElement(1);
        header.setText("1. Header");
        rootElement.appendChild(header, true);

        TOCIElement toci = content.createTOCIElement();
        tocElement.appendChild(toci, true);
        header.addEntryToTocPage(tocPage, toci);
        toci.addRef(header);

        document.save(outputFile.toString());
    }
}
```

## 创建带有目录页的高级标记 PDF

此示例构建了一个更复杂的标记目录，其中包含链接的页面标题、嵌套列表项和多个标题级别。

1. 创建一个新的带标签的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并准备一个带有可见标题的 TOC 页面。
1. 创建目录结构，将目录标题和条目链接到标题和列表项，并添加相关内容元素。
1. 使用高级目录结构保存最终文档。

```java
public static void createPdfWithTocPageAdvanced(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent content = document.getTaggedContent();
        StructureElement rootElement = content.getRootElement();
        content.setLanguage("en-US");

        Page tocPage = document.getPages().add();
        tocPage.setTocInfo(new TocInfo());
        tocPage.getTocInfo().setTitle(new TextFragment("Table of Contents"));

        TOCElement tocElement = content.createTOCElement();
        HeaderElement headerForTocPageTitle = content.createHeaderElement(1);
        tocElement.linkTocPageTitleToHeaderElement(tocPage, headerForTocPageTitle);

        rootElement.appendChild(headerForTocPageTitle, true);
        rootElement.appendChild(tocElement, true);

        document.getPages().add();

        HeaderElement header = content.createHeaderElement(1);
        header.setText("1. Header");
        rootElement.appendChild(header, true);

        TOCIElement toci = content.createTOCIElement();
        tocElement.appendChild(toci, true);
        header.addEntryToTocPage(tocPage, toci);
        toci.addRef(header);

        ListElement listElement = content.createListElement();
        for (int i = 1; i < 4; i++) {
            ListLIElement li = content.createListLIElement();
            listElement.appendChild(li, true);

            HeaderElement subHeader = content.createHeaderElement(2);
            subHeader.getStructureTextState().setFontSize(Nullable.of(14.0f));
            subHeader.setLanguage("en-US");
            subHeader.setText("1." + i + " subheader ");
            subHeader.addEntryToTocPage(tocPage, li);
            li.addRef(subHeader);

            ParagraphElement p = content.createParagraphElement();
            p.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit.");
            p.setLanguage("en-US");

            rootElement.appendChild(subHeader, true);
            rootElement.appendChild(p, true);
        }
        toci.appendChild(listElement, true);

        HeaderElement header2 = content.createHeaderElement(1);
        header2.setText("2. Header");
        rootElement.appendChild(header2, true);

        TOCIElement toci2 = content.createTOCIElement();
        tocElement.appendChild(toci2, true);
        header2.addEntryToTocPage(tocPage, toci2);
        toci2.addRef(header2);

        document.save(outputFile.toString());
    }
}
```

---
title: 操作PDF文档
linktitle: 操作PDF文档
type: docs
weight: 30
url: /zh/java/manipulate-pdf-document/
description: 本文包含有关如何验证PDF文档以符合PDF A标准，如何处理目录，如何设置PDF过期日期，以及如何确定PDF文件生成进度的信息。
lastmod: "2021-06-05"
---

## 验证PDF文档是否符合PDF A标准（A 1A 和 A 1B）

要验证PDF文档是否兼容PDF/A-1a或PDF/A-1b，请使用[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类的[validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-)方法。此方法允许您指定结果要保存的文件名称和所需的验证类型[PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat)枚举：PDF_A_1A或PDF_A_1B。

输出XML格式是自定义的Aspose格式。
 The XML 包含一组名为 Problem 的标签；每个标签包含特定问题的详细信息。Problem 标签的 ObjectID 属性表示此问题相关的特定对象的 ID。Clause 属性表示 PDF 规范中的相应规则。

```java
  public static void ValidatePDFDocumentForPDF_A_Standard() {
    // 打开文档
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 验证 PDF/A-1a 的 PDF
    pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);

    // 保存更新后的 PDF 文件
    // document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## 处理目录

### 向现有 PDF 添加目录

aspose.pdf 包中的 ListSection 类允许您在从头创建 PDF 文档时创建目录。要添加作为目录元素的标题，请使用 [aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 类。

要向现有 PDF 文件添加目录，请使用 com.aspose.pdf 包中的 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 类。 com.aspose.pdf 包可以创建新的 PDF 文件和操作现有的 PDF 文件。要向现有的 PDF 添加目录，请使用 com.aspose.pdf 包。

下面的代码片段展示了如何在现有的 PDF 文件中创建一个目录。

```java
public static void AddTOCtoExistingPDF() {
    // 加载现有的 PDF 文件
    Document document = new Document(_dataDir + "sample.pdf");

    // 访问 PDF 文件的第一页
    Page tocPage = document.getPages().insert(1);

    // 创建对象以表示目录信息
    com.aspose.pdf.TocInfo tocInfo = new com.aspose.pdf.TocInfo();
    com.aspose.pdf.TextFragment title = new com.aspose.pdf.TextFragment("目录");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(com.aspose.pdf.FontStyles.Bold);

    // 设置目录的标题
    tocInfo.setTitle(title);
    tocPage.setTocInfo(tocInfo);

    // 创建字符串对象，将用作目录元素
    String[] titles = new String[4];
    titles[0] = "第一页";
    titles[1] = "第二页";
    titles[2] = "第三页";
    titles[3] = "第四页";
    for (int i = 0; i < 4; i++) {
      // 创建 Heading 对象
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(1);

      com.aspose.pdf.TextSegment segment2 = new com.aspose.pdf.TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);

      // 指定 Heading 对象的目标页
      heading2.setDestinationPage(document.getPages().get_Item(i + 2));

      // 目标页
      heading2.setTop(document.getPages().get_Item(i + 2).getRect().getHeight());

      // 目标坐标
      segment2.setText(titles[i]);

      // 将 Heading 添加到包含目录的页面
      tocPage.getParagraphs().add(heading2);
    }
    // 保存更新后的文档
    document.save("TOC_Output_Java.pdf");
  }
```
### 为不同的目录级别设置不同的 TabLeaderType

Aspose.PDF 还允许为不同的目录级别设置不同的 TabLeaderType。您需要通过以下方式将 FormatArray 的 LineDash 属性设置为 TabLeaderType 枚举的适当值。

```java
  public static void SetDifferentTabLeaderTypeForTOCLevels() {

    String outFile = "TOC.pdf";

    Document document = new Document();
    Page tocPage = document.getPages().add();

    TocInfo tocInfo = new TocInfo();

    // 设置 LeaderType

    tocInfo.setLineDash(TabLeaderType.Solid);

    TextFragment title = new TextFragment("目录");
    title.getTextState().setFontSize(30);
    tocInfo.setTitle(title);

    // 将列表部分添加到 Pdf 文档的 sections 集合中

    tocPage.setTocInfo(tocInfo);

    // 通过设置左边距和每个级别的文本格式设置来定义四级列表的格式

    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setLeft(0);
    tocInfo.getFormatArray()[0].getMargin().setRight(30);
    tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
    tocInfo.getFormatArray()[1].getMargin().setLeft(10);
    tocInfo.getFormatArray()[1].getMargin().setRight(30);
    tocInfo.getFormatArray()[1].setLineDash(TabLeaderType.None);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
    tocInfo.getFormatArray()[2].getMargin().setLeft(20);
    tocInfo.getFormatArray()[2].getMargin().setRight(0);
    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
    tocInfo.getFormatArray()[3].getMargin().setLeft(30);
    tocInfo.getFormatArray()[3].getMargin().setRight(30);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    // 在 Pdf 文档中创建一个部分
    Page page = document.getPages().add();

    // 在部分中添加四个标题
    for (int Level = 1; Level <= 4; Level++) {
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(Level);
      TextSegment segment2 = new TextSegment();

      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      heading2.setTocPage(tocPage);

      segment2.setText("示例标题" + Level);
      heading2.getTextState().setFont(FontRepository.findFont("Arial UnicodeMS"));

      // 将标题添加到目录中。
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }

    // 保存 PDF
    document.save(outFile);
  }
```

### 在目录中隐藏页码

如果您不想在目录中显示页码，可以将[TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo)类的[IsShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo)属性设置为false。请检查以下代码片段以在目录中隐藏页码：

```java
public static void HidePageNumbersInTOC() {
    String outFile = _dataDir + "HiddenPageNumbers_out.pdf";
    Document doc = new Document();
    Page tocPage = doc.getPages().add();
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("目录");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.setTitle(title);

    // 将列表部分添加到Pdf文档的部分集合中
    tocPage.setTocInfo(tocInfo);

    // 通过设置左边距和文本格式设置来定义四级列表的格式

    tocInfo.setShowPageNumbers(false);
    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setRight(0);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);

    tocInfo.getFormatArray()[1].getMargin().setLeft(30);
    tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);

    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    Page page = doc.getPages().add();

    // 在部分中添加四个标题
    for (int Level = 1; Level != 5; Level++) {
      Heading heading2 = new Heading(Level);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      segment2.setText("这是第 " + Level + " 级的标题");
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }
    doc.save(_dataDir + outFile);
  }
```


### 在添加目录时自定义页码

在 PDF 文档中添加目录时，自定义目录中的页码是很常见的。例如，我们可能需要在页码前添加一些前缀，如 P1, P2, P3 等。在这种情况下，Aspose.PDF for Java 提供了 TocInfo 类的 PageNumbersPrefix 属性，可以用来自定义页码，如下面的代码示例所示。

```java
  public static void CustomizePageNumbersWhileAddingTOC() {

    String inFile = _dataDir + "sample.pdf";
    String outFile = _dataDir + "42824_out.pdf";

    // 加载现有的 PDF 文件
    Document doc = new Document(inFile);
    // 访问 PDF 文件的第一页
    Page tocPage = doc.getPages().insert(1);
    // 创建对象以表示目录信息
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Table Of Contents");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);

    // 设置目录的标题
    tocInfo.setTitle(title);
    tocInfo.setPageNumbersPrefix("P");
    tocPage.setTocInfo(tocInfo);

    for (int i = 1; i < doc.getPages().size(); i++) {
      // 创建 Heading 对象
      Heading heading2 = new Heading(1);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      // 指定标题对象的目标页
      heading2.setDestinationPage(doc.getPages().get_Item(i + 1));
      // 目标页
      heading2.setTop(doc.getPages().get_Item(i + 1).getRect().getHeight());
      // 目标坐标
      segment2.setText("Page " + i);
      // 将标题添加到包含目录的页面
      tocPage.getParagraphs().add(heading2);
    }

    // 保存更新后的文档
    doc.save(outFile);
  }
```


## 添加图层到 PDF 文件

图层可以在 PDF 文档中有多种用途。你可能有一个多语言文件想要分发，并希望每种语言的文本出现在不同的图层上，而背景设计出现在一个单独的图层上。你也可以创建包含动画的文档，该动画出现在一个单独的图层上。一个例子是将许可证协议添加到你的文件中，并且不希望用户在同意协议条款之前查看内容。

Aspose.PDF for Java 支持向 PDF 文件添加图层。

要在 PDF 文件中使用图层，请使用以下 API 成员。

[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) 类表示一个图层，并包含以下属性：

- **Name** – 图层的名称。
- **Id** – 图层的 ID。
- **Contents** – 图层操作列表。

一旦定义了 [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) 对象，就将它们添加到 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 对象的 Layers 集合中。
 文档下方的代码展示了如何向 PDF 文档添加图层。

```java
public static void AddLayersToPDFFile() {
    Document doc = new Document();
    Page page = doc.getPages().add();
    Layer layer = new Layer("oc1", "Red Line");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(1, 0, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 700));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 700));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.setLayers(new ArrayList<Layer>());
    page.getLayers().add(layer);
    layer = new Layer("oc2", "Green Line");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 1, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 750));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 750));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    layer = new Layer("oc3", "Blue Line");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 0, 1));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 800));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 800));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    doc.save("output.pdf");
  
```
## 设置 PDF 过期

PDF 过期功能设置 PDF 文件的有效期。在特定日期，如果有人尝试访问它，将显示一个弹出窗口，说明文件已过期，需要新的文件。

Aspose.PDF 允许您在创建和编辑 PDF 文件时设置过期日期。

下面的代码片段展示了如何为 PDF 文件设置过期日期。您需要使用 JavaScript，因为由第三方组件保存的文件（例如 OwnerGuard）无法在没有该工具的其他工作站上查看。

可以使用带有过期日期的现有文件通过 PDF OwnerGuard 创建 PDF 文件。但新文件只能在安装了 PDF OwnerGuard 的工作站上打开。没有 PDF OwnerGuard 的工作站将给出 ExpirationFeatureError。例如，如果安装了 OwnerGuard，PDF 阅读器可以打开文件，但 Adobe Acrobat 会返回错误。

```java
  public static void SetPDFExpiration() {
    Document document = new Document(_dataDir+"sample.pdf");    
    JavascriptAction javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" + 
      "expiry = new Date(year, month);" + 
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    document.setOpenAction(javaScript);
    document.save(_dataDir + "JavaScript-Added.pdf");
  }
```
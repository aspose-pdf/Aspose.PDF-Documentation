---
title: 格式化PDF文档 
linktitle: 格式化PDF文档
type: docs
weight: 20
url: /java/formatting-pdf-document/
description: 使用Aspose.PDF for Java格式化PDF文档。使用下一个代码片段来解决您的任务。
lastmod: "2021-06-05"
---

## 获取文档窗口和页面显示属性

本主题帮助您了解如何获取文档窗口、查看器应用程序的属性以及页面的显示方式。

要设置这些不同的属性，请使用[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类打开PDF文件。现在，您可以获取[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的方法，例如：

- [IsCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – 将文档窗口居中于屏幕。默认：false。
- [SetDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – 阅读顺序。
 这决定了当页面并排显示时的布局方式。默认：从左到右。
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – 在文档窗口的标题栏中显示文档标题。默认：false（显示标题）。
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-) – 隐藏或显示文档窗口的菜单栏。默认：false（显示菜单栏）。
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-) – 隐藏或显示文档窗口的工具栏。默认：false（显示工具栏）。
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-) – 隐藏或显示文档窗口元素，如滚动条。默认：false（显示UI元素）。

- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-) – 当文档不以全页面模式显示时，如何显示文档。- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-) – 页面布局。
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-) – 文档首次打开时的显示方式。选项包括显示缩略图、全屏显示、显示附件面板。

以下代码片段向您展示如何使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类获取属性。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleFormatting {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void GetDocumentWindowAndPageDisplayProperties() {

    // 打开文档
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 获取不同的文档属性
    // 文档窗口的位置 - 默认值: false
    System.out.printf("CenterWindow : " + pdfDocument.isCenterWindow());

    // 主要的阅读顺序；确定页面的位置
    // 当并排显示时 - 默认值: L2R
    System.out.printf("Direction :- " + pdfDocument.getDirection());

    // 窗口的标题栏是否应显示文档标题。
    // 如果为假，标题栏显示 PDF 文件名 - 默认值: false
    System.out.printf("DisplayDocTitle :- " + pdfDocument.isDisplayDocTitle());

    // 是否调整文档窗口的大小以适应
    // 首次显示的页面的大小 - 默认值: false
    System.out.printf("FitWindow :- " + pdfDocument.isFitWindow());

    // 是否隐藏查看器应用程序的菜单栏 - 默认值: false
    System.out.printf("HideMenuBar :-" + pdfDocument.isHideMenubar());

    // 是否隐藏查看器应用程序的工具栏 - 默认值: false
    System.out.printf("HideToolBar :-" + pdfDocument.isHideToolBar());

    // 是否隐藏像滚动条这样的 UI 元素
    // 仅显示页面内容 - 默认值: false
    System.out.printf("HideWindowUI :-" + pdfDocument.isHideWindowUI());

    // 文档的页面模式。退出全屏模式时如何显示文档。
    System.out.printf("NonFullScreenPageMode :-" + pdfDocument.getNonFullScreenPageMode());

    // 页面布局，即单页，一列
    System.out.printf("PageLayout :-" + pdfDocument.getPageLayout());

    // 打开时文档应如何显示。
    System.out.printf("pageMode :-" + pdfDocument.getPageMode());

  }

```

## 设置文档窗口和页面显示属性

本主题解释如何设置文档窗口、查看器应用程序和页面显示的属性。

要设置这些不同的属性：

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开 PDF 文件。
1. 设置 Document 对象的属性。
1. 使用 Save 方法保存更新后的 PDF 文件。

可用的属性有：

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

以下代码片段向您展示如何使用[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类设置属性。

```java
  public static void SetDocumentWindowAndPageDisplayProperties() {

    // 打开文档
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    
    // 设置不同的文档属性
    // 指定是否居中显示文档窗口 - 默认值: false
    pdfDocument.setCenterWindow(true);
    
    // 主要阅读顺序; 确定页面在并排显示时的位置 - 默认: L2R
    pdfDocument.setDirection(com.aspose.pdf.Direction.R2L);
    
    // 指定窗口标题栏是否应显示文档标题
    // 如果为false，标题栏显示PDF文件名 - 默认值: false
    pdfDocument.setDisplayDocTitle(true);
    
    // 指定是否调整文档窗口的大小以适应
    // 第一个显示的页面的大小 - 默认值: false
    pdfDocument.setFitWindow(true);
    
    // 指定是否隐藏查看器应用程序的菜单栏 - 默认值:
    // false
    pdfDocument.setHideMenubar(true);
    
    // 指定是否隐藏查看器应用程序的工具栏 - 默认值:
    // false
    pdfDocument.setHideToolBar(true);
    
    // 指定是否隐藏UI元素如滚动条
    // 仅显示页面内容 - 默认值: false
    pdfDocument.setHideWindowUI(true);
    
    // 文档的页面模式。指定退出
    // 全屏模式时如何显示文档。
    pdfDocument.setNonFullScreenPageMode(com.aspose.pdf.PageMode.UseOC);
    
    // 指定页面布局，即单页、一列
    pdfDocument.setPageLayout(com.aspose.pdf.PageLayout.TwoColumnLeft);
    
    // 指定打开文档时应如何显示
    // 即显示缩略图、全屏、显示附件面板
    pdfDocument.setPageMode(com.aspose.pdf.PageMode.UseThumbs);
    
    // 保存更新后的PDF文件
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");

  }
```

## 在现有 PDF 文件中嵌入字体

PDF 阅读器支持[14 种核心字体](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts)，以便无论文档在哪个平台上显示，都能以相同的方式呈现。当 PDF 包含核心字体之外的字体时，嵌入字体以避免字体替换。

Aspose.PDF for Java 支持在现有 PDF 文档中嵌入字体。您可以嵌入完整字体或子集。要嵌入字体：

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开现有的 PDF 文件。
1. 使用 [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) 类嵌入字体。
   1. setEmbedded(true) 方法嵌入完整字体。
   1. pageFont.isSubset(true) 方法嵌入字体的子集。

字体子集仅嵌入使用的字符，这在字体用于简短句子或标语时很有用，例如企业字体用于标识但不用于正文文本的情况。
 使用子集可以减少输出PDF的文件大小。

但是，如果为正文文本使用自定义字体，请将其完整嵌入。

以下代码片段展示了如何在PDF文件中嵌入字体。
```java
public static void EmbeddingFontsInAnExistingPDFFile() {
    // 打开文档
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // 遍历所有页面
    for (com.aspose.pdf.Page page : (Iterable<com.aspose.pdf.Page>) pdfDocument.getPages()) {
      if (page.getResources().getFonts() != null) {
        for (com.aspose.pdf.Font pageFont : (Iterable<com.aspose.pdf.Font>) page.getResources().getFonts()) {
          // 检查字体是否已经嵌入
          if (!pageFont.isEmbedded())
            pageFont.setEmbedded(true);
        }
      }

      // 检查表单对象
      for (com.aspose.pdf.XForm form : (Iterable<com.aspose.pdf.XForm>) page.getResources().getForms()) {
        if (form.getResources().getFonts() != null) {
          for (com.aspose.pdf.Font formFont : (Iterable<com.aspose.pdf.Font>) form.getResources().getFonts()) {
            // 检查字体是否嵌入
            if (!formFont.isEmbedded())
              formFont.setEmbedded(true);
          }
        }
      }
    }
    // 保存更新后的PDF文件
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## 创建 PDF 时嵌入字体

如果您需要使用 Adobe Reader 支持的 14 种核心字体以外的任何字体，则在生成 PDF 文件时必须嵌入字体描述。如果字体信息未嵌入，Adobe Reader 会从操作系统中获取它（如果系统上安装了字体），或者根据 PDF 中的字体描述构建替代字体。请注意，嵌入的字体必须安装在主机上，即在以下代码中，‘Univers Condensed’ 字体已安装在系统上。

我们使用 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) 类的 setEmbedded 属性将字体信息嵌入到 PDF 文件中。将该属性的值设置为 ‘true’ 将会将整个字体文件嵌入到 PDF 中，考虑到这会增加 PDF 文件的大小。以下是可用于将字体信息嵌入 PDF 的代码片段。

```java
public static void EmbeddingFontsWhileCreatingPDF() {

    // 通过调用其空构造函数实例化 PDF 对象
    com.aspose.pdf.Document document = new com.aspose.pdf.Document();

    // 在 Pdf 对象中创建一个部分
    com.aspose.pdf.Page page = document.getPages().add();

    com.aspose.pdf.TextFragment fragment = new com.aspose.pdf.TextFragment("");

    com.aspose.pdf.TextSegment segment = new com.aspose.pdf.TextSegment(" This is a sample text using Custom font.");
    com.aspose.pdf.TextState ts = new com.aspose.pdf.TextState();
    ts.setFont(FontRepository.findFont("Univers Condensed"));
    ts.getFont().setEmbedded(true);
    segment.setTextState(ts);
    fragment.getSegments().add(segment);
    page.getParagraphs().add(fragment);

    // 保存更新后的 PDF 文件
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## 保存 PDF 时设置默认字体名称

当 PDF 文档中包含的字体在文档本身和设备上不可用时，API 会将这些字体替换为默认字体。当字体可用时（已安装在设备上或嵌入到文档中），输出 PDF 应具有相同的字体（不应替换为默认字体）。默认字体的值应包含字体的名称（而不是字体文件的路径）。我们实现了一个功能，可以在将文档保存为 PDF 时设置默认字体名称。以下代码片段可用于设置默认字体：

```java
public static void SetDefaultFontNameWhileSavingPDF() {

    // 加载现有的 PDF 文档
    Document document = new Document("input.pdf");

    String newName = "Arial";

    // 初始化 PDF 格式的保存选项
    PdfSaveOptions ops = new PdfSaveOptions();

    // 设置默认字体名称
    ops.setDefaultFontName(newName);

    // 保存 PDF 文件
    document.save(_dataDir + "output_out.pdf", ops);
  }
```


## 获取PDF文档中的所有字体

如果您想从PDF文档中获取所有字体，可以使用[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类中提供的**Document.getFontUtilities().getAllFonts()**方法。请查看以下代码片段以从现有PDF文档中获取所有字体：

```java
public static void GetAllFontsFromPDFDocument() {

    // 加载现有的PDF文档
    Document document = new Document(_dataDir + "sample.pdf");

    // 从文档中获取所有字体
    com.aspose.pdf.Font[] fonts = document.getFontUtilities().getAllFonts();
    for (com.aspose.pdf.Font f : fonts) {
      System.out.println(f.getFontName());
    }
  }
```

## 获取和设置PDF文件的缩放因子

有时，您可能想要设置或获取PDF文档的缩放因子。您可以使用Aspose.PDF轻松实现这一要求。

[GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction)对象允许您获取与PDF文件相关联的缩放值。
 同样，它可以用于设置文件的缩放因子。

```java
  public static void GetSetZoomFactorOfPDFFile() {
    // 加载现有的PDF文档
    Document document = new Document(_dataDir + "sample.pdf");
    double zoom = .5;
    // 设置文档的缩放因子
    GoToAction actionzoom = new GoToAction(new XYZExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth(),
        document.getPages().get_Item(1).getMediaBox().getHeight(), zoom));

    // 设置动作以适应页面宽度缩放
    GoToAction actionFittoWidth = new GoToAction(new FitHExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth()));

    // 设置动作以适应页面高度缩放
    GoToAction actionFittoHeight = new GoToAction(new FitVExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getHeight()));

    document.setOpenAction(actionzoom);
    document.setOpenAction(actionFittoWidth);
    document.setOpenAction(actionFittoHeight);
```

以下代码片段展示了如何获取 PDF 文件的缩放因子。

```java
    // 实例化新的 Document 对象
    Document doc1 = new Document(_dataDir + "Zoomed_actionzoom.pdf");
    // 创建 GoToAction 对象
    GoToAction action = (GoToAction) doc1.getOpenAction();
    // 获取 PDF 文件的缩放因子
    System.out.println(((XYZExplicitDestination) action.getDestination()).getZoom());

    // 保存更新后的 PDF 文件
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
}
```
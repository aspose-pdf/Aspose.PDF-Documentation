---
title: 替换 PDF 中的文本 
linktitle: 替换 PDF 中的文本
type: docs
weight: 40
url: /java/replace-text-in-a-pdf-document/
description: 了解更多关于替换和删除 PDF 文本的各种方法。Aspose.PDF 允许在特定区域或使用正则表达式替换文本。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 替换 PDF 文档所有页面中的文本

{{% alert color="primary" %}}

您可以尝试使用 Aspose.PDF 在文档中查找并替换文本，并在此[链接](https://products.aspose.app/pdf/redaction)上在线获取结果

{{% /alert %}}

要在 PDF 文档的所有页面上替换文本，可以使用 [Aspose.PDF for Java](https://products.aspose.com/pdf/java):

1. 首先使用 [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) 找到要替换的特定短语。

1. 然后，遍历所有 [TextFragments](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber#getTextFragments--) 来替换文本并更改任何其他属性。
1. 最后，使用 Document 类的 [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) 方法保存输出 PDF。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleReplaceText {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void ReplaceTextOnAllPages() {
        Document pdfDocument = new Document(_dataDir+"sample.pdf");

        // 创建 TextAbsorber 对象以查找输入搜索短语的所有实例
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Web");
        
        // 接受文档第一页的吸收器
        pdfDocument.getPages().accept(textFragmentAbsorber);
        
        // 将提取的文本片段放入集合中
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
        
        // 遍历片段
        for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
            // 更新文本和其他属性
            textFragment.setText("World Wide Web");
            textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getBlue());
            textFragment.getTextState().setBackgroundColor(Color.getGray());
        }
        // 保存更新后的 PDF 文件
        pdfDocument.save(_dataDir+"Updated_Text.pdf");
    }
}
```


## 在特定页面区域替换文本

为了在特定页面区域替换文本，首先，我们需要实例化 TextFragmentAbsorber 对象，使用 [TextSearchOptions.setRectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions#setRectangle-com.aspose.pdf.Rectangle-) 指定页面区域，然后遍历所有的 TextFragments 来替换文本。一旦这些操作完成，我们只需要使用 Document 对象的 save 方法保存输出的 PDF。

以下代码片段展示了如何在 PDF 文档的所有页面中替换文本。

```java
public static void ReplaceTextInParticularRegion(){
    // 加载 PDF 文件
    Document pdfDocument = new Document(_dataDir+"sample.pdf");

    // 实例化 TextFragment Absorber 对象
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("PDF");

    // 在页面边界内搜索文本
    textFragmentAbsorber.getTextSearchOptions().setLimitToPageBounds(true);

    // 指定 TextSearch Options 的页面区域
    textFragmentAbsorber.getTextSearchOptions().setRectangle(new Rectangle(100, 700, 400, 770));

    // 从 PDF 文件的第一页搜索文本
    pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);

    // 遍历单个 TextFragment
    for(TextFragment tf : textFragmentAbsorber.getTextFragments())
    {
        // 用 "---" 替换文本
        tf.setText("---");
    }

    // 保存更新后的 PDF 文件
    pdfDocument.save(_dataDir+"Updated_Text.pdf");
}
```


## 基于正则表达式替换文本

如果你想基于正则表达式替换一些短语，你首先需要使用 TextFragmentAbsorber 找到所有匹配该特定正则表达式的短语。你需要将正则表达式作为参数传递给 TextFragmentAbsorber 构造函数。你还需要创建一个 TextSearchOptions 对象来指定是否使用正则表达式。一旦在 TextFragments 中获得匹配的短语，你需要遍历所有这些短语并根据需要进行更新。最后，你需要使用 Document 对象的 Save 方法保存更新的 PDF。

以下代码片段向你展示了如何基于正则表达式替换文本。

```java
public static void ReplaceTextWithRegularExpression() {
    // 加载 PDF 文件
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // 创建 TextAbsorber 对象以查找输入搜索短语的所有实例
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); 
    // 例如 1999-2000

    // 设置文本搜索选项以指定正则表达式的使用
    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

    // 接受文档第一页的吸收器
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 将提取的文本片段放入集合中
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // 遍历片段
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // 更新文本和其他属性
        textFragment.setText("ABCD-EFGH");
        textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }

    // 保存更新后的 PDF 文件
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


## 替换现有 PDF 文件中的字体

Aspose.PDF for Java 支持在 PDF 文档中替换文本的功能。但是，有时您可能需要仅替换 PDF 文档中使用的字体。因此，与其替换文本，不如仅替换所使用的字体。TextFragmentAbsorber 构造函数的一个重载接受 TextEditOptions 对象作为参数，我们可以使用 TextEditOptions.FontReplace 枚举中的 RemoveUnusedFonts 值来实现我们的需求。

以下代码片段展示了如何替换 PDF 文档中的字体。

```java
public static void ReplaceFonts() {
    // 实例化 Document 对象
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 搜索文本片段并设置编辑选项为移除未使用的字体
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(
            new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

    // 接受文档所有页面的吸收器
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 遍历所有的 TextFragments
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection)
    {
        String fontName = textFragment.getTextState().getFont().getFontName();
        // 如果字体名称是 ArialMT，将字体名称替换为 Arial
        if (fontName.equals("ArialMT")) {
            textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        }
    }

    // 保存更新后的 PDF 文件
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


### 使用非英语（日本）字体替换文本

以下代码片段展示了如何用日文字符替换文本。请注意，要添加日文文本，您需要使用支持日文字体的字体（例如 MSGothic）。

```java
public static void UseNonEnglishFontWhenReplacingText() {

    // 实例化 Document 对象
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 让我们将每个“page”一词替换为某些带有特定字体 TakaoMincho 的日文文本，该字体可能安装在操作系统中
    // 另外，它也可能是另一个支持象形文字的字体
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("page");

    // 创建文本搜索选项的实例
    TextSearchOptions searchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(searchOptions);

    // 为文档的所有页面接受吸收器
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 将提取的文本片段获取到集合中
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    
    // 遍历片段
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // 更新文本和其他属性
        textFragment.setText("ファイル");
        textFragment.getTextState().setFont(FontRepository.findFont("MSGothic"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }
    // 保存更新后的文档
    pdfDocument.save(_dataDir + "Japanese_Text.pdf");
}
```


## 文本替换应自动重新排列页面内容

Aspose.PDF for Java 支持在 PDF 文件中搜索和替换文本的功能。然而，最近一些客户在替换文本时遇到了问题，当特定的 TextFragment 被替换为较小的内容时，结果 PDF 中会显示一些额外的空格，或者在 TextFragment 被替换为较长的字符串时，单词会与现有的页面内容重叠。因此，需要引入一种机制，一旦 PDF 文档中的文本被替换，内容应重新排列。

为了满足上述场景，Aspose.PDF for Java 已得到增强，以便在 PDF 文件中替换文本时不会出现此类问题。以下代码片段显示了如何在 PDF 文件中替换文本并自动重新排列页面内容。

```java
public static void RearrangeContent() {
    // 加载源 PDF 文件
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 创建带有正则表达式的 TextFragment Absorber 对象
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[PDF,Web]");

    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
    
    //您还可以指定 ReplaceAdjustment.WholeWordsHyphenation 选项，以在下一行或当前行换行
    //如果在替换后当前行变得太长或太短：
    //textFragmentAbsorber.getTextReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.WholeWordsHyphenation);

    // 接受文档所有页面的吸收器
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // 将提取的文本片段放入集合中
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // 替换每个 TextFragment
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // 设置被替换文本片段的字体
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        // 设置字体大小
        textFragment.getTextState().setFontSize(10);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
        // 用比占位符更大的字符串替换文本
        textFragment.setText("This is a larger string for the testing of this feature");
    }
    // 保存结果 PDF
    pdfDocument.save(_dataDir + "RearrangeContentsUsingTextReplacement_out.pdf");
}
```


## 在创建 PDF 时渲染可替换符号

可替换符号是文本字符串中的特殊符号，可以在运行时替换为相应的内容。目前，Aspose.PDF 命名空间的新文档对象模型支持的可替换符号有 `$P`、`$p`、`\n`、`\r`。`$p` 和 `$P` 用于在运行时处理页码。`$p` 将被替换为当前段落类所在页面的页码。`$P` 将被替换为文档中的总页数。在将 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) 添加到 PDF 文档的段落集合时，不支持文本中的换行。然而，为了添加带有换行的文本，请使用 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) 与 [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph)：

- 在 TextFragment 中使用 "\r\n" 或 Environment.NewLine 而不是单个 "\n";
- 创建一个 TextParagraph 对象。
 它将添加带有行分隔的文本；
- 使用 TextParagraph.AppendLine 添加 TextFragment；
- 使用 TextBuilder.AppendParagraph 添加 TextParagraph。

```java
public static void RenderingReplaceableSymbols() {
    // 加载 PDF 文件
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    Page page = pdfDocument.getPages().add();

    // 初始化新的 TextFragment，其中包含所需换行符的文本
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // 如有必要，设置文本片段属性
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

    // 创建 TextParagraph 对象
    TextParagraph par = new TextParagraph();

    // 将新的 TextFragment 添加到段落中
    par.appendLine(textFragment);

    // 设置段落位置
    par.setPosition (new Position(100, 600));

    // 创建 TextBuilder 对象
    TextBuilder textBuilder = new TextBuilder(page);
    // 使用 TextBuilder 添加 TextParagraph
    textBuilder.appendParagraph(par);

    _dataDir = _dataDir + "RenderingReplaceableSymbols_out.pdf";
    pdfDocument.save(_dataDir);
}
```

## 页眉/页脚区域中的可替换符号

可替换符号也可以放在 PDF 文件的页眉/页脚部分。请查看以下代码片段，了解如何在页脚部分添加可替换符号的详细信息。

```java
public static void ReplaceableSymbolsInHeaderFooterArea() {
    Document doc = new Document();
    Page page = doc.getPages().add();

    MarginInfo marginInfo = new MarginInfo();
    marginInfo.setTop(90);
    marginInfo.setBottom(50);
    marginInfo.setLeft(50);
    marginInfo.setRight(50);

    // 将 marginInfo 实例分配给 sec1.PageInfo 的 Margin 属性
    page.getPageInfo().setMargin(marginInfo);

    HeaderFooter hfFirst = new HeaderFooter();
    page.setHeader(hfFirst);
    hfFirst.getMargin().setLeft(50);
    hfFirst.getMargin().setRight(50);

    // 实例化一个文本段落，将存储要显示为页眉的内容
    TextFragment t1 = new TextFragment("报告标题");
    t1.getTextState().setFont(FontRepository.findFont("Arial"));
    t1.getTextState().setFontSize(16);
    t1.getTextState().setForegroundColor(Color.getBlack());
    t1.getTextState().setFontStyle(FontStyles.Bold);
    t1.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t1.getTextState().setLineSpacing(5f);
    hfFirst.getParagraphs().add(t1);

    TextFragment t2 = new TextFragment("报告名称");
    t2.getTextState().setFont(FontRepository.findFont("Arial"));
    t2.getTextState().setForegroundColor(Color.getBlack());
    t2.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t2.getTextState().setLineSpacing(5f);
    t2.getTextState().setFontSize(12);
    hfFirst.getParagraphs().add(t2);

    // 为该部分创建一个 HeaderFooter 对象
    HeaderFooter hfFoot = new HeaderFooter();

    // 将 HeaderFooter 对象设置为奇数和偶数页脚
    page.setFooter(hfFoot);
    hfFoot.getMargin().setLeft(50);
    hfFoot.getMargin().setRight(50);

    // 添加一个文本段落，包含当前页码与总页数
    TextFragment t3 = new TextFragment("生成于测试日期");
    TextFragment t4 = new TextFragment("报告名称 ");
    TextFragment t5 = new TextFragment("页 $p 共 $P 页");

    // 实例化一个表对象
    Table tab2 = new Table();

    // 将表添加到所需部分的段落集合中
    hfFoot.getParagraphs().add(tab2);

    // 设置表的列宽
    tab2.setColumnWidths("165 172 165");

    // 在表中创建行，然后在行中创建单元格
    Row row3 = tab2.getRows().add();

    row3.getCells().add();
    row3.getCells().add();
    row3.getCells().add();

    // 将文本的垂直对齐设置为居中对齐
    row3.getCells().get_Item(0).setAlignment(HorizontalAlignment.Left);
    row3.getCells().get_Item(1).setAlignment(HorizontalAlignment.Center);
    row3.getCells().get_Item(2).setAlignment(HorizontalAlignment.Right);

    row3.getCells().get_Item(0).getParagraphs().add(t3);
    row3.getCells().get_Item(1).getParagraphs().add(t4);
    row3.getCells().get_Item(2).getParagraphs().add(t5);

    Table table = new Table();

    table.setColumnWidths("33% 33% 34%");
    table.setDefaultCellPadding(new MarginInfo());
    table.getDefaultCellPadding().setTop(10);
    table.getDefaultCellPadding().setBottom(10);

    // 将表添加到所需部分的段落集合中
    page.getParagraphs().add(table);

    // 使用 BorderInfo 对象设置默认单元格边框
    table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));

    // 使用另一个自定义 BorderInfo 对象设置表格边框
    table.setBorder(new BorderInfo(BorderSide.All, 1f));

    table.setRepeatingRowsCount(1);

    // 在表中创建行，然后在行中创建单元格
    Row row1 = table.getRows().add();

    row1.getCells().add("列1");
    row1.getCells().add("列2");
    row1.getCells().add("列3");
    String CRLF = "\r\n";

    for (int i = 0; i <= 10; i++) {
        Row row = table.getRows().add();
        row.setRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            Cell c1;
            if (c == 2)
                c1 = row.getCells().add(
                        "Aspose.Total for Java 是 Aspose 提供的每个 Java 组件的汇编。它是基于"
                                + CRLF
                                + "每日编译，以确保它包含我们每个 Java 组件的最新版本。"
                                + CRLF
                                + "每日编译，以确保它包含我们每个 Java 组件的最新版本。"
                                + CRLF
                                + "使用 Aspose.Total for Java 开发人员可以创建各种应用程序。");
            else
                c1 = row.getCells().add("项目1" + c);
            c1.setMargin(new MarginInfo());
            c1.getMargin().setLeft(30);
            c1.getMargin().setTop(10);
            c1.getMargin().setBottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```


## 从 PDF 文档中删除所有文本

### 使用操作符删除所有文本

在某些文本操作中，您需要从 PDF 文档中删除所有文本，为此，您通常需要将找到的文本设置为空字符串值。关键是，更改多个文本片段的文本会引发许多检查和文本位置调整操作。这些操作在文本编辑场景中是必不可少的。困难在于，您无法确定在循环处理中将删除多少文本片段。

因此，我们建议在需要删除 PDF 页面上所有文本的场景中使用另一种方法。请考虑以下代码片段，该代码运行速度非常快。

```java
public static void RemoveAllTextUsingOperators() {
    // 打开文档
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 遍历 PDF 文档的所有页面
    for (int i = 1; i <= pdfDocument.getPages().size(); i++) {
        Page page = pdfDocument.getPages().get_Item(i);
        OperatorSelector operatorSelector = new OperatorSelector(new com.aspose.pdf.operators.TextShowOperator());
        // 选择页面上的所有文本
        page.getContents().accept(operatorSelector);
        // 删除所有文本
        page.getContents().delete(operatorSelector.getSelected());
    }
    // 保存文档
    pdfDocument.save(_dataDir + "RemoveAllText_out.pdf");
}
```
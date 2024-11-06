---
title: 向PDF文件添加文本
linktitle: 向PDF文件添加文本
type: docs
weight: 10
url: zh/java/add-text-to-pdf-file/
description: 本文介绍了在Aspose.PDF中处理文本的各个方面。了解如何向PDF添加文本、添加HTML片段或使用自定义OTF字体。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

要向现有PDF文件添加文本：

1. 使用Document对象打开输入PDF。
2. 获取要添加文本的特定页面。
3. 使用输入文本和其他文本属性创建一个TextFragment对象。从要添加文本的特定页面创建的TextBuilder对象允许您使用AppendText方法将TextFragment对象添加到页面中。
4. 调用Document对象的Save方法并保存输出的PDF文件。

## 添加文本

以下代码片段向您展示如何在现有的PDF文件中添加文本。

```java
public static void AddingText() {
    // 加载PDF文件
    Document document = new Document(_dataDir + "sample.pdf");

    // 获取特定页面
    Page pdfPage = document.getPages().get_Item(1);
    // 创建文本片段
    TextFragment textFragment = new TextFragment("Aspose.PDF");
    textFragment.setPosition(new Position(80, 700));

    // 设置文本属性
    textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
    textFragment.getTextState().setFontSize(14);
    textFragment.getTextState().setForegroundColor(Color.getBlue());
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());

    // 创建TextBuilder对象
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // 将文本片段追加到PDF页面
    textBuilder.appendText(textFragment);

    // 保存生成的PDF文档。
    document.save(_dataDir + "AddText_out.pdf");
}
```


## 从流加载字体

以下代码片段展示了如何在向 PDF 文档添加文本时，从 Stream 对象加载字体。

```java
import com.aspose.pdf.*;
import com.aspose.pdf.text.FontTypes;

import java.io.FileInputStream;
import java.io.FileNotFoundException;  
//...
public static void LoadingFontFromStream() throws FileNotFoundException{
    
    String fontFile = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf";

    // 加载输入 PDF 文件
    Document doc = new Document(_dataDir + "input.pdf");
    // 为文档的第一页创建文本构建器对象
    TextBuilder textBuilder = new TextBuilder(doc.getPages().get_Item(1));
    // 创建带有示例字符串的文本片段
    TextFragment textFragment = new TextFragment("Hello world");
    
    if (fontFile != "")
    {
        // 将 TrueType 字体加载到流对象中
        FileInputStream fontStream=new FileInputStream(fontFile);            
        // 为文本字符串设置字体名称
        textFragment.getTextState().setFont (FontRepository.openFont(fontStream, FontTypes.TTF));
        // 指定文本片段的位置
        textFragment.setPosition(new Position(10, 10));
        // 将文本添加到 TextBuilder 以便可以放置在 PDF 文件上
        textBuilder.appendText(textFragment);
        
        _dataDir = _dataDir + "LoadingFontFromStream_out.pdf";
    
        // 保存结果 PDF 文档。
        doc.save(_dataDir); 
    }       
}
```


## 使用TextParagraph添加文字

下面的代码片段展示了如何使用[TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph)类在PDF文档中添加文字。

```java
public static void AddTextUsingTextParagraph() {
    // 打开文档
    Document doc = new Document();
    // 在文档对象的页面集合中添加页面
    Page page = doc.getPages().add();
    TextBuilder builder = new TextBuilder(page);
    // 创建文本段落
    TextParagraph paragraph = new TextParagraph();
    // 设置后续行缩进
    paragraph.setSubsequentLinesIndent (20);
    // 指定添加TextParagraph的位置
    paragraph.setRectangle(new Rectangle(100, 300, 200, 700));
    // 指定自动换行模式
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    // 创建文本片段
    TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
    fragment1.getTextState().setFont (FontRepository.findFont("Times New Roman"));
    fragment1.getTextState().setFontSize (12);
    // 将片段添加到段落
    paragraph.appendLine(fragment1);
    // 添加段落
    builder.appendParagraph(paragraph);

    _dataDir = _dataDir + "AddTextUsingTextParagraph_out.pdf";

    // 保存生成的PDF文档。
    doc.save(_dataDir);        
}
```


## 向 TextSegment 添加超链接

PDF 页面可能包含一个或多个 TextFragment 对象，其中每个 TextFragment 对象可以有一个或多个 TextSegment 实例。为了为 TextSegment 设置超链接，可以在提供 Aspose.Pdf.WebHyperlink 实例的对象时使用 TextSegment 类的 Hyperlink 属性。请尝试使用以下代码片段来完成此要求。

```java
public static void AddHyperlinkToTextSegment() {
    // 创建文档实例
    Document doc = new Document();
    // 向 PDF 文件的页面集合中添加页面
    Page page1 = doc.getPages().add();

    // 创建 TextFragment 实例
    TextFragment tf = new TextFragment("Sample Text Fragment");
    // 为 TextFragment 设置水平对齐
    tf.setHorizontalAlignment(HorizontalAlignment.Right);

    // 创建带有示例文本的 textsegment
    TextSegment segment = new TextSegment(" ... Text Segment 1...");
    // 将 segment 添加到 TextFragment 的 segments 集合中
    tf.getSegments().add(segment);

    // 创建一个新的 TextSegment
    segment = new TextSegment("Link to Google");
    // 将 segment 添加到 TextFragment 的 segments 集合中

    tf.getSegments().add(segment);

    // 为 TextSegment 设置超链接
    segment.setHyperlink(new com.aspose.pdf.WebHyperlink("www.aspose.com"));

    // 设置文本段的前景色
    segment.getTextState().setForegroundColor(com.aspose.pdf.Color.getBlue());

    // 设置文本格式为斜体
    segment.getTextState().setFontStyle(FontStyles.Italic);

    // 创建另一个 TextSegment 对象
    segment = new TextSegment("TextSegment without hyperlink");

    // 将 segment 添加到 TextFragment 的 segments 集合中
    tf.getSegments().add(segment);

    // 将 TextFragment 添加到页面对象的段落集合中
    page1.getParagraphs().add(tf);

    _dataDir = _dataDir + "AddHyperlinkToTextSegment_out.pdf";

    // 保存生成的 PDF 文档。
    doc.save(_dataDir);

}
```


## 使用 OTF 字体

Aspose.PDF for Java 提供了在创建/操作 PDF 文件内容时使用自定义/TrueType 字体的功能，以便文件内容可以使用除默认系统字体以外的字体显示。从 Aspose.PDF for Java 10.4.0 开始，我们提供了对开放字体格式的支持。

```java
public static void UseOTFFont() {
    // 创建新的文档实例
    Document pdfDocument = new Document();
    // 将页面添加到 PDF 文件的页面集合中
    Page page = pdfDocument.getPages().add();
    // 使用示例文本创建 TextFragment 实例
    TextFragment fragment = new TextFragment("OTF 字体中的示例文本");
    // 或者您甚至可以指定系统目录中 OTF 字体的路径
    fragment.getTextState().setFont(FontRepository.openFont("/home/aspose/.fonts/Montserrat-Black.otf"));
    // 指定在 PDF 文件中嵌入字体，以便正确显示，
    // 即使目标机器上未安装/存在特定字体
    fragment.getTextState().getFont().setEmbedded(true);
    // 将 TextFragment 添加到 Page 实例的段落集合中
    page.getParagraphs().add(fragment);
    // 保存生成的 PDF 文档。
    pdfDocument.save(_dataDir + "OTFFont_out.pdf");
}
```


## 使用 DOM 添加 HTML 字符串

Aspose.Pdf.Generator.Text 类包含一个名为 IsHtmlTagSupported 的属性，可以将 HTML 标签/内容添加到 PDF 文件中。添加的内容以原生 HTML 标签呈现，而不是简单的文本字符串。为了在 Aspose.Pdf 命名空间的新文档对象模型 (DOM) 中支持类似功能，引入了 HtmlFragment 类。

[HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlFragment) 实例可用于指定应放置在 PDF 文件中的 HTML 内容。与 TextFragment 类似，HtmlFragment 是段落级对象，可以添加到 Page 对象的段落集合中。以下代码片段展示了使用 DOM 方法将 HTML 内容放置到 PDF 文件中的步骤。

```java
public static void AddingHtmlString() {
    // 实例化 Document 对象
    Document doc = new Document();
    // 向 PDF 文件的页面集合添加一页
    Page page = doc.getPages().add();
    // 用 HTML 内容实例化 HtmlFragment
    HtmlFragment title = new HtmlFragment("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");
    // 设置 MarginInfo 以获取边距详细信息
    MarginInfo Margin = new MarginInfo();
    Margin.setBottom(10);
    Margin.setTop(200);
    // 设置边距信息
    title.setMargin(Margin);
    // 将 HTML Fragment 添加到页面的段落集合中
    page.getParagraphs().add(title);
    // 保存 PDF 文件
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


以下代码片段演示了如何将HTML有序列表添加到文档中的步骤：

```java
public static void AddHTMLOrderedListIntoDocuments() {
    // 实例化Document对象
    Document doc = new Document();
    // 使用相应的HTML片段实例化HtmlFragment对象
    HtmlFragment t = new HtmlFragment(
            "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // 在Pages集合中添加页面
    Page page = doc.getPages().add();
    // 在页面中添加HtmlFragment
    page.getParagraphs().add(t);
    // 保存生成的PDF文件
    doc.save(_dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
}
```

你还可以使用TextState对象设置HTML字符串格式，如下所示：

```java
public static void AddHTMLStringFormatting() {
    // 实例化Document对象
    Document doc = new Document();
    // 向PDF文件的页面集合中添加页面
    Page page = doc.getPages().add();
    // 使用HTML内容实例化HtmlFragment
    HtmlFragment title = new HtmlFragment("<h1><strong>HTML String Demo</strong></h1>");
    TextState textState = new TextState(12);
    textState.setFont(FontRepository.findFont("Calibri"));
    textState.setForegroundColor(Color.getGreen());
    textState.setBackgroundColor(Color.getCoral());
    title.setTextState(textState);

    // 将HTML Fragment添加到页面的段落集合中
    page.getParagraphs().add(title);
    // 保存PDF文件
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


在某些情况下，如果您通过HTML标记设置了一些文本属性值，然后在TextState属性中提供相同的值，它们将通过TextState实例的属性表单覆盖HTML参数。以下代码片段展示了所描述的行为。

```java
public static void AddHTMLUsingDOMAndOverwrite() {
    // 实例化Document对象
    Document doc = new Document();
    // 将页面添加到PDF文件的页面集合
    Page page = doc.getPages().add();
    // 使用HTML内容实例化HtmlFragment
    HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>表格包含文本</i></b></p>");
    // 字体系列将从'Verdana'重置为'Arial'
    title.setTextState(new TextState("Arial Black"));
    title.setTextState(new TextState(20));
    // 设置底部边距信息
    title.getMargin().setBottom(10);
    // 设置顶部边距信息
    title.getMargin().setTop(400);
    // 将HTML片段添加到页面的段落集合
    page.getParagraphs().add(title);
    // 保存PDF文件
    doc.save(_dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
}
```


## 脚注和尾注 (DOM)

脚注通过使用连续的上标数字在您的论文中指示注释。实际的注释是缩进的，可以作为脚注出现在页面底部。

### 添加脚注

在脚注引用系统中，通过以下方式指示引用：

- 在直接跟随源材料的文本行上方放置一个小数字。这个数字被称为注释标识符。它略高于文本行。
- 在页面底部放置相同的数字，后跟您的来源引用。脚注应为数字和按时间顺序排列：第一个引用是1，第二个是2，依此类推。

脚注的优点是读者可以简单地将目光向下移动页面，以发现他们感兴趣的引用来源。

请按照下面指定的步骤创建脚注：

- 创建一个 Document 实例
- 创建一个 Page 对象
- 创建一个 TextFragment 对象

- 创建一个 Note 实例并将其值传递给 TextFragment.FootNote 属性
- 将 TextFragment 添加到页面实例的段落集合中

### 自定义脚注的行样式

以下示例演示了如何将脚注添加到 Pdf 页面的底部并定义自定义行样式。

```java
public static void AddFootNote() {
    // 创建 Document 实例
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("演示");
    t.setFootNote(note);

    // 创建 TextFragment 实例
    TextFragment text = new TextFragment("Hello World");
    // 为 TextFragment 设置脚注值
    text.setFootNote(new Note("测试文本 1 的脚注"));
    // 将 TextFragment 添加到文档第一页的段落集合中
    page.getParagraphs().add(text);
    // 创建第二个 TextFragment
    text = new TextFragment("Aspose.Pdf for Java");
    // 为第二个文本片段设置脚注
    text.setFootNote(new Note("测试文本 2 的脚注"));
    // 将第二个文本片段添加到 PDF 文件的段落集合中
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


我们可以使用 TextState 对象设置脚注标签（注释标识符）格式，如下所示：

```java
public static void AddCustomFootNoteLabel() {
    // 创建 Document 实例
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Demo");
    t.setFootNote(note);

    // 创建 TextFragment 实例
    TextFragment text = new TextFragment("Hello World");
    // 设置 TextFragment 的 FootNote 值
    text.setFootNote(new Note("foot note for test text 1"));
    text.getFootNote().setText("21");
    TextState ts = new TextState();
    ts.setForegroundColor(Color.getBlue());
    ts.setFontStyle(FontStyles.Italic);
    text.getFootNote().setTextState(ts);

    // 将 TextFragment 添加到文档第一页的段落集合中
    page.getParagraphs().add(text);
    // 创建第二个 TextFragment
    text = new TextFragment("Aspose.Pdf for Java");
    // 为第二个文本片段设置 FootNote
    text.setFootNote(new Note("foot note for test text 2"));
    // 将第二个文本片段添加到 PDF 文件的段落集合中
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


### 自定义脚注标签

默认情况下，脚注编号从1开始递增。然而，我们可能需要设置自定义的脚注标签。为了实现这个需求，请尝试使用以下代码片段

```java
public static void CustomFootNote_Label() {
    // 创建 Document 实例
    Document document = new Document();
    // 将页面添加到 PDF 的页面集合中
    Page page = document.getPages().add();
    // 创建 GraphInfo 对象
    GraphInfo graph = new GraphInfo();
    // 设置线宽为 2
    graph.setLineWidth(2);
    // 设置图形对象的颜色
    graph.setColor(Color.getRed());
    // 设置虚线数组值为 3
    graph.setDashArray(new int[] { 3 });
    // 设置虚线相位值为 1
    graph.setDashPhase(1);
    // 将页面的脚注线样式设置为图形
    page.setNoteLineStyle(graph);

    // 创建 TextFragment 实例
    TextFragment text = new TextFragment("Hello World");
    // 设置 TextFragment 的脚注值
    text.setFootNote(new Note("foot note for test text 1"));
    // 指定脚注的自定义标签
    text.getFootNote().setText(" Aspose(2021)");
    // 将 TextFragment 添加到文档第一页的段落集合中
    page.getParagraphs().add(text);

    document.save(_dataDir + "CustomizeFootNoteLabel_out.pdf");
}
```


## 向脚注添加图像和表格

在早期版本中，提供了脚注支持，但它仅适用于 TextFragment 对象。然而，从 Aspose.PDF for Java 10.7.0 版本开始，您还可以向 PDF 文档中的其他对象（例如表格、单元格等）添加脚注。以下代码片段展示了向 TextFragment 对象添加脚注的步骤，然后向脚注部分的段落集合中添加图像和表格对象。

```java
public static void AddingImageAndTableToFootnote() {
    // 创建 Document 实例
    Document document = new Document();
    // 向 PDF 的页面集合中添加页面
    Page page = document.getPages().add();
    // 创建 TextFragment 实例
    TextFragment text = new TextFragment("Hello World");

    page.getParagraphs().add(text);

    text.setFootNote(new Note());
    Image image = new Image();
    image.setFile(_dataDir + "aspose-logo.jpg");
    image.setFixHeight(20);
    text.getFootNote().getParagraphs().add(image);
    TextFragment footNote = new TextFragment("脚注文本");
    footNote.getTextState().setFontSize(20);
    footNote.setInLineParagraph(true);
    text.getFootNote().getParagraphs().add(footNote);
    Table table = new Table();
    table.getRows().add().getCells().add().getParagraphs().add(new TextFragment("行 1 单元格 1"));
    text.getFootNote().getParagraphs().add(table);

    page.getParagraphs().add(text);

    document.save(_dataDir + "AddImageAndTable_out.pdf");
}
```


## 如何创建尾注

尾注是一种源引用，指引读者在论文末尾的特定位置找到引用或提到的信息或文字的来源。当使用尾注时，你引用或改述的句子或总结的材料后面跟着一个上标数字。

以下示例演示如何在 Pdf 页面中添加尾注。

```java
public static void HowToCreateEndNotes() {
    Document doc = new Document();
    // 将页面添加到 PDF 的页面集合中
    Page page = doc.getPages().add();
    // 创建 TextFragment 实例
    TextFragment text = new TextFragment("Hello World");
    // 设置 TextFragment 的尾注值
    text.setEndNote(new Note("sample End note"));
    // 为尾注指定自定义标签
    text.getEndNote().setText(" Aspose(2021)");
    // 将 TextFragment 添加到文档第一页的段落集合中
    page.getParagraphs().add(text);
    // 保存 PDF 文件
    doc.save(_dataDir + "EndNote.pdf");
}
```


## 文本和图像作为内联段落

PDF 文件的默认布局是流布局（从左上到右下）。因此，每个新元素被添加到 PDF 文件时，都是在右下方的流中添加。然而，我们可能需要在同一级别显示各种页面元素，即图像和文本（一个接一个）。一种方法是创建一个表实例，并将两个元素添加到各自的单元格对象中。然而，另一种方法可以是内联段落。通过将图像和文本的 IsInLineParagraph 属性设置为 true，这些段落将出现在其他页面元素的内联中。

以下代码片段向您展示如何在 PDF 文件中添加文本和图像作为内联段落。

```java
 public static void TextAndImageAsInLineParagraph() {
    // 实例化 Document 实例
    Document doc = new Document();
    // 向 Document 实例的页面集合添加页面
    Page page = doc.getPages().add();
    // 创建 TextFragment
    TextFragment text = new TextFragment("Hello World.. ");
    // 将文本片段添加到 Page 对象的段落集合中
    page.getParagraphs().add(text);
    // 创建一个图像实例
    Image image = new Image();
    // 将图像设置为内联段落，以便它出现在
    // 前一个段落对象（TextFragment）之后
    image.setInLineParagraph(true);
    // 指定图像文件路径
    image.setFile(_dataDir + "aspose-logo.jpg");
    // 设置图像高度（可选）
    image.setFixHeight(30);
    // 设置图像宽度（可选）
    image.setFixWidth(100);
    // 将图像添加到页面对象的段落集合中
    page.getParagraphs().add(image);
    // 使用不同的内容重新初始化 TextFragment 对象
    text = new TextFragment(" Hello Again..");
    // 将 TextFragment 设置为内联段落
    text.setInLineParagraph(true);
    // 将新创建的 TextFragment 添加到页面的段落集合中
    page.getParagraphs().add(text);
    
    doc.save(_dataDir + "TextAndImageAsParagraph_out.pdf");
}
```


## 指定添加文本时的字符间距

可以使用 TextFragment 实例或 TextParagraph 对象将文本添加到 PDF 文件的段落集合中，甚至可以使用 TextStamp 类在 PDF 内部添加文本。在添加文本时，我们可能需要为文本对象指定字符间距。为了满足这一要求，引入了一个名为 CharacterSpacing 的新属性。请查看以下方法以满足这一要求。

以下方法显示了在 PDF 文档中添加文本时指定字符间距的步骤。

## 使用 TextBuilder 和 TextFragment

```java
 public static void CharacterSpacing_TextFragment(){
    // 创建文档实例
    Document pdfDocument = new Document();
    // 将页面添加到文档的页面集合中
    Page page = pdfDocument.getPages().add();
    // 创建 TextBuilder 实例
    TextBuilder builder = new TextBuilder(page);
    // 创建包含示例内容的文本片段实例
    TextFragment wideFragment = new TextFragment("Text with increased character spacing");
    wideFragment.getTextState().applyChangesFrom(new TextState("Arial", 12));
    // 为 TextFragment 指定字符间距
    wideFragment.getTextState().setCharacterSpacing(2.0f);
    // 指定 TextFragment 的位置
    wideFragment.setPosition(new Position(100, 650));
    // 将 TextFragment 添加到 TextBuilder 实例中
    builder.appendText(wideFragment);        
    // 保存生成的 PDF 文档。
    pdfDocument.save(_dataDir+ "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
}
```


## 使用 TextBuilder 和 TextParagraph

```java
public static void CharacterSpacing_TextParagraph() {
    // 创建文档实例
    Document pdfDocument = new Document();
    // 将页面添加到文档的页面集合中
    Page page = pdfDocument.getPages().add();
    // 创建 TextBuilder 实例
    TextBuilder builder = new TextBuilder(page);
    // 实例化 TextParagraph 实例
    TextParagraph paragraph = new TextParagraph();
    // 创建 TextState 实例以指定字体名称和大小
    TextState state = new TextState("Arial", 12);
    // 指定字符间距
    state.setCharacterSpacing(1.5f);
    // 将文本附加到 TextParagraph 对象
    paragraph.appendLine("这是一个带有字符间距的段落", state);
    // 指定 TextParagraph 的位置
    paragraph.setPosition(new Position(100, 550));
    // 将 TextParagraph 附加到 TextBuilder 实例
    builder.appendParagraph(paragraph);
    // 保存生成的 PDF 文档。
    pdfDocument.save(_dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
}
```


## 使用文本印章

```java
public static void CharacterSpacing_TextStamp() {
    // 创建 Document 实例
    Document pdfDocument = new Document();
    // 向 Document 的页面集合添加页面
    Page page = pdfDocument.getPages().add();
    // 用示例文本实例化 TextStamp 实例
    TextStamp stamp = new TextStamp("这是带有字符间距的文本印章");
    // 为 Stamp 对象指定字体名称
    stamp.getTextState().setFont(FontRepository.findFont("Arial"));
    // 为 TextStamp 指定字体大小
    stamp.getTextState().setFontSize(12);
    // 指定字符间距为 1f
    stamp.getTextState().setCharacterSpacing (1f);
    // 设置印章的 X 偏移
    stamp.setXIndent(100);
    // 设置印章的 Y 偏移
    stamp.setYIndent(500);
    // 将文本印章添加到页面实例
    stamp.put(page);        
    // 保存生成的 PDF 文档。
    pdfDocument.save(_dataDir+"CharacterSpacingUsingTextStamp_out.pdf");        
}
```

## 创建多列 PDF 文档

在杂志和报纸中，我们大多看到新闻在单个页面上显示为多列，而不是在书籍中，文本段落大多从左到右打印在整页上。
 许多文档处理应用程序，如 Microsoft Word 和 Adobe Acrobat Writer，允许用户在单页上创建多列，然后向其中添加数据。

Aspose.PDF for Java 也提供了在 PDF 文档页面内创建多列的功能。为了创建多列 PDF 文件，我们可以使用 Aspose.Pdf.FloatingBox 类，因为它提供了 ColumnInfo.ColumnCount 属性来指定 FloatingBox 内的列数，我们还可以使用 ColumnInfo.ColumnSpacing 和 ColumnInfo.ColumnWidths 属性来分别指定列间距和列宽。请注意，FloatingBox 是文档对象模型中的一个元素，与相对定位（例如文本、图形、图像等）相比，它可以具有独立的定位。
列间距是指列之间的空间，默认的列间距是1.25厘米。如果未指定列宽，则Aspose.PDF for Java会根据页面大小和列间距自动计算每列的宽度。

下面给出了一个示例，演示如何创建包含图形对象（线条）的两列，并将它们添加到FloatingBox的段落集合中，然后再添加到Page实例的段落集合中。

```java
public static void CreateMultiColumn() {
    Document doc = new Document();
    // 指定PDF文件的左边距信息
    doc.getPageInfo().getMargin().setLeft(40);
    
    // 指定PDF文件的右边距信息
    doc.getPageInfo().getMargin().setRight(40);
    
    Page page = doc.getPages().add();

    com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500, 2);
    
    // 将线条添加到节对象的段落集合中
    page.getParagraphs().add(graph1);

    // 指定线条的坐标
    float[] posArr = new float[] { 1, 2, 500, 2 };
    com.aspose.pdf.drawing.Line l1 = new com.aspose.pdf.drawing.Line(posArr);
    graph1.getShapes().add(l1);
    
    // 创建包含HTML标签的文本字符串变量
    String s = "<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">"
                +"<strong> 如何避免金钱诈骗</<strong> </span>";
    
    // 创建包含HTML文本的文本段落

    HtmlFragment heading_text = new HtmlFragment(s);
    page.getParagraphs().add(heading_text);

    FloatingBox box = new FloatingBox();
    
    // 在节中添加四列
    box.getColumnInfo().setColumnCount(2);
    // 设置列之间的间距
    box.getColumnInfo().setColumnSpacing("5");

    box.getColumnInfo().setColumnWidths("105 105");
    TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
    text1.getTextState().setFontSize (8);
    text1.getTextState().setLineSpacing (2);
    text1.getTextState().setFontSize (10);
    text1.getTextState().setFontStyle (FontStyles.Italic);

    box.getParagraphs().add(text1);
    
    // 创建一个图形对象来绘制线条
    com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50, 10);
    // 指定线条的坐标
    float[] posArr2 = new float[] { 1, 10, 100, 10 };
    com.aspose.pdf.drawing.Line l2 = new com.aspose.pdf.drawing.Line(posArr2);
    graph2.getShapes().add(l2);

    // 将线条添加到节对象的段落集合中
    box.getParagraphs().add(graph2);

    TextFragment text2 = new TextFragment("Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. "
    +"Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue."
    +"Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur "
    +"ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean "
    +"posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. "
    +"Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, "
    +"risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam "
    +"luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, "
    +"sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, "
    +"pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,"
    +"iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus "
    +"mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla."
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,"
    +"iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique"
    +"ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    +"Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. "
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box.getParagraphs().add(text2);

    page.getParagraphs().add(box);

    // 保存PDF文件
    doc.save(_dataDir + "CreateMultiColumnPdf_out.pdf");        
}
```


## 使用自定义制表位

制表位是制表的停止点。在文字处理过程中，每行包含若干个定期间隔放置的制表位（例如，每半英寸）。然而，它们是可以更改的，因为大多数文字处理器允许您设置任意位置的制表位。当您按下 Tab 键时，光标或插入点会跳到下一个制表位，该制表位本身是不可见的。尽管制表位在文本文件中不存在，但文字处理器会跟踪它们，以便能够对 Tab 键做出正确反应。

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) 允许开发人员在 PDF 文档中使用自定义制表位。Aspose.Pdf.Text.TabStop 类用于在 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) 类中设置自定义制表位。

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) 还提供了一些预定义的制表符引导类型，作为一个名为 TabLeaderType 的枚举，其预定义值及其描述如下：

|**Tab Leader Type**|**Description**|
| :- | :- |
|None|无标签引导符|
|Solid|实线标签引导符|
|Dash|虚线标签引导符|
|Dot|点状标签引导符|

这是设置自定义TAB停止位的示例。

```java
public static void CustomTabStops() {
    Document pdfdocument = new Document();
    Page page = pdfdocument.getPages().add();

    com.aspose.pdf.TabStops ts = new com.aspose.pdf.TabStops();
    com.aspose.pdf.TabStop ts1 = ts.add(100);
    ts1.setAlignmentType(TabAlignmentType.Right);
    ts1.setLeaderType (TabLeaderType.Solid);
    
    com.aspose.pdf.TabStop ts2 = ts.add(200);
    ts2.setAlignmentType(TabAlignmentType.Center);
    ts2.setLeaderType (TabLeaderType.Dash);

    com.aspose.pdf.TabStop ts3 = ts.add(300);
    ts3.setAlignmentType(TabAlignmentType.Left);
    ts3.setLeaderType (TabLeaderType.Dot);

    TextFragment header = new TextFragment("这是一个使用TAB停止位形成表格的示例", ts);
    TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data22 "));
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data23"));

    page.getParagraphs().add(header);
    page.getParagraphs().add(text0);
    page.getParagraphs().add(text1);
    page.getParagraphs().add(text2);
    
    pdfdocument.save(_dataDir + "CustomTabStops_out.pdf"); 
}
```


## 如何在 PDF 中添加透明文本

PDF 文件包含图像、文本、图形、附件、注释等对象，在创建 TextFragment 时，可以设置前景色、背景色信息以及文本格式化。Aspose.PDF for Java 支持添加具有 Alpha 颜色通道的文本。以下代码片段展示了如何添加具有透明颜色的文本。

```java
  public static void AddTransparentText() {
    // 创建 Document 实例
    Document pdfdocument = new Document();
    // 在 PDF 文件的页面集合中添加页面
    Page page = pdfdocument.getPages().add();

    // 创建 Graph 对象
    Graph canvas = new Graph(100, 400);
    // 使用特定尺寸创建矩形实例
    com.aspose.pdf.drawing.Rectangle rect = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
    // 从 Alpha 颜色通道创建颜色对象
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;
    Color alphaColor = Color.fromArgb(alpha, red, green, blue);
    rect.getGraphInfo().setFillColor(alphaColor);
    // 将矩形添加到 Graph 对象的形状集合中
    canvas.getShapes().add(rect);
    // 将 graph 对象添加到页面对象的段落集合中
    page.getParagraphs().add(canvas);
    // 设置值以不更改 graph 对象的位置
    canvas.setChangePosition(false);

    // 使用示例值创建 TextFragment 实例
    TextFragment text = new TextFragment(
            "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
    // 从 Alpha 通道创建颜色对象
    alpha = 30;
    alphaColor = Color.fromArgb(alpha, red, green, blue);
    // 设置文本实例的颜色信息
    text.getTextState().setForegroundColor(alphaColor);
    // 将文本添加到页面实例的段落集合中
    page.getParagraphs().add(text);
    
    pdfdocument.save(_dataDir + "AddTransparentText_out.pdf");
}
```


## 为字体指定行间距

每种字体都有一个抽象方框，其高度是同一字号中行与行之间的预期距离。这个方框称为 `em square`，是定义字形轮廓的设计网格。许多输入字体的字母有一些点被放置在字体的 `em square` 边界之外，因此为了正确显示字体，需要使用特殊设置。对象 TextFragment 具有一组可通过方法 [TextState.getFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#getFormattingOptions--) 访问的文本格式选项。此方法返回 [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) 类。
 这个类有一个枚举[LineSpacingMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions.LineSpacingMode)，专为特定字体设计，例如输入字体 "HPSimplified.ttf"。此外，类[TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions)有一个方法[setLineSpacing](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions#setLineSpacing-int-)，类型为LineSpacingMode。您只需将LineSpacing设置为LineSpacingMode.FullSize。获取字体正确显示的代码片段如下所示：

```java
public static void SpecifyLineSpacingForFonts() {
    String fontFile = _dataDir + "hp-simplified.ttf";
    // 加载输入的PDF文件
    Document doc = new Document();
    // 创建TextFormattingOptions与LineSpacingMode.FullSize
    TextFormattingOptions formattingOptions = new TextFormattingOptions();
    formattingOptions.setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);

    // 为文档第一页创建文本构建器对象
    // TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
    // 使用示例字符串创建文本片段
    TextFragment textFragment = new TextFragment("Hello world");

    // 将TrueType字体加载到流对象中
    FileInputStream fontStream;
    try {
        fontStream = new FileInputStream(fontFile);
    } catch (FileNotFoundException e) {
        e.printStackTrace();
        return;
    }

    // 设置文本字符串的字体名称
    textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
    // 为文本片段指定位置
    textFragment.setPosition(new Position(100, 600));
    // 将当前片段的TextFormattingOptions设置为预定义（指向LineSpacingMode.FullSize）
    textFragment.getTextState().setFormattingOptions(formattingOptions);
    // 将文本添加到TextBuilder，以便可以将其放置在PDF文件上
    // textBuilder.AppendText(textFragment);
    Page page = doc.getPages().add();
    page.getParagraphs().add(textFragment);

    // 保存生成的PDF文档
    doc.save(_dataDir + "SpecifyLineSpacing_out.pdf");
}
```

## 动态获取文本宽度

有时，需要动态获取文本宽度。Aspose.PDF for Java 包含两个用于字符串宽度测量的方法。您可以调用 com.aspose.pdf.Font 或 com.aspose.pdf.TextState 类（或两者）的 [MeasureString](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState#measureString--) 方法。下面的代码片段展示了如何使用此功能。

```java
public static void GetTextWidthDynamicaly() {
    Font font = FontRepository.findFont("Arial");
    TextState ts = new TextState();
        ts.setFont(font);
        ts.setFontSize(14);
        if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001)
            System.out.println("Unexpected font string measure!");

        if (Math.abs(ts.measureString("z") - 7.0) > 0.001)
        System.out.println("Unexpected font string measure!");

        for (char c = 'A'; c <= 'z'; c++)
        {
            double fnMeasure = font.measureString(String.valueOf(c), 14);
            double tsMeasure = ts.measureString(String.valueOf(c));

            if (Math.abs(fnMeasure - tsMeasure) > 0.001)
                System.out.println("Font and state string measuring doesn't match!");
        }
}
```
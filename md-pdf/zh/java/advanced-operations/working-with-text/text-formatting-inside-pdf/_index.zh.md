---
title: PDF 中的文本格式化 
linktitle: PDF 中的文本格式化
type: docs
weight: 30
url: /java/text-formatting-inside-pdf/
description: 本页解释了如何在 PDF 文件中格式化文本。这包括添加行缩进、添加文本边框、添加下划线文本、在添加的文本周围添加边框、浮动框内容的文本对齐等。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 如何向 PDF 添加行缩进

Aspose.PDF for Java 为 [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) 类提供了 SubsequentLinesIndent 属性。可以在使用 TextFragment 和段落集合的 PDF 生成场景中指定行缩进。

请使用以下代码片段来使用该属性：

```java
public static void AddLineIndentToPDF() {
        // 创建新的文档对象
        Document document = new Document();
        Page page = document.getPages().add();

        TextFragment text = new TextFragment(
                "A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

        // 初始化文本片段的 TextFormattingOptions，并指定
        // SubsequentLinesIndent 值
        TextFormattingOptions textOptions = new TextFormattingOptions();
        textOptions.setSubsequentLinesIndent(20);
        text.getTextState().setFormattingOptions(textOptions);

        page.getParagraphs().add(text);

        text = new TextFragment("Line2");
        page.getParagraphs().add(text);

        text = new TextFragment("Line3");
        page.getParagraphs().add(text);

        text = new TextFragment("Line4");
        page.getParagraphs().add(text);

        text = new TextFragment("Line5");
        page.getParagraphs().add(text);

        document.save(_dataDir + "SubsequentIndent_out.pdf");
    }
```


## 如何添加文字边框

以下代码片段展示了如何使用 TextBuilder 并设置 TextState 的 DrawTextRectangleBorder 方法为文本添加边框：

```java
public static void AddTextBorder() {
    // 创建新的文档对象
    Document pdfDocument = new Document();
    // 获取特定页面
    Page pdfPage = pdfDocument.getPages().add();
    // 创建文本片段
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition(new Position(100, 600));
    // 设置文本属性
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());
    // 使用 setStrokingColor 为文本矩形周围绘制边框（描边）
    textFragment.getTextState().setStrokingColor (Color.getDarkRed());
    // 使用 setDrawTextRectangleBorder 方法将值设置为 true
    textFragment.getTextState().setDrawTextRectangleBorder(true);
    TextBuilder tb = new TextBuilder(pdfPage);
    tb.appendText(textFragment);
    // 保存文档
    pdfDocument.save(_dataDir + "PDFWithTextBorder_out.pdf");
}
```


## 如何添加下划线文本

以下代码片段展示了在创建新的PDF文件时如何添加下划线文本。

```java
public static void AddUnderlineText(){
    // 创建文档对象
    Document pdfDocument = new Document();
    // 向PDF文档添加页面
    Page page = pdfDocument.getPages().add();
    // 为第一页创建TextBuilder
    TextBuilder tb = new TextBuilder(page);
    // 带有示例文本的TextFragment
    TextFragment fragment = new TextFragment("带下划线装饰的文本");
    // 设置TextFragment的字体
    fragment.getTextState().setFont (FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize (10);
    // 将文本格式设置为下划线
    fragment.getTextState().setUnderline(true);
    // 指定TextFragment需要放置的位置
    fragment.setPosition (new Position(10, 800));
    // 将TextFragment添加到PDF文件
    tb.appendText(fragment);

    // 保存生成的PDF文档。
    pdfDocument.save(_dataDir + "AddUnderlineText_out.pdf");
}
```


## 如何在添加的文本周围添加边框

您可以控制添加文本的外观和感觉。下面的示例显示了如何通过在添加的文本周围绘制一个矩形来添加边框。了解更多关于 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 类的信息。

```java
public static void AddBorderAroundAddedText() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir + "input.pdf");
    LineInfo lineInfo = new LineInfo();
    lineInfo.setLineWidth(2);
    lineInfo.setVerticeCoordinate (new float[] { 0, 0, 100, 100, 50, 100 });
    lineInfo.setVisibility(true);
    editor.createPolygon(lineInfo, 1, new java.awt.Rectangle(0, 0, 0, 0), "");

    // 保存生成的 PDF 文档。
    editor.save(_dataDir + "AddingBorderAroundAddedText_out.pdf");
}
```

## 如何添加换行符

TextFragment 不支持文本内部的换行符。
 然而，为了添加带有换行符的文本，请使用 TextFragment 和 TextParagraph：

- 在 TextFragment 中使用 "\r\n" 或 Environment.NewLine，而不是单个“\n”；
- 创建 TextParagraph 对象。它将添加带有行拆分的文本；
- 使用 TextParagraph.AppendLine 添加 TextFragment；
- 使用 TextBuilder.AppendParagraph 添加 TextParagraph。
请使用下面的代码片段。

```java
public static void AddNewLineFeed() {        
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    // 初始化包含所需换行符标记的文本的新 TextFragment
    TextFragment textFragment = new TextFragment("申请人姓名: " + System.lineSeparator() + " Joe Smoe");

    // 如有必要，设置文本片段属性
    textFragment.getTextState().setFontSize (12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());

    // 创建 TextParagraph 对象
    TextParagraph par = new TextParagraph();

    // 将新的 TextFragment 添加到段落
    par.appendLine(textFragment);

    // 设置段落位置
    par.setPosition (new Position(100, 600));

    // 创建 TextBuilder 对象
    TextBuilder textBuilder = new TextBuilder(page);
    // 使用 TextBuilder 添加 TextParagraph
    textBuilder.appendParagraph(par);

    // 保存生成的 PDF 文档。
    pdfDocument.save(_dataDir + "AddNewLineFeed_out.pdf");
}
```

## 如何添加删除线文本

TextState 类提供了设置 PDF 文档中放置的 TextFragments 格式的功能。您可以使用此类将文本格式设置为粗体、斜体、下划线，并且从此版本开始，API 提供了将文本格式标记为删除线的功能。请尝试使用以下代码片段添加带有删除线格式的 TextFragment。

请使用完整的代码片段：

```java
public static void AddStrikeOutText(){
    // 打开文档
    Document pdfDocument = new Document();
    // 获取特定页面
    Page pdfPage = (Page)pdfDocument.getPages().add();

    // 创建文本片段
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition (new Position(100, 600));

    // 设置文本属性
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());
    // 使用 setStrikeOut 方法启用删除线文本
    textFragment.getTextState().setStrikeOut(true);
    // 将文本标记为粗体
    textFragment.getTextState().setFontStyle(FontStyles.Bold);

    // 创建 TextBuilder 对象
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // 将文本片段追加到 PDF 页面
    textBuilder.appendText(textFragment);

    // 保存生成的 PDF 文档。
    pdfDocument.save(_dataDir + "AddStrikeOutText_out.pdf");        
}
```


## 应用渐变着色到文本

在文本编辑场景中，API 的文本格式化功能已得到进一步增强，现在您可以在 PDF 文档中添加带有图案颜色空间的文本。com.aspose.pdf.Color 类通过引入新方法 `setPatternColorSpace` 得到了进一步增强，该方法可用于指定文本的着色颜色。这个新方法为文本添加了不同的渐变着色，例如：轴向着色，径向（类型 3）着色，如以下代码片段所示：

```java
public static void ApplyGradientShading() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));

    // 使用图案颜色空间创建新颜色
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```


为了应用径向渐变，您可以在上面的代码片段中使用`setPatternColorSpace`方法等于`GradientRadialShading(startingColor, endingColor)`。

```java
public static void ApplyGradientShadingRadial() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));

    // 使用图案颜色空间创建新颜色
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

## 如何将文本对齐到浮动内容

Aspose.PDF支持为浮动框元素内的内容设置文本对齐。
 Aspose.Pdf.FloatingBox 实例的对齐属性可用于实现这一点，如以下代码示例所示。

```java
public static void AlignTextToFloatContent() {
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    FloatingBox floatBox = new FloatingBox(100, 100);
    floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
    floatBox.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
    floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
    
    page.getParagraphs().add(floatBox);

    FloatingBox floatBox1 = new FloatingBox(100, 100);
    floatBox1.setVerticalAlignment(VerticalAlignment.Center);
    floatBox1.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox1.getParagraphs().add(new TextFragment("FloatingBox_center"));
    floatBox1.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox1);

    FloatingBox floatBox2 = new FloatingBox(100, 100);
    floatBox2.setVerticalAlignment(VerticalAlignment.Top);
    floatBox2.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox2.getParagraphs().add(new TextFragment("FloatingBox_top"));
    floatBox2.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox2);

    pdfDocument.save(_dataDir + "FloatingBox_alignment_review_out.pdf");        
}
```
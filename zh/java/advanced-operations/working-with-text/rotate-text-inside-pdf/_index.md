---
title: 在 PDF 中旋转文本
linktitle: 在 PDF 中旋转文本
type: docs
weight: 50
url: zh/java/rotate-text-inside-pdf/
description: 学习不同方式在 PDF 中旋转文本。Aspose.PDF 允许您以任意角度旋转文本，旋转文本片段或整个段落。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用旋转属性在 PDF 中旋转文本

通过使用 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) 类的 [setRotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#setRotation-double-) 方法，您可以在不同角度旋转文本。文本旋转可以用于文档生成的不同场景。您可以指定旋转角度（以度为单位）来根据需要旋转文本。请查看以下不同场景，您可以在其中实现文本旋转。

## 使用 TextFragment 和 TextBuilder 实现旋转

```java
public class ExampleRotateText {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ImplementRotationUsingTextFragmentAndTextBuilder() {

        // 初始化文档对象
        Document pdfDocument = new Document();
        // 获取特定页面
        Page pdfPage = pdfDocument.getPages().add();
        // 创建文本片段
        TextFragment textFragment1 = new TextFragment("main text");
        textFragment1.setPosition(new Position(100, 600));

        // 设置文本属性
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        // 创建旋转的文本片段
        TextFragment textFragment2 = new TextFragment("rotated text");
        textFragment2.setPosition(new Position(200, 600));
        // 设置文本属性
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(45);

        // 创建旋转的文本片段
        TextFragment textFragment3 = new TextFragment("rotated text");
        textFragment3.setPosition(new Position(300, 600));

        // 设置文本属性
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(90);

        // 创建 TextBuilder 对象
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // 将文本片段添加到 PDF 页面
        textBuilder.appendText(textFragment1);
        textBuilder.appendText(textFragment2);
        textBuilder.appendText(textFragment3);

        // 保存文档
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated1_out.pdf");
    }
}
```


## 实现使用 TextParagraph 和 TextBuilder 进行旋转（旋转的片段）

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    // 初始化文档对象
    Document pdfDocument = new Document();
    // 获取特定页面
    Page pdfPage = (Page) pdfDocument.getPages().add();
    TextParagraph paragraph = new TextParagraph();
    paragraph.setPosition(new Position(200, 600));
    // 创建文本片段
    TextFragment textFragment1 = new TextFragment("rotated text");
    // 设置文本属性
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // 设置旋转
    textFragment1.getTextState().setRotation(45);

    // 创建文本片段
    TextFragment textFragment2 = new TextFragment("main text");
    // 设置文本属性
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // 创建文本片段
    TextFragment textFragment3 = new TextFragment("another rotated text");
    // 设置文本属性
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // 设置旋转
    textFragment3.getTextState().setRotation(-45);

    // 将文本片段附加到段落
    paragraph.appendLine(textFragment1);
    paragraph.appendLine(textFragment2);
    paragraph.appendLine(textFragment3);
    // 创建 TextBuilder 对象
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // 将文本段落附加到 PDF 页面
    textBuilder.appendParagraph(paragraph);
    // 保存文档
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated2_out.pdf");
}
```


## 实现使用 TextFragment 和 Page.Paragraphs 的旋转

```csharp
public static void ImplementRotationUsingTextFragmentAndPageParagraphs() {
    // 初始化文档对象
    Document pdfDocument = new Document();
    // 获取特定页面
    Page pdfPage = (Page) pdfDocument.getPages().add();
    // 创建文本片段
    TextFragment textFragment1 = new TextFragment("main text");
    // 设置文本属性
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // 创建文本片段
    TextFragment textFragment2 = new TextFragment("rotated text");

    // 设置文本属性
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // 设置旋转
    textFragment2.getTextState().setRotation(315);

    // 创建文本片段
    TextFragment textFragment3 = new TextFragment("rotated text");
    // 设置文本属性
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // 设置旋转
    textFragment3.getTextState().setRotation(270);
    pdfPage.getParagraphs().add(textFragment1);
    pdfPage.getParagraphs().add(textFragment2);
    pdfPage.getParagraphs().add(textFragment3);

    // 保存文档
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated3_out.pdf");
    }
```


## 使用 TextParagraph 和 TextBuilder 实现旋转（整个段落旋转）

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder() {

    // 初始化文档对象
    Document pdfDocument = new Document();
    // 获取特定页面
    Page pdfPage = pdfDocument.getPages().add();
    for (int i = 0; i < 4; i++) {
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));
        // 指定旋转
        paragraph.setRotation(i * 90 + 45);
        // 创建文本片段
        TextFragment textFragment1 = new TextFragment("段落文本");
        // 创建文本片段
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment1.getTextState().setForegroundColor(Color.getBlue());

        // 创建文本片段
        TextFragment textFragment2 = new TextFragment("第二行文本");
        // 设置文本属性
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment2.getTextState().setForegroundColor(Color.getBlue());

        // 创建文本片段
        TextFragment textFragment3 = new TextFragment("还有更多文本...");
        // 设置文本属性
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment3.getTextState().setForegroundColor(Color.getBlue());
        textFragment3.getTextState().setUnderline(true);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);
        // 创建 TextBuilder 对象
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // 将文本片段添加到 PDF 页面
        textBuilder.appendParagraph(paragraph);
    }
    // 保存文档
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated4_out.pdf");
}
```
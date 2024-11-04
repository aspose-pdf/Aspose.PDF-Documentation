---
title: 将PDF转换为Java中的Microsoft Word文档
linktitle: 将PDF转换为Word
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2021-11-19"
description: 使用Aspose.PDF for Java轻松全面地控制将PDF文件转换为DOC和DOCX格式。了解更多如何调整PDF到Microsoft Word文档的转换。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概述

本文解释了如何使用Java将PDF转换为Word。代码非常简单，只需将PDF加载到Document类并将其保存为输出的Microsoft Word DOC或DOCX格式。它涵盖以下主题

- [Java PDF到Word](#convert-pdf-to-doc)
- [Java PDF到DOC](#convert-pdf-to-doc)
- [Java PDF到DOCX](#convert-pdf-to-docx)
- [Java将PDF转换为Word](#convert-pdf-to-docx)
- [Java将PDF转换为DOC](#convert-pdf-to-doc)
- [Java将PDF转换为DOCX](#convert-pdf-to-docx)
- [Java如何将PDF文件转换为Word DOC](#convert-pdf-to-doc)或[Word DOCX](#convert-pdf-to-docx)

- [Java PDF到Word库、API或代码以编程方式从PDF保存、生成或创建Word文档](#convert-pdf-to-docx)

## 转换 PDF 为 DOC

最受欢迎的功能之一是将 PDF 转换为 Microsoft Word DOC，使内容易于操作。Aspose.PDF for Java 允许您将 PDF 文件转换为 DOC。

**Aspose.PDF for Java** 可以从头创建 PDF 文档，是更新、编辑和操作现有 PDF 文档的强大工具包。一个重要功能是将页面和整个 PDF 文档转换为图像。另一个受欢迎的功能是将 PDF 转换为 Microsoft Word DOC，使内容易于操作。（大多数用户无法编辑 PDF 文档，但可以轻松处理 Microsoft Word 中的表格、文本和图像。）

为了简单易懂，Aspose.PDF for Java 提供了一个两行代码，用于将源 PDF 文件转换为 DOC 文件。

以下 Java 代码片段显示了将 PDF 文件转换为 DOC 格式的过程。

1. 创建一个 [Document](https://reference.aspose.com/page/java/com.aspose.page/document) 对象实例，使用源 PDF 文档。
2. 通过调用 **Document.save()** 方法将其保存为 **SaveFormat.Doc** 格式。

```java
public static void convertPDFtoWord() {
    // 打开源 PDF 文档
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // 将文件保存为 MS 文档格式
    document.save(DATA_DIR + "PDFToDOC_out.doc", SaveFormat.Doc);
    document.close();
}
```

## 使用 DocSaveOptions 类

[DocSaveOptions 类](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) 提供了许多属性，可以改善将 PDF 文件转换为 DOC 格式的过程。在这些属性中，Mode 允许您指定 PDF 内容的识别模式。您可以为此属性指定 RecognitionMode 枚举中的任何值。每个值都有特定的优点和限制：

- [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) 模式速度快，并且有助于保持 PDF 文件的原始外观，但生成的文档的可编辑性可能有限。
 每个在原始 PDF 中视觉上分组的文本块在输出文档中被转换为文本框。这实现了与原始文档的最大相似性，因此输出文档看起来很好，但它完全由文本框组成，这可能会使在 Microsoft Word 中进行编辑变得困难。

- Flow 是完整识别模式， 引擎执行分组和多级分析以根据作者的意图恢复原始文档，同时生成一个易于编辑的文档。限制是输出文档可能看起来与原始文档不同。

- RelativeHorizontalProximity 属性可用于控制文本元素之间的相对接近度，意味着距离是以字体大小为标准的。较大的字体可能在音节之间有较大的距离，仍然被视为一个整体。它被指定为字体大小的百分比，例如，1 = 100%。这意味着两个12pt的字符相隔12pt是接近的。

- RecognitionBullets 用于在转换过程中开启项目符号识别。
```java
public static void convertPDFtoWordDocAdvanced() {
    Path pdfFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.pdf");
    Path docFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.doc");
    Document document = new Document(pdfFile.toString());
    DocSaveOptions saveOptions = new DocSaveOptions();

    // 指定输出格式为DOC
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    // 设置识别模式为Flow
    saveOptions.setMode(DocSaveOptions.RecognitionMode.Flow);

    // 设置水平接近度为2.5
    saveOptions.setRelativeHorizontalProximity(2.5f);

    // 在转换过程中启用识别项目符号的值
    saveOptions.setRecognizeBullets(true);

    document.save(docFile.toString(), saveOptions);
    document.close();
}
```

{{% alert color="success" %}}
**尝试在线将PDF转换为DOC**

Aspose.PDF for Java 为您提供在线免费应用程序 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，您可以尝试调查其功能和工作质量。

[![Convert PDF to DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 转换 PDF 为 DOCX

DocFormat 枚举还提供选择 DOCX 作为 Word 文档输出格式的选项。要将源 PDF 文件渲染为 DOCX 格式，请使用下面指定的代码片段。

## 如何将 PDF 转换为 DOCX

以下 Java 代码片段展示了将 PDF 文件转换为 DOCX 格式的过程。

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/page/java/com.aspose.page/document) 对象的实例。
2. 通过调用 **Document.save()** 方法将其保存为 **SaveFormat.DocX** 格式。

```java
public static void convertPDFtoWord_DOCX_Format() {
    // 打开源 PDF 文档
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // 保存生成的 DOC 文件
    document.save(DATA_DIR + "saveOptionsOutput_out.doc", SaveFormat.DocX);
    document.close();
}
```

[DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) 类有一个名为 Format 的属性，提供了指定生成文档格式（即 DOC 或 DOCX）的功能。
 为了将 PDF 文件转换为 DOCX 格式，请从 DocSaveOptions.DocFormat 枚举中传递 Docx 值。

请查看以下代码片段，该代码提供了使用 Java 将 PDF 文件转换为 DOCX 格式的功能。

```java
public static void convertPDFtoWord_Advanced_DOCX_Format() {
    // 打开源 PDF 文档
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");

    // 实例化 DocSaveOptions 对象
    DocSaveOptions saveOptions = new DocSaveOptions();
    // 指定输出格式为 DOCX
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    // 设置其他 DocSaveOptions 参数
    // ....

    // 以 docx 格式保存文档
    document.save("ConvertToDOCX_out.docx", saveOptions);
    document.close();
}
```

{{% alert color="warning" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for Java 为您提供在线免费应用程序 ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，您可以尝试研究其功能和质量。
[![Aspose.PDF 转换 PDF 到 DOCX 免费应用](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}
---
title: 将PDF文件转换为其他格式
linktitle: 将PDF转换为其他格式
type: docs
weight: 90
url: zh/java/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: 本主题展示了如何使用Aspose.PDF将PDF文件转换为其他文件格式。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将PDF转换为EPUB

{{% alert color="success" %}}
**尝试在线将PDF转换为EPUB**

Aspose.PDF for Java为您提供了一个在线免费应用程序["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将PDF转换为EPUB](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>**（电子出版物的缩写）是国际数字出版论坛（IDPF）的一种免费开放的电子书标准。
 文件扩展名为.epub。EPUB 设计用于可重排内容，这意味着 EPUB 阅读器可以针对特定显示设备优化文本。EPUB 还支持固定布局内容。该格式旨在作为出版商和转换公司可以在内部使用的单一格式，以及用于分发和销售。它取代了 Open eBook 标准。

Aspose.PDF for Java 支持将 PDF 文档转换为 EPUB 格式的功能。Aspose.PDF for Java 有一个名为 [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) 的类，可以用作 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) 方法的第二个参数，以生成 EPUB 文件。请尝试使用以下代码片段来完成此要求。

```java
// 加载 PDF 文档
Document document = new Document(DATA_DIR + "PDFToEPUB.pdf");
// 实例化 Epub 保存选项
EpubSaveOptions options = new EpubSaveOptions();
// 指定内容的布局
options.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
// 保存 ePUB 文档
document.save(DATA_DIR + "PDFToEPUB_out.epub", options);
document.close();
```

## 将 PDF 转换为 LaTeX/TeX

**Aspose.PDF for Java** 支持将 PDF 转换为 LaTeX/TeX。 LaTeX 文件格式是一种带有特殊标记的文本文件格式，用于基于 TeX 的文档准备系统中的高质量排版。

要将 PDF 文件转换为 TeX，Aspose.PDF 提供了类 [TeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXSaveOptions)，该类提供了 `setOutDirectoryPath` 方法用于在转换过程中保存临时图像。

以下代码片段展示了使用 Java 将 PDF 文件转换为 TEX 格式的过程。

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX.pdf").toString();
String texDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX_out.tex").toString();

// 创建文档对象
Document document = new Document(documentFileName);

// 实例化 LaTex 保存选项
TeXSaveOptions saveOptions = new TeXSaveOptions();

// 指定输出目录
String pathToOutputDirectory = DATA_DIR.toString();

// 设置保存选项对象的输出目录路径
saveOptions.setOutDirectoryPath(pathToOutputDirectory);

// 将 PDF 文件保存为 LaTex 格式
document.save(texDocumentFileName, saveOptions);
document.close();
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for Java 为您提供在线免费应用程序 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 LaTeX/TeX 免费应用程序](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## 将 PDF 转换为文本

**Aspose.PDF for Java** 支持将整个 PDF 文档和单个页面转换为文本文件。

### 将整个 PDF 文档转换为文本文件

您可以使用 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 类的 Visit 方法将 PDF 文档转换为 TXT 文件。

下面的代码片段解释了如何从所有页面提取文本。

```java
// 打开文档
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// 加载 PDF 文档
Document document = new Document(pdfFileName);
TextAbsorber ta = new TextAbsorber();
ta.visit(document);
// 将提取的文本保存到文本文件中
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为文本**

Aspose.PDF for Java 为您提供免费在线应用程序 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，您可以在其中尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到文本的免费应用程序](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### 将 PDF 页面转换为文本文件

您可以使用 Aspose.PDF for Java 将 PDF 文档转换为 TXT 文件。您应该使用 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 类的 Visit 方法来解决此任务。

以下代码片段说明了如何从特定页面中提取文本。

```java
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// 加载 PDF 文档
Document document = new Document(pdfFileName);

TextAbsorber ta = new TextAbsorber();
int[] pages = new int[] { 1, 3, 4 };

for (int page : pages) {
    ta.visit(document.getPages().get_Item(page));
}

// 将提取的文本保存到文本文件中
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
document.close();
```


## 将 PDF 转换为 XPS

**Aspose.PDF for Java** 提供了将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式的可能性。让我们尝试使用提供的代码片段将 PDF 文件转换为 Java 中的 XPS 格式。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for Java 为您提供在线免费应用程序 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 XPS](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS 文件类型主要与 Microsoft Corporation 的 XML Paper Specification 相关联。XML Paper Specification（XPS），前身代号为 Metro，并包含下一代打印路径（NGPP）营销概念，是 Microsoft 将文档创建和查看集成到 Windows 操作系统中的一项计划。

为了将 PDF 文件转换为 XPS，Aspose.PDF 拥有 [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) 类，该类用作 Document.save(..) 构造函数的第二个参数以生成 XPS 文件。
 以下代码片段显示了将PDF文件转换为XPS格式的过程。

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "sample.pdf").toString();
String xpsDocumentFileName = Paths.get(DATA_DIR.toString(), "sample-res-xps.xps").toString();

// 创建Document对象
Document document = new Document(documentFileName);

// 实例化XPS保存选项
XpsSaveOptions saveOptions = new XpsSaveOptions();

// 以XML格式保存输出
document.save(xpsDocumentFileName, saveOptions);
document.close();
```
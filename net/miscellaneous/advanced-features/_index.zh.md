---
title: 高级功能
type: docs
weight: 210
url: /net/advanced-features/
---

## 将 Pdf 发送到浏览器以下载

有时在开发 ASP.NET 应用程序时，您需要将 PDF 文件发送到网页浏览器以供下载，而无需物理保存它们。为了实现这一点，您可以在生成 PDF 文档后将其保存到 MemoryStream 对象中，并将该 MemoryStream 中的字节传递给 Response 对象。这样做将使浏览器下载生成的 PDF 文档。

以下代码片段演示了上述功能：

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-Examples.Web-SendPdfToBrowserForDownload.aspx-1.cs" >}}

## 从 PDF 文件中提取嵌入文件

在处理 PDF 格式文件的高级功能方面，Aspose.PDF 表现突出。它提取嵌入文件的方式比其他提供此功能的工具要好得多。

使用 Aspose.PDF for .NET，您可以有效地提取任何嵌入文件，无论是嵌入字体、图像、视频还是音频。
使用 Aspose.PDF for .NET，您可以高效地提取任何嵌入式文件，包括嵌入式字体、图像、视频或音频。

以下代码片段提取 PDF 文件中的所有嵌入式文件：

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-DocumentConversion-PDFToXML-PDFToXML.cs" >}}

## 使用 Latex 脚本添加数学表达式

使用 Aspose.PDF，您可以使用 latex 脚本在 PDF 文档中添加数学表达式/公式。以下示例展示了如何以两种不同方式使用此功能，在表格单元格中添加数学公式：

### 无前导代码和文档环境

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript-WithoutPreambleanddocument.cs" >}}

### 带前导代码和文档环境

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript2-WithPreambleanddocument.cs" >}}

### 支持 Latex 标签
### 支持 Latex 标签

align 环境在 amsmath 包中定义，proof 环境在 amsthm 包中定义。因此，您需要在文档前言中使用 \usepackage 命令指定这些包。这意味着您必须将 LaTeX 文本包含在文档环境中，如下面的代码示例所示。

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Text-UseLatexScript3-UseLatexScript3.cs" >}}

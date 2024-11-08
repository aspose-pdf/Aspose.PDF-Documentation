---
title: 在C#中合并PDF文档
linktitle: 合并PDF文档
type: docs
weight: 20
url: /zh/net/concatenate-pdf-documents/
description: 本节解释如何使用PdfFileEditor类通过Aspose.PDF Facades合并PDF文档。
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-06-05"
---

## **概述**

本文解释如何使用C#合并、组合或连接不同的PDF文件为单个PDF。它涵盖了以下主题，例如

- [C# 合并PDF文件](#concatenate-pdf-files-using-file-paths)
- [C# 组合PDF文件](#concatenate-pdf-files-using-file-paths)

- [C# 将多个PDF文件合并为一个PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# 合并多个 PDF 文件为一个 PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# 合并文件夹中的所有 PDF 文件](#concatenating-all-pdf-files-in-particular-folder)
- [C# 合并文件夹中的所有 PDF 文件](#concatenating-all-pdf-files-in-particular-folder)
- [C# 使用文件路径合并 PDF 文件](#concatenate-pdf-files-using-file-paths)
- [C# 使用流合并 PDF 文件](#concatenate-array-of-pdf-files-using-streams)
- [C# 合并文件夹中的所有 PDF 文件](#concatenate-pdf-files-in-folder)

## 使用文件路径合并 PDF 文件

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 是 [Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 中的类，允许您合并多个 PDF 文件。 你不仅可以使用 FileStreams 来连接文件，还可以使用 MemoryStreams。在本文中，将解释如何使用 MemoryStreams 来连接文件，并通过代码片段进行展示。

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类的 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法可以用来连接两个 PDF 文件。[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法允许您传递三个参数：第一个输入 PDF，第二个输入 PDF 和输出 PDF。最终的输出 PDF 包含两个输入 PDF 文件。

以下 C# 代码片段展示了如何使用文件路径连接 PDF 文件。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

在某些情况下，当有大量大纲时，用户可以通过将 CopyOutlines 设置为 false 来禁用它们，从而提高连接的性能。
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-CopyOutline.cs" >}}

## 使用内存流连接多个PDF文件

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类的 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法将源PDF文件和目标PDF文件作为参数。这些参数可以是磁盘上PDF文件的路径，也可以是内存流。现在，对于这个示例，我们将首先创建两个文件流以从磁盘读取PDF文件。然后我们将这些文件转换为字节数组。PDF文件的这些字节数组将被转换为内存流。一旦我们从PDF文件中获取到内存流，我们就可以将它们传递给连接方法并合并到一个单一的输出文件中。

以下C#代码片段向您展示了如何使用内存流连接多个PDF文件：

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## 使用文件路径连接PDF文件数组

如果您想连接多个PDF文件，您可以使用[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)方法的重载，它允许您传递PDF文件数组。最终输出被保存为一个从数组中所有文件创建的合并文件。以下C#代码片段向您展示如何使用文件路径连接PDF文件数组。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## 使用流连接PDF文件数组

连接PDF文件数组不仅限于仅限于磁盘上的文件。 你还可以连接来自流的 PDF 文件数组。如果您想连接多个 PDF 文件，可以使用 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法的适当重载。首先，您需要创建一个输入流数组和一个用于输出 PDF 的流，然后调用 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法。输出将保存在输出流中。以下 C# 代码片段向您展示如何使用流连接 PDF 文件数组。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## 连接特定文件夹中的所有 Pdf 文件

您甚至可以在运行时读取特定文件夹中的所有 Pdf 文件并将它们连接起来，甚至无需知道文件名。 简单提供包含您想要连接的PDF文档的目录路径。

请尝试使用以下C#代码片段来实现此功能。

## 连接PDF表单并保持字段名称唯一

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类在 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 中提供了连接PDF文件的功能。 现在，如果要连接的 PDF 文件中包含具有相似字段名称的表单字段，Aspose.PDF 提供了使结果 PDF 文件中的字段保持唯一的功能，并且您还可以指定后缀以使字段名称唯一。[KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) 属性的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 设为 true 时将使字段名称在连接 PDF 表单时唯一。此外，PdfFileEditor 的 [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) 属性可用于指定用户定义的后缀格式，该后缀将添加到字段名称中以使其在表单连接时唯一。此字符串必须包含 `%NUM%` 子字符串，该子字符串将在结果文件中替换为数字。

请参阅以下简单代码片段以实现此功能。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePDFForms-ConcatenatePDFForms.cs" >}}
## 合并 PDF 文件并创建目录

## 合并 PDF 文件

请查看以下代码片段，了解如何合并 PDF 文件。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-ConcatenatePdfFilesAndCreateTOC.cs" >}}

### 插入空白页

PDF 文件合并后，我们可以在文档的开头插入一个空白页，在其上创建目录。为了实现这一要求，我们可以将合并后的文件加载到 **Document** 对象中，并需要调用 Page.Insert(...) 方法插入空白页。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}

### 添加文本印章

为了创建目录，我们需要在第一页使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp) 对象添加文本印章。 Stamp 类提供 `BindLogo(...)` 方法来添加 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)，我们还可以使用 `SetOrigin(..)` 方法指定添加这些文本印章的位置。在本文中，我们正在连接两个 PDF 文件，因此我们需要创建两个文本印章对象指向这些单独的文档。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

### 创建本地链接

现在我们需要添加指向连接文件内部页面的链接。为了完成这一要求，我们可以使用 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类的 `CreateLocalLink(..)` 方法。在以下代码片段中，我们将 Transparent 作为第四个参数传递，以便链接周围的矩形不可见。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}
### 完整代码

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}

## 合并文件夹中的 PDF 文件

Aspose.Pdf.Facades 命名空间中的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类为您提供了合并 PDF 文件的功能。您甚至可以在运行时读取特定文件夹中的所有 Pdf 文件并将它们合并，而无需知道文件名。只需提供包含您要合并的 PDF 文档的目录路径即可。

请尝试使用以下 C# 代码片段从 Aspose.PDF 实现此功能：

```csharp
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// 检索特定目录中所有 Pdf 文件的名称
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// 获取当前系统日期并设置其格式
string date = DateTime.Now.ToString("MM-dd-yyyy");
// 获取当前系统时间并设置其格式
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// 设置最终结果 Pdf 文档的值
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// 实例化 PdfFileEditor 对象
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// 调用 PdfFileEditor 对象的 Concatenate 方法将所有输入文件
// 合并为一个输出文件
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```
---
title: 在 C# 中合并 PDF 文档
linktitle: 合并 PDF 文档
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/concatenate-pdf-documents/
description: 本节解释如何使用 PdfFileEditor 类通过 Aspose.PDF Facades 合并 PDF 文档。
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Concatenate PDF documents in C#",
    "alternativeHeadline": "Effortlessly Merge PDF Files in C#",
    "abstract": "Aspose.PDF for .NET 中的功能允许开发人员使用 C# 中的 PdfFileEditor 类高效地合并多个 PDF 文档。此功能支持通过文件路径和 MemoryStreams 合并文件，在 PDF 表单中创建唯一的字段名称，甚至在最终文档中生成目录，为文档管理和集成提供了简化的解决方案。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1615",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/concatenate-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/concatenate-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

## **概述**

本文解释了如何使用 C# 将不同的 PDF 文件合并、组合或连接成单个 PDF。它涵盖了以下主题：

- [C# 合并 PDF 文件](#concatenate-pdf-files-using-file-paths)
- [C# 组合 PDF 文件](#concatenate-pdf-files-using-file-paths)
- [C# 将多个 PDF 文件合并为一个 PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# 将多个 PDF 文件组合为一个 PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# 合并文件夹中的所有 PDF 文件](#concatenating-all-pdf-files-in-particular-folder)
- [C# 组合文件夹中的所有 PDF 文件](#concatenating-all-pdf-files-in-particular-folder)
- [C# 使用文件路径合并 PDF 文件](#concatenate-pdf-files-using-file-paths)
- [C# 使用流合并 PDF 文件](#concatenate-array-of-pdf-files-using-streams)
- [C# 合并文件夹中的所有 PDF 文件](#concatenate-pdf-files-in-folder)

## 使用文件路径合并 PDF 文件

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 是 [Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 中的类，允许您合并多个 PDF 文件。您不仅可以使用 FileStreams 合并文件，还可以使用 MemoryStreams。在本文中，将解释使用 MemoryStreams 合并文件的过程，并通过代码片段进行演示。

[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法可以用于合并两个 PDF 文件。 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法允许您传递三个参数：第一个输入 PDF、第二个输入 PDF 和输出 PDF。最终输出的 PDF 包含两个输入 PDF 文件。

以下 C# 代码片段演示了如何使用文件路径合并 PDF 文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Concatenate files
    pdfEditor.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths2.pdf", dataDir + "ConcatenateUsingPath_out.pdf");
}
```

在某些情况下，当有很多大纲时，用户可以通过将 CopyOutlines 设置为 false 来禁用它们，从而提高合并性能。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pfe = new Aspose.Pdf.Facades.PdfFileEditor();
    // Setting CopyOutlines to false
    pfe.CopyOutlines = false;
    // Concatenate files
    pfe.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled2.pdf", dataDir + "ConcatenateUsingPath_CopyOutlinesDisabled_out.pdf");
}
```

## 使用 MemoryStreams 合并多个 PDF 文件

[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类将源 PDF 文件和目标 PDF 文件作为参数。这些参数可以是磁盘上 PDF 文件的路径，也可以是 MemoryStreams。现在，对于这个示例，我们将首先创建两个文件流以从磁盘读取 PDF 文件。然后，我们将这些文件转换为字节数组。这些 PDF 文件的字节数组将转换为 MemoryStreams。一旦我们从 PDF 文件中获取 MemoryStreams，我们就可以将它们传递给合并方法并合并为一个输出文件。

以下 C# 代码片段演示了如何使用 MemoryStreams 合并多个 PDF 文件：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateMultiplePdfFilesUsingMemoryStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    string document1Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams1.pdf";
    string document2Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams2.pdf";
    string resultPdfPath = dataDir + "concatenated_out.pdf";
    
    // Create two file streams to read PDF files
    using (var fs1 = new FileStream(document1Path, FileMode.Open, FileAccess.Read))
    {
        using (var fs2 = new FileStream(document2Path, FileMode.Open, FileAccess.Read))
        {
            // Create byte arrays to keep the contents of PDF files
            var buffer1 = new byte[Convert.ToInt32(fs1.Length)];
            var buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            var i = 0;
            // Read PDF file contents into byte arrays
            i = fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            i = fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Now, first convert byte arrays into MemoryStreams and then concatenate those streams
            using (var pdfStream = new MemoryStream())
            {
                using (var fileStream1 = new MemoryStream(buffer1))
                {
                    using (var fileStream2 = new MemoryStream(buffer2))
                    {
                        // Create instance of PdfFileEditor class to concatenate streams
                        var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                        // Concatenate both input MemoryStreams and save to output MemoryStream
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convert MemoryStream back to byte array
                        var data = pdfStream.ToArray();
                        // Create a FileStream to save the output PDF file
                        using (var output = new FileStream(resultPdfPath, FileMode.Create, FileAccess.Write))
                        {
                            // Write byte array contents in the output file stream
                            output.Write(data, 0, data.Length);
                        }
                    }
                }
            }
        }
    }
}
```

## 使用文件路径合并 PDF 文件数组

如果您想合并多个 PDF 文件，可以使用 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法的重载，允许您传递一个 PDF 文件数组。最终输出将作为一个合并文件保存，该文件由数组中的所有文件创建。以下 C# 代码片段演示了如何使用文件路径合并 PDF 文件数组。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of files
    var filesArray = new string[2];
    filesArray[0] = dataDir + "Concatenate1.pdf";
    filesArray[1] = dataDir + "Concatenate2.pdf";
    // Concatenate files
    pdfEditor.Concatenate(filesArray, dataDir + "ConcatenateArrayOfPdfFilesUsingFilePaths_out.pdf");
}
```

## 使用流合并 PDF 文件数组

合并 PDF 文件数组不仅限于磁盘上的文件。您还可以从流中合并 PDF 文件数组。如果您想合并多个 PDF 文件，可以使用 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法的适当重载。首先，您需要创建一个输入流数组和一个输出 PDF 的流，然后调用 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法。输出将保存在输出流中。以下 C# 代码片段演示了如何使用流合并 PDF 文件数组。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    var document1Path = dataDir + "Concatenate1.pdf";
    var document2Path = dataDir + "Concatenate2.pdf";
    var resultPdfPath = dataDir + "ConcatenateArrayOfPdfUsingStreams_out.pdf";

    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Output stream
    using (var outputStream = new FileStream(resultPdfPath, FileMode.Create))
    {
        using (var stream1 = new FileStream(document1Path, FileMode.Open))
        {
            using (var stream2 = new FileStream(document2Path, FileMode.Open))
            {
                // Array of streams
                var inputStreams = new Stream[2];
                inputStreams[0] = stream1;
                inputStreams[1] = stream2;
                // Concatenate file
                pdfEditor.Concatenate(inputStreams, outputStream);
            }   
        }
    }
}
```

## 合并特定文件夹中的所有 PDF 文件

您甚至可以在运行时读取特定文件夹中的所有 PDF 文件并将它们合并，而无需知道文件名。只需提供包含您希望合并的 PDF 文档的目录路径。

请尝试使用以下 C# 代码片段来实现此功能。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatingAllPdfFilesInParticularFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    var fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    var resultPdfPath = dataDir + "ConcatenatingAllPdfFilesInParticularFolder_out.pdf";
    // Instantiate PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, resultPdfPath);
}
```

## 合并 PDF 表单并保持字段名称唯一

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类在 [Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 中提供了合并 PDF 文件的能力。如果要合并的 PDF 文件具有相似字段名称的表单字段，Aspose.PDF 提供了将结果 PDF 文件中的字段保持唯一的功能，您还可以指定后缀以使字段名称唯一。将 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 的 [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) 属性设置为 true 将使字段名称在合并 PDF 表单时保持唯一。此外，PdfFileEditor 的 [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) 属性可用于指定用户定义的后缀格式，该后缀将添加到字段名称以使其在合并表单时保持唯一。该字符串必须包含 `%NUM%` 子字符串，该子字符串将在结果文件中替换为数字。

请参见以下简单代码片段以实现此功能。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFormsAndKeepFieldsUnique()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique1.pdf";
    var inputFile2 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique2.pdf";
    var outFile = dataDir + "ConcatenatePDFForms_out.pdf";
    // Open PDF documents
    var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // To keep unique field Id for all the fields 
    fileEditor.KeepFieldsUnique = true;
    // Format of the suffix which is added to field name to make it unique when forms are concatenated.
    fileEditor.UniqueSuffix = "_%NUM%";
    // Concatenate the files into a resultant Pdf file
    fileEditor.Concatenate(inputFile1, inputFile2, outFile);
}
```

## 合并 PDF 文件并创建目录

## 合并 PDF 文件

请查看以下代码片段以获取有关如何合并 PDF 文件的信息。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFiles()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenateInput1.pdf";
    var inputFile2 = dataDir + "ConcatenateInput2.pdf";
    var outFile = dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf";
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();

    // Open PDF documents
    using (var outputStream = new FileStream(outFile, FileMode.Create))
    {
        using (var stream1 = new FileStream(inputFile1, FileMode.Open))
        {
            using (var stream2 = new FileStream(inputFile2, FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(stream1, stream2, outputStream);
            }
        }
    }
}
```

### 插入空白页

合并 PDF 文件后，我们可以在文档的开头插入一个空白页，以便创建目录。为了实现此要求，我们可以将合并的文件加载到 **Document** 对象中，并调用 Page.Insert(...) 方法以插入空白页。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertBlankPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Insert a blank page at the beginning of concatenated file to display Table of Contents
    using (var document = new Aspose.Pdf.Document(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf"))
    {
        // Insert a blank page in a PDF
        document.Pages.Insert(1);
    }
}
```

### 添加文本印章

为了创建目录，我们需要使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp) 对象在第一页上添加文本印章。Stamp 类提供 `BindLogo(...)` 方法以添加 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)，我们还可以使用 `SetOrigin(..)` 方法指定添加这些文本印章的位置。在本文中，我们正在合并两个 PDF 文件，因此我们需要创建两个指向这些单独文档的文本印章对象。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampForTableOfContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    var inputPdfFile = Path.Combine(dataDir, "ConcatenateInput1.pdf");
    // Set Text Stamp to display string Table Of Contents
    var stamp = new Aspose.Pdf.Facades.Stamp();
    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent, Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(inputPdfFile).GetPageWidth(1) / 3, 700);
    // Set particular pages
    stamp.Pages = new[] { 1 };
}
```

### 创建本地链接

现在我们需要添加指向合并文件内部页面的链接。为了实现此要求，我们可以使用 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类的 `CreateLocalLink(..)` 方法。在以下代码片段中，我们将透明作为第四个参数传递，以便链接周围的矩形不可见。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLocalLinks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Now we need to add Heading for Table Of Contents and links for documents
    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
    // Bind PDF document
    contentEditor.BindPdf(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf");
    // Create link for first document
    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
}
```

### 完整代码

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CompleteCode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create a MemoryStream object to hold the resultant PDf file
    using (var concatenatedStream = new MemoryStream())
    {
        using (var fs1 = new FileStream(dataDir + "ConcatenateInput1.pdf", FileMode.Open))
        {
            using (var fs2 = new FileStream(dataDir + "ConcatenateInput2.pdf", FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(fs1, fs2, concatenatedStream);
            }
        }

        using (var concatenatedPdfDocument = new Aspose.Pdf.Document(concatenatedStream))
        {
            // Insert a blank page at the beginning of concatenated file to display Table of Contents
            concatenatedPdfDocument.Pages.Insert(1);

            // Hold the result file with empty page added
            using (var documentWithBlankPage = new MemoryStream())
            {
                // Save PDF document
                concatenatedPdfDocument.Save(documentWithBlankPage);

                using (var documentWithTocHeading = new MemoryStream())
                {
                    // Add Table Of Contents logo as stamp to PDF file
                    var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp();
                    // Bind PDF document
                    fileStamp.BindPdf(documentWithBlankPage);

                    // Set Text Stamp to display string Table Of Contents
                    var stamp = new Aspose.Pdf.Facades.Stamp();
                    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(documentWithBlankPage).GetPageWidth(1) / 3, 700);
                    // Set particular pages
                    stamp.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(stamp);

                    // Create stamp text for first item in Table Of Contents
                    var document1Link = new Aspose.Pdf.Facades.Stamp();
                    document1Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("1 - Link to Document 1", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document1Link.SetOrigin(150, 650);
                    // Set particular pages on which stamp should be displayed
                    document1Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document1Link);

                    // Create stamp text for second item in Table Of Contents
                    var document2Link = new Aspose.Pdf.Facades.Stamp();
                    document2Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("2 - Link to Document 2", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document2Link.SetOrigin(150, 620);
                    // Set particular pages on which stamp should be displayed
                    document2Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document2Link);

                    // Save PDF document
                    fileStamp.Save(documentWithTocHeading);
                    fileStamp.Close();

                    // Now we need to add Heading for Table Of Contents and links for documents
                    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
                    // Bind PDF document
                    contentEditor.BindPdf(documentWithTocHeading);
                    // Create link for first document
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
                    // Create link for Second document
                    // We have used   new PdfFileInfo("d:/pdftest/Input1.pdf").NumberOfPages + 2   as PdfFileInfo.NumberOfPages(..) returns the page count for first document
                    // And 2 is because, second document will start at Input1+1 and 1 for the page containing Table Of Contents.
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 620, 100, 20),
                        new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "ConcatenateInput1.pdf").NumberOfPages + 2, 1, System.Drawing.Color.Transparent);
                    // Save PDF document
                    contentEditor.Save(dataDir + "Concatenated_Table_Of_Contents_out.pdf");
                }
            }
        }
    }
}
```

## 合并文件夹中的 PDF 文件

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类在 Aspose.Pdf.Facades 命名空间中为您提供了合并 PDF 文件的能力。您甚至可以在运行时读取特定文件夹中的所有 PDF 文件并将它们合并，而无需知道文件名。只需提供包含您希望合并的 PDF 文档的目录路径。

请尝试使用以下 C# 代码片段从 Aspose.PDF 实现此功能：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesInFolder()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, dataDir + "ConcatenatePdfFilesInFolder_out.pdf");
}
```
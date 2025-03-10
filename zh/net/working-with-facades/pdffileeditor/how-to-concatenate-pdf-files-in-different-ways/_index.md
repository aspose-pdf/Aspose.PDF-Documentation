---
title: 使用 .NET 5 合并 PDF 文件
linktitle: 如何合并 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 75
url: /zh/net/how-to-concatenate-pdf-files-in-different-ways/
description: 本文解释了将任意数量的现有 PDF 文件合并为单个 PDF 文件的可能方法。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge PDF files",
    "alternativeHeadline": "Effortlessly Combine Multiple PDFs",
    "abstract": "通过 Aspose.PDF for .NET 中的新功能无缝地将多个 PDF 文件合并为一个文档。此功能允许开发人员通过简单的方法调用连接任意数量的 PDF，从而提高 PDF 管理和操作的生产力。轻松将此功能集成到各种 .NET 应用程序中，包括 ASP.NET 和 Windows 应用程序，采用多种方法以满足不同需求。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "840",
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
    "url": "/net/how-to-concatenate-pdf-files-in-different-ways/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-concatenate-pdf-files-in-different-ways/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

本文描述了如何使用 [Aspose.PDF for .NET](/pdf/zh/net/) 组件将多个 PDF 文档 [合并](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 为一个单一的 PDF 文档。[Aspose.PDF for .NET](/pdf/zh/net/) 使这项工作变得轻而易举。

{{% /alert %}}

您只需调用 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类的 [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) 方法，所有输入的 PDF 文件将被合并在一起，并生成一个单一的 PDF 文件。让我们创建一个应用程序来练习 PDF 文件的合并。我们将使用 Visual Studio.NET 2019 创建一个应用程序。

{{% alert color="primary" %}}

Aspose.PDF for .NET 可以在任何运行于 .NET Framework 的应用程序中使用，无论是 ASP.NET Web 应用程序还是 Windows 应用程序。

{{% /alert %}}

## 如何以不同方式合并 PDF 文件

在表单中，有三个文本框（textBox1, textBox2, textBox3）及其各自的链接标签（linkLabel1, linkLabel2, linkLabel3）用于浏览 PDF 文件。点击“浏览”链接标签，将出现一个输入文件对话框（inputFileDialog1），使我们能够选择要合并的 PDF 文件。

```csharp
private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
    if (openFileDialog1.ShowDialog()==DialogResult.OK)
    {
        textBox1.Text=openFileDialog1.FileName;
    }
}
```

展示了一个 Windows 窗体应用程序的视图，以演示 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类的 PDF 文件合并功能。

![合并 PDF 文件](how-to-concatenate-pdf-files-in-different-ways_1.png)

选择 PDF 文件并点击 OK 按钮后，完整的文件名和路径将分配给相关的文本框。

![选择 PDF 文件](how-to-concatenate-pdf-files-in-different-ways_2.png)

同样，我们可以选择两个或三个输入 PDF 文件进行合并，如下所示：

![选择两个或三个输入 PDF 文件](how-to-concatenate-pdf-files-in-different-ways_3.png)

最后一个文本框（textBox4）将接受输出 PDF 文件的目标路径及其名称，输出文件将在此路径下创建。

![输出 PDF 文件的目标路径](how-to-concatenate-pdf-files-in-different-ways_4.png)

![合并方法](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Concatenate() 方法

Concatenate() 方法可以以三种方式使用。让我们仔细看看每一种：

### 方法 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

这种方法仅适用于需要合并两个 PDF 文件的情况。前两个参数（firstInputFile 和 secInputFile）提供要合并的两个输入 PDF 文件的完整文件名及其存储路径。第三个参数（outputFile）提供所需输出 PDF 文件的文件名及路径。

![使用文件名合并两个 PDF](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### 方法 2

- Concatenate(Stream firstInputStream, Stream secInputStream, Stream outputStream)

与上述方法类似，此方法也允许合并两个 PDF 文件。前两个参数（firstInputStream 和 secInputStream）提供作为流的两个输入 PDF 文件（流是位/字节的数组），第三个参数（outputStream）提供所需输出 PDF 文件的流表示。

![使用文件流合并两个 PDF](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
            {
                var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                pdfEditor.Concatenate(pdf1, pdf2, outputStream);
            }
        }
    }
}
```

### 方法 3

- Concatenate(Stream inputStreams[], Stream outputStream)

如果您想合并多个 PDF 文件，那么此方法将是您的最佳选择。第一个参数（inputStreams[]）提供要合并的输入 PDF 文件的流数组。第二个参数（outputStream）提供所需输出 PDF 文件的流表示。

![使用流数组合并多个 PDF](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var pdf3 = new FileStream(textBox3.Text, FileMode.Open))
            {
                var pdfStreams = new Stream[] { pdf1, pdf2, pdf3 };
                using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
                {
                    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                    pdfEditor.Concatenate(pdfStreams, outputStream);
                }
            }
        }
    }
}
```
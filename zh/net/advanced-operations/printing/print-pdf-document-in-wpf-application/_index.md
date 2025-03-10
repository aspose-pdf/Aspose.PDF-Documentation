---
title: 在 WPF 应用程序中打印 PDF
linktitle: 在 WPF 应用程序中打印 PDF 文档
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/print-pdf-document-in-wpf-application/
description: C# 从 WPF 应用程序打印 PDF 文档。此代码示例演示如何使用 C# 从 WPF 应用程序打印 PDF 文档。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Print PDF in WPF application",
    "alternativeHeadline": "Print PDF Documents Directly from WPF Applications",
    "abstract": "此新功能使得可以直接从 WPF 应用程序使用 C# 无缝打印 PDF 文档。此功能允许用户将 PDF 文件转换为 XPS 格式并高效打印，从而增强其应用程序中的文档管理能力。通过一个简单的代码示例，开发人员可以轻松实现此功能，以简化其 PDF 打印流程。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Print PDF, WPF application, C# PDF printing, Aspose.PDF library, convert PDF to XPS, direct printing, view PDF document, DocViewer class, MemoryStream object, FixedDocumentSequence",
    "wordcount": "406",
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
    "url": "/net/print-pdf-document-in-wpf-application/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-pdf-document-in-wpf-application/"
    },
    "dateModified": "2024-11-25",
    "description": "C# 从 WPF 应用程序打印 PDF 文档。此代码示例演示如何使用 C# 从 WPF 应用程序打印 PDF 文档。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 直接打印

Aspose.PDF 库具有将 PDF 文件转换为 XPS 的能力。我们可以使用此功能来组织文档的打印。
让我们考虑直接打印的示例：

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DirectPrintWpf()
{
    // Select a PDF document to print
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(openFileDialog.FileName))
        {
            using (var memoryStream = new MemoryStream())
            {
                // Convert the document to the XPS format
                document.Save(memoryStream, SaveFormat.Xps);
        
                // Create XPS package
                using (var package = Package.Open(memoryStream))
                {
                    //Create URI for the XPS package
                    //Any Uri will actually be fine here. It acts as a placeholder for the
                    //Uri of the package inside the PackageStore
                    var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
                    var packageUri = new Uri(inMemoryPackageName);
        
                    //Add the package to PackageStore
                    PackageStore.AddPackage(packageUri, package);
        
                    // Open the XPS document from the package
                    using (var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName))
                    {
                        // Get the root document sequence
                        var fixedDocumentSequence = xpsDoc.GetFixedDocumentSequence();
        
                        // Open a print dialog to set printing options
                        var printDialog = new PrintDialog();
                        if (printDialog.ShowDialog() == true)
                        {
                            if (fixedDocumentSequence != null)
                            {
                                // Print converted document
                                printDialog.PrintDocument(fixedDocumentSequence.DocumentPaginator,
                                    "A fixed document");
                            }
                        }
        
                        // Remove the package from the store and close the document after the print
                        PackageStore.RemovePackage(packageUri);
                    }
                }
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DirectPrintWpf()
{
    // Select a PDF document to print
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog())
    {
        // Open PDF document
        using var document = new Aspose.Pdf.Document(openFileDialog.FileName);
        
        // Convert the document to the XPS format
        using var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);
        
        // Create XPS package
        using var package = Package.Open(memoryStream);
        
        //Create URI for the XPS package
        //Any Uri will actually be fine here. It acts as a placeholder for the
        //Uri of the package inside the PackageStore
        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);
        
        //Add the package to PackageStore
        PackageStore.AddPackage(packageUri, package);
        
        // Open the XPS document from the package
        using var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);
        
        // Get the root document sequence
        var fixedDocumentSequence = xpsDoc.GetFixedDocumentSequence();
        
        // Open a print dialog to set printing options
        var printDialog = new PrintDialog();
        if (printDialog.ShowDialog() == true)
        {
            if (fixedDocumentSequence != null)
            {
                // Print converted document
                printDialog.PrintDocument(fixedDocumentSequence.DocumentPaginator,
                    "A fixed document");
            }
        }
        
        // Remove the package from the store and close the document after the print
        PackageStore.RemovePackage(packageUri);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

在这种情况下，我们将遵循以下步骤：

1. 使用 OpenFileDialog 打开 PDF 文件。
1. 将 PDF 转换为 XPS 并存储在 MemoryStream 对象中。
1. 将 MemoryStream 对象与 Xps 包关联。
1. 将包添加到包存储中。
1. 基于包创建 XpsDocument。
1. 获取 FixedDocumentSequence 的实例。
1. 使用 PrintDialog 将此序列发送到打印机。

## 查看和打印文档

在许多情况下，用户希望在打印之前查看文档。为了实现查看功能，我们可以使用 `DocumentViewer` 控件。
实现此方法的大部分步骤与前面的示例类似。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PreviewDocumentWithDocumentViewer(DocumentViewer docViewer)
{
    // Select a PDF document to print
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(openFileDialog.FileName))
        {
            using (var memoryStream = new MemoryStream())
            {
                // Convert the document to the XPS format
                document.Save(memoryStream, SaveFormat.Xps);

                // Create XPS package
                using (var package = Package.Open(memoryStream))
                {
                    //Create URI for the XPS package
                    var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
                    var packageUri = new Uri(inMemoryPackageName);

                    //Add package to PackageStore
                    PackageStore.AddPackage(packageUri, package);

                    // Open the XPS document from the package
                    using (var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName))
                    {
                        // Display the document in the DocumentViewer
                        docViewer.Document = xpsDoc.GetFixedDocumentSequence();
                    }
                }
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PreviewDocumentWithDocumentViewer(DocumentViewer docViewer)
{
    // Select a PDF document to print
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        // Open PDF document
        using var document = new Aspose.Pdf.Document(openFileDialog.FileName);

        // Convert the document to the XPS format
        using var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);

        // Create XPS package
        using var package = Package.Open(memoryStream);

        //Create URI for the XPS package
        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //Add package to PackageStore
        PackageStore.AddPackage(packageUri, package);

        // Open the XPS document from the package
        using var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);

        // Display the document in the DocumentViewer
        docViewer.Document = xpsDoc.GetFixedDocumentSequence();
    }
}
```
{{< /tab >}}
{{< /tabs >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
---
title: WPFアプリケーションでPDFを印刷
linktitle: WPFアプリケーションでPDFドキュメントを印刷
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/print-pdf-document-in-wpf-application/
description: C#を使用してWPFアプリケーションからPDFドキュメントを印刷します。このコードサンプルは、C#を使用してWPFアプリケーションからPDFドキュメントを印刷する方法を示しています。
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
    "abstract": "この新機能により、C#を使用してWPFアプリケーションからPDFドキュメントをシームレスに印刷できます。この機能により、ユーザーはPDFファイルをXPS形式に変換し、効率的に印刷できるため、アプリケーション内でのドキュメント管理機能が向上します。簡単なコード例を使用して、開発者はこの機能を簡単に実装し、PDF印刷プロセスを効率化できます。",
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
    "description": "C#を使用してWPFアプリケーションからPDFドキュメントを印刷します。このコードサンプルは、C#を使用してWPFアプリケーションからPDFドキュメントを印刷する方法を示しています。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## 直接印刷

Aspose.PDFライブラリは、PDFファイルをXPSに変換する機能を持っています。この機能を使用して、ドキュメントの印刷を整理できます。
直接印刷の例を考えてみましょう：

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

この場合、次の手順に従います：

1. OpenFileDialogを使用してPDFファイルを開きます。
1. PDFをXPSに変換し、MemoryStreamオブジェクトに保存します。
1. MemoryStreamオブジェクトをXpsパッケージに関連付けます。
1. パッケージをパッケージストアに追加します。
1. パッケージに基づいてXpsDocumentを作成します。
1. FixedDocumentSequenceのインスタンスを取得します。
1. PrintDialogを使用してこのシーケンスをプリンターに送信します。

## ドキュメントの表示と印刷

多くの場合、ユーザーは印刷する前にドキュメントを見たいと考えます。表示を実装するために、`DocumentViewer`コントロールを使用できます。
このアプローチを実装するためのほとんどの手順は、前の例と似ています。

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
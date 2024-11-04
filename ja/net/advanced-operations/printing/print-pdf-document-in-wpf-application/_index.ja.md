---
title: WPFアプリケーションでPDFを印刷する
linktitle: WPFアプリケーションでPDFドキュメントを印刷する
type: docs
weight: 50
url: /net/print-pdf-document-in-wpf-application/
description: WPFアプリケーションからC#を使用してPDFドキュメントを印刷します。このコードサンプルは、C#を使用してWPFアプリケーションからPDFドキュメントを印刷する方法を示しています。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "WPFアプリケーションでPDFを印刷する",
    "alternativeHeadline": "WPFアプリケーションでPDFを印刷する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, WPFアプリケーションでのpdf",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "WPFアプリケーションからC#を使用してPDFドキュメントを印刷します。このコードサンプルは、C#を使用してWPFアプリケーションからPDFドキュメントを印刷する方法を示しています。"
}
</script>
次のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

## 直接印刷

Aspose.PDF ライブラリには、PDFファイルをXPSに変換する機能があります。この機能を使用して、ドキュメントの印刷を整理できます。
直接印刷の例を考えてみましょう：

```csharp
    private void Print_OnClick(object sender, RoutedEventArgs e)
    {
        var openFileDialog = new OpenFileDialog
        {
            Filter = "PDF Documents|*.pdf"
        };
        openFileDialog.ShowDialog();

        Aspose.Pdf.Document document = new Document(openFileDialog.FileName);
        var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);
        var package = Package.Open(memoryStream);

        //Create URI for Xps Package
        //Any Uri will actually be fine here. It acts as a place holder for the
        //Uri of the package inside of the PackageStore
        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //Add package to PackageStore
        PackageStore.AddPackage(packageUri, package);

        var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);
        var fixedDocumentSequence = xpsDoc.GetFixedDocumentSequence();

        var printDialog = new PrintDialog();
        if (printDialog.ShowDialog() == true)
        {
            if (fixedDocumentSequence != null)
                printDialog.PrintDocument(fixedDocumentSequence.DocumentPaginator, "A fixed document");
            else
                throw new NullReferenceException();
        }
        PackageStore.RemovePackage(packageUri);
        xpsDoc.Close();

    }
```
このケースでは、以下のステップに従います：

1. OpenFileDialogを使用してPDFファイルを開く
1. PDFをXPSに変換し、MemoryStreamオブジェクトに保存する
1. MemoryStreamオブジェクトをXpsパッケージに関連付ける
1. パッケージをパッケージストアに追加する
1. パッケージに基づいてXpsDocumentを作成する
1. FixedDocumentSequenceのインスタンスを取得する
1. このシーケンスをPrintDialogを使用してプリンターに送信する

## 文書の表示と印刷

多くの場合、ユーザーは印刷前に文書を見たいと思います。ビューを実装するために、DocViewerクラスを使用できます。
このアプローチを実装するためのステップのほとんどは、前の例と同様です。

```csharp
private void OpenFile_OnClick(object sender, RoutedEventArgs e)
{
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        var document = new Document(openFileDialog.FileName);
        var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);

        var package = Package.Open(memoryStream);

        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //パッケージをパッケージストアに追加
        PackageStore.AddPackage(packageUri, package);

        var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);
        DocViewer.Document = xpsDoc.GetFixedDocumentSequence();
        xpsDoc.Close();
    };
}
```

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
    "applicationCategory": ".NET用PDF操作ライブラリ",
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
```


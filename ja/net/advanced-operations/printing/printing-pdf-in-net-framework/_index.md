---
title: .NET FrameworkでPDFを印刷する
linktitle: .NET FrameworkでPDFを印刷する
type: docs
weight: 10
url: /ja/net/printing-pdf-in-net-framework/
keywords: "print pdf file c#, c# print pdf"
description: プリンターとページ設定を使用して、C#でPDFファイルをデフォルトプリンターに印刷することができます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": ".NET FrameworkでPDFを印刷する",
    "alternativeHeadline": ".NET FrameworkでPDFを印刷する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdf in .NET Framework",
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
    "url": "/net/printing-pdf-in-net-framework/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-in-net-framework/"
    },
    "dateModified": "2022-02-04",
    "description": "プリンターとページ設定を使用して、C#でPDFファイルをデフォルトプリンターに印刷することができます。"
}
</script>
以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリとも連携します。

## **C#でPDFファイルを印刷 - プリンターとページ設定を使用してデフォルトプリンターにPDFファイルを印刷する**

この記事では、C#でプリンターとページ設定を使用してデフォルトプリンターにPDFファイルを印刷する方法について説明します。

[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) クラスを使用すると、PDFファイルをデフォルトプリンターに印刷できます。PdfViewerオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2) メソッドを使用してPDFを開きます。異なる印刷設定を指定するには、`PageSettings` と `PrinterSettings` クラスを使用します。最後に、[PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) メソッドを呼び出して、プリンターとページ設定を使用してPDFをデフォルトプリンターに印刷します。次のコードスニペットは、プリンターとページ設定を使用してデフォルトプリンターにPDFを印刷する方法を示しています。

```csharp
public static void SimplePrint()
{
    // PdfViewerオブジェクトを作成
    PdfViewer viewer = new PdfViewer();

    // 入力PDFファイルを開く
    viewer.BindPdf(System.IO.Path.Combine(_dataDir, "input.pdf"));

    // 印刷のための属性を設定
    viewer.AutoResize = true;         // サイズを調整してファイルを印刷
    viewer.AutoRotate = true;         // 回転を調整してファイルを印刷
    viewer.PrintPageDialog = false;   // 印刷時にページ番号ダイアログを表示しない

    // プリンターとページ設定およびPrintDocumentのオブジェクトを作成
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
    System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

    // プリンター名を設定
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

    // 必要に応じてPageSizeを設定
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // 必要に応じてPageMarginsを設定
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // プリンターとページ設定を使用して文書を印刷
    viewer.PrintDocumentWithSettings(pgs, ps);

    // 印刷後にPDFファイルを閉じる
    viewer.Close();
}
```
印刷ダイアログを表示するには、次のコードスニペットを使用してみてください：

```csharp
System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    // ドキュメント印刷コードはここに記述
    // プリンタとページ設定を使用してドキュメントを印刷
    viewer.PrintDocumentWithSettings(pgs, ps);
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



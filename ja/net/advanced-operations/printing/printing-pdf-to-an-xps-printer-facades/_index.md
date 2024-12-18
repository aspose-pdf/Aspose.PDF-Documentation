---
title: PDFをXPSプリンターに印刷する
linktitle: PDFをXPSプリンターに印刷する（ファサード）
type: docs
weight: 20
url: /ja/net/printing-pdf-to-an-xps-printer-facades/
description: このページでは、PdfViewerクラスを使用してPDFをXPSプリンターに印刷する方法を示しています。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFをXPSプリンターに印刷する",
    "alternativeHeadline": "PDFをXPSプリンターに印刷する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, XPSプリンターへのpdf",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDFドキュメントチーム",
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
    "url": "/net/printing-pdf-to-an-xps-printer-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-to-an-xps-printer-facades/"
    },
    "dateModified": "2022-02-04",
    "description": "このページでは、PdfViewerクラスを使用してPDFをXPSプリンターに印刷する方法を示しています。"
}
</script>

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリでも動作します。

## **C#でPDFをXPSプリンタに印刷する**

PDFファイルをXPSプリンタ、またはその他のソフトプリンタに印刷するには、[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) クラスを使用します。これを行うには、PdfViewer クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2) メソッドを使用してPDFファイルを開きます。PrinterSettings と PageSettings クラスを使用して異なる印刷設定を設定することができます。また、インストールされているXPSまたはその他のソフトプリンタの PrinterName プロパティを設定する必要があります。

最後に、[PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) メソッドを使用して、PDFをXPSまたはその他のソフトプリンタに印刷します。以下のコードスニペットは、PDFファイルをXPSプリンタに印刷する方法を示しています。

```csharp
public static void PrintToXpsPrinter()
{
    // PdfViewer オブジェクトを作成する
    PdfViewer viewer = new PdfViewer();

    // 入力PDFファイルを開く
    viewer.BindPdf(_dataDir + "input.pdf");

    // 印刷のための属性を設定する
    viewer.AutoResize = true;         // サイズを調整してファイルを印刷する
    viewer.AutoRotate = true;         // 回転を調整してファイルを印刷する
    viewer.PrintPageDialog = false;   // 印刷時にページ番号ダイアログを表示しない

    // プリンタとページ設定、PrintDocumentのためのオブジェクトを作成する
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // XPS/PDFプリンタ名を設定する
    ps.PrinterName = "Microsoft XPS Document Writer";
    // またはPDFプリンタを設定する
    // Ps.PrinterName = "Adobe PDF";

    // 必要に応じてPageSizeを設定する
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // 必要に応じてPageMarginsを設定する
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // プリンタとページ設定を使用してドキュメントを印刷する
    viewer.PrintDocumentWithSettings(pgs, ps);

    // 印刷後にPDFファイルを閉じる
    viewer.Close();
}
```

## Choosing paper source by PDF page size
 
Since the 24.4 release, choosing paper source by PDF page size in the print dialog is possible. The next code snippet enables picking a printer tray based on the PDF's page size.

This preference can be switched on and off using the 'PdfContentEditor' facade.

```cs
using (PdfContentEditor contentEditor = new PdfContentEditor())
{
    contentEditor.BindPdf("input.pdf");

    // Set the flag to choose a paper tray using the PDF page size
    contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
    contentEditor.Save("result.pdf");
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
                "areaServed": "AU",
                "availableLanguage": "英語"
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


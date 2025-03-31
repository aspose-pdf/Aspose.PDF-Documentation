---
title: PDFページスタンプの追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/add-pdf-page-stamp/
description: Aspose.PDFを使用して、ウォーターマークやブランディングのために、テキストや画像を含むPDFページにスタンプを追加する方法を発見してください。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Page Stamp",
    "alternativeHeadline": "Enhance PDFs with Custom Stamps and Page Numbers",
    "abstract": "PdfFileStampクラスを使用して、PDFドキュメントのすべてまたは特定のページにカスタマイズされたスタンプを簡単に追加できるPDFページスタンプ機能を紹介します。この機能は、ページスタンプの回転、背景、カスタム番号スタイルなどのさまざまな属性を有効にすることで、ドキュメントのパーソナライズを強化し、PDFファイルをユニークでプロフェッショナルに仕上げます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1309",
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
    "url": "/net/add-pdf-page-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pdf-page-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDFファイルのすべてのページにPDFページスタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスを使用すると、PDFファイルのすべてのページにPDFページスタンプを追加できます。PDFページスタンプを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)と[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスのオブジェクトを作成する必要があります。また、[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスの[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)メソッドを使用してPDFページスタンプを作成する必要があります。他の属性（原点、回転、背景など）も[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)オブジェクトを使用して設定できます。その後、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[AddStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp/methods/addstamp)メソッドを使用してPDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[Close](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルのすべてのページにPDFページスタンプを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "AddPageStampOnAllPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnAllPages_out.pdf");
    }
}
```

## PDFファイルの特定のページにPDFページスタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスを使用すると、PDFファイルの特定のページにPDFページスタンプを追加できます。PDFページスタンプを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)と[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスのオブジェクトを作成する必要があります。また、[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスの[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用してPDFページスタンプを作成する必要があります。他の属性（原点、回転、背景など）も[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)オブジェクトを使用して設定できます。PDFファイルの特定のページにPDFページスタンプを追加するには、[Stamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf/stamp)クラスの[Pages](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/stamp/properties/pages)プロパティを設定する必要があります。このプロパティには、スタンプを追加したいページの番号を含む整数配列が必要です。その後、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[AddStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp/methods/addstamp)メソッドを使用してPDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[Close](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルの特定のページにPDFページスタンプを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnCertainPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "PageStampOnCertainPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;
        stamp.Pages = new[] { 1, 3 };  // Apply stamp to specific pages (1 and 3)

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnCertainPages_out.pdf");
    }
}
```

## PDFファイルにページ番号を追加

[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスを使用すると、PDFファイルにページ番号を追加できます。ページ番号を追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスのオブジェクトを作成する必要があります。「ページXのN」のようにページ番号を表示したい場合、Xは現在のページ番号、NはPDFファイルの総ページ数です。最初に[PdfFileInfo](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileinfo)クラスの[NumberOfpages](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages)プロパティを使用してページ数を取得する必要があります。現在のページ番号を取得するには、テキストの任意の場所に**#**記号を使用できます。ページ番号のテキストは、[FormattedText](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formattedtext)クラスを使用してフォーマットできます。特定の番号からページ番号を開始したい場合は、[StartingNumber](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber)プロパティを設定できます。ファイルにページ番号を追加する準備ができたら、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffilestamp)クラスの[AddPageNumber](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7)メソッドを呼び出す必要があります。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/facade/methods/close)クラスの[Close](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルにページ番号を追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;
        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```

### カスタム番号スタイル

PdfFileStampクラスは、PDFドキュメント内にスタンプオブジェクトとしてページ番号情報を追加する機能を提供します。このリリース以前は、クラスはページ番号スタイルとして1,2,3,4のみをサポートしていました。しかし、PDFドキュメント内にページ番号スタンプを配置する際にカスタム番号スタイルを使用するという顧客からの要望がありました。この要件を満たすために、[NumberingStyle](https://reference.aspose.com/pdf/ja/net/aspose.pdf/numberingstyle)プロパティが導入され、[NumberingStyle](https://reference.aspose.com/pdf/ja/net/aspose.pdf/numberingstyle)列挙から値を受け入れます。この列挙で提供される値は以下の通りです。

- 小文字のアルファベット。
- 大文字のアルファベット。
- アラビア数字。
- ローマ数字（小文字）。
- ローマ数字（大文字）。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCustomPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Specify numbering style as Numerals Roman UpperCase
        fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;

        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddCustomPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```
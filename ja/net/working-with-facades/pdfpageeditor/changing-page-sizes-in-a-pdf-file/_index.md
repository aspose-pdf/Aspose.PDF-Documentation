---
title: PDF ファイルにおけるページサイズの変更
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/changing-page-sizes-in-a-pdf-file/
description: PdfPageEditor クラスを使用して、PDF ファイルのページサイズを変更する方法を学んでみましょう.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Changing page sizes in PDF file",
    "alternativeHeadline": "Effortlessly Adjust PDF Page Sizes with PdfPageEditor",
    "abstract": "Aspose.PdfのPdfPageEditorクラスの機能により、ユーザーはPDFファイル内の個々のページまたは複数のページのページサイズを簡単に変更できます。PageSizeプロパティとPagesプロパティを利用することで、ユーザーはさまざまな事前定義されたページサイズから選択し、効果的に適用することができ、PDFドキュメントのレイアウトの柔軟性とカスタマイズ性が向上します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "197",
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
    "url": "/net/changing-page-sizes-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-page-sizes-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーや開発者向けの情報を確認してください。"
}
</script>

## 実装の詳細

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) クラスは [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) 内に存在し、個々のページまたは複数のページのページサイズを一度に変更するために使用できる [PageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagesize) プロパティを含んでいます。 Pages プロパティを使用して、新しいページサイズを適用するページの番号を指定することができます。 PageSize クラスは、そのメンバーとしてさまざまなページサイズのリストを保持しています。このクラスのいずれかのメンバーは、[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) クラスの PageSize プロパティに割り当てることができます。 GetPageSize メソッドを使用して該当するページ番号を渡すことで、任意のページのページサイズを取得することもできます。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfPageEditor object
    using (var pdfPageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        // Change page size of the selected pages
        pdfPageEditor.ProcessPages = new[] { 1 };

        // Select a predefined page size (LETTER) and assign it
        pdfPageEditor.PageSize = Aspose.Pdf.PageSize.PageLetter;

        // Save the file with the updated page size
        pdfPageEditor.Save(dataDir + "ChangePageSizes_out.pdf");

        // Get and display the page size assigned
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        var pageSize = pdfPageEditor.GetPageSize(1);
        Console.WriteLine($"Width: {pageSize.Width}, Height: {pageSize.Height}");
    }
}
```
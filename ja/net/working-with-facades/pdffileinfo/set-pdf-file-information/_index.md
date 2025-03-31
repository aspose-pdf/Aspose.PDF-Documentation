---
title: PDFファイル情報の設定
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/set-pdf-file-information/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイル情報を設定する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set PDF File Information",
    "alternativeHeadline": "Set Custom Metadata for PDF Files Effortlessly",
    "abstract": "Aspose.PDF for .NETの新機能を使用して、著者、タイトル、キーワードなどのファイル固有の情報を簡単に設定および更新できることで、PDFファイル管理を強化します。PdfFileInfoクラスを利用して、PDFを効率的に修正し、組織化と検索性を向上させるための貴重なメタデータを追加します。SaveNewInfoメソッドを使用して、これらの更新をシームレスに保存することで、ワークフローを合理化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "251",
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
    "url": "/net/set-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo)クラスを使用すると、PDFファイルのファイル固有の情報を設定できます。[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo)クラスのオブジェクトを作成し、著者、タイトル、キーワード、作成者などのさまざまなファイル固有のプロパティを設定する必要があります。最後に、[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo)オブジェクトの[SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1)メソッドを使用して、更新されたPDFファイルを保存します。

次のコードスニペットは、PDFファイル情報を設定する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfFileInfo object to work with PDF metadata
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set PDF information
        fileInfo.Author = "Aspose";
        fileInfo.Title = "Hello World!";
        fileInfo.Keywords = "Peace and Development";
        fileInfo.Creator = "Aspose";
        
        // Save the PDF with updated information
        fileInfo.SaveNewInfo(dataDir + "SetFileInfo_out.pdf");
    }
}
```

## メタ情報の設定

[SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo)メソッドを使用すると、任意の情報を追加できます。私たちの例では、フィールドを追加しました。次のコードスニペットを確認してください：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMetaInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of the PdfFileInfo object
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set a new custom attribute as meta info
        fileInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

        // Save the updated file
        fileInfo.SaveNewInfo(dataDir + "SetMetaInfo_out.pdf");
    }
}
```
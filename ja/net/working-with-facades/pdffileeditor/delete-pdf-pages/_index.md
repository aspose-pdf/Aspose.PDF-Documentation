---
title: PDFページの削除
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ja/net/delete-pdf-pages/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDF FacadesでPDFページを削除する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete PDF pages",
    "alternativeHeadline": "Effortlessly Remove Pages from PDF Files",
    "abstract": "特定のページをPDF文書から簡単に削除するには、Aspose.PDF for .NET Facadesを使用します。PdfFileEditorクラスを利用することで、ファイルパスとストリームの両方から不要なページを削除し、最終出力に対する正確な制御を持ってPDF編集プロセスを効率化できます。この効率的なページ削除機能で文書管理能力を向上させましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "262",
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
    "url": "/net/delete-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/delete-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

ディスク上にあるPDFファイルから複数のページを削除したい場合は、次の3つのパラメーターを受け取る[Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index)メソッドのオーバーロードを使用できます：入力ファイルパス、削除するページ番号の配列、および出力PDFファイルパス。2番目のパラメーターは、削除する必要があるすべてのページを表す整数配列です。指定されたページは入力ファイルから削除され、結果は出力ファイルとして保存されます。以下のコードスニペットは、ファイルパスを使用してPDFページを削除する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of pages to delete
    var pagesToDelete = new int[] { 1, 2 };
    // Delete pages
    pdfEditor.Delete(dataDir + "DeletePagesInput.pdf", pagesToDelete, dataDir + "DeletePagesUsingFilePath_out.pdf");
}
```

## ストリームを使用したPDFページの削除

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスの[Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index)メソッドは、入力PDFファイルからページを削除するためのオーバーロードも提供しています。このオーバーロードは、入力ストリーム、削除するPDFページの整数配列、および出力ストリームの3つのパラメーターを受け取ります。以下のコードスニペットは、ストリームを使用してPDFページを削除する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "DeletePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "DeletePagesUsingStream_out.pdf", FileMode.Create))
        {
            // Array of pages to delete
            var pagesToDelete = new int[] { 1, 2 };
            // Delete pages
            pdfEditor.Delete(inputStream, pagesToDelete, outputStream);
        }
    }
}
```
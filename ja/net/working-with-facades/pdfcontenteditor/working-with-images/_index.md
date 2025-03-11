---
title: PdfContentEditorを使用した画像の操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/working-with-images-in-pdf
description: このセクションでは、PdfContentEditorクラスを使用してAspose.PDF Facadesで画像を追加および削除する方法について説明します。
lastmod: "2021-06-24"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with Images using PdfContentEditor",
    "alternativeHeadline": "Enhance PDF Images with PdfContentEditor Features",
    "abstract": "Aspose.PDF for .NETは、PdfContentEditorクラスを通じて強化された画像管理機能を提供し、ユーザーが特定のページから特定の画像を簡単に削除したり、PDFファイルからすべての画像を完全に削除したりできるようにします。さらに、この機能により、画像の置き換えがシームレスに行え、編集プロセスが効率化され、文書のカスタマイズが向上します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "415",
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
    "url": "/net/working-with-images-in-pdf",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-images-in-pdf"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## PDFの特定のページから画像を削除する（ファサード）

特定のページから画像を削除するには、pageNumberおよびindexパラメーターを使用して[DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1)メソッドを呼び出す必要があります。indexパラメーターは、削除する画像のインデックスを表す整数の配列です。まず、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)クラスのオブジェクトを作成し、その後[DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1)メソッドを呼び出します。その後、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index)メソッドを使用して更新されたPDFファイルを保存できます。

以下のコードスニペットは、PDFの特定のページから画像を削除する方法を示しています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf")))
    {
        editor.DeleteImage(2, new[] { 2 });

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo10.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor Object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf"));

    editor.DeleteImage(2, new[] { 2 });

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo10.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## PDFファイルからすべての画像を削除する（ファサード）

すべての画像は、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)の[DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1)メソッドを使用してPDFファイルから削除できます。[DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1)メソッドを呼び出し、パラメーターなしのオーバーロードを使用してすべての画像を削除し、その後[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index)メソッドを使用して更新されたPDFファイルを保存します。

以下のコードスニペットは、PDFファイルからすべての画像を削除する方法を示しています。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf")))
    {
        editor.DeleteImage();

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo11.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample.pdf"));

    editor.DeleteImage();

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo11.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## PDFファイル内の画像を置き換える（ファサード）

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)を使用すると、PDFファイル内の画像を置き換えることができます。このために[ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage)メソッドを呼び出し、結果を保存します。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample_cats_dogs.pdf")))
    {
        editor.ReplaceImage(2, 4, dataDir + "Image.jpg");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo12.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, dataDir + "Image.jpg");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo12.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}
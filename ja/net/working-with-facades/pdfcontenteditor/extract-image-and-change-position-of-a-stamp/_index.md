---
title: 画像を抽出し、スタンプの位置を変更する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ja/net/extract-image-and-change-position-of-a-stamp/
description: このセクションでは、Aspose.PDF Facadesを使用して画像を抽出し、スタンプの位置を変更する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract image and change stamp position",
    "alternativeHeadline": "Extract Images and Adjust Stamp Positions in PDF",
    "abstract": "Aspose.PDF for .NETの機能により、ユーザーはPDFスタンプから画像を効率的に抽出し、精密に再配置することができます。PdfContentEditorクラスを利用することで、開発者はスタンプ画像を簡単に管理および操作でき、PDF編集機能を向上させ、全体的な文書のプレゼンテーションを改善します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "393",
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
    "url": "/net/extract-image-and-change-position-of-a-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-change-position-of-a-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 画像スタンプから画像を抽出する

[PdfContentEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfcontenteditor)クラスを使用すると、PDFファイルのスタンプから画像を抽出できます。まず、[PdfContentEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfcontenteditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、[GetStamps](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps)メソッドを呼び出して、PDFファイルの特定のページからStampInfoオブジェクトの配列を取得します。次に、StampInfo.Imageプロパティを使用してStampInfoから画像を取得できます。画像を取得したら、画像を保存するか、画像のさまざまなプロパティで作業できます。以下のコードスニペットは、画像スタンプから画像を抽出する方法を示しています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ExtractImage-ImageStamp.pdf");

        // Get Stamp info for the first stamp
        var infos = pdfContentEditor.GetStamps(1);

        // Get the image from Stamp Info
        var image = infos[0].Image;

        // Save the extracted image
        image.Save(dataDir + "image_out.jpg");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ExtractImage-ImageStamp.pdf");

    // Get Stamp info for the first stamp
    var infos = pdfContentEditor.GetStamps(1);

    // Get the image from Stamp Info
    var image = infos[0].Image;

    // Save the extracted image
    image.Save(dataDir + "image_out.jpg");
}
```
{{< /tab >}}
{{< /tabs >}}

## PDFファイル内のスタンプの位置を変更する

[PdfContentEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfcontenteditor)クラスを使用すると、PDFファイル内のスタンプの位置を変更できます。まず、[PdfContentEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfcontenteditor)クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades.facade/bindpdf/methods/3)メソッドを使用して入力PDFファイルをバインドする必要があります。その後、スタンプインデックスとPDFファイルの特定のページ上の新しい位置を指定して[MoveStamp](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp)メソッドを呼び出します。次に、[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたファイルを保存できます。以下のコードスニペットは、特定のページでスタンプを移動する方法を示しています。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeStampPosition()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

        int pageId = 1;
        int stampIndex = 1;
        double x = 200;
        double y = 200;

        // Change the position of the stamp to new x and y position
        pdfContentEditor.MoveStamp(pageId, stampIndex, x, y);

        // Save PDF document
        pdfContentEditor.Save(dataDir + "ChangeStampPosition_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeStampPosition()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

    int pageId = 1;
    int stampIndex = 1;
    double x = 200;
    double y = 200;

    // Change the position of the stamp to new x and y position
    pdfContentEditor.MoveStamp(pageId, stampIndex, x, y);

    // Save PDF document
    pdfContentEditor.Save(dataDir + "ChangeStampPosition_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

また、[MoveStampById](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid)メソッドを使用して、StampIdを使用して特定のスタンプを移動することもできます。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveStampById()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor Object
    using (var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

        int pageId = 1;
        int stampId = 1;
        double x = 200;
        double y = 200;

        // Change the position of the stamp to new x and y position
        pdfContentEditor.MoveStamp(pageId, stampId, x, y);

        // Save PDF document
        pdfContentEditor.Save(dataDir + "ChangeStampPositionByID_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveStampById()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_StampsWatermarks();

    // Instantiate PdfContentEditor Object
    using var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    pdfContentEditor.BindPdf(dataDir + "ChangeStampPosition.pdf");

    int pageId = 1;
    int stampId = 1;
    double x = 200;
    double y = 200;

    // Change the position of the stamp to new x and y position
    pdfContentEditor.MoveStamp(pageId, stampId, x, y);

    // Save PDF document
    pdfContentEditor.Save(dataDir + "ChangeStampPositionByID_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}
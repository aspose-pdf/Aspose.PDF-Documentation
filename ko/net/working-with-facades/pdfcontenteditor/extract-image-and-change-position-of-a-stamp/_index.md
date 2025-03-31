---
title: 이미지 추출 및 스탬프 위치 변경
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/extract-image-and-change-position-of-a-stamp/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 이미지를 추출하고 스탬프의 위치를 변경하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract image and change stamp position",
    "alternativeHeadline": "Extract Images and Adjust Stamp Positions in PDF",
    "abstract": "Aspose.PDF for .NET의 기능은 사용자가 PDF 스탬프에서 이미지를 효율적으로 추출하고 정밀하게 재배치할 수 있도록 합니다. PdfContentEditor 클래스를 활용하여 개발자는 스탬프 이미지를 쉽게 관리하고 조작할 수 있으며, PDF 편집 기능을 향상시키고 전체 문서 프레젠테이션을 개선할 수 있습니다.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 이미지 스탬프에서 이미지 추출

[PdfContentEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor) 클래스는 PDF 파일의 스탬프에서 이미지를 추출할 수 있게 해줍니다. 먼저, [PdfContentEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [GetStamps](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps) 메서드를 호출하여 PDF 파일의 특정 페이지에서 StampInfo 객체 배열을 가져옵니다. 그런 다음 StampInfo.Image 속성을 사용하여 StampInfo에서 이미지를 가져올 수 있습니다. 이미지를 얻은 후에는 이미지를 저장하거나 이미지의 다양한 속성과 작업할 수 있습니다. 다음 코드 스니펫은 이미지 스탬프에서 이미지를 추출하는 방법을 보여줍니다.

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

## PDF 파일에서 스탬프 위치 변경

[PdfContentEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor) 클래스는 PDF 파일에서 스탬프의 위치를 변경할 수 있게 해줍니다. 먼저, [PdfContentEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, 특정 페이지에서 스탬프 인덱스와 새로운 위치를 사용하여 [MoveStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) 메서드를 호출합니다. 그런 다음, [Save](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 파일을 저장할 수 있습니다. 다음 코드 스니펫은 특정 페이지에서 스탬프를 이동하는 방법을 보여줍니다.

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

또한, [MoveStampById](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) 메서드를 사용하여 StampId를 사용하여 특정 스탬프를 이동할 수 있습니다.

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
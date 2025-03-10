---
title: 헤더 및 푸터 관리
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/manage-header-and-footer/
description: Aspose.PDF를 사용하여 .NET에서 PDF 파일의 헤더와 푸터를 조작하는 방법을 탐색하여 문서 구조를 개선합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manage Header and Footer",
    "alternativeHeadline": "Enhance PDFs with Custom Headers and Footers",
    "abstract": "Aspose.PDF for .NET의 헤더 및 푸터 관리 기능을 통해 사용자는 PdfFileStamp 클래스를 사용하여 PDF 문서에 헤더와 푸터를 쉽게 추가, 사용자 정의 및 형식화할 수 있습니다. 이 기능은 텍스트와 이미지를 포함할 수 있어 문서 프레젠테이션의 유연성을 제공하며 전문적인 형식을 보장합니다. 사용자는 이 기능을 애플리케이션에 원활하게 통합하여 PDF 파일의 시각적 매력과 조직을 향상시킬 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1007",
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
    "url": "/net/manage-header-and-footer/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manage-header-and-footer/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## PDF 파일에 헤더 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스는 PDF 파일에 헤더를 추가할 수 있습니다. 헤더를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 객체를 생성해야 합니다. [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 클래스를 사용하여 헤더 텍스트의 형식을 지정할 수 있습니다. 파일에 헤더를 추가할 준비가 되면 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 메서드를 호출해야 합니다. 또한 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 메서드에서 최소한의 상단 여백을 지정해야 합니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에 헤더를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the header
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Yellow,
            System.Drawing.Color.Black,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add header
        fileStamp.AddHeader(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddHeader_out.pdf");
    }
}
```

## PDF 파일에 푸터 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스는 PDF 파일에 푸터를 추가할 수 있습니다. 푸터를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 객체를 생성해야 합니다. [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 클래스를 사용하여 푸터 텍스트의 형식을 지정할 수 있습니다. 파일에 푸터를 추가할 준비가 되면 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 메서드를 호출해야 합니다. 또한 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 메서드에서 최소한의 하단 여백을 지정해야 합니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에 푸터를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the footer
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add footer
        fileStamp.AddFooter(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddFooter_out.pdf");
    }
}
```

## 기존 PDF 파일의 헤더에 이미지 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스는 PDF 파일의 헤더에 이미지를 추가할 수 있습니다. 헤더에 이미지를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 객체를 생성해야 합니다. 그 후, [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 메서드를 호출해야 합니다. 이미지를 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 메서드에 전달할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 헤더에 이미지를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add Header
        using (var fs = new FileStream(dataDir + "ImageHeader.png", FileMode.Open))
        {
            fileStamp.AddHeader(fs, 10);  // Add image header with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageHeader_out.pdf");
        }
    }
}
```

## 기존 PDF 파일의 푸터에 이미지 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스는 PDF 파일의 푸터에 이미지를 추가할 수 있습니다. 푸터에 이미지를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 객체를 생성해야 합니다. 그 후, [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 메서드를 호출해야 합니다. 이미지를 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 메서드에 전달할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 푸터에 이미지를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add footer
        using (var fs = new FileStream(dataDir + "ImageFooter.png", FileMode.Open))
        {
            fileStamp.AddFooter(fs, 10);  // Add image footer with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageFooter_out.pdf");
        }
    }
}
```
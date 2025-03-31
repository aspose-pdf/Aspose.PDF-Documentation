---
title: 텍스트 및 이미지 스탬프 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/add-text-and-image-stamp/
description: 이 섹션에서는 PdfFileStamp 클래스를 사용하여 Aspose.PDF Facades로 텍스트 및 이미지 스탬프를 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text and Image Stamp",
    "alternativeHeadline": "Add Custom Text and Image Stamps in PDFs",
    "abstract": "Aspose.PDF for .NET의 텍스트 및 이미지 스탬프 추가 기능을 통해 사용자는 PDF 문서의 모든 페이지 또는 특정 페이지에 맞춤형 텍스트 및 이미지 스탬프를 원활하게 적용할 수 있습니다. 이 기능은 문서 개인화를 향상시켜 스탬프 속성(위치, 회전 및 품질 등)에 대한 세부적인 제어를 가능하게 하여 PDF 파일의 프레젠테이션 및 브랜딩을 개선합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1435",
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
    "url": "/net/add-text-and-image-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-and-image-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## PDF 파일의 모든 페이지에 텍스트 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 모든 페이지에 텍스트 스탬프를 추가할 수 있습니다. 텍스트 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 또한 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) 메서드를 사용하여 텍스트 스탬프를 생성해야 합니다. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 객체를 사용하여 원점, 회전, 배경 등의 다른 속성도 설정할 수 있습니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 모든 페이지에 텍스트 스탬프를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));

        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnAllPages_out.pdf");
    }
}
```

## PDF 파일의 특정 페이지에 텍스트 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 특정 페이지에 텍스트 스탬프를 추가할 수 있습니다. 텍스트 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 또한 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) 메서드를 사용하여 텍스트 스탬프를 생성해야 합니다. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 객체를 사용하여 원점, 회전, 배경 등의 다른 속성도 설정할 수 있습니다. PDF 파일의 특정 페이지에 텍스트 스탬프를 추가하려면 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) 속성도 설정해야 합니다. 이 속성은 스탬프를 추가할 페이지 번호를 포함하는 정수 배열을 요구합니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 특정 페이지에 텍스트 스탬프를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));
        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnParticularPages_out.pdf");
    }
}
```

## PDF 파일의 모든 페이지에 이미지 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 모든 페이지에 이미지 스탬프를 추가할 수 있습니다. 이미지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 또한 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) 메서드를 사용하여 이미지 스탬프를 생성해야 합니다. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 객체를 사용하여 원점, 회전, 배경 등의 다른 속성도 설정할 수 있습니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 모든 페이지에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnAllPages_out.pdf");
    }
}
```

### 스탬프 추가 시 이미지 품질 제어

이미지를 스탬프 객체로 추가할 때 이미지 품질도 제어할 수 있습니다. 이 요구 사항을 충족하기 위해 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스에 품질 속성이 추가되었습니다. 이는 이미지 품질을 백분율로 나타내며(유효 값은 0..100)입니다.

## PDF 파일의 특정 페이지에 이미지 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 특정 페이지에 이미지 스탬프를 추가할 수 있습니다. 이미지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 또한 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) 메서드를 사용하여 이미지 스탬프를 생성해야 합니다. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 객체를 사용하여 원점, 회전, 배경 등의 다른 속성도 설정할 수 있습니다. PDF 파일의 특정 페이지에 이미지 스탬프를 추가하려면 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) 속성도 설정해야 합니다. 이 속성은 스탬프를 추가할 페이지 번호를 포함하는 정수 배열을 요구합니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 특정 페이지에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnParticularPages_out.pdf");
    }
}
```
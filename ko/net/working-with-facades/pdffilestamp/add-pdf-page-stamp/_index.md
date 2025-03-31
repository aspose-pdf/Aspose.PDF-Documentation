---
title: PDF 페이지 스탬프 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/add-pdf-page-stamp/
description: Aspose.PDF를 사용하여 워터마크 또는 브랜딩을 위해 텍스트 및 이미지를 포함하여 .NET에서 PDF 페이지에 스탬프를 추가하는 방법을 알아보세요.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Page Stamp",
    "alternativeHeadline": "Enhance PDFs with Custom Stamps and Page Numbers",
    "abstract": "PdfFileStamp 클래스를 사용하여 PDF 문서의 모든 페이지 또는 특정 페이지에 사용자 정의 스탬프를 쉽게 추가할 수 있는 PDF 페이지 스탬프 기능을 소개합니다. 이 기능은 페이지 스탬프에 대한 회전, 배경 및 사용자 정의 번호 스타일과 같은 다양한 속성을 활성화하여 문서 개인화를 향상시켜 PDF 파일을 독특하고 전문적으로 다듬어 줍니다.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## PDF 파일의 모든 페이지에 PDF 페이지 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 모든 페이지에 PDF 페이지 스탬프를 추가할 수 있습니다. PDF 페이지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 또한 [Stamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf/stamp) 클래스의 [PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 메서드를 사용하여 PDF 페이지 스탬프를 생성해야 합니다. [Stamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf/stamp) 객체를 사용하여 원점, 회전, 배경 등의 다른 속성도 설정할 수 있습니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 모든 페이지에 PDF 페이지 스탬프를 추가하는 방법을 보여줍니다.

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

## PDF 파일의 특정 페이지에 PDF 페이지 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 특정 페이지에 PDF 페이지 스탬프를 추가할 수 있습니다. PDF 페이지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 또한 [Stamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf/stamp) 클래스의 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 PDF 페이지 스탬프를 생성해야 합니다. [Stamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf/stamp) 객체를 사용하여 원점, 회전, 배경 등의 다른 속성도 설정할 수 있습니다. PDF 파일의 특정 페이지에 PDF 페이지 스탬프를 추가하려면 [Stamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf/stamp) 클래스의 [Pages](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/stamp/properties/pages) 속성도 설정해야 합니다. 이 속성은 스탬프를 추가할 페이지 번호를 포함하는 정수 배열을 요구합니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 특정 페이지에 PDF 페이지 스탬프를 추가하는 방법을 보여줍니다.

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

## PDF 파일에 페이지 번호 추가

[PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일에 페이지 번호를 추가할 수 있습니다. 페이지 번호를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 클래스의 객체를 생성해야 합니다. 현재 페이지 번호가 X이고 PDF 파일의 총 페이지 수가 N인 경우 "페이지 X / N"과 같이 페이지 번호를 표시하려면 먼저 [PdfFileInfo](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileinfo) 클래스의 [NumberOfpages](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) 속성을 사용하여 페이지 수를 가져와야 합니다. 현재 페이지 번호를 가져오려면 텍스트의 원하는 위치에 **#** 기호를 사용할 수 있습니다. [FormattedText](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formattedtext) 클래스를 사용하여 페이지 번호 텍스트를 형식화할 수 있습니다. 특정 번호에서 페이지 번호 매기기를 시작하려면 [StartingNumber](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber) 속성을 설정할 수 있습니다. 파일에 페이지 번호를 추가할 준비가 되면 [PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddPageNumber](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) 메서드를 호출해야 합니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/facade/methods/close) 클래스의 [Close](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에 페이지 번호를 추가하는 방법을 보여줍니다.

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

### 사용자 정의 번호 매기기 스타일

PdfFileStamp 클래스는 PDF 문서 내에 스탬프 객체로 페이지 번호 정보를 추가하는 기능을 제공합니다. 이전 릴리스에서는 클래스가 페이지 번호 매기기 스타일로 1,2,3,4만 지원했습니다. 그러나 일부 고객의 요구에 따라 PDF 문서 내에 페이지 번호 스탬프를 배치할 때 사용자 정의 번호 매기기 스타일을 사용해야 했습니다. 이 요구 사항을 충족하기 위해 [NumberingStyle](https://reference.aspose.com/pdf/ko/net/aspose.pdf/numberingstyle) 속성이 도입되었으며, 이는 [NumberingStyle](https://reference.aspose.com/pdf/ko/net/aspose.pdf/numberingstyle) 열거형의 값을 허용합니다. 이 열거형에서 제공되는 값은 다음과 같습니다.

- LettersLowercase.
- LettersUppercase.
- NumeralsArabic.
- NumeralsRomanLowercase.
- NumeralsRomanUppercase.

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
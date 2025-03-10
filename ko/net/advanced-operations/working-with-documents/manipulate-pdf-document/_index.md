---
title: C#에서 PDF 문서 조작
linktitle: PDF 문서 조작
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/manipulate-pdf-document/
description: 이 문서에는 PDF A 표준에 대한 PDF 문서 검증 방법, TOC 작업 방법, PDF 만료 날짜 설정 방법 등이 포함되어 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate PDF Document in C#",
    "alternativeHeadline": "Enhanced PDF Manipulation Features in C# Library",
    "abstract": "C#에서 PDF 문서를 조작하는 강력한 기능을 발견하세요. PDF/A 표준 검증, 목차 생성 및 사용자 정의, 문서 만료 날짜 설정 등을 포함합니다. 이 기능은 문서 관리뿐만 아니라 산업 표준 준수를 보장하여 강력한 PDF 처리 솔루션을 찾는 개발자에게 필수적입니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "manipulate PDF, C#, validate PDF/A, TOC, set PDF expiry date, flatten fillable PDF, Aspose.PDF, PDF generation progress, customize page numbers, PDF encryption",
    "wordcount": "2170",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "이 문서에는 PDF A 표준에 대한 PDF 문서 검증 방법, TOC 작업 방법, PDF 만료 날짜 설정 방법 등이 포함되어 있습니다."
}
</script>

## **C#에서 PDF 문서 조작**

## PDF A 표준에 대한 PDF 문서 검증 (A 1A 및 A 1B)

PDF/A-1a 또는 PDF/A-1b 호환성을 위해 PDF 문서를 검증하려면 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 Validate 메서드를 사용하세요. 이 메서드는 결과를 저장할 파일의 이름과 필요한 검증 유형 [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat) 열거형: PDF_A_1A 또는 PDF_A_1B를 지정할 수 있습니다.

{{% alert color="primary" %}}

출력 XML 형식은 사용자 정의 Aspose 형식입니다. XML에는 Problem이라는 이름의 태그 모음이 포함되어 있으며, 각 태그는 특정 문제의 세부 정보를 포함합니다. Problem 태그의 ObjectID 속성은 이 문제와 관련된 특정 객체의 ID를 나타냅니다. Clause 속성은 PDF 사양의 해당 규칙을 나타냅니다.

{{% /alert %}}

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

다음 코드 조각은 PDF/A-1A에 대한 PDF 문서를 검증하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateToPdfA1aStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1a
        document.Validate(dataDir + "validation-result-A1A.xml", Aspose.Pdf.PdfFormat.PDF_A_1A);
    }
}
```

다음 코드 조각은 PDF/A-1b에 대한 PDF 문서를 검증하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateToPdfA1bStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1b
        document.Validate(dataDir + "validation-result-A1B.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
    }
}
```

{{% alert color="primary" %}}

Aspose.PDF for .NET은 로드된 문서가 유효한 PDF인지 여부를 결정하는 데 사용할 수 있으며, [암호화 여부](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/)도 확인할 수 있습니다. Document 클래스의 기능을 확장하기 위해 *IsPdfaCompliant* 속성이 추가되어 입력 파일이 PDF/A 준수 여부를 결정하고, *PdfaFormat*이라는 속성이 PDF/A 형식을 식별하는 데 도입되었습니다.

{{% /alert %}}

## TOC 작업하기

### 기존 PDF에 TOC 추가

Aspose.PDF API를 사용하면 PDF를 생성할 때 또는 기존 파일에 목차를 추가할 수 있습니다. Aspose.Pdf.Generator 네임스페이스의 ListSection 클래스는 PDF를 처음부터 생성할 때 목차를 만들 수 있게 해줍니다. TOC의 요소인 제목을 추가하려면 Aspose.Pdf.Generator.Heading 클래스를 사용하세요.

기존 PDF 파일에 TOC를 추가하려면 Aspose.PDF 네임스페이스의 Heading 클래스를 사용하세요. Aspose.Pdf 네임스페이스는 새 PDF를 생성하고 기존 PDF 파일을 조작할 수 있습니다. 기존 PDF 파일 내에 목차를 만드는 방법은 다음 코드 조각을 참조하세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTOCToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTOC.pdf"))
    {
        // Get access to the first page of PDF file
        var tocPage = document.Pages.Insert(1);

        // Create an object to represent TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Set the title for TOC
        tocInfo.Title = title;
        tocPage.TocInfo = tocInfo;

        // Create string objects which will be used as TOC elements
        string[] titles = { "First page", "Second page", "Third page", "Fourth page" };

        for (int i = 0; i < 2; i++)
        {
            // Create Heading object
            var heading = new Aspose.Pdf.Heading(1);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.TocPage = tocPage;
            heading.Segments.Add(segment);

            // Specify the destination page for the heading object
            heading.DestinationPage = document.Pages[i + 2];

            // Destination page
            heading.Top = document.Pages[i + 2].Rect.Height;

            // Destination coordinate
            segment.Text = titles[i];

            // Add heading to the page containing TOC
            tocPage.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### 다른 TOC 수준에 대해 다른 TabLeaderType 설정

Aspose.PDF는 또한 다른 TOC 수준에 대해 다른 TabLeaderType을 설정할 수 있습니다. FormatArray의 LineDash 속성을 TabLeaderType 열거형의 적절한 값으로 설정해야 합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTocWithCustomFormatting()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a TOC page
        var tocPage = document.Pages.Add();

        // Create TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();

        // Set LeaderType
        tocInfo.LineDash = Aspose.Pdf.Text.TabLeaderType.Solid;

        // Set the title for TOC
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 30;
        tocInfo.Title = title;

        // Add the TOC section to the document
        tocPage.TocInfo = tocInfo;

        // Define the format of the four levels list by setting the left margins
        // and text format settings of each level
        tocInfo.FormatArrayLength = 4;

        // Level 1
        tocInfo.FormatArray[0].Margin.Left = 0;
        tocInfo.FormatArray[0].Margin.Right = 30;
        tocInfo.FormatArray[0].LineDash = Aspose.Pdf.Text.TabLeaderType.Dot;
        tocInfo.FormatArray[0].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;

        // Level 2
        tocInfo.FormatArray[1].Margin.Left = 10;
        tocInfo.FormatArray[1].Margin.Right = 30;
        tocInfo.FormatArray[1].LineDash = Aspose.Pdf.Text.TabLeaderType.None;
        tocInfo.FormatArray[1].TextState.FontSize = 10;

        // Level 3
        tocInfo.FormatArray[2].Margin.Left = 20;
        tocInfo.FormatArray[2].Margin.Right = 30;
        tocInfo.FormatArray[2].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Level 4
        tocInfo.FormatArray[3].LineDash = Aspose.Pdf.Text.TabLeaderType.Solid;
        tocInfo.FormatArray[3].Margin.Left = 30;
        tocInfo.FormatArray[3].Margin.Right = 30;
        tocInfo.FormatArray[3].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create a section in the Pdf document
        var page = document.Pages.Add();

        // Add four headings in the section
        for (int level = 1; level <= 4; level++)
        {
            var heading = new Aspose.Pdf.Heading(level);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.Segments.Add(segment);
            heading.IsAutoSequence = true;
            heading.TocPage = tocPage;
            segment.Text = "Sample Heading " + level;
            heading.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial Unicode MS");

            // Add the heading into Table Of Contents.
            heading.IsInList = true;
            page.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### TOC에서 페이지 번호 숨기기

TOC에서 제목과 함께 페이지 번호를 표시하고 싶지 않은 경우 [TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) 클래스의 [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) 속성을 false로 설정할 수 있습니다. TOC에서 페이지 번호를 숨기기 위한 다음 코드 조각을 확인하세요:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTocWithHiddenPageNumbers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a TOC page
        var tocPage = document.Pages.Add();

        // Create TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();

        // Set the title for TOC
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        tocInfo.Title = title;

        // Add the TOC section to the document
        tocPage.TocInfo = tocInfo;

        // Hide page numbers in TOC
        tocInfo.IsShowPageNumbers = false;

        // Define the format of the four levels list by setting the left margins and
        // text format settings of each level
        tocInfo.FormatArrayLength = 4;

        // Level 1
        tocInfo.FormatArray[0].Margin.Right = 0;
        tocInfo.FormatArray[0].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;

        // Level 2
        tocInfo.FormatArray[1].Margin.Left = 30;
        tocInfo.FormatArray[1].TextState.Underline = true;
        tocInfo.FormatArray[1].TextState.FontSize = 10;

        // Level 3
        tocInfo.FormatArray[2].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Level 4
        tocInfo.FormatArray[3].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create a section in the Pdf document
        var page = document.Pages.Add();

        // Add four headings in the section
        for (int level = 1; level <= 4; level++)
        {
            var heading = new Aspose.Pdf.Heading(level);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.TocPage = tocPage;
            heading.Segments.Add(segment);
            heading.IsAutoSequence = true;
            segment.Text = "this is heading of level " + level;
            heading.IsInList = true;
            page.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### TOC 추가 시 페이지 번호 사용자 정의

PDF 문서에 TOC를 추가할 때 TOC의 페이지 번호를 사용자 정의하는 것이 일반적입니다. 예를 들어, 페이지 번호 앞에 P1, P2, P3와 같은 접두사를 추가해야 할 수 있습니다. 이 경우, Aspose.PDF for .NET은 페이지 번호를 사용자 정의하는 데 사용할 수 있는 TocInfo 클래스의 PageNumbersPrefix 속성을 제공합니다. 다음 코드 샘플을 참조하세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizePageNumbersAddingToC()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CustomizePageNumbersAddingToC.pdf"))
    {
        // Get access to first page of PDF file
        Page tocPage = document.Pages.Insert(1);

        // Create object to represent TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Set the title for TOC
        tocInfo.Title = title;
        tocInfo.PageNumbersPrefix = "P";
        tocPage.TocInfo = tocInfo;

        // Loop through the pages to create TOC entries
        for (int i = 1; i < document.Pages.Count; i++)
        {
            // Create Heading object
            var heading2 = new Aspose.Pdf.Heading(1);
            var segment2 = new Aspose.Pdf.Text.TextSegment();
            heading2.TocPage = tocPage;
            heading2.Segments.Add(segment2);

            // Specify the destination page for heading object
            heading2.DestinationPage = document.Pages[i + 1];

            // Destination page
            heading2.Top = document.Pages[i + 1].Rect.Height;

            // Destination coordinate
            segment2.Text = "Page " + i.ToString();

            // Add heading to page containing TOC
            tocPage.Paragraphs.Add(heading2);
        }

        // Save PDF document
        document.Save(dataDir + "CustomizePageNumbersAddingToC_out.pdf");
    }
}
```

## PDF 만료 날짜 설정 방법

PDF 파일에 접근 권한을 적용하여 특정 사용자 그룹이 PDF 문서의 특정 기능/객체에 접근할 수 있도록 합니다. PDF 파일 접근을 제한하기 위해 일반적으로 암호화를 적용하며, 사용자가 문서를 접근/보기할 때 PDF 파일 만료에 대한 유효한 알림을 받도록 PDF 파일 만료 날짜를 설정해야 할 수 있습니다.

위의 요구 사항을 달성하기 위해 *JavascriptAction* 객체를 사용할 수 있습니다. 다음 코드 조각을 참조하세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add text fragment to paragraphs collection of page object
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World..."));

        // Create JavaScript object to set PDF expiry date
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(
            "var year=2017;" +
            "var month=5;" +
            "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
            "expiry = new Date(year, month);" +
            "if (today.getTime() > expiry.getTime())" +
            "app.alert('The file is expired. You need a new one.');"
        );

        // Set JavaScript as PDF open action
        document.OpenAction = javaScript;

        // Save PDF Document
        document.Save(dataDir + "SetExpiryDate_out.pdf");
    }
}
```

## PDF 파일 생성 진행 상황 확인

고객이 PDF 파일 생성 진행 상황을 확인할 수 있는 기능을 추가해 달라고 요청했습니다. 이에 대한 응답은 다음과 같습니다.

[DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) 클래스의 [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) 필드는 PDF 생성 진행 상황을 확인할 수 있게 해줍니다. 핸들러는 다음과 같은 유형을 가집니다:

- DocSaveOptions.ConversionProgessEventHandler.
- DocSaveOptions.ProgressEventHandlerInfo.
- DocSaveOptions.ProgressEventType.

아래 코드 조각은 CustomerProgressHandler를 사용하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineProgress()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTOC.pdf"))
    {
        // Create DocSaveOptions instance and set custom progress handler
        var saveOptions = new Aspose.Pdf.DocSaveOptions();
        saveOptions.CustomProgressHandler = new Aspose.Pdf.UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

        // Save PDF Document
        document.Save(dataDir + "DetermineProgress_out.pdf", saveOptions);
    }
}

// Method to handle progress and display it on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Conversion progress : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            Console.WriteLine(String.Format("{0}  - Source page {1} of {2} analyzed.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Result page's {1} of {2} layout created.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Result page {1} of {2} exported.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }
}
```

## 작성 가능한 PDF 평탄화

PDF 문서에는 종종 라디오 버튼, 체크박스, 텍스트 상자, 목록 등과 같은 대화형 작성 가능한 위젯이 포함됩니다. 다양한 응용 프로그램 목적을 위해 편집할 수 없도록 PDF 파일을 평탄화해야 합니다. Aspose.PDF는 몇 줄의 코드로 C#에서 PDF를 평탄화하는 기능을 제공합니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Fillable PDF
        if (document.Form.Fields.Count() > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
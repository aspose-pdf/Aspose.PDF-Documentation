---
title: C#를 사용한 PDF 문서 포맷팅
linktitle: PDF 문서 포맷팅
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/formatting-pdf-document/
description: Aspose.PDF for .NET로 PDF 문서를 생성하고 포맷합니다. 다음 코드 스니펫을 사용하여 작업을 해결하세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatting Document using C#",
    "alternativeHeadline": "Enhance PDF Formatting with Aspose.PDF for .NET",
    "abstract": "사용자가 PDF 문서를 원활하게 생성하고 포맷할 수 있도록 하는 Aspose.PDF for .NET의 강력한 새로운 기능을 발견하세요. 창 표시 설정, 글꼴 포함 옵션 및 사용자 정의 가능한 확대/축소 비율과 같은 문서 속성에 대한 포괄적인 제어를 통해 개발자는 사용자 경험을 향상하고 다양한 플랫폼에서 문서 무결성을 유지할 수 있습니다. 이 강력한 기능으로 PDF 조작 작업을 최적화하여 .NET 애플리케이션의 효율성을 크게 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Formatting PDF Document, Aspose.PDF for .NET, PDF document properties, embed fonts, font substitution, set zoom factor, document window properties, PDF manipulation library, PDF document generation, C# PDF formatting",
    "wordcount": "2526",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET로 PDF 문서를 생성하고 포맷합니다. 다음 코드 스니펫을 사용하여 작업을 해결하세요."
}
</script>

## PDF 문서 포맷팅

### 문서 창 및 페이지 표시 속성 가져오기

이 주제는 문서 창, 뷰어 애플리케이션의 속성과 페이지가 표시되는 방식을 이해하는 데 도움이 됩니다. 이러한 속성을 설정하려면:

[Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 클래스를 사용하여 PDF 파일을 엽니다. 이제 Document 객체의 속성을 설정할 수 있습니다.

- CenterWindow – 화면 중앙에 문서 창을 배치합니다. 기본값: false.
- Direction – 읽기 순서. 페이지가 나란히 표시될 때 레이아웃을 결정합니다. 기본값: 왼쪽에서 오른쪽.
- DisplayDocTitle – 문서 창 제목 표시줄에 문서 제목을 표시합니다. 기본값: false (제목이 표시됨).
- HideMenuBar – 문서 창의 메뉴 바를 숨기거나 표시합니다. 기본값: false (메뉴 바가 표시됨).
- HideToolBar – 문서 창의 도구 모음을 숨기거나 표시합니다. 기본값: false (도구 모음이 표시됨).
- HideWindowUI – 스크롤 바와 같은 문서 창 요소를 숨기거나 표시합니다. 기본값: false (UI 요소가 표시됨).
- NonFullScreenPageMode – 전체 페이지 모드로 표시되지 않을 때 문서의 표시 방식.
- PageLayout – 페이지 레이아웃.
- PageMode – 문서를 처음 열 때 표시되는 방식. 옵션은 썸네일 표시, 전체 화면, 첨부 패널 표시입니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 클래스를 사용하여 속성을 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetDocumentWindow.pdf"))
    {
        // Get different document properties
        // Position of document's window - Default: false
        Console.WriteLine("CenterWindow : {0}", document.CenterWindow);

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        Console.WriteLine("Direction : {0}", document.Direction);

        // Whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        Console.WriteLine("DisplayDocTitle : {0}", document.DisplayDocTitle);

        // Whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        Console.WriteLine("FitWindow : {0}", document.FitWindow);

        // Whether to hide menu bar of the viewer application - Default: false
        Console.WriteLine("HideMenuBar : {0}", document.HideMenubar);

        // Whether to hide tool bar of the viewer application - Default: false
        Console.WriteLine("HideToolBar : {0}", document.HideToolBar);

        // Whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        Console.WriteLine("HideWindowUI : {0}", document.HideWindowUI);

        // Document's page mode. How to display document on exiting full-screen mode.
        Console.WriteLine("NonFullScreenPageMode : {0}", document.NonFullScreenPageMode);

        // The page layout i.e. single page, one column
        Console.WriteLine("PageLayout : {0}", document.PageLayout);

        // How the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        Console.WriteLine("PageMode : {0}", document.PageMode);
    }
}
```

### 문서 창 및 페이지 표시 속성 설정

이 주제는 문서 창, 뷰어 애플리케이션 및 페이지 표시의 속성을 설정하는 방법을 설명합니다. 이러한 다양한 속성을 설정하려면:

1. [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 클래스를 사용하여 PDF 파일을 엽니다.
1. Document 객체의 속성을 설정합니다.
1. Save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

사용 가능한 속성은 다음과 같습니다.

- CenterWindow.
- Direction.
- DisplayDocTitle.
- FitWindow.
- HideMenuBar.
- HideToolBar.
- HideWindowUI.
- NonFullScreenPageMode.
- PageLayout.
- PageMode.

각 속성은 아래 코드에서 사용되고 설명됩니다. 다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 클래스를 사용하여 속성을 설정하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetDocumentWindow.pdf"))
    {
        // Set different document properties
        // Specify to position document's window - Default: false
        document.CenterWindow = true;

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        document.Direction = Aspose.Pdf.Direction.R2L;

        // Specify whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        document.DisplayDocTitle = true;

        // Specify whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        document.FitWindow = true;

        // Specify whether to hide menu bar of the viewer application - Default: false
        document.HideMenubar = true;

        // Specify whether to hide tool bar of the viewer application - Default: false
        document.HideToolBar = true;

        // Specify whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        document.HideWindowUI = true;

        // Document's page mode. Specify how to display document on exiting full-screen mode.
        document.NonFullScreenPageMode = Aspose.Pdf.PageMode.UseOC;

        // Specify the page layout i.e. single page, one column
        document.PageLayout = Aspose.Pdf.PageLayout.TwoColumnLeft;

        // Specify how the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseThumbs;

        // Save PDF document
        document.Save(dataDir + "SetDocumentWindow_out.pdf");
    }
}
```

### 기존 PDF 파일에 글꼴 포함하기

PDF 리더는 문서가 표시되는 플랫폼에 관계없이 문서가 동일한 방식으로 표시될 수 있도록 [14개의 핵심 글꼴](https://en.wikipedia.org/wiki/PDF#Text)을 지원합니다. PDF에 14개의 핵심 글꼴 중 하나가 아닌 글꼴이 포함된 경우, 글꼴 대체를 피하기 위해 PDF 파일에 글꼴을 포함해야 합니다.

Aspose.PDF for .NET은 기존 PDF 파일에 글꼴 포함을 지원합니다. 전체 글꼴 또는 글꼴의 하위 집합을 포함할 수 있습니다. 글꼴을 포함하려면 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 클래스를 사용하여 PDF 파일을 엽니다. 그런 다음 [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text) 클래스를 사용하여 PDF 파일에 글꼴을 포함합니다. 전체 글꼴을 포함하려면 Font 클래스의 IsEmbeded 속성을 사용하고, 글꼴의 하위 집합을 사용하려면 IsSubset 속성을 사용합니다.

{{% alert color="primary" %}}

글꼴 하위 집합은 사용된 문자만 포함하며, 예를 들어 로고에 기업 글꼴이 사용되지만 본문 텍스트에는 사용되지 않는 경우와 같이 짧은 문장이나 슬로건에 유용합니다. 하위 집합을 사용하면 출력 PDF의 파일 크기가 줄어듭니다. 그러나 본문 텍스트에 사용자 정의 글꼴이 사용되는 경우, 전체 글꼴을 포함해야 합니다.

{{% /alert %}}

다음 코드 스니펫은 PDF 파일에 글꼴을 포함하는 방법을 보여줍니다.

### 표준 타입 1 글꼴 포함하기

일부 PDF 문서에는 특별한 Adobe 글꼴 세트의 글꼴이 포함되어 있습니다. 이 세트의 글꼴을 "표준 타입 1 글꼴"이라고 합니다. 이 세트에는 14개의 글꼴이 포함되어 있으며, 이러한 유형의 글꼴을 포함하려면 특별한 플래그인 [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/properties/embedstandardfonts)를 사용해야 합니다. 다음은 표준 타입 1 글꼴을 포함하여 모든 글꼴이 포함된 문서를 얻기 위해 사용할 수 있는 코드 스니펫입니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontsType1ToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set EmbedStandardFonts property of document
        document.EmbedStandardFonts = true;

        // Iterate through each page
        foreach (var page in document.Pages)
        {
            if (page.Resources.Fonts != null)
            {
                foreach (var pageFont in page.Resources.Fonts)
                {
                    // Check if font is already embedded
                    if (!pageFont.IsEmbedded)
                    {
                        pageFont.IsEmbedded = true;
                    }
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "EmbeddedFontsUpdated_out.pdf");
    }
}
```

### PDF 생성 시 글꼴 포함하기

Adobe Reader에서 지원하는 14개의 핵심 글꼴 외에 다른 글꼴을 사용해야 하는 경우, PDF 파일을 생성할 때 글꼴 설명을 포함해야 합니다. 글꼴 정보가 포함되지 않으면 Adobe Reader는 시스템에 설치된 경우 운영 체제에서 가져오거나 PDF의 글꼴 설명에 따라 대체 글꼴을 구성합니다.

>포함된 글꼴은 호스트 머신에 설치되어 있어야 합니다. 즉, 다음 코드에서 'Univers Condensed' 글꼴이 시스템에 설치되어 있어야 합니다.

우리는 Font 클래스의 IsEmbedded 속성을 사용하여 PDF 파일에 글꼴 정보를 포함합니다. 이 속성의 값을 'True'로 설정하면 전체 글꼴 파일이 PDF에 포함되며, 이는 PDF 파일 크기를 증가시킵니다. 다음은 PDF에 글꼴 정보를 포함하는 데 사용할 수 있는 코드 스니펫입니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontWhileCreatingPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create a section in the Pdf object
        var page = document.Pages.Add();

        // Create a TextFragment
        var fragment = new Aspose.Pdf.Text.TextFragment("");

        // Create a TextSegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" This is a sample text using Custom font.");

        // Create and configure TextState
        var ts = new Aspose.Pdf.Text.TextState();
        ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        ts.Font.IsEmbedded = true;
        segment.TextState = ts;

        // Add the segment to the fragment
        fragment.Segments.Add(segment);

        // Add the fragment to the page
        page.Paragraphs.Add(fragment);

        // Save PDF Document
        document.Save(dataDir + "EmbedFontWhileDocCreation_out.pdf");
    }
}
```

### PDF 저장 시 기본 글꼴 이름 설정

PDF 문서에 글꼴이 포함되어 있지만 문서 자체와 장치에서 사용할 수 없는 경우, API는 이러한 글꼴을 기본 글꼴로 대체합니다. 글꼴이 사용 가능한 경우(장치에 설치되거나 문서에 포함된 경우), 출력 PDF는 동일한 글꼴을 가져야 합니다(기본 글꼴로 대체되지 않아야 함). 기본 글꼴의 값은 글꼴의 이름(글꼴 파일 경로가 아님)을 포함해야 합니다. 문서를 PDF로 저장할 때 기본 글꼴 이름을 설정하는 기능을 구현했습니다. 다음 코드 스니펫을 사용하여 기본 글꼴을 설정할 수 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDefaultFontOnDocumentSave(string documentName, string newName)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var fs = new FileStream(dataDir + "GetDocumentWindow.pdf", FileMode.Open))
    {
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create PdfSaveOptions and specify Default Font Name
            var pdfSaveOptions = new Aspose.Pdf.PdfSaveOptions
            {
                DefaultFontName = newName
            };

            // Save PDF document
            document.Save(dataDir + "DefaultFont_out.pdf", pdfSaveOptions);
        }
    }
}
```

### PDF 문서에서 모든 글꼴 가져오기

PDF 문서에서 모든 글꼴을 가져오려면 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 클래스에서 제공하는 FontUtilities.GetAllFonts() 메서드를 사용할 수 있습니다. 기존 PDF 문서에서 모든 글꼴을 가져오기 위한 다음 코드 스니펫을 확인하세요:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllFontsFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get all fonts used in the document
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through each font and print its name
        foreach (var font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```

### 글꼴 대체에 대한 경고 가져오기

Aspose.PDF for .NET은 글꼴 대체 사례를 처리하기 위해 글꼴 대체에 대한 알림을 받을 수 있는 메서드를 제공합니다. 아래 코드 스니펫은 해당 기능을 사용하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void NotificationFontSubstitution()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Attach the FontSubstitution event handler
        document.FontSubstitution += OnFontSubstitution;
        // You can use lambda
        // (oldFont, newFont) => Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        //                                                                        oldFont.FontName, newFont.FontName));

        // Save PDF document
        document.Save(dataDir + "NotificationFontSubstitution_out.pdf");
    }
}
```

**OnFontSubstitution** 메서드는 아래와 같습니다.

```csharp
private static void OnFontSubstitution(Aspose.Pdf.Text.Font oldFont, Aspose.Pdf.Text.Font newFont)
{
    // Handle the font substitution event here
    Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        oldFont.FontName, newFont.FontName));
}
```

### FontSubsetStrategy를 사용하여 글꼴 포함 개선하기

하위 집합으로 글꼴을 포함하는 기능은 IsSubset 속성을 사용하여 수행할 수 있지만, 때때로 전체 포함된 글꼴 세트를 문서에서 사용되는 하위 집합으로 줄이고 싶을 수 있습니다. Aspose.Pdf.Document에는 FontUtilities 속성이 있으며, 여기에는 SubsetFonts(FontSubsetStrategy subsetStrategy) 메서드가 포함되어 있습니다. SubsetFonts() 메서드에서 subsetStrategy 매개변수는 하위 집합 전략을 조정하는 데 도움이 됩니다. FontSubsetStrategy는 다음 두 가지 글꼴 하위 집합 변형을 지원합니다.

- SubsetAllFonts - 문서에서 사용된 모든 글꼴을 하위 집합으로 만듭니다.
- SubsetEmbeddedFontsOnly - 문서에 완전히 포함된 글꼴만 하위 집합으로 만듭니다.

다음 코드 스니펫은 FontSubsetStrategy를 설정하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFontSubsetStrategy()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // All fonts will be embedded as subset into document in case of SubsetAllFonts.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetAllFonts);

        // Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetEmbeddedFontsOnly);

        // Save PDF document
        document.Save(dataDir + "SetFontSubsetStrategy_out.pdf");
    }
}
```

### PDF 파일의 확대/축소 비율 가져오기 및 설정하기

때때로 PDF 문서의 현재 확대/축소 비율을 확인하고 싶을 수 있습니다. Aspose.Pdf를 사용하면 현재 값을 확인하고 설정할 수 있습니다.

[GoToAction](https://reference.aspose.com/pdf/ko/net/aspose.pdf.annotations/gotoaction) 클래스의 Destination 속성을 사용하여 PDF 파일과 관련된 확대/축소 값을 가져올 수 있습니다. 마찬가지로 파일의 확대/축소 비율을 설정하는 데 사용할 수 있습니다.

#### 확대/축소 비율 설정

다음 코드 스니펫은 PDF 파일의 확대/축소 비율을 설정하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetZoomFactor.pdf"))
    {
        // Create GoToAction with a specific zoom factor
        var action = new Aspose.Pdf.Annotations.GoToAction(new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 0, 0, 0.5));
        document.OpenAction = action;

        // Save PDF document
        document.Save(dataDir + "ZoomFactor_out.pdf");
    }
}
```

#### 확대/축소 비율 가져오기

다음 코드 스니펫은 PDF 파일의 확대/축소 비율을 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Zoomed_pdf.pdf"))
    {
        // Create GoToAction object
        if (document.OpenAction is Aspose.Pdf.Annotations.GoToAction action)
        {
            // Get the Zoom factor of PDF file
            if (action.Destination is Aspose.Pdf.Annotations.XYZExplicitDestination destination)
            {
                System.Console.WriteLine(destination.Zoom); // Document zoom value;
            }
        }
    }
}
```

### 인쇄 대화 상자 미리 설정 속성 설정

Aspose.PDF는 PDF 문서의 인쇄 대화 상자 미리 설정 속성을 설정할 수 있습니다. 기본적으로 단면으로 설정된 PDF 문서의 DuplexMode 속성을 변경할 수 있습니다. 이는 아래에 표시된 두 가지 방법론을 사용하여 달성할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Set duplex printing to DuplexFlipLongEdge
        document.Duplex = Aspose.Pdf.PrintDuplex.DuplexFlipLongEdge;

        // Save PDF document
        document.Save(dataDir + "SetPrintDlgPresetProperties_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
    }
}
```

### PDF 콘텐츠 편집기를 사용하여 인쇄 대화 상자 미리 설정 속성 설정

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetPropertiesUsingPdfContentEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    string inputFile = dataDir + "input.pdf";

    using (var ed = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        ed.BindPdf(inputFile);

        // Check if the file has duplex flip short edge
        if ((ed.GetViewerPreference() & Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge) > 0)
        {
            Console.WriteLine("The file has duplex flip short edge");
        }

        // Change the viewer preference to duplex flip short edge
        ed.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge);

        // Save PDF document
        ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
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
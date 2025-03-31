---
title: C#를 사용하여 PDF에 텍스트 추가
linktitle: PDF에 텍스트 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/add-text-to-pdf-file/
description: Aspose.PDF를 사용하여 .NET에서 PDF 문서에 텍스트를 추가하는 방법을 배우고 콘텐츠 향상 및 문서 편집을 수행합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text to PDF using C#",
    "alternativeHeadline": "Add Custom Text to Existing PDFs with C#",
    "abstract": "Aspose.PDF의 C#을 사용하여 PDF에 텍스트 추가 기능은 개발자가 기존 PDF 문서 내에서 텍스트를 원활하게 통합하고 조작할 수 있도록 합니다. 텍스트 조각 추가, 사용자 정의 OTF 글꼴 사용, HTML 콘텐츠 추가와 같은 기능을 통해 이 기능은 문서 형식 및 프레젠테이션을 향상시켜 전문적이고 맞춤화된 PDF를 프로그래밍 방식으로 쉽게 생성할 수 있게 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "5625",
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
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "이 문서에서는 Aspose.PDF에서 텍스트 작업의 다양한 측면을 설명합니다. PDF에 텍스트를 추가하고, HTML 조각을 추가하거나, 사용자 정의 OTF 글꼴을 사용하는 방법을 배우십시오."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

기존 PDF 파일에 텍스트를 추가하려면:

1. Document 객체를 사용하여 입력 PDF를 엽니다.
2. 텍스트를 추가할 특정 페이지를 가져옵니다.
3. 입력 텍스트와 기타 텍스트 속성을 사용하여 TextFragment 객체를 생성합니다. 텍스트를 추가할 특정 페이지에서 생성된 TextBuilder 객체를 사용하여 AppendText 메서드를 사용하여 페이지에 TextFragment 객체를 추가할 수 있습니다.
4. Document 객체의 Save 메서드를 호출하고 출력 PDF 파일을 저장합니다.

## 텍스트 추가

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();

        // Create text fragment
        var textFragment = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Set text properties
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);

        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "AddText_out.pdf");
    }
}
```

## 스트림에서 글꼴 로드

다음 코드 스니펫은 PDF 문서에 텍스트를 추가할 때 스트림 객체에서 글꼴을 로드하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LoadingFontFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    var fontFile = dataDir + "HPSimplified.ttf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "LoadFonts.pdf"))
    {
        // Create text builder object for first page of document
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // Create text fragment with sample string
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello world");

        if (File.Exists(fontFile))
        {
            // Load the TrueType font into stream object
            using (FileStream fontStream = File.OpenRead(fontFile))
            {
                // Set the font name for text string
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(fontStream, Aspose.Pdf.Text.FontTypes.TTF);
                // Specify the position for Text Fragment
                textFragment.Position = new Aspose.Pdf.Text.Position(10, 10);
                // Add the text to TextBuilder so that it can be placed over the PDF file
                textBuilder.AppendText(textFragment);
            }

            // Save PDF document
            document.Save(dataDir + "LoadingFontFromStream_out.pdf");
        }
    }
}
```

## TextParagraph를 사용하여 텍스트 추가

다음 코드 스니펫은 [TextParagraph](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text/textparagraph) 클래스를 사용하여 PDF 문서에 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextWithTextParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document object
        var page = document.Pages.Add();
        var builder = new Aspose.Pdf.Text.TextBuilder(page);
        // Create text paragraph
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        // Set subsequent lines indent
        paragraph.SubsequentLinesIndent = 20;
        // Specify the location to add TextParagraph
        paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
        // Specify word wraping mode
        paragraph.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        // Create text fragment
        var fragment = new Aspose.Pdf.Text.TextFragment("the quick brown fox jumps over the lazy dog");
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        fragment.TextState.FontSize = 12;
        // Add fragment to paragraph
        paragraph.AppendLine(fragment);
        // Add paragraph
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "AddTextUsingTextParagraph_out.pdf");
    }
}
```

## TextSegment에 하이퍼링크 추가

PDF 페이지는 하나 이상의 TextFragment 객체로 구성될 수 있으며, 각 TextFragment 객체는 하나 이상의 TextSegment 인스턴스를 가질 수 있습니다. TextSegment에 하이퍼링크를 설정하려면 [TextSegment](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text/textsegment) 클래스의 Hyperlink 속성을 사용하여 Aspose.Pdf.WebHyperlink 인스턴스의 객체를 제공할 수 있습니다. 이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용해 보십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlinkToTextSegment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instance
        var fragment = new Aspose.Pdf.Text.TextFragment("Sample Text Fragment");
        // Set horizontal alignment for TextFragment
        fragment.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        // Create a textsegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" ... Text Segment 1...");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Create a new TextSegment
        segment = new Aspose.Pdf.Text.TextSegment("Link to Google");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Set hyperlink for TextSegment
        segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
        // Set forground color for text segment
        segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
        // Set text formatting as italic
        segment.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        // Create another TextSegment object
        segment = new Aspose.Pdf.Text.TextSegment("TextSegment without hyperlink");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Add TextFragment to paragraphs collection of page object
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "AddHyperlinkToTextSegment_out.pdf");
    }
}
```

## OTF 글꼴 사용

Aspose.PDF for .NET은 PDF 파일 콘텐츠를 생성/조작할 때 사용자 정의/TrueType 글꼴을 사용할 수 있는 기능을 제공하여 파일 콘텐츠가 기본 시스템 글꼴 이외의 콘텐츠로 표시되도록 합니다. Aspose.PDF for .NET 10.3.0의 시작 릴리스부터 Open Type Fonts에 대한 지원을 제공했습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UseOTFFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instnace with sample text
        var fragment = new Aspose.Pdf.Text.TextFragment("Sample Text in OTF font");
        // Find font inside system font directory
        // Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
        // Or you can even specify the path of OTF font in system directory
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(dataDir + "space age.otf");
        // Specify to emend font inside PDF file, so that its displayed properly,
        // Even if specific font is not installed/present over target machine
        fragment.TextState.Font.IsEmbedded = true;
        // Add TextFragment to paragraphs collection of Page instance
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "OTFFont_out.pdf");
    }
}
```

## DOM을 사용하여 HTML 문자열 추가

Aspose.Pdf.Generator.Text 클래스에는 PDF 파일에 HTML 태그/내용을 추가할 수 있는 IsHtmlTagSupported라는 속성이 포함되어 있습니다. 추가된 콘텐츠는 단순한 텍스트 문자열로 나타나는 대신 기본 HTML 태그로 렌더링됩니다. Aspose.Pdf 네임스페이스의 새로운 Document Object Model (DOM)에서 유사한 기능을 지원하기 위해 HtmlFragment 클래스가 도입되었습니다.

[HtmlFragment](https://reference.aspose.com/pdf/ko/net/aspose.pdf/htmlfragment) 인스턴스를 사용하여 PDF 파일 내에 배치할 HTML 콘텐츠를 지정할 수 있습니다. TextFragment와 유사하게 HtmlFragment는 단락 수준 객체이며 Page 객체의 단락 컬렉션에 추가할 수 있습니다. 다음 코드 스니펫은 DOM 접근 방식을 사용하여 PDF 파일 내에 HTML 콘텐츠를 배치하는 단계를 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLStringUsingDOM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a page to pages collection of PDF file
        var page = document.Pages.Add();
        // Instantiate HtmlFragment with HTML contnets
        var title = new Aspose.Pdf.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
        // Set bottom margin information
        title.Margin.Bottom = 10;
        // Set top margin information
        title.Margin.Top = 200;
        // Add HTML Fragment to paragraphs collection of page
        page.Paragraphs.Add(title);

        // Save PDF document
        document.Save(dataDir + "AddHTMLUsingDOM_out.pdf");
    }
}
```

다음 코드 스니펫은 문서에 HTML 정렬 목록을 추가하는 단계를 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLOrderedListIntoDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Instantiate HtmlFragment object with corresponding HTML fragment 
        var fragment = new Aspose.Pdf.HtmlFragment("`<body style='line-height: 100px;'><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul>Text after the list.<br/>Next line<br/>Last line</body>`");
        // Add Page in Pages Collection 
        var page = document.Pages.Add();
        // Add HtmlFragment inside page 
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
    }
}
```

TextState 객체를 사용하여 HTML 문자열 형식을 설정할 수도 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetHTMLStringFormatting()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var fragment = new Aspose.Pdf.HtmlFragment("some text");
        fragment.TextState = new Aspose.Pdf.Text.TextState();
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Calibri");
        // Add Page in Pages Collection 
        var page = document.Pages.Add();
        // Add HtmlFragment inside page 
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "SetHTMLStringFormatting_out.pdf");
    }
}
```

HTML 마크업을 통해 일부 텍스트 속성 값을 설정한 경우 TextState 속성에서 동일한 값을 제공하면 TextState 인스턴스의 속성에 의해 HTML 매개변수가 덮어쓰여집니다. 다음 코드 스니펫은 설명된 동작을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLUsingDOMAndOverwrite()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a page to pages collection of PDF file
        var page = document.Pages.Add();
        // Instantiate HtmlFragment with HTML contnets
        var title = new Aspose.Pdf.HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
        //Font-family from 'Verdana' will be reset to 'Arial'
        title.TextState = new Aspose.Pdf.Text.TextState("Arial");
        title.TextState.FontSize = 20;
        // Set bottom margin information
        title.Margin.Bottom = 10;
        // Set top margin information
        title.Margin.Top = 400;
        // Add HTML Fragment to paragraphs collection of page
        page.Paragraphs.Add(title);
        
        // Save PDF document
        document.Save(dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
    }
}
```

## 각주 및 미주 (DOM)

각주는 연속적인 위 첨자 번호를 사용하여 논문 텍스트의 주석을 나타냅니다. 실제 주석은 들여쓰기가 되어 있으며 페이지 하단에 각주로 나타날 수 있습니다.

### 각주 추가

각주 참조 시스템에서 참조를 나타내려면:

- 출처 자료 바로 뒤에 오는 텍스트 줄 위에 작은 숫자를 넣습니다. 이 숫자를 주석 식별자라고 합니다. 텍스트 줄보다 약간 위에 위치합니다.
- 페이지 하단에 동일한 숫자와 출처 인용을 넣습니다. 각주는 숫자 순서로 되어야 하며: 첫 번째 참조는 1, 두 번째는 2 등입니다.

각주의 장점은 독자가 관심 있는 참조의 출처를 찾기 위해 페이지 아래를 간단히 살펴볼 수 있다는 것입니다.

각주를 생성하려면 아래의 단계를 따르십시오:

- Document 인스턴스를 생성합니다.
- Page 객체를 생성합니다.
- TextFragment 객체를 생성합니다.
- Note 인스턴스를 생성하고 그 값을 TextFragment.FootNote 속성에 전달합니다.
- TextFragment를 페이지 인스턴스의 단락 컬렉션에 추가합니다.

### 각주에 대한 사용자 정의 선 스타일

다음 예제는 PDF 페이지 하단에 각주를 추가하고 사용자 정의 선 스타일을 정의하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomLineStyleForFootNote()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create GraphInfo object
        var graph = new Aspose.Pdf.GraphInfo();
        // Set line width as 2
        graph.LineWidth = 2;
        // Set the color for graph object
        graph.Color = Aspose.Pdf.Color.Red;
        // Set dash array value as 3
        graph.DashArray = new int[] { 3 };
        // Set dash phase value as 1
        graph.DashPhase = 1;
        // Set footnote line style for page as graph
        page.NoteLineStyle = graph;
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);
        // Create second TextFragment
        text = new Aspose.Pdf.Text.TextFragment("Aspose.PDF for .NET");
        // Set FootNote for second text fragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 2");
        // Add second text fragment to paragraphs collection of PDF file
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CustomLineStyleForFootNote_out.pdf");
    }
}
```

각주 레이블(주석 식별자) 형식을 TextState 객체를 사용하여 다음과 같이 설정할 수 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FormattingUsingTextStateObject()
{
    var text = new Aspose.Pdf.Text.TextFragment("test text 1");
    text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
    text.FootNote.Text = "21";
    text.FootNote.TextState = new Aspose.Pdf.Text.TextState();
    text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    text.FootNote.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
}
```

### 각주 레이블 사용자 정의

기본적으로 각주 번호는 1부터 시작하여 증가합니다. 그러나 사용자 정의 각주 레이블을 설정해야 할 수도 있습니다. 이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용해 보십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizeFootNoteLabel()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create GraphInfo object
        var graph = new Aspose.Pdf.GraphInfo();
        // Set line width as 2
        graph.LineWidth = 2;
        // Set the color for graph object
        graph.Color = Aspose.Pdf.Color.Red;
        // Set dash array value as 3
        graph.DashArray = new int[] { 3 };
        // Set dash phase value as 1
        graph.DashPhase = 1;
        // Set footnote line style for page as graph
        page.NoteLineStyle = graph;
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
        // Specify custom label for FootNote
        text.FootNote.Text = " Aspose(2015)";
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CustomizeFootNoteLabel_out.pdf");
    }
}
```

## 각주에 이미지 및 표 추가

이전 릴리스 버전에서는 각주 지원이 제공되었지만 TextFragment 객체에만 적용되었습니다. 그러나 Aspose.PDF for .NET 10.7.0 릴리스부터는 PDF 문서 내의 다른 객체(예: 표, 셀 등)에 각주를 추가할 수 있습니다. 다음 코드 스니펫은 TextFragment 객체에 각주를 추가한 다음 각주 섹션의 단락 컬렉션에 이미지 및 표 객체를 추가하는 단계를 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageAndTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var text = new Aspose.Pdf.Text.TextFragment("some text");
        page.Paragraphs.Add(text);

        text.FootNote = new Aspose.Pdf.Note();
        // Create image
        Aspose.Pdf.Image image = new Aspose.Pdf.Image();
        image.File = dataDir + "aspose-logo.jpg";
        image.FixHeight = 20;
        text.FootNote.Paragraphs.Add(image);

        var footNote = new Aspose.Pdf.Text.TextFragment("footnote text");
        footNote.TextState.FontSize = 20;
        footNote.IsInLineParagraph = true;
        text.FootNote.Paragraphs.Add(footNote);

        var table = new Aspose.Pdf.Table();
        table.Rows.Add().Cells.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Row 1 Cell 1"));
        text.FootNote.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddImageAndTable_out.pdf");
    }
}
```

## 미주 생성 방법

미주는 독자가 논문의 끝에서 정보 또는 인용된 단어의 출처를 찾을 수 있는 특정 장소를 참조하는 출처 인용입니다. 미주를 사용할 때 인용된 문장이나 요약된 자료 뒤에는 위 첨자 번호가 옵니다.

다음 예제는 PDF 페이지에 미주를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateEndNotes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.EndNote = new Aspose.Pdf.Note("sample End note");
        // Specify custom label for FootNote
        text.EndNote.Text = " Aspose(2015)";
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateEndNotes_out.pdf");
    }
}
```

## 텍스트와 이미지를 인라인 단락으로

PDF 파일의 기본 레이아웃은 흐름 레이아웃(왼쪽 상단에서 오른쪽 하단으로)입니다. 따라서 PDF 파일에 추가되는 모든 새로운 요소는 오른쪽 하단 흐름에 추가됩니다. 그러나 이미지와 텍스트와 같은 다양한 페이지 요소를 동일한 수준(서로 뒤따라)으로 표시해야 할 수도 있습니다. 한 가지 접근 방식은 Table 인스턴스를 생성하고 두 요소를 개별 셀 객체에 추가하는 것입니다. 그러나 또 다른 접근 방식은 인라인 단락입니다. 이미지와 텍스트의 IsInLineParagraph 속성을 true로 설정하면 이러한 단락이 다른 페이지 요소에 인라인으로 나타납니다.

다음 코드 스니펫은 PDF 파일에 텍스트와 이미지를 인라인 단락으로 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextAndImageAsParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document instance
        var page = document.Pages.Add();
        // Create TextFragmnet
        var text = new Aspose.Pdf.Text.TextFragment("Hello World.. ");
        // Add text fragment to paragraphs collection of Page object
        page.Paragraphs.Add(text);
        // Create an image instance
        var image = new Aspose.Pdf.Image();
        // Set image as inline paragraph so that it appears right after
        // The previous paragraph object (TextFragment)
        image.IsInLineParagraph = true;
        // Specify image file path
        image.File = dataDir + "aspose-logo.jpg";
        // Set image Height (optional)
        image.FixHeight = 30;
        // Set Image Width (optional)
        image.FixWidth = 100;
        // Add image to paragraphs collection of page object
        page.Paragraphs.Add(image);
        // Re-initialize TextFragment object with different contents
        text = new Aspose.Pdf.Text.TextFragment(" Hello Again..");
        // Set TextFragment as inline paragraph
        text.IsInLineParagraph = true;
        // Add newly created TextFragment to paragraphs collection of page
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "TextAndImageAsParagraph_out.pdf");
    }
}
```

## 텍스트 추가 시 문자 간격 지정

텍스트는 TextFragment 인스턴스 또는 TextParagraph 객체를 사용하여 PDF 파일의 단락 컬렉션 내에 추가할 수 있으며, TextStamp 클래스를 사용하여 PDF 내에 텍스트를 스탬프할 수도 있습니다. 텍스트를 추가할 때 텍스트 객체의 문자 간격을 지정해야 할 수도 있습니다. 이 요구 사항을 충족하기 위해 CharacterSpacing라는 새로운 속성이 도입되었습니다. 다음 접근 방식을 통해 이 요구 사항을 충족하는 단계를 살펴보십시오.

다음 접근 방식은 PDF 문서에 텍스트를 추가할 때 문자 간격을 지정하는 단계를 보여줍니다.

### TextBuilder 및 TextFragment 사용

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextBuilderAndFragment()
{            
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        document.Pages.Add();
        // Create TextBuilder instance
        var builder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // Create text fragment instance with sample contents
        var wideFragment = new Aspose.Pdf.Text.TextFragment("Text with increased character spacing");
        wideFragment.TextState.ApplyChangesFrom(new Aspose.Pdf.Text.TextState("Arial", 12));
        // Specify character spacing for TextFragment
        wideFragment.TextState.CharacterSpacing = 2.0f;
        // Specify the position of TextFragment
        wideFragment.Position = new Aspose.Pdf.Text.Position(100, 650);
        // Append TextFragment to TextBuilder instance
        builder.AppendText(wideFragment);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
    }
}
```

### TextParagraph 사용

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextBuilderAndParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        var page = document.Pages.Add();
        // Create TextBuilder instance
        var builder = new Aspose.Pdf.Text.TextBuilder(page);
        // Instantiate TextParagraph instance
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        // Create TextState instance to specify font name and size
        var state = new Aspose.Pdf.Text.TextState("Arial", 12);
        // Specify the character spacing
        state.CharacterSpacing = 1.5f;
        // Append text to TextParagraph object
        paragraph.AppendLine("This is paragraph with character spacing", state);
        // Specify the position for TextParagraph
        paragraph.Position = new Aspose.Pdf.Text.Position(100, 550);
        // Append TextParagraph to TextBuilder instance
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
    }
}
```

### TextStamp 사용

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        var page = document.Pages.Add();
        // Instantiate TextStamp instance with sample text
        var stamp = new Aspose.Pdf.TextStamp("This is text stamp with character spacing");
        // Specify font name for Stamp object
        stamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        // Specify Font size for TextStamp
        stamp.TextState.FontSize = 12;
        // Specify character specing as 1f
        stamp.TextState.CharacterSpacing = 1f;
        // Set the XIndent for Stamp
        stamp.XIndent = 100;
        // Set the YIndent for Stamp
        stamp.YIndent = 500;
        // Add textual stamp to page instance
        stamp.Put(page);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextStamp_out.pdf");
    }
}
```

## 다중 열 PDF 문서 생성

잡지와 신문에서는 뉴스가 일반적으로 책에서처럼 왼쪽에서 오른쪽으로 전체 페이지에 인쇄되는 대신 단일 페이지에 여러 열로 표시되는 것을 자주 볼 수 있습니다. Microsoft Word 및 Adobe Acrobat Writer와 같은 많은 문서 처리 응용 프로그램은 사용자가 단일 페이지에서 여러 열을 생성한 다음 데이터를 추가할 수 있도록 합니다.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) 또한 PDF 문서의 페이지 내에서 여러 열을 생성하는 기능을 제공합니다. 다중 열 PDF 파일을 생성하기 위해 Aspose.Pdf.FloatingBox 클래스를 사용할 수 있으며, 이 클래스는 FloatingBox 내의 열 수를 지정하기 위해 ColumnInfo.ColumnCount 속성을 제공하며, ColumnInfo.ColumnSpacing 및 ColumnInfo.ColumnWidths 속성을 사용하여 열 간격 및 열 너비를 지정할 수 있습니다. FloatingBox는 Document Object Model 내의 요소이며 상대적 위치 지정(예: 텍스트, 그래프, 이미지 등)에 비해 구식 위치 지정을 가질 수 있습니다.

열 간격은 열 사이의 공간을 의미하며 기본 열 간격은 1.25cm입니다. 열 너비가 지정되지 않은 경우 [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)은 페이지 크기 및 열 간격에 따라 각 열의 너비를 자동으로 계산합니다.

다음 예제는 그래프 객체(선)를 사용하여 두 개의 열을 생성하는 방법을 보여주며, 이들은 FloatingBox의 단락 컬렉션에 추가되고, 이후 페이지 인스턴스의 단락 컬렉션에 추가됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateMultiColumnPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Specify the left margin info for the PDF file
        document.PageInfo.Margin.Left = 40;
        // Specify the Right margin info for the PDF file
        document.PageInfo.Margin.Right = 40;
        var page = document.Pages.Add();

        var graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
        // Add the line to paraphraphs collection of section object
        page.Paragraphs.Add(graph1);

        // Specify the coordinates for the line
        float[] posArr = new float[] { 1, 2, 500, 2 };
        var line1 = new Aspose.Pdf.Drawing.Line(posArr);
        graph1.Shapes.Add(line1);
        // Create string variables with text containing html tags
        string s = "<font face=\"Times New Roman\" size=4>" +

        "<strong> How to Steer Clear of money scams</<strong> "
        + "</font>";
        // Create text paragraphs containing HTML text
        var heading_text = new Aspose.Pdf.HtmlFragment(s);
        page.Paragraphs.Add(heading_text);

        var box = new Aspose.Pdf.FloatingBox();
        // Add four columns in the section
        box.ColumnInfo.ColumnCount = 2;
        // Set the spacing between the columns
        box.ColumnInfo.ColumnSpacing = "5";

        box.ColumnInfo.ColumnWidths = "105 105";
        var text1 = new Aspose.Pdf.Text.TextFragment("By A Googler (The Official Google Blog)");
        text1.TextState.FontSize = 8;
        text1.TextState.LineSpacing = 2;
        box.Paragraphs.Add(text1);
        text1.TextState.FontSize = 10;

        text1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        // Create a graphs object to draw a line
        var graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
        // Specify the coordinates for the line
        float[] posArr2 = new float[] { 1, 10, 100, 10 };
        var line2 = new Aspose.Pdf.Drawing.Line(posArr2);
        graph2.Shapes.Add(line2);

        // Add the line to paragraphs collection of section object
        box.Paragraphs.Add(graph2);

        var text2 = new Aspose.Pdf.Text.TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
        box.Paragraphs.Add(text2);

        page.Paragraphs.Add(box);

        // Save PDF document
        document.Save(dataDir + "CreateMultiColumnPdf_out.pdf");
    }
}
```

## 사용자 정의 탭 정지 작업

탭 정지는 탭을 위한 정지 지점입니다. 워드 프로세싱에서 각 줄에는 정기적인 간격(예: 매 0.5인치)으로 배치된 여러 개의 탭 정지가 포함됩니다. 그러나 대부분의 워드 프로세서는 원하는 위치에 탭 정지를 설정할 수 있도록 허용하므로 변경할 수 있습니다. Tab 키를 누르면 커서 또는 삽입 지점이 다음 탭 정지로 점프하며, 이 탭 정지는 보이지 않습니다. 탭 정지는 텍스트 파일에 존재하지 않지만, 워드 프로세서는 Tab 키에 올바르게 반응할 수 있도록 이를 추적합니다.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)은 개발자가 PDF 문서에서 사용자 정의 탭 정지를 사용할 수 있도록 합니다. Aspose.Pdf.Text.TabStop 클래스는 [TextFragment](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text/textfragment) 클래스에서 사용자 정의 탭 정지를 설정하는 데 사용됩니다.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)은 또한 TabLeaderType이라는 열거형으로 미리 정의된 탭 리더 유형을 제공하며, 그 미리 정의된 값과 설명은 다음과 같습니다:

|**탭 리더 유형**|**설명**|
| :- | :- |
|없음|탭 리더 없음|
|단단함|단단한 탭 리더|
|대시|대시 탭 리더|
|점|점 탭 리더|

다음은 사용자 정의 탭 정지를 설정하는 방법의 예입니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomTabStops()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var tabStops = new Aspose.Pdf.Text.TabStops();
        var tabStop1 = tabStops.Add(100);
        tabStop1.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Right;
        tabStop1.LeaderType = Aspose.Pdf.Text.TabLeaderType.Solid;

        var tabStop2 = tabStops.Add(200);
        tabStop2.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Center;
        tabStop2.LeaderType = Aspose.Pdf.Text.TabLeaderType.Dash;

        var tabStop3 = tabStops.Add(300);
        tabStop3.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Left;
        tabStop3.LeaderType = Aspose.Pdf.Text.TabLeaderType.Dot;

        var header = new Aspose.Pdf.Text.TextFragment("This is a example of forming table with TAB stops", tabStops);
        var text0 = new Aspose.Pdf.Text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        var text1 = new Aspose.Pdf.Text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);
        var text2 = new Aspose.Pdf.Text.TextFragment("#$TABdata21 ", tabStops);
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("#$TAB"));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("data22 "));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("#$TAB"));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("data23"));

        // Add text fragments to page
        page.Paragraphs.Add(header);
        page.Paragraphs.Add(text0);
        page.Paragraphs.Add(text1);
        page.Paragraphs.Add(text2);

        // Save PDF document
        document.Save(dataDir + "CustomTabStops_out.pdf");
    }
}
```

## PDF에 투명 텍스트 추가 방법

PDF 파일에는 이미지, 텍스트, 그래프, 첨부 파일, 주석 객체가 포함되어 있으며, TextFragment를 생성할 때 전경 및 배경 색상 정보와 텍스트 형식을 설정할 수 있습니다. Aspose.PDF for .NET은 알파 색상 채널로 텍스트를 추가하는 기능을 지원합니다. 다음 코드 스니펫은 투명 색상으로 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTransparentText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create page to pages collection of PDF file
        var page = document.Pages.Add();

        // Create Graph object
        var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
        // Create rectangle instance with certain dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
        // Create color object from Alpha color channel
        rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
        // Add rectanlge to shapes collection of Graph object
        canvas.Shapes.Add(rect);
        // Add graph object to paragraphs collection of page object
        page.Paragraphs.Add(canvas);
        // Set value to not change position for graph object
        canvas.IsChangePosition = false;

        // Create TextFragment instance with sample value
        var text = new Aspose.Pdf.Text.TextFragment("transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
        // Create color object from Alpha channel
        Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
        // Set color information for text instance
        text.TextState.ForegroundColor = color;
        // Add text to paragraphs collection of page instance
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "AddTransparentText_out.pdf");
    }
}
```

## 글꼴에 대한 줄 간격 지정

모든 글꼴에는 같은 글자 크기에서 줄 간격으로 의도된 거리를 나타내는 추상 정사각형이 있습니다. 이 정사각형을 em 정사각형이라고 하며, 글리프 윤곽이 정의되는 디자인 그리드입니다. 입력 글꼴의 많은 글자는 글꼴의 em 정사각형 경계를 넘어 배치된 점을 가지고 있으므로 글꼴을 올바르게 표시하려면 특별한 설정이 필요합니다. TextFragment 객체에는 TextState.FormattingOptions 속성을 통해 접근할 수 있는 텍스트 형식 옵션 세트가 있습니다. 이 경로의 마지막 속성은 Aspose.Pdf.Text.TextFormattingOptions 유형의 속성입니다. 이 클래스에는 특정 글꼴을 위해 설계된 [LineSpacingMode](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text.textformattingoptions/linespacingmode)라는 열거형이 있습니다. 또한 [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text/textformattingoptions) 클래스에는 LineSpacingMode 유형의 [LineSpacing](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text/textformattingoptions/properties/linespacing) 속성이 있습니다. LineSpacing을 LineSpacingMode.FullSize로 설정하기만 하면 됩니다. 글꼴을 올바르게 표시하기 위한 코드 스니펫은 다음과 같습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyLineSpacing()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    string fontFile = dataDir + "HPSimplified.TTF";

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        //Create TextFormattingOptions with LineSpacingMode.FullSize
        var formattingOptions = new Aspose.Pdf.Text.TextFormattingOptions();
        formattingOptions.LineSpacing = Aspose.Pdf.Text.TextFormattingOptions.LineSpacingMode.FullSize;

        // Create text builder object for first page of document
        //TextBuilder textBuilder = new TextBuilder(document.Pages[1]);
        // Create text fragment with sample string
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello world");

        if (fontFile != "")
        {
            // Load the TrueType font into stream object
            using (FileStream fontStream = File.OpenRead(fontFile))
            {
                // Set the font name for text string
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(fontStream, Aspose.Pdf.Text.FontTypes.TTF);
                // Specify the position for Text Fragment
                textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
                //Set TextFormattingOptions of current fragment to predefined(which points to LineSpacingMode.FullSize)
                textFragment.TextState.FormattingOptions = formattingOptions;
                // Add the text to TextBuilder so that it can be placed over the PDF file
                //textBuilder.AppendText(textFragment);
                var page = document.Pages.Add();
                page.Paragraphs.Add(textFragment);
            }

            // Save PDF document
            document.Save(dataDir + "SpecifyLineSpacing_out.pdf");
        }
    }
}
```

## 텍스트 너비를 동적으로 가져오기

때때로 텍스트 너비를 동적으로 가져와야 할 필요가 있습니다. Aspose.PDF for .NET은 문자열 너비 측정을 위한 두 가지 메서드를 포함합니다. Aspose.Pdf.Text.Font 또는 Aspose.Pdf.Text.TextState 클래스의 [MeasureString](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text/font/methods/measurestring) 메서드를 호출할 수 있습니다(또는 둘 다). 아래의 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTextWidthDynamically()
{            
    var font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
    var textState = new Aspose.Pdf.Text.TextState();
    textState.Font = font;
    textState.FontSize = 14;

    if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    {
        Console.WriteLine("Unexpected font string measure!");
    }

    if (Math.Abs(textState.MeasureString("z") - 7.0) > 0.001)
    {
        Console.WriteLine("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++)
    {
        double fontMeasure = font.MeasureString(c.ToString(), 14);
        double textStateMeasure = textState.MeasureString(c.ToString());

        if (Math.Abs(fontMeasure - textStateMeasure) > 0.001)
        {
            Console.WriteLine("Font and state string measuring doesn't match!");
        }
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
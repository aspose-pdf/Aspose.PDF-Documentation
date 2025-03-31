---
title: PDF 내 텍스트 서식 지정 C# 사용
linktitle: PDF 내 텍스트 서식 지정
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/text-formatting-inside-pdf/
description: Aspose.PDF를 사용하여 .NET에서 PDF 문서 내 텍스트를 서식 지정하는 방법을 배우고 문서의 시각적 표현을 향상시킵니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Text Formatting inside PDF using C#",
    "alternativeHeadline": "Enhance PDF Text Formatting with New C# Features",
    "abstract": "Aspose.PDF for .NET의 강력한 텍스트 서식 지정 기능을 발견하여 PDF 문서에 줄 들여쓰기, 텍스트 테두리, 밑줄 효과 등을 추가할 수 있습니다. 이 기능은 텍스트 미학과 레이아웃에 대한 정밀한 제어를 가능하게 하여 PDF 파일의 전반적인 프레젠테이션을 향상시킵니다. 개발자를 위해 맞춤화된 다양한 서식 옵션으로 PDF 생성 워크플로를 최적화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1642",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "이 페이지에서는 PDF 파일 내에서 텍스트를 서식 지정하는 방법을 설명합니다. 줄 들여쓰기 추가, 텍스트 테두리 추가, 밑줄 텍스트 추가 등이 있습니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF에 줄 들여쓰기 추가하는 방법

Aspose.PDF for .NET는 [TextFormattingOptions](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text/textformattingoptions) 클래스에 SubsequentLinesIndent 속성을 제공합니다. 이 속성은 TextFragment 및 Paragraphs 컬렉션과 함께 PDF 생성 시 줄 들여쓰기를 지정하는 데 사용할 수 있습니다.

다음 코드 스니펫을 사용하여 속성을 사용하세요:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextFormattingInsidePdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

        Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

        // Initilize TextFormattingOptions for the text fragment and specify SubsequentLinesIndent value
        text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
        {
            SubsequentLinesIndent = 20
        };

        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line2");
        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line3");
        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line4");
        page.Paragraphs.Add(text);

        text = new Aspose.Pdf.Text.TextFragment("Line5");
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "SubsequentIndent_out.pdf");
    }
}
```

## 텍스트 테두리 추가하는 방법

다음 코드 스니펫은 TextBuilder를 사용하여 텍스트에 테두리를 추가하는 방법과 TextState의 DrawTextRectangleBorder 속성을 설정하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextBorder()
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
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        // Set StrokingColor property for drawing border (stroking) around text rectangle
        textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
        // Set DrawTextRectangleBorder property value to true
        textFragment.TextState.DrawTextRectangleBorder = true;
        var tb = new Aspose.Pdf.Text.TextBuilder(page);
        tb.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "PDFWithTextBorder_out.pdf");
    }
}
```

## 밑줄 텍스트 추가하는 방법

다음 코드 스니펫은 새 PDF 파일을 생성할 때 밑줄 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddUnderlineText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add age page to PDF document
        document.Pages.Add();
        // Create TextBuilder for first page
        var tb = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // TextFragment with sample text
        var fragment = new Aspose.Pdf.Text.TextFragment("Test message");
        // Set the font for TextFragment
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment.TextState.FontSize = 10;
        // Set the formatting of text as Underline
        fragment.TextState.Underline = true;
        // Specify the position where TextFragment needs to be placed
        fragment.Position = new Aspose.Pdf.Text.Position(10, 800);
        // Append TextFragment to PDF file
        tb.AppendText(fragment);

        // Save PDF document
        document.Save(dataDir + "AddUnderlineText_out.pdf");
    }
}
```

## 추가된 텍스트 주위에 테두리 추가하는 방법

추가한 텍스트의 모양과 느낌을 제어할 수 있습니다. 아래 예제는 추가한 텍스트 주위에 사각형을 그려 테두리를 추가하는 방법을 보여줍니다. [PdfContentEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfcontenteditor) 클래스에 대해 더 알아보세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    
    // Open PDF document
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "AddBorder.pdf");
        var lineInfo = new Aspose.Pdf.Facades.LineInfo();
        lineInfo.LineWidth = 2;
        lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
        lineInfo.Visibility = true;
        // Add border
        editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

        // Save PDF document
        editor.Save(dataDir + "AddingBorderAroundAddedText_out.pdf");
    }
}
```

## 줄 바꿈 추가하는 방법

TextFragment는 텍스트 내에서 줄 바꿈을 지원하지 않습니다. 그러나 줄 바꿈이 있는 텍스트를 추가하려면 TextFragment와 TextParagraph를 사용하세요:

- TextFragment에서 단일 "\n" 대신 "\r\n" 또는 Environment.NewLine을 사용하세요.
- TextParagraph 객체를 생성합니다. 그러면 줄 분할이 있는 텍스트가 추가됩니다.
- TextParagraph.AppendLine으로 TextFragment를 추가합니다.
- TextBuilder.AppendParagraph로 TextParagraph를 추가합니다.

아래 코드 스니펫을 사용하세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddNewLine()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Initialize new TextFragment with text containing required newline markers
        var textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

        // Set text fragment properties if necessary
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

        // Create TextParagraph object
        var par = new Aspose.Pdf.Text.TextParagraph();

        // Add new TextFragment to paragraph
        par.AppendLine(textFragment);

        // Set paragraph position
        par.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Add the TextParagraph using TextBuilder
        textBuilder.AppendParagraph(par);

        // Save PDF document
        document.Save(dataDir + "AddNewLineFeed_out.pdf");
    }
}
```

## 취소선 텍스트 추가하는 방법

TextState 클래스는 PDF 문서 내에 배치되는 TextFragments의 서식을 설정하는 기능을 제공합니다. 이 클래스를 사용하여 텍스트 서식을 굵게, 기울임, 밑줄로 설정할 수 있으며, 이번 릴리스부터 API는 텍스트 서식을 취소선으로 표시하는 기능을 제공합니다. 다음 코드 스니펫을 사용하여 취소선 서식이 있는 TextFragment를 추가해 보세요.

전체 코드 스니펫을 사용하세요:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStrikeoutText()
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
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        // Set StrikeOut property
        textFragment.TextState.StrikeOut = true;
        // Mark text as Bold
        textFragment.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);
        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "AddStrikeOutText_out.pdf");
    }
}
```

## 텍스트에 그라디언트 음영 적용하기

API의 텍스트 편집 시나리오에서 텍스트 서식이 더욱 향상되었으며, 이제 PDF 문서 내에 패턴 색상 공간을 가진 텍스트를 추가할 수 있습니다. Aspose.Pdf.Color 클래스는 텍스트의 음영 색상을 지정하는 데 사용할 수 있는 PatternColorSpace의 새로운 속성을 도입하여 더욱 향상되었습니다. 이 새로운 속성은 텍스트에 다양한 그라디언트 음영을 추가합니다. 예를 들어, 다음 코드 스니펫에 표시된 대로 축 방향 음영, 방사형(유형 3) 음영 등이 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ApplyGradientShadingToText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "text_sample4.pdf"))
    {
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Lorem ipsum");
        document.Pages.Accept(absorber);

        var textFragment = absorber.TextFragments[1];

        // Create new color with pattern colorspace
        textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
        {
            PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.Blue)
        };
        textFragment.TextState.Underline = true;

        // Save PDF document
        document.Save(dataDir +"ApplyGradientShadingToText_out.pdf");
    }
}
```

> 방사형 그라디언트를 적용하려면 위 코드 스니펫에서 'PatternColorSpace' 속성을 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)'로 설정할 수 있습니다.

## 텍스트를 플로팅 콘텐츠에 맞추는 방법

Aspose.PDF는 플로팅 박스 요소 내의 콘텐츠에 대한 텍스트 정렬을 설정하는 것을 지원합니다. Aspose.Pdf.FloatingBox 인스턴스의 정렬 속성을 사용하여 이를 달성할 수 있습니다. 아래 코드 샘플을 참조하세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AlignTextToFloat()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Create float box
        Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom;
        floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_bottom"));
        floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox);

        // Create float box
        Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_center"));
        floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox1);

        // Create float box
        Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
        // Set settings to float box
        floatBox2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        floatBox2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("FloatingBox_top"));
        floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
        // Add float box
        page.Paragraphs.Add(floatBox2);

        // Save PDF document
        document.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
    }
}
```

## PDF 파일에서 숨겨진 텍스트 제거하는 방법

먼저, 코드 스니펫은 파일에서 Document 객체를 생성합니다. 그런 다음, 텍스트를 찾고 편집하기 위해 TextFragmentAbsorber를 추가합니다. 이후 숨겨진 텍스트를 확인하고 삭제합니다. 마지막으로 업데이트된 문서를 저장합니다.

이 방법은 보이는 텍스트를 그대로 유지하고 레이아웃을 보존합니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveHiddenText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "HiddenText.pdf"))
    {
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // This option can be used to prevent other text fragments from moving after hidden text replacement
        textAbsorber.TextReplaceOptions = new Aspose.Pdf.Text.TextReplaceOptions(Aspose.Pdf.Text.TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        // Remove hidden text
        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        // Save PDF document
        document.Save(dataDir + "HiddenText_out.pdf");
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
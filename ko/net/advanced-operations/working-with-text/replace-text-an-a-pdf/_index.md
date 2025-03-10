---
title: PDF에서 텍스트 교체
linktitle: PDF에서 텍스트 교체
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/replace-text-in-pdf/
description: Aspose.PDF for .NET 라이브러리에서 텍스트를 교체하고 제거하는 다양한 방법에 대해 알아보세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text in PDF",
    "alternativeHeadline": "Efficiently Modify Text Across PDF Pages with Ease",
    "abstract": "Aspose.PDF for .NET의 PDF에서 텍스트 교체 기능은 사용자가 전체 PDF 문서 또는 특정 페이지 영역에서 텍스트를 효율적으로 찾고 교체할 수 있도록 합니다. 정규 표현식을 기반으로 한 텍스트 교체, 교체 후 페이지 콘텐츠의 자동 재배치, 사용하지 않는 글꼴 제거 기능을 지원하여 문서 편집 경험을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2744",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET 라이브러리에서 텍스트를 교체하고 제거하는 다양한 방법에 대해 알아보세요."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 문서의 모든 페이지에서 텍스트 교체

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 문서에서 텍스트를 찾고 교체해 볼 수 있으며, 결과는 이 [링크](https://products.aspose.app/pdf/redaction)에서 확인할 수 있습니다.

{{% /alert %}}

PDF 문서의 모든 페이지에서 텍스트를 교체하려면 먼저 TextFragmentAbsorber를 사용하여 교체할 특정 구문을 찾아야 합니다. 그 후, 모든 TextFragments를 통해 텍스트를 교체하고 다른 속성을 변경해야 합니다. 이를 완료한 후에는 Document 객체의 Save 메서드를 사용하여 출력 PDF를 저장하면 됩니다. 다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 교체하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for all the pages
        document.Pages.Accept(absorber);

        // Get the extracted text fragments
        var textFragmentCollection = absorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            // Update text and other properties
            textFragment.Text = "TEXT";
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
            textFragment.TextState.FontSize = 22;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
            textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextInAllPages_out.pdf");
    }
}
```

## 특정 페이지 영역에서 텍스트 교체

특정 페이지 영역에서 텍스트를 교체하려면 먼저 TextFragmentAbsorber 객체를 인스턴스화하고 TextSearchOptions.Rectangle 속성을 사용하여 페이지 영역을 지정한 다음 모든 TextFragments를 반복하여 텍스트를 교체해야 합니다. 이러한 작업이 완료되면 Document 객체의 Save 메서드를 사용하여 출력 PDF를 저장하면 됩니다. 다음 코드 스니펫은 PDF 문서의 특정 페이지 영역에서 텍스트를 교체하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "programaticallyproducedpdf.pdf"))
    {
        // instantiate TextFragment Absorber object
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // search text within page bound
        absorber.TextSearchOptions.LimitToPageBounds = true;

        // specify the page region for TextSearch Options
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 100, 200, 200);

        // search text from first page of PDF file
        document.Pages[1].Accept(absorber);

        // iterate through individual TextFragment
        foreach (var textFragment in absorber.TextFragments)
        {
            // update text to blank characters
            textFragment.Text = "";
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextInParticularPageRegion_out.pdf");
    }
}
```

## 정규 표현식을 기반으로 텍스트 교체

정규 표현식을 기반으로 일부 구문을 교체하려면 먼저 TextFragmentAbsorber를 사용하여 해당 정규 표현식과 일치하는 모든 구문을 찾아야 합니다. 정규 표현식을 TextFragmentAbsorber 생성자에 매개변수로 전달해야 합니다. 또한 정규 표현식 사용 여부를 지정하는 TextSearchOptions 객체를 생성해야 합니다. TextFragments에서 일치하는 구문을 얻은 후에는 모든 구문을 반복하여 필요에 따라 업데이트해야 합니다. 마지막으로 Document 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장해야 합니다. 다음 코드 스니펫은 정규 표현식을 기반으로 텍스트를 교체하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextBasedOnARegularExpression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionPage.pdf"))
    {

        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

        // Set text search option to specify regular expression usage
        absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

        // Accept the absorber for a single page
        document.Pages[1].Accept(absorber);

        // Get the extracted text fragments
        var collection = absorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in collection)
        {
            // Update text and other properties
            textFragment.Text = "New Phrase";
            // Set to an instance of an object.
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
            textFragment.TextState.FontSize = 22;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
            textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextonRegularExpression_out.pdf");
    }
}
```

## 기존 PDF 파일에서 글꼴 교체

Aspose.PDF for .NET은 PDF 문서에서 텍스트를 교체하는 기능을 지원합니다. 그러나 때때로 PDF 문서 내에서 사용되는 글꼴만 교체해야 하는 요구 사항이 있습니다. 따라서 텍스트를 교체하는 대신 사용되는 글꼴만 교체됩니다. TextFragmentAbsorber 생성자의 오버로드 중 하나는 TextEditOptions 객체를 인수로 받아들이며, 우리의 요구 사항을 충족하기 위해 TextEditOptions.FontReplace 열거형의 RemoveUnusedFonts 값을 사용할 수 있습니다. 다음 코드 스니펫은 PDF 문서 내에서 글꼴을 교체하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextPage.pdf"))
    {
        // Create text edit options
        var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);

        // Search text fragments and set edit option as remove unused fonts
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(options);

        // Accept the absorber for all the pages
        document.Pages.Accept(absorber);

        // Traverse through all the TextFragments
        foreach (var textFragment in absorber.TextFragments)
        {
            // If the font name is ArialMT, replace font name with Arial
            if (textFragment.TextState.Font.FontName == "Arial,Bold")
            {
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceFonts_out.pdf");
    }
}
```

## 텍스트 교체는 페이지 콘텐츠를 자동으로 재배치해야 합니다

Aspose.PDF for .NET은 PDF 파일 내에서 텍스트를 검색하고 교체하는 기능을 지원합니다. 그러나 최근 일부 고객은 특정 TextFragment가 더 작은 콘텐츠로 교체될 때 텍스트 교체 중에 문제가 발생했으며, 결과 PDF에 여분의 공백이 표시되거나 TextFragment가 더 긴 문자열로 교체될 경우 단어가 기존 페이지 콘텐츠와 겹치는 문제가 발생했습니다. 따라서 PDF 문서 내에서 텍스트가 교체된 후 콘텐츠가 재배치되어야 하는 메커니즘을 도입해야 했습니다.

위에서 언급한 시나리오를 처리하기 위해 Aspose.PDF for .NET은 PDF 파일 내에서 텍스트를 교체할 때 이러한 문제가 발생하지 않도록 개선되었습니다. 다음 코드 스니펫은 PDF 파일 내에서 텍스트를 교체하고 페이지 콘텐츠가 자동으로 재배치되는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutomaticallyReArrangePageContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // Create TextFragment Absorber object with regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
        document.Pages.Accept(absorber);

        // Replace each TextFragment
        foreach (var textFragment in absorber.TextFragments)
        {
            // Set font of text fragment being replaced
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            // Set font size
            textFragment.TextState.FontSize = 12;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
            // Replace the text with larger string than placeholder
            textFragment.Text = "This is a Larger String for the Testing of this issue";
        }

        // Save PDF document
        document.Save(dataDir + "AutomaticallyReArrangePageContents_out.pdf");
    }
}
```

## PDF 생성 중 교체 가능한 기호 렌더링

교체 가능한 기호는 텍스트 문자열 내에서 런타임에 해당 콘텐츠로 교체될 수 있는 특별한 기호입니다. Aspose.PDF 네임스페이스의 새로운 Document Object Model에서 현재 지원하는 교체 가능한 기호는 `$P`, `$p`, `\n`, `\r`입니다. `$p`와 `$P`는 런타임에 페이지 번호를 처리하는 데 사용됩니다. `$p`는 현재 Paragraph 클래스가 있는 페이지의 번호로 교체됩니다. `$P`는 문서의 총 페이지 수로 교체됩니다. PDF 문서의 단락 컬렉션에 `TextFragment`를 추가할 때 텍스트 내에서 줄 바꿈을 지원하지 않습니다. 그러나 줄 바꿈이 있는 텍스트를 추가하려면 `TextParagraph`와 함께 `TextFragment`를 사용하십시오:

- TextFragment에서 단일 "\n" 대신 "\r\n" 또는 Environment.NewLine을 사용하십시오.
- TextParagraph 객체를 생성합니다. 그러면 줄 분할이 있는 텍스트가 추가됩니다.
- TextFragment를 TextParagraph.AppendLine으로 추가합니다.
- TextParagraph를 TextBuilder.AppendParagraph로 추가합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenderingReplaceableSymbols()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Initialize new TextFragment with text containing required newline markers
        Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

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
        document.Save(dataDir + "RenderingReplaceableSymbols_out.pdf");
    }
}
```

## 헤더/푸터 영역의 교체 가능한 기호

교체 가능한 기호는 PDF 파일의 헤더/푸터 섹션에도 배치할 수 있습니다. 푸터 섹션에 교체 가능한 기호를 추가하는 방법에 대한 자세한 내용은 다음 코드 스니펫을 참조하십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceableSymbolsInHeaderOrFooterArea()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Create margin info
        var marginInfo = new Aspose.Pdf.MarginInfo();
        marginInfo.Top = 90;
        marginInfo.Bottom = 50;
        marginInfo.Left = 50;
        marginInfo.Right = 50;
        // Assign the marginInfo instance to Margin property of sec1.PageInfo
        page.PageInfo.Margin = marginInfo;

        var headerFooterFirst = new Aspose.Pdf.HeaderFooter();
        page.Header = headerFooterFirst;
        headerFooterFirst.Margin.Left = 50;
        headerFooterFirst.Margin.Right = 50;

        // Instantiate a Text paragraph that will store the content to show as header
        var fragment1 = new Aspose.Pdf.Text.TextFragment("report title");
        fragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment1.TextState.FontSize = 16;
        fragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
        fragment1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        fragment1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        fragment1.TextState.LineSpacing = 5f;
        headerFooterFirst.Paragraphs.Add(fragment1);

        var fragment2 = new Aspose.Pdf.Text.TextFragment("Report_Name");
        fragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
        fragment2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        fragment2.TextState.LineSpacing = 5f;
        fragment2.TextState.FontSize = 12;
        headerFooterFirst.Paragraphs.Add(fragment2);

        // Create a HeaderFooter object for the section
        var headerFooterFoot = new Aspose.Pdf.HeaderFooter();

        // Set the HeaderFooter object to odd & even footer
        page.Footer = headerFooterFoot;
        headerFooterFoot.Margin.Left = 50;
        headerFooterFoot.Margin.Right = 50;

        // Add a text paragraph containing current page number of total number of pages
        var fragment3 = new Aspose.Pdf.Text.TextFragment("Generated on test date");
        var fragment4 = new Aspose.Pdf.Text.TextFragment("report name ");
        var fragment5 = new Aspose.Pdf.Text.TextFragment("Page $p of $P");

        // Instantiate a table object
        var table2 = new Aspose.Pdf.Table();

        // Add the table in paragraphs collection of the desired section
        headerFooterFoot.Paragraphs.Add(table2);

        // Set with column widths of the table
        table2.ColumnWidths = "165 172 165";

        // Create rows in the table and then cells in the rows
        var row3 = table2.Rows.Add();

        row3.Cells.Add();
        row3.Cells.Add();
        row3.Cells.Add();

        // Set the vertical allignment of the text as center alligned
        row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
        row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
        row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

        row3.Cells[0].Paragraphs.Add(fragment3);
        row3.Cells[1].Paragraphs.Add(fragment4);
        row3.Cells[2].Paragraphs.Add(fragment5);

        // Sec1.Paragraphs.Add(New Text("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL"))
        var table = new Aspose.Pdf.Table();

        table.ColumnWidths = "33% 33% 34%";
        table.DefaultCellPadding = new Aspose.Pdf.MarginInfo();
        table.DefaultCellPadding.Top = 10;
        table.DefaultCellPadding.Bottom = 10;

        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(table);

        // Set default cell border using BorderInfo object
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1f);

        // Set table border using another customized BorderInfo object
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1f);

        table.RepeatingRowsCount = 1;

        // Create rows in the table and then cells in the rows
        var row1 = table.Rows.Add();

        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add("col3");
        const string CRLF = "\r\n";
        for (int i = 0; i <= 10; i++)
        {
            var row = table.Rows.Add();
            row.IsRowBroken = true;
            for (int c = 0; c <= 2; c++)
            {
                Aspose.Pdf.Cell c1;
                if (c == 2)
                {
                    c1 = row.Cells.Add("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a" + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "Using Aspose.Total for Java developers can create a wide range of applications.");
                }
                else
                {
                    c1 = row.Cells.Add("item1" + c);
                }
                c1.Margin = new Aspose.Pdf.MarginInfo();
                c1.Margin.Left = 30;
                c1.Margin.Top = 10;
                c1.Margin.Bottom = 10;
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf");
    }
}
```

## PDF 파일에서 사용하지 않는 글꼴 제거

Aspose.PDF for .NET은 PDF 문서를 생성할 때 글꼴을 포함하는 기능과 기존 PDF 파일에 글꼴을 포함하는 기능을 지원합니다. Aspose.PDF for .NET 7.3.0부터는 PDF 문서에서 중복되거나 사용하지 않는 글꼴을 제거할 수 있습니다.

글꼴을 교체하려면 다음 접근 방식을 사용하십시오:

1. [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) 클래스를 호출합니다.
1. TextFragmentAbsorber 클래스의 TextEditOptions.FontReplace.RemoveUnusedFonts 매개변수를 호출합니다. (이것은 글꼴 교체 중에 사용하지 않게 된 글꼴을 제거합니다).
1. 각 텍스트 조각에 대해 글꼴을 개별적으로 설정합니다.

다음 코드 스니펫은 모든 문서 페이지의 모든 텍스트 조각에 대해 글꼴을 교체하고 사용하지 않는 글꼴을 제거합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveUnusedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextPage.pdf"))
    {
        var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages.Accept(absorber);

        // Iterate through all the TextFragments
        foreach (var textFragment in absorber.TextFragments)
        {
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial, Bold");
        }

        // Save PDF document
        document.Save(dataDir + "RemoveUnusedFonts_out.pdf");
    }
}
```

## PDF 문서에서 모든 텍스트 제거

### 연산자를 사용하여 모든 텍스트 제거

일부 텍스트 작업에서는 PDF 문서에서 모든 텍스트를 제거해야 하며, 이를 위해 발견된 텍스트를 일반적으로 빈 문자열 값으로 설정해야 합니다. 문제는 다수의 텍스트 조각에 대해 텍스트를 변경하는 것이 여러 검사 및 텍스트 위치 조정 작업을 호출한다는 것입니다. 이는 텍스트 편집 시나리오에서 필수적입니다. 어려운 점은 루프에서 처리되는 시나리오에서 얼마나 많은 텍스트 조각이 제거될지를 결정할 수 없다는 것입니다.

따라서 PDF 페이지에서 모든 텍스트를 제거하는 시나리오에 대해 다른 접근 방식을 사용하는 것이 좋습니다. 다음 코드 스니펫은 매우 빠르게 작동하는 방법을 고려하십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveAllTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveAllText.pdf"))
    {
        // Loop through all pages of PDF Document
        for (int i = 1; i <= document.Pages.Count; i++)
        {
            var page = document.Pages[i];
            var operatorSelector = new Aspose.Pdf.OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
            // Select all text on the page
            page.Contents.Accept(operatorSelector);
            // Delete all text
            page.Contents.Delete(operatorSelector.Selected);
        }
        // Save PDF document
        document.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
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
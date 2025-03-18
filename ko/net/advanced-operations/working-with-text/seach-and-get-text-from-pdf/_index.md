---
title: PDF 페이지에서 텍스트 검색 및 가져오기
linktitle: 텍스트 검색 및 가져오기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ko/net/search-and-get-text-from-pdf/
description: Aspose.PDF를 사용하여 .NET에서 PDF 파일에서 텍스트를 검색하고 추출하는 방법을 알아보세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Search and Get Text from Pages of PDF",
    "alternativeHeadline": "Search and Extract Text from PDF Pages",
    "abstract": "Aspose.PDF for .NET는 사용자가 PDF 문서의 모든 페이지에서 텍스트를 효율적으로 검색하고 추출할 수 있도록 합니다. 이 기능은 TextFragmentAbsorber 클래스를 활용하여 지정된 구문이나 텍스트 세그먼트를 찾고, 정규 표현식에 대한 고급 지원을 제공하여 정확한 텍스트 검색 및 조작을 가능하게 합니다. 개발자에게 이상적인 이 기능은 텍스트 추출 프로세스를 단순화하여 PDF 문서 처리 능력을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2762",
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
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "이 문서에서는 Aspose.PDF for .NET에서 텍스트를 검색하고 가져오는 다양한 도구를 사용하는 방법을 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 문서의 모든 페이지에서 텍스트 검색 및 가져오기

[TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) 클래스는 PDF 문서의 모든 페이지에서 특정 구문과 일치하는 텍스트를 찾을 수 있도록 합니다. 전체 문서에서 텍스트를 검색하려면 Pages 컬렉션의 Accept 메서드를 호출해야 합니다. [Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) 메서드는 TextFragmentAbsorber 객체를 매개변수로 받아들이며, 이는 TextFragment 객체의 컬렉션을 반환합니다. 모든 조각을 반복하여 Text, Position (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor 등의 속성을 가져올 수 있습니다.

다음 코드 스니펫은 모든 페이지에서 텍스트를 검색하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine("Text : {0} ", textFragment.Text);
            Console.WriteLine("Position : {0} ", textFragment.Position);
            Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
            Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
            Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
            Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
            Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
            Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
            Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
            Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
        }
    }
}
```

특정 PDF 페이지 내에서 텍스트를 검색해야 하는 경우, Document 인스턴스의 페이지 컬렉션에서 페이지 번호를 지정하고 해당 페이지에 대해 Accept 메서드를 호출하십시오(아래 코드 줄에 표시됨).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for a particular page
        document.Pages[2].Accept(textFragmentAbsorber);
    }
}
```

### TextFragmentAbsorber에서 구문 목록을 통해 검색하기

C# 라이브러리는 TextFragmentAbsorber에 하나의 구문만 전달할 수 있지만, Aspose.PDF의 24.2 릴리스 이후로 목록 검색 알고리즘을 위한 새로운 알고리즘이 구현되었습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // Create resular expressions
    var regexes = new Regex[]
    {
        new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)", RegexOptions.IgnoreCase),
        new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:? ", RegexOptions.IgnoreCase),
        new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
        new Regex("Vested in:", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regexes, new Aspose.Pdf.Text.TextSearchOptions(true));
        document.Pages.Accept(absorber);
        // Get result
        var result = absorber.RegexResults;
    }
}
```

코드 스니펫은 정규 표현식을 사용하여 PDF 문서에서 문서 번호, 키워드 및 파일 번호와 같은 특정 패턴을 검색합니다. PDF를 로드하고 검색을 적용하며, 추가 처리를 위한 일치하는 결과를 검색합니다.

## PDF 문서의 모든 페이지에서 텍스트 세그먼트 검색 및 가져오기

모든 페이지에서 텍스트 세그먼트를 검색하려면 먼저 문서에서 TextFragment 객체를 가져와야 합니다. TextFragmentAbsorber는 PDF 문서의 모든 페이지에서 특정 구문과 일치하는 텍스트를 찾을 수 있도록 합니다. 전체 문서에서 텍스트를 검색하려면 Pages 컬렉션의 Accept 메서드를 호출해야 합니다. Accept 메서드는 TextFragmentAbsorber 객체를 매개변수로 받아들이며, 이는 TextFragment 객체의 컬렉션을 반환합니다. 문서에서 TextFragmentCollection을 가져온 후, 이 컬렉션을 반복하여 각 TextFragment 객체의 TextSegmentCollection을 가져와야 합니다. 그 후, 각 TextSegment 객체의 모든 속성을 가져올 수 있습니다. 다음 코드 스니펫은 모든 페이지에서 텍스트 세그먼트를 검색하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextPage.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Figure");

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            foreach (var textSegment in textFragment.Segments)
            {
                Console.WriteLine("Text : {0} ", textSegment.Text);
                Console.WriteLine("Position : {0} ", textSegment.Position);
                Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
                Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
                Console.WriteLine("Font - Name : {0}", textSegment.TextState.Font.FontName);
                Console.WriteLine("Font - IsAccessible : {0} ", textSegment.TextState.Font.IsAccessible);
                Console.WriteLine("Font - IsEmbedded : {0} ", textSegment.TextState.Font.IsEmbedded);
                Console.WriteLine("Font - IsSubset : {0} ", textSegment.TextState.Font.IsSubset);
                Console.WriteLine("Font Size : {0} ", textSegment.TextState.FontSize);
                Console.WriteLine("Foreground Color : {0} ", textSegment.TextState.ForegroundColor);
            }
        }
    }
}
```

특정 PDF 페이지에서 TextSegments를 검색하고 가져오려면 Accept(..) 메서드를 호출할 때 특정 페이지 인덱스를 지정해야 합니다. 다음 코드 줄을 참조하십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for a particular page
        document.Pages[2].Accept(textFragmentAbsorber);
    }
}
```

## 정규 표현식을 사용하여 모든 페이지에서 텍스트 검색 및 가져오기

TextFragmentAbsorber는 정규 표현식을 기반으로 모든 페이지에서 텍스트를 검색하고 가져오는 데 도움을 줍니다. 먼저, 정규 표현식을 TextFragmentAbsorber 생성자에 구문으로 전달해야 합니다. 그 후, TextFragmentAbsorber 객체의 TextSearchOptions 속성을 설정해야 합니다. 이 속성은 TextSearchOptions 객체를 필요로 하며, 새 객체를 생성할 때 true를 매개변수로 전달해야 합니다. 모든 페이지에서 일치하는 텍스트를 검색하려면 Pages 컬렉션의 Accept 메서드를 호출해야 합니다. TextFragmentAbsorber는 정규 표현식으로 지정된 기준과 일치하는 모든 조각을 포함하는 TextFragmentCollection을 반환합니다. 다음 코드 스니펫은 정규 표현식을 기반으로 모든 페이지에서 텍스트를 검색하고 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

        // Set text search option to specify regular expression usage
        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

        textFragmentAbsorber.TextSearchOptions = textSearchOptions;

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine("Text : {0} ", textFragment.Text);
            Console.WriteLine("Position : {0} ", textFragment.Position);
            Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
            Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
            Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
            Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
            Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
            Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
            Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
            Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
        }
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextFragmentAbsorberCtor()
{
    Aspose.Pdf.Text.TextFragmentAbsorber textFragmentAbsorber;
    // In order to search exact match of a word, you may consider using regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"\bWord\b", new Aspose.Pdf.Text.TextSearchOptions(true));

    // In order to search a string in either upper case or lowercase, you may consider using regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("(?i)Line", new Aspose.Pdf.Text.TextSearchOptions(true));

    // In order to search all the strings (parse all strings) inside PDF document, please try using following regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");

    // Find match of search string and get anything after the string till line break
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(?i)the ((.)*)");

    // Please use following regular expression to find text following to the regex match
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(?<=word).*");

    // In order to search Hyperlink/URL's inside PDF document, please try using following regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
}
```

## 정규 표현식 기반으로 텍스트 검색 및 하이퍼링크 추가

정규 표현식을 기반으로 텍스트 구문 위에 하이퍼링크를 추가하려면, 먼저 TextFragmentAbsorber를 사용하여 해당 정규 표현식과 일치하는 모든 구문을 찾아야 하며, 이러한 구문 위에 하이퍼링크를 추가해야 합니다.

구문을 찾아 하이퍼링크를 추가하려면:

1. 정규 표현식을 TextFragmentAbsorber 생성자에 매개변수로 전달합니다.
2. 정규 표현식 사용 여부를 지정하는 TextSearchOptions 객체를 생성합니다.
3. 일치하는 구문을 TextFragments에 가져옵니다.
4. 일치 항목을 반복하여 사각형 치수를 가져오고, 전경색을 파란색으로 변경합니다(선택 사항 - 하이퍼링크처럼 보이도록 하며 PdfContentEditor 클래스의 CreateWebLink(..) 메서드를 사용하여 링크를 생성합니다).
5. Document 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장합니다.
다음 코드 스니펫은 정규 표현식을 사용하여 PDF 파일 내에서 텍스트를 검색하고 일치 항목 위에 하이퍼링크를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create absorber object to find all instances of the input search phrase
    var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}");

    // Enable regular expression search
    absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

    // Create the editor
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");

        // Accept the absorber for the page
        editor.Document.Pages[1].Accept(absorber);

        int[] dashArray = { };
        String[] LEArray = { };
        System.Drawing.Color blue = System.Drawing.Color.Blue;

        // Loop through the fragments
        foreach (var textFragment in absorber.TextFragments)
        {
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
                (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
                (int)Math.Round(textFragment.Rectangle.Height + 1));
            Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
            editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
            editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
                (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
        }

        // Save PDF document
        editor.Save(dataDir + "SearchTextAndAddHyperlink_out.pdf");
    }
}
```

## 각 TextFragment 주위에 사각형 그리기

Aspose.PDF for .NET은 각 문자 또는 텍스트 조각의 좌표를 검색하고 가져오는 기능을 지원합니다. 따라서 각 문자에 대해 반환되는 좌표에 대해 확실히 하기 위해 각 문자 주위에 하이라이트(사각형 추가)를 고려할 수 있습니다.

텍스트 단락의 경우, 단락 구분을 결정하기 위해 일부 정규 표현식을 사용하는 것을 고려할 수 있으며, 그 주위에 사각형을 그릴 수 있습니다. 다음 코드 스니펫을 참조하십시오. 다음 코드 스니펫은 각 문자의 좌표를 가져오고 각 문자 주위에 사각형을 생성합니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndDraw()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {

        // Create TextAbsorber object to find all the phrases matching the regular expression
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(".");

        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);
        textAbsorber.TextSearchOptions = textSearchOptions;

        document.Pages.Accept(textAbsorber);

        foreach (var textFragment in textAbsorber.TextFragments)
        {
            DrawRectangleOnPage(textFragment.Rectangle, textFragment.Page, new Aspose.Pdf.Operators.SetRGBColorStroke(System.Drawing.Color.Red));
        }   
        // Save PDF document
        document.Save(dataDir + "SearchTextAndDrawRectangle_out.pdf");
    }
}

 private static void DrawRectangleOnPage(Aspose.Pdf.Rectangle rectangle, Aspose.Pdf.Page page, Aspose.Pdf.Operators.SetRGBColorStroke colorStroke = null)
 {
     if (colorStroke == null)
     {
         colorStroke = new Aspose.Pdf.Operators.SetRGBColorStroke(0.7, 0, 0);
     }

     page.Contents.Add(new Aspose.Pdf.Operators.GSave());
     page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
     page.Contents.Add(colorStroke);
     page.Contents.Add(
         new Re(rectangle.LLX,
             rectangle.LLY,
             rectangle.Width,
             rectangle.Height));
     page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
     page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
 }
```

## PDF 문서에서 각 문자 강조 표시

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 문서에서 텍스트를 검색하고 결과를 온라인에서 확인할 수 있습니다. 이 [링크](https://products.aspose.app/pdf/search)를 클릭하세요.

{{% /alert %}}

Aspose.PDF for .NET는 각 문자 또는 텍스트 조각의 좌표를 검색하고 가져오는 기능을 지원합니다. 따라서 각 문자에 대해 반환되는 좌표가 확실한지 확인하기 위해 각 문자 주위에 하이라이트(사각형 추가)를 고려할 수 있습니다. 다음 코드 스니펫은 각 문자의 좌표를 가져오고 각 문자 주위에 사각형을 생성합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndHighlight()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    int resolution = 150;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {

        using (MemoryStream stream = new MemoryStream())
        {
            var conv = new Aspose.Pdf.Facades.PdfConverter(document);
            conv.Resolution = new Aspose.Pdf.Devices.Resolution(resolution, resolution);
            conv.GetNextImage(stream, System.Drawing.Imaging.ImageFormat.Png);

            using (var bmp = System.Drawing.Bitmap.FromStream(stream))
            {

                using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
                {
                    float scale = resolution / 72f;
                    gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

                    for (int i = 0; i < document.Pages.Count; i++)
                    {
                        var page = document.Pages[1];
                        // Create TextAbsorber object to find all words
                        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");
                        textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
                        page.Accept(textFragmentAbsorber);
                        // Get the extracted text fragments
                        var textFragmentCollection = textFragmentAbsorber.TextFragments;
                        // Loop through the fragments
                        foreach (var textFragment in textFragmentCollection)
                        {
                            if (i == 0)
                            {
                                gr.DrawRectangle(
                                    System.Drawing.Pens.Yellow,
                                    (float)textFragment.Position.XIndent,
                                    (float)textFragment.Position.YIndent,
                                    (float)textFragment.Rectangle.Width,
                                    (float)textFragment.Rectangle.Height);

                                for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
                                {
                                    var segment = textFragment.Segments[segNum];

                                    for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
                                    {
                                        var characterInfo = segment.Characters[charNum];

                                        Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
                                        Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
                                            "   TextFragment URY = " + textFragment.Rectangle.URY);

                                        gr.DrawRectangle(
                                            System.Drawing.Pens.Black,
                                            (float)characterInfo.Rectangle.LLX,
                                            (float)characterInfo.Rectangle.LLY,
                                            (float)characterInfo.Rectangle.Width,
                                            (float)characterInfo.Rectangle.Height);
                                    }

                                    gr.DrawRectangle(
                                        System.Drawing.Pens.Green,
                                        (float)segment.Rectangle.LLX,
                                        (float)segment.Rectangle.LLY,
                                        (float)segment.Rectangle.Width,
                                        (float)segment.Rectangle.Height);
                                }
                            }
                        }
                    }
                }
                
                // Save result
                bmp.Save(dataDir + "HighlightCharacterInPDF_out.png", System.Drawing.Imaging.ImageFormat.Png);
            }
        }
    }
}
```

## 숨겨진 텍스트 추가 및 검색

때때로 PDF 문서에 숨겨진 텍스트를 추가한 다음 숨겨진 텍스트를 검색하고 그 위치를 후처리에 사용하고 싶습니다. 귀하의 편의를 위해 Aspose.PDF for .NET는 이러한 기능을 제공합니다. 문서 생성 중에 숨겨진 텍스트를 추가할 수 있습니다. 또한 TextFragmentAbsorber를 사용하여 숨겨진 텍스트를 찾을 수 있습니다. 숨겨진 텍스트를 추가하려면 추가된 텍스트에 대해 TextState.Invisible을 'true'로 설정합니다. TextFragmentAbsorber는 패턴과 일치하는 모든 텍스트를 찾습니다(지정된 경우). 이는 변경할 수 없는 기본 동작입니다. 발견된 텍스트가 실제로 보이지 않는지 확인하기 위해 TextState.Invisible 속성을 사용할 수 있습니다. 아래 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAndSearchText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var frag1 = new Aspose.Pdf.Text.TextFragment("This is common text.");
        var frag2 = new Aspose.Pdf.Text.TextFragment("This is invisible text.");

        //Set text property - invisible
        frag2.TextState.Invisible = true;

        page.Paragraphs.Add(frag1);
        page.Paragraphs.Add(frag2);
        // Save PDF document
        document.Save(dataDir + "CreateAndSearchText_out.pdf");
    }

    // Search text in the document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateAndSearchText_out.pdf"))
    {
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        foreach (var fragment in absorber.TextFragments)
        {
            //Do something with fragments
            Console.WriteLine("Text '{0}' on pos {1} invisibility: {2} ",
            fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
        }
    }
}
```

## .NET Regex로 텍스트 검색

Aspose.PDF for .NET는 표준 .NET Regex 옵션을 사용하여 문서를 검색하는 기능을 제공합니다. TextFragmentAbsorber는 아래 코드 샘플과 같이 이 목적을 위해 사용할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create Regex object to find all words
    var regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf"))
    {

        // Get a particular page
        var page = document.Pages[1];

        // Create TextAbsorber object to find all instances of the input regex
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regex);
        textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

        // Accept the absorber for the page
        page.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine(textFragment.Text);
        }
    }
}
```

## 굵은 텍스트 검색

Aspose.PDF for .NET은 사용자가 글꼴 스타일 속성을 사용하여 문서를 검색할 수 있도록 합니다. TextFragmentAbsorber는 아래 코드 샘플과 같이 이 목적을 위해 사용할 수 있습니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractBoldText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractBoldText.pdf"))
    {
        // Create TextFragmentAbsorber object to extract text
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // Accept the absorber for all document
        textFragmentAbsorber.Visit(document);

        // Loop through the fragments
        foreach (var textFragment in textFragmentAbsorber.TextFragments)
        {
            // Get the text properties of the text fragment
            var textState = textFragment.TextState;
            // Check if text is bold
            if (textState.FontStyle == FontStyles.Bold)
            {
                // Print the text from the text fragment
                Console.WriteLine("Text :- " + textFragment.Text);
            }
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
---
title: PDF 페이지에서 텍스트 검색 및 가져오기
linktitle: 텍스트 검색 및 가져오기
type: docs
weight: 60
url: /ko/net/search-and-get-text-from-pdf/
description: 이 문서에서는 Aspose.PDF for .NET을 사용하여 다양한 도구로 텍스트를 검색하고 가져오는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 페이지에서 텍스트 검색 및 가져오기",
    "alternativeHeadline": "PDF 페이지에서 텍스트 검색 및 가져오기 도구",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 텍스트 검색, pdf에서 텍스트 가져오기",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "이 문서에서는 Aspose.PDF for .NET을 사용하여 다양한 도구로 텍스트를 검색하고 가져오는 방법을 설명합니다."
}
</script>
다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

## PDF 문서의 모든 페이지에서 텍스트 검색 및 가져오기

[TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) 클래스를 사용하면 PDF 문서의 모든 페이지에서 특정 구문과 일치하는 텍스트를 찾을 수 있습니다. 문서 전체에서 텍스트를 검색하려면 Pages 컬렉션의 Accept 메소드를 호출해야 합니다. [Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) 메소드는 TextFragment 객체의 컬렉션을 반환하는 TextFragmentAbsorber 객체를 매개변수로 사용합니다. 모든 프래그먼트를 반복하며 텍스트, 위치 (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor 등의 속성을 가져올 수 있습니다.

다음 코드 스니펫은 모든 페이지에서 텍스트를 검색하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// 입력 검색 구문의 모든 인스턴스를 찾기 위해 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// 모든 페이지에 대해 흡수기 수락
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 추출된 텍스트 프래그먼트 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 프래그먼트를 반복합니다
foreach (TextFragment textFragment in textFragmentCollection)
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
```
PDF 문서의 특정 페이지 내에서 텍스트를 검색해야 하는 경우, Document 인스턴스의 페이지 컬렉션에서 페이지 번호를 지정하고 아래 코드 줄에 표시된 대로 해당 페이지에 Accept 메소드를 호출하십시오.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Accept the absorber for a particular page
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## PDF 문서의 모든 페이지에서 텍스트 세그먼트 검색 및 가져오기

모든 페이지에서 텍스트 세그먼트를 검색하려면 먼저 문서에서 TextFragment 객체를 가져와야 합니다.
모든 페이지에서 텍스트 세그먼트를 검색하려면 먼저 문서에서 TextFragment 객체를 가져와야 합니다.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// Create TextAbsorber object to find all instances of the input search phrase
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// Accept the absorber for all the pages
pdfDocument.Pages.Accept(textFragmentAbsorber);
// Get the extracted text fragments
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Loop through the fragments
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
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
```
PDF의 특정 페이지에서 TextSegments를 검색하고 가져오려면 Accept(..) 메서드를 호출할 때 특정 페이지 인덱스를 지정해야 합니다. 다음 코드 줄을 참고하십시오.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 모든 페이지에 대해 absorber를 수락합니다
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## 정규 표현식을 사용하여 모든 페이지에서 텍스트 검색 및 가져오기

TextFragmentAbsorber는 정규 표현식을 기반으로 모든 페이지에서 텍스트를 검색하고 검색하는 데 도움을 줍니다.
TextFragmentAbsorber는 정규 표현식을 기반으로 모든 페이지에서 텍스트를 검색하고 검색하는 데 도움이 됩니다.

```csharp
// 완벽한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 으로 이동하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// 정규 표현식과 일치하는 모든 구절을 찾기 위해 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 예: 1999-2000

// 정규 표현식 사용을 지정하기 위해 텍스트 검색 옵션 설정
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// 모든 페이지에 대해 absorber를 적용
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 추출된 텍스트 조각들을 가져옴
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 조각들을 순회하면서
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("텍스트 : {0} ", textFragment.Text);
    Console.WriteLine("위치 : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("폰트 - 이름 : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("폰트 - 접근 가능 : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("폰트 - 내장됨 : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("폰트 - 부분 집합 : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("폰트 크기 : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("전경색 : {0} ", textFragment.TextState.ForegroundColor);
}
```
```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
TextFragmentAbsorber textFragmentAbsorber;
// 단어의 정확한 일치를 검색하려면 정규 표현식을 사용하는 것을 고려해 보세요.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// 대문자 또는 소문자의 문자열을 검색하려면 정규 표현식을 사용하는 것을 고려해 보세요.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// PDF 문서 내의 모든 문자열(모든 문자열 파싱)을 검색하려면 다음 정규 표현식을 사용해 보세요.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// 검색 문자열의 일치를 찾고 줄 바꿈까지 문자열 뒤에 오는 것을 가져오세요.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// 정규 표현식 일치 뒤의 텍스트를 찾으려면 다음 정규 표현식을 사용하세요.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// PDF 문서 내에서 하이퍼링크/URL을 검색하려면 다음 정규 표현식을 사용해 보세요.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```
## 정규 표현식을 기반으로 텍스트 검색하고 하이퍼링크 추가

정규 표현식을 기반으로 텍스트 구를 찾아 하이퍼링크를 추가하고 싶다면, 먼저 TextFragmentAbsorber를 사용하여 해당 정규 표현식과 일치하는 모든 구를 찾고 이들에게 하이퍼링크를 추가하세요.

구를 찾고 그 위에 하이퍼링크를 추가하기 위해서:

1. 정규 표현식을 TextFragmentAbsorber 생성자에 매개변수로 전달합니다.
2. 정규 표현식 사용 여부를 명시하는 TextSearchOptions 객체를 생성합니다.
3. 일치하는 구들을 TextFragments로 가져옵니다.
4. 일치하는 항목을 순회하면서 직사각형 치수를 가져오고, 전경색을 파란색으로 변경(선택 사항 - 하이퍼링크처럼 보이게 하기 위해)하고 PdfContentEditor 클래스의 CreateWebLink(..) 메소드를 사용하여 링크를 생성합니다.
5. Document 객체의 Save 메소드를 사용하여 업데이트된 PDF를 저장합니다.
다음 코드 스니펫은 정규 표현식을 사용하여 PDF 파일 내의 텍스트를 검색하고 일치하는 항목에 하이퍼링크를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Create absorber object to find all instances of the input search phrase
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// Enable regular expression search
absorber.TextSearchOptions = new TextSearchOptions(true);
// Open document
PdfContentEditor editor = new PdfContentEditor();
// Bind source PDF file
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// Accept the absorber for the page
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// Loop through the fragments
foreach (TextFragment textFragment in absorber.TextFragments)
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

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```
## 각 TextFragment 주위에 사각형 그리기

Aspose.PDF for .NET은 각 문자 또는 텍스트 조각의 좌표를 검색하고 가져오는 기능을 지원합니다. 따라서 각 문자에 대해 반환되는 좌표에 대해 확신할 수 있도록 각 문자 주위에 사각형(하이라이트 추가)을 그릴 수 있습니다.

텍스트 단락의 경우, 단락이 끊기는 지점을 결정하기 위해 정규 표현식을 사용할 수 있고 그 주위에 사각형을 그릴 수 있습니다. 다음 코드 조각을 확인해 주세요. 다음 코드 조각은 각 문자의 좌표를 가져와 각 문자 주위에 사각형을 생성합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하실 수 있습니다.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// 모든 구문을 찾기 위해 TextAbsorber 객체 생성

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```
## PDF 문서의 각 문자를 강조 표시

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 문서에서 텍스트를 검색하고 이 [링크](https://products.aspose.app/pdf/search)에서 결과를 온라인으로 확인할 수 있습니다.

{{% /alert %}}

Aspose.PDF for .NET은 각 문자 또는 텍스트 조각의 좌표를 검색하고 얻는 기능을 지원합니다. 따라서 각 문자에 대해 반환되는 좌표를 확실히 하기 위해, 우리는 각 문자 주변에 사각형을 추가하는 것을 고려할 수 있습니다. 다음 코드 조각은 각 문자의 좌표를 얻고 각 문자 주변에 사각형을 만듭니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
            Page page = pdfDocument.Pages[1];
            // 모든 단어를 찾기 위한 TextAbsorber 객체 생성
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
            textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
            page.Accept(textFragmentAbsorber);
            // 추출된 텍스트 조각 가져오기
            TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
            // 조각들을 반복 처리
            foreach (TextFragment textFragment in textFragmentCollection)
            {
                if (i == 0)
                {
                    gr.DrawRectangle(
                    Pens.Yellow,
                    (float)textFragment.Position.XIndent,
                    (float)textFragment.Position.YIndent,
                    (float)textFragment.Rectangle.Width,
                    (float)textFragment.Rectangle.Height);

                    for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
                    {
                        TextSegment segment = textFragment.Segments[segNum];

                        for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
                        {
                            CharInfo characterInfo = segment.Characters[charNum];

                            Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
                            Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
                                "   TextFragment URY = " + textFragment.Rectangle.URY);

                            gr.DrawRectangle(
                            Pens.Black,
                            (float)characterInfo.Rectangle.LLX,
                            (float)characterInfo.Rectangle.LLY,
                            (float)characterInfo.Rectangle.Width,
                            (float)characterInfo.Rectangle.Height);
                        }

                        gr.DrawRectangle(
                        Pens.Green,
                        (float)segment.Rectangle.LLX,
                        (float)segment.Rectangle.LLY,
                        (float)segment.Rectangle.Width,
                        (float)segment.Rectangle.Height);
                    }
                }
            }
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```
## 숨겨진 텍스트 추가 및 검색

PDF 문서에 숨겨진 텍스트를 추가하고 싶은 경우가 있습니다. 그리고 숨겨진 텍스트를 검색하여 후처리에 사용할 수 있습니다. 편리를 위해 Aspose.PDF for .NET은 이러한 기능을 제공합니다. 문서 생성 중에 숨겨진 텍스트를 추가할 수 있습니다. 또한 TextFragmentAbsorber를 사용하여 숨겨진 텍스트를 찾을 수 있습니다. 숨겨진 텍스트를 추가하려면 추가된 텍스트에 대해 TextState.Invisible을 ‘true’로 설정하세요. TextFragmentAbsorber는 패턴(지정된 경우)과 일치하는 모든 텍스트를 찾습니다. 이것은 변경할 수 없는 기본 동작입니다. 찾은 텍스트가 실제로 보이지 않는지 확인하려면 TextState.Invisible 속성을 사용할 수 있습니다. 아래 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 숨겨진 텍스트와 함께 문서 생성
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("이것은 일반 텍스트입니다.");
TextFragment frag2 = new TextFragment("이것은 보이지 않는 텍스트입니다.");

// 텍스트 속성 설정 - 보이지 않음
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

// 문서에서 텍스트 검색
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    // 조각들을 가지고 무언가를 하세요
    Console.WriteLine("텍스트 '{0}' 위치 {1} 보이지 않음: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```
## .NET Regex를 사용한 텍스트 검색

Aspose.PDF for .NET은 표준 .NET Regex 옵션을 사용하여 문서를 검색할 수 있는 기능을 제공합니다. 아래 코드 샘플에서 보여주는 것처럼 이를 위해 TextFragmentAbsorber를 사용할 수 있습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-NET 에서 확인해 주세요.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 모든 단어를 찾기 위해 Regex 객체 생성
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// 문서 열기
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// 특정 페이지 가져오기
Page page = document.Pages[1];

// 입력된 regex의 모든 인스턴스를 찾기 위해 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// 페이지에 대해 absorber 수락
page.Accept(textFragmentAbsorber);

// 추출된 텍스트 조각들 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 조각들을 반복
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
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
    "applicationCategory": ".NET용 PDF 조작 라이브러리",
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
```


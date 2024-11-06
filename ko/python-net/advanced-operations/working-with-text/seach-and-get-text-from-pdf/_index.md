---
title: PDF 페이지에서 텍스트 검색 및 가져오기
linktitle: 텍스트 검색 및 가져오기
type: docs
weight: 60
url: ko/python-net/search-and-get-text-from-pdf/
description: 이 문서에서는 Aspose.PDF for .NET에서 다양한 도구를 사용하여 텍스트를 검색하고 가져오는 방법을 설명합니다.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 페이지에서 텍스트 검색 및 가져오기",
    "alternativeHeadline": "PDF 페이지에서 텍스트를 검색하고 가져오는 도구",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 텍스트 검색, pdf에서 텍스트 가져오기",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "이 문서에서는 Aspose.PDF for .NET에서 다양한 도구를 사용하여 텍스트를 검색하고 가져오는 방법을 설명합니다."
}
</script>


## PDF 문서의 모든 페이지에서 텍스트 검색 및 가져오기

[TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) 클래스는 PDF 문서의 모든 페이지에서 특정 구문과 일치하는 텍스트를 찾을 수 있게 해줍니다. 전체 문서에서 텍스트를 검색하려면 Pages 컬렉션의 Accept 메서드를 호출해야 합니다. [Accept](https://reference.aspose.com/pdf/python-net/aspose.pdf.page/accept/methods/3) 메서드는 TextFragmentAbsorber 객체를 매개변수로 사용하며, TextFragment 객체의 컬렉션을 반환합니다. 모든 프래그먼트를 반복하여 Text, Position (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor 등의 속성을 가져올 수 있습니다.

다음 코드 스니펫은 모든 페이지에서 텍스트를 검색하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET를 참조하십시오.
// 문서 디렉토리의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// 입력 검색 구문의 모든 인스턴스를 찾기 위한 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// 모든 페이지에 대해 흡수기 수락
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 추출된 텍스트 프래그먼트 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 프래그먼트를 반복
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


특정 PDF 페이지 내에서 텍스트를 검색해야 하는 경우, Document 인스턴스의 페이지 모음에서 페이지 번호를 지정하고 해당 페이지에 대해 Accept 메서드를 호출하세요 (아래 코드 줄에서 보여줌).

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET을 참조하세요.
// 특정 페이지에 대해 흡수기를 수락합니다.
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## PDF 문서의 모든 페이지에서 텍스트 세그먼트 검색 및 가져오기

모든 페이지에서 텍스트 세그먼트를 검색하려면, 먼저 문서에서 TextFragment 객체를 가져와야 합니다.
 TextFragmentAbsorber는 PDF 문서의 모든 페이지에서 특정 구문과 일치하는 텍스트를 찾을 수 있게 해줍니다. 문서 전체에서 텍스트를 검색하려면 Pages 컬렉션의 Accept 메서드를 호출해야 합니다. Accept 메서드는 TextFragmentAbsorber 객체를 매개변수로 받아들여, TextFragment 객체의 컬렉션을 반환합니다. 문서에서 TextFragmentCollection을 가져오면, 이 컬렉션을 순회하여 각 TextFragment 객체의 TextSegmentCollection을 가져와야 합니다. 그런 다음, 개별 TextSegment 객체의 모든 속성을 얻을 수 있습니다. 다음 코드 스니펫은 모든 페이지에서 텍스트 세그먼트를 검색하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET을 참조하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// 입력 검색 구문의 모든 인스턴스를 찾기 위한 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// 모든 페이지에 대해 absorber를 수락
pdfDocument.Pages.Accept(textFragmentAbsorber);
// 추출된 텍스트 프래그먼트 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// 프래그먼트를 순회
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

특정 페이지의 PDF에서 TextSegments를 검색하고 가져오려면 Accept(..) 메서드를 호출할 때 특정 페이지 인덱스를 지정해야 합니다. 다음 코드 줄을 참조하십시오.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET를 방문하십시오.
// 모든 페이지에 대해 흡수기를 수락합니다.
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## 정규식을 사용하여 모든 페이지에서 텍스트 검색 및 가져오기

TextFragmentAbsorber는 정규식을 기반으로 모든 페이지에서 텍스트를 검색하고 검색하는 데 도움이 됩니다.
 먼저, 정규 표현식을 TextFragmentAbsorber 생성자에 구문으로 전달해야 합니다. 그 후, TextFragmentAbsorber 객체의 TextSearchOptions 속성을 설정해야 합니다. 이 속성은 TextSearchOptions 객체를 필요로 하며, 새 객체를 생성하는 동안 생성자에 true를 매개변수로 전달해야 합니다. 모든 페이지에서 일치하는 텍스트를 검색하려면 Pages 컬렉션의 Accept 메서드를 호출해야 합니다. TextFragmentAbsorber는 정규 표현식으로 지정된 조건에 맞는 모든 조각이 포함된 TextFragmentCollection을 반환합니다. 다음 코드 스니펫은 정규 표현식을 기반으로 모든 페이지에서 텍스트를 검색하고 가져오는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET를 참조하세요.
// 문서 디렉터리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// 정규 표현식과 일치하는 모든 구문을 찾기 위해 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 예: 1999-2000

// 정규 표현식 사용을 지정하기 위해 텍스트 검색 옵션 설정
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// 모든 페이지에 대해 흡수기 허용
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 추출된 텍스트 조각 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 조각을 반복
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("텍스트 : {0} ", textFragment.Text);
    Console.WriteLine("위치 : {0} ", textFragment.Position);
    Console.WriteLine("X 들여쓰기 : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("Y 들여쓰기 : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("글꼴 - 이름 : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("글꼴 - 접근 가능 여부 : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("글꼴 - 포함 여부 : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("글꼴 - 부분 집합 여부 : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("글꼴 크기 : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("전경색 : {0} ", textFragment.TextState.ForegroundColor);
}
```

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET을 참조하세요.
TextFragmentAbsorber textFragmentAbsorber;
// 단어의 정확한 일치를 검색하기 위해 정규 표현식을 사용할 수 있습니다.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// 문자열을 대문자 또는 소문자로 검색하기 위해 정규 표현식을 사용할 수 있습니다.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// PDF 문서 내의 모든 문자열을 검색(모든 문자열을 구문 분석)하기 위해 다음 정규 표현식을 사용해보세요.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// 검색 문자열의 일치를 찾고 줄 바꿈까지 문자열 이후의 모든 것을 가져옵니다.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// 정규식 일치 후의 텍스트를 찾기 위해 다음 정규 표현식을 사용하세요.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// PDF 문서 내의 하이퍼링크/URL을 검색하기 위해 다음 정규 표현식을 사용해보세요.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```


## 정규 표현식을 기반으로 텍스트 검색 및 하이퍼링크 추가

정규 표현식을 기반으로 텍스트 구에 하이퍼링크를 추가하려면, 먼저 TextFragmentAbsorber를 사용하여 해당 정규 표현식과 일치하는 모든 구를 찾고 이러한 구에 하이퍼링크를 추가하십시오.

구를 찾아 하이퍼링크를 추가하려면:

1. 정규 표현식을 TextFragmentAbsorber 생성자의 매개변수로 전달합니다.
2. 정규 표현식이 사용되는지 여부를 지정하는 TextSearchOptions 객체를 생성합니다.
3. 일치하는 구를 TextFragments에 가져옵니다.
4. 일치하는 항목을 반복하여 사각형 차원을 얻고, 전경색을 파란색으로 변경한 후(선택 사항 - 하이퍼링크처럼 보이도록 하기 위해) PdfContentEditor 클래스의 CreateWebLink(..) 메서드를 사용하여 링크를 생성합니다.
5. Document 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장합니다. 다음 코드 스니펫은 정규 표현식을 사용하여 PDF 파일 내에서 텍스트를 검색하고 일치 항목에 하이퍼링크를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 입력 검색 구의 모든 인스턴스를 찾기 위한 흡수기 객체 생성
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// 정규 표현식 검색 활성화
absorber.TextSearchOptions = new TextSearchOptions(true);
// 문서 열기
PdfContentEditor editor = new PdfContentEditor();
// 원본 PDF 파일 바인딩
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// 페이지에 대한 흡수기를 수락
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// 조각들을 반복
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


## 각 TextFragment 주위에 사각형을 검색하고 그리기

Aspose.PDF for .NET은 각 문자 또는 텍스트 조각의 좌표를 검색하고 가져오는 기능을 지원합니다. 따라서 각 문자에 대해 반환되는 좌표가 확실하도록 각 문자 주위에 사각형을 추가하여 강조 표시하는 것을 고려할 수 있습니다.

텍스트 단락의 경우 일부 정규식을 사용하여 단락 구분을 결정하고 그 주위에 사각형을 그리는 것을 고려할 수 있습니다. 다음 코드 스니펫을 살펴보세요. 다음 코드 스니펫은 각 문자의 좌표를 가져오고 각 문자 주위에 사각형을 만듭니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET을 참조하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// 정규식과 일치하는 모든 구문을 찾기 위한 TextAbsorber 객체 생성

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


## PDF 문서에서 각 문자 강조

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 문서에서 텍스트를 검색하고 결과를 온라인으로 확인할 수 있습니다. 이 [링크](https://products.aspose.app/pdf/search)에서 가능합니다.

{{% /alert %}}

Aspose.PDF for .NET은 각 문자 또는 텍스트 조각의 좌표를 검색하는 기능을 지원합니다. 따라서 각 문자에 대해 반환되는 좌표에 대해 확신하기 위해 각 문자 주위에 직사각형을 추가하여 강조하는 것을 고려할 수 있습니다. 다음 코드 스니펫은 각 문자의 좌표를 가져오고 각 문자 주위에 직사각형을 만듭니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET을 참조하세요.
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
// 모든 단어를 찾기 위해 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// 추출된 텍스트 조각 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// 조각을 순회
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

때때로 우리는 PDF 문서에 숨겨진 텍스트를 추가한 후 숨겨진 텍스트를 검색하고 그 위치를 후처리에 사용하고자 합니다. 귀하의 편의를 위해 Aspose.PDF for .NET은 이러한 기능을 제공합니다. 문서 생성 중에 숨겨진 텍스트를 추가할 수 있습니다. 또한 TextFragmentAbsorber를 사용하여 숨겨진 텍스트를 찾을 수 있습니다. 숨겨진 텍스트를 추가하려면 추가된 텍스트의 TextState.Invisible을 'true'로 설정하십시오. TextFragmentAbsorber는 패턴과 일치하는 모든 텍스트를 찾습니다(지정된 경우). 이는 변경할 수 없는 기본 동작입니다. 발견된 텍스트가 실제로 보이지 않는지 확인하려면 TextState.Invisible 속성을 사용할 수 있습니다. 아래 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참조하세요
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//숨겨진 텍스트로 문서 생성
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("This is common text.");
TextFragment frag2 = new TextFragment("This is invisible text.");

//텍스트 속성 설정 - 보이지 않음
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//문서에서 텍스트 검색
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //조각으로 작업 수행
    Console.WriteLine("Text '{0}' on pos {1} invisibility: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```


## .NET Regex로 텍스트 검색하기

Aspose.PDF for .NET은 표준 .NET Regex 옵션을 사용하여 문서를 검색할 수 있는 기능을 제공합니다. TextFragmentAbsorber는 아래의 코드 샘플에서와 같이 이 목적에 사용될 수 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET를 참조하세요.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 모든 단어를 찾기 위한 Regex 객체 생성
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// 문서 열기
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// 특정 페이지 가져오기
Page page = document.Pages[1];

// 입력된 정규 표현식의 모든 인스턴스를 찾기 위한 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// 페이지에 대한 흡수기 허용
page.Accept(textFragmentAbsorber);

// 추출된 텍스트 조각들 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 조각을 루프 처리
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
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF 조작 라이브러리 for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
---
title: C#를 사용하여 PDF에 텍스트 추가
linktitle: PDF에 텍스트 추가
type: docs
weight: 10
url: /ko/net/add-text-to-pdf-file/
description: 이 문서는 Aspose.PDF에서 텍스트 작업의 다양한 측면을 설명합니다. PDF에 텍스트 추가, HTML 조각 추가 또는 사용자 지정 OTF 폰트 사용 방법을 배워보세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#를 사용하여 PDF에 텍스트 추가",
    "alternativeHeadline": "PDF에 텍스트 추가 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf에 텍스트 추가",
    "wordcount": "302",
    "proficiencyLevel":"초급",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
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
    "dateModified": "2022-02-04",
    "description": "이 문서는 Aspose.PDF에서 텍스트 작업의 다양한 측면을 설명합니다. PDF에 텍스트 추가, HTML 조각 추가 또는 사용자 지정 OTF 폰트 사용 방법을 배워보세요."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

기존 PDF 파일에 텍스트를 추가하려면:

1. Document 객체를 사용하여 입력 PDF를 엽니다.
2. 텍스트를 추가하려는 특정 페이지를 가져옵니다.
3. 입력 텍스트와 다른 텍스트 속성을 가진 TextFragment 객체를 생성합니다. 해당 페이지에서 생성된 TextBuilder 객체를 사용하여 AppendText 메소드를 사용하여 페이지에 TextFragment 객체를 추가할 수 있습니다.
4. Document 객체의 Save 메소드를 호출하고 출력 PDF 파일을 저장합니다.

## 텍스트 추가

다음 코드 조각은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "input.pdf");

// 특정 페이지 가져오기
Page pdfPage = (Page)pdfDocument.Pages[1];

// 텍스트 조각 생성
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// 텍스트 속성 설정
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

// TextBuilder 객체 생성
TextBuilder textBuilder = new TextBuilder(pdfPage);

// PDF 페이지에 텍스트 조각 추가
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddText_out.pdf";

// 결과 PDF 문서 저장.
pdfDocument.Save(dataDir);
```
## 스트림에서 폰트 로드

다음 코드 조각은 PDF 문서에 텍스트를 추가할 때 스트림 객체에서 폰트를 로드하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string fontFile = "";

// 입력 PDF 파일 로드
Document doc = new Document(dataDir + "input.pdf");
// 문서의 첫 페이지에 대한 텍스트 빌더 객체 생성
TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// 샘플 문자열을 가진 텍스트 조각 생성
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // TrueType 폰트를 스트림 객체에 로드
    using (FileStream fontStream = File.OpenRead(fontFile))
    {
        // 텍스트 문자열에 대한 폰트 이름 설정
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // 텍스트 조각의 위치 지정
        textFragment.Position = new Position(10, 10);
        // PDF 파일 위에 배치할 수 있도록 TextBuilder에 텍스트 추가
        textBuilder.AppendText(textFragment);
    }

    dataDir = dataDir + "LoadingFontFromStream_out.pdf";

    // 결과 PDF 문서 저장.
    doc.Save(dataDir);
}
```
## TextParagraph를 사용하여 텍스트 추가

다음 코드 스니펫은 [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph) 클래스를 사용하여 PDF 문서에 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 문서 열기
Document doc = new Document();
// Document 객체의 페이지 컬렉션에 페이지 추가
Page page = doc.Pages.Add();
TextBuilder builder = new TextBuilder(page);
// 텍스트 단락 생성
TextParagraph paragraph = new TextParagraph();
// 후속 줄 들여쓰기 설정
paragraph.SubsequentLinesIndent = 20;
// TextParagraph를 추가할 위치 지정
paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
// 단어별로 줄 바꿈 모드 지정
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
// 텍스트 조각 생성
TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
fragment1.TextState.Font = FontRepository.FindFont("Times New Roman");
fragment1.TextState.FontSize = 12;
// 단락에 조각 추가
paragraph.AppendLine(fragment1);
// 단락 추가
builder.AppendParagraph(paragraph);

dataDir = dataDir + "AddTextUsingTextParagraph_out.pdf";

// 결과 PDF 문서 저장.
doc.Save(dataDir);
```
## 텍스트 세그먼트에 하이퍼링크 추가

PDF 페이지는 하나 이상의 TextFragment 객체로 구성될 수 있으며, 각 TextFragment 객체는 하나 이상의 TextSegment 인스턴스를 가질 수 있습니다. TextSegment에 하이퍼링크를 설정하려면 [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment) 클래스의 Hyperlink 속성을 사용하면서 Aspose.Pdf.WebHyperlink 인스턴스의 객체를 제공하면 됩니다. 다음 코드 스니펫을 사용해 이 요구사항을 완수해보세요.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 문서 인스턴스 생성
Document doc = new Document();
// PDF 파일의 페이지 컬렉션에 페이지 추가
Page page1 = doc.Pages.Add();
// TextFragment 인스턴스 생성
TextFragment tf = new TextFragment("샘플 텍스트 조각");
// TextFragment의 수평 정렬 설정
tf.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
// 샘플 텍스트를 가진 텍스트 세그먼트 생성
TextSegment segment = new TextSegment(" ... 텍스트 세그먼트 1...");
// 세그먼트를 TextFragment의 세그먼트 컬렉션에 추가
tf.Segments.Add(segment);
// 새 TextSegment 생성
segment = new TextSegment("Google로의 링크");
// 세그먼트를 TextFragment의 세그먼트 컬렉션에 추가
tf.Segments.Add(segment);
// TextSegment에 하이퍼링크 설정
segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
// 텍스트 세그먼트의 전경색 설정
segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
// 텍스트 포맷을 이탤릭체로 설정
segment.TextState.FontStyle = FontStyles.Italic;
// 하이퍼링크 없는 TextSegment 객체 생성
segment = new TextSegment("하이퍼링크 없는 텍스트 세그먼트");
// 세그먼트를 TextFragment의 세그먼트 컬렉션에 추가
tf.Segments.Add(segment);
// TextFragment를 페이지 객체의 문단 컬렉션에 추가
page1.Paragraphs.Add(tf);

dataDir = dataDir + "AddHyperlinkToTextSegment_out.pdf";

// 결과 PDF 문서 저장.
doc.Save(dataDir);
```
## OTF 글꼴 사용하기

Aspose.PDF for .NET은 사용자 정의/트루타입 글꼴을 사용하여 PDF 파일 내용을 생성하거나 조작하는 기능을 제공하여 파일 내용이 기본 시스템 글꼴 이외의 내용을 사용하여 표시됩니다. Aspose.PDF for .NET 10.3.0 버전부터 Open Type 글꼴에 대한 지원을 제공했습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 새 문서 인스턴스를 생성합니다.
Document pdfDocument = new Document();
// PDF 파일의 페이지 컬렉션에 페이지를 추가합니다.
Aspose.Pdf.Page page = pdfDocument.Pages.Add();
// 샘플 텍스트로 TextFragment 인스턴스를 생성합니다.
TextFragment fragment = new TextFragment("Sample Text in OTF font");
// 시스템 글꼴 디렉토리 내에서 글꼴을 찾습니다.
// Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
// 또는 시스템 디렉토리에서 OTF 글꼴의 경로를 지정할 수도 있습니다.
fragment.TextState.Font = FontRepository.OpenFont(dataDir + "space age.otf");
// PDF 파일 내에 글꼴을 포함시켜 특정 글꼴이 타깃 기기에 설치되어 있지 않더라도 제대로 표시되도록 합니다.
fragment.TextState.Font.IsEmbedded = true;
// TextFragment를 페이지 인스턴스의 단락 컬렉션에 추가합니다.

page.Paragraphs.Add(fragment);

dataDir = dataDir + "OTFFont_out.pdf";

// 결과 PDF 문서를 저장합니다.
pdfDocument.Save(dataDir);
```
## DOM을 사용하여 HTML 문자열 추가하기

Aspose.Pdf.Generator.Text 클래스에는 IsHtmlTagSupported라는 속성이 포함되어 있어 HTML 태그/내용을 PDF 파일에 추가할 수 있습니다. 추가된 내용은 단순한 텍스트 문자열로 표시되는 대신 네이티브 HTML 태그로 렌더링됩니다. Aspose.Pdf 네임스페이스의 새로운 문서 객체 모델(DOM)에서 유사한 기능을 지원하기 위해 HtmlFragment 클래스가 도입되었습니다.

[HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) 인스턴스는 PDF 파일 내부에 배치해야 할 HTML 내용을 지정하는 데 사용할 수 있습니다. TextFragment와 유사하게 HtmlFragment는 단락 수준 객체이며 Page 객체의 단락 컬렉션에 추가할 수 있습니다. 다음 코드 스니펫은 DOM 접근 방식을 사용하여 PDF 파일 내부에 HTML 내용을 배치하는 단계를 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 객체를 인스턴스화합니다.
Document doc = new Document();
// PDF 파일의 페이지 컬렉션에 페이지를 추가합니다.
Page page = doc.Pages.Add();
// HTML 내용이 포함된 HtmlFragment를 인스턴스화합니다.
HtmlFragment title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
// 아래쪽 여백 정보를 설정합니다.
title.Margin.Bottom = 10;
// 위쪽 여백 정보를 설정합니다.
title.Margin.Top = 200;
// 페이지의 단락 컬렉션에 HTML Fragment를 추가합니다.
page.Paragraphs.Add(title);

dataDir = dataDir + "AddHTMLUsingDOM_out.pdf";
// PDF 파일을 저장합니다.
doc.Save(dataDir);
```
다음 코드 스니펫은 문서에 HTML 정렬 목록을 추가하는 단계를 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 출력 문서의 경로입니다.
string outFile = dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf";
// 문서 객체를 인스턴스화합니다.
Document doc = new Document();
// 해당 HTML 조각을 가진 HtmlFragment 객체를 인스턴스화합니다.
HtmlFragment t = new HtmlFragment("`<body style='line-height: 100px;'><ul><li>첫 번째</li><li>두 번째</li><li>세 번째</li><li>네 번째</li><li>다섯 번째</li></ul>목록 후 텍스트.<br/>다음 줄<br/>마지막 줄</body>`");
// 페이지 컬렉션에 페이지를 추가합니다.
Page page = doc.Pages.Add();
// 페이지 내부에 HtmlFragment를 추가합니다.
page.Paragraphs.Add(t);
// 결과 PDF 파일을 저장합니다.
doc.Save(outFile);
```

다음과 같이 TextState 객체를 사용하여 HTML 문자열 형식을 설정할 수도 있습니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요
HtmlFragment html = new HtmlFragment("일부 텍스트");
html.TextState = new TextState();
html.TextState.Font = FontRepository.FindFont("Calibri");
```
HTML 마크업을 통해 일부 텍스트 속성 값을 설정한 후에 동일한 값을 TextState 속성에서 제공하면 TextState 인스턴스의 속성에 의해 HTML 매개변수가 덮어쓰여집니다. 다음 코드 조각은 설명된 동작을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Document 객체를 인스턴스화합니다
Document doc = new Document();
// PDF 파일의 페이지 컬렉션에 페이지를 추가합니다
Page page = doc.Pages.Add();
// HTML 콘텐츠가 있는 HtmlFragment를 인스턴스화합니다
HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>표에는 텍스트가 포함되어 있습니다</i></b></p>");
// 'Verdana'의 글꼴 가족은 'Arial'로 재설정됩니다
title.TextState = new TextState("Arial");
title.TextState.FontSize = 20;
// 하단 여백 정보를 설정합니다
title.Margin.Bottom = 10;
// 상단 여백 정보를 설정합니다
title.Margin.Top = 400;
// 페이지의 단락 컬렉션에 HTML Fragment를 추가합니다
page.Paragraphs.Add(title);
// PDF 파일을 저장합니다
dataDir = dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf";
// PDF 파일을 저장합니다
doc.Save(dataDir);
```
## 바닥글과 끝글 (DOM)

바닥글은 연속된 첨자 번호를 사용하여 귀하의 논문 텍스트에 메모를 표시합니다. 실제 메모는 들여쓰기 되며 페이지 하단에 바닥글로 나타날 수 있습니다.

### 바닥글 추가

바닥글 참조 시스템에서는 다음과 같이 참조를 표시합니다:

- 출처 자료 바로 다음에 오는 줄의 윗부분에 작은 숫자를 넣습니다. 이 숫자를 참조 식별자라고 합니다. 이는 텍스트 줄 위에 약간 떠 있습니다.
- 같은 숫자를 사용하고, 페이지 하단에 출처를 인용하여 넣습니다. 바닥글은 숫자와 시간 순으로 이루어져야 합니다: 첫 번째 참조는 1, 두 번째는 2, 그리고 계속됩니다.

바닥글의 장점은 독자가 페이지를 내려다보기만 하면 그들이 관심 있는 참조의 출처를 발견할 수 있다는 것입니다.

바닥글을 생성하기 위해 아래 단계를 따르세요:

- Document 인스턴스 생성
- Page 객체 생성
- TextFragment 객체 생성
- Note 인스턴스를 생성하고 그 값을 TextFragment.FootNote 속성에 전달하세요
- 노트 인스턴스를 생성하고 그 값을 TextFragment.FootNote 속성에 전달하세요.
- TextFragment를 페이지 인스턴스의 단락 컬렉션에 추가하세요.

### FootNote의 사용자 정의 선 스타일

다음 예시는 Pdf 페이지 하단에 각주를 추가하고 사용자 정의 선 스타일을 정의하는 방법을 보여줍니다.

```csharp
// 완전한 예시와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 로 이동하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Document 인스턴스 생성
Document doc = new Document();
// PDF의 페이지 컬렉션에 페이지 추가
Page page = doc.Pages.Add();
// GraphInfo 객체 생성
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// 선 너비를 2로 설정
graph.LineWidth = 2;
// 그래프 객체의 색상 설정
graph.Color = Aspose.Pdf.Color.Red;
// 대시 배열 값을 3으로 설정
graph.DashArray = new int[] { 3 };
// 대시 위상 값을 1로 설정
graph.DashPhase = 1;
// 페이지의 각주 선 스타일을 graph로 설정
page.NoteLineStyle = graph;
// TextFragment 인스턴스 생성
TextFragment text = new TextFragment("Hello World");
// TextFragment의 FootNote 값 설정
text.FootNote = new Note("foot note for test text 1");
// 문서 첫 페이지의 단락 컬렉션에 TextFragment 추가
page.Paragraphs.Add(text);
// 두 번째 TextFragment 생성
text = new TextFragment("Aspose.Pdf for .NET");
// 두 번째 텍스트 프래그먼트의 각주 설정
text.FootNote = new Note("foot note for test text 2");
// PDF 파일의 단락 컬렉션에 두 번째 텍스트 프래그먼트 추가
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomLineStyleForFootNote_out.pdf";

// 결과 PDF 문서 저장.
doc.Save(dataDir);
```
다음과 같이 TextState 객체를 사용하여 각주 레이블(노트 식별자) 형식을 설정할 수 있습니다:

```csharp
TextFragment text = new TextFragment("test text 1");
text.FootNote = new Note("foot note for test text 1");
text.FootNote.Text = "21";
text.FootNote.TextState = new TextState();
text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
text.FootNote.TextState.FontStyle = FontStyles.Italic;
```

### 각주 레이블 사용자 정의

기본적으로 FootNote 번호는 1부터 증가합니다. 그러나 사용자 정의 각주 레이블을 설정해야 할 수도 있습니다. 이 요구 사항을 달성하려면 다음 코드 조각을 사용해 보세요.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Create Document instance
Document doc = new Document();
// Add page to pages collection of PDF
Page page = doc.Pages.Add();
// Create GraphInfo object
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
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
TextFragment text = new TextFragment("Hello World");
// Set FootNote value for TextFragment
text.FootNote = new Note("foot note for test text 1");
// Specify custom label for FootNote
text.FootNote.Text = " Aspose(2015)";
// Add TextFragment to paragraphs collection of first page of document
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomizeFootNoteLabel_out.pdf";
```
## 이미지와 테이블을 각주에 추가하기

이전 릴리스 버전에서는 각주 지원이 제공되었지만 TextFragment 객체에만 적용되었습니다. 그러나 Aspose.PDF for .NET 10.7.0 릴리스부터 PDF 문서 내의 다른 객체, 예를 들어 테이블, 셀 등에도 각주를 추가할 수 있습니다. 다음 코드 스니펫은 TextFragment 객체에 각주를 추가하고 각주 섹션의 단락 컬렉션에 이미지와 테이블 객체를 추가하는 단계를 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();
TextFragment text = new TextFragment("some text");
page.Paragraphs.Add(text);

text.FootNote = new Note();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = dataDir + "aspose-logo.jpg";
image.FixHeight = 20;
text.FootNote.Paragraphs.Add(image);
TextFragment footNote = new TextFragment("footnote text");
footNote.TextState.FontSize = 20;
footNote.IsInLineParagraph = true;
text.FootNote.Paragraphs.Add(footNote);
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.Rows.Add().Cells.Add().Paragraphs.Add(new TextFragment("Row 1 Cell 1"));
text.FootNote.Paragraphs.Add(table);

dataDir = dataDir + "AddImageAndTable_out.pdf";

// 결과 PDF 문서를 저장합니다.
doc.Save(dataDir);
```
## 엔드노트 생성 방법

엔드노트는 독자들이 종이 끝에서 정보나 인용된 단어의 출처를 찾을 수 있는 특정 장소를 참조하는 출처 인용입니다. 엔드노트를 사용할 때 인용하거나 요약된 문장 또는 요약된 자료는 첨자 번호가 뒤따릅니다.

다음 예제는 Pdf 페이지에 엔드노트를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Document 인스턴스 생성
Document doc = new Document();
// PDF의 페이지 컬렉션에 페이지 추가
Page page = doc.Pages.Add();
// TextFragment 인스턴스 생성
TextFragment text = new TextFragment("Hello World");
// TextFragment에 대한 FootNote 값 설정
text.EndNote = new Note("sample End note");
// FootNote에 대한 사용자 정의 레이블 지정
text.EndNote.Text = " Aspose(2015)";
// 문서의 첫 페이지의 단락 컬렉션에 TextFragment 추가
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateEndNotes_out.pdf";
// 결과 PDF 문서 저장.
doc.Save(dataDir);
```
## 텍스트와 이미지를 인라인 단락으로

PDF 파일의 기본 레이아웃은 흐름 레이아웃(왼쪽 상단에서 오른쪽 하단으로)입니다. 따라서 PDF 파일에 새 요소를 추가하면 오른쪽 하단 흐름에 추가됩니다. 그러나 우리는 다양한 페이지 요소 즉, 이미지와 텍스트를 같은 레벨(한 후에 다른 하나)에서 표시할 필요가 있을 수 있습니다. 하나의 접근 방식은 테이블 인스턴스를 생성하고 두 요소를 개별 셀 객체에 추가하는 것일 수 있습니다. 그러나 다른 접근 방식은 인라인 단락일 수 있습니다. 이미지와 텍스트의 IsInLineParagraph 속성을 true로 설정하면 이러한 단락은 다른 페이지 요소와 인라인으로 표시됩니다.

다음 코드 스니펫은 PDF 파일에서 텍스트와 이미지를 인라인 단락으로 추가하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Document 인스턴스를 생성합니다.
Document doc = new Document();
// Document 인스턴스의 페이지 컬렉션에 페이지를 추가합니다.
Page page = doc.Pages.Add();
// TextFragmnet을 생성합니다.
TextFragment text = new TextFragment("Hello World.. ");
// 페이지 객체의 단락 컬렉션에 텍스트 프래그먼트를 추가합니다.
page.Paragraphs.Add(text);
// 이미지 인스턴스를 생성합니다.
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
// 이미지를 인라인 단락으로 설정하여 이전 단락 객체(텍스트 프래그먼트) 바로 뒤에 표시됩니다.
image.IsInLineParagraph = true;
// 이미지 파일 경로를 지정합니다.
image.File = dataDir + "aspose-logo.jpg";
// 이미지 높이를 설정합니다(선택 사항).
image.FixHeight = 30;
// 이미지 너비를 설정합니다(선택 사항).
image.FixWidth = 100;
// 페이지 객체의 단락 컬렉션에 이미지를 추가합니다.
page.Paragraphs.Add(image);
// 다른 내용으로 TextFragment 객체를 다시 초기화합니다.
text = new TextFragment(" Hello Again..");
// TextFragment를 인라인 단락으로 설정합니다.
text.IsInLineParagraph = true;
// 페이지의 단락 컬렉션에 새로 생성된 TextFragment를 추가합니다.
page.Paragraphs.Add(text);

dataDir = dataDir + "TextAndImageAsParagraph_out.pdf";
doc.Save(dataDir);
```
## 텍스트 추가 시 문자 간격 지정

PDF 파일의 문단 컬렉션 내에 텍스트를 추가할 때 TextFragment 인스턴스를 사용하거나 TextParagraph 객체를 사용하거나 TextStamp 클래스를 사용하여 PDF 내에 텍스트를 스탬프할 수 있습니다. 텍스트를 추가할 때, 텍스트 객체에 대한 문자 간격을 지정해야 할 필요가 있을 수 있습니다. 이 요구 사항을 충족하기 위해 CharacterSpacing 속성이라는 새 속성이 도입되었습니다. 다음 접근 방식을 살펴보아 이 요구 사항을 충족하시기 바랍니다.

다음 접근 방식은 PDF 문서 내에 텍스트를 추가할 때 문자 간격을 지정하는 단계를 보여줍니다.

### TextBuilder 및 TextFragment 사용

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Document 인스턴스 생성
Document pdfDocument = new Document();
// Document의 페이지 컬렉션에 페이지 추가
Page page = pdfDocument.Pages.Add();
// TextBuilder 인스턴스 생성
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// 샘플 내용이 포함된 텍스트 프래그먼트 인스턴스 생성
TextFragment wideFragment = new TextFragment("문자 간격이 넓은 텍스트");
wideFragment.TextState.ApplyChangesFrom(new TextState("Arial", 12));
// TextFragment에 대한 문자 간격 지정
wideFragment.TextState.CharacterSpacing = 2.0f;
// TextFragment의 위치 지정
wideFragment.Position = new Position(100, 650);
// TextFragment를 TextBuilder 인스턴스에 추가
builder.AppendText(wideFragment);
dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf";
// 결과 PDF 문서 저장.
pdfDocument.Save(dataDir);
```
### 텍스트 단락 사용하기

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 를 참고하세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Document 인스턴스 생성
Document pdfDocument = new Document();
// Document의 페이지 컬렉션에 페이지 추가
Page page = pdfDocument.Pages.Add();
// TextBuilder 인스턴스 생성
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// TextParagraph 인스턴스 인스턴스화
TextParagraph paragraph = new TextParagraph();
// 폰트 이름과 크기를 명시하는 TextState 인스턴스 생성
TextState state = new TextState("Arial", 12);
// 문자 간격 지정
state.CharacterSpacing = 1.5f;
// TextParagraph 객체에 텍스트 추가
paragraph.AppendLine("이것은 문자 간격이 있는 단락입니다", state);
// TextParagraph의 위치 지정
paragraph.Position = new Position(100, 550);
// TextBuilder 인스턴스에 TextParagraph 추가
builder.AppendParagraph(paragraph);

dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf";
// 결과 PDF 문서 저장.
pdfDocument.Save(dataDir);
```

### TextStamp 사용하기

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하실 수 있습니다.
// 문서 디렉토리 경로
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Document 인스턴스 생성
Document pdfDocument = new Document();
// 문서의 페이지 컬렉션에 페이지 추가
Page page = pdfDocument.Pages.Add();
// 샘플 텍스트와 함께 TextStamp 인스턴스 생성
TextStamp stamp = new TextStamp("This is text stamp with character spacing");
// Stamp 객체에 대한 글꼴 이름 지정
stamp.TextState.Font = FontRepository.FindFont("Arial");
// TextStamp에 대한 글꼴 크기 지정
stamp.TextState.FontSize = 12;
// 문자 간격을 1f로 지정
stamp.TextState.CharacterSpacing = 1f;
// Stamp의 XIndent 설정
stamp.XIndent = 100;
// Stamp의 YIndent 설정
stamp.YIndent = 500;
// 페이지 인스턴스에 텍스트 스탬프 추가
stamp.Put(page);
dataDir = dataDir + "CharacterSpacingUsingTextStamp_out.pdf";
// 결과 PDF 문서 저장.
pdfDocument.Save(dataDir);
```
## PDF 문서에 다단 칼럼 만들기

잡지와 신문에서는 대부분의 뉴스가 책에서처럼 전체 페이지에 왼쪽에서 오른쪽으로 텍스트 단락이 인쇄되는 대신 단일 페이지에 여러 칼럼으로 표시되는 것을 볼 수 있습니다. Microsoft Word와 Adobe Acrobat Writer와 같은 많은 문서 처리 애플리케이션은 사용자가 단일 페이지에 여러 칼럼을 생성하고 그 안에 데이터를 추가할 수 있도록 합니다.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)은 PDF 문서의 페이지 내부에 여러 칼럼을 생성하는 기능도 제공합니다.
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)은 PDF 문서의 페이지 내에 여러 열을 생성하는 기능도 제공합니다.

열 간격은 열 사이의 공간을 의미하며 기본 열 간격은 1.25cm입니다. 열 너비가 지정되지 않은 경우 [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)은 페이지 크기와 열 간격에 따라 각 열의 너비를 자동으로 계산합니다.

아래 예시는 두 열을 그래프 객체(선)와 함께 생성하고 이를 FloatingBox의 단락 컬렉션에 추가한 다음, 페이지 인스턴스의 단락 컬렉션에 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예시와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET으로 이동하세요.
// 문서 디렉터리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
// PDF 파일의 왼쪽 여백 정보를 지정합니다
doc.PageInfo.Margin.Left = 40;
// PDF 파일의 오른쪽 여백 정보를 지정합니다
doc.PageInfo.Margin.Right = 40;
Page page = doc.Pages.Add();

Aspose.Pdf.Drawing.Graph graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
// 섹션 객체의 단락 컬렉션에 선을 추가합니다
page.Paragraphs.Add(graph1);

// 선의 좌표를 지정합니다
float[] posArr = new float[] { 1, 2, 500, 2 };
Aspose.Pdf.Drawing.Line l1 = new Aspose.Pdf.Drawing.Line(posArr);
graph1.Shapes.Add(l1);
// HTML 태그를 포함한 텍스트가 포함된 문자열 변수를 생성합니다

string s = "<font face=\"Times New Roman\" size=4>" +

"<strong> 돈 사기를 피하는 방법</<strong> "
+ "</font>";
// HTML 텍스트를 포함하는 텍스트 단락을 생성합니다

HtmlFragment heading_text = new HtmlFragment(s);
page.Paragraphs.Add(heading_text);

Aspose.Pdf.FloatingBox box = new Aspose.Pdf.FloatingBox();
// 섹션에 네 개의 열을 추가합니다
box.ColumnInfo.ColumnCount = 2;
// 열 사이의 간격을 설정합니다
box.ColumnInfo.ColumnSpacing = "5";

box.ColumnInfo.ColumnWidths = "105 105";
TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
text1.TextState.FontSize = 8;
text1.TextState.LineSpacing = 2;
box.Paragraphs.Add(text1);
text1.TextState.FontSize = 10;

text1.TextState.FontStyle = FontStyles.Italic;
// 선을 그리기 위한 그래프 객체를 생성합니다
Aspose.Pdf.Drawing.Graph graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
// 선의 좌표를 지정합니다
float[] posArr2 = new float[] { 1, 10, 100, 10 };
Aspose.Pdf.Drawing.Line l2 = new Aspose.Pdf.Drawing.Line(posArr2);
graph2.Shapes.Add(l2);

// 섹션 객체의 단락 컬렉션에 선을 추가합니다
box.Paragraphs.Add(graph2);

TextFragment text2 = new TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
box.Paragraphs.Add(text2);

page.Paragraphs.Add(box);

dataDir = dataDir + "CreateMultiColumnPdf_out.pdf";
// PDF 파일을 저장합니다
doc.Save(dataDir);
```
## 맞춤 탭 정지 작업

탭 정지는 탭을 입력할 때 멈추는 지점입니다. 워드 프로세싱에서 각 줄은 정기적인 간격(예를 들어, 매 반 인치마다)에 배치된 여러 탭 정지를 포함하고 있습니다. 하지만 대부분의 워드 프로세서에서는 원하는 위치에 탭 정지를 설정할 수 있습니다. 탭 키를 누르면 커서 또는 삽입 지점이 다음 탭 정지로 점프합니다. 이 탭 정지는 보이지 않습니다. 탭 정지는 텍스트 파일에 존재하지 않지만, 워드 프로세서는 탭 키에 올바르게 반응할 수 있도록 이를 추적합니다.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)은 개발자가 PDF 문서에서 맞춤 탭 정지를 사용할 수 있도록 합니다. Aspose.Pdf.Text.TabStop 클래스는 [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) 클래스에서 맞춤 탭 정지를 설정하는 데 사용됩니다.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)은 또한 TabLeaderType이라는 열거형으로 몇 가지 사전 정의된 탭 리더 유형을 제공하며, 그 사전 정의된 값과 설명은 아래와 같습니다:
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) 에서는 TabLeaderType이라는 열거형을 통해 몇 가지 사전 정의된 탭 리더 유형을 제공하며, 그 사전 정의된 값과 설명은 아래와 같습니다:

|**탭 리더 유형**|**설명**|
| :- | :- |
|None|탭 리더 없음|
|Solid|실선 탭 리더|
|Dash|대시 탭 리더|
|Dot|점 탭 리더|

다음은 사용자 정의 탭 정지를 설정하는 예입니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document _pdfdocument = new Document();
Page page = _pdfdocument.Pages.Add();

Aspose.Pdf.Text.TabStops ts = new Aspose.Pdf.Text.TabStops();
Aspose.Pdf.Text.TabStop ts1 = ts.Add(100);
ts1.AlignmentType = TabAlignmentType.Right;
ts1.LeaderType = TabLeaderType.Solid;
Aspose.Pdf.Text.TabStop ts2 = ts.Add(200);
ts2.AlignmentType = TabAlignmentType.Center;
ts2.LeaderType = TabLeaderType.Dash;
Aspose.Pdf.Text.TabStop ts3 = ts.Add(300);
ts3.AlignmentType = TabAlignmentType.Left;
ts3.LeaderType = TabLeaderType.Dot;

TextFragment header = new TextFragment("This is a example of forming table with TAB stops", ts);
TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data22 "));
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data23"));

page.Paragraphs.Add(header);
page.Paragraphs.Add(text0);
page.Paragraphs.Add(text1);
page.Paragraphs.Add(text2);

dataDir = dataDir + "CustomTabStops_out.pdf";
_pdfdocument.Save(dataDir);
```
## PDF에 투명 텍스트 추가하기

PDF 파일은 이미지, 텍스트, 그래프, 첨부 파일, 주석 객체를 포함하고 있으며 TextFragment를 생성할 때 전경, 배경색 정보 및 텍스트 형식을 설정할 수 있습니다. Aspose.PDF for .NET은 알파 색상 채널을 사용하여 텍스트를 추가하는 기능을 지원합니다. 다음 코드 스니펫은 투명한 색상으로 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Document 인스턴스 생성
Document doc = new Document();
// PDF 파일의 페이지 컬렉션에 페이지 생성
Aspose.Pdf.Page page = doc.Pages.Add();

// Graph 객체 생성
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// 특정 차원으로 사각형 인스턴스 생성
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
// 알파 색상 채널에서 색상 객체 생성
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// Graph 객체의 도형 컬렉션에 사각형 추가
canvas.Shapes.Add(rect);
// 페이지 객체의 단락 컬렉션에 그래프 객체 추가
page.Paragraphs.Add(canvas);
// 그래프 객체의 위치 변경 안 함 설정
canvas.IsChangePosition = false;

// 샘플 값으로 TextFragment 인스턴스 생성
TextFragment text = new TextFragment("투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 투명 텍스트 ");
// 알파 채널에서 색상 객체 생성
Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
// 텍스트 인스턴스에 대한 색상 정보 설정
text.TextState.ForegroundColor = color;
// 페이지 인스턴스의 단락 컬렉션에 텍스트 추가
page.Paragraphs.Add(text);

dataDir = dataDir + "AddTransparentText_out.pdf";
doc.Save(dataDir);
```
## 글꼴에 대한 줄 간격 지정

모든 글꼴에는 같은 글꼴 크기의 타입 라인 간 거리로 의도된 높이인 추상적인 정사각형이 있습니다.
모든 폰트에는 같은 크기의 글꼴에서 줄 간격을 의도하는 추상 정사각형이 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string fontFile = dataDir + "HPSimplified.TTF";
// 입력 PDF 파일을 로드합니다
Document doc = new Document();
// LineSpacingMode.FullSize를 사용하여 TextFormattingOptions 생성
TextFormattingOptions formattingOptions = new TextFormattingOptions();
formattingOptions.LineSpacing = TextFormattingOptions.LineSpacingMode.FullSize;

// 문서 첫 페이지에 대한 텍스트 빌더 객체 생성
//TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// 샘플 문자열이 포함된 텍스트 조각 생성
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // TrueType 폰트를 스트림 객체로 로드합니다
    using (FileStream fontStream = System.IO.File.OpenRead(fontFile))
    {
        // 텍스트 문자열에 대한 폰트 이름 설정
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // 텍스트 조각의 위치 지정
        textFragment.Position = new Position(100, 600);
        // 현재 조각의 TextFormattingOptions를 사전 정의된 것으로 설정합니다(LineSpacingMode.FullSize를 가리킴)
        textFragment.TextState.FormattingOptions = formattingOptions;
        // 텍스트를 TextBuilder에 추가하여 PDF 파일 위에 배치할 수 있습니다
        //textBuilder.AppendText(textFragment);
        var page = doc.Pages.Add();
        page.Paragraphs.Add(textFragment);
    }

    dataDir = dataDir + "SpecifyLineSpacing_out.pdf";
    // 결과 PDF 문서를 저장합니다
    doc.Save(dataDir);
}
```
## 동적으로 텍스트 너비 가져오기

때때로 텍스트 너비를 동적으로 측정할 필요가 있습니다. Aspose.PDF for .NET은 문자열 너비 측정을 위한 두 가지 메소드를 포함하고 있습니다. Aspose.Pdf.Text.Font 또는 Aspose.Pdf.Text.TextState 클래스(또는 둘 다)의 [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) 메소드를 호출할 수 있습니다. 아래 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Text.Font font = FontRepository.FindFont("Arial");
TextState ts = new TextState();
ts.Font = font;
ts.FontSize = 14;

if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    Console.WriteLine("예상치 못한 글꼴 문자열 측정!");

if (Math.Abs(ts.MeasureString("z") - 7.0) > 0.001)
    Console.WriteLine("예상치 못한 글꼴 문자열 측정!");

for (char c = 'A'; c <= 'z'; c++)
{
    double fnMeasure = font.MeasureString(c.ToString(), 14);
    double tsMeasure = ts.MeasureString(c.ToString());

    if (Math.Abs(fnMeasure - tsMeasure) > 0.001)
        Console.WriteLine("글꼴과 상태 문자열 측정이 일치하지 않습니다!");
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



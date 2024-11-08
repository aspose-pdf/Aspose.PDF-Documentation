---
title: PDF 내에서 C#을 사용한 텍스트 포맷팅
linktitle: PDF 내 텍스트 포맷팅
type: docs
weight: 30
url: /ko/net/text-formatting-inside-pdf/
description: 이 페이지는 PDF 파일 내에서 텍스트를 포맷하는 방법을 설명합니다. 들여쓰기 추가, 텍스트 테두리 추가, 밑줄 텍스트 추가 등이 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 내에서 C#을 사용한 텍스트 포맷팅",
    "alternativeHeadline": "PDF 파일에서 텍스트 포맷 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, pdf 내 텍스트 포맷",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "이 페이지는 PDF 파일 내에서 텍스트를 포맷하는 방법을 설명합니다. 들여쓰기 추가, 텍스트 테두리 추가, 밑줄 텍스트 추가 등이 있습니다."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

## PDF에 줄 들여쓰기 추가 방법

Aspose.PDF for .NET은 [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions) 클래스에 SubsequentLinesIndent 속성을 제공합니다. 이 속성은 TextFragment 및 Paragraphs 컬렉션을 사용한 PDF 생성 시나리오에서 줄 들여쓰기를 지정하는 데 사용할 수 있습니다.

다음 코드 조각을 사용하여 속성을 사용하세요:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 새 문서 객체 생성
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// 텍스트 프래그먼트에 대한 TextFormattingOptions를 초기화하고 SubsequentLinesIndent 값을 지정합니다.
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

document.Save(dataDir + "SubsequentIndent_out.pdf");
```
## 텍스트 테두리 추가 방법

다음 코드 스니펫은 TextBuilder를 사용하여 텍스트에 테두리를 추가하고 TextState의 DrawTextRectangleBorder 속성을 설정하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 새 문서 객체 생성
Document pdfDocument = new Document();
// 특정 페이지 가져오기
Page pdfPage = (Page)pdfDocument.Pages.Add();
// 텍스트 조각 생성
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);
// 텍스트 속성 설정
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// 텍스트 사각형 주위에 테두리 (stroking) 그리기 위한 StrokingColor 속성 설정
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// DrawTextRectangleBorder 속성 값을 true로 설정
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// 문서 저장
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```
## 밑줄 텍스트 추가 방법

다음 코드 스니펫은 새 PDF 파일을 생성할 때 밑줄 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 방문하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 객체 생성
Document pdfDocument = new Document();
// PDF 문서에 페이지 추가
pdfDocument.Pages.Add();
// 첫 번째 페이지에 대한 TextBuilder 생성
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// 샘플 텍스트가 있는 TextFragment
TextFragment fragment = new TextFragment("Test message");
// TextFragment에 대한 폰트 설정
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// 텍스트의 형식을 밑줄로 설정
fragment.TextState.Underline = true;
// TextFragment를 배치할 위치 지정
fragment.Position = new Position(10, 800);
// PDF 파일에 TextFragment 추가
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// 결과 PDF 문서 저장.
pdfDocument.Save(dataDir);
```
## 추가된 텍스트 주위에 테두리 추가 방법

추가하는 텍스트의 모양과 느낌을 제어할 수 있습니다. 아래 예제는 추가한 텍스트 주위에 사각형을 그려 테두리를 추가하는 방법을 보여줍니다. [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스에 대해 자세히 알아보세요.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// 결과 PDF 문서를 저장합니다.
editor.Save(dataDir);
```

## 새 줄 피드 추가 방법
## 새로운 줄 추가하는 방법

TextFragment는 텍스트 내부에 줄 바꿈을 지원하지 않습니다. 그러나 줄 바꿈이 포함된 텍스트를 추가하려면 TextFragment와 TextParagraph를 사용하십시오:

- TextFragment에서 단일 "\n" 대신 "\r\n" 또는 Environment.NewLine을 사용하세요;
- TextParagraph 객체를 생성하세요. 이것은 줄 분할이 있는 텍스트를 추가합니다;
- TextFragment를 TextParagraph.AppendLine에 추가하세요;
- TextParagraph를 TextBuilder.AppendParagraph에 추가하세요.
아래 코드 스니펫을 사용하세요.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// 필요한 줄바꿈 마커를 포함한 텍스트로 새 TextFragment를 초기화합니다
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("지원자 이름: " + Environment.NewLine + " 조 스모");

// 필요한 경우 텍스트 프래그먼트 속성을 설정하세요
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// TextParagraph 객체를 생성하세요
TextParagraph par = new TextParagraph();

// 단락에 새 TextFragment를 추가하세요
par.AppendLine(textFragment);

// 단락 위치를 설정하세요
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// TextBuilder 객체를 생성하세요
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// TextBuilder를 사용하여 TextParagraph를 추가하세요
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// 결과 PDF 문서를 저장하세요.
pdfApplicationDoc.Save(dataDir);
```
## StrikeOut 텍스트 추가하는 방법

TextState 클래스는 PDF 문서 내에 배치되는 TextFragments의 서식을 설정할 수 있는 기능을 제공합니다. 이 클래스를 사용하여 텍스트 서식을 굵게, 기울임꼴, 밑줄, 그리고 이번 릴리스부터는 Strikeout으로 텍스트 서식을 표시할 수 있는 기능을 제공합니다. 다음 코드 스니펫을 사용하여 Strikeout 서식이 있는 TextFragment를 추가해 보세요.

전체 코드 스니펫을 사용하십시오:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 문서 열기
Document pdfDocument = new Document();
// 특정 페이지 가져오기
Page pdfPage = (Page)pdfDocument.Pages.Add();

// 텍스트 프래그먼트 생성
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// 텍스트 속성 설정
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// StrikeOut 속성 설정
textFragment.TextState.StrikeOut = true;
// 텍스트를 굵게 표시
textFragment.TextState.FontStyle = FontStyles.Bold;

// TextBuilder 객체 생성
TextBuilder textBuilder = new TextBuilder(pdfPage);
// PDF 페이지에 텍스트 프래그먼트 추가
textBuilder.AppendText(textFragment);


dataDir = dataDir + "AddStrikeOutText_out.pdf";

// 결과 PDF 문서 저장.
pdfDocument.Save(dataDir);
```
## 텍스트에 그라디언트 음영 적용하기

텍스트 편집 시나리오에서 API의 텍스트 포맷팅이 더욱 향상되었으며 이제 PDF 문서 내부에 패턴 색상 공간을 가진 텍스트를 추가할 수 있습니다. Aspose.Pdf.Color 클래스는 텍스트의 음영 색상을 지정하는데 사용할 수 있는 PatternColorSpace라는 새로운 속성으로 강화되었습니다. 이 새로운 속성은 다음 코드 스니펫에서 보여주는 것처럼 텍스트에 다양한 그라디언트 음영을 추가합니다 예를 들어 축 방향 음영, 방사형 (타입 3) 음영:

```csharp
// 완전한 예제와 데이터 파일은 다음을 참조하세요 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // 패턴 색상 공간으로 새 색상 생성
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```
>원판 그라디언트를 적용하려면 위 코드 스니펫에서 'PatternColorSpace' 속성을 'Aspose.Pdf.Drawing.GradientRadialShading(시작색, 끝색)'과 같이 설정할 수 있습니다.

## 텍스트를 플로팅 콘텐츠에 맞추는 방법

Aspose.PDF는 플로팅 박스 요소 내부의 콘텐츠에 대한 텍스트 정렬 설정을 지원합니다. 다음 코드 샘플에서 보여주는 것처럼 Aspose.Pdf.FloatingBox 인스턴스의 정렬 속성을 사용하여 이를 달성할 수 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
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


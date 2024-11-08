---
title: PDF 내 텍스트 서식 설정을 위한 Python 사용
linktitle: PDF 내 텍스트 서식 설정
type: docs
weight: 30
url: /ko/python-net/text-formatting-inside-pdf/
description: 이 페이지는 PDF 파일 내에서 텍스트를 서식화하는 방법을 설명합니다. 줄 들여쓰기 추가, 텍스트 테두리 추가, 밑줄 텍스트 추가 등이 포함됩니다.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 내 텍스트 서식 설정을 위한 Python 사용",
    "alternativeHeadline": "PDF 파일에서 텍스트 서식화 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, pdf 내 텍스트 서식화",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-formatting-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "이 페이지는 PDF 파일 내에서 텍스트를 서식화하는 방법을 설명합니다. 줄 들여쓰기 추가, 텍스트 테두리 추가, 밑줄 텍스트 추가 등이 포함됩니다."
}
</script>


## PDF에 줄 들여쓰기 추가하는 방법

Aspose.PDF for .NET은 [TextFormattingOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textformattingoptions) 클래스에 SubsequentLinesIndent 속성을 제공합니다. 이는 TextFragment 및 Paragraphs 컬렉션과 함께 PDF 생성 시나리오에서 줄 들여쓰기를 지정하는 데 사용할 수 있습니다.

다음 코드 스니펫을 사용하여 속성을 사용하세요:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 새 문서 객체 생성
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// 텍스트 조각에 대한 TextFormattingOptions를 초기화하고 SubsequentLinesIndent 값을 지정합니다
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

다음 코드 스니펫은 TextBuilder를 사용하고 TextState의 DrawTextRectangleBorder 속성을 설정하여 텍스트에 테두리를 추가하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요
// 문서 디렉토리 경로
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 새로운 문서 객체 생성
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
// 텍스트 직사각형 주위에 테두리(스트로킹)를 그리기 위한 StrokingColor 속성 설정
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
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET를 참조하세요.
// 문서 디렉터리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 객체 생성
Document pdfDocument = new Document();
// PDF 문서에 페이지 추가
pdfDocument.Pages.Add();
// 첫 페이지를 위한 TextBuilder 생성
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// 샘플 텍스트가 포함된 TextFragment
TextFragment fragment = new TextFragment("Test message");
// TextFragment의 폰트 설정
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// 텍스트 서식을 밑줄로 설정
fragment.TextState.Underline = true;
// TextFragment가 배치될 위치 지정
fragment.Position = new Position(10, 800);
// PDF 파일에 TextFragment 추가
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// 결과 PDF 문서 저장.
pdfDocument.Save(dataDir);
```


## 텍스트 추가 주위에 테두리 추가하는 방법

추가한 텍스트의 외관을 제어할 수 있습니다. 아래 예제는 사각형을 그려 추가한 텍스트 주위에 테두리를 추가하는 방법을 보여줍니다. [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor) 클래스에 대해 더 알아보세요.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// 결과 PDF 문서 저장.
editor.Save(dataDir);
```

## 새 줄 추가하는 방법

TextFragment는 텍스트 내의 줄 바꿈을 지원하지 않습니다. 그러나 줄 바꿈이 있는 텍스트를 추가하기 위해서는 TextParagraph와 함께 TextFragment를 사용하십시오:

- 단일 "\n" 대신 "\r\n" 또는 Environment.NewLine을 TextFragment에서 사용하십시오;
- TextParagraph 객체를 생성하십시오. 이는 텍스트를 줄로 분할하여 추가합니다;
- TextFragment를 TextParagraph.AppendLine으로 추가하십시오;
- TextParagraph를 TextBuilder.AppendParagraph로 추가하십시오.
아래 코드 스니핏을 사용하십시오.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하십시오.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// 필요한 줄 바꿈 표식을 포함하는 텍스트로 새로운 TextFragment를 초기화합니다
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// 필요에 따라 텍스트 프래그먼트 속성을 설정합니다
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// TextParagraph 객체를 생성합니다
TextParagraph par = new TextParagraph();

// 새 TextFragment를 문단에 추가합니다
par.AppendLine(textFragment);

// 문단 위치를 설정합니다
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// TextBuilder 객체를 생성합니다
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// TextBuilder를 사용하여 TextParagraph를 추가합니다
textBuilder.AppendParagraph(par);

dataDir = dataDir + "AddNewLineFeed_out.pdf";

// 결과 PDF 문서를 저장합니다.
pdfApplicationDoc.Save(dataDir);
```


## StrikeOut 텍스트 추가하는 방법

TextState 클래스는 PDF 문서 내에 배치되는 TextFragment의 서식을 설정하는 기능을 제공합니다. 이 클래스를 사용하여 텍스트 서식을 굵게, 기울임꼴, 밑줄로 설정할 수 있으며, 이번 릴리스부터 API는 텍스트 서식을 취소선으로 표시하는 기능을 제공합니다. 다음 코드 스니펫을 사용하여 취소선 서식으로 TextFragment를 추가해 보세요.

완전한 코드 스니펫을 사용하세요:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참조하세요.
// 문서 디렉터리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 문서 열기
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
// 취소선 속성 설정
textFragment.TextState.StrikeOut = true;
// 텍스트를 굵게 표시
textFragment.TextState.FontStyle = FontStyles.Bold;

// TextBuilder 객체 생성
TextBuilder textBuilder = new TextBuilder(pdfPage);
// PDF 페이지에 텍스트 조각 추가
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddStrikeOutText_out.pdf";

// 생성된 PDF 문서 저장.
pdfDocument.Save(dataDir);
```


## 텍스트에 그라데이션 음영 적용하기

텍스트 서식은 텍스트 편집 시나리오를 위한 API에서 더욱 향상되었으며, 이제 PDF 문서 내에 패턴 색상 공간을 사용하여 텍스트를 추가할 수 있습니다. Aspose.Pdf.Color 클래스는 텍스트의 음영 색상을 지정할 수 있는 새로운 속성 PatternColorSpace를 도입하여 더욱 강화되었습니다. 이 새로운 속성은 텍스트에 다양한 그라데이션 음영을 추가합니다. 예를 들어, 다음 코드 스니펫에 표시된 것처럼 축형 음영, 방사형 (유형 3) 음영 등이 있습니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참조하세요.
// 문서 디렉토리의 경로.
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


> Radial Gradient를 적용하려면 위 코드 스니펫에서 'PatternColorSpace' 속성을 ‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’로 설정할 수 있습니다.

## 텍스트를 플로팅 콘텐츠에 맞추는 방법

Aspose.PDF는 Floating Box 요소 내부의 콘텐츠에 대한 텍스트 정렬 설정을 지원합니다. Aspose.Pdf.FloatingBox 인스턴스의 정렬 속성을 사용하여 다음 코드 샘플과 같이 이를 구현할 수 있습니다.

```csharp
// 전체 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET를 참조하세요.
// 문서 디렉토리의 경로입니다.
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
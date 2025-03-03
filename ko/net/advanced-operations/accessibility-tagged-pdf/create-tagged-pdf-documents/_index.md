---
title: C#를 사용하여 태그가 지정된 PDF 생성
linktitle: 태그가 지정된 PDF 생성
type: docs
weight: 10
url: /ko/net/create-tagged-pdf/
description: 이 문서는 Aspose.PDF for .NET을 사용하여 프로그래밍 방식으로 태그가 지정된 PDF 문서의 구조 요소를 생성하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#를 사용하여 태그가 지정된 PDF 생성",
    "alternativeHeadline": "태그가 지정된 PDF 생성 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "생성, 태그, PDF",
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
    "url": "/net/create-tagged-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-tagged-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "이 문서는 Aspose.PDF for .NET을 사용하여 프로그래밍 방식으로 태그가 지정된 PDF 문서의 구조 요소를 생성하는 방법을 설명합니다."
}
</script>
태그가 지정된 PDF를 생성한다는 것은 문서에 특정 요소를 추가하거나 생성하여 문서가 PDF/UA 요구 사항에 따라 검증될 수 있도록 하는 것을 의미합니다. 이러한 요소들은 종종 구조 요소라고 불립니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 태그가 지정된 PDF 생성 (간단한 시나리오)

태그가 지정된 PDF 문서에서 구조 요소를 생성하기 위해, Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) 인터페이스를 사용하여 구조 요소를 생성하는 메서드를 제공합니다. 다음 코드 조각은 헤더와 단락 2개 요소가 포함된 태그가 지정된 PDF를 생성하는 방법을 보여줍니다.

```csharp
private static void CreateTaggedPdfDocument01()
{
    // PDF 문서 생성
    var document = new Document();

    // TaggedPdf 작업용 컨텐츠 가져오기
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // 문서의 제목과 언어 설정
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // 
    HeaderElement mainHeader = taggedContent.CreateHeaderElement();
    mainHeader.SetText("Main Header");

    ParagraphElement paragraphElement = taggedContent.CreateParagraphElement();
    paragraphElement.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
    "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
    "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
    "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
    "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
    "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
    "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
    "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
    "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");

    rootElement.AppendChild(mainHeader);
    rootElement.AppendChild(paragraphElement);

    // 태그가 지정된 PDF 문서 저장
    document.Save("C:\\Samples\\TaggedPDF\\Sample1.pdf");
}
```
생성 후 다음 문서를 얻을 수 있습니다.

![태그가 지정된 PDF 문서, 2개의 요소 - 헤더 및 단락](taggedpdf-01.png)

## 중첩 요소가 있는 태그가 지정된 PDF 생성 (구조 요소 트리 생성)

어떤 경우에는 더 복잡한 구조를 만들어야 할 수도 있습니다. 예를 들어 문단에 인용문을 배치합니다.
구조 요소 트리를 생성하려면 [AppendChild](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/appendchild) 메서드를 사용해야 합니다.
다음 코드 스니펫은 태그가 지정된 PDF 문서의 구조 요소 트리를 생성하는 방법을 보여줍니다:

```csharp
private static void CreateTaggedPdfDocument02()
{
    // Pdf 문서 생성
    var document = new Document();

    // TaggedPdf 작업을 위한 컨텐츠 가져오기
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // 문서의 제목 및 언어 설정
    taggedContent.SetTitle("태그가 지정된 PDF 문서");
    taggedContent.SetLanguage("en-US");

    HeaderElement header1 = taggedContent.CreateHeaderElement(1);
    header1.SetText("1단계 헤더");

    ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
    paragraphWithQuotes.StructureTextState.Font = FontRepository.FindFont("Calibri");
    // Adjust position
    paragraphWithQuotes.AdjustPosition(new Aspose.Pdf.Tagged.PositionSettings
    {
        Margin = new Aspose.Pdf.MarginInfo(10, 5, 10, 5)
    });

    SpanElement spanElement1 = taggedContent.CreateSpanElement();
    spanElement1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
    QuoteElement quoteElement = taggedContent.CreateQuoteElement();
    quoteElement.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.");
    quoteElement.StructureTextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
    SpanElement spanElement2 = taggedContent.CreateSpanElement();
    spanElement2.SetText(" Sed non consectetur elit.");

    paragraphWithQuotes.AppendChild(spanElement1);
    paragraphWithQuotes.AppendChild(quoteElement);
    paragraphWithQuotes.AppendChild(spanElement2);

    rootElement.AppendChild(header1);
    rootElement.AppendChild(paragraphWithQuotes);

    // 태그가 지정된 PDF 문서 저장
    document.Save("C:\\Samples\\TaggedPDF\\Sample2.pdf");
}
```
다음과 같은 문서가 생성된 후 얻을 수 있습니다:
![태그가 지정된 PDF 문서에 중첩된 요소 - span과 따옴표](taggedpdf-02.png)

## 텍스트 구조 스타일링

태그가 지정된 PDF 문서에서 텍스트 구조를 스타일링하기 위해, Aspose.PDF는 [StructureTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate) 클래스의 [Font](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/font), [FontSize](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontsize), [FontStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontstyle) 및 [ForegroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/foregroundcolor) 속성을 제공합니다. 다음 코드 스니펫은 태그가 지정된 PDF 문서에서 텍스트 구조를 스타일링하는 방법을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf 문서 생성
Document document = new Document();

// TaggedPdf 작업을 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.TaggedContent;

// 문서의 제목과 언어 설정
taggedContent.SetTitle("태그가 지정된 Pdf 문서");
taggedContent.SetLanguage("en-US");

ParagraphElement p = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(p);

// 개발 중
p.StructureTextState.FontSize = 18F;
p.StructureTextState.ForegroundColor = Color.Red;
p.StructureTextState.FontStyle = FontStyles.Italic;

p.SetText("레드 이탤릭 텍스트.");

// 태그가 지정된 Pdf 문서 저장
document.Save(dataDir + "StyleTextStructure.pdf");
```
## 구조 요소 설명

Tagged PDF 문서에서 구조 요소를 설명하기 위해 Aspose.PDF는 [IllustrationElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/illustrationelement) 클래스를 제공합니다. 다음 코드 스니펫은 Tagged PDF 문서에서 구조 요소를 설명하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf 문서 생성
Document document = new Document();

// TaggedPdf 작업을 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.TaggedContent;

// 문서의 제목 및 언어 설정
taggedContent.SetTitle("Tagged Pdf 문서");
taggedContent.SetLanguage("en-US");

// 개발 중
IllustrationElement figure1 = taggedContent.CreateFigureElement();
taggedContent.RootElement.AppendChild(figure1);
figure1.AlternativeText = "그림 하나";
figure1.Title = "이미지 1";
figure1.SetTag("Fig1");
figure1.SetImage("image.png");

// Tagged Pdf 문서 저장
document.Save(dataDir + "IllustrationStructureElements.pdf");

```

## 태그된 PDF 유효성 검사

Aspose.PDF for .NET은 PDF/UA 태그가 지정된 PDF 문서의 유효성을 검사할 수 있는 기능을 제공합니다. PDF/UA 표준의 유효성 검사는 다음을 지원합니다:

- XObjects 검사
- Actions 검사
- 선택적 콘텐츠 검사
- 내장된 파일 검사
- Acroform 필드 검사(자연 언어 및 대체 이름 및 디지털 서명 유효성 검사)
- XFA 폼 필드 검사
- 보안 설정 검사
- 탐색 검사
- 주석 검사

아래 코드 스니펫은 태그가 지정된 PDF 문서를 검증하는 방법을 보여줍니다. 해당 문제는 XML 로그 보고서에 표시됩니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inputFileName = dataDir + "StructureElements.pdf";
string outputLogName = dataDir + "ua-20.xml";

using (var document = new Aspose.Pdf.Document(inputFileName))
{
    bool isValid = document.Validate(outputLogName, Aspose.Pdf.PdfFormat.PDF_UA_1);

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
    "applicationCategory": ".NET을 위한 PDF 조작 라이브러리",
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


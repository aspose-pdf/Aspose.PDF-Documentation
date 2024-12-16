---
title: 파이썬을 사용하여 PDF 내 텍스트 회전
linktitle: PDF 내 텍스트 회전
type: docs
weight: 50
url: /ko/python-net/rotate-text-inside-pdf/
description: PDF에 텍스트를 회전하는 다양한 방법을 배웁니다. Aspose.PDF는 텍스트를 임의의 각도로 회전하거나 텍스트 조각 또는 전체 단락을 회전할 수 있습니다.
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "파이썬을 사용하여 PDF 내 텍스트 회전",
    "alternativeHeadline": "PDF 파일에서 텍스트를 회전하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 문서 생성",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
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
    "url": "/python-net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/rotate-text-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "PDF에 텍스트를 회전하는 다양한 방법을 배웁니다. Aspose.PDF는 텍스트를 임의의 각도로 회전하거나 텍스트 조각 또는 전체 단락을 회전할 수 있습니다."
}
</script>


## PDF 내부의 텍스트 회전 속성을 사용하여 텍스트 회전

[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment) 클래스의 회전 속성을 사용하여 다양한 각도로 텍스트를 회전할 수 있습니다. 텍스트 회전은 문서 생성의 다양한 시나리오에서 사용할 수 있습니다. 요구 사항에 따라 텍스트를 회전하기 위해 각도를 도 단위로 지정할 수 있습니다. 다음은 텍스트 회전을 구현할 수 있는 다양한 시나리오를 확인해 주시기 바랍니다.

## TextFragment 및 TextBuilder를 사용하여 회전 구현

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참조하세요.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 문서 객체 초기화
Document pdfDocument = new Document();
// 특정 페이지 가져오기
Page pdfPage = (Page)pdfDocument.Pages.Add();
// 텍스트 조각 생성
TextFragment textFragment1 = new TextFragment("main text");
textFragment1.Position = new Position(100, 600);
// 텍스트 속성 설정
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 회전된 텍스트 조각 생성
TextFragment textFragment2 = new TextFragment("rotated text");
textFragment2.Position = new Position(200, 600);
// 텍스트 속성 설정
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// 회전된 텍스트 조각 생성
TextFragment textFragment3 = new TextFragment("rotated text");
textFragment3.Position = new Position(300, 600);
// 텍스트 속성 설정
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// TextBuilder 객체 생성
TextBuilder textBuilder = new TextBuilder(pdfPage);
// PDF 페이지에 텍스트 조각 추가
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// 문서 저장
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```


## TextParagraph 및 TextBuilder를 사용한 회전 구현 (회전된 조각)

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참조하세요.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 문서 객체 초기화
Document pdfDocument = new Document();
// 특정 페이지 가져오기
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// 텍스트 조각 생성
TextFragment textFragment1 = new TextFragment("rotated text");
// 텍스트 속성 설정
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 회전 설정
textFragment1.TextState.Rotation = 45;
// 텍스트 조각 생성
TextFragment textFragment2 = new TextFragment("main text");
// 텍스트 속성 설정
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 텍스트 조각 생성
TextFragment textFragment3 = new TextFragment("another rotated text");
// 텍스트 속성 설정
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 회전 설정
textFragment3.TextState.Rotation = -45;
// 텍스트 조각을 단락에 추가
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// TextBuilder 객체 생성
TextBuilder textBuilder = new TextBuilder(pdfPage);
// PDF 페이지에 텍스트 단락 추가
textBuilder.AppendParagraph(paragraph);
// 문서 저장
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```


## TextFragment 및 Page.Paragraphs를 사용하여 회전 구현

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에 있습니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 문서 객체 초기화
Document pdfDocument = new Document();
// 특정 페이지 가져오기
Page pdfPage = (Page)pdfDocument.Pages.Add();
// 텍스트 조각 생성
TextFragment textFragment1 = new TextFragment("main text");
// 텍스트 속성 설정
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 텍스트 조각 생성
TextFragment textFragment2 = new TextFragment("rotated text");
// 텍스트 속성 설정
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 회전 설정
textFragment2.TextState.Rotation = 315;
// 텍스트 조각 생성
TextFragment textFragment3 = new TextFragment("rotated text");
// 텍스트 속성 설정
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 회전 설정
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// 문서 저장
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```


## TextParagraph 및 TextBuilder를 사용하여 회전 구현 (문단 전체 회전)

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET를 참조하세요.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 문서 객체 초기화
Document pdfDocument = new Document();
// 특정 페이지 가져오기
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // 회전 지정
    paragraph.Rotation = i * 90 + 45;
    // 텍스트 조각 생성
    TextFragment textFragment1 = new TextFragment("문단 텍스트");
    // 텍스트 조각 생성
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // 텍스트 조각 생성
    TextFragment textFragment2 = new TextFragment("두 번째 줄의 텍스트");
    // 텍스트 속성 설정
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // 텍스트 조각 생성
    TextFragment textFragment3 = new TextFragment("그리고 더 많은 텍스트...");
    // 텍스트 속성 설정
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // TextBuilder 객체 생성
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // PDF 페이지에 텍스트 조각 추가
    textBuilder.AppendParagraph(paragraph);
}
// 문서 저장
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
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
---
title: PDF용 텍스트 주석 사용하기
linktitle: 텍스트 주석
type: docs
weight: 10
url: /ko/net/text-annotation/
description: Aspose.PDF for .NET은 PDF 문서에서 텍스트 주석을 추가, 가져오기 및 삭제할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF용 텍스트 주석 사용하기",
    "alternativeHeadline": "PDF에서 텍스트 주석 추가 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, 텍스트 주석",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET은 PDF 문서에서 텍스트 주석을 추가, 가져오기 및 삭제할 수 있습니다."
}
</script>
## 기존 PDF 파일에 텍스트 주석 추가하기

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

텍스트 주석은 PDF 문서의 특정 위치에 첨부된 주석입니다. 주석이 닫혀 있으면 아이콘으로 표시되며, 열리면 독자가 선택한 글꼴과 크기로 메모 텍스트가 포함된 팝업 창이 표시되어야 합니다.

주석은 특정 페이지의 [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) 컬렉션에 포함되어 있습니다. 이 컬렉션은 해당 페이지의 주석만 포함하며, 각 페이지마다 자체 Annotations 컬렉션이 있습니다.

특정 페이지에 주석을 추가하려면, [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add) 메서드를 사용하여 해당 페이지의 Annotations 컬렉션에 추가하십시오.

1. 먼저 PDF에 추가하고자 하는 주석을 생성하십시오.
1. 그런 다음 입력 PDF를 엽니다.
1.
1.

PDF 페이지에 주석을 추가하는 방법을 보여주는 다음 코드 스니펫입니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// 문서 열기
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// 주석 생성
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "샘플 주석 제목";
textAnnotation.Subject = "샘플 주제";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "주석의 샘플 내용";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;

Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

// 페이지의 주석 컬렉션에 주석 추가
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// 출력 파일 저장
pdfDocument.Save(dataDir);
```
## 팝업 주석 추가 방법

팝업 주석은 입력 및 편집을 위해 팝업 창에 텍스트를 표시합니다. 단독으로 나타나지 않으며 마크업 주석, 부모 주석과 연결되어 있으며 부모의 텍스트를 편집하는 데 사용됩니다.

자체적인 외관 스트림이나 연관된 작업이 없어야 하며 부모의 주석 사전에서 Popup 항목으로 식별됩니다.

다음 코드 스니펫은 PDF 페이지에 [팝업 주석](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation)을 추가하는 방법을 보여줍니다. 부모의 [라인 주석](/pdf/ko/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file)을 추가하는 예제를 사용합니다.

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // 문서 디렉토리 경로입니다.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // PDF 파일을 로드합니다
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

                // 라인 주석 생성
                var lineAnnotation = new LineAnnotation(
                    document.Pages[1],
                    new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443))
                {
                    Title = "John Smith",
                    Color = Color.Red,
                    Width = 3,
                    StartingStyle = LineEnding.OpenArrow,
                    EndingStyle = LineEnding.OpenArrow,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
                };

                // 페이지에 주석 추가
                document.Pages[1].Annotations.Add(lineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
## 새로운 자유 텍스트 주석 추가(또는 생성)

자유 텍스트 주석은 페이지에 직접 텍스트를 표시합니다. [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 메소드는 이 유형의 주석을 생성할 수 있습니다. 다음 스니펫에서는 문자열의 첫 번째 발생 위에 자유 텍스트 주석을 추가합니다.

```csharp
private static void AddFreeTextAnnotationDemo()
{
    _document = new Document(@"C:\tmp\pdf-sample.pdf");
    var pdfContentEditor = new PdfContentEditor(_document);

    tfa.Visit(_document.Pages[1]);
    if (tfa.TextFragments.Count <= 0) return;
    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number
    pdfContentEditor.Save(@"C:\tmp\pdf-sample-0.pdf");
}
```

### 자유 텍스트 주석에 콜아웃 속성 설정
### FreeTextAnnotation에 대한 Callout 속성 설정

PDF 문서에서 주석 구성을 더 유연하게 설정하기 위해 Aspose.PDF for .NET은 FreeTextAnnotation 클래스의 [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) 속성을 제공합니다. 이 속성은 콜아웃 라인의 포인트 배열을 지정할 수 있습니다. 다음 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for.NET을 참조하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```
### XFDF 파일에 대한 콜아웃 속성 설정

XFDF 파일에서 가져오기를 사용하실 경우, 단순히 Callout 대신 callout-line 이름을 사용해 주세요. 다음 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document( dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```

다음 메서드는 XFDF를 생성하는 데 사용됩니다:

```csharp
/// <summary>
/// XFDF 생성
/// </summary>
/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">This is a sample</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```
### 자유 텍스트 주석을 보이지 않게 만들기

때때로 문서를 볼 때는 보이지 않지만 문서를 인쇄할 때는 보여야 하는 워터마크를 생성할 필요가 있습니다. 이 목적을 위해 주석 플래그를 사용하세요. 다음 코드 스니펫에서는 이를 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// 문서 열기
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// 출력 파일 저장
doc.Save(dataDir);
```
### FreeTextAnnotation의 서식 설정

이 부분에서는 자유 텍스트 주석 내의 텍스트 서식을 설정하는 방법을 살펴봅니다.

주석은 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션에 포함되어 있습니다. PDF 문서에 [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)을 추가할 때는 [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index) 클래스를 사용하여 글꼴, 크기, 색상 등의 서식 정보를 지정할 수 있습니다. 또한, TextStyle 속성을 사용하여 서식 정보를 지정할 수 있습니다. 또한, PDF 문서에 이미 있는 FreeTextAnnotation의 서식을 업데이트할 수 있습니다.

[TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) 클래스는 기본 스타일 항목을 사용하는 작업을 지원합니다.
[TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) 클래스는 기본 스타일 항목을 사용하는 것을 지원합니다.

- FontName 속성은 글꼴 이름을 가져오거나 설정합니다 (문자열).
- FontSize 속성은 기본 텍스트 크기를 가져오고 설정합니다 (더블).
- System.Drawing.Color 속성은 텍스트 색상을 가져오고 설정합니다 (색상).
- TextAlignment 속성은 주석의 텍스트 정렬을 가져오고 설정합니다 (정렬).

다음 코드 스니펫은 특정 텍스트 포맷으로 FreeTextAnnotation을 추가하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-SetFreeTextAnnotationFormatting-SetFreeTextAnnotationFormatting.cs" >}}

{{% alert color="primary" %}}

자유 텍스트 주석의 내용이나 텍스트 스타일을 변경할 때, 주석의 모양이 변경사항을 반영하도록 재생성됩니다.

{{% /alert %}}

### StrikeOutAnnotation을 사용하여 단어에 취소선 추가하기

Aspose.PDF for .NET은 PDF 문서에서 주석을 추가, 삭제 및 업데이트할 수 있습니다.
Aspose.PDF for .NET은 PDF 문서에서 주석을 추가, 삭제 및 업데이트할 수 있습니다.

특정 TextFragment에 취소선을 그으려면:

1. PDF 파일에서 TextFragment를 검색합니다.
1. TextFragment 객체의 좌표를 가져옵니다.
1. 좌표를 사용하여 StrikeOutAnnotation 객체를 인스턴스화합니다.

다음 코드 스니펫은 특정 TextFragment를 검색하고 해당 객체에 StrikeOutAnnotation을 추가하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

이 기능은 버전 19.6 이상에서 지원됩니다.

{{% /alert %}}

## PDF 파일의 페이지에서 모든 주석 삭제

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션은 해당 페이지의 모든 주석을 포함합니다.
[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션은 해당 페이지의 모든 주석을 포함합니다.

다음 코드 스니펫은 특정 페이지에서 모든 주석을 삭제하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// 문서 열기
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// 특정 주석 삭제
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```

## PDF 파일에서 특정 주석 삭제

{{% alert color="primary" %}}

Aspose.PDF의 품질을 확인하고 이 링크에서 결과를 얻을 수 있습니다:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF는 PDF 파일에서 특정 주석을 제거할 수 있습니다. 이 주제에서는 방법을 설명합니다.

PDF에서 특정 주석을 삭제하려면 [페이지](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체에 속한 [AnnotationCollection 컬렉션의 Delete 메소드](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1)를 호출하세요. Delete 메소드는 삭제하려는 주석의 인덱스가 필요합니다. 그런 다음 업데이트된 PDF 파일을 저장하세요. 다음 코드 스니펫은 특정 주석을 삭제하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// 문서 열기
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// 특정 주석 삭제
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```
## PDF 문서의 페이지에서 모든 주석 가져오기

Aspose.PDF를 사용하면 전체 문서 또는 지정된 페이지에서 주석을 가져올 수 있습니다. PDF 문서의 페이지에서 모든 주석을 가져오려면 원하는 페이지 리소스의 [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션을 반복합니다. 다음 코드 스니펫은 페이지의 모든 주석을 가져오는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// 문서 열기
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// 모든 주석을 반복 처리
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // 주석 속성 가져오기
    Console.WriteLine("제목 : {0} ", annotation.Title);
    Console.WriteLine("주제 : {0} ", annotation.Subject);
    Console.WriteLine("내용 : {0} ", annotation.Contents);
}
```
PDF 전체에서 모든 주석을 가져오려면 먼저 문서의 PageCollection 클래스 컬렉션을 반복한 다음 AnnotationCollection 클래스 컬렉션을 탐색해야 합니다. 컬렉션의 각 주석은 MarkupAnnotation 클래스라는 기본 주석 유형에서 가져올 수 있으며 그 속성을 표시할 수 있습니다.

## PDF 파일에서 특정 주석 가져오기

주석은 개별 페이지와 연관되어 있으며 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션에 저장됩니다.
개별 페이지에 연관된 주석은 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션에 저장됩니다.

```csharp
// 전체 예시와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// 문서 열기
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// 특정 주석 가져오기
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];

// 주석 속성 가져오기
Console.WriteLine("Title : {0} ", textAnnotation.Title);
Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
```

## 주석의 리소스 가져오기

Aspose.PDF는 전체 문서 또는 지정된 페이지에서 주석의 리소스를 가져올 수 있습니다.
Aspose.PDF를 사용하면 전체 문서 또는 지정된 페이지에서 주석의 리소스를 가져올 수 있습니다.

```csharp
// 완벽한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// 문서 열기
Document doc = new Document(dataDir + "AddAnnotation.pdf");
// 주석 생성
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// 문서 저장
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

// 문서 열기
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

// 주석의 액션 가져오기
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;

// 렌디션 액션의 렌디션 가져오기
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;

// 미디어 클립
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
// 미디어 데이터는 FileSpecification.Contents에서 접근 가능합니다.
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
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
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
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


---
title: 구조 요소 속성 설정
linktitle: 구조 요소 속성 설정
type: docs
weight: 30
url: /net/setting-structure-elements-properties/
description: Aspose.PDF for .NET으로 PDF 문서의 다양한 구조 요소 속성을 설정할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "구조 요소 속성 설정",
    "alternativeHeadline": "구조적 요소의 속성을 설정하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 텍스트 구조 설정, 언어 설정, 제목 설정, 노트 구조 요소 설정",
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
    "url": "/net/setting-structure-elements-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/setting-structure-elements-properties/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET으로 PDF 문서의 다양한 구조 요소 속성을 설정할 수 있습니다."
}
</script>

태그가 지정된 PDF 문서에서 구조 요소의 속성을 설정하려면 Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) 인터페이스의 [CreateSectElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createsectelement) 및 [CreateHeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createheaderelement/index) 메서드를 제공합니다.

다음 코드 조각은 태그가 지정된 PDF 문서의 구조 요소 속성을 설정하는 방법을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf 문서 생성
Document document = new Document();

// TaggedPdf 작업을 위한 내용 가져오기
ITaggedContent taggedContent = document.TaggedContent;

// 문서의 제목과 언어 설정
taggedContent.SetTitle("Tagged Pdf 문서");
taggedContent.SetLanguage("en-US");

// 구조 요소 생성
StructureElement rootElement = taggedContent.RootElement;

SectElement sect = taggedContent.CreateSectElement();
rootElement.AppendChild(sect);

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
sect.AppendChild(h1);
h1.SetText("헤더");

h1.Title = "제목";
h1.Language = "en-US";
h1.AlternativeText = "대체 텍스트";
h1.ExpansionText = "확장 텍스트";
h1.ActualText = "실제 텍스트";

// 태그가 지정된 Pdf 문서 저장
document.Save(dataDir + "StructureElementsProperties.pdf");
```
## 텍스트 구조 요소 설정

Tagged PDF 문서의 텍스트 구조 요소를 설정하기 위해 Aspose.PDF는 [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement) 클래스를 제공합니다. 다음 코드 스니펫은 Tagged PDF 문서의 텍스트 구조 요소를 설정하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf 문서 생성
Document document = new Document();

// TaggedPdf 작업을 위한 컨텐츠 가져오기
ITaggedContent taggedContent = document.TaggedContent;

// 문서의 제목과 언어 설정
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// 루트 구조 요소 가져오기
StructureElement rootElement = taggedContent.RootElement;

ParagraphElement p = taggedContent.CreateParagraphElement();
// 텍스트를 텍스트 구조 요소에 설정
p.SetText("Paragraph.");
rootElement.AppendChild(p);


// Tagged Pdf 문서 저장
document.Save(dataDir + "TextStructureElement.pdf");
```
## 텍스트 블록 구조 요소 설정

태그가 지정된 PDF 문서의 텍스트 블록 구조 요소를 설정하기 위해 Aspose.PDF는 [HeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/headerelement) 및 [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement) 클래스를 제공합니다. 이러한 클래스의 객체를 [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement) 객체의 자식으로 추가할 수 있습니다.
다음 코드 스니펫은 태그가 지정된 PDF 문서의 텍스트 블록 구조 요소를 설정하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf 문서 생성
Document document = new Document();

// 태그가 지정된 Pdf 작업을 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.TaggedContent;

// 문서의 제목 및 언어 설정
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// 루트 구조 요소 가져오기
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
h1.SetText("H1. 1단계 헤더");
h2.SetText("H2. 2단계 헤더");
h3.SetText("H3. 3단계 헤더");
h4.SetText("H4. 4단계 헤더");
h5.SetText("H5. 5단계 헤더");
h6.SetText("H6. 6단계 헤더");
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.AppendChild(p);

// 태그가 지정된 Pdf 문서 저장
document.Save(dataDir + "TextBlockStructureElements.pdf");
```
## 인라인 구조 요소 설정

태그가 지정된 PDF 문서의 인라인 구조 요소를 설정하기 위해 Aspose.PDF는 [SpanElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/spanelement) 및 [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement) 클래스를 제공합니다. 이 클래스의 객체를 [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement) 객체의 자식으로 추가할 수 있습니다. 다음 코드 스니펫은 태그가 지정된 PDF 문서의 인라인 구조 요소를 설정하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 방문하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf 문서 생성
Document document = new Document();

// TaggedPdf 작업을 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.TaggedContent;

// 문서의 제목 및 언어 설정
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// 루트 구조 요소 가져오기
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

SpanElement spanH11 = taggedContent.CreateSpanElement();
spanH11.SetText("H1. ");
h1.AppendChild(spanH11);
SpanElement spanH12 = taggedContent.CreateSpanElement();
spanH12.SetText("1단계 헤더");
h1.AppendChild(spanH12);

SpanElement spanH21 = taggedContent.CreateSpanElement();
spanH21.SetText("H2. ");
h2.AppendChild(spanH21);
SpanElement spanH22 = taggedContent.CreateSpanElement();
spanH22.SetText("2단계 헤더");
h2.AppendChild(spanH22);

SpanElement spanH31 = taggedContent.CreateSpanElement();
spanH31.SetText("H3. ");
h3.AppendChild(spanH31);
SpanElement spanH32 = taggedContent.CreateSpanElement();
spanH32.SetText("3단계 헤더");
h3.AppendChild(spanH32);

SpanElement spanH41 = taggedContent.CreateSpanElement();
spanH41.SetText("H4. ");
h4.AppendChild(spanH41);
SpanElement spanH42 = taggedContent.CreateSpanElement();
spanH42.SetText("4단계 헤더");
h4.AppendChild(spanH42);

SpanElement spanH51 = taggedContent.CreateSpanElement();
spanH51.SetText("H5. ");
h5.AppendChild(spanH51);
SpanElement spanH52 = taggedContent.CreateSpanElement();
spanH52.SetText("5단계 헤더");
h5.AppendChild(spanH52);

SpanElement spanH61 = taggedContent.CreateSpanElement();
spanH61.SetText("H6. ");
h6.AppendChild(spanH61);
SpanElement spanH62 = taggedContent.CreateSpanElement();
spanH62.SetText("6단계 헤더");
h6.AppendChild(spanH62);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. ");
rootElement.AppendChild(p);
SpanElement span1 = taggedContent.CreateSpanElement();
span1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.AppendChild(span1);
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.AppendChild(span2);
SpanElement span3 = taggedContent.CreateSpanElement();
span3.SetText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.AppendChild(span3);
SpanElement span4 = taggedContent.CreateSpanElement();
span4.SetText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.AppendChild(span4);
SpanElement span5 = taggedContent.CreateSpanElement();
span5.SetText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.AppendChild(span5);
SpanElement span6 = taggedContent.CreateSpanElement();
span6.SetText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.AppendChild(span6);
SpanElement span7 = taggedContent.CreateSpanElement();
span7.SetText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.AppendChild(span7);
SpanElement span8 = taggedContent.CreateSpanElement();
span8.SetText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.AppendChild(span8);
SpanElement span9 = taggedContent.CreateSpanElement();
span9.SetText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.AppendChild(span9);
SpanElement span10 = taggedContent.CreateSpanElement();
span10.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.AppendChild(span10);

// 태그가 지정된 Pdf 문서 저장
document.Save(dataDir + "InlineStructureElements.pdf");
```
## 사용자 정의 태그 이름 설정

Tagged PDF Document의 요소에 사용자 정의 태그 이름을 설정하기 위해, Aspose.PDF는 요소에 대한 StructureElement 클래스의 [SetTag](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/methods/settag) 메소드를 제공합니다. 다음 코드 스니펫은 사용자 정의 태그 이름을 설정하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일에 대해서는 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참고하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf 문서 생성
Document document = new Document();

// TaggedPdf 작업을 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.TaggedContent;

// 문서 제목 및 언어 설정
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// 논리 구조 요소 생성
SectElement sect = taggedContent.CreateSectElement();
taggedContent.RootElement.AppendChild(sect);

ParagraphElement p1 = taggedContent.CreateParagraphElement();
ParagraphElement p2 = taggedContent.CreateParagraphElement();
ParagraphElement p3 = taggedContent.CreateParagraphElement();
ParagraphElement p4 = taggedContent.CreateParagraphElement();

p1.SetText("P1. ");
p2.SetText("P2. ");
p3.SetText("P3. ");
p4.SetText("P4. ");

p1.SetTag("P1");
p2.SetTag("Para");
p3.SetTag("Para");
p4.SetTag("Paragraph");

sect.AppendChild(p1);
sect.AppendChild(p2);
sect.AppendChild(p3);
sect.AppendChild(p4);

SpanElement span1 = taggedContent.CreateSpanElement();
SpanElement span2 = taggedContent.CreateSpanElement();
SpanElement span3 = taggedContent.CreateSpanElement();
SpanElement span4 = taggedContent.CreateSpanElement();

span1.SetText("Span 1.");
span2.SetText("Span 2.");
span3.SetText("Span 3.");
span4.SetText("Span 4.");

span1.SetTag("SPAN");
span2.SetTag("Sp");
span3.SetTag("Sp");
span4.SetTag("TheSpan");

p1.AppendChild(span1);
p2.AppendChild(span2);
p3.AppendChild(span3);
p4.AppendChild(span4);

// Tagged Pdf 문서 저장
document.Save(dataDir + "CustomTag.pdf");
```
## 요소에 구조 요소 추가

**이 기능은 버전 19.4 이상에서 지원됩니다.**

태그가 지정된 PDF 문서에서 링크 구조 요소를 설정하려면 Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) 인터페이스의 [CreateLinkElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createlinkelement) 메소드를 제공합니다. 다음 코드 조각은 태그가 지정된 PDF 문서의 텍스트가 있는 단락에 구조 요소를 설정하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "LinkStructureElements_Output.pdf";
string logFile = dataDir + "46035_log.xml";
string imgFile = dataDir + "google-icon-512.png";

// 문서 생성 및 태그 지정된 PDF 콘텐츠 가져오기
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// 문서의 제목 및 자연 언어 설정
taggedContent.SetTitle("Link Elements Example");
taggedContent.SetLanguage("en-US");

// 루트 구조 요소 가져오기 (문서 구조 요소)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
LinkElement link1 = taggedContent.CreateLinkElement();
p1.AppendChild(link1);
link1.Hyperlink = new WebHyperlink("http://google.com");
link1.SetText("Google");
link1.AlternateDescriptions = "Google로의 링크";


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
LinkElement link2 = taggedContent.CreateLinkElement();
p2.AppendChild(link2);
link2.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Google");
link2.AppendChild(span2);
link2.AlternateDescriptions = "Google로의 링크";


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
LinkElement link3 = taggedContent.CreateLinkElement();
p3.AppendChild(link3);
link3.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("G");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText("oogle");
link3.AppendChild(span31);
link3.SetText("-");
link3.AppendChild(span32);
link3.AlternateDescriptions = "Google로의 링크";


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
LinkElement link4 = taggedContent.CreateLinkElement();
p4.AppendChild(link4);
link4.Hyperlink = new WebHyperlink("http://google.com");
link4.SetText("다중 줄 링크: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google");
link4.AlternateDescriptions = "Google로의 링크 (다중 줄)";


ParagraphElement p5 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p5);
LinkElement link5 = taggedContent.CreateLinkElement();
p5.AppendChild(link5);
link5.Hyperlink = new WebHyperlink("http://google.com");
FigureElement figure5 = taggedContent.CreateFigureElement();
figure5.SetImage(imgFile, 1200);
figure5.AlternativeText = "Google 아이콘";
StructureAttributes linkLayoutAttributes = link5.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
placementAttribute.SetNameValue(AttributeName.Placement_Block);
linkLayoutAttributes.SetAttribute(placementAttribute);
link5.AppendChild(figure5);
link5.AlternateDescriptions = "Google로의 링크";


// 태그 지정된 PDF 문서 저장
document.Save(outFile);

// PDF/UA 준수 확인
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("PDF/UA 준수: {0}", isPdfUaCompliance));
```
## 링크 구조 요소 설정

**이 기능은 버전 19.4 이상에서 지원됩니다.**

Aspose.PDF for .NET API는 링크 구조 요소를 추가할 수도 있습니다. 다음 코드 스니펫은 태그가 지정된 PDF 문서에 링크 구조 요소를 추가하는 방법을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
string logFile = dataDir + "46144_log.xml";

// 문서 생성 및 태그된 PDF 내용 가져오기
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// 문서의 제목 및 자연어 설정
taggedContent.SetTitle("Text Elements Example");
taggedContent.SetLanguage("en-US");

// 루트 구조 요소 가져오기 (문서 구조 요소)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
SpanElement span11 = taggedContent.CreateSpanElement();
span11.SetText("Span_11");
SpanElement span12 = taggedContent.CreateSpanElement();
span12.SetText(" and Span_12.");
p1.SetText("Paragraph with ");
p1.AppendChild(span11);
p1.AppendChild(span12);


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
SpanElement span21 = taggedContent.CreateSpanElement();
span21.SetText("Span_21");
SpanElement span22 = taggedContent.CreateSpanElement();
span22.SetText("Span_22.");
p2.AppendChild(span21);
p2.SetText(" and ");
p2.AppendChild(span22);


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("Span_31");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText(" and Span_32");
p3.AppendChild(span31);
p3.AppendChild(span32);
p3.SetText(".");


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
SpanElement span41 = taggedContent.CreateSpanElement();
SpanElement span411 = taggedContent.CreateSpanElement();
span411.SetText("Span_411, ");
span41.SetText("Span_41, ");
span41.AppendChild(span411);
SpanElement span42 = taggedContent.CreateSpanElement();
SpanElement span421 = taggedContent.CreateSpanElement();
span421.SetText("Span 421 and ");
span42.AppendChild(span421);
span42.SetText("Span_42");
p4.AppendChild(span41);
p4.AppendChild(span42);
p4.SetText(".");


// 태그가 지정된 PDF 문서 저장
document.Save(outFile);

// PDF/UA 준수 확인
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("PDF/UA 준수 여부: {0}", isPdfUaCompliance));
```
## 노트 구조 요소 설정

Aspose.PDF for .NET API는 태그가 지정된 PDF 문서에 [NoteElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/noteelement)를 추가할 수도 있습니다. 다음 코드 스니펫은 태그가 지정된 PDF 문서에 노트 요소를 추가하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "45929_doc.pdf";
string logFile = dataDir + "45929_log.xml";

// Pdf 문서 생성
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("노트 요소의 예");
taggedContent.SetLanguage("en-US");

// 문단 요소 추가
ParagraphElement paragraph = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(paragraph);

// NoteElement 추가
NoteElement note1 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note1);
note1.SetText("자동 생성 ID를 가진 노트. ");

// NoteElement 추가
NoteElement note2 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note2);
note2.SetText("ID = 'note_002'인 노트. ");
note2.SetId("note_002");

// NoteElement 추가
NoteElement note3 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note3);
note3.SetText("ID = 'note_003'인 노트. ");
note3.SetId("note_003");

// 예외 발생 필요 - Aspose.Pdf.Tagged.TaggedException : ID='note_002'인 구조 요소가 이미 존재함
//note3.SetId("note_002");

// 노트 구조 요소에 대해 ClearId()를 사용하면 PDF/UA 준수가 되지 않음
//note3.ClearId();


// 태그가 지정된 PDF 문서 저장
document.Save(outFile);

// PDF/UA 준수성 검사
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("PDF/UA 준수: {0}", isPdfUaCompliance));
```
## 언어 및 제목 설정

**이 기능은 19.6 버전 이상에서 지원됩니다.**

Aspose.PDF for .NET API는 PDF/UA 사양에 따라 문서의 언어와 제목을 설정할 수 있습니다. 언어는 전체 문서 또는 개별 구조적 요소에 대해 설정할 수 있습니다. 다음 코드 조각은 태그가 지정된 PDF 문서에서 언어와 제목을 설정하는 방법을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
Document document = new Document();
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// TaggedContent 가져오기
Tagged.ITaggedContent taggedContent = document.TaggedContent;

// 제목 및 언어 설정
taggedContent.SetTitle("예제 태그 문서");
taggedContent.SetLanguage("en-US");

// 헤더 (en-US, 문서에서 상속됨)
LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
h1.SetText("다양한 언어의 문구");
taggedContent.RootElement.AppendChild(h1);

// 문단 (영어)
LogicalStructure.ParagraphElement pEN = taggedContent.CreateParagraphElement();
pEN.SetText("Hello, World!");
pEN.Language = "en-US";
taggedContent.RootElement.AppendChild(pEN);

// 문단 (독일어)
LogicalStructure.ParagraphElement pDE = taggedContent.CreateParagraphElement();
pDE.SetText("Hallo Welt!");
pDE.Language = "de-DE";
taggedContent.RootElement.AppendChild(pDE);

// 문단 (프랑스어)
LogicalStructure.ParagraphElement pFR = taggedContent.CreateParagraphElement();
pFR.SetText("Bonjour le monde!");
pFR.Language = "fr-FR";
taggedContent.RootElement.AppendChild(pFR);

// 문단 (스페인어)
LogicalStructure.ParagraphElement pSP = taggedContent.CreateParagraphElement();
pSP.SetText("¡Hola Mundo!");
pSP.Language = "es-ES";
taggedContent.RootElement.AppendChild(pSP);

// 태그가 지정된 Pdf 문서 저장
document.Save(dataDir + "SetupLanguageAndTitle.pdf");
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


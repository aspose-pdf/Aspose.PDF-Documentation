---
title: PDF에서 태그된 콘텐츠 추출
linktitle: 태그된 콘텐츠 추출
type: docs
weight: 20
url: /net/extract-tagged-content-from-tagged-pdfs/
description: 이 글은 Aspose.PDF for .NET을 사용하여 PDF 문서에서 태그된 콘텐츠를 추출하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 태그된 콘텐츠 추출",
    "alternativeHeadline": "PDF에서 이미지 태그하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "태그, pdf, 추출",
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
    "url": "/net/extract-tagged-content-from-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-tagged-content-from-tagged-pdfs/"
    },
    "dateModified": "2022-02-04",
    "description": "이 글은 Aspose.PDF for .NET을 사용하여 PDF 문서에서 태그된 콘텐츠를 추출하는 방법을 설명합니다."
}
</script>
이 문서에서는 C#을 사용하여 태그가 지정된 콘텐츠 PDF 문서를 추출하는 방법을 배우게 됩니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

## 태그된 PDF 콘텐츠 가져오기

태그된 텍스트가 있는 PDF 문서의 콘텐츠를 가져오기 위해 Aspose.PDF는 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 [TaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/taggedcontent) 속성을 제공합니다.

다음 코드 스니펫은 태그된 텍스트가 있는 PDF 문서의 콘텐츠를 가져오는 방법을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf 문서 생성
Document document = new Document();

// TaggedPdf와 작업할 콘텐츠 가져오기
ITaggedContent taggedContent = document.TaggedContent;

//
// Tagged Pdf 콘텐츠 작업
//

// 문서의 제목과 언어 설정
taggedContent.SetTitle("Simple Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// Tagged Pdf 문서 저장
document.Save(dataDir + "TaggedPDFContent.pdf");
```
## 루트 구조 얻기

Tagged PDF 문서의 루트 구조를 얻기 위해, Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) 인터페이스의 [StructTreeRootElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement) 속성과 [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement)를 제공합니다. 다음 코드 스니펫은 Tagged PDF 문서의 루트 구조를 얻는 방법을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf 문서 생성
Document document = new Document();

// TaggedPdf 작업을 위한 콘텐츠 가져오기
ITaggedContent taggedContent = document.TaggedContent;

// 문서의 제목과 언어 설정
taggedContent.SetTitle("Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// StructTreeRootElement 속성과 RootElement는 pdf 문서의 StructTreeRoot 객체와
// 루트 구조 요소(문서 구조 요소)에 접근하기 위해 사용됩니다.
StructTreeRootElement structTreeRootElement = taggedContent.StructTreeRootElement;
StructureElement rootElement = taggedContent.RootElement;
```
## 자식 요소 접근하기

태그가 지정된 PDF 문서의 자식 요소에 접근하기 위해 Aspose.PDF는 [ElementList](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/elementlist) 클래스를 제공합니다. 다음 코드 스니펫은 태그가 지정된 PDF 문서의 자식 요소에 접근하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인할 수 있습니다.
// 문서 디렉토리 경로
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Pdf 문서 열기
Document document = new Document(dataDir + "StructureElementsTree.pdf");

// 태그가 지정된 Pdf 작업을 위한 내용 가져오기
ITaggedContent taggedContent = document.TaggedContent;

// 루트 요소(들)에 접근
ElementList elementList = taggedContent.StructTreeRootElement.ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // 속성 가져오기
        string title = structureElement.Title;
        string language = structureElement.Language;
        string actualText = structureElement.ActualText;
        string expansionText = structureElement.ExpansionText;
        string alternativeText = structureElement.AlternativeText;
    }
}

// 루트 요소의 첫 번째 요소의 자식 요소에 접근
elementList = taggedContent.RootElement.ChildElements[1].ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // 속성 설정
        structureElement.Title = "title";
        structureElement.Language = "fr-FR";
        structureElement.ActualText = "actual text";
        structureElement.ExpansionText = "exp";
        structureElement.AlternativeText = "alt";
    }
}

// 태그가 지정된 Pdf 문서 저장
document.Save(dataDir + "AccessChildElements.pdf");
```
## 기존 PDF에서 이미지 태깅

기존 PDF 문서에서 이미지를 태그하기 위해, Aspose.PDF는 [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement) 클래스의 [FindElements](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/findelements/_1) 메소드를 제공합니다. [FigureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/figureelement) 클래스의 [AlternativeText](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext) 속성을 사용하여 그림에 대한 대체 텍스트를 추가할 수 있습니다.

다음 코드 스니펫은 기존 PDF 문서에서 이미지를 태그하는 방법을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inFile = dataDir + "TH.pdf";
string outFile = dataDir + "TH_out.pdf";
string logFile = dataDir + "TH_out.xml";

// 문서 열기
Document document = new Document(inFile);

// 태그된 내용과 루트 구조 요소 가져오기
ITaggedContent taggedContent = document.TaggedContent;
StructureElement rootElement = taggedContent.RootElement;

// 태그된 pdf 문서의 제목 설정
taggedContent.SetTitle("이미지가 포함된 문서");

foreach (FigureElement figureElement in rootElement.FindElements<FigureElement>(true))
{
    // 그림에 대한 대체 텍스트 설정
    figureElement.AlternativeText = "그림 대체 텍스트 (기법 2)";


    // BBox 속성 생성 및 설정
    StructureAttribute bboxAttribute = new StructureAttribute(AttributeKey.BBox);
    bboxAttribute.SetRectangleValue(new Rectangle(0.0, 0.0, 100.0, 100.0));

    StructureAttributes figureLayoutAttributes = figureElement.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
    figureLayoutAttributes.SetAttribute(bboxAttribute);
}

// Span 요소를 Paragraph로 이동 (첫 번째 TD에서 잘못된 span 및 paragraph 찾기)
TableElement tableElement = rootElement.FindElements<TableElement>(true)[0];
SpanElement spanElement = tableElement.FindElements<SpanElement>(true)[0];
TableTDElement firstTdElement = tableElement.FindElements<TableTDElement>(true)[0];
ParagraphElement paragraph = firstTdElement.FindElements<ParagraphElement>(true)[0];

// Span 요소를 Paragraph로 이동
spanElement.ChangeParentElement(paragraph);


// 문서 저장
document.Save(outFile);



// 외부 문서의 PDF/UA 준수 확인
document = new Document(outFile);

bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("PDF/UA 준수 여부: {0}", isPdfUaCompliance));
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET 라이브러리",
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


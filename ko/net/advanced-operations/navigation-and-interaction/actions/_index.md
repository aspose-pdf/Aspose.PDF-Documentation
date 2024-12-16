---
title: PDF에서 작업 다루기
linktitle: Actions
type: docs
weight: 20
url: /ko/net/actions/
description: 이 섹션에서는 C#을 사용하여 문서와 폼 필드에 프로그래밍 방식으로 작업을 추가하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 작업 다루기",
    "alternativeHeadline": "PDF에 작업 추가 방법",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf에서의 작업",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션에서는 C#을 사용하여 문서와 폼 필드에 프로그래밍 방식으로 작업을 추가하는 방법을 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 파일에 하이퍼링크 추가

PDF 파일에 하이퍼링크를 추가할 수 있으며, 독자가 PDF의 다른 부분으로 이동하거나 외부 콘텐츠로 이동할 수 있습니다.

PDF 문서에 웹 하이퍼링크를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. 링크를 추가하고 싶은 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스를 가져옵니다.
1. Page와 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) 객체를 사용하여 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 생성합니다. Rectangle 객체는 링크를 추가할 페이지 상의 위치를 지정하는 데 사용됩니다.
1. Action 속성을 원격 URI의 위치를 지정하는 [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) 객체로 설정합니다.
1. 자유 텍스트 추가하기:

- [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 객체를 인스턴스화합니다. Page 및 Rectangle 객체를 인수로 받아들이므로 LinkAnnotation 생성자에 지정된 값과 동일한 값을 제공할 수 있습니다.
- [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 객체의 Contents 속성을 사용하여 출력 PDF에 표시되어야 할 문자열을 지정합니다.
- 선택적으로, [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 및 FreeTextAnnotation 객체의 테두리 너비를 0으로 설정하여 PDF 문서에 표시되지 않도록 할 수 있습니다.
- [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 및 [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 객체가 정의되면 이 링크들을 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 Annotations 컬렉션에 추가합니다.
- [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 및 [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 객체를 정의한 후, 이 링크들을 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 Annotations 컬렉션에 추가하세요.
- 마지막으로, [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메소드를 사용하여 업데이트된 PDF를 저장하세요.

다음 코드 스니펫은 PDF 파일에 하이퍼링크를 추가하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 다음을 참조하세요 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// 문서 열기
Document document = new Document(dataDir + "AddHyperlink.pdf");
// 링크 생성
Page page = document.Pages[1];
// Link annotation 객체 생성
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
// LinkAnnotation의 border 객체 생성
Border border = new Border(link);
// border 너비를 0으로 설정
border.Width = 0;
// LinkAnnotation의 border 설정
link.Border = border;
// 링크 타입을 원격 URI로 지정
link.Action = new GoToURIAction("www.aspose.com");
// 링크 annotation을 PDF 파일 첫 페이지의 annotations 컬렉션에 추가
page.Annotations.Add(link);

// Free Text annotation 생성
FreeTextAnnotation textAnnotation = new FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
// Free text로 추가될 문자열
textAnnotation.Contents = "Link to Aspose website";
// Free Text Annotation의 border 설정
textAnnotation.Border = border;
// FreeText annotation을 문서 첫 페이지의 annotations 컬렉션에 추가
document.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddHyperlink_out.pdf";
// 업데이트된 문서 저장
document.Save(dataDir);
```
## PDF 내 같은 페이지로 하이퍼링크 만들기

Aspose.PDF for .NET은 PDF 생성과 조작을 위한 훌륭한 기능을 제공합니다. 이 기능 중에는 PDF 페이지에 링크를 추가하는 기능도 포함되어 있으며, 링크는 다른 PDF 파일의 페이지, 웹 URL, 애플리케이션을 실행하는 링크 또는 동일한 PDF 파일 내 페이지로 연결될 수 있습니다. 동일한 PDF 파일의 페이지로의 로컬 하이퍼링크를 추가하기 위해, Aspose.PDF 네임스페이스에 [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink) 클래스가 추가되었으며, 이 클래스는 하이퍼링크의 대상/목적지 페이지를 지정하는 데 사용되는 TargetPageNumber라는 속성을 가지고 있습니다.

로컬 하이퍼링크를 추가하려면, 링크가 연결될 TextFragment를 생성해야 합니다. [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) 클래스는 LocalHyperlink 인스턴스와 연결되는 Hyperlink라는 속성을 가지고 있습니다. 다음 코드 조각은 이 요구 사항을 달성하기 위한 단계를 보여줍니다.

```csharp
// PDF 문서 생성
Document pdfDocument = new Document();
// 페이지 추가
Page page = pdfDocument.Pages.Add();
// 텍스트 조각 생성
TextFragment textFragment = new TextFragment("이 페이지로 이동");
// 로컬 하이퍼링크 생성
LocalHyperlink localHyperlink = new LocalHyperlink();
// 대상 페이지 번호 지정
localHyperlink.TargetPageNumber = 2;
// 텍스트 조각에 하이퍼링크 연결
textFragment.Hyperlink = localHyperlink;
// 페이지에 텍스트 조각 추가
page.Paragraphs.Add(textFragment);
// PDF 파일 저장
pdfDocument.Save("output.pdf");
```
```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// 문서 인스턴스 생성
Document doc = new Document();
// PDF 파일의 페이지 컬렉션에 페이지 추가
Page page = doc.Pages.Add();
// 텍스트 프래그먼트 인스턴스 생성
Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment("7번 페이지로 링크하는 페이지 번호 테스트");
// 로컬 하이퍼링크 인스턴스 생성
Aspose.Pdf.LocalHyperlink link = new Aspose.Pdf.LocalHyperlink();
// 링크 인스턴스에 대상 페이지 설정
link.TargetPageNumber = 7;
// 텍스트프래그먼트에 하이퍼링크 설정
text.Hyperlink = link;
// 페이지의 문단 컬렉션에 텍스트 추가
page.Paragraphs.Add(text);
// 새 텍스트프래그먼트 인스턴스 생성
text = new TextFragment("1번 페이지로 링크하는 페이지 번호 테스트");
// 텍스트프래그먼트는 새 페이지에 추가되어야 함
text.IsInNewPage = true;
// 또 다른 로컬 하이퍼링크 인스턴스 생성
link = new LocalHyperlink();
// 두 번째 하이퍼링크에 대상 페이지 설정
link.TargetPageNumber = 1;
// 두 번째 텍스트프래그먼트에 링크 설정
text.Hyperlink = link;
// 페이지 객체의 문단 컬렉션에 텍스트 추가
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateLocalHyperlink_out.pdf";
// 업데이트된 문서 저장
doc.Save(dataDir);
```
## PDF 하이퍼링크 목적지(URL) 얻기

링크는 PDF 파일에서 주석으로 표현되며 추가, 업데이트 또는 삭제가 가능합니다. Aspose.PDF for .NET은 또한 PDF 파일에서 하이퍼링크의 목적지(URL)를 얻는 것을 지원합니다.

링크의 URL을 얻으려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성합니다.
1. 링크를 추출하고 싶은 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 가져옵니다.
1. [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) 클래스를 사용하여 지정된 페이지에서 모든 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 객체를 추출합니다.
1. [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) 객체를 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 Accept 메서드에 전달합니다.
1.
1.
1. 마지막으로, LinkAnnotation Action을 GoToURIAction으로 추출하세요.

다음 코드 스니펫은 PDF 파일에서 하이퍼링크 목적지(URL)를 얻는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일을 보려면, https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 방문하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// PDF 파일 로드
Document document = new Document(dataDir + "input.pdf");

// PDF의 모든 페이지를 순회
foreach (Aspose.Pdf.Page page in document.Pages)
{
    // 특정 페이지에서 링크 주석 가져오기
    AnnotationSelector selector = new AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

    page.Accept(selector);
    // 모든 링크를 보유하는 리스트 생성
    IList<Annotation> list = selector.Selected;
    // 리스트 내 각각의 아이템을 순회
    foreach (LinkAnnotation a in list)
    {
        // 목적지 URL 출력
        Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
    }
}
```
## 하이퍼링크 텍스트 가져오기

하이퍼링크는 문서에 표시되는 텍스트와 목적지 URL의 두 부분으로 구성됩니다. 경우에 따라서는 URL보다 텍스트가 필요할 수 있습니다.

PDF 파일의 텍스트와 주석/동작은 다른 엔티티에 의해 표현됩니다. 페이지의 텍스트는 단어와 문자의 집합일 뿐이며, 주석은 하이퍼링크에서 볼 수 있는 상호작용과 같은 일부 상호작용을 제공합니다.

URL 내용을 찾으려면 주석과 텍스트 모두를 다뤄야 합니다. [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) 객체는 텍스트를 가지고 있지 않지만 페이지의 텍스트 아래에 위치합니다. 따라서 텍스트를 얻으려면 Annotation이 URL의 경계를 제공하고 Text 객체가 URL 내용을 제공합니다. 다음 코드 스니펫을 참조하세요.

```csharp
  {
        public static void Run()
        {
            try
            {
                // ExStart:GetHyperlinkText
                // 문서 디렉토리 경로.
                string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
                // PDF 파일 로드
                Document document = new Document(dataDir + "input.pdf");
                // PDF의 각 페이지를 반복
                foreach (Page page in document.Pages)
                {
                    // 링크 주석 표시
                    ShowLinkAnnotations(page);
                }
                // ExEnd:GetHyperlinkText
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // ExStart:ShowLinkAnnotations
        public static void ShowLinkAnnotations(Page page)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annot in page.Annotations)
            {
                if (annot is LinkAnnotation)
                {
                    // 각 링크 주석의 URL 출력
                    Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
                    TextAbsorber absorber = new TextAbsorber();
                    absorber.TextSearchOptions.LimitToPageBounds = true;
                    absorber.TextSearchOptions.Rectangle = annot.Rect;
                    page.Accept(absorber);
                    string extractedText = absorber.Text;
                    // 하이퍼링크와 관련된 텍스트 출력
                    Console.WriteLine(extractedText);
                }

            }
        }
        // ExEnd:ShowLinkAnnotations
    }
}
```
## PDF 파일에서 문서 열기 동작 제거

[문서를 볼 때 PDF 페이지 지정하는 방법](#how-to-specify-pdf-page-when-viewing-document)에서는 문서를 첫 번째 페이지가 아닌 다른 페이지에서 열도록 설정하는 방법에 대해 설명했습니다. 여러 문서를 연결할 때 하나 이상의 문서에 GoTo 동작이 설정된 경우, 이를 제거하고 싶을 수 있습니다. 예를 들어, 두 문서를 결합하고 두 번째 문서에 두 번째 페이지로 이동하는 GoTo 동작이 있는 경우, 출력 문서는 결합된 문서의 첫 페이지가 아닌 두 번째 문서의 두 번째 페이지에서 열립니다. 이러한 동작을 방지하기 위해 열기 동작 명령을 제거합니다.

열기 동작을 제거하는 방법:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) 속성을 null로 설정하세요.
1. Document 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메소드를 사용하여 업데이트된 PDF를 저장하세요.

다음 코드 스니펫은 PDF 파일에서 문서 열기 동작을 제거하는 방법을 보여줍니다.

다음 코드 스니펫은 PDF 파일에서 문서 열기 작업을 제거하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// 문서 열기
Document document = new Document(dataDir + "RemoveOpenAction.pdf");
// 문서 열기 작업 제거
document.OpenAction = null;
dataDir = dataDir + "RemoveOpenAction_out.pdf";
// 업데이트된 문서 저장
document.Save(dataDir);
```

## 문서를 볼 때 PDF 페이지 지정 방법 {#how-to-specify-pdf-page-when-viewing-document}

Adobe Reader와 같은 PDF 뷰어에서 PDF 파일을 볼 때, 파일은 보통 첫 페이지에서 열립니다. 그러나, 다른 페이지에서 파일을 열도록 설정할 수 있습니다.

[XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) 클래스를 사용하면 열고 싶은 PDF 파일의 페이지를 지정할 수 있습니다.
[XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) 클래스는 PDF 파일에서 열고자 하는 페이지를 지정할 수 있습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// PDF 파일을 로드합니다.
Document doc = new Document(dataDir + "SpecifyPageWhenViewing.pdf");
// 문서의 두 번째 페이지 인스턴스를 가져옵니다.
Page page2 = doc.Pages[2];
// 대상 페이지의 확대/축소 인자를 설정하는 변수를 생성합니다.
double zoom = 1;
// GoToAction 인스턴스를 생성합니다.
GoToAction action = new GoToAction(doc.Pages[2]);
// 2 페이지로 이동합니다.
action.Destination = new XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
// 문서 오픈 액션을 설정합니다.
doc.OpenAction = action;
// 업데이트된 문서를 저장합니다.
doc.Save(dataDir + "goto2page_out.pdf");
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
    "applicationCategory": "PDF Manipulation Library for .NET",
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



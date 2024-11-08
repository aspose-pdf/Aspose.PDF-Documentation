---
title: C#를 사용하여 PDF 문서 포맷하기
linktitle: PDF 문서 포맷하기
type: docs
weight: 11
url: /ko/net/formatting-pdf-document/
description: Aspose.PDF for .NET을 사용하여 PDF 문서를 생성하고 포맷하세요. 다음 코드 스니펫을 사용하여 작업을 해결하세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#를 사용하여 PDF 문서 포맷하기",
    "alternativeHeadline": ".NET에서 PDF 문서를 포맷하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, dotnet, pdf 문서 포맷",
    "wordcount": "302",
    "proficiencyLevel":"초심자",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 사용하여 PDF 문서를 생성하고 포맷하세요. 다음 코드 스니펫을 사용하여 작업을 해결하세요."
}
</script>
## PDF 문서 형식

### 문서 창 및 페이지 디스플레이 속성 가져오기

이 주제는 문서 창, 뷰어 애플리케이션의 속성을 얻는 방법과 페이지가 어떻게 표시되는지를 이해하는 데 도움이 됩니다. 이러한 속성을 설정하려면:

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 PDF 파일을 엽니다. 이제 Document 객체의 속성을 설정할 수 있습니다.

- CenterWindow – 화면에 문서 창을 중앙에 배치합니다. 기본값: false.
- Direction – 읽기 순서입니다. 이것은 페이지가 나란히 표시될 때의 레이아웃을 결정합니다. 기본값: 왼쪽에서 오른쪽으로.
- DisplayDocTitle – 문서 창 제목 표시줄에 문서 제목을 표시합니다. 기본값: false (제목이 표시됩니다).
- HideMenuBar – 문서 창의 메뉴 바를 숨기거나 표시합니다. 기본값: false (메뉴 바가 표시됩니다).
- HideToolBar – 문서 창의 툴바를 숨기거나 표시합니다. 기본값: false (툴바가 표시됩니다).
- HideWindowUI – 스크롤 바와 같은 문서 창 요소를 숨기거나 표시합니다.
- HideWindowUI – 문서 창 요소(예: 스크롤 바)를 숨기거나 표시합니다.
- NonFullScreenPageMode – 문서가 전체 페이지 모드로 표시되지 않을 때의 모드입니다.
- PageLayout – 페이지 레이아웃입니다.
- PageMode – 문서가 처음 열릴 때 어떻게 표시되는지에 대한 옵션은 썸네일 표시, 전체 화면, 첨부 파일 패널 표시입니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 속성을 가져오는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "GetDocumentWindow.pdf");

// 다양한 문서 속성 가져오기
// 문서 창의 위치 - 기본값: false
Console.WriteLine("CenterWindow : {0}", pdfDocument.CenterWindow);
  
// 페이지의 우선 읽기 순서; 페이지가 나란히 표시될 때의 위치 결정 - 기본값: L2R
Console.WriteLine("Direction : {0}", pdfDocument.Direction);

// 창 제목 표시줄이 문서 제목을 표시할지 여부
// false인 경우, 제목 표시줄은 PDF 파일 이름을 표시 - 기본값: false
Console.WriteLine("DisplayDocTitle : {0}", pdfDocument.DisplayDocTitle);

// 문서 창의 크기를 첫 페이지의 크기에 맞게 조정할지 여부 - 기본값: false
Console.WriteLine("FitWindow : {0}", pdfDocument.FitWindow);

// 뷰어 애플리케이션의 메뉴 바를 숨길지 여부 - 기본값: false
Console.WriteLine("HideMenuBar : {0}", pdfDocument.HideMenubar);

// 뷰어 애플리케이션의 도구 모음을 숨길지 여부 - 기본값: false
Console.WriteLine("HideToolBar : {0}", pdfDocument.HideToolBar);

// 스크롤 바와 같은 UI 요소를 숨기고 페이지 콘텐츠만 표시할지 여부 - 기본값: false
Console.WriteLine("HideWindowUI : {0}", pdfDocument.HideWindowUI);

// 전체 화면 모드를 종료할 때 문서의 페이지 모드입니다.
Console.WriteLine("NonFullScreenPageMode : {0}", pdfDocument.NonFullScreenPageMode);

// 페이지 레이아웃, 예: 단일 페이지, 한 열
Console.WriteLine("PageLayout : {0}", pdfDocument.PageLayout);

// 문서가 열릴 때의 표시 방법
// 예: 썸네일 표시, 전체 화면, 첨부 파일 패널 표시
Console.WriteLine("pageMode : {0}", pdfDocument.PageMode);
```
### 문서 창 및 페이지 디스플레이 속성 설정

이 주제는 문서 창, 뷰어 애플리케이션 및 페이지 디스플레이의 속성을 설정하는 방법에 대해 설명합니다. 이러한 다양한 속성을 설정하려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 PDF 파일을 엽니다.
1. Document 객체의 속성을 설정합니다.
1. Save 메소드를 사용하여 업데이트된 PDF 파일을 저장합니다.

사용 가능한 속성은 다음과 같습니다:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

각각은 아래 코드에서 사용되고 설명됩니다. 다음 코드 조각은 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 속성을 설정하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요
// 문서 디렉토리의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SetDocumentWindow.pdf");

// 다양한 문서 속성 설정
// 문서 창의 위치 지정 - 기본값: false
pdfDocument.CenterWindow = true;

// 페이지의 우선 읽기 순서; 페이지가 나란히 표시될 때의 위치 결정 - 기본값: L2R
pdfDocument.Direction = Direction.R2L;

// 창 제목 표시줄이 문서 제목을 표시해야 하는지 여부
// false인 경우, 제목 표시줄은 PDF 파일 이름을 표시 - 기본값: false
pdfDocument.DisplayDocTitle = true;

// 문서 창의 크기를
// 첫 페이지 표시 크기에 맞게 조정해야 하는지 여부 - 기본값: false
pdfDocument.FitWindow = true;

// 뷰어 애플리케이션의 메뉴 바 숨기기 - 기본값: false
pdfDocument.HideMenubar = true;

// 뷰어 애플리케이션의 도구 모음 숨기기 - 기본값: false
pdfDocument.HideToolBar = true;

// 스크롤 바와 같은 UI 요소를 숨기고
// 페이지 내용만 표시되도록 지정 - 기본값: false
pdfDocument.HideWindowUI = true;

// 문서의 페이지 모드. 전체 화면 모드를 종료할 때 문서 표시 방식 지정.
pdfDocument.NonFullScreenPageMode = PageMode.UseOC;

// 페이지 레이아웃 지정, 즉 단일 페이지, 한 열
pdfDocument.PageLayout = PageLayout.TwoColumnLeft;

// 문서를 열 때 표시 방식 지정
// 즉, 썸네일 표시, 전체 화면, 첨부 파일 패널 표시
pdfDocument.PageMode = PageMode.UseThumbs;

dataDir = dataDir + "SetDocumentWindow_out.pdf";
// 업데이트된 PDF 파일 저장
pdfDocument.Save(dataDir);
```
### 기존 PDF 파일에 폰트 삽입하기

PDF 리더는 문서가 표시되는 플랫폼에 관계없이 동일한 방식으로 문서를 표시할 수 있도록 [14개의 기본 폰트](https://en.wikipedia.org/wiki/PDF#Text)를 지원합니다. PDF에 14개의 기본 폰트에 속하지 않는 폰트가 포함되어 있는 경우, 폰트 치환을 피하기 위해 폰트를 PDF 파일에 삽입하세요.

Aspose.PDF for .NET은 기존 PDF 파일에 폰트를 삽입하는 것을 지원합니다. 전체 폰트 또는 폰트의 부분집합을 삽입할 수 있습니다. 폰트를 삽입하려면 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 PDF 파일을 열고, [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) 클래스를 사용하여 PDF 파일에 폰트를 삽입하세요. 전체 폰트를 사용하려면 Font 클래스의 IsEmbeded 속성을 사용하고, 폰트의 부분집합을 사용하려면 IsSubset 속성을 사용하세요.

{{% alert color="primary" %}}

폰트 부분집합은 사용된 문자만을 삽입하고, 폰트가 로고용으로 사용되지만 본문 텍스트에는 사용되지 않는 경우와 같이 짧은 문장이나 슬로건에 사용될 때 유용합니다.
글꼴 서브셋은 사용되는 문자만 포함하고, 예를 들어 기업 글꼴이 로고에 사용되지만 본문 텍스트에는 사용되지 않는 경우와 같이 짧은 문장이나 슬로건에 사용될 때 유용합니다.

다음 코드 조각은 PDF 파일에 글꼴을 포함하는 방법을 보여줍니다.
{{% /alert %}}

### 표준 타입 1 글꼴 포함

일부 PDF 문서에는 특별한 Adobe 글꼴 세트에서 가져온 글꼴이 있습니다. 이 세트의 글꼴은 "표준 타입 1 글꼴"이라고 불립니다. 이 세트에는 14개의 글꼴이 포함되어 있으며, 이 유형의 글꼴을 포함하려면 특별한 플래그를 사용해야 합니다. 예를 들어 [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts)를 사용하면 됩니다. 다음은 표준 타입 1 글꼴을 포함한 모든 글꼴이 포함된 문서를 얻기 위해 사용할 수 있는 코드 조각입니다:

```csharp
// 전체 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 기존 PDF 문서 로드
Document pdfDocument = new Document(dataDir + "input.pdf");
// 문서의 EmbedStandardFonts 속성 설정
pdfDocument.EmbedStandardFonts = true;
foreach (Aspose.Pdf.Page page in pdfDocument.Pages)
{
    if (page.Resources.Fonts != null)
    {
        foreach (Aspose.Pdf.Text.Font pageFont in page.Resources.Fonts)
        {
// 글꼴이 이미 포함되어 있는지 확인
if (!pageFont.IsEmbedded)
{
    pageFont.IsEmbedded = true;
}
        }
    }
}
pdfDocument.Save(dataDir + "EmbeddedFonts-updated_out.pdf");
```
### PDF 생성 시 폰트 임베딩하기

Adobe Reader에서 지원하는 14개의 기본 폰트 이외의 폰트를 사용해야 하는 경우, PDF 파일을 생성할 때 폰트 설명을 임베딩해야 합니다. 폰트 정보가 임베딩되지 않은 경우, Adobe Reader는 운영 체제에 설치된 폰트를 사용하거나 PDF의 폰트 설명자에 따라 대체 폰트를 생성합니다.

>임베딩된 폰트는 호스트 기계에 설치되어 있어야 합니다. 예를 들어 다음 코드에서는 ‘Univers Condensed’ 폰트가 시스템에 설치되어 있습니다.

PDF 파일에 폰트 정보를 임베딩하기 위해 Font 클래스의 IsEmbedded 속성을 사용합니다. 이 속성의 값을 'True'로 설정하면 PDF에 폰트 파일 전체가 임베딩되어 PDF 파일 크기가 증가한다는 사실을 알아야 합니다. 다음은 PDF에 폰트 정보를 임베딩하는 데 사용할 수 있는 코드 스니펫입니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 비어 있는 생성자를 호출하여 Pdf 객체를 인스턴스화합니다.
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();

// Pdf 객체에 섹션을 생성합니다.
Aspose.Pdf.Page page = doc.Pages.Add();

Aspose.Pdf.Text.TextFragment fragment = new Aspose.Pdf.Text.TextFragment("");

Aspose.Pdf.Text.TextSegment segment = new Aspose.Pdf.Text.TextSegment(" 이것은 사용자 정의 폰트를 사용하는 샘플 텍스트입니다.");
Aspose.Pdf.Text.TextState ts = new Aspose.Pdf.Text.TextState();
ts.Font = FontRepository.FindFont("Arial");
ts.Font.IsEmbedded = true;
segment.TextState = ts;
fragment.Segments.Add(segment);
page.Paragraphs.Add(fragment);

dataDir = dataDir + "EmbedFontWhileDocCreation_out.pdf";
// PDF 문서를 저장합니다.
doc.Save(dataDir);
```
### PDF 저장 시 기본 글꼴 이름 설정

PDF 문서에 문서 자체나 장치에 없는 글꼴이 포함되어 있을 때, API는 이러한 글꼴을 기본 글꼴로 대체합니다. 글꼴이 사용 가능할 경우(장치에 설치되었거나 문서에 포함되어 있을 경우), 출력 PDF는 같은 글꼴을 가져야 합니다(기본 글꼴로 대체되어서는 안 됩니다). 기본 글꼴의 값은 글꼴 파일 경로가 아닌 글꼴 이름을 포함해야 합니다. 문서를 PDF로 저장할 때 기본 글꼴 이름을 설정하는 기능을 구현했습니다. 다음 코드 스니펫을 사용하여 기본 글꼴을 설정할 수 있습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// 누락된 글꼴이 있는 기존 PDF 문서를 로드합니다.
string documentName = dataDir + "input.pdf";
string newName = "Arial";
using (System.IO.FileStream fs = new System.IO.FileStream(documentName, System.IO.FileMode.Open))
using (Document document = new Document(fs))
{
    PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();
    // 기본 글꼴 이름 지정
    pdfSaveOptions.DefaultFontName = newName;
    document.Save(dataDir + "output_out.pdf", pdfSaveOptions);
}
```
### PDF 문서에서 모든 글꼴 가져오기

PDF 문서에서 모든 글꼴을 가져오고 싶다면 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스에서 제공하는 FontUtilities.GetAllFonts() 메소드를 사용할 수 있습니다. 기존 PDF 문서에서 모든 글꼴을 가져오는 방법은 다음 코드 스니펫을 확인하세요:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인할 수 있습니다.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

### 글꼴 대체에 대한 경고 받기

Aspose.PDF for .NET은 글꼴 대체 사례를 처리하기 위해 글꼴 대체에 대한 알림을 받는 메소드를 제공합니다. 아래 코드 스니펫은 해당 기능을 사용하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인할 수 있습니다.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

Document doc = new Document(dataDir + "input.pdf");

doc.FontSubstitution += new Document.FontSubstitutionHandler(OnFontSubstitution);
```
**OnFontSubstitution** 메소드는 아래와 같습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하십시오.
Console.WriteLine(string.Format("글꼴 '{0}'이(가) 다른 글꼴 '{1}'로 대체되었습니다.",
oldFont.FontName, newFont.FontName));
```

### 폰트 임베딩 개선을 위한 FontSubsetStrategy 사용하기

폰트를 부분 집합으로 임베딩하는 기능은 IsSubset 속성을 사용하여 달성할 수 있지만, 때로는 문서에서 사용된 부분 집합만으로 전체 임베딩된 폰트 세트를 줄이고 싶을 수 있습니다. Aspose.Pdf.Document에는 FontUtilities라는 속성이 포함되어 있으며, 이는 SubsetFonts(FontSubsetStrategy subsetStrategy) 메소드를 포함합니다. SubsetFonts() 메소드에서 subsetStrategy 매개변수는 부분 집합 전략을 조정하는 데 도움이 됩니다. FontSubsetStrategy는 폰트 부분 집합에 대한 다음 두 가지 변형을 지원합니다.

- SubsetAllFonts - 문서에서 사용된 모든 글꼴을 부분 집합화합니다.
- SubsetEmbeddedFontsOnly - 문서에 완전히 임베딩된 글꼴만 부분 집합화합니다.

다음 코드 스니펫은 FontSubsetStrategy를 설정하는 방법을 보여줍니다.
다음 코드 스니펫은 FontSubsetStrategy를 설정하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
// SubsetAllFonts의 경우 모든 글꼴이 문서에 부분적으로 포함됩니다.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetAllFonts);
// 완전히 포함된 글꼴에 대해서는 부분적으로 포함되지만 문서에 포함되지 않은 글꼴은 영향을 받지 않습니다.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
doc.Save(dataDir + "Output_out.pdf");
```

### PDF 파일의 확대/축소 비율 가져오기 및 설정하기

PDF 문서의 현재 확대/축소 비율이 무엇인지 결정하고 싶을 때가 있습니다. Aspose.Pdf를 사용하면 현재 값을 찾고 설정할 수 있습니다.

[GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) 클래스의 Destination 속성을 사용하면 PDF 파일과 관련된 확대 값을 가져올 수 있습니다.
[GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) 클래스의 Destination 속성을 사용하면 PDF 파일과 관련된 확대/축소 값을 가져올 수 있습니다.

#### 확대/축소 비율 설정

다음 코드 스니펫은 PDF 파일의 확대/축소 비율을 설정하는 방법을 보여줍니다.

```csharp
// 완전한 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 새로운 Document 객체를 생성합니다.
Document doc = new Document(dataDir + "SetZoomFactor.pdf");

GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0, 0, .5));
doc.OpenAction = action;
dataDir = dataDir + "Zoomed_pdf_out.pdf";
// 문서를 저장합니다.
doc.Save(dataDir);
```

#### 확대/축소 비율 가져오기

다음 코드 스니펫은 PDF 파일의 확대/축소 비율을 가져오는 방법을 보여줍니다.

```csharp
// 완전한 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 새로운 Document 객체를 생성합니다.
Document doc = new Document(dataDir + "Zoomed_pdf.pdf");

// GoToAction 객체를 생성합니다.
GoToAction action = doc.OpenAction as GoToAction;

// PDF 파일의 확대/축소 비율을 가져옵니다.
System.Console.WriteLine((action.Destination as XYZExplicitDestination).Zoom); // 문서의 확대/축소 값;
```
### 인쇄 대화 상자 프리셋 속성 설정

Aspoose.PDF는 PDF 문서의 인쇄 대화 상자 프리셋 속성을 설정할 수 있습니다. 기본값으로 설정된 Simplex 모드를 DuplexMode 속성으로 변경할 수 있습니다. 아래에 표시된 두 가지 방법을 사용하여 이를 달성할 수 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

using (Document doc = new Document())
{
    doc.Pages.Add();
    doc.Duplex = PrintDuplex.DuplexFlipLongEdge;
    doc.Save(dataDir + "35297_out.pdf", SaveFormat.Pdf);
}
```

### PDF 콘텐츠 편집기를 사용한 인쇄 대화 상자 프리셋 속성 설정

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

string outputFile = dataDir + "input.pdf";
using (PdfContentEditor ed = new PdfContentEditor())
{
    ed.BindPdf(outputFile);
    if ((ed.GetViewerPreference() & ViewerPreference.DuplexFlipShortEdge) > 0)
    {
        Console.WriteLine("파일은 양면 짧은 가장자리를 뒤집습니다.");
    }

    ed.ChangeViewerPreference(ViewerPreference.DuplexFlipShortEdge);
    ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
}
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
                "areaServed": "AU",
                "availableLanguage": "영어"
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


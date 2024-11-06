---
title: PDF 문서 조작하기 in C#
linktitle: PDF 문서 조작하기
type: docs
weight: 20
url: ko/net/manipulate-pdf-document/
description: 이 글은 PDF A 표준에 대한 PDF 문서를 검증하는 방법, 목차(TOC) 작업 방법, PDF 만료 날짜 설정 방법 등에 대한 정보를 담고 있습니다.
keywords: "manipulate pdf c#"
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 문서 조작하기",
    "alternativeHeadline": "PDF 파일 조작 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, dotnet, manipulate pdf file",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "이 글은 PDF A 표준에 대한 PDF 문서를 검증하는 방법, 목차(TOC) 작업 방법, PDF 만료 날짜 설정 방법 등에 대한 정보를 담고 있습니다."
}
</script>

## **PDF 문서 조작 in C#**

## PDF 문서를 PDF A 표준 (A 1A 및 A 1B)에 맞게 검증

PDF/A-1a 또는 PDF/A-1b 호환성을 검증하려면 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 Validate 메서드를 사용하세요. 이 메서드는 결과를 저장할 파일의 이름과 필요한 검증 유형 [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat) 열거형을 지정할 수 있습니다: PDF_A_1A 또는 PDF_A_1B.

{{% alert color="primary" %}}

출력 XML 형식은 Aspose의 사용자 정의 형식입니다. XML에는 문제의 이름을 가진 태그 컬렉션이 포함되어 있으며, 각 태그는 특정 문제의 세부 정보를 포함합니다. 문제 태그의 ObjectID 속성은 이 문제와 관련된 특정 객체의 ID를 나타냅니다. Clause 속성은 PDF 사양의 해당 규칙을 나타냅니다.

{{% /alert %}}

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

다음 코드 스니펫은 PDF 문서를 PDF/A-1A로 검증하는 방법을 보여줍니다.
다음 코드 조각은 PDF 문서를 PDF/A-1A로 검증하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// PDF/A-1a를 위한 PDF 검증
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);
```

다음 코드 조각은 PDF 문서를 PDF/A-1B로 검증하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// PDF/A-1b를 위한 PDF 검증
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```
{{% alert color="primary" %}}

Aspose.PDF for .NET은 로드된 문서가 유효한 PDF인지, 또는 [암호화되었는지 여부](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/)를 확인하는 데 사용할 수 있습니다. Document 클래스의 기능을 더 확장하기 위해 입력 파일이 PDF/A 준수 여부를 결정하는 *IsPdfaCompliant* 속성과 PDF/A 형식을 식별하는 *PdfaFormat* 속성이 도입되었습니다.

{{% /alert %}}

## 목차 작업

### 기존 PDF에 목차 추가

Aspose.PDF API를 사용하면 PDF를 생성할 때 또는 기존 파일에 목차를 추가할 수 있습니다. Aspose.Pdf.Generator 네임스페이스의 ListSection 클래스를 사용하여 처음부터 PDF를 생성할 때 목차를 만들 수 있습니다. TOC의 요소인 제목을 추가하려면 Aspose.Pdf.Generator.Heading 클래스를 사용하세요.

기존 PDF 파일에 TOC를 추가하려면 Aspose.Pdf 네임스페이스의 Heading 클래스를 사용하세요.
기존 PDF 파일에 목차를 추가하려면 Aspose.Pdf 네임스페이스의 Heading 클래스를 사용하세요.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 기존 PDF 파일을 로드합니다.
Document doc = new Document(dataDir + "AddTOC.pdf");

// PDF 파일의 첫 페이지에 접근합니다.
Page tocPage = doc.Pages.Insert(1);

// TOC 정보를 나타내는 객체를 생성합니다.
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("목차");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;

// TOC의 제목을 설정합니다.
tocInfo.Title = title;
tocPage.TocInfo = tocInfo;

// TOC 요소로 사용될 문자열 객체를 생성합니다.
string[] titles = new string[4];
titles[0] = "첫 페이지";
titles[1] = "두 번째 페이지";
titles[2] = "세 번째 페이지";
titles[3] = "네 번째 페이지";
for (int i = 0; i < 2; i++)
{
    // Heading 객체를 생성합니다.
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);

    // heading 객체의 목적지 페이지를 지정합니다.
    heading2.DestinationPage = doc.Pages[i + 2];

    // 목적지 페이지
    heading2.Top = doc.Pages[i + 2].Rect.Height;

    // 목적지 좌표
    segment2.Text = titles[i];

    // TOC를 포함하는 페이지에 heading을 추가합니다.
    tocPage.Paragraphs.Add(heading2);
}
dataDir = dataDir + "TOC_out.pdf";
// 문서를 업데이트하여 저장합니다.
doc.Save(dataDir);
```
### 다른 TOC 레벨에 대해 다른 TabLeaderType 설정하기

Aspose.PDF는 다른 TOC 레벨에 대해 다양한 TabLeaderType을 설정할 수 있도록 합니다. 다음과 같이 FormatArray의 LineDash 속성에 TabLeaderType 열거형의 적절한 값을 설정해야 합니다.

```csharp
 string outFile = "TOC.pdf";

Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();

//LeaderType 설정
tocInfo.LineDash = TabLeaderType.Solid;
TextFragment title = new TextFragment("목차");
title.TextState.FontSize = 30;
tocInfo.Title = title;

//PDF 문서의 섹션 컬렉션에 리스트 섹션을 추가
tocPage.TocInfo = tocInfo;
//네 레벨 리스트의 형식을 설정하여 왼쪽 여백 설정
//및
//각 레벨의 텍스트 형식 설정

tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Left = 0;
tocInfo.FormatArray[0].Margin.Right = 30;
tocInfo.FormatArray[0].LineDash = TabLeaderType.Dot;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 10;
tocInfo.FormatArray[1].Margin.Right = 30;
tocInfo.FormatArray[1].LineDash = TabLeaderType.None;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].Margin.Left = 20;
tocInfo.FormatArray[2].Margin.Right = 30;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].LineDash = TabLeaderType.Solid;
tocInfo.FormatArray[3].Margin.Left = 30;
tocInfo.FormatArray[3].Margin.Right = 30;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;

//PDF 문서에 섹션 생성
Page page = doc.Pages.Add();

//섹션에 네 개의 제목 추가
for (int Level = 1; Level <= 4; Level++)
{

    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(Level);
    TextSegment segment2 = new TextSegment();
    heading2.Segments.Add(segment2);
    heading2.IsAutoSequence = true;
    heading2.TocPage = tocPage;
    segment2.Text = "샘플 제목" + Level;
    heading2.TextState.Font = FontRepository.FindFont("Arial Unicode MS");

    //목차에 제목 추가.
    heading2.IsInList = true;
    page.Paragraphs.Add(heading2);
}

// PDF 저장

doc.Save(outFile);
```
### 목차에서 페이지 번호 숨기기

목차에서 제목과 함께 페이지 번호를 표시하고 싶지 않은 경우, [TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) 클래스의 [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) 속성을 false로 사용할 수 있습니다. 목차에서 페이지 번호를 숨기기 위한 다음 코드 스니펫을 확인하세요:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "HiddenPageNumbers_out.pdf";
Document doc = new Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Table Of Contents");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
tocInfo.Title = title;
//Pdf 문서의 섹션 컬렉션에 목록 섹션을 추가합니다
tocPage.TocInfo = tocInfo;
//각 레벨의 왼쪽 여백과 텍스트 형식 설정을 설정하여 네 레벨 목록의 형식을 정의합니다

tocInfo.IsShowPageNumbers = false;
tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Right = 0;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 30;
tocInfo.FormatArray[1].TextState.Underline = true;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;
Page page = doc.Pages.Add();
//섹션에 네 개의 제목을 추가합니다
for (int Level = 1; Level != 5; Level++)

{ Heading heading2 = new Heading(Level); TextSegment segment2 = new TextSegment(); heading2.TocPage = tocPage; heading2.Segments.Add(segment2); heading2.IsAutoSequence = true; segment2.Text = "this is heading of level " + Level; heading2.IsInList = true; page.Paragraphs.Add(heading2); }
doc.Save(outFile);
```
### 목차 페이지 번호 사용자 정의하기

PDF 문서에 목차(TOC)를 추가할 때 페이지 번호를 사용자 정의하는 것이 일반적입니다. 예를 들어, 페이지 번호 앞에 P1, P2, P3 등의 접두사를 추가할 수 있습니다. 이러한 경우 Aspose.PDF for .NET은 다음 코드 샘플에서 보여주는 것처럼 페이지 번호를 사용자 정의할 수 있는 TocInfo 클래스의 PageNumbersPrefix 속성을 제공합니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해주세요.
string inFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824.pdf";
string outFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824_out.pdf";
// 기존 PDF 파일을 불러옵니다
Document doc = new Document(inFile);
// PDF 파일의 첫 페이지에 접근합니다
Aspose.Pdf.Page tocPage = doc.Pages.Insert(1);
// TOC 정보를 나타내는 객체를 생성합니다
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("목차");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
// TOC의 제목을 설정합니다
tocInfo.Title = title;
tocInfo.PageNumbersPrefix = "P";
tocPage.TocInfo = tocInfo;
for (int i = 1; i<doc.Pages.Count; i++)
{
    // Heading 객체를 생성합니다
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);
    // heading 객체의 목적지 페이지를 지정합니다
    heading2.DestinationPage = doc.Pages[i + 1];
    // 목적지 페이지
    heading2.Top = doc.Pages[i + 1].Rect.Height;
    // 목적지 좌표
    segment2.Text = "페이지 " + i.ToString();
    // TOC가 포함된 페이지에 heading을 추가합니다
    tocPage.Paragraphs.Add(heading2);
}

// 문서를 저장합니다
doc.Save(outFile);
```
## PDF 만료 날짜 설정 방법

PDF 파일에 접근 권한을 설정하여 특정 사용자 그룹이 PDF 문서의 특정 기능/객체에 접근할 수 있도록 합니다. PDF 파일 접근을 제한하기 위해 일반적으로 암호화를 적용하며, 사용자가 문서를 접근/열람할 때 PDF 파일의 만료에 대한 유효한 알림을 받도록 PDF 파일 만료 설정이 필요할 수 있습니다.

위에서 언급한 요구 사항을 달성하기 위해 *JavascriptAction* 객체를 사용할 수 있습니다. 다음 코드 스니펫을 확인해 주세요.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Document 객체를 인스턴스화
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
// PDF 파일의 페이지 컬렉션에 페이지 추가
doc.Pages.Add();
// 페이지 객체의 단락 컬렉션에 텍스트 조각 추가
doc.Pages[1].Paragraphs.Add(new TextFragment("Hello World..."));
// PDF 만료 날짜를 설정하는 JavaScript 객체 생성
JavascriptAction javaScript = new JavascriptAction(
"var year=2017;"
+ "var month=5;"
+ "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
+ "expiry = new Date(year, month);"
+ "if (today.getTime() > expiry.getTime())"
+ "app.alert('The file is expired. You need a new one.');");
// PDF 열기 액션으로 JavaScript 설정
doc.OpenAction = javaScript;

dataDir = dataDir + "SetExpiryDate_out.pdf";
// PDF 문서 저장
doc.Save(dataDir);
```
## PDF 파일 생성 진행 상황 결정

고객이 PDF 파일 생성의 진행 상황을 확인할 수 있는 기능을 추가해 달라고 요청했습니다. 이에 대한 응답은 다음과 같습니다.

[DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) 클래스의 [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) 필드를 사용하면 PDF 생성 진행 상황을 확인할 수 있습니다. 핸들러에는 다음과 같은 유형이 있습니다:

- DocSaveOptions.ConversionProgessEventHandler
- DocSaveOptions.ProgressEventHandlerInfo
- DocSaveOptions.ProgressEventType

아래 코드 스니펫은 CustomerProgressHandler 사용 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "AddTOC.pdf");
DocSaveOptions saveOptions = new DocSaveOptions();
saveOptions.CustomProgressHandler = new UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

dataDir = dataDir + "DetermineProgress_out.pdf";
pdfDocument.Save(dataDir, saveOptions);
Console.ReadLine();
```
```csharp
// 완벽한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
public static void ShowProgressOnConsole(DocSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case DocSaveOptions.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - 변환 진행 상황 : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.SourcePageAnalized:
            Console.WriteLine(String.Format("{0}  - 원본 페이지 {1} / {2} 분석됨.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - 결과 페이지 {1} / {2} 레이아웃 생성됨.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - 결과 페이지 {1} / {2} 내보내기 완료.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }

}
```
## C#에서 입력 가능한 PDF 평탄화

PDF 문서는 종종 라디오 버튼, 체크박스, 텍스트 박스, 목록 등과 같은 대화형 입력 가능 위젯을 포함합니다. 다양한 애플리케이션 목적에 맞게 편집할 수 없도록 하기 위해 PDF 파일을 평탄화할 필요가 있습니다.
Aspose.PDF는 몇 줄의 코드만으로 C#에서 PDF를 평탄화할 수 있는 기능을 제공합니다:

```csharp

// 원본 PDF 폼 로드
Document doc = new Document(dataDir + "input.pdf");

// 입력 가능한 PDF 평탄화
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// 업데이트된 문서 저장
doc.Save(dataDir);
```


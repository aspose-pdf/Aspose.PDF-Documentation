---
title: PDF에서 텍스트 교체
linktitle: PDF에서 텍스트 교체
type: docs
weight: 40
url: ko/net/replace-text-in-pdf/
description: Aspose.PDF for .NET 라이브러리에서 텍스트를 교체하고 제거하는 다양한 방법에 대해 알아보세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 텍스트 교체",
    "alternativeHeadline": "PDF 파일에서 텍스트 교체 및 제거",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, 텍스트 교체, 텍스트 제거",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET 라이브러리에서 텍스트를 교체하고 제거하는 다양한 방법에 대해 알아보세요."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 문서의 모든 페이지에서 텍스트 교체

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 문서에서 텍스트를 찾아 교체하고 이 [링크](https://products.aspose.app/pdf/redaction)에서 결과를 온라인으로 확인할 수 있습니다.

{{% /alert %}}

PDF 문서의 모든 페이지에서 텍스트를 교체하려면 먼저 TextFragmentAbsorber를 사용하여 교체하고자 하는 특정 구절을 찾아야 합니다. 그 후에는 모든 TextFragments를 순회하면서 텍스트를 교체하고 다른 속성들을 변경해야 합니다. 이 작업을 마친 후에는 Document 객체의 Save 메소드를 사용하여 출력 PDF를 저장하기만 하면 됩니다. 다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 교체하는 방법을 보여줍니다.

```csharp
// 전체 예시와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해주세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "ReplaceTextAll.pdf");

// 입력 검색 구절의 모든 인스턴스를 찾기 위해 TextAbsorber 객체를 생성합니다.
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// 모든 페이지에 대해 absorber를 적용합니다.
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 추출된 텍스트 조각을 가져옵니다.
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 조각들을 순회합니다.
foreach (TextFragment textFragment in textFragmentCollection)
{
    // 텍스트와 다른 속성을 업데이트합니다.
    textFragment.Text = "TEXT";
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}

dataDir = dataDir + "ReplaceTextAll_out.pdf";
// 결과 PDF 문서를 저장합니다.
pdfDocument.Save(dataDir);
```
## 특정 페이지 영역에서 텍스트 교체

특정 페이지 영역에서 텍스트를 교체하려면 먼저 TextFragmentAbsorber 객체를 인스턴스화하고, TextSearchOptions.Rectangle 속성을 사용하여 페이지 영역을 지정한 다음 모든 TextFragments를 순회하며 텍스트를 교체해야 합니다. 이러한 작업이 완료되면 Document 객체의 Save 메서드를 사용하여 출력 PDF를 저장하기만 하면 됩니다. 다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 교체하는 방법을 보여줍니다.

```csharp
// PDF 파일 로드
Aspose.PDF.Document pdf = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// TextFragment Absorber 객체 인스턴스화
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// 페이지 경계 내에서 텍스트 검색
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// TextSearch Options에 대한 페이지 영역 지정
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// PDF 파일의 첫 페이지에서 텍스트 검색
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// 개별 TextFragment를 순회
foreach (Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // 텍스트를 빈 문자로 업데이트
    tf.Text = "";
}

// 텍스트 교체 후 업데이트된 PDF 파일 저장
pdf.Save("c:/pdftest/TextUpdated.pdf");
```
## 정규 표현식을 기반으로 텍스트 교체하기

정규 표현식을 기반으로 일부 구문을 교체하고 싶다면, 특정 정규 표현식과 일치하는 모든 구문을 찾기 위해 TextFragmentAbsorber를 사용해야 합니다. 정규 표현식을 TextFragmentAbsorber 생성자에 매개변수로 전달해야 합니다. 또한 정규 표현식 사용 여부를 지정하는 TextSearchOptions 객체를 생성해야 합니다. 일치하는 구문을 TextFragments에서 얻은 후, 모든 구문을 반복하며 필요에 따라 업데이트해야 합니다. 마지막으로, Document 객체의 Save 메소드를 사용하여 업데이트된 PDF를 저장해야 합니다. 다음 코드 스니펫은 정규 표현식을 기반으로 텍스트를 교체하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉터리의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// 정규 표현식과 일치하는 모든 구문을 찾는 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 예: 1999-2000

// 정규 표현식 사용을 지정하기 위해 텍스트 검색 옵션 설정
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// 단일 페이지에 대해 absorber를 적용
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// 추출된 텍스트 구문 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 구문을 반복
foreach (TextFragment textFragment in textFragmentCollection)
{
    // 텍스트 및 기타 속성 업데이트
    textFragment.Text = "New Phrase";
    // 객체의 인스턴스로 설정.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```
## 기존 PDF 파일에서 폰트 교체하기

Aspose.PDF for .NET은 PDF 문서에서 텍스트를 교체하는 기능을 지원합니다. 그러나 때때로 PDF 문서 내에서 사용되는 폰트만 교체해야 할 필요가 있습니다. 따라서 텍스트를 교체하는 대신 사용되는 폰트만 교체됩니다. TextFragmentAbsorber 생성자의 오버로드 중 하나는 인수로 TextEditOptions 객체를 받아들이며, TextEditOptions.FontReplace 열거형에서 RemoveUnusedFonts 값을 사용하여 요구 사항을 충족할 수 있습니다. 다음 코드 조각은 PDF 문서 내에서 폰트를 교체하는 방법을 보여줍니다.

```csharp
// 전체 예제 및 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET을 방문하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 원본 PDF 파일 로드
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// 텍스트 조각을 검색하고 편집 옵션으로 사용되지 않는 폰트 제거를 설정
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// 모든 페이지에 대해 absorber를 수락
pdfDocument.Pages.Accept(absorber);
// 모든 TextFragments를 순회
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // 폰트 이름이 ArialMT인 경우 폰트 이름을 Arial로 교체
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```
## 텍스트 교체는 자동으로 페이지 내용을 재배열해야 합니다

Aspose.PDF for .NET은 PDF 파일 내부의 텍스트를 검색하고 교체하는 기능을 지원합니다. 그러나 최근 일부 고객들이 텍스트 교체 중에 특정 TextFragment가 더 작은 내용으로 교체되어 결과 PDF에 추가 공간이 표시되거나 TextFragment가 더 긴 문자열로 교체된 경우 기존 페이지 내용과 단어가 겹치는 문제를 겪었습니다. 따라서 PDF 문서 내의 텍스트가 교체된 후 내용이 재배열되어야 한다는 메커니즘을 도입할 필요가 있었습니다.

위에 언급한 시나리오를 처리하기 위해 Aspose.PDF for .NET이 개선되어 PDF 파일 내의 텍스트를 교체할 때 이러한 문제가 발생하지 않도록 하였습니다. 다음 코드 스니펫은 PDF 파일 내의 텍스트를 교체하는 방법과 페이지 내용이 자동으로 재배열되는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 원본 PDF 파일을 로드합니다
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// 정규 표현식을 사용하여 TextFragment Absorber 객체를 생성합니다
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// 각 TextFragment 교체
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // 교체되는 텍스트 조각의 글꼴 설정
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // 글꼴 크기 설정
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // 플레이스홀더보다 큰 문자열로 텍스트 교체
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// 결과 PDF 저장
doc.Save(dataDir);
```
## PDF 생성 시 대체 가능한 기호 렌더링

대체 가능한 기호는 실행 시 해당 내용으로 대체될 수 있는 텍스트 문자열의 특수 기호입니다. Aspose.PDF 네임스페이스의 새로운 문서 객체 모델에서 현재 지원하는 대체 가능한 기호는 `$P`, `$p`, `\n`, `\r`입니다. `$p`와 `$P`는 실행 시 페이지 번호를 처리하는 데 사용됩니다. `$p`는 현재 Paragraph 클래스가 있는 페이지의 번호로 대체됩니다. `$P`는 문서의 전체 페이지 수로 대체됩니다. PDF 문서의 paragraphs 컬렉션에 `TextFragment`를 추가할 때, 텍스트 내에 개행을 지원하지 않습니다. 그러나 개행이 있는 텍스트를 추가하려면 `TextFragment`를 `TextParagraph`와 함께 사용하십시오:

- `TextFragment`에서 단일 "\n" 대신 "\r\n" 또는 Environment.NewLine을 사용하십시오;
- TextParagraph 객체를 생성합니다. 이것은 텍스트를 분할하여 추가합니다;
- TextFragment를 TextParagraph.AppendLine에 추가합니다;
- TextParagraph를 TextBuilder.AppendParagraph에 추가합니다.

```csharp
// 전체 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// 필요한 개행 마커를 포함하는 텍스트로 새 TextFragment를 초기화합니다
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("지원자 이름: " + Environment.NewLine + " Joe Smoe");

// 필요한 경우 텍스트 프래그먼트 속성을 설정합니다
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// TextParagraph 객체를 생성합니다
TextParagraph par = new TextParagraph();

// 새 TextFragment를 단락에 추가합니다
par.AppendLine(textFragment);

// 단락 위치를 설정합니다
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// TextBuilder 객체를 생성합니다
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// TextBuilder를 사용하여 TextParagraph를 추가합니다
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```
## 헤더/푸터 영역에서 교체 가능한 기호

PDF 파일의 헤더/푸터 섹션 내부에도 교체 가능한 기호를 배치할 수 있습니다. 아래 코드 스니펫을 참고하여 푸터 섹션에 교체 가능한 기호를 추가하는 방법에 대해 살펴보세요.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// MarginInfo 인스턴스를 sec1.PageInfo의 Margin 속성에 할당합니다.
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// 헤더로 표시할 내용을 저장할 텍스트 단락을 인스턴스화합니다.
TextFragment t1 = new TextFragment("report title");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("Report_Name");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// 섹션용 HeaderFooter 객체를 생성합니다.
HeaderFooter hfFoot = new HeaderFooter();
// 홀수 및 짝수 푸터에 HeaderFooter 객체를 설정합니다.
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// 총 페이지 수 중 현재 페이지 번호를 포함하는 텍스트 단락을 추가합니다.
TextFragment t3 = new TextFragment("Generated on test date");
TextFragment t4 = new TextFragment("report name ");
TextFragment t5 = new TextFragment("Page $p of $P");

// 테이블 객체를 인스턴스화합니다.
Table tab2 = new Table();

// 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
hfFoot.Paragraphs.Add(tab2);

// 테이블의 열 너비를 설정합니다.
tab2.ColumnWidths = "165 172 165";

// 테이블에 행을 생성하고 그 행에 셀을 생성합니다.
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// 텍스트의 수직 정렬을 중앙 정렬로 설정합니다.
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
page.Paragraphs.Add(table);

// BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다.
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// 또 다른 맞춤형 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// 테이블에 행을 생성하고 그 행에 셀을 생성합니다.
Row row1 = table.Rows.Add();

row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total for Java는 Aspose가 제공하는 모든 Java 컴포넌트의 컴파일입니다. 매일 컴파일되어 각 Java 컴포넌트의 가장 최신 버전을 포함하도록 보장합니다." + CRLF + "Java 개발자는 다양한 애플리케이션을 생성할 수 있습니다.");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```
## PDF 파일에서 사용하지 않는 글꼴 제거

Aspose.PDF for .NET은 PDF 문서를 생성할 때 글꼴을 임베드하는 기능을 지원할 뿐만 아니라 기존 PDF 파일에 글꼴을 임베드하는 기능도 지원합니다. Aspose.PDF for .NET 7.3.0부터는 PDF 문서에서 중복되거나 사용되지 않는 글꼴을 제거할 수도 있습니다.

글꼴을 교체하려면 다음 접근 방식을 사용하세요:

1. [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) 클래스를 호출하세요.
1. TextFragmentAbsorber 클래스의 TextEditOptions.FontReplace.RemoveUnusedFonts 매개변수를 호출하세요. (이는 글꼴 교체 중에 사용되지 않게 된 글꼴을 제거합니다).
1. 각 텍스트 조각에 대해 글꼴을 개별적으로 설정하세요.

다음 코드 조각은 모든 문서 페이지의 모든 텍스트 조각에 대해 글꼴을 교체하고 사용하지 않는 글꼴을 제거합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참조하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 원본 PDF 파일을 로드합니다.
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// 모든 TextFragments를 반복 처리합니다.
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// 업데이트된 문서를 저장합니다.
doc.Save(dataDir);
```
## PDF 문서에서 모든 텍스트 제거

### 연산자를 사용하여 모든 텍스트 제거

텍스트 작업에서 PDF 문서에서 모든 텍스트를 제거해야 할 때가 있으며, 이 경우 일반적으로 발견된 텍스트를 빈 문자열 값으로 설정해야 합니다. 텍스트를 여러 텍스트 조각에 대해 변경하는 것은 검사 및 텍스트 위치 조정 작업을 여러 번 호출합니다. 이러한 작업은 텍스트 편집 시나리오에서 필수적입니다. 문제는 루프에서 처리될 때 제거될 텍스트 조각의 수를 결정할 수 없다는 것입니다.

따라서 PDF 페이지에서 모든 텍스트를 제거하는 시나리오에 대해 다른 접근 방식을 사용하는 것이 좋습니다. 매우 빠르게 작동하는 다음 코드 조각을 고려해 주세요.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// PDF 문서의 모든 페이지를 순환합니다
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // 페이지의 모든 텍스트 선택
    page.Contents.Accept(operatorSelector);
    // 모든 텍스트 삭제
    page.Contents.Delete(operatorSelector.Selected);
}
// 문서 저장
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
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


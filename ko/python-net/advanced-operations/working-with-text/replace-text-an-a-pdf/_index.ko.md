---
title: Python을 통한 PDF에서 텍스트 교체
linktitle: PDF에서 텍스트 교체
type: docs
weight: 40
url: /python-net/replace-text-in-pdf/
description: Aspose.PDF for Python via .NET 라이브러리에서 텍스트를 교체 및 제거하는 다양한 방법에 대해 알아보세요.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
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
    "keywords": "pdf, python, 텍스트 교체, 텍스트 제거",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/python-net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/replace-text-in-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Aspose.PDF for Python via .NET 라이브러리에서 텍스트를 교체 및 제거하는 다양한 방법에 대해 알아보세요."
}
</script>


## PDF 문서의 모든 페이지에서 텍스트 교체

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 문서에서 텍스트를 찾고 교체하여 결과를 온라인으로 얻을 수 있습니다 [링크](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

PDF 문서의 모든 페이지에서 텍스트를 교체하려면 먼저 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/)를 사용하여 교체하려는 특정 구문을 찾아야 합니다. 그런 다음 모든 TextFragment를 통해 텍스트를 교체하고 다른 속성을 변경해야 합니다. 완료한 후에는 Document 객체의 Save 메서드를 사용하여 출력 PDF를 저장하기만 하면 됩니다. 다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 교체하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # 문서 열기
    document = ap.Document(input_pdf)

    # 입력 검색 구문의 모든 인스턴스를 찾기 위해 TextAbsorber 객체 생성
    absorber = ap.text.TextFragmentAbsorber("format")

    # 모든 페이지에 대해 absorber 수락
    document.pages.accept(absorber)

    # 추출된 텍스트 조각 가져오기
    collection = absorber.text_fragments

    # 조각을 반복
    for text_fragment in collection:
        # 텍스트 및 기타 속성 업데이트
        text_fragment.text = "FORMAT"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
        text_fragment.text_state.font_size = 22
        text_fragment.text_state.foreground_color = ap.Color.blue
        text_fragment.text_state.background_color = ap.Color.green

    # 문서 저장
    document.save(output_pdf)
```


## 특정 페이지 영역의 텍스트 교체

특정 페이지 영역의 텍스트를 교체하기 위해, 먼저 TextFragmentAbsorber 객체를 인스턴스화하고, TextSearchOptions.Rectangle 속성을 사용하여 페이지 영역을 지정한 다음 모든 TextFragments를 반복하여 텍스트를 교체해야 합니다. 이러한 작업이 완료되면, Document 객체의 Save 메서드를 사용하여 출력 PDF를 저장하기만 하면 됩니다. 다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 교체하는 방법을 보여줍니다.

```python
// PDF 파일 불러오기
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// TextFragment Absorber 객체 인스턴스화
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// 페이지 경계 내에서 텍스트 검색
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// TextSearch 옵션에 대한 페이지 영역 지정
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// PDF 파일의 첫 페이지에서 텍스트 검색
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// 개별 TextFragment 반복
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // 텍스트를 빈 문자로 업데이트
    tf.Text = "";
}

// 텍스트 교체 후 업데이트된 PDF 파일 저장
pdf.Save("c:/pdftest/TextUpdated.pdf");
```


## 정규 표현식을 기반으로 텍스트 교체

정규 표현식을 기반으로 일부 구문을 교체하려면 먼저 TextFragmentAbsorber를 사용하여 특정 정규 표현식과 일치하는 모든 구문을 찾아야 합니다. TextFragmentAbsorber 생성자에 정규 표현식을 매개변수로 전달해야 합니다. 정규 표현식이 사용되는지 여부를 지정하는 TextSearchOptions 객체도 생성해야 합니다. TextFragments에서 일치하는 구문을 얻으면 모든 구문을 반복하여 필요에 따라 업데이트해야 합니다. 마지막으로, Document 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장해야 합니다. 다음 코드 스니펫은 정규 표현식을 기반으로 텍스트를 교체하는 방법을 보여줍니다.

```python
// 전체 예제 및 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참조하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// 정규 표현식과 일치하는 모든 구문을 찾기 위한 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 예: 1999-2000

// 정규 표현식 사용 여부를 지정하도록 텍스트 검색 옵션 설정
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// 단일 페이지에 대해 흡수기 수락
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// 추출된 텍스트 조각 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 조각 반복
foreach (TextFragment textFragment in textFragmentCollection)
{
    // 텍스트 및 기타 속성 업데이트
    textFragment.Text = "새로운 구문";
    // 객체의 인스턴스로 설정합니다.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```


## 기존 PDF 파일에서 글꼴 교체

Aspose.PDF for Python via .NET은 PDF 문서에서 텍스트를 교체하는 기능을 지원합니다. 그러나 때때로 PDF 문서 내에서 사용되는 글꼴만 교체해야 할 필요가 있습니다. 따라서 텍스트를 교체하는 대신, 사용되는 글꼴만 교체됩니다. TextFragmentAbsorber 생성자의 오버로드 중 하나는 TextEditOptions 객체를 인수로 받아들이며, 우리는 TextEditOptions.FontReplace 열거형에서 RemoveUnusedFonts 값을 사용하여 우리의 요구사항을 충족할 수 있습니다. 다음 코드 스니펫은 PDF 문서 내의 글꼴을 교체하는 방법을 보여줍니다.

```python
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET를 참조하세요.
// 문서 디렉토리의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 소스 PDF 파일 로드
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// 텍스트 조각 검색 및 편집 옵션을 사용하지 않는 글꼴 제거로 설정
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// 모든 페이지에 대해 흡수기 허용
pdfDocument.Pages.Accept(absorber);
// 모든 TextFragment를 순회
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // 글꼴 이름이 ArialMT인 경우, 글꼴 이름을 Arial로 교체
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```


## 텍스트 교체는 페이지 내용을 자동으로 재배치해야 합니다

Aspose.PDF for Python via .NET은 PDF 파일 내에서 텍스트를 검색하고 교체하는 기능을 지원합니다. 그러나 최근 몇몇 고객들이 특정 TextFragment가 더 작은 내용으로 교체될 때 결과 PDF에 여분의 공백이 표시되거나, TextFragment가 더 긴 문자열로 교체될 때 단어가 기존 페이지 콘텐츠와 겹치는 문제가 발생했습니다. 따라서 PDF 문서 내의 텍스트가 교체되면 콘텐츠가 재배치되어야 한다는 요구사항이 있었습니다.

위에서 언급한 시나리오를 해결하기 위해, Aspose.PDF for Python via .NET이 향상되어, PDF 파일 내에서 텍스트를 교체할 때 이러한 문제가 발생하지 않도록 했습니다. 다음 코드 스니펫은 PDF 파일 내의 텍스트를 교체하고 페이지 내용이 자동으로 재배치되는 방법을 보여줍니다.

```python
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하세요
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 소스 PDF 파일 로드
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// 정규 표현식을 사용하여 TextFragment Absorber 객체 생성
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
    // 자리 표시자보다 큰 문자열로 텍스트 교체
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// 결과 PDF 저장
doc.Save(dataDir);
```


## PDF 생성 중 교체 가능한 기호 렌더링

교체 가능한 기호는 실행 시점에 해당 내용으로 대체될 수 있는 텍스트 문자열 내의 특별한 기호입니다. Aspose.PDF 네임스페이스의 새로운 문서 객체 모델이 현재 지원하는 교체 가능한 기호는 `$P`, `$p,` `\n`, `\r`입니다. `$p`와 `$P`는 실행 시점에 페이지 번호를 처리하는 데 사용됩니다. `$p`는 현재 Paragraph 클래스가 위치한 페이지의 번호로 대체됩니다. `$P`는 문서의 총 페이지 수로 대체됩니다. PDF 문서의 단락 컬렉션에 `TextFragment`를 추가할 때, 텍스트 내의 줄 바꿈은 지원되지 않습니다. 그러나 줄 바꿈이 있는 텍스트를 추가하기 위해서는 `TextParagraph`와 함께 `TextFragment`를 사용하십시오:

- 단일 "\n" 대신 TextFragment에서 "\r\n" 또는 Environment.NewLine을 사용하십시오;
- TextParagraph 객체를 생성하십시오. 그러면 텍스트를 줄 단위로 나누어 추가합니다;
- TextFragment를 TextParagraph.AppendLine으로 추가하십시오;
- TextParagraph를 TextBuilder.AppendParagraph로 추가하십시오.

```python
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 를 참조하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// 필요한 줄 바꿈 표시를 포함한 텍스트로 새로운 TextFragment 초기화
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// 필요 시 텍스트 조각 속성 설정
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// TextParagraph 객체 생성
TextParagraph par = new TextParagraph();

// 새 TextFragment를 단락에 추가
par.AppendLine(textFragment);

// 단락 위치 설정
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// TextBuilder 객체 생성
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// TextBuilder를 사용하여 TextParagraph 추가
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```


## 헤더/푸터 영역의 대체 가능한 기호

대체 가능한 기호는 PDF 파일의 헤더/푸터 섹션 안에 배치할 수도 있습니다. 푸터 섹션에 대체 가능한 기호를 추가하는 방법에 대한 자세한 내용은 다음 코드 스니펫을 참조하십시오.

```python
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET를 참조하십시오.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// marginInfo 인스턴스를 sec1.PageInfo의 Margin 속성에 할당합니다.
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

// 섹션에 대한 HeaderFooter 객체를 만듭니다.
HeaderFooter hfFoot = new HeaderFooter();
// 헤더푸터 객체를 홀수 및 짝수 페이지의 푸터에 설정합니다.
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// 현재 페이지 번호와 총 페이지 수를 포함하는 텍스트 단락을 추가합니다.
TextFragment t3 = new TextFragment("Generated on test date");
TextFragment t4 = new TextFragment("report name ");
TextFragment t5 = new TextFragment("Page $p of $P");

// 테이블 객체를 인스턴스화합니다.
Table tab2 = new Table();

// 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
hfFoot.Paragraphs.Add(tab2);

// 테이블의 열 너비를 설정합니다.
tab2.ColumnWidths = "165 172 165";

// 테이블에 행을 생성한 후 행에 셀을 추가합니다.
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// 텍스트의 수직 정렬을 가운데 정렬로 설정합니다.
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

// Sec1.Paragraphs.Add(New Text("Aspose.Total for Java는 Aspose가 제공하는 모든 Java 컴포넌트의 컴파일입니다. 매일 컴파일되어 각 Java 컴포넌트의 최신 버전을 포함하는지 확인합니다. Aspose.Total for Java를 사용하여 개발자는 다양한 응용 프로그램을 만들 수 있습니다. Aspose.Total for Java는 Aspose가 제공하는 모든 Java 컴포넌트의 컴파일입니다. 매일 컴파일되어 각 Java 컴포넌트의 최신 버전을 포함하는지 확인합니다. Aspose.Total for Java를 사용하여 개발자는 다양한 응용 프로그램을 만들 수 있습니다. Aspose.Total for Java는 Aspose가 제공하는 모든 Java 컴포넌트의 컴파일입니다. 매일 컴파일되어 각 Java 컴포넌트의 최신 버전을 포함하는지 확인합니다. Aspose.Total for Java를 사용하여 개발자는 다양한 응용 프로그램을 만들 수 있습니다."))
Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
page.Paragraphs.Add(table);

// BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다.
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// 또 다른 사용자 정의 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// 테이블에 행을 생성한 후 행에 셀을 추가합니다.
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
            c1 = row.Cells.Add("Aspose.Total for Java는 Aspose가 제공하는 모든 Java 컴포넌트의 컴파일입니다. 매일 컴파일되어 각 Java 컴포넌트의 최신 버전을 포함하는지 확인합니다. " + CRLF + "매일 컴파일되어 각 Java 컴포넌트의 최신 버전을 포함하는지 확인합니다. " + CRLF + "Aspose.Total for Java를 사용하여 개발자는 다양한 응용 프로그램을 만들 수 있습니다.");
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


## PDF 파일에서 사용되지 않는 글꼴 제거

Aspose.PDF for Python via .NET은 PDF 문서를 생성할 때 글꼴을 포함하는 기능뿐만 아니라 기존 PDF 파일에 글꼴을 포함하는 기능도 지원합니다. Aspose.PDF for Python via .NET 7.3.0부터는 PDF 문서에서 중복되거나 사용되지 않는 글꼴을 제거할 수도 있습니다.

글꼴을 교체하려면 다음 접근 방법을 사용하세요:

1. [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) 클래스를 호출합니다.
1. TextFragmentAbsorber 클래스의 TextEditOptions.FontReplace.RemoveUnusedFonts 매개변수를 호출합니다. (이 옵션은 글꼴 교체 중 사용되지 않게 된 글꼴을 제거합니다).
1. 각 텍스트 조각에 대해 개별적으로 글꼴을 설정합니다.

다음 코드 스니펫은 모든 문서 페이지의 모든 텍스트 조각에 대해 글꼴을 교체하고 사용되지 않는 글꼴을 제거합니다.

```python
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 를 참조하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 소스 PDF 파일 로드
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// 모든 TextFragments를 반복
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// 업데이트된 문서 저장
doc.Save(dataDir);
```


## PDF 문서에서 모든 텍스트 제거

### 연산자를 사용하여 모든 텍스트 제거

일부 텍스트 작업에서는 PDF 문서에서 모든 텍스트를 제거해야 하며, 이를 위해 일반적으로 발견된 텍스트를 빈 문자열 값으로 설정해야 합니다. 다수의 텍스트 조각의 텍스트를 변경하면 여러 검증과 텍스트 위치 조정 작업이 필요합니다. 이러한 작업은 텍스트 편집 시나리오에서 필수적입니다. 문제는 루프에서 처리될 때 얼마나 많은 텍스트 조각이 제거될지 알 수 없다는 것입니다.

따라서 PDF 페이지에서 모든 텍스트를 제거하는 시나리오에서는 다른 접근 방식을 사용하는 것이 좋습니다. 다음의 매우 빠르게 작동하는 코드 스니펫을 고려해 보십시오.

```python
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET를 참조하십시오.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// PDF 문서의 모든 페이지를 반복
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
    "name": "Aspose.PDF for Python via .NET Library",
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
    "applicationCategory": "Python용 PDF 조작 라이브러리",
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
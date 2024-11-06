---
title: PDF에서 C#을 사용하여 테이블 생성 또는 추가
linktitle: 테이블 생성 또는 추가
type: docs
weight: 10
url: ko/net/add-table-in-existing-pdf-document/
description: Aspose.PDF for .NET은 PDF 테이블을 생성, 읽기 및 편집하는 데 사용되는 라이브러리입니다. 이 주제에서 다른 고급 기능을 확인하세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-extract-a-table/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 C#을 사용하여 테이블 생성 또는 추가",
    "alternativeHeadline": ".NET으로 PDF에 테이블 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf에서 테이블 생성, 테이블 추가",
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
    "url": "/net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET은 PDF 테이블을 생성, 읽기 및 편집하는 데 사용되는 라이브러리입니다. 이 주제에서 다른 고급 기능을 확인하세요."
}
</script>
## C#을 사용하여 테이블 만들기

PDF 문서를 작업할 때 테이블은 중요합니다. 이들은 정보를 체계적인 방식으로 표시하는 데 훌륭한 기능을 제공합니다. Aspose.PDF 네임스페이스에는 PDF 문서를 처음부터 생성할 때 테이블을 만드는 기능을 제공하는 [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row)과 같은 클래스가 포함되어 있습니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 함께 작동합니다.

Table 클래스의 객체를 생성하여 테이블을 만들 수 있습니다.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### 기존 PDF 문서에 테이블 추가

Aspose.PDF for .NET을 사용하여 기존 PDF 파일에 테이블을 추가하려면 다음 단계를 따르십시오:

1. 소스 파일을 로드합니다.
1. 테이블을 초기화하고 열과 행을 설정합니다.
1. 테이블 설정을 설정합니다(우리는 테두리를 설정했습니다).
1. 테이블을 채웁니다.
1. 페이지에 테이블을 추가합니다.
1.
다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 소스 PDF 문서를 로드합니다
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddTable.pdf");
// 테이블의 새 인스턴스를 초기화합니다
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// 테이블 테두리 색상을 LightGray로 설정합니다
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// 테이블 셀의 테두리를 설정합니다
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// 10개의 행을 추가하기 위한 루프를 생성합니다
for (int row_count = 1; row_count < 10; row_count++)
{
    // 테이블에 행을 추가합니다
    Aspose.Pdf.Row row = table.Rows.Add();
    // 테이블 셀을 추가합니다
    row.Cells.Add("Column (" + row_count + ", 1)");
    row.Cells.Add("Column (" + row_count + ", 2)");
    row.Cells.Add("Column (" + row_count + ", 3)");
}
// 입력 문서의 첫 페이지에 테이블 객체를 추가합니다
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "document_with_table_out.pdf";
// 테이블 객체를 포함한 업데이트된 문서를 저장합니다
doc.Save(dataDir);
```
### 테이블에서 ColSpan과 RowSpan

Aspose.PDF for .NET은 테이블에서 열을 병합하기 위한 [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan) 속성과 행을 병합하기 위한 [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan) 속성을 제공합니다.

`Cell` 객체에서 `ColSpan` 또는 `RowSpan` 속성을 사용하며, 이 객체는 테이블 셀을 생성합니다. 필요한 속성을 적용한 후 생성된 셀을 테이블에 추가할 수 있습니다.

```csharp
public static void AddTable_RowColSpan()
{
    // 소스 PDF 문서 불러오기
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.Pages.Add();

    // 테이블의 새 인스턴스 초기화
    Aspose.Pdf.Table table = new Aspose.Pdf.Table
    {
        // 테이블 테두리 색상을 LightGray로 설정
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
        // 테이블 셀의 테두리 설정
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
    };

    // 테이블에 첫 번째 행 추가
    Aspose.Pdf.Row row1 = table.Rows.Add();
    for (int cellCount = 1; cellCount <5; cellCount++)
    {
        // 테이블 셀 추가
        row1.Cells.Add($"Test 1 {cellCount}");
    }

    // 테이블에 두 번째 행 추가
    Aspose.Pdf.Row row2 = table.Rows.Add();
    row2.Cells.Add($"Test 2 1");
    var cell = row2.Cells.Add($"Test 2 2");
    cell.ColSpan = 2;
    row2.Cells.Add($"Test 2 4");

    // 테이블에 세 번째 행 추가
    Aspose.Pdf.Row row3 = table.Rows.Add();
    row4.Cells.Add("Test 3 1");
    row4.Cells.Add("Test 3 2");
    row4.Cells.Add("Test 3 3");
    row4.Cells.Add("Test 3 4");

    // 테이블에 네 번째 행 추가
    Aspose.Pdf.Row row4 = table.Rows.Add();
    row3.Cells.Add("Test 4 1");
    cell = row3.Cells.Add("Test 4 2");
    cell.RowSpan = 2;
    row3.Cells.Add("Test 4 3");
    row3.Cells.Add("Test 4 4");

    // 테이블에 다섯 번째 행 추가
    row4 = table.Rows.Add();
    row4.Cells.Add("Test 5 1");
    row4.Cells.Add("Test 5 3");
    row4.Cells.Add("Test 5 4");

    // 테이블 객체를 입력 문서의 첫 페이지에 추가
    pdfDocument.Pages[1].Paragraphs.Add(table);

    // 테이블 객체를 포함한 업데이트된 문서 저장
    doc.Save(Path.Combine(_dataDir, "document_with_table_out.pdf"));
}
```
아래 코드 실행 결과는 다음 이미지에 표시된 테이블입니다:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## 테두리, 여백 및 패딩 작업

테이블의 테두리 스타일, 여백 및 셀 패딩을 설정하는 기능도 지원한다는 점을 유의해 주세요. 기술적인 세부사항으로 들어가기 전에, 아래 다이어그램에서 제시된 테두리, 여백 및 패딩의 개념을 이해하는 것이 중요합니다:

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

위 그림에서 볼 수 있듯이 테이블, 행, 셀의 테두리가 겹칩니다. Aspose.PDF를 사용하여 테이블에는 여백을 설정할 수 있고 셀에는 패딩을 설정할 수 있습니다. 셀 여백을 설정하려면 셀 패딩을 설정해야 합니다.

### 테두리

테이블, [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) 및 [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell) 객체의 테두리를 설정하려면 Table.Border, Row.Border 및 Cell.Border 속성을 사용하세요.
테이블, [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) 및 [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell) 객체의 테두리를 설정하려면 Table.Border, Row.Border 및 Cell.Border 속성을 사용하세요.

### 여백 또는 패딩

셀 패딩은 Table 클래스의 [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) 속성을 사용하여 관리할 수 있습니다. 모든 패딩 관련 속성은 `Left`, `Right`, `Top` 및 `Bottom` 매개변수에 대한 정보를 가져와 사용자 정의 여백을 생성하는 [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo) 클래스의 인스턴스에 할당됩니다.

다음 예에서는 셀 테두리의 너비를 0.1포인트로, 테이블 테두리의 너비를 1포인트로 설정하고 셀 패딩은 5포인트로 설정합니다.

![PDF 테이블의 여백과 테두리](margin-border.png)

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Document 객체를 빈 생성자를 호출하여 인스턴스화합니다.
Document doc = new Document();
Page page = doc.Pages.Add();
// 테이블 객체를 인스턴스화합니다
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// 원하는 섹션의 문단 컬렉션에 테이블을 추가합니다
page.Paragraphs.Add(tab1);
// 테이블의 열 너비를 설정합니다
tab1.ColumnWidths = "50 50 50";
// BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// 또 다른 사용자 정의 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// MarginInfo 객체를 생성하고 왼쪽, 아래, 오른쪽, 위쪽 여백을 설정합니다
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// MarginInfo 객체에 기본 셀 패딩을 설정합니다
tab1.DefaultCellPadding = margin;
// 테이블에 행을 생성한 다음 행에 셀을 생성합니다
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add();
TextFragment mytext = new TextFragment("col3 with large text string");
// Row1.Cells.Add("col3 with large text string to be placed inside cell");
row1.Cells[2].Paragraphs.Add(mytext);
row1.Cells[2].IsWordWrapped = false;
// Row1.Cells[2].Paragraphs[0].FixedWidth= 80;
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");
dataDir = dataDir + "MarginsOrPadding_out.pdf";
// Pdf를 저장합니다
doc.Save(dataDir);
```
모서리가 둥근 테이블을 만들려면 BorderInfo 클래스의 `RoundedBorderRadius` 값을 사용하고 테이블 모서리 스타일을 둥글게 설정하십시오.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

GraphInfo graph = new GraphInfo();
graph.Color = Aspose.Pdf.Color.Red;
// 빈 BorderInfo 객체를 생성합니다
BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
// 모서리의 반경을 15로 설정하여 둥근 테두리를 설정합니다
bInfo.RoundedBorderRadius = 15;
// 테이블 모서리 스타일을 둥글게 설정합니다.
tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
// 테이블 테두리 정보를 설정합니다
tab1.Border = bInfo;
```

## 테이블에 다양한 자동 맞춤 설정 적용

Microsoft Word와 같은 시각적 에이전트를 사용하여 테이블을 만들 때 종종 원하는 너비로 테이블을 자동으로 크기 조정하는 AutoFit 옵션 중 하나를 사용하게 됩니다.
마이크로소프트 워드와 같은 시각적 에이전트를 사용하여 테이블을 생성할 때, 종종 원하는 너비로 테이블을 자동 크기 조정하기 위해 AutoFit 옵션 중 하나를 사용하게 됩니다.

기본적으로 Aspose.Pdf는 `ColumnAdjustment`를 `Customized` 값으로 사용하여 새 테이블을 삽입합니다. 테이블은 페이지에 사용 가능한 너비에 맞게 크기가 조정됩니다. 이러한 테이블 또는 기존 테이블의 크기 조정 동작을 변경하려면 Table.autoFit(int) 메소드를 호출할 수 있습니다. 이 메소드는 테이블에 적용된 자동 맞춤 유형을 정의하는 AutoFitBehavior 열거형을 받아들입니다.

마이크로소프트 워드에서와 같이, autofit 메소드는 실제로 한 번에 테이블에 다양한 속성을 적용하는 단축키입니다. 이러한 속성들이 실제로 테이블에 관찰된 동작을 제공합니다. 각 autofit 옵션에 대한 이러한 속성들을 논의할 것입니다. 다음 테이블을 사용하고 다양한 자동 맞춤 설정을 적용하여 시연할 것입니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 빈 생성자를 호출하여 Pdf 객체를 인스턴스화합니다
Document doc = new Document();
// Pdf 객체에 섹션을 생성합니다
Page sec1 = doc.Pages.Add();

// 테이블 객체를 인스턴스화합니다
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다
sec1.Paragraphs.Add(tab1);

// 테이블의 열 너비를 설정합니다
tab1.ColumnWidths = "50 50 50";
tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

// BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

// 또 다른 맞춤형 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// MarginInfo 객체를 생성하고 왼쪽, 하단, 오른쪽, 상단 여백을 설정합니다
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;

// MarginInfo 객체로 기본 셀 패딩을 설정합니다
tab1.DefaultCellPadding = margin;

// 테이블에 행을 생성하고 행에 셀을 추가합니다
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");

dataDir = dataDir + "AutoFitToWindow_out.pdf";
// 테이블 객체를 포함한 업데이트된 문서를 저장합니다
doc.Save(dataDir);
```
### 테이블 너비 가져오기

때때로 테이블의 너비를 동적으로 가져와야 할 필요가 있습니다. Aspose.PDF.Table 클래스에는 이 목적을 위한 [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) 메소드가 있습니다. 예를 들어, 테이블 열 너비를 명시적으로 설정하지 않고 [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment)를 AutoFitToContent로 설정한 경우 다음과 같이 테이블 너비를 가져올 수 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 새 문서 생성
Document doc = new Document();
// 문서에 페이지 추가
Page page = doc.Pages.Add();
// 새 테이블 초기화
Table table = new Table
{
    ColumnAdjustment = ColumnAdjustment.AutoFitToContent
};
// 테이블에 행 추가
Row row = table.Rows.Add();
// 테이블에 셀 추가
Cell cell = row.Cells.Add("Cell 1 text");
cell = row.Cells.Add("Cell 2 text");
// 테이블 너비 가져오기
Console.WriteLine(table.GetWidth());
```

## 테이블 셀에 SVG 이미지 추가하기
## 테이블 셀에 SVG 이미지 추가

Aspose.PDF for .NET은 PDF 파일에 테이블 셀을 추가하는 기능을 지원합니다. 테이블을 생성할 때 셀에 텍스트나 이미지를 추가할 수 있습니다. 또한, API는 SVG 파일을 PDF 형식으로 변환하는 기능도 제공합니다. 이러한 기능을 조합하여 SVG 이미지를 로드하고 테이블 셀에 추가할 수 있습니다.

다음 코드 스니펫은 테이블 인스턴스를 생성하고 테이블 셀 안에 SVG 이미지를 추가하는 단계를 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참조하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Document 객체를 인스턴스화합니다.
Document doc = new Document();
// 이미지 인스턴스를 생성합니다.
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// 이미지 유형을 SVG로 설정합니다.
img.FileType = Aspose.Pdf.ImageFileType.Svg;
// 소스 파일 경로입니다.
img.File = dataDir + "SVGToPDF.svg";
// 이미지 인스턴스의 너비를 설정합니다.
img.FixWidth = 50;
// 이미지 인스턴스의 높이를 설정합니다.
img.FixHeight = 50;
// 테이블 인스턴스를 생성합니다.
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// 테이블 셀의 너비를 설정합니다.
table.ColumnWidths = "100 100";
// 행 객체를 생성하고 테이블 인스턴스에 추가합니다.
Aspose.Pdf.Row row = table.Rows.Add();
// 셀 객체를 생성하고 행 인스턴스에 추가합니다.
Aspose.Pdf.Cell cell = row.Cells.Add();
// 셀 객체의 단락 컬렉션에 TextFragment를 추가합니다.
cell.Paragraphs.Add(new TextFragment("첫 번째 셀"));
// 행 객체에 다른 셀을 추가합니다.
cell = row.Cells.Add();
// 최근에 추가된 셀 인스턴스의 단락 컬렉션에 SVG 이미지를 추가합니다.
cell.Paragraphs.Add(img);
// 페이지 객체를 생성하고 문서 인스턴스의 페이지 컬렉션에 추가합니다.
Page page = doc.Pages.Add();
// 페이지 객체의 단락 컬렉션에 테이블을 추가합니다.
page.Paragraphs.Add(table);

dataDir = dataDir + "AddSVGObject_out.pdf";
// PDF 파일을 저장합니다.
doc.Save(dataDir);
```
## 테이블 내에서 HTML 태그 사용하기

때로는 HTML 태그가 포함된 데이터베이스 내용을 가져와서 Table 객체에 내용을 가져올 필요가 생길 수 있습니다. 내용을 가져올 때 PDF 문서 내에서 HTML 태그가 적절하게 렌더링되어야 합니다. 이러한 요구 사항을 달성하기 위해 ImprotDataTable() 메소드를 개선하였습니다:

{{% alert color="primary" %}}

테이블 요소 내에서 HTML 태그를 사용하면 문서 생성 시간이 증가한다는 점을 유의해 주세요. API는 HTML 태그를 적절하게 처리하고 출력 PDF 문서에 렌더링해야 합니다.

{{% /alert %}}

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("data", System.Type.GetType("System.String"));

DataRow dr = dt.NewRow();
dr[0] = "<li>응급의학과: 3400 스프루스 스트리트 그라운드 실버스타인 빌딩 필라델피아 PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>펜 관찰 의학 서비스: 3400 스프루스 스트리트 그라운드 플로어 도너 필라델피아 PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>UPHS/프레스비터리언 - 응급의학과: 51 N. 39th Street . 필라델피아 PA 19104-2640</li>";
dt.Rows.Add(dr);

Document doc = new Document();
doc.Pages.Add();
// 테이블의 새 인스턴스 초기화
Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
// 테이블의 열 너비 설정
tableProvider.ColumnWidths = "400 50 ";
// 테이블 테두리 색상을 LightGray로 설정
tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// 테이블 셀의 테두리 설정
tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 2.5F;
margin.Left = 2.5F;
margin.Bottom = 1.0F;
tableProvider.DefaultCellPadding = margin;

tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

doc.Pages[1].Paragraphs.Add(tableProvider);
doc.Save(dataDir + "HTMLInsideTableCell_out.pdf");
```
## 테이블 행 사이에 페이지 구분 삽입

기본적으로 PDF 파일 내에 테이블을 생성할 때, 테이블이 하단 마진에 도달하면 테이블은 연속 페이지로 넘어갑니다. 그러나 특정 수의 행이 추가될 때 강제로 페이지 구분을 삽입해야 할 필요가 있을 수 있습니다. 다음 코드 조각은 테이블에 10개의 행이 추가될 때 페이지 구분을 삽입하는 단계를 보여줍니다.

```csharp
// 전체 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 로 이동하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 문서 인스턴스를 인스턴스화합니다
Document doc = new Document();
// PDF 파일의 페이지 컬렉션에 페이지를 추가합니다
doc.Pages.Add();
// 테이블 인스턴스를 생성합니다
Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
// 테이블의 테두리 스타일을 설정합니다
tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// 빨간색 테두리로 기본 테두리 스타일을 설정합니다
tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// 테이블의 열 너비를 지정합니다
tab.ColumnWidths = "100 100";
// 테이블에 200개의 행을 추가하기 위한 루프를 생성합니다
for (int counter = 0; counter <= 200; counter++)
{
    Aspose.Pdf.Row row = new Aspose.Pdf.Row();
    tab.Rows.Add(row);
    Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
    cell1.Paragraphs.Add(new TextFragment("Cell " + counter + ", 0"));
    row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
    cell2.Paragraphs.Add(new TextFragment("Cell " + counter + ", 1"));
    row.Cells.Add(cell2);
    // 10행이 추가될 때마다 새 페이지에 새 행을 렌더링합니다
    if (counter % 10 == 0 && counter != 0) row.IsInNewPage = true;
}
// 테이블을 PDF 파일의 단락 컬렉션에 추가합니다
doc.Pages[1].Paragraphs.Add(tab);

dataDir = dataDir + "InsertPageBreak_out.pdf";
// PDF 문서를 저장합니다
doc.Save(dataDir);
```
## 새 페이지에 테이블 렌더링

기본적으로, 문단들은 Page 객체의 Paragraphs 컬렉션에 추가됩니다. 그러나 이전에 추가된 문단 수준 객체 바로 뒤가 아닌 새 페이지에 테이블을 렌더링하는 것이 가능합니다.

### 예제: C#을 사용하여 새 페이지에 테이블 렌더링하는 방법

새 페이지에 테이블을 렌더링하려면 BaseParagraph 클래스의 [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) 속성을 사용하세요. 다음 코드 스니펫이 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document();
PageInfo pageInfo = doc.PageInfo;
Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

marginInfo.Left = 37;
marginInfo.Right = 37;
marginInfo.Top = 37;
marginInfo.Bottom = 37;

pageInfo.IsLandscape = true;

Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "50 100";
// 페이지 추가.
Page curPage = doc.Pages.Add();
for (int i = 1; i <= 120; i++)
{
    Aspose.Pdf.Row row = table.Rows.Add();
    row.FixedRowHeight = 15;
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("Content 1"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("HHHHH"));
}
Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
paragraphs.Add(table);
/********************************************/
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table.ColumnWidths = "100 100";
for (int i = 1; i <= 10; i++)
{
    Aspose.Pdf.Row row = table1.Rows.Add();
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("LAAAAAAA"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("LAAGGGGGG"));
}
table1.IsInNewPage = true;
// 테이블 1을 다음 페이지에 유지하고 싶습니다...
paragraphs.Add(table1);
dataDir = dataDir + "IsNewPageProperty_Test_out.pdf";
doc.Save(dataDir);
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


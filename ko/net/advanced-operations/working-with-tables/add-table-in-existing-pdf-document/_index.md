---
title: PDF에서 C#을 사용하여 테이블 만들기 또는 추가하기
linktitle: 테이블 만들기 또는 추가하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/add-table-in-existing-pdf-document/
description: Aspose.PDF for .NET은 PDF 테이블을 생성, 읽기 및 편집하는 데 사용되는 라이브러리입니다. 이 주제에서 다른 고급 기능을 확인하세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create or Add Table In PDF using C#",
    "alternativeHeadline": "Add Tables to PDFs Effortlessly with C#",
    "abstract": "Aspose.PDF for .NET의 새로운 기능은 개발자가 C#을 사용하여 기존 PDF 문서에 테이블을 원활하게 생성하고 추가할 수 있도록 합니다. 이 기능에는 사용자 정의 가능한 테두리, 셀 여백 및 ColSpan 및 RowSpan으로 셀 병합을 지원하는 고급 기능이 포함되어 있어 PDF 파일의 데이터 표현을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "3283",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET은 PDF 테이블을 생성, 읽기 및 편집하는 데 사용되는 라이브러리입니다. 이 주제에서 다른 고급 기능을 확인하세요."
}
</script>

## C#을 사용하여 테이블 만들기

PDF 문서 작업 시 테이블은 중요합니다. 테이블은 정보를 체계적으로 표시하는 데 훌륭한 기능을 제공합니다. Aspose.PDF 네임스페이스에는 PDF 문서를 처음부터 생성할 때 테이블을 생성하는 기능을 제공하는 [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row)라는 클래스가 포함되어 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

Table 클래스의 객체를 생성하여 테이블을 만들 수 있습니다.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### 기존 PDF 문서에 테이블 추가하기

Aspose.PDF for .NET을 사용하여 기존 PDF 파일에 테이블을 추가하려면 다음 단계를 따르세요:

1. 소스 파일을 로드합니다.
1. 테이블을 초기화하고 열과 행을 설정합니다.
1. 테이블 설정을 지정합니다(테두리를 설정했습니다).
1. 테이블을 채웁니다.
1. 페이지에 테이블을 추가합니다.
1. 파일을 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTable.pdf"))
    {
        // Initializes a new instance of the Table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        // Set the table border color as LightGray
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Set the border for table cells
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Create a loop to add 10 rows
        for (int row_count = 1; row_count < 10; row_count++)
        {
            // Add row to table
            Aspose.Pdf.Row row = table.Rows.Add();
            // Add table cells
            row.Cells.Add("Column (" + row_count + ", 1)");
            row.Cells.Add("Column (" + row_count + ", 2)");
            row.Cells.Add("Column (" + row_count + ", 3)");
        }
        // Add table object to first page of input document
        document.Pages[1].Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddTable_out.pdf");
    }
}
```

### 테이블의 ColSpan 및 RowSpan

Aspose.PDF for .NET은 테이블에서 열을 병합하기 위한 [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan) 속성과 행을 병합하기 위한 [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan) 속성을 제공합니다.

우리는 테이블 셀을 생성하는 `Cell` 객체에서 `ColSpan` 또는 `RowSpan` 속성을 사용합니다. 필요한 속성을 적용한 후 생성된 셀을 테이블에 추가할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTableRowColSpan()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Initializes a new instance of the Table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table
        {
            // Set the table border color as LightGray
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
            // Set the border for table cells
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
        };

        // Add 1st row to table
        Aspose.Pdf.Row row1 = table.Rows.Add();
        for (int cellCount = 1; cellCount <5; cellCount++)
        {
            // Add table cells
            row1.Cells.Add($"Test 1 {cellCount}");
        }

        // Add 2nd row to table
        Aspose.Pdf.Row row2 = table.Rows.Add();
        row2.Cells.Add($"Test 2 1");
        var cell = row2.Cells.Add($"Test 2 2");
        cell.ColSpan = 2;
        row2.Cells.Add($"Test 2 4");

        // Add 3rd row to table
        Aspose.Pdf.Row row3 = table.Rows.Add();
        row4.Cells.Add("Test 3 1");
        row4.Cells.Add("Test 3 2");
        row4.Cells.Add("Test 3 3");
        row4.Cells.Add("Test 3 4");

        // Add 4th row to table
        Aspose.Pdf.Row row4 = table.Rows.Add();
        row3.Cells.Add("Test 4 1");
        cell = row3.Cells.Add("Test 4 2");
        cell.RowSpan = 2;
        row3.Cells.Add("Test 4 3");
        row3.Cells.Add("Test 4 4");

        // Add 5th row to table
        row4 = table.Rows.Add();
        row4.Cells.Add("Test 5 1");
        row4.Cells.Add("Test 5 3");
        row4.Cells.Add("Test 5 4");

        // Add table object to first page of input document
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddTableRowColSpan_out.pdf");
    }
}
```

아래 실행 코드의 결과는 다음 이미지에 묘사된 테이블입니다:

![ColSpan 및 RowSpan 데모](colspan_rowspan.png)

## 테두리, 여백 및 패딩 작업하기

테이블에 대한 테두리 스타일, 여백 및 셀 패딩을 설정하는 기능도 지원합니다. 더 기술적인 세부 사항으로 들어가기 전에, 아래 다이어그램에 제시된 테두리, 여백 및 패딩의 개념을 이해하는 것이 중요합니다:

![테두리, 여백 및 패딩](set-border-style-margins-and-padding-of-table_1.png)

위 그림에서 테이블, 행 및 셀의 테두리가 겹치는 것을 볼 수 있습니다. Aspose.PDF를 사용하면 테이블에 여백이 있을 수 있고 셀에 패딩이 있을 수 있습니다. 셀 여백을 설정하려면 셀 패딩을 설정해야 합니다.

### 테두리

테이블, [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) 및 [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell) 객체의 테두리를 설정하려면 Table.Border, Row.Border 및 Cell.Border 속성을 사용합니다. 셀 테두리는 [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) 또는 Row 클래스의 DefaultCellBorder 속성을 사용하여 설정할 수도 있습니다. 위에서 논의된 모든 테두리 관련 속성은 Row 클래스의 인스턴스에 할당되며, 이는 생성자를 호출하여 생성됩니다. Row 클래스에는 테두리를 사용자 정의하는 데 필요한 거의 모든 매개변수를 사용하는 여러 오버로드가 있습니다.

### 여백 또는 패딩

셀 패딩은 Table 클래스의 [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) 속성을 사용하여 관리할 수 있습니다. 모든 패딩 관련 속성은 `Left`, `Right`, `Top` 및 `Bottom` 매개변수에 대한 정보를 가져와 사용자 정의 여백을 생성하는 [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo) 클래스의 인스턴스에 할당됩니다.

다음 예제에서는 셀 테두리의 너비를 0.1 포인트로 설정하고, 테이블 테두리의 너비를 1 포인트로 설정하며, 셀 패딩을 5 포인트로 설정합니다.

![PDF 테이블의 여백 및 테두리](margin-border.png)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddMarginsOrPadding()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page page = document.Pages.Add();
        // Instantiate a table object
        Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(tab1);
        // Set with column widths of the table
        tab1.ColumnWidths = "50 50 50";
        // Set default cell border using BorderInfo object
        tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
        // Set table border using another customized BorderInfo object
        tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
        // Create MarginInfo object and set its left, bottom, right and top margins
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 5f;
        margin.Left = 5f;
        margin.Right = 5f;
        margin.Bottom = 5f;
        // Set the default cell padding to the MarginInfo object
        tab1.DefaultCellPadding = margin;
        // Create rows in the table and then cells in the rows
        Aspose.Pdf.Row row1 = tab1.Rows.Add();
        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add();
        Aspose.Pdf.Text.TextFragment mytext = new Aspose.Pdf.Text.TextFragment("col3 with large text string");
        // Row1.Cells.Add("col3 with large text string to be placed inside cell");
        row1.Cells[2].Paragraphs.Add(mytext);
        row1.Cells[2].IsWordWrapped = false;
        // Row1.Cells[2].Paragraphs[0].FixedWidth= 80;
        Aspose.Pdf.Row row2 = tab1.Rows.Add();
        row2.Cells.Add("item1");
        row2.Cells.Add("item2");
        row2.Cells.Add("item3");
        // Save PDF document
        document.Save(dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

모서리가 둥근 테이블을 만들려면 BorderInfo 클래스의 `RoundedBorderRadius` 값을 사용하고 테이블 모서리 스타일을 둥글게 설정합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTableWithRoundCorner()
{
    Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

    Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
    graph.Color = Aspose.Pdf.Color.Red;
    // Create a blank BorderInfo object
    Aspose.Pdf.BorderInfo bInfo = new Aspose.Pdf.BorderInfo(BorderSide.All, graph);
    // Set the border a rounder border where radius of round is 15
    bInfo.RoundedBorderRadius = 15;
    // Set the table Corner style as Round.
    tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
    // Set the table border information
    tab1.Border = bInfo;
}
```

## 테이블에 다양한 자동 맞춤 설정 적용하기

Microsoft Word와 같은 시각적 에이전트를 사용하여 테이블을 만들 때, 테이블을 원하는 너비에 자동으로 크기를 조정하기 위해 자동 맞춤 옵션 중 하나를 사용하는 경우가 많습니다. 예를 들어, AutoFit to Window 옵션을 사용하여 테이블을 페이지의 너비에 맞추고, AutoFit to Contents 옵션을 사용하여 각 셀이 내용을 수용하기 위해 성장하거나 축소되도록 할 수 있습니다.

기본적으로 Aspose.PDF는 `Customized` 값으로 `ColumnAdjustment`를 사용하여 새 테이블을 삽입합니다. 테이블은 페이지에서 사용 가능한 너비에 맞춰 크기가 조정됩니다. 이러한 테이블이나 기존 테이블의 크기 조정 동작을 변경하려면 Table.autoFit(int) 메서드를 호출할 수 있습니다. 이 메서드는 테이블에 적용되는 자동 맞춤 유형을 정의하는 AutoFitBehavior 열거형을 수락합니다.

Microsoft Word와 마찬가지로 자동 맞춤 메서드는 실제로 테이블에 여러 속성을 한 번에 적용하는 단축키입니다. 이러한 속성은 실제로 테이블에 관찰된 동작을 부여합니다. 각 자동 맞춤 옵션에 대한 이러한 속성에 대해 논의할 것입니다. 다음 테이블을 사용하고 다양한 자동 맞춤 설정을 적용하여 시연하겠습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAutoFitToWindow()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page sec1 = document.Pages.Add();

        // Instantiate a table object
        Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
        // Add the table in paragraphs collection of the desired section
        sec1.Paragraphs.Add(tab1);

        // Set with column widths of the table
        tab1.ColumnWidths = "50 50 50";
        tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

        // Set default cell border using BorderInfo object
        tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

        // Set table border using another customized BorderInfo object
        tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
        // Create MarginInfo object and set its left, bottom, right and top margins
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 5f;
        margin.Left = 5f;
        margin.Right = 5f;
        margin.Bottom = 5f;

        // Set the default cell padding to the MarginInfo object
        tab1.DefaultCellPadding = margin;

        // Create rows in the table and then cells in the rows
        Aspose.Pdf.Row row1 = tab1.Rows.Add();
        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add("col3");
        Aspose.Pdf.Row row2 = tab1.Rows.Add();
        row2.Cells.Add("item1");
        row2.Cells.Add("item2");
        row2.Cells.Add("item3");

        // Save PDF document
        document.Save(dataDir + "AutoFitToWindow_out.pdf");
    }
}
```

### 테이블 너비 가져오기

때때로 테이블 너비를 동적으로 가져와야 할 필요가 있습니다. Aspose.PDF.Table 클래스에는 이를 위한 [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) 메서드가 있습니다. 예를 들어, 테이블 열 너비를 명시적으로 설정하지 않고 [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment)를 AutoFitToContent로 설정한 경우, 다음과 같이 테이블 너비를 가져올 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTableWidth()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page page = document.Pages.Add();
        // Initialize new table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table
        {
            ColumnAdjustment = ColumnAdjustment.AutoFitToContent
        };
        // Add row in table
        Aspose.Pdf.Row row = table.Rows.Add();
        // Add cell in table
        Aspose.Pdf.Cell cell = row.Cells.Add("Cell 1 text");
        cell = row.Cells.Add("Cell 2 text");
        // Get table width
        Console.WriteLine(table.GetWidth());
    }
}
```

## 테이블 셀에 SVG 이미지 추가하기

Aspose.PDF for .NET은 PDF 파일에 테이블 셀을 추가하는 기능을 지원합니다. 테이블을 생성할 때 셀에 텍스트나 이미지를 추가할 수 있습니다. 또한 API는 SVG 파일을 PDF 형식으로 변환하는 기능도 제공합니다. 이러한 기능의 조합을 사용하여 SVG 이미지를 로드하고 테이블 셀에 추가할 수 있습니다.

다음 코드 스니펫은 테이블 인스턴스를 생성하고 테이블 셀 안에 SVG 이미지를 추가하는 단계를 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddSvgObjectToTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create an image instance
        Aspose.Pdf.Image img = new Aspose.Pdf.Image();
        // Set image type as SVG
        img.FileType = Aspose.Pdf.ImageFileType.Svg;
        // Path for source file
        img.File = dataDir + "SVGToPDF.svg";
        // Set width for image instance
        img.FixWidth = 50;
        // Set height for image instance
        img.FixHeight = 50;
        // Create table instance
        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        // Set width for table cells
        table.ColumnWidths = "100 100";
        // Create row object and add it to table instance
        Aspose.Pdf.Row row = table.Rows.Add();
        // Create cell object and add it to row instance
        Aspose.Pdf.Cell cell = row.Cells.Add();
        // Add textfragment to paragraphs collection of cell object
        cell.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("First cell"));
        // Add another cell to row object
        cell = row.Cells.Add();
        // Add SVG image to paragraphs collection of recently added cell instance
        cell.Paragraphs.Add(img);
        // Create page object and add it to pages collection of document instance
        Aspose.Pdf.Page page = document.Pages.Add();
        // Add table to paragraphs collection of page object
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddSVGObjectToTable_out.pdf");
    }
}
```

## 테이블 내에서 HTML 태그 사용하기

때때로 HTML 태그가 포함된 데이터베이스 내용을 가져와서 Table 객체에 내용을 가져와야 할 필요가 있습니다. 내용을 가져올 때, PDF 문서 내에서 HTML 태그가 적절하게 렌더링되어야 합니다. 이러한 요구 사항을 달성하기 위해 ImprotDataTable() 메서드를 개선했습니다:

{{% alert color="primary" %}}

테이블 요소 내에서 HTML 태그를 사용하는 것은 문서 생성 시간을 증가시킵니다. API는 HTML 태그를 적절하게 처리하고 출력 PDF 문서에 렌더링해야 하기 때문입니다.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHtmlInsideTableCell()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    DataTable dt = new DataTable("Employee");
    dt.Columns.Add("data", System.Type.GetType("System.String"));

    DataRow dr = dt.NewRow();
    dr[0] = "<li>Department of Emergency Medicine: 3400 Spruce Street Ground Silverstein Bldg Philadelphia PA 19104-4206</li>";
    dt.Rows.Add(dr);
    dr = dt.NewRow();
    dr[0] = "<li>Penn Observation Medicine Service: 3400 Spruce Street Ground Floor Donner Philadelphia PA 19104-4206</li>";
    dt.Rows.Add(dr);
    dr = dt.NewRow();
    dr[0] = "<li>UPHS/Presbyterian - Dept. of Emergency Medicine: 51 N. 39th Street . Philadelphia PA 19104-2640</li>";
    dt.Rows.Add(dr);

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Initializes a new instance of the Table
        Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
        //Set column widths of the table
        tableProvider.ColumnWidths = "400 50 ";
        // Set the table border color as LightGray
        tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Set the border for table cells
        tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 2.5F;
        margin.Left = 2.5F;
        margin.Bottom = 1.0F;
        tableProvider.DefaultCellPadding = margin;

        tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

        page.Paragraphs.Add(tableProvider);

        // Save PDF document
        document.Save(dataDir + "HTMLInsideTableCell_out.pdf");
    }
}
```

## 테이블의 행 사이에 페이지 나누기 삽입하기

기본 동작으로, PDF 파일 내에서 테이블을 생성할 때, 테이블이 하단 여백에 도달하면 테이블이 다음 페이지로 흐릅니다. 그러나 특정 수의 행이 테이블에 추가될 때 강제로 페이지 나누기를 삽입해야 할 필요가 있을 수 있습니다. 다음 코드 스니펫은 테이블에 10개의 행이 추가될 때 페이지 나누기를 삽입하는 단계를 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPageBreak()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create table instance
        Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
        // Set border style for table
        tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
        // Set default border style for table with border color as Red
        tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
        // Specify table columsn widht
        tab.ColumnWidths = "100 100";
        // Create a loop to add 200 rows for table
        for (int counter = 0; counter <= 200; counter++)
        {
            Aspose.Pdf.Row row = new Aspose.Pdf.Row();
            tab.Rows.Add(row);
            Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
            cell1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Cell " + counter + ", 0"));
            row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
            cell2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Cell " + counter + ", 1"));
            row.Cells.Add(cell2);
            // When 10 rows are added, render new row in new page
            if (counter % 10 == 0 && counter != 0)
            {
                row.IsInNewPage = true;
            }
        }
        // Add table to paragraphs collection of PDF file
        page.Paragraphs.Add(tab);

        // Save PDF document
        document.Save(dataDir + "InsertPageBreak_out.pdf");
    }
}
```

## 새 페이지에 테이블 렌더링하기

기본적으로 단락은 페이지 객체의 단락 컬렉션에 추가됩니다. 그러나 이전에 추가된 단락 수준 객체 바로 뒤가 아니라 새 페이지에 테이블을 렌더링할 수 있습니다.

### 샘플: C#을 사용하여 새 페이지에 테이블 렌더링하기

새 페이지에 테이블을 렌더링하려면 BaseParagraph 클래스의 [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) 속성을 사용합니다. 다음 코드 스니펫은 그 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTableOnNewPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.PageInfo pageInfo = document.PageInfo;
        Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

        marginInfo.Left = 37;
        marginInfo.Right = 37;
        marginInfo.Top = 37;
        marginInfo.Bottom = 37;

        pageInfo.IsLandscape = true;

        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        table.ColumnWidths = "50 100";
        // Add page
        Page curPage = document.Pages.Add();
        for (int i = 1; i <= 120; i++)
        {
            Aspose.Pdf.Row row = table.Rows.Add();
            row.FixedRowHeight = 15;
            Aspose.Pdf.Cell cell1 = row.Cells.Add();
            cell1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Content 1"));
            Aspose.Pdf.Cell cell2 = row.Cells.Add();
            cell2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("HHHHH"));
        }
        Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
        paragraphs.Add(table);

        Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
        table.ColumnWidths = "100 100";
        for (int i = 1; i <= 10; i++)
        {
            Aspose.Pdf.Row row = table1.Rows.Add();
            Aspose.Pdf.Cell cell1 = row.Cells.Add();
            cell1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("LAAAAAAA"));
            Aspose.Pdf.Cell cell2 = row.Cells.Add();
            cell2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("LAAGGGGGG"));
        }
        table1.IsInNewPage = true;
        // Keep table 1 to next page
        paragraphs.Add(table1);
        // Save PDF document
        document.Save(dataDir + "AddTableOnNewPage_out.pdf");
    }
}
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
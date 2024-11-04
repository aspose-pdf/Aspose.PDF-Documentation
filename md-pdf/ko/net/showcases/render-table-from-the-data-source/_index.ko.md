---
title: 데이터 소스에서 테이블 렌더링
linktitle: 데이터 소스에서 테이블 렌더링
type: docs
weight: 30
url: /net/render-table-from-the-data-source/
description: 이 페이지는 Aspose.PDF 라이브러리를 사용하여 데이터 소스에서 테이블을 렌더링하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF를 사용하면 PdfLightTable 클래스를 사용하여 DataSet, 데이터 테이블, 배열 및 IEnumerable 객체에서 데이터 소스와 함께 테이블을 생성할 수 있습니다.

[테이블 클래스](https://reference.aspose.com/pdf/net/aspose.pdf/table)는 테이블을 처리하는 데 사용됩니다. 이 클래스는 [행](https://reference.aspose.com/pdf/net/aspose.pdf/rows)과 [셀](https://reference.aspose.com/pdf/net/aspose.pdf/cell)을 사용하여 문서에 테이블을 생성하고 배치할 수 있는 기능을 제공합니다. 따라서 테이블을 생성하려면 필요한 수의 행을 추가하고 적절한 수의 셀로 채워야 합니다.

다음 예제는 4x10 테이블을 생성합니다.

```csharp
var table = new Table
    {
        // 테이블의 열 자동 너비 설정
        ColumnWidths = "25% 25% 25% 25%",
        // 셀 패딩 설정
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // 왼쪽 아래 오른쪽 위
        // 테이블 테두리 색상을 녹색으로 설정
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // 테이블 셀의 테두리를 검정색으로 설정
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // 테이블에 행 추가
        var row = table.Rows.Add();
        // 테이블 셀 추가
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // 입력 문서의 첫 페이지에 테이블 객체 추가
    document.Pages[1].Paragraphs.Add(table);
```
Table 객체를 초기화할 때 최소한의 스킨 설정을 사용했습니다:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - 열의 너비(기본값);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - 테이블 셀의 기본 여백;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - 테이블 테두리 속성(스타일, 두께, 색상);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - 셀 테두리 속성(스타일, 두께, 색상).

## 객체 배열에서 데이터 내보내기

Table 클래스는 ADO.NET 데이터 소스와 상호 작용하기 위한 메소드를 제공합니다 - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) 및 [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).

이 객체들이 MVC 템플릿에서 작업하는 데 편리하지 않다는 전제 하에, 우리는 간단한 예제로 제한할 것입니다. 이 예제에서 (50번째 줄) ImportDataTable 메서드가 호출되며 매개변수로 DataTable 인스턴스와 헤더 플래그 및 데이터 출력을 위한 초기 위치(행/열)와 같은 추가 설정을 받습니다.

```csharp
// PDF 문서 새로 생성
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// 보고서 제목을 위한 TextFragment의 새 인스턴스 초기화
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // 테이블의 열 너비 설정
    ColumnWidths = "25% 25% 25% 25%",
    // 셀 패딩 설정
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // 왼쪽 아래 오른쪽 위
    // 테이블 테두리 색상을 녹색으로 설정
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // 테이블 셀의 테두리를 검정색으로 설정
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("config.json에 연결 문자열이 없습니다.");

var resultTable = new DataTable();

using (var conn = new SqlConnection(connectionString))
{
    const string sql = "SELECT * FROM Tennats";
    using (var cmd = new SqlCommand(sql, conn))
    {
        using (var adapter = new SqlDataAdapter(cmd))
        {
            adapter.Fill(resultTable);
        }
    }
}

table.ImportDataTable(resultTable,true,1,1);

// 문서의 첫 페이지에 테이블 객체 추가
document.Pages[1].Paragraphs.Add(table);
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "demotable2.pdf"
    };
}
```


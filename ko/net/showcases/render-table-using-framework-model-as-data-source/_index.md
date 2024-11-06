---
title: Entity Framework를 사용하여 테이블 렌더링
linktitle: Entity Framework를 사용하여 테이블 렌더링
type: docs
weight: 40
url: ko/net/render-table-using-entity-framework-model-as-data-source/
description: 이 문서는 Aspose.PDF for .NET을 사용하여 Entity Framework 모델을 데이터 소스로 사용하여 테이블을 렌더링하는 방법을 보여줍니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

때때로 데이터베이스에서 PDF 문서로 데이터를 내보내는 것이 최근 인기 있는 HTML에서 PDF로의 변환 스키마를 사용하지 않고 더 편리할 수 있는 작업이 여러 가지 있습니다.

이 문서는 Aspose.PDF for .NET을 사용하여 PDF 문서를 생성하는 방법을 보여줄 것입니다.

## Aspose.PDF로 PDF 생성의 기초

Aspose.PDF에서 가장 중요한 클래스 중 하나는 [Document 클래스](https://reference.aspose.com/pdf/net/aspose.pdf/document)입니다. 이 클래스는 PDF 렌더링 엔진입니다. PDF 구조를 제시하기 위해 Aspose.PDF 라이브러리는 다음과 같은 문서-페이지 모델을 사용합니다:

* Document - PDF 문서의 속성을 포함하며 페이지 컬렉션을 포함합니다;
* 문서 - PDF 문서의 속성과 페이지 모음을 포함합니다.
* 페이지 - 특정 페이지의 속성과 이 페이지와 관련된 다양한 요소 모음을 포함합니다.

따라서 Aspose.PDF로 PDF 문서를 생성하려면 다음 단계를 따라야 합니다:

1. 문서 객체 생성;
1. 문서 객체에 페이지(페이지 객체) 추가;
1. 페이지에 배치될 객체 생성(예: 텍스트 조각, 테이블 등)
1. 생성된 항목을 페이지의 해당 컬렉션에 추가(이 경우 문단 컬렉션일 것입니다);
1. 문서를 PDF 파일로 저장.

```csharp
// 1단계
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

// 2단계
var pdfPage = document.Pages.Add();

// 3단계
var textFragment = new TextFragment(reportTitle);
// ..........................................

var table = new Table
{
    // .................................
};

// 4단계
pdfPage.Paragraphs.Add(textFragment);
pdfPage.Paragraphs.Add(table);

// 5단계
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
가장 일반적인 문제는 데이터를 테이블 형식으로 출력하는 것입니다. [Table 클래스](https://reference.aspose.com/pdf/net/aspose.pdf/table)는 테이블을 처리하는 데 사용됩니다. 이 클래스를 사용하면 테이블을 생성하고 [행](https://reference.aspose.com/pdf/net/aspose.pdf/rows)과 [셀](https://reference.aspose.com/pdf/net/aspose.pdf/cell)을 사용하여 문서에 배치할 수 있습니다. 따라서 테이블을 생성하려면 필요한 수의 행을 추가하고 적절한 수의 셀로 채워야 합니다.

다음 예제는 4x10 테이블을 만듭니다.

```csharp
var table = new Table
    {
        // 테이블의 열 자동 너비 설정
        ColumnWidths = "25% 25% 25% 25%",
        // 셀 패딩 설정
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // 왼쪽 아래 오른쪽 위
        // 테이블 테두리 색상을 녹색으로 설정
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // 테이블 셀의 테두리를 검은색으로 설정
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

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - 기본적으로 열의 너비;
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - 테이블 셀을 위한 기본 필드;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - 테이블 프레임 속성 (스타일, 두께, 색상);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - 셀 프레임의 속성 (스타일, 두께, 색상).

결과적으로, 폭이 같은 4x10 테이블을 얻게 됩니다.

![Table 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## ADO.NET 객체에서 데이터 내보내기

Table 클래스는 ADO.NET 데이터 소스와 상호 작용하기 위한 메소드를 제공합니다 - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) 및 [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
Table 클래스는 ADO.NET 데이터 소스와 상호작용하는 메소드를 제공합니다 - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) 및 [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
이 객체들이 MVC 템플릿에서 작업하기에는 적합하지 않다는 전제 하에, 간단한 예제로 제한하겠습니다. 이 예제에서는 (50번째 줄에서) ImportDataTable 메소드가 호출되어 DataTable 인스턴스와 헤더 플래그, 데이터 출력을 위한 초기 위치(행/열) 등의 추가 설정을 매개변수로 받습니다.

```csharp
// 새 PDF 문서 생성
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
    throw new ArgumentException("config.json에 연결 문자열이 없습니다");

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

// 테이블 객체를 입력 문서의 첫 페이지에 추가
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
## 엔티티 프레임워크에서 데이터 내보내기

현대 .NET에서 더욱 관련이 있는 것은 ORM 프레임워크에서 데이터를 가져오는 것입니다. 이 경우, 간단한 리스트 또는 그룹화된 데이터에서 데이터를 가져오기 위해 Table 클래스를 확장 메소드로 확장하는 것이 좋은 생각입니다. 가장 인기 있는 ORM 중 하나인 엔티티 프레임워크의 예를 들어 보겠습니다.

```csharp
public static class PdfHelper
    {
        public static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
        {
            var headRow = table.Rows.Add();

            var props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
                headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
            }

            foreach (var item in data)
            {
                // Add row to table
                var row = table.Rows.Add();
                // Add table cells
                foreach (var t in props)
                {
                    var dataItem = t.GetValue(item, null);
                    if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                        switch (dataType.DataType)
                        {

                            case DataType.Currency:
                                row.Cells.Add(string.Format("{0:C}", dataItem));
                                break;
                            case DataType.Date:
                                var dateTime = (DateTime)dataItem;
                                if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                {
                                    row.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                        ? dateTime.ToShortDateString()
                                        : string.Format(df.DataFormatString, dateTime));
                                }
                                break;
                            default:
                                row.Cells.Add(dataItem.ToString());
                                break;
                        }
                    else
                    {
                        row.Cells.Add(dataItem.ToString());
                    }
                }
            }
        }
        public static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
        {
            var headRow = table.Rows.Add();           
            var props = typeof(TValue).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
               headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);               
            }

            foreach (var group in groupedData)
            {
                // Add group row to table
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // Add data row to table
                    var dataRow = table.Rows.Add();
                    // Add cells
                    foreach (var t in props)
                    {
                        var dataItem = t.GetValue(item, null);

                        if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                            switch (dataType.DataType)
                            {
                                case DataType.Currency:
                                    dataRow.Cells.Add(string.Format("{0:C}", dataItem));
                                    break;
                                case DataType.Date:
                                    var dateTime = (DateTime)dataItem;
                                    if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                    {
                                        dataRow.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                            ? dateTime.ToShortDateString()
                                            : string.Format(df.DataFormatString, dateTime));
                                    }
                                    break;
                                default:
                                    dataRow.Cells.Add(dataItem.ToString());
                                    break;
                            }
                        else
                        {
                            dataRow.Cells.Add(dataItem.ToString());
                        }
                    }
                }
            }
        }
    }
```
데이터 주석 속성은 종종 모델을 설명하고 테이블 생성을 돕기 위해 사용됩니다. 따라서 ImportEntityList에 대해 다음 테이블 생성 알고리즘이 선택되었습니다:

* 12-18행: 헤더 행을 구성하고 "DisplayAttribute가 존재하면 그 값을 사용하고, 그렇지 않으면 속성 이름을 사용" 규칙에 따라 헤더 셀을 추가합니다.
* 50-53행: 데이터 행을 구성하고 "DataTypeAttribute 속성이 정의된 경우, 추가 디자인 설정이 필요한지 검토하고, 그렇지 않으면 데이터를 문자열로 변환하여 셀에 추가합니다." 규칙에 따라 행 셀을 추가합니다.

이 예시에서는 DataType.Currency(32-34행) 및 DataType.Date(35-43행)에 대한 추가 사용자 정의가 이루어졌지만, 필요에 따라 다른 사용자 정의를 추가할 수 있습니다.
ImportGroupedData 메서드의 알고리즘은 이전과 거의 동일합니다. 추가적으로 GroupViewModel 클래스가 사용되어 그룹화된 데이터를 저장합니다.

```csharp
using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
우리가 그룹을 처리하기 때문에, 먼저 키 값에 대한 라인을 생성합니다(66-71 줄), 그리고 그 후에 이 그룹의 라인들을 생성합니다.

---
title: Entity Framework로 테이블 렌더링
linktitle: Entity Framework로 테이블 렌더링
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/render-table-using-entity-framework-model-as-data-source/
description: 이 문서에서는 Entity Framework 모델을 데이터 소스로 사용하여 테이블을 렌더링하는 방법을 보여줍니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render table with Entity Framework",
    "alternativeHeadline": "Render PDF from Entity Framework Data Easily",
    "abstract": "Aspose.PDF for .NET을 사용하여 Entity Framework 모델에서 PDF 문서로 테이블을 원활하게 렌더링할 수 있는 새로운 기능을 소개합니다. 이 기능은 ORM 프레임워크에서 데이터를 효율적으로 가져와 사용자 정의 속성과 형식 옵션을 갖춘 잘 구조화된 테이블을 생성하여 데이터 시각화를 단순화합니다. HTML 기반 변환 없이 깔끔하고 전문적인 PDF 출력을 제공하는 이 강력한 통합으로 보고서 기능을 향상시키십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1540",
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
    "url": "/net/render-table-using-entity-framework-model-as-data-source/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-table-using-entity-framework-model-as-data-source/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

어떤 이유로 데이터베이스에서 PDF 문서로 데이터를 내보내는 것이 최근에 인기 있는 HTML에서 PDF 변환 방식 없이 더 편리할 때가 있습니다.

이 문서에서는 Aspose.PDF for .NET을 사용하여 PDF 문서를 생성하는 방법을 보여줍니다.

## Aspose.PDF로 PDF 생성의 기초

Aspose.PDF에서 가장 중요한 클래스 중 하나는 [Document class](https://reference.aspose.com/pdf/net/aspose.pdf/document)입니다. 이 클래스는 PDF 렌더링 엔진입니다. PDF 구조를 표현하기 위해 Aspose.PDF 라이브러리는 Document-Page 모델을 사용합니다. 여기서:

* Document - 페이지 컬렉션을 포함한 PDF 문서의 속성을 포함합니다.
* Page - 특정 페이지의 속성과 이 페이지와 관련된 다양한 요소 컬렉션을 포함합니다.

따라서 Aspose.PDF로 PDF 문서를 생성하려면 다음 단계를 따라야 합니다:

1. Document 객체를 생성합니다.
1. Document 객체에 페이지(Page 객체)를 추가합니다.
1. 페이지에 배치할 객체를 생성합니다(예: 텍스트 조각, 테이블 등).
1. 생성된 항목을 페이지의 해당 컬렉션에 추가합니다(우리의 경우 단락 컬렉션이 될 것입니다).
1. 문서를 PDF 파일로 저장합니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document
           {
               PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
           })
    {
        // Add page
        var page = document.Pages.Add();

        var textFragment = new Aspose.Pdf.Text.TextFragment(reportTitle);

        var table = new Aspose.Pdf.Table
        {
            // .................................
        };

        page.Paragraphs.Add(textFragment);
        page.Paragraphs.Add(table);

        using (var streamOut = new MemoryStream())
        {
            // Save PDF document
            document.Save(streamOut);

            return new FileContentResult(streamOut.ToArray(), "application/pdf")
            {
                FileDownloadName = "tenants.pdf"
            };
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };

    // Add page
    var page = document.Pages.Add();

    var textFragment = new Aspose.Pdf.Text.TextFragment(reportTitle);

    var table = new Aspose.Pdf.Table
    {
        // .................................
    };

    page.Paragraphs.Add(textFragment);
    page.Paragraphs.Add(table);

    using var streamOut = new MemoryStream();

    // Save PDF document
    document.Save(streamOut);

    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
{{< /tab >}}
{{< /tabs >}}

가장 일반적인 문제는 테이블 형식으로 데이터를 출력하는 것입니다. [Table class](https://reference.aspose.com/pdf/net/aspose.pdf/table)는 테이블을 처리하는 데 사용됩니다. 이 클래스는 테이블을 생성하고 문서에 배치할 수 있는 기능을 제공합니다. [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows)와 [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell)를 사용합니다. 따라서 테이블을 생성하려면 필요한 수의 행을 추가하고 적절한 수의 셀로 채워야 합니다.

다음 예제는 4x10 테이블을 생성합니다.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        var table = new Aspose.Pdf.Table
        {
            // Set column auto widths of the table
            ColumnWidths = "25% 25% 25% 25%",

            // Set cell padding
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top

            // Set the table border color as Green
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),

            // Set the border for table cells as Black
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
        };

        for (var rowCount = 0; rowCount < 10; rowCount++)
        {
            // Add row to table
            var row = table.Rows.Add();

            // Add table cells
            for (int i = 0; i < 4; i++)
            {
                row.Cells.Add($"Cell ({i + 1}, {rowCount + 1})");
            }
        }

        // Add table object to first page of input document
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddTable_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page
    var page = document.Pages.Add();

    var table = new Aspose.Pdf.Table
    {
        // Set column auto widths of the table
        ColumnWidths = "25% 25% 25% 25%",

        // Set cell padding
        DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top

        // Set the table border color as Green
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),

        // Set the border for table cells as Black
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
    };

    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Add row to table
        var row = table.Rows.Add();

        // Add table cells
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i + 1}, {rowCount + 1})");
        }
    }

    // Add table object to first page of input document
    page.Paragraphs.Add(table);

    // Save PDF document
    document.Save(dataDir + "AddTable_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Table 객체를 초기화할 때 최소한의 스킨 설정이 사용되었습니다:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - 열의 너비(기본값).
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - 테이블 셀의 기본 필드.
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - 테이블 프레임 속성(스타일, 두께, 색상).
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - 셀 프레임의 속성(스타일, 두께, 색상).

결과적으로 우리는 동일한 너비의 열을 가진 4x10 테이블을 얻습니다.

![Table 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## ADO.NET 객체에서 데이터 내보내기

Table 클래스는 ADO.NET 데이터 소스와 상호작용하기 위한 메서드를 제공합니다 - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) 및 [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview). 첫 번째 메서드는 DataTable에서 데이터를 가져오고, 두 번째는 DataView에서 가져옵니다.
이 객체들이 MVC 템플릿에서 작업하기에 그리 편리하지 않다는 전제를 두고 간단한 예제로 제한하겠습니다. 이 예제(50행)에서는 ImportDataTable 메서드를 호출하고 DataTable 인스턴스와 헤더 플래그 및 데이터 출력을 위한 초기 위치(행/열)와 같은 추가 설정을 매개변수로 받습니다.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    })
    {
        var table = new Aspose.Pdf.Table
        {
            // Set column widths of the table
            ColumnWidths = "25% 25% 25% 25%",
            // Set cell padding
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
            // Set the table border color as Green
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),
            // Set the border for table cells as Black
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
        };

        var configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("config.json", false)
            .Build();

        var connectionString = configuration.GetSection("connectionString").Value;

        if (string.IsNullOrEmpty(connectionString))
        {
            throw new ArgumentException("No connection string in config.json");
        }

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

        table.ImportDataTable(resultTable, true, 1, 1);

        // Add table object to first page of input document
        document.Pages[1].Paragraphs.Add(table);

        using (var streamOut = new MemoryStream())
        {
            // Save PDF document
            document.Save(streamOut);

            return new FileContentResult(streamOut.ToArray(), "application/pdf")
            {
                FileDownloadName = "demotable2.pdf"
            };
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };

    var table = new Aspose.Pdf.Table
    {
        // Set column widths of the table
        ColumnWidths = "25% 25% 25% 25%",
        // Set cell padding
        DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
        // Set the table border color as Green
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),
        // Set the border for table cells as Black
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
    };

    var configuration = new ConfigurationBuilder()
        .SetBasePath(Directory.GetCurrentDirectory())
        .AddJsonFile("config.json", false)
        .Build();

    var connectionString = configuration.GetSection("connectionString").Value;

    if (string.IsNullOrEmpty(connectionString))
    {
        throw new ArgumentException("No connection string in config.json");
    }

    var resultTable = new DataTable();

    using var conn = new SqlConnection(connectionString);

    const string sql = "SELECT * FROM Tennats";

    using var cmd = new SqlCommand(sql, conn);

    using var adapter = new SqlDataAdapter(cmd);
    
    adapter.Fill(resultTable);

    table.ImportDataTable(resultTable, true, 1, 1);

    // Add table object to first page of input document
    document.Pages[1].Paragraphs.Add(table);

    using var streamOut = new MemoryStream();
    
    // Save PDF document
    document.Save(streamOut);

    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };
}
```
{{< /tab >}}
{{< /tabs >}}

## Entity Framework에서 데이터 내보내기

현대 .NET에 더 관련성이 높은 것은 ORM 프레임워크에서 데이터를 가져오는 것입니다. 이 경우, 간단한 목록이나 그룹화된 데이터에서 데이터를 가져오기 위한 확장 메서드로 Table 클래스를 확장하는 것이 좋습니다. 가장 인기 있는 ORM 중 하나인 Entity Framework에 대한 예를 들어 보겠습니다.

```csharp
public static class PdfHelper
{
    private static void ImportEntityList<TSource>(this Aspose.Pdf.Table table, IList<TSource> data)
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

    private static void ImportGroupedData<TKey, TValue>(this Aspose.Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
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
            cell.BackgroundColor = Aspose.Pdf.Color.DarkGray;
            cell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.White;

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

데이터 주석 속성은 모델을 설명하는 데 자주 사용되며 테이블을 생성하는 데 도움을 줍니다. 따라서 ImportEntityList에 대한 다음 테이블 생성 알고리즘이 선택되었습니다:

* 12-18행: 헤더 행을 구축하고 "DisplayAttribute가 있으면 해당 값을 가져오고, 그렇지 않으면 속성 이름을 가져온다"는 규칙에 따라 헤더 셀을 추가합니다.
* 50-53행: 데이터 행을 구축하고 "DataTypeAttribute가 정의되어 있으면 추가 디자인 설정이 필요한지 확인하고, 그렇지 않으면 데이터를 문자열로 변환하여 셀에 추가한다"는 규칙에 따라 행 셀을 추가합니다.

이 예제에서는 DataType.Currency(32-34행) 및 DataType.Date(35-43행)에 대해 추가 사용자 정의가 이루어졌지만 필요에 따라 다른 사용자 정의를 추가할 수 있습니다.
ImportGroupedData 메서드의 알고리즘은 이전 것과 거의 동일합니다. 그룹화된 데이터를 저장하기 위해 추가 GroupViewModel 클래스가 사용됩니다.

```csharp
using System.Collections.Generic;
public class GroupViewModel<K,T>
{
    public K Key;
    public IEnumerable<T> Values;
}
```

우리가 그룹을 처리하므로 먼저 키 값에 대한 행을 생성하고(66-71행), 그 다음에 이 그룹의 행을 생성합니다.
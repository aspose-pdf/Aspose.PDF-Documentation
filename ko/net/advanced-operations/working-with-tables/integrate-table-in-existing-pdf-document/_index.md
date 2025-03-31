---
title: 데이터 소스 PDF와 테이블 통합
linktitle: 테이블 통합
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/integrate-table/
description: 이 문서에서는 PDF 테이블을 통합하는 방법을 보여줍니다. 데이터베이스와 테이블을 통합하고 테이블이 현재 페이지에서 분할될지 여부를 결정합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Integrate Table with Data Sources PDF",
    "alternativeHeadline": "Integrate PDF Tables with Data Sources Seamlessly",
    "abstract": "데이터 소스 PDF와 테이블 통합 기능은 개발자가 데이터베이스 및 엔터티 프레임워크를 포함한 다양한 소스에서 PDF 테이블로 데이터를 원활하게 가져올 수 있도록 합니다. 페이지 매김을 결정하는 기능과 반복 열을 지원하여 이 기능은 문서의 무결성을 유지하면서 데이터 프레젠테이션을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2201",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2024-11-26",
    "description": "이 문서에서는 PDF 테이블을 통합하는 방법을 보여줍니다. 데이터베이스와 테이블을 통합하고 테이블이 현재 페이지에서 분할될지 여부를 결정합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 데이터베이스와 테이블 통합

데이터베이스는 데이터를 저장하고 관리하기 위해 구축됩니다. 프로그래머가 데이터베이스에서 데이터를 가져와 다양한 객체를 채우는 것은 일반적인 관행입니다. 이 문서에서는 데이터베이스에서 테이블로 데이터를 추가하는 방법에 대해 설명합니다. Aspose.PDF for .NET를 사용하여 모든 데이터 소스에서 [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) 객체를 데이터로 채우는 것이 가능합니다. 그리고 이는 가능할 뿐만 아니라 매우 쉽습니다.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)는 개발자가 다음에서 데이터를 가져올 수 있도록 합니다:

- 객체 배열
- DataTable
- DataView

이 주제는 DataTable 또는 DataView에서 데이터를 가져오는 방법에 대한 정보를 제공합니다.

.NET 플랫폼에서 작업하는 모든 개발자는 .NET Framework에서 도입된 기본 ADO.NET 개념에 익숙해야 합니다. ADO.NET을 사용하여 거의 모든 종류의 데이터 소스에 연결할 수 있습니다. 우리는 데이터베이스에서 데이터를 검색하고 이를 DataSet, DataTable 또는 DataView에 저장할 수 있습니다. Aspose.PDF for .NET는 이들로부터 데이터를 가져오는 것도 지원합니다. 이는 개발자가 PDF 문서의 테이블을 모든 데이터 소스에서 채울 수 있는 더 많은 자유를 제공합니다.

Table 클래스의 ImportDataTable(..) 및 ImportDataView(..) 메서드는 데이터베이스에서 데이터를 가져오는 데 사용됩니다.

아래 예제는 ImportDataTable 메서드의 사용을 보여줍니다. 이 예제에서는 DataTable 객체가 처음부터 생성되고 레코드가 프로그래밍 방식으로 추가됩니다. 개발자는 원하는 대로 데이터베이스에서 DataTable을 채울 수도 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFromDataTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    DataTable dt = new DataTable("Employee");
    dt.Columns.Add("Employee_ID", typeof(Int32));
    dt.Columns.Add("Employee_Name", typeof(string));
    dt.Columns.Add("Gender", typeof(string));
    // Add 2 rows into the DataTable object programmatically
    DataRow dr = dt.NewRow();
    dr[0] = 1;
    dr[1] = "John Smith";
    dr[2] = "Male";
    dt.Rows.Add(dr);
    dr = dt.NewRow();
    dr[0] = 2;
    dr[1] = "Mary Miller";
    dr[2] = "Female";
    dt.Rows.Add(dr);
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Initializes a new instance of the Table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        // Set column widths of the table
        table.ColumnWidths = "40 100 100 100";
        // Set the table border color as LightGray
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Set the border for table cells
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        table.ImportDataTable(dt, true, 0, 1, 3, 3);

        // Add table object to first page of input document
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "ImportFromDataTable_out.pdf");
    }
}
```

## 현재 페이지에서 테이블이 분할될지 여부 결정하는 방법

테이블은 기본적으로 왼쪽 상단 위치에서 추가되며, 테이블이 페이지 끝에 도달하면 자동으로 분할됩니다. 프로그래밍 방식으로 테이블이 현재 페이지에 수용될 수 있는지 또는 페이지 하단에서 분할될지를 알 수 있습니다. 이를 위해 먼저 문서 크기 정보를 가져오고, 페이지 상단 및 하단 여백 정보, 테이블 상단 여백 정보 및 테이블 높이를 가져와야 합니다. 페이지 상단 여백 + 페이지 하단 여백 + 테이블 상단 여백 + 테이블 높이를 더하고 이를 문서 높이에서 빼면 문서 위에 남아 있는 공간의 양을 알 수 있습니다. 특정 행의 높이에 따라(지정한 경우) 테이블의 모든 행이 페이지 위의 남은 공간에 수용될 수 있는지 여부를 계산할 수 있습니다. 다음 코드 스니펫을 살펴보십시오. 다음 코드에서 평균 행 높이는 23.002 포인트입니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineTableBreak()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = pdf.Pages.Add();
        // Instantiate a table object
        Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
        table1.Margin.Top = 300;
        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(table1);
        // Set with column widths of the table
        table1.ColumnWidths = "100 100 100";
        // Set default cell border using BorderInfo object
        table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
        // Set table border using another customized BorderInfo object
        table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
        // Create MarginInfo object and set its left, bottom, right and top margins
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 5f;
        margin.Left = 5f;
        margin.Right = 5f;
        margin.Bottom = 5f;
        // Set the default cell padding to the MarginInfo object
        table1.DefaultCellPadding = margin;
        // If you increase the counter to 17, table will break
        // Because it cannot be accommodated any more over this page
        for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
        {
            // Create rows in the table and then cells in the rows
            Aspose.Pdf.Row row1 = table1.Rows.Add();
            row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
        }
        // Get the Page Height information
        float PageHeight = (float)pdf.PageInfo.Height;
        // Get the total height information of Page Top & Bottom margin,
        // Table Top margin and table height.
        float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

        // Display Page Height, Table Height, table Top margin and Page Top
        // And Bottom margin information
        Console.WriteLine("PDF document Height = " + pdf.PageInfo.Height.ToString() + "\nTop Margin Info = " + page.PageInfo.Margin.Top.ToString() + "\nBottom Margin Info = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nTable-Top Margin Info = " + table1.Margin.Top.ToString() + "\nAverage Row Height = " + table1.Rows[0].MinRowHeight.ToString() + " \nTable height " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nTotal Page Height =" + PageHeight.ToString() + "\nCummulative height including Table =" + TotalObjectsHeight.ToString());

        // Check if we deduct the sume of Page top margin + Page Bottom margin
        // + Table Top margin and table height from Page height and its less
        // Than 10 (an average row can be greater than 10)
        if ((PageHeight - TotalObjectsHeight) <= 10)
        {
            // If the value is less than 10, then display the message.
            // Which shows that another row can not be placed and if we add new
            // Row, table will break. It depends upon the row height value.
            Console.WriteLine("Page Height - Objects Height < 10, so table will break");
        }

        // Save PDF document
        document.Save(dataDir + "DetermineTableBreak_out.pdf");
    }
}
```

## 테이블에 반복 열 추가

Aspose.Pdf.Table 클래스에서는 테이블이 수직으로 너무 길어 다음 페이지로 넘칠 경우 반복 행 수를 설정할 수 있습니다. 그러나 경우에 따라 테이블이 너무 넓어 단일 페이지에 맞지 않고 다음 페이지로 계속되어야 합니다. 이를 위해 Aspose.Pdf.Table 클래스에 RepeatingColumnsCount 속성을 구현했습니다. 이 속성을 설정하면 테이블이 다음 페이지로 열 단위로 분할되고 주어진 열 수가 다음 페이지의 시작 부분에 반복됩니다. 다음 코드 스니펫은 RepeatingColumnsCount 속성의 사용을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRepeatingColumn()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Instantiate an outer table that takes up the entire page
        Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
        outerTable.ColumnWidths = "100%";
        outerTable.HorizontalAlignment = HorizontalAlignment.Left;

        // Instantiate a table object that will be nested inside outerTable that will break inside the same page
        Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
        mytable.Broken = TableBroken.VerticalInSamePage;
        mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

        // Add the outerTable to the page paragraphs
        // Add mytable to outerTable
        page.Paragraphs.Add(outerTable);
        var bodyRow = outerTable.Rows.Add();
        var bodyCell = bodyRow.Cells.Add();
        bodyCell.Paragraphs.Add(mytable);
        mytable.RepeatingColumnsCount = 5;
        page.Paragraphs.Add(mytable);

        // Add header Row
        Aspose.Pdf.Row row = mytable.Rows.Add();
        row.Cells.Add("header 1");
        row.Cells.Add("header 2");
        row.Cells.Add("header 3");
        row.Cells.Add("header 4");
        row.Cells.Add("header 5");
        row.Cells.Add("header 6");
        row.Cells.Add("header 7");
        row.Cells.Add("header 11");
        row.Cells.Add("header 12");
        row.Cells.Add("header 13");
        row.Cells.Add("header 14");
        row.Cells.Add("header 15");
        row.Cells.Add("header 16");
        row.Cells.Add("header 17");

        for (int RowCounter = 0; RowCounter <= 5; RowCounter++)
        {
            // Create rows in the table and then cells in the rows
            Aspose.Pdf.Row row1 = mytable.Rows.Add();
            row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 4");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 5");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 6");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 7");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 11");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 12");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 13");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 14");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 15");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 16");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 17");
        }

        // Save PDF document
        document.Save(dataDir + "AddRepeatingColumn_out.pdf");
    }
}
```

## 엔터티 프레임워크 소스와 테이블 통합

현대 .NET에 더 관련성이 높은 것은 ORM 프레임워크에서 데이터를 가져오는 것입니다. 이 경우, 간단한 목록이나 그룹화된 데이터에서 데이터를 가져오기 위해 Table 클래스를 확장하는 것이 좋습니다. 가장 인기 있는 ORM 중 하나인 엔터티 프레임워크에 대한 예를 들어 보겠습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static class PdfHelper
{
    private static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
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
    
    private static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
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

데이터 주석 속성은 종종 모델을 설명하고 테이블을 생성하는 데 도움을 줍니다. 따라서 ImportEntityList에 대한 다음 테이블 생성 알고리즘이 선택되었습니다:

- 12-18행: 헤더 행을 구축하고 "DisplayAttribute가 존재하면 해당 값을 사용하고, 그렇지 않으면 속성 이름을 사용"이라는 규칙에 따라 헤더 셀을 추가합니다.
- 50-53행: 데이터 행을 구축하고 "DataTypeAttribute가 정의되어 있으면 추가 디자인 설정이 필요한지 확인하고, 그렇지 않으면 데이터를 문자열로 변환하여 셀에 추가"라는 규칙에 따라 행 셀을 추가합니다.

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

우리는 그룹을 처리하므로 먼저 키 값에 대한 행을 생성하고(66-71행), 그 다음에 이 그룹의 행을 생성합니다.

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
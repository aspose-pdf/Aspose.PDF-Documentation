---
title: 데이터 소스 PDF와 테이블 통합
linktitle: 테이블 통합
type: docs
weight: 30
url: /ko/net/integrate-table/
description: 이 기사는 PDF 테이블을 통합하는 방법을 보여줍니다. 데이터베이스와 테이블을 통합하고 현재 페이지에서 테이블이 분할될지 결정합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "데이터 소스 PDF와 테이블 통합",
    "alternativeHeadline": "데이터 소스 PDF와 테이블 통합 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 테이블 통합",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2022-02-04",
    "description": "이 기사는 PDF 테이블을 통합하는 방법을 보여줍니다. 데이터베이스와 테이블을 통합하고 현재 페이지에서 테이블이 분할될지 결정합니다."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 데이터베이스와 테이블 통합

데이터베이스는 데이터를 저장하고 관리하기 위해 구축됩니다. 프로그래머들이 데이터베이스에서 데이터를 가져와 다양한 객체를 채우는 것은 일반적인 관행입니다. 이 글은 데이터베이스에서 데이터를 테이블에 추가하는 방법을 논의합니다. Aspose.PDF for .NET을 사용하여 [테이블](https://reference.aspose.com/pdf/net/aspose.pdf/table) 객체를 어떠한 데이터 소스에서도 데이터로 채울 수 있습니다. 뿐만 아니라 매우 쉽습니다.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/)은 개발자들이 다음에서 데이터를 가져올 수 있도록 합니다:

- 객체 배열
- 데이터테이블
- 데이터뷰

이 주제는 데이터테이블 또는 데이터뷰에서 데이터를 가져오는 정보를 제공합니다.

.NET 플랫폼에서 일하는 모든 개발자들은 .NET 프레임워크에서 도입된 기본적인 ADO.NET 개념을 잘 알고 있어야 합니다.
.NET 플랫폼에서 일하는 모든 개발자는 .NET 프레임워크에 의해 도입된 기본 ADO.NET 개념을 숙지해야 합니다.

Table 클래스의 ImportDataTable(..) 및 ImportDataView(..) 메소드는 데이터베이스에서 데이터를 가져오는 데 사용됩니다.

아래 예시는 ImportDataTable 메소드의 사용 방법을 보여줍니다. 이 예시에서는 DataTable 객체를 처음부터 생성하고 데이터베이스에서 데이터를 채우는 대신 프로그래밍 방식으로 레코드를 추가합니다. 개발자는 원하는 대로 데이터베이스에서 DataTable을 채울 수 있습니다.

```csharp
// 완전한 예시와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("Employee_ID", typeof(Int32));
dt.Columns.Add("Employee_Name", typeof(string));
dt.Columns.Add("Gender", typeof(string));
// DataTable 객체에 프로그래밍 방식으로 2 행 추가
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
// Document 인스턴스 생성
Document doc = new Document();
doc.Pages.Add();
// Table의 새 인스턴스 초기화
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// 테이블의 열 너비 설정
table.ColumnWidths = "40 100 100 100";
// 테이블 테두리 색상을 LightGray로 설정
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// 테이블 셀의 테두리 설정
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
table.ImportDataTable(dt, true, 0, 1, 3, 3);

// 테이블 객체를 입력 문서의 첫 페이지에 추가
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "DataIntegrated_out.pdf";
// 테이블 객체가 포함된 업데이트된 문서 저장
doc.Save(dataDir);
```
## 현재 페이지에서 테이블이 넘칠지 결정하는 방법

테이블은 기본적으로 왼쪽 상단 위치에서 추가되며 테이블이 페이지 끝에 도달하면 자동으로 나뉩니다. 테이블이 현재 페이지에 배치될 수 있는지 아니면 페이지 하단에서 나뉠지에 대한 정보를 프로그래밍 방식으로 얻을 수 있습니다. 이를 위해 먼저 문서 크기 정보를 가져온 다음, 페이지 상단 및 하단 여백 정보, 테이블 상단 여백 정보 및 테이블 높이를 가져와야 합니다. 페이지 상단 여백 + 페이지 하단 여백 + 테이블 상단 여백 + 테이블 높이를 더하고 문서 높이에서 이를 뺌으로써 문서에 남아 있는 공간의 양을 알 수 있습니다. 특정 행 높이(지정한 높이)에 따라, 페이지에 남은 공간 내에 테이블의 모든 행을 수용할 수 있는지 계산할 수 있습니다. 다음 코드 조각을 참조하십시오. 다음 코드에서 평균 행 높이는 23.002 포인트입니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// PDF 클래스 객체를 인스턴스화합니다.
Document pdf = new Document();
// PDF 문서 섹션 컬렉션에 섹션을 추가합니다.
Aspose.Pdf.Page page = pdf.Pages.Add();
// 테이블 객체를 인스턴스화합니다.
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table1.Margin.Top = 300;
// 원하는 섹션의 문단 컬렉션에 테이블을 추가합니다.
page.Paragraphs.Add(table1);
// 테이블의 열 너비를 설정합니다.
table1.ColumnWidths = "100 100 100";
// BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다.
table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// 또 다른 사용자 정의 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.
table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// MarginInfo 객체를 생성하고 왼쪽, 아래쪽, 오른쪽 및 상단 여백을 설정합니다.
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// MarginInfo 객체에 기본 셀 패딩을 설정합니다.
table1.DefaultCellPadding = margin;
// 카운터를 17로 증가시키면 테이블이 넘칩니다.
// 이 페이지에서 더 이상 수용할 수 없기 때문입니다.
for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
{
    // 테이블에 행을 생성하고 행에 셀을 생성합니다.
    Aspose.Pdf.Row row1 = table1.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
}
// 페이지 높이 정보를 가져옵니다.
float PageHeight = (float)pdf.PageInfo.Height;
// 페이지 상단 및 하단 여백,
// 테이블 상단 여백 및 테이블 높이의 총 높이 정보를 가져옵니다.
float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

// 페이지 높이, 테이블 높이, 테이블 상단 여백 및 페이지 상단
// 및 하단 여백 정보를 표시합니다.
Console.WriteLine("PDF 문서 높이 = " + pdf.PageInfo.Height.ToString() + "\n상단 여백 정보 = " + page.PageInfo.Margin.Top.ToString() + "\n하단 여백 정보 = " + page.PageInfo.Margin.Bottom.ToString() + "\n\n테이블-상단 여백 정보 = " + table1.Margin.Top.ToString() + "\n평균 행 높이 = " + table1.Rows[0].MinRowHeight.ToString() + " \n테이블 높이 " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\n총 페이지 높이 =" + PageHeight.ToString() + "\n테이블을 포함한 누적 높이 =" + TotalObjectsHeight.ToString());

// 페이지 상단 여백 + 페이지 하단 여백
// + 테이블 상단 여백 및 테이블 높이의 합을 페이지 높이에서 뺀 값이
// 10보다 작으면 (평균 행이 10보다 클 수 있음)
if ((PageHeight - TotalObjectsHeight) <= 10)
    // 값이 10보다 작으면, 새로운
    // 행을 추가하면 테이블이 넘칠 것입니다. 이는 행 높이 값에 따라 다릅니다.
    Console.WriteLine("페이지 높이 - 객체 높이 < 10, 따라서 테이블이 넘칠 것입니다.");


dataDir = dataDir + "DetermineTableBreak_out.pdf";
// pdf 문서를 저장합니다.
pdf.Save(dataDir);
```
## 테이블에 반복 열 추가

Aspose.Pdf.Table 클래스에서는 테이블이 세로로 너무 길어 다음 페이지로 넘어갈 때 반복할 행의 수를 설정할 수 있는 RepeatingRowsCount를 설정할 수 있습니다. 그러나 일부 경우에는 테이블이 너무 넓어 단일 페이지에 맞지 않고 다음 페이지로 이어져야 할 필요가 있습니다. 이 목적을 위해 Aspose.Pdf.Table 클래스에 RepeatingColumnsCount 속성을 구현했습니다. 이 속성을 설정하면 테이블이 다음 페이지로 열 방향으로 나누어지고 다음 페이지 시작 부분에서 지정된 열 수를 반복합니다. 다음 코드 스니펫은 RepeatingColumnsCount 속성의 사용 방법을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

string outFile = dataDir + "AddRepeatingColumn_out.pdf";
// 새 문서 생성
Document doc = new Document();
Aspose.Pdf.Page page = doc.Pages.Add();

// 전체 페이지를 차지하는 외부 테이블 인스턴스화
Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
outerTable.ColumnWidths = "100%";
outerTable.HorizontalAlignment = HorizontalAlignment.Left;

// 같은 페이지 내에서 끊어지는 내부 테이블 객체 인스턴스화
Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
mytable.Broken = TableBroken.VerticalInSamePage;
mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

// 외부 테이블을 페이지 단락에 추가
// 내부 테이블을 외부 테이블에 추가
page.Paragraphs.Add(outerTable);
var bodyRow = outerTable.Rows.Add();
var bodyCell = bodyRow.Cells.Add();
bodyCell.Paragraphs.Add(mytable);
mytable.RepeatingColumnsCount = 5;
page.Paragraphs.Add(mytable);

// 헤더 행 추가
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
    // 테이블에 행을 생성한 다음 행에 셀을 생성합니다.
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
doc.Save(outFile);
```
## Entity Framework 소스와 테이블 통합

현대 .NET에 더욱 적합한 것은 ORM 프레임워크에서 데이터를 가져오는 것입니다. 이 경우, 간단한 리스트나 그룹화된 데이터에서 데이터를 가져오기 위해 Table 클래스를 확장 메서드로 확장하는 것이 좋습니다. 가장 인기 있는 ORM 중 하나인 Entity Framework를 예로 들어 보겠습니다.

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
                // 테이블에 행 추가
                var row = table.Rows.Add();
                // 테이블 셀 추가
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
                // 그룹 행을 테이블에 추가
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // 데이터 행을 테이블에 추가
                    var dataRow = table.Rows.Add();
                    // 셀 추가
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
Data Annotations 속성은 종종 모델을 설명하고 테이블 생성을 돕기 위해 사용됩니다. 따라서 ImportEntityList를 위해 다음과 같은 테이블 생성 알고리즘이 선택되었습니다:

- 12-18라인: 헤더 행을 구성하고 "DisplayAttribute가 존재하면 그 값을 사용하고, 그렇지 않으면 속성 이름을 사용한다"는 규칙에 따라 헤더 셀을 추가합니다.
- 50-53라인: 데이터 행을 구성하고 "DataTypeAttribute 속성이 정의되어 있으면 추가 디자인 설정이 필요한지 확인하고, 그렇지 않으면 데이터를 문자열로 변환하여 셀에 추가한다"는 규칙에 따라 행 셀을 추가합니다.

이 예제에서는 DataType.Currency(32-34라인)와 DataType.Date(35-43라인)에 대한 추가 사용자 정의가 이루어졌지만 필요에 따라 다른 사용자 정의를 추가할 수 있습니다.
ImportGroupedData 메소드의 알고리즘은 이전과 거의 같습니다. 추가로 GroupViewModel 클래스를 사용하여 그룹화된 데이터를 저장합니다.

```csharp
using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```

그룹을 처리하기 때문에, 먼저 키 값에 대한 라인을 생성합니다(66-71 라인), 그 후 이 그룹의 라인들을 생성합니다.

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


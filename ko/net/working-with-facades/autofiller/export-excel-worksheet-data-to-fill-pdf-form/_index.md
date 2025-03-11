---
title: Excel 데이터를 내보내 PDF 양식 채우기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/export-excel-worksheet-data-to-fill-pdf-form/
description: 이 섹션에서는 AutoFiller 클래스를 사용하여 Excel 워크시트 데이터를 PDF 양식에 채우는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Export Excel data to fill PDF form",
    "alternativeHeadline": "Export Excel Data to Auto-Fill PDF Forms",
    "abstract": "Aspose.PDF for .NET의 기능을 통해 사용자는 AutoFiller 클래스를 사용하여 Excel 워크시트에서 PDF 양식으로 데이터를 원활하게 내보낼 수 있습니다. ExportDataTable 메서드를 활용하여 사용자는 Excel 데이터를 DataTable로 변환하고 PDF 양식을 효율적으로 채워 데이터 입력 프로세스를 간소화하고 생산성을 높일 수 있습니다. 이 기능은 PDF 양식이 Excel의 데이터 구조에 따라 정확하고 자동으로 채워지도록 보장합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "908",
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
    "url": "/net/export-excel-worksheet-data-to-fill-pdf-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/export-excel-worksheet-data-to-fill-pdf-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)는 [Aspose.PDF for .NET](/pdf/ko/net/)에서 PDF 양식을 채우는 다양한 방법을 제공합니다. XML 파일, DFD, XFDF에서 데이터를 가져오거나 API를 사용하고 Excel 워크시트의 데이터를 사용할 수 있습니다.
우리는 [Aspose.Cells](https://docs.aspose.com//cells/net)의 [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) 클래스의 [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) 메서드를 사용하여 Excel 시트의 데이터를 DataTable 객체로 내보낼 것입니다. 그런 다음 [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) 클래스의 [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) 메서드를 사용하여 이 데이터를 PDF 양식으로 가져와야 합니다. DataTable의 열 이름이 PDF 양식의 필드 이름과 동일한지 확인하십시오.

{{% /alert %}}

## 구현 세부정보

다음 시나리오에서는 ID, 이름 및 성별이라는 세 개의 양식 필드가 포함된 PDF 양식을 사용할 것입니다.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

위의 양식에는 "ID", "이름" 및 "성별"이라는 세 개의 필드가 있는 한 페이지가 있습니다. 우리는 다음 Excel 시트에서 데이터를 DataTable 객체로 추출할 것입니다.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

[AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) 클래스의 객체를 생성하고 위 그림에 있는 PDF 양식을 바인딩한 다음 [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) 메서드를 사용하여 DataTable 객체에 있는 데이터를 사용하여 양식 필드를 채워야 합니다.
메서드가 호출되면 Excel 시트의 데이터를 기반으로 채워진 양식이 포함된 새로운 PDF 양식 파일이 생성됩니다. 입력 PDF 양식은 단일 페이지였고 결과는 5페이지입니다. 이는 Excel 시트의 데이터 행 수가 5이기 때문입니다. DataTable 클래스는 시트의 첫 번째 행을 열 이름으로 사용할 수 있는 기능을 제공합니다.

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportExcelToPdfForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Excel();

    var workbook = new Workbook();
    // Creating a file stream containing the Excel file to be opened
    using (FileStream fstream = new FileStream(dataDir + "newBook1.xls", FileMode.Open))
    {
        // Opening the Excel file through the file stream
        workbook.Open(fstream);
        // Accessing the first worksheet in the Excel file
        var worksheet = workbook.Worksheets[0];
        // Exporting the contents of 7 rows and 2 columns starting from 1st cell to DataTable
        System.Data.DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
        // Create an object of AutoFiller class
        using (var autoFiller = new Aspose.Pdf.Facades.AutoFiller())
        {
            // The input pdf file that contains form fields
            autoFiller.InputFileName = dataDir + "DataTableExample.pdf";
            // The resultant pdf, that will contain the form fields filled with information from DataTable
            autoFiller.OutputFileName = dataDir + "DataTableExample_out.pdf";
            // Call the method to import the data from DataTable object into Pdf form fields
            autoFiller.ImportDataTable(dataTable);
            // Save PDF document
            autoFiller.Save();
        }
    }
}
```

XLSX에서 채우려면 다음 코드 스니펫을 사용하십시오:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillFromXLSX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Excel();

    // Create an object of AutoFiller class
    using (var autoFiller = new Aspose.Pdf.Facades.AutoFiller())
    {
        // Bind PDF document
        autoFiller.BindPdf(dataDir + "Sample-Form-01.pdf");

        System.Data.DataTable dataTable = GenerateDataTable();

        // Call the method to import the data from DataTable object into Pdf form fields
        autoFiller.ImportDataTable(dataTable);

        // Save PDF document
        autoFiller.Save(dataDir + "Sample-Form-01_out.pdf");
    }
}
```

Aspose.PDF for .NET은 PDF 문서에서 데이터 테이블을 생성할 수 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static System.Data.DataTable GenerateDataTable()
{
    string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
    // Create a new DataTable
    var table = new System.Data.DataTable("Students");

    // Create new DataColumn, set DataType,
    // ColumnName and add to DataTable
    var column = new System.Data.DataColumn
    {
        DataType = System.Type.GetType("System.Int32"),
        ColumnName = "id",
        ReadOnly = true,
        Unique = true
    };
    // Add the Column to the DataColumnCollection
    table.Columns.Add(column);

    // Create second column
    column = new System.Data.DataColumn
    {
        DataType = System.Type.GetType("System.String"),
        ColumnName = "First Name",
        AutoIncrement = false,
        Caption = "First Name",
        ReadOnly = false,
        Unique = false
    };
    // Add the column to the table
    table.Columns.Add(column);

    // Make the ID column the primary key column
    var primaryKeyColumns = new System.Data.DataColumn[1];
    primaryKeyColumns[0] = table.Columns["id"];
    table.PrimaryKey = primaryKeyColumns;

    // Create three new DataRow objects and add
    // them to the DataTable
    var rand = new Random();
    System.Data.DataRow row;
    for (int i = 1; i <= 4; i++)
    {
        row = table.NewRow();
        row["id"] = i;
        row["First Name"] = names[rand.Next(names.Length)];
        table.Rows.Add(row);
    }
    return table;
}
```

## 결론

{{% alert color="primary" %}}
[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades)는 데이터베이스의 데이터를 사용하여 PDF 양식을 채울 수 있는 기능도 제공하지만 이 기능은 현재 .NET 버전에서만 지원됩니다.
{{% /alert %}}
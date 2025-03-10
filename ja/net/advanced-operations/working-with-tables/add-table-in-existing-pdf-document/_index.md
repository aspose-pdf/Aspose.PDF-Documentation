---
title: C#を使用してPDFにテーブルを作成または追加する
linktitle: テーブルを作成または追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/add-table-in-existing-pdf-document/
description: Aspose.PDF for .NETは、PDFテーブルを作成、読み取り、編集するために使用されるライブラリです。このトピックで他の高度な機能を確認してください。
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
    "headline": "Create or Add Table In PDF using C#",
    "alternativeHeadline": "Add Tables to PDFs Effortlessly with C#",
    "abstract": "Aspose.PDF for .NETの新機能により、開発者はC#を使用して既存のPDFドキュメントにテーブルをシームレスに作成および追加できます。この機能には、カスタマイズ可能な境界線、セルのパディング、ColSpanおよびRowSpanを使用したセルの結合をサポートするなどの高度な機能が含まれており、PDFファイル内のデータのプレゼンテーションを向上させます。",
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
    "description": "Aspose.PDF for .NETは、PDFテーブルを作成、読み取り、編集するために使用されるライブラリです。このトピックで他の高度な機能を確認してください。"
}
</script>

## C#を使用したテーブルの作成

テーブルはPDFドキュメントを扱う際に重要です。情報を体系的に表示するための優れた機能を提供します。Aspose.PDF名前空間には、PDFドキュメントをゼロから生成する際にテーブルを作成する機能を提供する[Table](https://reference.aspose.com/pdf/net/aspose.pdf/table)、[Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell)、および[Row](https://reference.aspose.com/pdf/net/aspose.pdf/row)という名前のクラスが含まれています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

テーブルはTableクラスのオブジェクトを作成することで作成できます。

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### 既存のPDFドキュメントにテーブルを追加する

Aspose.PDF for .NETを使用して既存のPDFファイルにテーブルを追加するには、次の手順を実行します。

1. ソースファイルをロードします。
1. テーブルを初期化し、その列と行を設定します。
1. テーブルの設定を行います（境界線を設定しました）。
1. テーブルにデータを入力します。
1. ページにテーブルを追加します。
1. ファイルを保存します。

以下のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています。

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

### テーブルのColSpanとRowSpan

Aspose.PDF for .NETは、テーブル内の列を結合するための[ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan)プロパティと、行を結合するための[RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan)プロパティを提供します。

`Cell`オブジェクトに`ColSpan`または`RowSpan`プロパティを使用してテーブルセルを作成します。必要なプロパティを適用した後、作成したセルをテーブルに追加できます。

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

以下の実行コードの結果は、次の画像に示されているテーブルです：

![ColSpanとRowSpanのデモ](colspan_rowspan.png)

## 境界線、マージン、パディングの操作

テーブルの境界線スタイル、マージン、セルのパディングを設定する機能もサポートしていることに注意してください。より技術的な詳細に入る前に、以下の図に示されている境界線、マージン、パディングの概念を理解することが重要です：

![境界線、マージン、パディング](set-border-style-margins-and-padding-of-table_1.png)

上の図では、テーブル、行、セルの境界線が重なっていることがわかります。Aspose.PDFを使用すると、テーブルにはマージンがあり、セルにはパディングがあります。セルのマージンを設定するには、セルのパディングを設定する必要があります。

### 境界線

テーブル、[Row](https://reference.aspose.com/pdf/net/aspose.pdf/row)、および[Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell)オブジェクトの境界線を設定するには、Table.Border、Row.Border、およびCell.Borderプロパティを使用します。セルの境界線は、[Table](https://reference.aspose.com/pdf/net/aspose.pdf/table)またはRowクラスのDefaultCellBorderプロパティを使用して設定することもできます。上記で説明したすべての境界線関連プロパティは、コンストラクタを呼び出すことによって作成されるRowクラスのインスタンスに割り当てられます。Rowクラスには、境界線をカスタマイズするために必要なほぼすべてのパラメータを受け取る多くのオーバーロードがあります。

### マージンまたはパディング

セルのパディングは、Tableクラスの[DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding)プロパティを使用して管理できます。すべてのパディング関連プロパティは、`Left`、`Right`、`Top`、および`Bottom`パラメータに関する情報を受け取る[MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo)クラスのインスタンスに割り当てられます。

以下の例では、セルの境界線の幅を0.1ポイント、テーブルの境界線の幅を1ポイント、セルのパディングを5ポイントに設定しています。

![PDFテーブルのマージンと境界線](margin-border.png)

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

角が丸いテーブルを作成するには、BorderInfoクラスの`RoundedBorderRadius`値を使用し、テーブルの角のスタイルを丸く設定します。

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

## テーブルに異なる自動調整設定を適用する

Microsoft Wordなどのビジュアルエージェントを使用してテーブルを作成する際には、テーブルを希望の幅に自動的にサイズ調整するために自動調整オプションの1つを使用することがよくあります。たとえば、AutoFit to Windowオプションを使用してテーブルをページの幅に合わせたり、AutoFit to Contentsオプションを使用して各セルがその内容に合わせて成長または縮小できるようにしたりできます。

デフォルトでは、Aspose.PDFは`ColumnAdjustment`を`Customized`値で使用して新しいテーブルを挿入します。テーブルはページの利用可能な幅にサイズ調整されます。このようなテーブルまたは既存のテーブルのサイズ調整動作を変更するには、Table.autoFit(int)メソッドを呼び出すことができます。このメソッドは、テーブルに適用される自動調整の種類を定義するAutoFitBehavior列挙型を受け取ります。

Microsoft Wordと同様に、自動調整メソッドは、テーブルに一度に異なるプロパティを適用するショートカットです。これらのプロパティは、テーブルに観察される動作を与えるものです。各自動調整オプションのこれらのプロパティについて説明します。以下のテーブルを使用し、デモとして異なる自動調整設定を適用します：

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

### テーブルの幅を取得する

時には、テーブルの幅を動的に取得する必要があります。Aspose.PDF.Tableクラスには、その目的のための[GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth)メソッドがあります。たとえば、テーブルの列幅を明示的に設定せず、[ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment)をAutoFitToContentに設定した場合、この場合、次のようにテーブルの幅を取得できます。

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

## テーブルセルにSVG画像を追加する

Aspose.PDF for .NETは、PDFファイルにテーブルセルを追加する機能をサポートしています。テーブルを作成する際に、セルにテキストや画像を追加することが可能です。さらに、APIはSVGファイルをPDF形式に変換する機能も提供しています。これらの機能を組み合わせることで、SVG画像をロードし、テーブルセルに追加することができます。

以下のコードスニペットは、テーブルインスタンスを作成し、テーブルセル内にSVG画像を追加する手順を示しています。

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

## テーブル内でHTMLタグを使用する

時には、HTMLタグを含むデータベースの内容をインポートし、その内容をTableオブジェクトにインポートする必要がある場合があります。内容をインポートする際には、PDFドキュメント内でHTMLタグが適切にレンダリングされる必要があります。この要件を達成するために、ImprotDataTable()メソッドを強化しました。

{{% alert color="primary" %}}

テーブル要素内でHTMLタグを使用すると、APIがHTMLタグを適切に処理し、出力PDFドキュメントにレンダリングする必要があるため、ドキュメント生成時間が増加することに注意してください。

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

## テーブルの行の間にページ区切りを挿入する

デフォルトの動作として、PDFファイル内にテーブルを作成する際、テーブルはテーブルの下部マージンに達すると次のページに流れます。ただし、テーブルに特定の行数が追加されたときに強制的にページ区切りを挿入する必要がある場合があります。以下のコードスニペットは、テーブルに10行追加されたときにページ区切りを挿入する手順を示しています。

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

## 新しいページにテーブルをレンダリングする

デフォルトでは、段落はページオブジェクトの段落コレクションに追加されます。ただし、ページ上の以前に追加された段落レベルオブジェクトの直後ではなく、新しいページにテーブルをレンダリングすることも可能です。

### サンプル：C#を使用して新しいページにテーブルをレンダリングする方法

新しいページにテーブルをレンダリングするには、BaseParagraphクラスの[IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage)プロパティを使用します。以下のコードスニペットはその方法を示しています。

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
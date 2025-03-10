---
title: Criar ou Adicionar Tabela em PDF usando C#
linktitle: Criar ou Adicionar Tabela
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/add-table-in-existing-pdf-document/
description: Aspose.PDF for .NET é uma biblioteca usada para criar, ler e editar Tabelas PDF. Confira outras funções avançadas neste tópico.
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
    "abstract": "O novo recurso em Aspose.PDF for .NET permite que os desenvolvedores criem e adicionem tabelas a documentos PDF existentes usando C#. Essa funcionalidade inclui recursos avançados, como bordas personalizáveis, preenchimento de células e suporte para mesclar células com ColSpan e RowSpan, melhorando a apresentação de dados em arquivos PDF.",
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
    "description": "Aspose.PDF for .NET é uma biblioteca usada para criar, ler e editar Tabelas PDF. Confira outras funções avançadas neste tópico."
}
</script>

## Criando Tabela usando C\#

Tabelas são importantes ao trabalhar com documentos PDF. Elas fornecem ótimos recursos para exibir informações de maneira sistemática. O namespace Aspose.PDF contém classes chamadas [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell) e [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) que oferecem funcionalidade para criar tabelas ao gerar documentos PDF do zero.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

A tabela pode ser criada criando um objeto da classe Table.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Adicionando Tabela em Documento PDF Existente

Para adicionar uma tabela a um arquivo PDF existente com Aspose.PDF for .NET, siga os seguintes passos:

1. Carregue o arquivo de origem.
1. Inicialize uma tabela e defina suas colunas e linhas.
1. Defina as configurações da tabela (definimos as bordas).
1. Preencha a tabela.
1. Adicione a tabela a uma página.
1. Salve o arquivo.

Os seguintes trechos de código mostram como adicionar texto em um arquivo PDF existente.

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

### ColSpan e RowSpan em Tabelas

Aspose.PDF for .NET fornece a propriedade [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan) para mesclar as colunas em uma tabela e a propriedade [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan) para mesclar as linhas.

Usamos a propriedade `ColSpan` ou `RowSpan` no objeto `Cell` que cria a célula da tabela. Após aplicar as propriedades necessárias, a célula criada pode ser adicionada à tabela.

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

O resultado da execução do código abaixo é a tabela representada na imagem a seguir:

![Demonstração de ColSpan e RowSpan](colspan_rowspan.png)

## Trabalhando com Bordas, Margens e Preenchimento

Observe que também suporta o recurso de definir estilo de borda, margens e preenchimento de células para tabelas. Antes de entrar em mais detalhes técnicos, é importante entender os conceitos de borda, margens e preenchimento, que são apresentados abaixo em um diagrama:

![Bordas, margens e preenchimento](set-border-style-margins-and-padding-of-table_1.png)

Na figura acima, você pode ver que as bordas da tabela, linha e célula se sobrepõem. Usando Aspose.PDF, uma tabela pode ter margens e as células podem ter preenchimentos. Para definir as margens da célula, precisamos definir o preenchimento da célula.

### Bordas

Para definir as bordas da Tabela, [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) e objetos [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), use as propriedades Table.Border, Row.Border e Cell.Border. As bordas das células também podem ser definidas usando a propriedade DefaultCellBorder da classe [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) ou Row. Todas as propriedades relacionadas a bordas discutidas acima são atribuídas a uma instância da classe Row, que é criada chamando seu construtor. A classe Row tem muitas sobrecargas que aceitam quase todos os parâmetros necessários para personalizar a borda.

### Margens ou Preenchimento

O preenchimento da célula pode ser gerenciado usando a propriedade [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) da classe Table. Todas as propriedades relacionadas ao preenchimento são atribuídas a uma instância da classe [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo) que recebe informações sobre os parâmetros `Left`, `Right`, `Top` e `Bottom` para criar margens personalizadas.

No exemplo a seguir, a largura da borda da célula é definida como 0,1 ponto, a largura da borda da tabela é definida como 1 ponto e o preenchimento da célula é definido como 5 pontos.

![Margem e Borda na Tabela PDF](margin-border.png)

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

Para criar uma tabela com cantos arredondados, use o valor `RoundedBorderRadius` da classe BorderInfo e defina o estilo do canto da tabela como arredondado.

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

## Aplicando Diferentes Configurações de AutoFit a uma Tabela

Ao criar uma tabela usando um agente visual como o Microsoft Word, você frequentemente se verá usando uma das opções de AutoFit para ajustar automaticamente a tabela à largura desejada. Por exemplo, você pode usar a opção AutoFit to Window para ajustar a tabela à largura da página e a opção AutoFit to Contents para permitir que cada célula cresça ou encolha para acomodar seu conteúdo.

Por padrão, Aspose.PDF insere uma nova tabela usando `ColumnAdjustment` com o valor `Customized`. A tabela será ajustada à largura disponível na página. Para alterar o comportamento de dimensionamento em tal tabela ou em uma tabela existente, você pode chamar o método Table.autoFit(int). Este método aceita uma enumeração AutoFitBehavior que define que tipo de ajuste automático é aplicado à tabela.

Assim como no Microsoft Word, um método de autofit é na verdade um atalho que aplica diferentes propriedades à tabela de uma só vez. Essas propriedades são, na verdade, o que dá à tabela o comportamento observado. Discutiremos essas propriedades para cada opção de autofit. Usaremos a seguinte tabela e aplicaremos as diferentes configurações de ajuste automático como demonstração:

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

### Obter Largura da Tabela

Às vezes, é necessário obter a largura da tabela dinamicamente. A classe Aspose.PDF.Table tem um método [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) para esse propósito. Por exemplo, você não definiu a largura das colunas da tabela explicitamente e definiu [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) para AutoFitToContent. Nesse caso, você pode obter a largura da tabela da seguinte forma.

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

## Adicionar Imagem SVG à Célula da Tabela

Aspose.PDF for .NET suporta o recurso de adicionar uma célula de tabela em um arquivo PDF. Ao criar uma tabela, é possível adicionar texto ou imagens nas células. Além disso, a API também oferece o recurso de converter arquivos SVG para o formato PDF. Usando uma combinação desses recursos, é possível carregar uma imagem SVG e adicioná-la a uma célula da tabela.

O seguinte trecho de código mostra os passos para criar uma instância de tabela e adicionar uma imagem SVG dentro de uma célula da tabela.

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

## Usando Tags HTML dentro da Tabela

Às vezes, você pode ter a necessidade de importar conteúdos de banco de dados que possuem algumas tags HTML e, em seguida, importar o conteúdo para o objeto Tabela. Ao importar o conteúdo, ele deve renderizar as tags HTML de acordo dentro do documento PDF. Melhoramos o método ImprotDataTable() para atender a essa necessidade da seguinte forma:

{{% alert color="primary" %}}

Por favor, leve em conta que o uso de Tags HTML dentro do elemento da tabela aumenta o tempo de geração do documento, pois a API precisa processar as Tags HTML de acordo e renderizá-las no documento PDF de saída.

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

## Inserir uma Quebra de Página entre as linhas da tabela

Como comportamento padrão, ao criar uma tabela dentro de um arquivo PDF, a tabela flui para as páginas subsequentes quando atinge a margem inferior da tabela. No entanto, podemos ter a necessidade de forçar a inserção de uma quebra de página quando um certo número de linhas é adicionado à tabela. O seguinte trecho de código mostra os passos para inserir uma quebra de página quando 10 linhas são adicionadas à tabela.

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

## Renderizar uma Tabela em Nova Página

Por padrão, parágrafos são adicionados à coleção de Parágrafos de um objeto Page. No entanto, é possível renderizar uma tabela em uma nova página em vez de diretamente após o objeto de nível de parágrafo previamente adicionado na página.

### Exemplo: Como Renderizar uma Tabela em Nova Página usando C\#

Para renderizar a tabela em uma nova página, use a propriedade [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) na classe BaseParagraph. O seguinte trecho de código mostra como.

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
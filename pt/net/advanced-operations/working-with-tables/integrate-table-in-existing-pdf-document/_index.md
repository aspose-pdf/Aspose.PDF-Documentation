---
title: Integrar Tabela com Fontes de Dados PDF
linktitle: Integrar Tabela
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/integrate-table/
description: Este artigo mostra como integrar tabelas PDF. Integre Tabela com Banco de Dados e determine se a tabela será dividida na página atual.
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
    "abstract": "O recurso de integrar Tabela com Fontes de Dados PDF permite que os desenvolvedores importem dados de várias fontes, incluindo bancos de dados e o Entity Framework, diretamente para tabelas PDF usando Aspose.PDF for .NET. Com funcionalidades para determinar a paginação e suporte para colunas repetidas, esse recurso melhora a apresentação de dados enquanto mantém a integridade do documento, evitando que tabelas sejam divididas entre páginas.",
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
    "description": "Este artigo mostra como integrar tabelas PDF. Integre Tabela com Banco de Dados e determine se a tabela será dividida na página atual."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Integrar Tabela com Banco de Dados

Bancos de dados são construídos para armazenar e gerenciar dados. É uma prática comum para programadores preencher diferentes objetos com dados de bancos de dados. Este artigo discute a adição de dados de um banco de dados em uma tabela. É possível preencher um objeto [Table](https://reference.aspose.com/pdf/pt/net/aspose.pdf/table) com dados de qualquer fonte de dados usando Aspose.PDF for .NET. E não é apenas possível, mas é muito fácil.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) permite que os desenvolvedores importem dados de:

- Array de Objetos
- DataTable
- DataView

Este tópico fornece informações sobre como buscar dados de um DataTable ou DataView.

Todos os desenvolvedores que trabalham na plataforma .NET devem estar familiarizados com os conceitos básicos do ADO.NET introduzidos pelo .NET Framework. É possível conectar-se a quase todos os tipos de fontes de dados usando ADO.NET. Podemos recuperar dados de bancos de dados e salvá-los em um DataSet, DataTable ou DataView. Aspose.PDF for .NET oferece suporte para importar dados a partir destes também. Isso dá mais liberdade aos desenvolvedores para preencher tabelas em documentos PDF a partir de qualquer fonte de dados.

Os métodos ImportDataTable(..) e ImportDataView(..) da classe Table são usados para importar dados de bancos de dados.

O exemplo abaixo demonstra o uso do método ImportDataTable. Neste exemplo, o objeto DataTable é criado do zero e os registros são adicionados programaticamente em vez de preencher o DataTable com dados de bancos de dados. Os desenvolvedores também podem preencher o DataTable a partir do banco de dados de acordo com seu desejo.

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

## Como determinar se a tabela será dividida na página atual

As tabelas são, por padrão, adicionadas a partir da posição superior esquerda e, se a tabela atingir o final da página, ela se divide automaticamente. Você pode obter programaticamente a informação se a Tabela será acomodada na página atual ou se ela se dividirá na parte inferior da página. Para isso, primeiro, você precisa obter as informações sobre o tamanho do documento, depois precisa obter as informações sobre a margem superior e inferior da página, as informações sobre a margem superior da tabela e a altura da tabela. Se você adicionar a Margem Superior da Página + Margem Inferior da Página + Margem Superior da Tabela + Altura da Tabela e deduzir isso da altura do documento, você pode obter a quantidade de espaço restante sobre o documento. Dependendo da altura particular da linha (que você especificou), você pode calcular se todas as linhas de uma tabela podem ser acomodadas dentro do espaço restante sobre uma página ou não. Por favor, dê uma olhada no seguinte trecho de código. No código a seguir, a altura média da linha é 23.002 Pontos.

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

## Adicionar Coluna Repetida na Tabela

Na classe Aspose.Pdf.Table, você pode definir um RepeatingRowsCount que repetirá linhas se a tabela for muito longa verticalmente e transbordar para a próxima página. No entanto, em alguns casos, as tabelas são muito largas para caber em uma única página e precisam ser continuadas na próxima página. Para atender a esse propósito, implementamos a propriedade RepeatingColumnsCount na classe Aspose.Pdf.Table. Definir essa propriedade fará com que a tabela se divida na próxima página coluna por coluna e repita a contagem de colunas dada no início da próxima página. O seguinte trecho de código mostra o uso da propriedade RepeatingColumnsCount:

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

## Integrar Tabela com a fonte do Entity Framework

Mais relevante para o .NET moderno é a importação de dados de frameworks ORM. Neste caso, é uma boa ideia estender a classe Table com métodos de extensão para importar dados de uma lista simples ou de dados agrupados. Vamos dar um exemplo para um dos ORMs mais populares - Entity Framework.

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

Os atributos de Anotações de Dados são frequentemente usados para descrever modelos e nos ajudam a criar a tabela. Portanto, o seguinte algoritmo de geração de tabela foi escolhido para ImportEntityList:

- linhas 12-18: construir uma linha de cabeçalho e adicionar células de cabeçalho de acordo com a regra "Se o DisplayAttribute estiver presente, então pegue seu valor, caso contrário, pegue o nome da propriedade"
- linhas 50-53: construir as linhas de dados e adicionar células de linha de acordo com a regra "Se o atributo DataTypeAttribute estiver definido, então verificamos se precisamos fazer configurações de design adicionais para ele, e caso contrário, apenas convertemos os dados para string e adicionamos à célula;"

Neste exemplo, personalizações adicionais foram feitas para DataType.Currency (linhas 32-34) e DataType.Date (linhas 35-43), mas você pode adicionar outras se necessário. O algoritmo do método ImportGroupedData é quase o mesmo que o anterior. Uma classe adicional GroupViewModel é usada para armazenar os dados agrupados.

```csharp
using System.Collections.Generic;
public class GroupViewModel<K,T>
{
    public K Key;
    public IEnumerable<T> Values;
}
```

Como processamos grupos, primeiro geramos uma linha para o valor da chave (linhas 66-71), e depois - as linhas deste grupo.

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
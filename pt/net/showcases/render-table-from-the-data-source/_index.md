---
title: Renderizar tabela a partir da fonte de dados
linktitle: Renderizar tabela a partir da fonte de dados
type: docs
weight: 30
url: pt/net/render-table-from-the-data-source/
description: Esta página explica como é possível renderizar uma tabela a partir da fonte de dados usando a biblioteca Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF permite criar uma tabela com DataSource de DataSet, DataTable, arrays e objetos IEnumerable usando a classe PdfLightTable

A [classe Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) é usada para processar tabelas. Esta classe nos dá a capacidade de criar tabelas e colocá-las no documento, usando [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) e [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Portanto, para criar a tabela, você precisa adicionar o número necessário de linhas e preenchê-las com o número apropriado de células.

O exemplo a seguir cria uma tabela 4x10.

```csharp
var table = new Table
    {
        // Definir larguras automáticas da coluna da tabela
        ColumnWidths = "25% 25% 25% 25%",
        // Definir o preenchimento da célula
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Esquerda Inferior Direita Superior
        // Definir a cor da borda da tabela como Verde
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Definir a borda para as células da tabela como Verde
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Adicionar linha à tabela
        var row = table.Rows.Add();
        // Adicionar células à tabela
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // Adicionar objeto de tabela à primeira página do documento de entrada
    document.Pages[1].Paragraphs.Add(table);
```
Ao inicializar o objeto Table, foram usadas as configurações mínimas de aparência:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - largura das colunas (por padrão);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - os campos padrão para a célula da tabela;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - atributos da moldura da tabela (estilo, espessura, cor);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - atributos da moldura da célula (estilo, espessura, cor).

## Exportando dados de um array de objetos

A classe Table fornece métodos para interagir com fontes de dados ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf/table/importdatatable/methods/1) e [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).

Considerando que esses objetos não são muito convenientes para trabalhar no modelo MVC, limitar-nos-emos a um breve exemplo. Neste exemplo (linha 50), o método ImportDataTable é chamado e recebe como parâmetros uma instância de DataTable e configurações adicionais como a bandeira de cabeçalho e a posição inicial (linhas/colunas) para a saída de dados.

```csharp
// Cria um novo documento PDF
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// Inicializa uma nova instância do TextFragment para o título do relatório
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // Define as larguras das colunas da tabela
    ColumnWidths = "25% 25% 25% 25%",
    // Define o preenchimento das células
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Esquerda Inferior Direita Superior
    // Define a cor da borda da tabela como Verde
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // Define a borda para as células da tabela como Preto
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("Sem string de conexão em config.json");

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

// Adiciona o objeto tabela à primeira página do documento de entrada
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


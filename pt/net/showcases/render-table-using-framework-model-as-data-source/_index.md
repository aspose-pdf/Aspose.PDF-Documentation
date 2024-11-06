---
title: Renderizar tabela com Entity Framework
linktitle: Renderizar tabela com Entity Framework
type: docs
weight: 40
url: pt/net/render-table-using-entity-framework-model-as-data-source/
description: Este artigo mostrará como renderizar uma tabela usando o modelo do Entity Framework como fonte de dados usando o Aspose.PDF para .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Existem várias tarefas nas quais, por algum motivo, é mais conveniente exportar dados de bancos de dados para um documento PDF sem utilizar o esquema de conversão de HTML para PDF recentemente popular.

Este artigo mostrará como gerar um documento PDF usando o Aspose.PDF para .NET.

## Fundamentos da geração de PDF com Aspose.PDF

Uma das classes mais importantes no Aspose.PDF é a [classe Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Esta classe é um motor de renderização de PDF. Para apresentar uma estrutura de PDF, a biblioteca Aspose.PDF utiliza o modelo Document-Page, onde:

* Document - contém as propriedades do documento PDF incluindo a coleção de páginas;
* Documento - contém as propriedades do documento PDF incluindo a coleção de páginas;
* Página - contém as propriedades de uma página específica e várias coleções de elementos associados a esta página.

Portanto, para criar um documento PDF com Aspose.PDF, você deve seguir estes passos:

1. Criar o objeto Documento;
1. Adicionar a página (o objeto Página) ao objeto Documento;
1. Criar objetos que são colocados na página (por exemplo, fragmento de texto, tabela, etc.)
1. Adicionar os itens criados à coleção correspondente na página (no nosso caso, será uma coleção de parágrafos);
1. Salvar o documento como arquivo PDF.

```csharp
// Passo 1
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

// Passo 2
var pdfPage = document.Pages.Add();

// Passo 3
var textFragment = new TextFragment(reportTitle);
// ..........................................

var table = new Table
{
    // .................................
};

// Passo 4
pdfPage.Paragraphs.Add(textFragment);
pdfPage.Paragraphs.Add(table);

// Passo 5
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
O problema mais comum é a saída de dados em formato de tabela. A [classe Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) é usada para processar tabelas. Esta classe nos dá a capacidade de criar tabelas e colocá-las no documento, usando [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) e [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Então, para criar a tabela, você precisa adicionar o número necessário de linhas e preenchê-las com o número apropriado de células.

O seguinte exemplo cria uma tabela 4x10.

```csharp
var table = new Table
    {
        // Define larguras automáticas das colunas da tabela
        ColumnWidths = "25% 25% 25% 25%",
        // Define o preenchimento das células
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Esquerda Inferior Direita Superior
        // Define a cor da borda da tabela como Verde
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Define a borda para as células da tabela como Preto
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Adiciona linha à tabela
        var row = table.Rows.Add();
        // Adiciona células à tabela
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // Adiciona o objeto tabela à primeira página do documento de entrada
    document.Pages[1].Paragraphs.Add(table);
```
Ao inicializar o objeto Table, foram utilizadas as configurações mínimas de aparência:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - largura das colunas (por padrão);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - campos padrão para a célula da tabela;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - atributos da moldura da tabela (estilo, espessura, cor);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - atributos da moldura da célula (estilo, espessura, cor).

Como resultado, obtemos uma tabela 4x10 com colunas de largura igual.

![Tabela 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## Exportando Dados de Objetos ADO.NET

A classe Table fornece métodos para interagir com fontes de dados ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) e [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
A classe Table oferece métodos para interagir com fontes de dados ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) e [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
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
    // Define o padding da célula
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Esquerda Inferior Direita Superior
    // Define a cor da borda da tabela como Verde
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // Define a borda para as células da tabela como Verde
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("Nenhuma string de conexão em config.json");

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
## Exportando Dados do Entity Framework

Mais relevante para o moderno .NET é a importação de dados de frameworks ORM. Neste caso, é uma boa ideia estender a classe Table com métodos de extensão para importar dados de uma lista simples ou de dados agrupados. Vamos dar um exemplo para um dos ORMs mais populares - Entity Framework.

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
                // Adicionar linha à tabela
                var row = table.Rows.Add();
                // Adicionar células à tabela
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
                // Adicionar linha de grupo à tabela
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // Adicionar linha de dados à tabela
                    var dataRow = table.Rows.Add();
                    // Adicionar células
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
Os atributos Data Annotations são frequentemente usados para descrever modelos e nos ajudam a criar a tabela. Portanto, o seguinte algoritmo de geração de tabela foi escolhido para ImportEntityList:

* linhas 12-18: construir uma linha de cabeçalho e adicionar células de cabeçalho de acordo com a regra "Se o DisplayAttribute estiver presente, então pegue seu valor, caso contrário pegue o nome da propriedade"
* linhas 50-53: construir as linhas de dados e adicionar células de linha de acordo com a regra "Se o atributo DataTypeAttribute for definido, então verificamos se precisamos fazer configurações de design adicionais para ele, e caso contrário apenas converter os dados para string e adicionar à célula;"

Neste exemplo, personalizações adicionais foram feitas para DataType.Currency (linhas 32-34) e DataType.Date (linhas 35-43), mas você pode adicionar outras se necessário.
O algoritmo do método ImportGroupedData é quase o mesmo que o anterior. Uma classe adicional GroupViewModel é usada para armazenar os dados agrupados.

```csharp
using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
Uma vez que processamos grupos, primeiro geramos uma linha para o valor chave (linhas 66-71), e após isso - as linhas deste grupo.

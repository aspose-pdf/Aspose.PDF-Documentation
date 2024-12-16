---
title: Integrar Tabela com Fontes de Dados em PDF
linktitle: Integrar Tabela
type: docs
weight: 30
url: /pt/net/integrate-table/
description: Este artigo mostra como integrar tabelas em PDF. Integrar Tabela com Banco de Dados e determinar se a tabela será dividida na página atual.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Integrar Tabela com Fontes de Dados em PDF",
    "alternativeHeadline": "Como integrar Tabela com Fontes de Dados em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos em PDF",
    "keywords": "pdf, c#, integrar tabela",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "description": "Este artigo mostra como integrar tabelas em PDF. Integrar Tabela com Banco de Dados e determinar se a tabela será dividida na página atual."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Integrar Tabela com Banco de Dados

Bancos de dados são construídos para armazenar e gerenciar dados. É prática comum para programadores popular diferentes objetos com dados de bancos de dados. Este artigo discute adicionar dados de um banco de dados em uma tabela. É possível popular um objeto [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) com dados de qualquer fonte de dados usando Aspose.PDF para .NET. E não é apenas possível, mas é muito fácil.

[Aspose.PDF para .NET](https://docs.aspose.com/pdf/net/) permite que desenvolvedores importem dados de:

- Array de Objetos
- DataTable
- DataView

Este tópico fornece informações sobre como buscar dados de um DataTable ou DataView.

Todos os desenvolvedores trabalhando sob a plataforma .NET devem estar familiarizados com os conceitos básicos de ADO.NET introduzidos pelo .NET Framework.
Todos os desenvolvedores que trabalham na plataforma .NET devem estar familiarizados com os conceitos básicos do ADO.NET introduzidos pelo .NET Framework.

Os métodos ImportDataTable(..) e ImportDataView(..) da classe Table são usados para importar dados de bancos de dados.

O exemplo abaixo demonstra o uso do método ImportDataTable. Neste exemplo, o objeto DataTable é criado do zero e os registros são adicionados programaticamente em vez de preencher o DataTable com dados de bancos de dados. Os desenvolvedores podem popular o DataTable a partir do banco de dados também, conforme o seu desejo.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("Employee_ID", typeof(Int32));
dt.Columns.Add("Employee_Name", typeof(string));
dt.Columns.Add("Gender", typeof(string));
// Adicionar 2 linhas no objeto DataTable programaticamente
DataRow dr = dt.NewRow();
dr[0] = 1;
dr[1] = "John Smith";
dr[2] = "Masculino";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = 2;
dr[1] = "Mary Miller";
dr[2] = "Feminino";
dt.Rows.Add(dr);
// Criar instância do Document
Document doc = new Document();
doc.Pages.Add();
// Inicializa uma nova instância da Table
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Define as larguras das colunas da tabela
table.ColumnWidths = "40 100 100 100";
// Define a cor da borda da tabela como Cinza Claro
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Define a borda para as células da tabela
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
table.ImportDataTable(dt, true, 0, 1, 3, 3);

// Adiciona o objeto tabela à primeira página do documento de entrada
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "DataIntegrated_out.pdf";
// Salva o documento atualizado contendo o objeto tabela
doc.Save(dataDir);
```
## Como determinar se a tabela será quebrada na página atual

As tabelas são adicionadas por padrão a partir da posição superior esquerda e, se a tabela alcançar o final da página, ela quebra automaticamente. Você pode obter programaticamente a informação de que a Tabela será acomodada na página atual ou se quebrará no final da página. Para isso, primeiro, você precisa obter a informação do tamanho do documento, em seguida, você precisa obter a informação da margem superior e inferior da página, informação da margem superior da tabela e altura da tabela. Se você adicionar Margem Superior da Página + Margem Inferior da Página + Margem Superior da Tabela + Altura da Tabela e subtrair isso da altura do documento, você pode obter a quantidade de espaço restante no documento. Dependendo da altura específica da linha (que você especificou), você pode calcular se todas as linhas de uma tabela podem ser acomodadas no espaço restante de uma página ou não. Por favor, dê uma olhada no seguinte trecho de código. No código a seguir, a altura média da linha é de 23,002 pontos.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instancie um objeto da classe PDF
Document pdf = new Document();
// Adicione a seção à coleção de seções do documento PDF
Aspose.Pdf.Page page = pdf.Pages.Add();
// Instancie um objeto de tabela
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table1.Margin.Top = 300;
// Adicione a tabela na coleção de parágrafos da seção desejada
page.Paragraphs.Add(table1);
// Defina as larguras das colunas da tabela
table1.ColumnWidths = "100 100 100";
// Defina a borda padrão das células usando o objeto BorderInfo
table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Defina a borda da tabela usando outro objeto BorderInfo personalizado
table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Crie um objeto MarginInfo e defina suas margens esquerda, inferior, direita e superior
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Defina o preenchimento padrão das células para o objeto MarginInfo
table1.DefaultCellPadding = margin;
// Se você aumentar o contador para 17, a tabela será quebrada
// Porque ela não pode ser mais acomodada nesta página
for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
{
    // Crie linhas na tabela e depois células nas linhas
    Aspose.Pdf.Row row1 = table1.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
}
// Obtenha a informação da Altura da Página
float PageHeight = (float)pdf.PageInfo.Height;
// Obtenha a informação da altura total da Margem Superior & Inferior da Página,
// Margem Superior da Tabela e altura da tabela.
float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

// Exiba a Altura do Documento PDF, Altura da Tabela, informação da margem superior da tabela e Margem Superior
// E informação da Margem Inferior da Página
Console.WriteLine("Altura do documento PDF = " + pdf.PageInfo.Height.ToString() + "\nInformação da Margem Superior = " + page.PageInfo.Margin.Top.ToString() + "\nInformação da Margem Inferior = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nInformação da Margem Superior da Tabela = " + table1.Margin.Top.ToString() + "\nAltura Média da Linha = " + table1.Rows[0].MinRowHeight.ToString() + " \nAltura da tabela " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nAltura Total da Página =" + PageHeight.ToString() + "\nAltura cumulativa incluindo a Tabela =" + TotalObjectsHeight.ToString());

// Verifique se deduzimos a soma da margem superior da página + margem inferior da página
// + Margem superior da tabela e altura da tabela da altura da página e é menor
// Que 10 (uma linha média pode ser maior que 10)
if ((PageHeight - TotalObjectsHeight) <= 10)
    // Se o valor for menor que 10, então exiba a mensagem.
    // Que mostra que outra linha não pode ser colocada e se adicionarmos nova
    // Linha, a tabela será quebrada. Isso depende do valor da altura da linha.
    Console.WriteLine("Altura da Página - Altura dos Objetos < 10, então a tabela será quebrada");


dataDir = dataDir + "DetermineTableBreak_out.pdf";
// Salve o documento pdf
pdf.Save(dataDir);
```
## Adicionar Coluna Repetida em Tabela

Na classe Aspose.Pdf.Table, você pode definir um RepeatingRowsCount que repetirá linhas se a tabela for muito longa verticalmente e transbordar para a próxima página. No entanto, em alguns casos, as tabelas são muito largas para caber em uma única página e precisam continuar na próxima página. Para atender a essa necessidade, implementamos a propriedade RepeatingColumnsCount na classe Aspose.Pdf.Table. Definir essa propriedade fará com que a tabela quebre para a próxima página em colunas e repita a contagem de colunas especificada no início da próxima página. O seguinte trecho de código mostra o uso da propriedade RepeatingColumnsCount:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

string outFile = dataDir + "AddRepeatingColumn_out.pdf";
// Criar um novo documento
Document doc = new Document();
Aspose.Pdf.Page page = doc.Pages.Add();

// Instanciar uma tabela externa que ocupa toda a página
Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
outerTable.ColumnWidths = "100%";
outerTable.HorizontalAlignment = HorizontalAlignment.Left;

// Instanciar um objeto de tabela que será aninhado dentro da outerTable que quebrará dentro da mesma página
Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
mytable.Broken = TableBroken.VerticalInSamePage;
mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

// Adicionar a outerTable aos parágrafos da página
// Adicionar mytable à outerTable
page.Paragraphs.Add(outerTable);
var bodyRow = outerTable.Rows.Add();
var bodyCell = bodyRow.Cells.Add();
bodyCell.Paragraphs.Add(mytable);
mytable.RepeatingColumnsCount = 5;
page.Paragraphs.Add(mytable);

// Adicionar linha de cabeçalho
Aspose.Pdf.Row row = mytable.Rows.Add();
row.Cells.Add("cabeçalho 1");
row.Cells.Add("cabeçalho 2");
row.Cells.Add("cabeçalho 3");
row.Cells.Add("cabeçalho 4");
row.Cells.Add("cabeçalho 5");
row.Cells.Add("cabeçalho 6");
row.Cells.Add("cabeçalho 7");
row.Cells.Add("cabeçalho 11");
row.Cells.Add("cabeçalho 12");
row.Cells.Add("cabeçalho 13");
row.Cells.Add("cabeçalho 14");
row.Cells.Add("cabeçalho 15");
row.Cells.Add("cabeçalho 16");
row.Cells.Add("cabeçalho 17");

for (int RowCounter = 0; RowCounter <= 5; RowCounter++)

{
    // Criar linhas na tabela e então células nas linhas
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
## Integre Tabela com a fonte do Entity Framework

Mais relevante para o .NET moderno é a importação de dados de frameworks ORM. Neste caso, é uma boa ideia estender a classe Table com métodos de extensão para importar dados de uma lista simples ou de dados agrupados. Vamos dar um exemplo para um dos ORMs mais populares - Entity Framework.

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
                // Adiciona linha à tabela
                var row = table.Rows.Add();
                // Adiciona células à tabela
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
                // Adiciona linha de grupo à tabela
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // Adiciona linha de dados à tabela
                    var dataRow = table.Rows.Add();
                    // Adiciona células
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
Os atributos Data Annotations são frequentemente usados para descrever modelos e nos ajudar a criar a tabela. Portanto, foi escolhido o seguinte algoritmo de geração de tabela para ImportEntityList:

- linhas 12-18: construir uma linha de cabeçalho e adicionar células de cabeçalho de acordo com a regra "Se o DisplayAttribute estiver presente, então pegue seu valor, caso contrário, pegue o nome da propriedade"
- linhas 50-53: construir as linhas de dados e adicionar células de acordo com a regra "Se o atributo DataTypeAttribute estiver definido, então verificamos se precisamos fazer configurações de design adicionais para ele, e caso contrário, apenas converter os dados para string e adicionar à célula;"

Neste exemplo, foram feitas personalizações adicionais para DataType.Currency (linhas 32-34) e DataType.Date (linhas 35-43), mas você pode adicionar outras se necessário.
O algoritmo do método ImportGroupedData é quase o mesmo que o anterior. Uma classe adicional GroupViewModel é usada para armazenar os dados agrupados.

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
    "name": "Biblioteca Aspose.PDF para .NET",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
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


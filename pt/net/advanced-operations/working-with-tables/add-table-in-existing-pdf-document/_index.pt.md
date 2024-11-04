---
title: Criar ou Adicionar Tabela em PDF usando C#
linktitle: Criar ou Adicionar Tabela
type: docs
weight: 10
url: /net/add-table-in-existing-pdf-document/
description: Aspose.PDF para .NET é uma biblioteca usada para criar, ler e editar Tabelas PDF. Verifique outras funções avançadas neste tópico.
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
    "headline": "Criar ou Adicionar Tabela em PDF usando C#",
    "alternativeHeadline": "Como adicionar Tabela em PDF com .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, criar tabela em pdf, adicionar tabela",
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
    "url": "/net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET é uma biblioteca usada para criar, ler e editar Tabelas PDF. Verifique outras funções avançadas neste tópico."
}
</script>
## Criando Tabela usando C\#

Tabelas são importantes ao trabalhar com documentos PDF. Elas oferecem ótimas funcionalidades para exibição de informações de maneira sistemática. O namespace Aspose.PDF contém classes chamadas [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell) e [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) que fornecem funcionalidades para a criação de tabelas ao gerar documentos PDF do zero.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Uma tabela pode ser criada ao criar um objeto da Classe Table.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Adicionando Tabela em um Documento PDF Existente

Para adicionar uma tabela a um arquivo PDF existente com Aspose.PDF para .NET, siga os passos abaixo:

1. Carregue o arquivo fonte.
1. Inicialize uma tabela e defina suas colunas e linhas.
1. Configure as definições da tabela (definimos as bordas).
1. Preencha a tabela.
1. Adicione a tabela a uma página.
1.
1.

Os seguintes trechos de código mostram como adicionar texto em um arquivo PDF existente.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Carregar o documento PDF de origem
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddTable.pdf");
// Inicializa uma nova instância da Tabela
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Define a cor da borda da tabela como Cinza Claro
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Define a borda para as células da tabela
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Cria um loop para adicionar 10 linhas
for (int row_count = 1; row_count < 10; row_count++)
{
    // Adiciona linha à tabela
    Aspose.Pdf.Row row = table.Rows.Add();
    // Adiciona células à tabela
    row.Cells.Add("Coluna (" + row_count + ", 1)");
    row.Cells.Add("Coluna (" + row_count + ", 2)");
    row.Cells.Add("Coluna (" + row_count + ", 3)");
}
// Adiciona o objeto tabela à primeira página do documento de entrada
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "documento_com_tabela_out.pdf";
// Salva o documento atualizado contendo o objeto tabela
doc.Save(dataDir);
```
### ColSpan e RowSpan em Tabelas

Aspose.PDF para .NET fornece a propriedade [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan) para mesclar colunas em uma tabela e a propriedade [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan) para mesclar linhas.

Usamos a propriedade `ColSpan` ou `RowSpan` no objeto `Cell` que cria a célula da tabela. Após aplicar as propriedades necessárias, a célula criada pode ser adicionada à tabela.

```csharp
public static void AddTable_RowColSpan()
{
    // Carrega o documento PDF de origem
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.Pages.Add();

    // Inicializa uma nova instância da Tabela
    Aspose.Pdf.Table table = new Aspose.Pdf.Table
    {
        // Define a cor da borda da tabela como CinzaClaro
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
        // Define a borda para as células da tabela
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
    };

    // Adiciona a 1ª linha à tabela
    Aspose.Pdf.Row row1 = table.Rows.Add();
    for (int cellCount = 1; cellCount <5; cellCount++)
    {
        // Adiciona células à tabela
        row1.Cells.Add($"Teste 1 {cellCount}");
    }

    // Adiciona a 2ª linha à tabela
    Aspose.Pdf.Row row2 = table.Rows.Add();
    row2.Cells.Add($"Teste 2 1");
    var cell = row2.Cells.Add($"Teste 2 2");
    cell.ColSpan = 2;
    row2.Cells.Add($"Teste 2 4");

    // Adiciona a 3ª linha à tabela
    Aspose.Pdf.Row row3 = table.Rows.Add();
    row3.Cells.Add("Teste 3 1");
    row3.Cells.Add("Teste 3 2");
    row3.Cells.Add("Teste 3 3");
    row3.Cells.Add("Teste 3 4");

    // Adiciona a 4ª linha à tabela
    Aspose.Pdf.Row row4 = table.Rows.Add();
    row4.Cells.Add("Teste 4 1");
    cell = row4.Cells.Add("Teste 4 2");
    cell.RowSpan = 2;
    row4.Cells.Add("Teste 4 3");
    row4.Cells.Add("Teste 4 4");

    // Adiciona a 5ª linha à tabela
    row4 = table.Rows.Add();
    row4.Cells.Add("Teste 5 1");
    row4.Cells.Add("Teste 5 3");
    row4.Cells.Add("Teste 5 4");

    // Adiciona o objeto tabela à primeira página do documento de entrada
    pdfDocument.Pages[1].Paragraphs.Add(table);

    // Salva o documento atualizado contendo o objeto tabela
    doc.Save(Path.Combine(_dataDir, "document_with_table_out.pdf"));
}
```
O resultado do código de execução abaixo é a tabela mostrada na seguinte imagem:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## Trabalhando com Bordas, Margens e Preenchimento

Observe que também suporta o recurso para definir estilo de borda, margens e preenchimento de célula para tabelas. Antes de entrar em detalhes técnicos, é importante entender os conceitos de borda, margens e preenchimento que são apresentados abaixo em um diagrama:

![Bordas, margens e preenchimento](set-border-style-margins-and-padding-of-table_1.png)

Na figura acima, você pode ver que as bordas da tabela, linha e célula se sobrepõem. Usando Aspose.PDF, uma tabela pode ter margens e as células podem ter preenchimentos. Para definir as margens das células, temos que definir o preenchimento da célula.

### Bordas

Para definir as bordas dos objetos Tabela, [Linha](https://reference.aspose.com/pdf/net/aspose.pdf/row) e [Célula](https://reference.aspose.com/pdf/net/aspose.pdf/cell), use as propriedades Table.Border, Row.Border e Cell.Border.
Para definir as bordas de objetos Table, [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) e [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), utilize as propriedades Table.Border, Row.Border e Cell.Border.

### Margens ou Preenchimento

O preenchimento da célula pode ser gerenciado usando a propriedade [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) da classe Table. Todas as propriedades relacionadas ao preenchimento são atribuídas a uma instância da classe [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo) que recebe informações sobre os parâmetros `Left`, `Right`, `Top` e `Bottom` para criar margens personalizadas.

No exemplo a seguir, a largura da borda da célula é definida como 0,1 ponto, a largura da borda da tabela é definida como 1 ponto e o preenchimento da célula é definido como 5 pontos.

![Margem e Bordas em Tabela PDF](margin-border.png)

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instancie o objeto Document chamando seu construtor vazio
Document doc = new Document();
Page page = doc.Pages.Add();
// Instancie um objeto tabela
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Adicione a tabela na coleção de parágrafos da seção desejada
page.Paragraphs.Add(tab1);
// Defina as larguras das colunas da tabela
tab1.ColumnWidths = "50 50 50";
// Defina a borda da célula padrão usando o objeto BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Defina a borda da tabela usando outro objeto BorderInfo personalizado
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Crie um objeto MarginInfo e defina suas margens esquerda, inferior, direita e superior
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Defina o preenchimento padrão da célula para o objeto MarginInfo
tab1.DefaultCellPadding = margin;
// Crie linhas na tabela e então células nas linhas
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add();
TextFragment mytext = new TextFragment("col3 com um texto longo");
// Row1.Cells.Add("col3 com um texto longo para ser colocado dentro da célula");
row1.Cells[2].Paragraphs.Add(mytext);
row1.Cells[2].IsWordWrapped = false;
// Row1.Cells[2].Paragraphs[0].FixedWidth= 80;
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");
dataDir = dataDir + "MarginsOrPadding_out.pdf";
// Salve o PDF
doc.Save(dataDir);
```
Para criar uma tabela com cantos arredondados, utilize o valor `RoundedBorderRadius` da classe BorderInfo e defina o estilo dos cantos da tabela para arredondado.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

GraphInfo graph = new GraphInfo();
graph.Color = Aspose.Pdf.Color.Red;
// Criar um objeto BorderInfo em branco
BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
// Definir a borda com um raio arredondado de 15
bInfo.RoundedBorderRadius = 15;
// Definir o estilo dos cantos da tabela como Arredondado.
tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
// Definir as informações de borda da tabela
tab1.Border = bInfo;
```

## Aplicando Diferentes Configurações de AutoAjuste a uma Tabela

Ao criar uma tabela usando um agente visual como o Microsoft Word, você frequentemente se encontrará utilizando uma das opções de AutoAjuste para dimensionar automaticamente a tabela para a largura desejada.
Ao criar uma tabela usando um agente visual como o Microsoft Word, você frequentemente se encontrará usando uma das opções de AutoAjuste para dimensionar automaticamente a tabela para a largura desejada.

Por padrão, o Aspose.Pdf insere uma nova tabela usando `ColumnAdjustment` com valor `Customized`. A tabela ajustará seu tamanho para a largura disponível na página. Para alterar o comportamento de dimensionamento de tal tabela ou de uma tabela existente, você pode chamar o método Table.autoFit(int). Este método aceita uma enumeração AutoFitBehavior que define que tipo de ajuste automático é aplicado à tabela.

Assim como no Microsoft Word, um método de autofit é na verdade um atalho que aplica diferentes propriedades à tabela de uma só vez. Essas propriedades são na verdade o que dá à tabela o comportamento observado. Discutiremos essas propriedades para cada opção de autofit. Usaremos a seguinte tabela e aplicaremos as diferentes configurações de ajuste automático como demonstração:

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instancie o objeto Pdf chamando seu construtor vazio
Document doc = new Document();
// Crie a seção no objeto Pdf
Page sec1 = doc.Pages.Add();

// Instancie um objeto tabela
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Adicione a tabela na coleção de parágrafos da seção desejada
sec1.Paragraphs.Add(tab1);

// Defina as larguras das colunas da tabela
tab1.ColumnWidths = "50 50 50";
tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

// Defina a borda padrão da célula usando o objeto BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

// Defina a borda da tabela usando outro objeto BorderInfo personalizado
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Crie um objeto MarginInfo e defina suas margens esquerda, inferior, direita e superior
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;

// Defina o preenchimento padrão da célula para o objeto MarginInfo
tab1.DefaultCellPadding = margin;

// Crie linhas na tabela e então células nas linhas
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");

dataDir = dataDir + "AutoFitToWindow_out.pdf";
// Salve o documento atualizado contendo o objeto tabela
doc.Save(dataDir);
```
### Obter Largura da Tabela

Às vezes, é necessário obter a largura da tabela dinamicamente. A classe Aspose.PDF.Table possui um método [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) para esse propósito. Por exemplo, você não definiu explicitamente a largura das colunas da tabela e configurou [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) para AutoFitToContent. Neste caso, você pode obter a largura da tabela da seguinte forma.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Criar um novo documento
Document doc = new Document();
// Adicionar página no documento
Page page = doc.Pages.Add();
// Inicializar nova tabela
Table table = new Table
{
    ColumnAdjustment = ColumnAdjustment.AutoFitToContent
};
// Adicionar linha na tabela
Row row = table.Rows.Add();
// Adicionar célula na tabela
Cell cell = row.Cells.Add("Texto da Célula 1");
cell = row.Cells.Add("Texto da Célula 2");
// Obter largura da tabela
Console.WriteLine(table.GetWidth());
```

## Adicionar Imagem SVG em Célula de Tabela
## Adicionar Imagem SVG à Célula de Tabela

Aspose.PDF para .NET suporta a funcionalidade de adicionar uma célula de tabela a um arquivo PDF. Ao criar uma tabela, é possível adicionar texto ou imagens às células. Além disso, a API também oferece a funcionalidade de converter arquivos SVG para o formato PDF. Usando uma combinação dessas funcionalidades, é possível carregar uma imagem SVG e adicioná-la a uma célula de tabela.

O seguinte trecho de código mostra os passos para criar uma instância de tabela e adicionar uma imagem SVG dentro de uma célula de tabela.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instanciar objeto Document
Document doc = new Document();
// Criar uma instância de imagem
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// Definir o tipo de imagem como SVG
img.FileType = Aspose.Pdf.ImageFileType.Svg;
// Caminho para o arquivo fonte
img.File = dataDir + "SVGToPDF.svg";
// Definir largura para a instância de imagem
img.FixWidth = 50;
// Definir altura para a instância de imagem
img.FixHeight = 50;
// Criar instância de tabela
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Definir largura para as células da tabela
table.ColumnWidths = "100 100";
// Criar objeto de linha e adicioná-lo à instância de tabela
Aspose.Pdf.Row row = table.Rows.Add();
// Criar objeto de célula e adicioná-lo à instância de linha
Aspose.Pdf.Cell cell = row.Cells.Add();
// Adicionar textfragment à coleção de parágrafos do objeto de célula
cell.Paragraphs.Add(new TextFragment("Primeira célula"));
// Adicionar outra célula ao objeto de linha
cell = row.Cells.Add();
// Adicionar imagem SVG à coleção de parágrafos da célula recentemente adicionada
cell.Paragraphs.Add(img);
// Criar objeto de página e adicioná-lo à coleção de páginas do documento
Page page = doc.Pages.Add();
// Adicionar tabela à coleção de parágrafos do objeto de página
page.Paragraphs.Add(table);

dataDir = dataDir + "AddSVGObject_out.pdf";
// Salvar arquivo PDF
doc.Save(dataDir);
```
## Usando Tags HTML Dentro de Tabelas

Às vezes, você pode se deparar com a necessidade de importar conteúdos de banco de dados que possuem algumas tags HTML e, em seguida, importar o conteúdo para o objeto Tabela. Ao importar o conteúdo, as tags HTML devem ser renderizadas adequadamente dentro do documento PDF. Aprimoramos o método ImprotDataTable(), para alcançar tal requisito da seguinte forma:

{{% alert color="primary" %}}

Por favor, leve em conta que o uso de Tags HTML dentro do elemento tabela aumenta o tempo de geração do documento, pois a API precisa processar as Tags HTML adequadamente e renderizá-las no documento PDF de saída.

{{% /alert %}}

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("data", System.Type.GetType("System.String"));

DataRow dr = dt.NewRow();
dr[0] = "<li>Departamento de Medicina de Emergência: 3400 Spruce Street Ground Silverstein Bldg Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>Serviço de Medicina de Observação da Penn: 3400 Spruce Street Ground Floor Donner Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>UPHS/Presbyterian - Dept. de Medicina de Emergência: 51 N. 39th Street. Philadelphia PA 19104-2640</li>";
dt.Rows.Add(dr);

Document doc = new Document();
doc.Pages.Add();
// Inicializa uma nova instância da Tabela
Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
// Define as larguras das colunas da tabela
tableProvider.ColumnWidths = "400 50 ";
// Define a cor da borda da tabela como Cinza Claro
tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Define a borda para as células da tabela
tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 2.5F;
margin.Left = 2.5F;
margin.Bottom = 1.0F;
tableProvider.DefaultCellPadding = margin;

tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

doc.Pages[1].Paragraphs.Add(tableProvider);
doc.Save(dataDir + "HTMLInsideTableCell_out.pdf");
```
## Inserir uma Quebra de Página entre as linhas de uma tabela

Como um comportamento padrão, ao criar uma tabela dentro de um arquivo PDF, a tabela flui para as páginas subsequentes quando atinge a margem inferior da tabela. No entanto, podemos ter a necessidade de inserir forçosamente uma quebra de página quando um certo número de linhas for adicionado à tabela. O seguinte trecho de código mostra os passos para inserir uma quebra de página quando 10 linhas são adicionadas à tabela.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Instanciar a instância Document
Document doc = new Document();
// Adicionar página à coleção de páginas do arquivo PDF
doc.Pages.Add();
// Criar instância de tabela
Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
// Definir estilo de borda para a tabela
tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Definir estilo de borda padrão para a tabela com cor de borda Vermelha
tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Especificar larguras das colunas da tabela
tab.ColumnWidths = "100 100";
// Criar um loop para adicionar 200 linhas à tabela
for (int counter = 0; counter <= 200; counter++)
{
    Aspose.Pdf.Row row = new Aspose.Pdf.Row();
    tab.Rows.Add(row);
    Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
    cell1.Paragraphs.Add(new TextFragment("Célula " + counter + ", 0"));
    row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
    cell2.Paragraphs.Add(new TextFragment("Célula " + counter + ", 1"));
    row.Cells.Add(cell2);
    // Quando 10 linhas forem adicionadas, renderizar nova linha em nova página
    if (counter % 10 == 0 && counter != 0) row.IsInNewPage = true;
}
// Adicionar tabela à coleção de parágrafos do arquivo PDF
doc.Pages[1].Paragraphs.Add(tab);

dataDir = dataDir + "InsertPageBreak_out.pdf";
// Salvar o documento PDF
doc.Save(dataDir);
```

## Renderizar uma Tabela em uma Nova Página

Por padrão, parágrafos são adicionados à coleção de Parágrafos de um objeto Página. No entanto, é possível renderizar uma tabela em uma nova página em vez de diretamente após o objeto de nível de parágrafo adicionado anteriormente na página.

### Exemplo: Como Renderizar uma Tabela em Nova Página usando C\#

Para renderizar uma tabela em uma nova página, use a propriedade [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) na classe BaseParagraph. O seguinte trecho de código mostra como fazer isso.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document();
PageInfo pageInfo = doc.PageInfo;
Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

marginInfo.Left = 37;
marginInfo.Right = 37;
marginInfo.Top = 37;
marginInfo.Bottom = 37;

pageInfo.IsLandscape = true;

Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "50 100";
// Página adicionada.
Page curPage = doc.Pages.Add();
for (int i = 1; i <= 120; i++)
{
    Aspose.Pdf.Row row = table.Rows.Add();
    row.FixedRowHeight = 15;
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("Conteúdo 1"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("HHHHH"));
}
Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
paragraphs.Add(table);
/********************************************/
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table.ColumnWidths = "100 100";
for (int i = 1; i até 10; i++)
{
    Aspose.Pdf.Row row = table1.Rows.Add();
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("LAAAAAAA"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("LAAGGGGGG"));
}
table1.IsInNewPage = true;
// Eu quero manter a tabela 1 para a próxima página, por favor...
paragraphs.Add(table1);
dataDir = dataDir + "IsNewPageProperty_Test_out.pdf";
doc.Save(dataDir);
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
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/destaque",
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
```


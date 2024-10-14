---
title: Substituir Texto em PDF
linktitle: Substituir Texto em PDF
type: docs
weight: 40
url: /net/replace-text-in-pdf/
description: Saiba mais sobre várias formas de substituir e remover texto da biblioteca Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Substituir Texto em PDF",
    "alternativeHeadline": "Substituindo e Removendo Texto em Arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, substituir texto, remover texto",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Saiba mais sobre várias formas de substituir e remover texto da biblioteca Aspose.PDF para .NET."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Substituir texto em todas as páginas do documento PDF

{{% alert color="primary" %}}

Você pode tentar encontrar e substituir o texto no documento usando Aspose.PDF e obter os resultados online neste [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Para substituir o texto em todas as páginas de um documento PDF, você primeiro precisa usar TextFragmentAbsorber para encontrar a frase específica que deseja substituir. Depois disso, você precisa percorrer todos os TextFragments para substituir o texto e alterar quaisquer outros atributos. Depois de fazer isso, você só precisa salvar o PDF de saída usando o método Save do objeto Document. O seguinte trecho de código mostra como substituir texto em todas as páginas do documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ReplaceTextAll.pdf");

// Criar objeto TextAbsorber para encontrar todas as instâncias da frase de busca
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("texto");

// Aceitar o absorvedor para todas as páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obter os fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Percorrer os fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Atualizar texto e outras propriedades
    textFragment.Text = "TEXTO";
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}

dataDir = dataDir + "ReplaceTextAll_out.pdf";
// Salvar o documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Substituir texto em uma região específica da página

Para substituir texto em uma região específica da página, primeiro precisamos instanciar o objeto TextFragmentAbsorber, especificar a região da página usando a propriedade TextSearchOptions.Rectangle e depois iterar por todos os TextFragments para substituir o texto. Uma vez que essas operações sejam concluídas, só precisamos salvar o PDF de saída usando o método Save do objeto Document. O seguinte trecho de código mostra como substituir texto em todas as páginas do documento PDF.

```csharp
// carregar arquivo PDF
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// instanciar objeto TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// buscar texto dentro dos limites da página
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// especificar a região da página para opções de busca de texto
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// buscar texto da primeira página do arquivo PDF
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// iterar por cada TextFragment individual
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // atualizar texto para caracteres em branco
    tf.Text = "";
}

// salvar arquivo PDF atualizado após substituição de texto
pdf.Save("c:/pdftest/TextUpdated.pdf");
```

## Substituir Texto Baseado em uma Expressão Regular

Se você deseja substituir algumas frases baseadas em expressão regular, primeiro precisa encontrar todas as frases que correspondem a essa expressão regular específica usando TextFragmentAbsorber. Você terá que passar a expressão regular como parâmetro para o construtor do TextFragmentAbsorber. Você também precisa criar um objeto TextSearchOptions que especifica se a expressão regular está sendo usada ou não. Uma vez que você obtém as frases correspondentes em TextFragments, você precisa percorrer todas elas e atualizar conforme necessário. Finalmente, você precisa salvar o PDF atualizado usando o método Save do objeto Document. O seguinte trecho de código mostra como substituir texto baseado em uma expressão regular.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// Criar objeto TextAbsorber para encontrar todas as frases que correspondem à expressão regular
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Como 1999-2000

// Definir opção de pesquisa de texto para especificar o uso de expressão regular
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Aceitar o absorvedor para uma única página
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// Obter os fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Percorrer os fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Atualizar texto e outras propriedades
    textFragment.Text = "Nova Frase";
    // Definido como uma instância de um objeto.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```
## Substituir fontes em um arquivo PDF existente

Aspose.PDF para .NET suporta a capacidade de substituir texto em um documento PDF. No entanto, às vezes você tem a necessidade de apenas substituir a fonte que está sendo usada dentro do documento PDF. Então, em vez de substituir o texto, apenas a fonte que está sendo usada é substituída. Um dos sobrecarregamentos do construtor TextFragmentAbsorber aceita o objeto TextEditOptions como argumento e podemos usar o valor RemoveUnusedFonts da enumeração TextEditOptions.FontReplace para cumprir nossos requisitos. O seguinte trecho de código mostra como substituir a fonte dentro de um documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Carregar arquivo PDF fonte
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// Procurar fragmentos de texto e configurar a opção de edição como remover fontes não utilizadas
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// Aceitar o absorvedor para todas as páginas
pdfDocument.Pages.Accept(absorber);
// Percorrer todos os TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // Se o nome da fonte for ArialMT, substituir o nome da fonte por Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// Salvar documento atualizado
pdfDocument.Save(dataDir);
```
## A substituição de texto deve reorganizar automaticamente o conteúdo da página

Aspose.PDF para .NET suporta o recurso de pesquisar e substituir texto dentro do arquivo PDF. No entanto, recentemente alguns clientes encontraram problemas durante a substituição de texto quando um TextFragment específico é substituído por conteúdos menores e alguns espaços extras são exibidos no PDF resultante ou, caso o TextFragment seja substituído por uma string mais longa, então as palavras se sobrepõem ao conteúdo existente da página. Portanto, a necessidade era introduzir um mecanismo que, uma vez que o texto dentro de um documento PDF é substituído, os conteúdos devem ser reorganizados.

Para atender aos cenários mencionados acima, Aspose.PDF para .NET foi aprimorado para que nenhum desses problemas apareça ao substituir texto dentro do arquivo PDF. O seguinte trecho de código mostra como substituir texto dentro de um arquivo PDF e o conteúdo da página deve ser reorganizado automaticamente.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Carregar arquivo PDF fonte
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// Criar objeto TextFragment Absorber com expressão regular
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// Substituir cada TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // Definir a fonte do fragmento de texto sendo substituído
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // Definir tamanho da fonte
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // Substituir o texto por uma string maior que o placeholder
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// Salvar o PDF resultante
doc.Save(dataDir);
```
## Renderizando Símbolos Substituíveis durante a criação de PDF

Símbolos substituíveis são símbolos especiais em uma cadeia de texto que podem ser substituídos por conteúdo correspondente em tempo de execução. Os símbolos substituíveis atualmente suportados pelo novo Modelo de Objeto de Documento do namespace Aspose.PDF são `$P`, `$p`, `\n`, `\r`. Os símbolos `$p` e `$P` são usados para lidar com a numeração de páginas em tempo de execução. `$p` é substituído pelo número da página onde a classe Paragraph atual está. `$P` é substituído pelo número total de páginas no documento. Ao adicionar `TextFragment` à coleção de parágrafos dos documentos PDF, não é suportado alimentação de linha dentro do texto. No entanto, para adicionar texto com uma quebra de linha, por favor use `TextFragment` com `TextParagraph`:

- use "\r\n" ou Environment.NewLine em TextFragment em vez de um único "\n";
- crie um objeto TextParagraph. Ele adicionará texto com divisão de linha;
- adicione o TextFragment com TextParagraph.AppendLine;
- adicione o TextParagraph com TextBuilder.AppendParagraph.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Inicialize um novo TextFragment com texto contendo os marcadores de nova linha necessários
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Nome do Candidato: " + Environment.NewLine + " Joe Smoe");

// Defina as propriedades do fragmento de texto se necessário
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Crie um objeto TextParagraph
TextParagraph par = new TextParagraph();

// Adicione o novo TextFragment ao parágrafo
par.AppendLine(textFragment);

// Defina a posição do parágrafo
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Crie um objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Adicione o TextParagraph usando TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```
## Símbolos Substituíveis na Área de Cabeçalho/Rodapé

Símbolos substituíveis também podem ser colocados na seção de Cabeçalho/Rodapé de um arquivo PDF. Por favor, veja o seguinte trecho de código para detalhes sobre como adicionar um símbolo substituível na seção do rodapé.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// Atribua a instância de marginInfo à propriedade Margin de sec1.PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// Instancie um parágrafo de Texto que armazenará o conteúdo a ser mostrado como cabeçalho
TextFragment t1 = new TextFragment("título do relatório");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("Nome_do_Relatório");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// Crie um objeto HeaderFooter para a seção
HeaderFooter hfFoot = new HeaderFooter();
// Defina o objeto HeaderFooter para rodapé ímpar e par
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// Adicione um parágrafo de texto contendo o número atual da página do total de páginas
TextFragment t3 = new TextFragment("Gerado na data de teste");
TextFragment t4 = new TextFragment("nome do relatório ");
TextFragment t5 = new TextFragment("Página $p de $P");

// Instancie um objeto de tabela
Table tab2 = new Table();

// Adicione a tabela na coleção de parágrafos da seção desejada
hfFoot.Paragraphs.Add(tab2);

// Defina as larguras das colunas da tabela
tab2.ColumnWidths = "165 172 165";

// Crie linhas na tabela e em seguida células nas linhas
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// Defina o alinhamento vertical do texto como centralizado
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// Adicione a tabela na coleção de parágrafos da seção desejada
page.Paragraphs.Add(table);

// Defina a borda padrão das células usando o objeto BorderInfo
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// Defina a borda da tabela usando outro objeto BorderInfo personalizado
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// Crie linhas na tabela e em seguida células nas linhas
Row row1 = table.Rows.Add();

row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total for Java é uma compilação de todos os componentes Java oferecidos pela Aspose. É compilado diariamente" + CRLF + "para garantir que contém as versões mais atualizadas de cada um dos nossos componentes Java. " + CRLF + "diariamente para garantir que contém as versões mais atualizadas de cada um dos nossos componentes Java. " + CRLF + "Usando Aspose.Total for Java, os desenvolvedores podem criar uma ampla gama de aplicações.");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```
## Remover Fontes Não Utilizadas de Arquivos PDF

Aspose.PDF para .NET suporta a funcionalidade de incorporar fontes ao criar um documento PDF, bem como a capacidade de incorporar fontes em arquivos PDF existentes. A partir do Aspose.PDF para .NET 7.3.0, também permite remover fontes duplicadas ou não utilizadas de documentos PDF.

Para substituir fontes, use a seguinte abordagem:

1. Chame a classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber).
1. Chame o parâmetro TextFragmentAbsorber da classe TextEditOptions.FontReplace.RemoveUnusedFonts. (Isso remove fontes que se tornaram não utilizadas durante a substituição de fontes).
1. Defina a fonte individualmente para cada fragmento de texto.

O seguinte trecho de código substitui a fonte para todos os fragmentos de texto de todas as páginas do documento e remove as fontes não utilizadas.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Carregar o arquivo PDF de origem
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// Iterar por todos os TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// Salvar o documento atualizado
doc.Save(dataDir);
```
## Remover Todo o Texto de um Documento PDF

### Remover Todo o Texto Usando Operadores

Em algumas operações de texto, você precisa remover todo o texto de um documento PDF e, para isso, você precisa definir o texto encontrado como um valor de string vazia, geralmente. O ponto é que alterar o texto para múltiplos fragmentos de texto invoca uma série de operações de verificação e ajuste de posição de texto. Elas são essenciais nos cenários de edição de texto. A dificuldade é que você não pode determinar quantos fragmentos de texto serão removidos no cenário onde eles são processados em um loop.

Portanto, recomendamos usar outra abordagem para o cenário de remoção de todo o texto das páginas PDF. Considere o seguinte trecho de código que funciona muito rápido.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// Percorrer todas as páginas do Documento PDF
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // Selecionar todo o texto na página
    page.Contents.Accept(operatorSelector);
    // Excluir todo o texto
    page.Contents.Delete(operatorSelector.Selected);
}
// Salvar o documento
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
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


---
title: Substituir Texto em PDF via Python
linktitle: Substituir Texto em PDF
type: docs
weight: 40
url: /pt/python-net/replace-text-in-pdf/
description: Saiba mais sobre várias maneiras de substituir e remover texto da biblioteca Aspose.PDF para Python via .NET.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
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
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, substituir texto, remover texto",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe Aspose.PDF Doc",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/replace-text-in-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Saiba mais sobre várias maneiras de substituir e remover texto da biblioteca Aspose.PDF para Python via .NET."
}
</script>


## Substituir Texto em todas as páginas de um documento PDF

{{% alert color="primary" %}}

Você pode tentar encontrar e substituir o texto no documento usando Aspose.PDF e obter os resultados online neste [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Para substituir texto em todas as páginas de um documento PDF, você primeiro precisa usar o [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) para encontrar a frase específica que deseja substituir. Depois disso, você precisa percorrer todos os TextFragments para substituir o texto e alterar quaisquer outros atributos. Uma vez feito isso, você só precisa salvar o PDF de saída usando o método Save do objeto Document. O trecho de código a seguir mostra como substituir texto em todas as páginas de um documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Criar objeto TextAbsorber para encontrar todas as instâncias da frase de busca de entrada
    absorber = ap.text.TextFragmentAbsorber("format")

    # Aceitar o absorvedor para todas as páginas
    document.pages.accept(absorber)

    # Obter os fragmentos de texto extraídos
    collection = absorber.text_fragments

    # Percorrer os fragmentos
    for text_fragment in collection:
        # Atualizar texto e outras propriedades
        text_fragment.text = "FORMAT"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
        text_fragment.text_state.font_size = 22
        text_fragment.text_state.foreground_color = ap.Color.blue
        text_fragment.text_state.background_color = ap.Color.green

    # Salvar o documento
    document.save(output_pdf)
```


## Substituir Texto em uma Região Específica da Página

Para substituir texto em uma região específica da página, primeiro, precisamos instanciar o objeto TextFragmentAbsorber, especificar a região da página usando a propriedade TextSearchOptions.Rectangle e então iterar por todos os TextFragments para substituir o texto. Uma vez que essas operações são concluídas, só precisamos salvar o PDF de saída usando o método Save do objeto Document. O seguinte trecho de código mostra como substituir texto em todas as páginas de um documento PDF.

```python
// carregar arquivo PDF
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// instanciar objeto TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// buscar texto dentro dos limites da página
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// especificar a região da página para as Opções de Busca de Texto
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// buscar texto a partir da primeira página do arquivo PDF
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// iterar por cada TextFragment
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // atualizar texto para caracteres em branco
    tf.Text = "";
}

// salvar arquivo PDF atualizado após substituir texto
pdf.Save("c:/pdftest/TextUpdated.pdf");
```


## Substituir Texto Com Base em uma Expressão Regular

Se você deseja substituir algumas frases com base em uma expressão regular, primeiro precisa encontrar todas as frases que correspondem a essa expressão regular específica usando TextFragmentAbsorber. Você terá que passar a expressão regular como um parâmetro para o construtor TextFragmentAbsorber. Você também precisa criar um objeto TextSearchOptions que especifica se a expressão regular está sendo usada ou não. Assim que você obtiver as frases correspondentes em TextFragments, você precisa percorrer todas elas e atualizar conforme necessário. Finalmente, você precisa salvar o PDF atualizado usando o método Save do objeto Document. O trecho de código a seguir mostra como substituir texto com base em uma expressão regular.

```python
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
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
    // Definir para uma instância de um objeto.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```


## Substituir fontes em arquivo PDF existente

Aspose.PDF para Python via .NET suporta a capacidade de substituir texto em documento PDF. No entanto, às vezes você tem a necessidade de apenas substituir a fonte sendo usada dentro do documento PDF. Então, ao invés de substituir o texto, apenas a fonte sendo usada é substituída. Uma das sobrecargas do construtor TextFragmentAbsorber aceita um objeto TextEditOptions como argumento e podemos usar o valor RemoveUnusedFonts da enumeração TextEditOptions.FontReplace para cumprir nossos requisitos. O trecho de código a seguir mostra como substituir a fonte dentro do documento PDF.

```python
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Carregar arquivo PDF de origem
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// Procurar fragmentos de texto e definir a opção de edição como remover fontes não utilizadas
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


## A Substituição de Texto deve reorganizar automaticamente o Conteúdo da Página

Aspose.PDF para Python via .NET suporta o recurso de buscar e substituir texto dentro do arquivo PDF. No entanto, recentemente alguns clientes encontraram problemas durante a substituição de texto quando um determinado TextFragment é substituído por conteúdos menores e alguns espaços extras são exibidos no PDF resultante ou, no caso do TextFragment ser substituído por uma string maior, as palavras se sobrepõem ao conteúdo existente da página. Assim, a exigência era introduzir um mecanismo que, uma vez que o texto dentro de um documento PDF seja substituído, os conteúdos deveriam ser reorganizados.

Para atender aos cenários acima mencionados, o Aspose.PDF para Python via .NET foi aprimorado para que tais problemas não apareçam ao substituir texto dentro do arquivo PDF. O seguinte trecho de código mostra como substituir texto dentro de um arquivo PDF e os conteúdos da página devem ser reorganizados automaticamente.

```python
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Carregar arquivo PDF de origem
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// Criar objeto TextFragment Absorber com expressão regular
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// Substituir cada TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // Definir a fonte do fragmento de texto que está sendo substituído
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // Definir o tamanho da fonte
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // Substituir o texto com uma string maior do que o espaço reservado
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// Salvar PDF resultante
doc.Save(dataDir);
```


## Renderização de Símbolos Substituíveis durante a criação de PDF

Símbolos substituíveis são símbolos especiais em uma string de texto que podem ser substituídos pelo conteúdo correspondente em tempo de execução. Os símbolos substituíveis atualmente suportados pelo novo Modelo de Objeto de Documento do namespace Aspose.PDF são `$P`, `$p,` `\n`, `\r`. O `$p` e `$P` são usados para lidar com a numeração de páginas em tempo de execução. `$p` é substituído pelo número da página onde a classe atual do Parágrafo está. `$P` é substituído pelo número total de páginas no documento. Ao adicionar `TextFragment` à coleção de parágrafos de documentos PDF, ele não suporta quebra de linha dentro do texto. No entanto, para adicionar texto com uma quebra de linha, use `TextFragment` com `TextParagraph`:

- use "\r\n" ou Environment.NewLine em TextFragment em vez de um único "\n";
- crie um objeto TextParagraph. Ele adicionará texto com divisão de linha;
- adicione o TextFragment com TextParagraph.AppendLine;
- adicione o TextParagraph com TextBuilder.AppendParagraph.

```python
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Inicializar novo TextFragment com texto contendo marcadores de nova linha necessários
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Nome do Candidato: " + Environment.NewLine + " Joe Smoe");

// Defina as propriedades do fragmento de texto, se necessário
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Criar objeto TextParagraph
TextParagraph par = new TextParagraph();

// Adicionar novo TextFragment ao parágrafo
par.AppendLine(textFragment);

// Definir posição do parágrafo
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Criar objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Adicionar o TextParagraph usando TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```


## Símbolos substituíveis na área de Cabeçalho/Rodapé

Símbolos substituíveis também podem ser colocados dentro da seção de Cabeçalho/Rodapé do arquivo PDF. Por favor, veja o trecho de código a seguir para detalhes sobre como adicionar um símbolo substituível na seção de rodapé.

```python
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// Atribuir a instância marginInfo à propriedade Margin de sec1.PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// Instanciar um parágrafo de texto que armazenará o conteúdo a ser exibido como cabeçalho
TextFragment t1 = new TextFragment("título do relatório");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("Nome_Relatório");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// Criar um objeto HeaderFooter para a seção
HeaderFooter hfFoot = new HeaderFooter();
// Definir o objeto HeaderFooter para rodapé ímpar e par
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// Adicionar um parágrafo de texto contendo o número da página atual do total de páginas
TextFragment t3 = new TextFragment("Gerado na data de teste");
TextFragment t4 = new TextFragment("nome do relatório ");
TextFragment t5 = new TextFragment("Página $p de $P");

// Instanciar um objeto tabela
Table tab2 = new Table();

// Adicionar a tabela na coleção de parágrafos da seção desejada
hfFoot.Paragraphs.Add(tab2);

// Definir larguras das colunas da tabela
tab2.ColumnWidths = "165 172 165";

// Criar linhas na tabela e depois células nas linhas
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// Definir o alinhamento vertical do texto como centralizado
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

// Sec1.Paragraphs.Add(New Text("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL"))
Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// Adicionar a tabela na coleção de parágrafos da seção desejada
page.Paragraphs.Add(table);

// Definir borda de célula padrão usando o objeto BorderInfo
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// Definir borda da tabela usando outro objeto BorderInfo personalizado
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// Criar linhas na tabela e depois células nas linhas
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
            c1 = row.Cells.Add("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a" + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "Using Aspose.Total for Java developers can create a wide range of applications.");
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


## Remover Fontes Não Utilizadas de Arquivo PDF

O Aspose.PDF para Python via .NET suporta o recurso de incorporar fontes ao criar um documento PDF, assim como a capacidade de incorporar fontes em arquivos PDF existentes. A partir do Aspose.PDF para Python via .NET 7.3.0, ele também permite que você remova fontes duplicadas ou não utilizadas de documentos PDF.

Para substituir fontes, use a seguinte abordagem:

1. Chame a classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Chame o parâmetro TextEditOptions.FontReplace.RemoveUnusedFonts da classe TextFragmentAbsorber. (Isso remove as fontes que se tornaram não utilizadas durante a substituição de fontes).
1. Defina a fonte individualmente para cada fragmento de texto.

O seguinte trecho de código substitui a fonte para todos os fragmentos de texto de todas as páginas do documento e remove fontes não utilizadas.

```python
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Carregar arquivo PDF de origem
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// Iterar por todos os TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// Salvar documento atualizado
doc.Save(dataDir);
```


## Remover Todo o Texto do Documento PDF

### Remover Todo o Texto usando Operadores

Em algumas operações de texto, você precisa remover todo o texto do documento PDF e, para isso, normalmente precisa definir o texto encontrado como valor de string vazia. A questão é que alterar o texto para uma multidão de fragmentos de texto invoca uma série de operações de verificação e ajuste de posição do texto. Elas são essenciais nos cenários de edição de texto. A dificuldade é que você não pode determinar quantos fragmentos de texto serão removidos no cenário em que eles são processados em um loop.

Portanto, recomendamos usar outra abordagem para o cenário de remoção de todo o texto das páginas do PDF. Considere o seguinte trecho de código que funciona muito rápido.

```python
// Para exemplos completos e arquivos de dados, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// Loop através de todas as páginas do Documento PDF
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
    "name": "Aspose.PDF para Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
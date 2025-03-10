---
title: Substituir Texto em PDF
linktitle: Substituir Texto em PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/replace-text-in-pdf/
description: Saiba mais sobre várias maneiras de substituir e remover texto da biblioteca Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text in PDF",
    "alternativeHeadline": "Efficiently Modify Text Across PDF Pages with Ease",
    "abstract": "O recurso Substituir Texto em PDF na biblioteca Aspose.PDF for .NET permite que os usuários localizem e substituam eficientemente texto em todo um documento PDF ou dentro de regiões específicas da página. Ele suporta capacidades avançadas, incluindo substituição de texto com base em expressões regulares, rearranjo automático do conteúdo da página após as substituições e a capacidade de remover fontes não utilizadas, melhorando a experiência de edição do documento.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2744",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "Saiba mais sobre várias maneiras de substituir e remover texto da biblioteca Aspose.PDF for .NET."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Substituir Texto em todas as páginas do documento PDF

{{% alert color="primary" %}}

Você pode tentar encontrar e substituir o texto no documento usando Aspose.PDF e obter os resultados online neste [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Para substituir texto em todas as páginas de um documento PDF, você primeiro precisa usar o TextFragmentAbsorber para encontrar a frase específica que deseja substituir. Depois disso, você precisa percorrer todos os TextFragments para substituir o texto e alterar quaisquer outros atributos. Uma vez feito isso, você só precisa salvar o PDF de saída usando o método Save do objeto Document. O seguinte trecho de código mostra como substituir texto em todas as páginas do documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for all the pages
        document.Pages.Accept(absorber);

        // Get the extracted text fragments
        var textFragmentCollection = absorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            // Update text and other properties
            textFragment.Text = "TEXT";
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
            textFragment.TextState.FontSize = 22;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
            textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextInAllPages_out.pdf");
    }
}
```

## Substituir Texto em uma região específica da página

Para substituir texto em uma região específica da página, primeiro, precisamos instanciar o objeto TextFragmentAbsorber, especificar a região da página usando a propriedade TextSearchOptions.Rectangle e, em seguida, iterar por todos os TextFragments para substituir o texto. Uma vez que essas operações sejam concluídas, precisamos apenas salvar o PDF de saída usando o método Save do objeto Document. O seguinte trecho de código mostra como substituir texto em todas as páginas do documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "programaticallyproducedpdf.pdf"))
    {
        // instantiate TextFragment Absorber object
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // search text within page bound
        absorber.TextSearchOptions.LimitToPageBounds = true;

        // specify the page region for TextSearch Options
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 100, 200, 200);

        // search text from first page of PDF file
        document.Pages[1].Accept(absorber);

        // iterate through individual TextFragment
        foreach (var textFragment in absorber.TextFragments)
        {
            // update text to blank characters
            textFragment.Text = "";
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextInParticularPageRegion_out.pdf");
    }
}
```

## Substituir Texto com Base em uma Expressão Regular

Se você deseja substituir algumas frases com base em uma expressão regular, primeiro precisa encontrar todas as frases que correspondem a essa expressão regular específica usando o TextFragmentAbsorber. Você terá que passar a expressão regular como um parâmetro para o construtor do TextFragmentAbsorber. Você também precisa criar um objeto TextSearchOptions que especifique se a expressão regular está sendo usada ou não. Uma vez que você obtenha as frases correspondentes nos TextFragments, precisa percorrer todas elas e atualizar conforme necessário. Finalmente, você precisa salvar o PDF atualizado usando o método Save do objeto Document. O seguinte trecho de código mostra como substituir texto com base em uma expressão regular.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextBasedOnARegularExpression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionPage.pdf"))
    {

        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

        // Set text search option to specify regular expression usage
        absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

        // Accept the absorber for a single page
        document.Pages[1].Accept(absorber);

        // Get the extracted text fragments
        var collection = absorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in collection)
        {
            // Update text and other properties
            textFragment.Text = "New Phrase";
            // Set to an instance of an object.
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
            textFragment.TextState.FontSize = 22;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
            textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextonRegularExpression_out.pdf");
    }
}
```

## Substituir fontes em arquivo PDF existente

A biblioteca Aspose.PDF for .NET suporta a capacidade de substituir texto em documentos PDF. No entanto, às vezes você tem a necessidade de substituir apenas a fonte que está sendo usada dentro do documento PDF. Assim, em vez de substituir o texto, apenas a fonte utilizada é substituída. Uma das sobrecargas do construtor do TextFragmentAbsorber aceita o objeto TextEditOptions como argumento e podemos usar o valor RemoveUnusedFonts da enumeração TextEditOptions.FontReplace para atender às nossas necessidades. O seguinte trecho de código mostra como substituir a fonte dentro do documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextPage.pdf"))
    {
        // Create text edit options
        var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);

        // Search text fragments and set edit option as remove unused fonts
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(options);

        // Accept the absorber for all the pages
        document.Pages.Accept(absorber);

        // Traverse through all the TextFragments
        foreach (var textFragment in absorber.TextFragments)
        {
            // If the font name is ArialMT, replace font name with Arial
            if (textFragment.TextState.Font.FontName == "Arial,Bold")
            {
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceFonts_out.pdf");
    }
}
```

## A Substituição de Texto deve reorganizar automaticamente o Conteúdo da Página

A biblioteca Aspose.PDF for .NET suporta o recurso de pesquisar e substituir texto dentro do arquivo PDF. No entanto, recentemente alguns clientes encontraram problemas durante a substituição de texto quando um determinado TextFragment é substituído por conteúdos menores e alguns espaços extras são exibidos no PDF resultante ou, no caso de o TextFragment ser substituído por uma string mais longa, as palavras sobrepõem o conteúdo existente da página. Portanto, a necessidade era introduzir um mecanismo que, uma vez que o texto dentro de um documento PDF é substituído, o conteúdo deve ser reorganizado.

Para atender aos cenários acima mencionados, a biblioteca Aspose.PDF for .NET foi aprimorada para que não apareçam tais problemas ao substituir texto dentro do arquivo PDF. O seguinte trecho de código mostra como substituir texto dentro do arquivo PDF e o conteúdo da página deve ser reorganizado automaticamente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutomaticallyReArrangePageContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // Create TextFragment Absorber object with regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
        document.Pages.Accept(absorber);

        // Replace each TextFragment
        foreach (var textFragment in absorber.TextFragments)
        {
            // Set font of text fragment being replaced
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            // Set font size
            textFragment.TextState.FontSize = 12;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
            // Replace the text with larger string than placeholder
            textFragment.Text = "This is a Larger String for the Testing of this issue";
        }

        // Save PDF document
        document.Save(dataDir + "AutomaticallyReArrangePageContents_out.pdf");
    }
}
```

## Renderizando Símbolos Substituíveis durante a criação do PDF

Símbolos substituíveis são símbolos especiais em uma string de texto que podem ser substituídos pelo conteúdo correspondente em tempo de execução. Os símbolos substituíveis atualmente suportados pelo novo Modelo de Objeto de Documento do namespace Aspose.PDF são `$P`, `$p`, `\n`, `\r`. O `$p` e o `$P` são usados para lidar com a numeração das páginas em tempo de execução. O `$p` é substituído pelo número da página onde a classe Paragraph atual está. O `$P` é substituído pelo número total de páginas no documento. Ao adicionar `TextFragment` à coleção de parágrafos dos documentos PDF, não suporta quebra de linha dentro do texto. No entanto, para adicionar texto com uma quebra de linha, use `TextFragment` com `TextParagraph`:

- Use "\r\n" ou Environment.NewLine em TextFragment em vez de um único "\n".
- Crie um objeto TextParagraph. Ele adicionará texto com divisão de linha.
- Adicione o TextFragment com TextParagraph.AppendLine.
- Adicione o TextParagraph com TextBuilder.AppendParagraph.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenderingReplaceableSymbols()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Initialize new TextFragment with text containing required newline markers
        Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

        // Set text fragment properties if necessary
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

        // Create TextParagraph object
        var par = new Aspose.Pdf.Text.TextParagraph();

        // Add new TextFragment to paragraph
        par.AppendLine(textFragment);

        // Set paragraph position
        par.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);

        // Add the TextParagraph using TextBuilder
        textBuilder.AppendParagraph(par);

        // Save PDF document
        document.Save(dataDir + "RenderingReplaceableSymbols_out.pdf");
    }
}
```

## Símbolos substituíveis na área de Cabeçalho/Rodapé

Símbolos substituíveis também podem ser colocados dentro da seção de Cabeçalho/Rodapé do arquivo PDF. Por favor, dê uma olhada no seguinte trecho de código para detalhes sobre como adicionar um símbolo substituível na seção de rodapé.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceableSymbolsInHeaderOrFooterArea()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Create margin info
        var marginInfo = new Aspose.Pdf.MarginInfo();
        marginInfo.Top = 90;
        marginInfo.Bottom = 50;
        marginInfo.Left = 50;
        marginInfo.Right = 50;
        // Assign the marginInfo instance to Margin property of sec1.PageInfo
        page.PageInfo.Margin = marginInfo;

        var headerFooterFirst = new Aspose.Pdf.HeaderFooter();
        page.Header = headerFooterFirst;
        headerFooterFirst.Margin.Left = 50;
        headerFooterFirst.Margin.Right = 50;

        // Instantiate a Text paragraph that will store the content to show as header
        var fragment1 = new Aspose.Pdf.Text.TextFragment("report title");
        fragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment1.TextState.FontSize = 16;
        fragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
        fragment1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        fragment1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        fragment1.TextState.LineSpacing = 5f;
        headerFooterFirst.Paragraphs.Add(fragment1);

        var fragment2 = new Aspose.Pdf.Text.TextFragment("Report_Name");
        fragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
        fragment2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        fragment2.TextState.LineSpacing = 5f;
        fragment2.TextState.FontSize = 12;
        headerFooterFirst.Paragraphs.Add(fragment2);

        // Create a HeaderFooter object for the section
        var headerFooterFoot = new Aspose.Pdf.HeaderFooter();

        // Set the HeaderFooter object to odd & even footer
        page.Footer = headerFooterFoot;
        headerFooterFoot.Margin.Left = 50;
        headerFooterFoot.Margin.Right = 50;

        // Add a text paragraph containing current page number of total number of pages
        var fragment3 = new Aspose.Pdf.Text.TextFragment("Generated on test date");
        var fragment4 = new Aspose.Pdf.Text.TextFragment("report name ");
        var fragment5 = new Aspose.Pdf.Text.TextFragment("Page $p of $P");

        // Instantiate a table object
        var table2 = new Aspose.Pdf.Table();

        // Add the table in paragraphs collection of the desired section
        headerFooterFoot.Paragraphs.Add(table2);

        // Set with column widths of the table
        table2.ColumnWidths = "165 172 165";

        // Create rows in the table and then cells in the rows
        var row3 = table2.Rows.Add();

        row3.Cells.Add();
        row3.Cells.Add();
        row3.Cells.Add();

        // Set the vertical allignment of the text as center alligned
        row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
        row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
        row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

        row3.Cells[0].Paragraphs.Add(fragment3);
        row3.Cells[1].Paragraphs.Add(fragment4);
        row3.Cells[2].Paragraphs.Add(fragment5);

        // Sec1.Paragraphs.Add(New Text("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL"))
        var table = new Aspose.Pdf.Table();

        table.ColumnWidths = "33% 33% 34%";
        table.DefaultCellPadding = new Aspose.Pdf.MarginInfo();
        table.DefaultCellPadding.Top = 10;
        table.DefaultCellPadding.Bottom = 10;

        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(table);

        // Set default cell border using BorderInfo object
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1f);

        // Set table border using another customized BorderInfo object
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1f);

        table.RepeatingRowsCount = 1;

        // Create rows in the table and then cells in the rows
        var row1 = table.Rows.Add();

        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add("col3");
        const string CRLF = "\r\n";
        for (int i = 0; i <= 10; i++)
        {
            var row = table.Rows.Add();
            row.IsRowBroken = true;
            for (int c = 0; c <= 2; c++)
            {
                Aspose.Pdf.Cell c1;
                if (c == 2)
                {
                    c1 = row.Cells.Add("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a" + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "Using Aspose.Total for Java developers can create a wide range of applications.");
                }
                else
                {
                    c1 = row.Cells.Add("item1" + c);
                }
                c1.Margin = new Aspose.Pdf.MarginInfo();
                c1.Margin.Left = 30;
                c1.Margin.Top = 10;
                c1.Margin.Bottom = 10;
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf");
    }
}
```

## Remover Fontes Não Utilizadas do Arquivo PDF

A biblioteca Aspose.PDF for .NET suporta o recurso de incorporar fontes ao criar um documento PDF, bem como a capacidade de incorporar fontes em arquivos PDF existentes. A partir da versão 7.3.0 da biblioteca Aspose.PDF for .NET, também permite remover fontes duplicadas ou não utilizadas de documentos PDF.

Para substituir fontes, use a seguinte abordagem:

1. Chame a classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber).
1. Chame o parâmetro TextEditOptions.FontReplace.RemoveUnusedFonts da classe TextFragmentAbsorber. (Isso remove fontes que se tornaram não utilizadas durante a substituição de fontes).
1. Defina a fonte individualmente para cada fragmento de texto.

O seguinte trecho de código substitui a fonte para todos os fragmentos de texto de todas as páginas do documento e remove fontes não utilizadas.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveUnusedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextPage.pdf"))
    {
        var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages.Accept(absorber);

        // Iterate through all the TextFragments
        foreach (var textFragment in absorber.TextFragments)
        {
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial, Bold");
        }

        // Save PDF document
        document.Save(dataDir + "RemoveUnusedFonts_out.pdf");
    }
}
```

## Remover Todo o Texto do Documento PDF

### Remover Todo o Texto usando Operadores

Em algumas operações de texto, você precisa remover todo o texto do documento PDF e, para isso, precisa definir o texto encontrado como um valor de string vazio, geralmente. O ponto é que mudar o texto para uma infinidade de fragmentos de texto invoca uma série de verificações e operações de ajuste de posição do texto. Elas são essenciais nos cenários de edição de texto. A dificuldade é que você não pode determinar quantos fragmentos de texto serão removidos no cenário em que eles são processados em um loop.

Portanto, recomendamos usar outra abordagem para o cenário de remoção de todo o texto das páginas PDF. Por favor, considere o seguinte trecho de código que funciona muito rápido.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveAllTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveAllText.pdf"))
    {
        // Loop through all pages of PDF Document
        for (int i = 1; i <= document.Pages.Count; i++)
        {
            var page = document.Pages[i];
            var operatorSelector = new Aspose.Pdf.OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
            // Select all text on the page
            page.Contents.Accept(operatorSelector);
            // Delete all text
            page.Contents.Delete(operatorSelector.Selected);
        }
        // Save PDF document
        document.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
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
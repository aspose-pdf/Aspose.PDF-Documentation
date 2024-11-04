---
title: Pesquisar e Obter Texto de Páginas de PDF
linktitle: Pesquisar e Obter Texto
type: docs
weight: 60
url: /python-net/search-and-get-text-from-pdf/
description: Este artigo explica como usar várias ferramentas para pesquisar e obter um texto do Aspose.PDF para .NET.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pesquisar e Obter Texto de Páginas de PDF",
    "alternativeHeadline": "Ferramentas para pesquisar e obter texto de Páginas de PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, pesquisar texto, obter texto de pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Este artigo explica como usar várias ferramentas para pesquisar e obter um texto do Aspose.PDF para .NET."
}
</script>


## Pesquisar e Obter Texto de Todas as Páginas de um Documento PDF

A classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) permite encontrar texto, correspondendo a uma determinada frase, de todas as páginas de um documento PDF. Para buscar texto em todo o documento, é necessário chamar o método Accept da coleção de Páginas. O método [Accept](https://reference.aspose.com/pdf/python-net/aspose.pdf.page/accept/methods/3) aceita um objeto TextFragmentAbsorber como parâmetro, que retorna uma coleção de objetos TextFragment. Você pode percorrer todos os fragmentos e obter suas propriedades como Texto, Posição (XIndent, YIndent), Nome da Fonte, Tamanho da Fonte, IsAccessible, IsEmbedded, IsSubset, ForegroundColor, etc.

O trecho de código a seguir mostra como buscar texto de todas as páginas.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Criar objeto TextAbsorber para encontrar todas as instâncias da frase de busca de entrada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// Aceitar o absorvedor para todas as páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obter os fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Percorrer os fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Texto : {0} ", textFragment.Text);
    Console.WriteLine("Posição : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Fonte - Nome : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Fonte - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Fonte - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Fonte - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Tamanho da Fonte : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Cor do Primeiro Plano : {0} ", textFragment.TextState.ForegroundColor);
}
```


Caso você precise pesquisar texto dentro de qualquer página específica de um PDF, especifique o número da página na coleção de páginas da instância do Documento e chame o método Accept para essa página (conforme mostrado na linha de código abaixo).

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Aceitar o absorvedor para uma página específica
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Pesquisar e Obter Segmentos de Texto de Todas as Páginas do Documento PDF

Para pesquisar segmentos de texto em todas as páginas, você primeiro precisa obter os objetos TextFragment do documento.
 TextFragmentAbsorber permite que você encontre texto, correspondendo a uma frase específica, em todas as páginas de um documento PDF. Para buscar texto de todo o documento, você precisa chamar o método Accept da coleção Pages. O método Accept recebe um objeto TextFragmentAbsorber como parâmetro, que retorna uma coleção de objetos TextFragment. Uma vez que a TextFragmentCollection é obtida do documento, você precisa percorrer essa coleção e obter a TextSegmentCollection de cada objeto TextFragment. Depois disso, você pode obter todas as propriedades do objeto TextSegment individual. O seguinte trecho de código mostra como buscar segmentos de texto de todas as páginas.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// Criar objeto TextAbsorber para encontrar todas as instâncias da frase de busca de entrada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// Aceitar o absorber para todas as páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);
// Obter os fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Percorrer os fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("Texto : {0} ", textSegment.Text);
        Console.WriteLine("Posição : {0} ", textSegment.Position);
        Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("Fonte - Nome : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("Fonte - IsAccessible : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("Fonte - IsEmbedded : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("Fonte - IsSubset : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("Tamanho da Fonte : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("Cor do Primeiro Plano : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```

Para buscar e obter TextSegments de uma página específica de um PDF, você precisa especificar o índice da página ao chamar o método Accept(..). Por favor, veja as seguintes linhas de código.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Aceitar o absorvedor para todas as páginas
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Buscar e Obter Texto de todas as páginas usando Expressão Regular

TextFragmentAbsorber ajuda você a buscar e recuperar texto, de todas as páginas, baseando-se em uma expressão regular.
 Primeiro, você precisa passar uma expressão regular para o construtor do TextFragmentAbsorber como a frase. Depois disso, você deve definir a propriedade TextSearchOptions do objeto TextFragmentAbsorber. Esta propriedade requer um objeto TextSearchOptions e você precisa passar true como um parâmetro para seu construtor ao criar novos objetos. Como você deseja recuperar o texto correspondente de todas as páginas, é necessário chamar o método Accept da coleção Pages. TextFragmentAbsorber retorna um TextFragmentCollection contendo todos os fragmentos que correspondem aos critérios especificados pela expressão regular. O trecho de código a seguir mostra como procurar e obter texto de todas as páginas com base em uma expressão regular.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// Criar objeto TextAbsorber para encontrar todas as frases que correspondem à expressão regular
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Como 1999-2000

// Definir a opção de pesquisa de texto para especificar o uso de expressão regular
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Aceitar o absorvedor para todas as páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obter os fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Percorrer os fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Texto : {0} ", textFragment.Text);
    Console.WriteLine("Posição : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Fonte - Nome : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Fonte - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Fonte - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Fonte - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Tamanho da Fonte : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Cor do Primeiro Plano : {0} ", textFragment.TextState.ForegroundColor);
}
```

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// Para buscar uma correspondência exata de uma palavra, você pode considerar usar expressões regulares.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// Para buscar uma string em maiúsculas ou minúsculas, você pode considerar usar expressões regulares.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// Para buscar todas as strings (analisar todas as strings) dentro do documento PDF, por favor, tente usar a seguinte expressão regular.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// Encontre a correspondência da string de busca e obtenha qualquer coisa após a string até a quebra de linha.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// Por favor, use a seguinte expressão regular para encontrar o texto após a correspondência do regex.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// Para buscar Hyperlink/URL's dentro do documento PDF, por favor, tente usar a seguinte expressão regular.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```


## Buscar Texto com base em Regex e Adicionar Hiperlink

Se você deseja adicionar um hiperlink sobre uma frase de texto com base em uma expressão regular, primeiro encontre todas as frases que correspondem a essa expressão regular específica usando TextFragmentAbsorber e adicione um hiperlink sobre essas frases.

Para encontrar uma frase e adicionar um hiperlink sobre ela:

1. Passe a expressão regular como um parâmetro para o construtor do TextFragmentAbsorber.
2. Crie um objeto TextSearchOptions que especifica se a expressão regular é usada ou não.
3. Obtenha as frases correspondentes em TextFragments.
4. Percorra as correspondências para obter suas dimensões retangulares, altere a cor do primeiro plano para azul (opcional - para fazê-lo parecer um hiperlink) e crie um link usando o método CreateWebLink(..) da classe PdfContentEditor.
5. Salve o PDF atualizado usando o método Save do objeto Document.
O snippet de código a seguir mostra como buscar texto dentro de um arquivo PDF usando uma expressão regular e adicionar hiperlinks sobre as correspondências.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Crie um objeto absorvedor para encontrar todas as instâncias da frase de pesquisa de entrada
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// Habilitar pesquisa por expressão regular
absorber.TextSearchOptions = new TextSearchOptions(true);
// Abra o documento
PdfContentEditor editor = new PdfContentEditor();
// Vincular arquivo PDF de origem
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// Aceitar o absorvedor para a página
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// Percorrer os fragmentos
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
        (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
        (int)Math.Round(textFragment.Rectangle.Height + 1));
    Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
    editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
    editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
        (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
}

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```


## Pesquisar e Desenhar Retângulo ao redor de cada TextFragment

Aspose.PDF para .NET suporta a funcionalidade de pesquisar e obter as coordenadas de cada caractere ou fragmento de texto. Portanto, para ter certeza sobre as coordenadas retornadas para cada caractere, podemos considerar destacar (adicionando retângulo) ao redor de cada caractere.

No caso de um parágrafo de texto, você pode considerar usar alguma expressão regular para determinar a quebra do parágrafo e desenhar um retângulo ao redor dele. Por favor, veja o seguinte trecho de código. O seguinte trecho de código obtém as coordenadas de cada caractere e cria um retângulo ao redor de cada caractere.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Criar objeto TextAbsorber para encontrar todas as frases que correspondem à expressão regular

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```


## Destaque cada caractere no documento PDF

{{% alert color="primary" %}}

Você pode tentar buscar texto em um documento usando Aspose.PDF e obter os resultados online neste [link](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF para .NET suporta o recurso de buscar e obter as coordenadas de cada caractere ou fragmentos de texto. Portanto, para ter certeza sobre as coordenadas sendo retornadas para cada caractere, podemos considerar destacá-los (adicionando retângulo) ao redor de cada caractere. O seguinte trecho de código obtém as coordenadas de cada caractere e cria um retângulo ao redor de cada um.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
Page page = pdfDocument.Pages[1];
// Criar objeto TextAbsorber para encontrar todas as palavras
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// Obter os fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Loop através dos fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    if (i == 0)
    {
        gr.DrawRectangle(
        Pens.Yellow,
        (float)textFragment.Position.XIndent,
        (float)textFragment.Position.YIndent,
        (float)textFragment.Rectangle.Width,
        (float)textFragment.Rectangle.Height);

        for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
        {
TextSegment segment = textFragment.Segments[segNum];

for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
{
    CharInfo characterInfo = segment.Characters[charNum];

    Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
    Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
          "   TextFragment URY = " + textFragment.Rectangle.URY);

    gr.DrawRectangle(
    Pens.Black,
    (float)characterInfo.Rectangle.LLX,
    (float)characterInfo.Rectangle.LLY,
    (float)characterInfo.Rectangle.Width,
    (float)characterInfo.Rectangle.Height);
}

gr.DrawRectangle(
Pens.Green,
(float)segment.Rectangle.LLX,
(float)segment.Rectangle.LLY,
(float)segment.Rectangle.Width,
(float)segment.Rectangle.Height);
        }
    }
}
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```


## Adicionar e Pesquisar Texto Oculto

Às vezes, queremos adicionar texto oculto em um documento PDF e, em seguida, pesquisar esse texto oculto e usar sua posição para pós-processamento. Para sua conveniência, o Aspose.PDF para .NET fornece essas habilidades. Você pode adicionar texto oculto durante a geração do documento. Além disso, você pode encontrar texto oculto usando o TextFragmentAbsorber. Para adicionar texto oculto, defina TextState.Invisible como 'true' para o texto adicionado. O TextFragmentAbsorber encontra todo o texto que corresponde ao padrão (se especificado). É o comportamento padrão que não pode ser alterado. Para verificar se o texto encontrado é realmente invisível, a propriedade TextState.Invisible pode ser usada. O trecho de código abaixo mostra como usar esse recurso.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//Criar documento com texto oculto
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("Este é um texto comum.");
TextFragment frag2 = new TextFragment("Este é um texto invisível.");

//Definir propriedade de texto - invisível
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//Pesquisar texto no documento
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //Fazer algo com os fragmentos
    Console.WriteLine("Texto '{0}' na posição {1} invisibilidade: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```


## Procurando Texto Com .NET Regex

Aspose.PDF para .NET fornece a capacidade de pesquisar documentos usando a opção padrão .NET Regex. O TextFragmentAbsorber pode ser usado para este propósito, como mostrado no exemplo de código abaixo.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Criar objeto Regex para encontrar todas as palavras
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// Abrir documento
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// Obter uma página específica
Page page = document.Pages[1];

// Criar objeto TextAbsorber para encontrar todas as instâncias do regex de entrada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// Aceitar o absorvedor para a página
page.Accept(textFragmentAbsorber);

// Obter os fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Percorrer os fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
}
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Biblioteca .NET",
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
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
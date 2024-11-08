---
title: Formatação de Texto dentro de PDF usando C#
linktitle: Formatação de Texto dentro de PDF
type: docs
weight: 30
url: /pt/net/text-formatting-inside-pdf/
description: Esta página explica como formatar texto dentro do seu arquivo PDF. Inclui adicionar indentação de linha, adicionar borda de texto, adicionar texto sublinhado, entre outros.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatação de Texto dentro de PDF usando C#",
    "alternativeHeadline": "Como formatar texto em arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos em PDF",
    "keywords": "pdf, c#, formatar texto em pdf",
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
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta página explica como formatar texto dentro do seu arquivo PDF. Inclui adicionar indentação de linha, adicionar borda de texto, adicionar texto sublinhado, entre outros."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Como adicionar Indentação de Linha ao PDF

Aspose.PDF para .NET oferece a propriedade SubsequentLinesIndent na classe [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions). Que pode ser usada para especificar a indentação de linha em cenários de geração de PDF com coleções de TextFragment e Paragraphs.

Por favor, use o seguinte trecho de código para usar a propriedade:

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Criar novo objeto de documento
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// Inicialize TextFormattingOptions para o fragmento de texto e especifique o valor SubsequentLinesIndent
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf");
```
## Como adicionar borda ao texto

O trecho de código a seguir mostra como adicionar uma borda a um texto usando TextBuilder e configurando a propriedade DrawTextRectangleBorder de TextState:

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Criar novo objeto de documento
Document pdfDocument = new Document();
// Obter página específica
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Criar fragmento de texto
TextFragment textFragment = new TextFragment("texto principal");
textFragment.Position = new Position(100, 600);
// Definir propriedades do texto
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Definir propriedade StrokingColor para desenhar borda (contorno) ao redor do retângulo do texto
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// Definir valor da propriedade DrawTextRectangleBorder para true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// Salvar o documento
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```
## Como adicionar Texto Sublinhado

O seguinte trecho de código mostra como adicionar texto sublinhado ao criar um novo arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Criar objeto de documentação
Document pdfDocument = new Document();
// Adicionar página ao documento PDF
pdfDocument.Pages.Add();
// Criar TextBuilder para a primeira página
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment com texto de exemplo
TextFragment fragment = new TextFragment("Mensagem de teste");
// Definir a fonte para TextFragment
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// Definir o formato do texto como Sublinhado
fragment.TextState.Underline = true;
// Especificar a posição onde o TextFragment precisa ser colocado
fragment.Position = new Position(10, 800);
// Anexar TextFragment ao arquivo PDF
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// Salvar o documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Como adicionar borda ao redor do texto adicionado

Você tem controle sobre a aparência do texto que adiciona. O exemplo abaixo mostra como adicionar uma borda ao redor de um texto que você adicionou, desenhando um retângulo ao redor dele. Saiba mais sobre a classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// Salvar o documento PDF resultante.
editor.Save(dataDir);
```

## Como adicionar quebra de linha
## Como adicionar uma quebra de linha

TextFragment não suporta quebra de linha dentro do texto. No entanto, para adicionar texto com quebra de linha, por favor use TextFragment com TextParagraph:

- use "\r\n" ou Environment.NewLine em TextFragment em vez de "\n" único;
- crie um objeto TextParagraph. Ele adicionará texto com divisão de linha;
- adicione o TextFragment com TextParagraph.AppendLine;
- adicione o TextParagraph com TextBuilder.AppendParagraph.
Por favor, use o trecho de código abaixo.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Inicialize novo TextFragment com texto contendo os marcadores de nova linha necessários
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Nome do Candidato: " + Environment.NewLine + " Joe Smoe");

// Defina as propriedades do fragmento de texto se necessário
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Crie objeto TextParagraph
TextParagraph par = new TextParagraph();

// Adicione novo TextFragment ao parágrafo
par.AppendLine(textFragment);

// Defina a posição do parágrafo
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Crie objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Adicione o TextParagraph usando TextBuilder
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// Salve o documento PDF resultante.
pdfApplicationDoc.Save(dataDir);
```
## Como adicionar Texto Tachado

A classe TextState fornece capacidades para definir a formatação de TextFragments sendo colocados dentro de um documento PDF. Você pode usar esta classe para definir a formatação de texto como Negrito, Itálico, Sublinhado e, a partir desta versão, a API forneceu capacidades para marcar a formatação de texto como Tachado. Por favor, tente usar o seguinte trecho de código para adicionar TextFragment com formatação Tachada.

Por favor, use o trecho de código completo:

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Abrir documento
Document pdfDocument = new Document();
// Obter página específica
Page pdfPage = (Page)pdfDocument.Pages.Add();

// Criar fragmento de texto
TextFragment textFragment = new TextFragment("texto principal");
textFragment.Position = new Position(100, 600);

// Definir propriedades do texto
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Definir propriedade StrikeOut
textFragment.TextState.StrikeOut = true;
// Marcar texto como Negrito
textFragment.TextState.FontStyle = FontStyles.Bold;

// Criar objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Anexar o fragmento de texto à página PDF
textBuilder.AppendText(textFragment);


dataDir = dataDir + "AddStrikeOutText_out.pdf";

// Salvar o documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Aplicar Sombreamento Gradiente ao Texto

A formatação de texto foi ainda mais aprimorada na API para cenários de edição de texto e agora você pode adicionar texto com espaço de cores de padrão dentro do documento PDF. A classe Aspose.Pdf.Color foi ainda mais aprimorada com a introdução da nova propriedade de PatternColorSpace, que pode ser usada para especificar cores de sombreamento para o texto. Esta nova propriedade adiciona diferentes Sombreamentos Gradientes ao texto, por exemplo, Sombreamento Axial, Sombreamento Radial (Tipo 3) como mostrado no seguinte trecho de código:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // Criar nova cor com espaço de cores de padrão
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```
>Para aplicar um Gradiente Radial, você pode definir a propriedade 'PatternColorSpace' como 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' no trecho de código acima.

## Como alinhar texto ao conteúdo flutuante

O Aspose.PDF suporta a configuração do alinhamento de texto para conteúdos dentro de um elemento Caixa Flutuante. As propriedades de alinhamento da instância Aspose.Pdf.FloatingBox podem ser usadas para alcançar isso conforme mostrado no exemplo de código a seguir.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Biblioteca .NET",
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


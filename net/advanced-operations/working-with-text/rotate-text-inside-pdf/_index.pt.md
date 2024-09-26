---
title: Rotacionar Texto Dentro de PDF usando C#
linktitle: Rotacionar Texto Dentro de PDF
type: docs
weight: 50
url: /net/rotate-text-inside-pdf/
description: Aprenda diferentes maneiras de rotacionar texto para PDF. Aspose.PDF permite rotacionar texto em qualquer ângulo, rotacionar fragmento de texto ou um parágrafo inteiro.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotacionar Texto Dentro de PDF usando C#",
    "alternativeHeadline": "Como rotacionar Texto em Arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, geração de documentos",
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
    "url": "/net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-text-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Aprenda diferentes maneiras de rotacionar texto para PDF. Aspose.PDF permite rotacionar texto em qualquer ângulo, rotacionar fragmento de texto ou um parágrafo inteiro."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Rotacionar Texto Dentro do PDF Usando a Propriedade de Rotação

Ao usar a propriedade de Rotação da Classe [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment), você pode rotacionar o texto em vários ângulos. A rotação de texto pode ser usada em diferentes cenários de geração de documentos. Você pode especificar o ângulo de rotação em graus para rotacionar o texto conforme sua necessidade. Por favor, verifique os diferentes cenários a seguir, nos quais você pode implementar a rotação de texto.

## Implementar Rotação Usando TextFragment e TextBuilder

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá até https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inicializa o objeto documento
Document pdfDocument = new Document();
// Obter página específica
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Criar fragmento de texto
TextFragment textFragment1 = new TextFragment("texto principal");
textFragment1.Position = new Position(100, 600);
// Definir propriedades do texto
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Criar fragmento de texto rotacionado
TextFragment textFragment2 = new TextFragment("texto rotacionado");
textFragment2.Position = new Position(200, 600);
// Definir propriedades do texto
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// Criar fragmento de texto rotacionado
TextFragment textFragment3 = new TextFragment("texto rotacionado");
textFragment3.Position = new Position(300, 600);
// Definir propriedades do texto
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// criar objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Anexar o fragmento de texto à página PDF
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// Salvar documento
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```
## Implementação de Rotação usando TextParagraph e TextBuilder (Fragmentos Rotacionados)

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inicializa o objeto do documento
Document pdfDocument = new Document();
// Obtém uma página específica
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// Cria um fragmento de texto
TextFragment textFragment1 = new TextFragment("texto rotacionado");
// Define as propriedades do texto
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Define a rotação
textFragment1.TextState.Rotation = 45;
// Cria um fragmento de texto
TextFragment textFragment2 = new TextFragment("texto principal");
// Define as propriedades do texto
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Cria um fragmento de texto
TextFragment textFragment3 = new TextFragment("outro texto rotacionado");
// Define as propriedades do texto
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Define a rotação
textFragment3.TextState.Rotation = -45;
// Anexa os fragmentos de texto ao parágrafo
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// Cria objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Anexa o parágrafo de texto à página PDF
textBuilder.AppendParagraph(paragraph);
// Salva o documento
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```
## Implementar Rotação usando TextFragment e Page.Paragraphs

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inicializar objeto documento
Document pdfDocument = new Document();
// Obter página específica
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Criar fragmento de texto
TextFragment textFragment1 = new TextFragment("texto principal");
// Definir propriedades do texto
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Criar fragmento de texto
TextFragment textFragment2 = new TextFragment("texto rotacionado");
// Definir propriedades do texto
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Definir rotação
textFragment2.TextState.Rotation = 315;
// Criar fragmento de texto
TextFragment textFragment3 = new TextFragment("texto rotacionado");
// Definir propriedades do texto
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Definir rotação
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// Salvar documento
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```
## Implementar Rotação usando TextParagraph e TextBuilder (Parágrafo Inteiro Rotacionado)

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Inicializa o objeto documento
Document pdfDocument = new Document();
// Obtém uma página específica
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // Especifica a rotação
    paragraph.Rotation = i * 90 + 45;
    // Cria um fragmento de texto
    TextFragment textFragment1 = new TextFragment("Texto do Parágrafo");
    // Cria um fragmento de texto
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Cria um fragmento de texto
    TextFragment textFragment2 = new TextFragment("Segunda linha do texto");
    // Define as propriedades do texto
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Cria um fragmento de texto
    TextFragment textFragment3 = new TextFragment("E mais um pouco de texto...");
    // Define as propriedades do texto
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // Cria objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Anexa o fragmento de texto à página do PDF
    textBuilder.AppendParagraph(paragraph);
}
// Salva o documento
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
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


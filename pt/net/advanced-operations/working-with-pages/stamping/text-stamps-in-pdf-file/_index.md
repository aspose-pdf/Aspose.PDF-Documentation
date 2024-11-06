---
title: Adicionar selos de texto em PDF C#
linktitle: Selos de texto em arquivo PDF
type: docs
weight: 20
url: pt/net/text-stamps-in-the-pdf-file/
description: Adicione um selo de texto a um documento PDF usando a classe TextStamp com a biblioteca Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar selos de texto em PDF C#",
    "alternativeHeadline": "Adicionar selos de texto em PDF C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Adicione um selo de texto a um documento PDF usando a classe TextStamp com a biblioteca Aspose.PDF para .NET."
}
</script>
## Adicionar Carimbo de Texto com C#

Você pode usar a classe [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) para adicionar um carimbo de texto em um arquivo PDF. A classe TextStamp fornece propriedades necessárias para criar um carimbo baseado em texto como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar um carimbo de texto, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Página para adicionar o carimbo no PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

O seguinte trecho de código mostra como adicionar um carimbo de texto no arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "AddTextStamp.pdf");

// Criar carimbo de texto
TextStamp textStamp = new TextStamp("Sample Stamp");
// Definir se o carimbo é de fundo
textStamp.Background = true;
// Definir origem
textStamp.XIndent = 100;
textStamp.YIndent = 100;
// Rotacionar carimbo
textStamp.Rotate = Rotation.on90;
// Definir propriedades do texto
textStamp.TextState.Font = FontRepository.FindFont("Arial");
textStamp.TextState.FontSize = 14.0F;
textStamp.TextState.FontStyle = FontStyles.Bold;
textStamp.TextState.FontStyle = FontStyles.Italic;
textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Aqua);
// Adicionar carimbo à página específica
pdfDocument.Pages[1].AddStamp(textStamp);

dataDir = dataDir + "AddTextStamp_out.pdf";
// Salvar documento de saída
pdfDocument.Save(dataDir);
```
## Definir alinhamento para o objeto TextStamp

Adicionar marcas d'água a documentos PDF é uma das funcionalidades frequentemente solicitadas e o Aspose.PDF para .NET é totalmente capaz de adicionar marcas d'água de Imagem e de Texto. Temos uma classe chamada [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) que oferece a funcionalidade de adicionar carimbos de texto sobre o arquivo PDF. Recentemente, surgiu a necessidade de suportar a funcionalidade de especificar o alinhamento do texto ao usar o objeto TextStamp. Portanto, para atender a essa necessidade, introduzimos a propriedade TextAlignment na classe TextStamp. Usando esta propriedade, podemos especificar o alinhamento horizontal do texto.

Os seguintes trechos de código mostram um exemplo de como carregar um documento PDF existente e adicionar TextStamp sobre ele.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Instanciar objeto Document com arquivo de entrada
Document doc = new Document(dataDir+ "DefineAlignment.pdf");
// Instanciar objeto FormattedText com string de exemplo
FormattedText text = new FormattedText("This");
// Adicionar nova linha de texto ao FormattedText
text.AddNewLineText("is sample");
text.AddNewLineText("Center Aligned");
text.AddNewLineText("TextStamp");
text.AddNewLineText("Object");
// Criar objeto TextStamp usando FormattedText
TextStamp stamp = new TextStamp(text);
// Especificar o Alinhamento Horizontal do carimbo de texto como Centralizado
stamp.HorizontalAlignment = HorizontalAlignment.Center;
// Especificar o Alinhamento Vertical do carimbo de texto como Centralizado
stamp.VerticalAlignment = VerticalAlignment.Center;
// Especificar o Alinhamento Horizontal do Texto do TextStamp como Centralizado
stamp.TextAlignment = HorizontalAlignment.Center;
// Definir margem superior para o objeto carimbo
stamp.TopMargin = 20;
// Adicionar o objeto carimbo na primeira página do documento
doc.Pages[1].AddStamp(stamp);

dataDir = dataDir + "StampedPDF_out.pdf";
// Salvar o documento atualizado
doc.Save(dataDir);
```
## Preencher Texto com Contorno como Carimbo em Arquivo PDF

Implementamos a configuração do modo de renderização para cenários de adição e edição de texto. Para renderizar texto com contorno, por favor crie um objeto TextState e defina RenderingMode para TextRenderingMode.StrokeText e também selecione a cor para a propriedade StrokingColor. Posteriormente, vincule o TextState ao carimbo usando o método BindTextState().

O seguinte trecho de código demonstra a adição de Texto com Preenchimento e Contorno:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
// Criar objeto TextState para transferir propriedades avançadas
TextState ts = new TextState();
// Definir cor para o contorno
ts.StrokingColor = Color.Gray;
// Definir modo de renderização de texto
ts.RenderingMode = TextRenderingMode.StrokeText;
// Carregar um documento PDF de entrada
Facades.PdfFileStamp fileStamp = new Facades.PdfFileStamp(new Aspose.Pdf.Document(dataDir + "input.pdf"));

Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
stamp.BindLogo(new Facades.FormattedText("PAGO EM CHEIO", System.Drawing.Color.Gray, "Arial", Facades.EncodingType.Winansi, true, 78));

// Vincular TextState
stamp.BindTextState(ts);
// Definir origem X,Y
stamp.SetOrigin(100, 100);
stamp.Opacity = 5;
stamp.BlendingSpace = Facades.BlendingColorSpace.DeviceRGB;
stamp.Rotation = 45.0F;
stamp.IsBackground = false;
// Adicionar Carimbo
fileStamp.AddStamp(stamp);
fileStamp.Save(dataDir + "ouput_out.pdf");
fileStamp.Close();
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para .NET Library",
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


---
title: Adicionar Cabeçalho e Rodapé ao PDF
linktitle: Adicionar Cabeçalho e Rodapé ao PDF
type: docs
weight: 70
url: /pt/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para .NET permite que você adicione cabeçalhos e rodapés ao seu arquivo PDF usando a classe TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Cabeçalho e Rodapé ao PDF",
    "alternativeHeadline": "Como adicionar Cabeçalho e Rodapé ao Arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, adicionar cabeçalho, adicionar rodapé em pdf",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET permite que você adicione cabeçalhos e rodapés ao seu arquivo PDF usando a classe TextStamp."
}
</script>

**Aspose.PDF para .NET** permite que você adicione cabeçalho e rodapé no seu arquivo PDF existente. Você pode adicionar imagens ou texto a um documento PDF. Além disso, tente adicionar diferentes cabeçalhos em um arquivo PDF com C#.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Adicionando Texto no Cabeçalho do Arquivo PDF

Você pode usar a classe [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) para adicionar texto no cabeçalho de um arquivo PDF. A classe TextStamp fornece propriedades necessárias para criar um carimbo baseado em texto como tamanho da fonte, estilo da fonte e cor da fonte etc. Para adicionar texto no cabeçalho, você precisa criar um objeto Document e um objeto TextStamp usando propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Página para adicionar o texto no cabeçalho do PDF.

Você precisa configurar a propriedade TopMargin de forma que ajuste o texto na área do cabeçalho do seu PDF. Você também precisa configurar HorizontalAlignment para Center e VerticalAlignment para Top.

O seguinte trecho de código mostra como adicionar texto no cabeçalho de um arquivo PDF com C#.
O seguinte trecho de código mostra como adicionar texto no cabeçalho de um arquivo PDF com C#.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir + "TextinHeader.pdf");

// Criar cabeçalho
TextStamp textStamp = new TextStamp("Texto do Cabeçalho");
// Definir propriedades do selo
textStamp.TopMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Top;
// Adicionar cabeçalho em todas as páginas
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// Salvar documento atualizado
pdfDocument.Save(dataDir + "TextinHeader_out.pdf");
```

## Adicionando Texto no Rodapé do Arquivo PDF

Você pode usar a classe TextStamp para adicionar texto no rodapé de um arquivo PDF.
Você pode usar a classe TextStamp para adicionar texto no rodapé de um arquivo PDF.

{{% alert color="primary" %}}

Você precisa configurar a propriedade Margem Inferior de modo que ajuste o texto na área do rodapé do seu PDF. Você também precisa definir HorizontalAlignment para Centro e VerticalAlignment para Baixo

{{% /alert %}}

O seguinte trecho de código mostra como adicionar texto no rodapé de um arquivo PDF com C#.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "TextinFooter.pdf");
// Criar rodapé
TextStamp textStamp = new TextStamp("Texto do Rodapé");
// Definir propriedades do selo
textStamp.BottomMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Adicionar rodapé em todas as páginas
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// Salvar arquivo de saída
doc.Save(dataDir + "TextinFooter_out.pdf");
```
## Adicionando Imagem no Cabeçalho de um Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) para adicionar uma imagem no cabeçalho de um arquivo PDF. A classe Image Stamp fornece propriedades necessárias para criar um carimbo baseado em imagem como tamanho da fonte, estilo da fonte e cor da fonte etc. Para adicionar uma imagem no cabeçalho, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) da Página para adicionar a imagem no cabeçalho do PDF.

{{% alert color="primary" %}}

Você precisa definir a propriedade TopMargin de tal forma que ajuste a imagem na área do cabeçalho do seu PDF. Você também precisa definir HorizontalAlignment para Center e VerticalAlignment para Top.

{{% /alert %}}

O seguinte trecho de código mostra como adicionar uma imagem no cabeçalho de um arquivo PDF com C#.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "ImageinHeader.pdf");

// Criar cabeçalho
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Definir propriedades do carimbo
imageStamp.TopMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Top;
// Adicionar cabeçalho em todas as páginas
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// Salvar arquivo de saída
doc.Save(dataDir + "ImageinHeader_out.pdf");
```
## Adicionando Imagem no Rodapé do Arquivo PDF

Você pode usar a classe Image Stamp para adicionar uma imagem no rodapé de um arquivo PDF. A classe Image Stamp fornece propriedades necessárias para criar um carimbo baseado em imagem como tamanho da fonte, estilo da fonte e cor da fonte etc. Para adicionar uma imagem no rodapé, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da página para adicionar a imagem no rodapé do PDF.

{{% alert color="primary" %}}

Você precisa configurar a propriedade [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) de modo que ela ajuste a imagem na área do rodapé do seu PDF. Você também precisa definir [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) para `Center` e [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) para `Bottom`.

{{% /alert %}}

O seguinte trecho de código mostra como adicionar imagem no rodapé de um arquivo PDF com C#.
O seguinte trecho de código mostra como adicionar uma imagem no rodapé de um arquivo PDF com C#.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "ImageInFooter.pdf");
// Criar rodapé
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Definir propriedades do selo
imageStamp.BottomMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Adicionar rodapé em todas as páginas
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// Salvar arquivo de saída
doc.Save(dataDir + "ImageInFooter_out.pdf");
```

## Adicionando diferentes Cabeçalhos em um único Arquivo PDF

Sabemos que podemos adicionar TextStamp na seção de Cabeçalho/Rodapé do documento usando as propriedades TopMargin ou Bottom Margin, mas às vezes podemos ter a necessidade de adicionar múltiplos cabeçalhos/rodapés em um único documento PDF.
Sabemos que podemos adicionar TextStamp na seção de cabeçalho/rodapé do documento usando as propriedades TopMargin ou Bottom Margin, mas às vezes podemos ter a necessidade de adicionar vários cabeçalhos/rodapés em um único documento PDF.

Para realizar essa necessidade, criaremos objetos TextStamp individuais (o número de objetos depende do número de cabeçalhos/rodapés necessários) e os adicionaremos ao documento PDF. Também podemos especificar diferentes informações de formatação para cada objeto de carimbo. No exemplo a seguir, criamos um objeto Document e três objetos TextStamp e, em seguida, usamos o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) da Página para adicionar o texto na seção de cabeçalho do PDF. O seguinte trecho de código mostra como adicionar uma imagem no rodapé de um arquivo PDF com Aspose.PDF para .NET.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento fonte
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddingDifferentHeaders.pdf");

// Criar três carimbos
Aspose.Pdf.TextStamp stamp1 = new Aspose.Pdf.TextStamp("Cabeçalho 1");
Aspose.Pdf.TextStamp stamp2 = new Aspose.Pdf.TextStamp("Cabeçalho 2");
Aspose.Pdf.TextStamp stamp3 = new Aspose.Pdf.TextStamp("Cabeçalho 3");

// Definir alinhamento do carimbo (posicionar o carimbo no topo da página, centralizado horizontalmente)
stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Especificar o estilo da fonte como Negrito
stamp1.TextState.FontStyle = FontStyles.Bold;
// Definir a cor de primeiro plano do texto como vermelho
stamp1.TextState.ForegroundColor = Color.Red;
// Especificar o tamanho da fonte como 14
stamp1.TextState.FontSize = 14;

// Agora precisamos definir o alinhamento vertical do segundo objeto de carimbo como Topo
stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Definir informações de alinhamento horizontal para o carimbo como Centralizado
stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Definir o fator de zoom para o objeto de carimbo
stamp2.Zoom = 10;

// Definir a formatação do terceiro objeto de carimbo
// Especificar informações de alinhamento vertical para o objeto de carimbo como TOPO
stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Definir as informações de alinhamento horizontal para o objeto de carimbo como Centralizado
stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Definir o ângulo de rotação para o objeto de carimbo
stamp3.RotateAngle = 35;
// Definir rosa como cor de fundo para o carimbo
stamp3.TextState.BackgroundColor = Color.Pink;
// Alterar as informações da fonte do carimbo para Verdana
stamp3.TextState.Font = FontRepository.FindFont("Verdana");
// O primeiro carimbo é adicionado na primeira página;
doc.Pages[1].AddStamp(stamp1);
// O segundo carimbo é adicionado na segunda página;
doc.Pages[2].AddStamp(stamp2);
// O terceiro carimbo é adicionado na terceira página.
doc.Pages[3].AddStamp(stamp3);
// Salvar o documento atualizado
doc.Save(dataDir + "MultiHeader_out.pdf");
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


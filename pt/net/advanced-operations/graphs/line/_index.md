---
title: Adicionar Objeto de Linha ao arquivo PDF
linktitle: Adicionar Linha
type: docs
weight: 40
url: /pt/net/add-line/
description: Este artigo explica como criar um objeto de linha em seu PDF usando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Objeto de Linha ao arquivo PDF",
    "alternativeHeadline": "Como criar Objeto de Linha em arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, linha no pdf",
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
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo explica como criar um objeto de linha em seu PDF usando Aspose.PDF para .NET."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Adicionar objeto Linha

Aspose.PDF para .NET suporta a funcionalidade de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Você também tem a vantagem de adicionar um objeto [Linha](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/line) onde você pode especificar o padrão de traço, cor e outras formatações para o elemento Linha.

Siga os passos abaixo:

1. Crie um novo [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document) PDF

1. Adicione [Página](https://reference.aspose.com/pdf/net/aspose.pdf/page) à coleção de páginas do arquivo PDF

1. Crie uma instância de [Gráfico](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph).

1. Adicione o objeto Gráfico à coleção de parágrafos da instância da página.

1. Crie uma instância de [Retângulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle).

1. Defina a largura da linha.
1. Salve seu arquivo PDF.

O seguinte trecho de código mostra como adicionar um objeto [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) que é preenchido com cor.

```csharp
        public static void AddLineObjectToPDF()
        {
            // Crie uma instância de Document
            var document = new Document();

            // Adicione página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Crie uma instância de Graph
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Adicione o objeto graph à coleção de parágrafos da instância de página
            page.Paragraphs.Add(graph);

            // Crie uma instância de Rectangle
            var line = new Line(new float[] { 100, 100, 200, 100 });

            // Especifique a cor de preenchimento para o objeto Graph
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            line.GraphInfo.DashPhase = 1;

            // Adicione o objeto rectangle à coleção de formas do objeto Graph
            graph.Shapes.Add(line);

            // Salve o arquivo PDF
            document.Save(_dataDir + "AddLineObject_out.pdf");
        }
```
![Adicionar Linha](add_line.png)

## Como adicionar Linha Pontilhada Tracejada ao seu documento PDF

```csharp
        public static void DashLengthInBlackAndDashLengthInWhite()
        {
            // Cria uma instância de Documento
            var document = new Document();

            // Adiciona página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Cria objeto de Desenho com dimensões específicas
            var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Adiciona objeto de desenho à coleção de parágrafos da instância de página
            page.Paragraphs.Add(canvas);

            // Cria objeto Linha
            var line = new Line(new float[] { 100, 100, 200, 100 });
            // Define cor para o objeto Linha
            line.GraphInfo.Color = Color.Red;
            // Especifica matriz de tracejado para o objeto linha
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            // Define a fase do tracejado para a instância Linha
            line.GraphInfo.DashPhase = 1;
            // Adiciona linha à coleção de formas do objeto de desenho
            canvas.Shapes.Add(line);
            // Salva o arquivo PDF
            document.Save(_dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
        }
```
Vamos verificar o resultado:

![Linha Tracejada](dash_line.png)

## Desenhar Linha Através da Página

Podemos também usar o objeto linha para desenhar uma cruz começando do canto Inferior-Esquerdo para o Superior-Direito e do canto Superior-Esquerdo para o Inferior-Direito.

Por favor, veja o seguinte trecho de código para realizar essa exigência.

```csharp
   public static void ExampleLineAcrossPage()
        {

            // Criar instância de Documento
            var document = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();
            // Definir margem da página em todos os lados como 0

            page.PageInfo.Margin.Left = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;

            // Criar objeto Gráfico com Largura e Altura iguais às dimensões da página
            var graph = new Aspose.Pdf.Drawing.Graph(
                (float)page.PageInfo.Width,
                (float)page.PageInfo.Height);

            // Criar primeiro objeto linha começando do canto Inferior-Esquerdo até o Superior-Direito da página
            var line = new Line(
                    new float[]{
                        (float)page.Rect.LLX, 0,
                        (float)page.PageInfo.Width,
                        (float)page.Rect.URY });

            // Adicionar linha à coleção de formas do objeto Gráfico
            graph.Shapes.Add(line);
            // Desenhar linha do canto Superior-Esquerdo da página até o Inferior-Direito da página
            var line2 = new Line(
                new float[]{ 0,
                    (float) page.Rect.URY,
                    (float) page.PageInfo.Width,
                    (float) page.Rect.LLX });

            // Adicionar linha à coleção de formas do objeto Gráfico
            graph.Shapes.Add(line2);

            // Adicionar objeto Gráfico à coleção de parágrafos da página
            page.Paragraphs.Add(graph);

            // Salvar arquivo PDF
            document.Save(_dataDir + "ExampleLineAcrossPage_out.pdf");
        }
```
![Desenho de Linha](draw_line.png)

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



---
title: Adicionar Objeto Elipse ao arquivo PDF
linktitle: Adicionar Elipse
type: docs
weight: 60
url: /net/add-ellipse/
description: Este artigo explica como criar um objeto Elipse em seu PDF usando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Objeto Elipse ao arquivo PDF",
    "alternativeHeadline": "Como criar Objeto Elipse em arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, elipse em pdf",
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
    "url": "/net/add-ellipse/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-ellipse/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo explica como criar um objeto Elipse em seu PDF usando Aspose.PDF para .NET."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Adicionar objeto Elipse

Aspose.PDF para .NET suporta a adição de objetos [Elipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) em documentos PDF. Ele também oferece o recurso de preencher o objeto elipse com uma determinada cor.

```csharp
 public static void Ellipse()
        {
            // Criar instância de Documento
            var document = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Criar objeto Drawing com dimensões específicas
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // Definir borda para o objeto Drawing
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(150, 100, 120, 60);
            ellipse1.GraphInfo.Color = Color.GreenYellow;
            ellipse1.Text = new TextFragment("Elipse");
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Aspose.Pdf.Drawing.Ellipse(50, 50, 18, 300);
            ellipse2.GraphInfo.Color = Color.DarkRed;

            graph.Shapes.Add(ellipse2);

            // Adicionar objeto Graph à coleção de parágrafos da página
            page.Paragraphs.Add(graph);

            // Salvar arquivo PDF
            document.Save(_dataDir + "DrawingEllipse_out.pdf");

        }
```
![Adicionar Elipse](ellipse.png)

## Criar Objeto de Elipse Preenchida

O seguinte trecho de código mostra como adicionar um objeto [Elipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) que está preenchido com cor.

```csharp
     public static void EllipseFilled()
        {
            // Criar instância do Documento
            var document = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Criar objeto de Desenho com dimensões específicas
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // Definir borda para o objeto de Desenho
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Elipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            graph.Shapes.Add(ellipse2);

            // Adicionar objeto Gráfico à coleção de parágrafos da página
            page.Paragraphs.Add(graph);

            // Salvar arquivo PDF
            document.Save(_dataDir + "DrawingEllipse_out.pdf");
        }
```
![Elipse Preenchida](fill_ellipse.png)

## Adicionar Texto Dentro da Elipse

Aspose.PDF para .NET suporta a adição de texto dentro do Objeto Gráfico. A propriedade Texto do Objeto Gráfico oferece a opção de definir o texto do Objeto Gráfico. O seguinte trecho de código mostra como adicionar texto dentro de um objeto Retângulo.

```csharp
        public static void EllipseWithText()
        {
            // Criar instância do Documento
            var document = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Criar objeto de Desenho com dimensões específicas
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Definir borda para o objeto de Desenho
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var textFragment = new TextFragment("Elipse");
            textFragment.TextState.Font = FontRepository.FindFont("Helvetica");
            textFragment.TextState.FontSize = 24;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            ellipse1.Text = textFragment;
            graph.Shapes.Add(ellipse1);


            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            ellipse2.Text = textFragment;
            graph.Shapes.Add(ellipse2);

            // Adicionar objeto Gráfico à coleção de parágrafos da página
            page.Paragraphs.Add(graph);

            // Salvar o arquivo PDF
            document.Save(_dataDir + "DrawingEllipseText_out.pdf");

        }
 ```
![Texto dentro da Elipse](text_ellipse.png)

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



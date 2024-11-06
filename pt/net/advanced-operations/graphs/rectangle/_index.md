---
title: Adicionar Objeto Retângulo ao arquivo PDF
linktitle: Adicionar Retângulo
type: docs
weight: 50
url: pt/net/add-rectangle/
description: Este artigo explica como criar um objeto Retângulo em seu PDF usando o Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Objeto Retângulo ao arquivo PDF",
    "alternativeHeadline": "Como criar Objeto Retângulo em arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, retângulo em pdf",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo explica como criar um objeto Retângulo em seu PDF usando o Aspose.PDF para .NET."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Adicionar objeto Retângulo

Aspose.PDF para .NET suporta a funcionalidade de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) aos documentos PDF. Você também tem a vantagem de adicionar um objeto [Retângulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) onde também oferece a funcionalidade de preencher o objeto retângulo com uma determinada cor, controlar a ordem Z, adicionar preenchimento de cor gradiente e etc.

Primeiro, vamos olhar para a possibilidade de criar um objeto Retângulo.

Siga os passos abaixo:

1. Crie um novo [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document) PDF

1. Adicione [Página](https://reference.aspose.com/pdf/net/aspose.pdf/page) à coleção de páginas do arquivo PDF

1. Adicione [Fragmento de texto](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) à coleção de parágrafos da instância da página

1. Crie uma instância [Gráfico](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)
1. Criar instância de Retângulo

1. Adicionar objeto [Retângulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) à coleção de formas do objeto Gráfico

1. Adicionar objeto gráfico à coleção de parágrafos da instância de página

1. Adicionar [Fragmento de texto](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) à coleção de parágrafos da instância de página

1. E salve seu arquivo PDF

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Criar objeto gráfico com dimensões especificadas para o objeto Retângulo
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // Podemos alterar a posição da instância do gráfico
                IsChangePosition = false,
                // Definir posição da coordenada Esquerda para a instância do Gráfico
                Left = x,
                // Definir posição da coordenada Superior para o objeto Gráfico
                Top = y
            };
            // Adicionar um retângulo dentro do "gráfico"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Definir a cor de preenchimento do retângulo
            rect.GraphInfo.FillColor = color;
            // Cor do objeto gráfico
            rect.GraphInfo.Color = color;
            // Adicionar retângulo à coleção de formas da instância do gráfico
            graph.Shapes.Add(rect);
            // Definir Z-Index para o objeto retângulo
            graph.ZIndex = zindex;
            // Adicionar gráfico à coleção de parágrafos do objeto de página
            page.Paragraphs.Add(graph);
        }
```
![Criar Retângulo](create_rectangle.png)

## Criar Objeto Retângulo Preenchido

Aspose.PDF para .NET também oferece a funcionalidade de preencher um objeto retângulo com uma determinada cor.

O seguinte trecho de código mostra como adicionar um objeto [Retângulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) que é preenchido com cor.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Criar instância de Document
            var doc = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = doc.Pages.Add();
            // Criar instância de Graph
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Adicionar objeto gráfico à coleção de parágrafos da instância de página
            page.Paragraphs.Add(graph);

            // Criar instância de Rectangle
            var rect = new Rectangle(100, 100, 200, 120);

            // Especificar cor de preenchimento para o objeto Graph
            rect.GraphInfo.FillColor = Color.Red;

            // Adicionar objeto retângulo à coleção de formas do objeto Graph
            graph.Shapes.Add(rect);

            // Salvar arquivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
Veja o resultado de um retângulo preenchido com cor sólida:

![Retângulo Preenchido](fill_rectangle.png)

## Adicionar Desenho com Preenchimento Gradiente

Aspose.PDF para .NET suporta a funcionalidade de adicionar objetos gráficos a documentos PDF e, às vezes, é necessário preencher objetos gráficos com Cor Gradiente. Para preencher objetos gráficos com Cor Gradiente, precisamos configurar setPatterColorSpace com o objeto gradientAxialShading conforme a seguir.

O seguinte trecho de código mostra como adicionar um objeto [Retângulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) que é preenchido com Cor Gradiente.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Criar instância de Documento
            var doc = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = doc.Pages.Add();
            // Criar instância de Gráfico
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Adicionar objeto gráfico à coleção de parágrafos da instância de página
            page.Paragraphs.Add(graph);
            // Criar instância de Retângulo
            var rect = new Rectangle(0, 0, 300, 300);
            // Especificar cor de preenchimento para o objeto Gráfico
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Adicionar objeto retângulo à coleção de formas do objeto Gráfico
            graph.Shapes.Add(rect);

            // Salvar arquivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Retângulo Gradiente](gradient.png)

## Criar Retângulo com Canal Alfa de Cor

O Aspose.PDF para .NET suporta o preenchimento de objetos retângulos com uma cor específica. Um objeto retângulo também pode ter um canal de cor Alfa para dar uma aparência transparente. O trecho de código a seguir mostra como adicionar um objeto [Retângulo](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) com canal de cor Alfa.

Os pixels da imagem podem armazenar informações sobre sua opacidade, juntamente com o valor da cor. Isso permite criar imagens com áreas transparentes ou semi-transparentes.

Em vez de tornar uma cor transparente, cada pixel armazena informações sobre o quão opaco ele é. Esses dados de opacidade são chamados de canal alfa e geralmente são armazenados após os canais de cor do pixel.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Criar instância do Documento
            var doc = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = doc.Pages.Add();
            // Criar instância de Gráfico
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Adicionar objeto gráfico à coleção de parágrafos da instância de página
            page.Paragraphs.Add(graph);
            // Criar instância de Retângulo
            var rect = new Rectangle(100, 100, 200, 120);
            // Especificar cor de preenchimento para o objeto Gráfico
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Adicionar objeto retângulo à coleção de formas do objeto Gráfico
            graph.Shapes.Add(rect);

            // Criar segundo objeto retângulo
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Adicionar instância de gráfico à coleção de parágrafos do objeto de página
            page.Paragraphs.Add(graph);

            // Salvar arquivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Rectangle Alpha Channel Color](rectangle_color.png)

## Controle a Ordem Z do Retângulo

Aspose.PDF para .NET suporta a funcionalidade de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Ao adicionar mais de uma instância do mesmo objeto dentro do arquivo PDF, podemos controlar sua renderização especificando a Ordem Z. A Ordem Z também é usada quando precisamos renderizar objetos sobrepostos uns aos outros.

O seguinte trecho de código mostra os passos para renderizar objetos [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) uns sobre os outros.

```csharp
 public static void AddRectangleZOrder()
        {
            // Instancie o objeto da classe Document
            Document doc1 = new Document();
            /// Adicione página à coleção de páginas do arquivo PDF
            Page page1 = doc1.Pages.Add();
            // Defina o tamanho da página PDF
            page1.SetPageSize(375, 300);
            // Defina a margem esquerda do objeto página como 0
            page1.PageInfo.Margin.Left = 0;
            // Defina a margem superior do objeto página como 0
            page1.PageInfo.Margin.Top = 0;
            // Crie um novo retângulo com Cor como Vermelho, Ordem Z como 0 e certas dimensões
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Crie um novo retângulo com Cor como Azul, Ordem Z como 0 e certas dimensões
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Crie um novo retângulo com Cor como Verde, Ordem Z como 0 e certas dimensões
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Salve o arquivo PDF resultante
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```
![Controlando a Ordem Z](control.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
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



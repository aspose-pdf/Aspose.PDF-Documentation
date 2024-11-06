---
title: Anotações adesivas em PDF usando C#
linktitle: Anotação Adesiva
type: docs
weight: 50
url: pt/net/sticky-annotations/
description: Este tópico sobre anotações adesivas, como exemplo mostramos a Anotação de Marca D'água no texto.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotações adesivas em PDF usando C#",
    "alternativeHeadline": "Como adicionar Anotações Adesivas em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, anotações adesivas, anotação de marca d'água",
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
    "url": "/net/sticky-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sticky-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "Este tópico sobre anotações adesivas, como exemplo mostramos a Anotação de Marca D'água no texto."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Adicionar Anotação de Marca D'água

Uma anotação de marca d'água deve ser usada para representar gráficos que devem ser impressos em um tamanho e posição fixos em uma página, independentemente das dimensões da página impressa.

Você pode adicionar Texto de Marca D'água usando [WatermarkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/watermarkannotation) em uma posição específica da página PDF. A opacidade da Marca D'água também pode ser controlada usando a propriedade de opacidade.

Por favor, verifique o seguinte trecho de código para adicionar WatermarkAnnotation.

```csharp
 //Carregar um Documento
Aspose.PDF.Document doc = new Aspose.PDF.Document("source.pdf");

//Carregar objeto Page para adicionar Anotação
Page page = doc.Pages[1];

//Criar Anotação
WatermarkAnnotation wa = new WatermarkAnnotation(page, new Aspose.PDF.Rectangle(100, 500, 400, 600));

//Adicionar anotação à coleção de Anotações da Página
page.Annotations.Add(wa);

//Criar TextState para configurações de Fonte
Aspose.PDF.Text.TextState ts = new Aspose.PDF.Text.TextState();

ts.ForegroundColor = Aspose.PDF.Color.Blue;
ts.Font = FontRepository.FindFont("Times New Roman");

ts.FontSize = 32;

//Definir nível de opacidade do Texto da Anotação

wa.Opacity = 0.5;
//Adicionar Texto na Anotação

wa.SetTextAndState(new string[] { "HELLO", "Linha 1", "Linha 2" }, ts);

//Salvar o Documento
doc.Save("Output.pdf");
```
## Adicionar Referência de uma Única Imagem Múltiplas Vezes em um Documento PDF

Às vezes temos a necessidade de usar a mesma imagem várias vezes em um documento PDF. Adicionar uma nova instância aumenta o tamanho do documento PDF resultante. Adicionamos um novo método XImageCollection.Add(XImage) no Aspose.PDF para .NET 17.1.0. Este método permite adicionar referência ao mesmo objeto PDF que a imagem original que otimiza o tamanho do Documento PDF.

```csharp
Aspose.PDF.Rectangle imageRectangle = new Aspose.PDF.Rectangle(0, 0, 30, 15);

using (Aspose.PDF.Document document = new Aspose.PDF.Document("input.pdf"))
{
    using (var imageStream = File.Open("icon.png", FileMode.Open))
    {
        XImage image = null;
        foreach (Page page in document.Pages)
        {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.Rect);
            XForm form = annotation.Appearance["N"];
            form.BBox = page.Rect;
            string name;
            if (image == null)
            {
                name = form.Resources.Images.Add(imageStream);
                image = form.Resources.Images[name];
            }
            else
            {
                name = form.Resources.Images.Add(image);
            }
            form.Contents.Add(new Operator.GSave());
            form.Contents.Add(new Operator.ConcatenateMatrix(new Aspose.PDF.Matrix(imageRectangle.Width, 0, 0, imageRectangle.Height, 0, 0)));
            form.Contents.Add(new Operator.Do(name));
            form.Contents.Add(new Operator.GRestore());
            page.Annotations.Add(annotation, false);
            imageRectangle = new Aspose.PDF.Rectangle(0, 0, imageRectangle.Width * 1.01, imageRectangle.Height * 1.01);
        }
    }
    document.Save("output.pdf");
}
```

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
```


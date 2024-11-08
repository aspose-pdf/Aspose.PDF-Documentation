---
title: Usando Anotações de Link em PDF
linktitle: Anotações de Link
type: docs
weight: 70
url: /pt/net/link-annotations/
description: Aspose.PDF para .NET permite que você Adicione, Obtenha e Exclua Anotação de Link do seu documento PDF.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Usando Anotação de Link para PDF",
    "alternativeHeadline": "Como adicionar Anotação de Link em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, anotação de texto",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET permite que você Adicione, Obtenha e Exclua Anotação de Texto do seu documento PDF."
}
</script>
## Adicionando Anotação de Link em um arquivo PDF existente

> O trecho de código a seguir também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Uma [Anotação de Link](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) representa um hiperlink, um destino em outro lugar e um documento. De acordo com o Padrão PDF, a anotação de link pode ser usada em três casos: abrir visualização de página, abrir arquivo e abrir página web.

### Usando Anotação de Link para abrir visualização de página

Vários passos adicionais foram realizados para criar a anotação. Usamos 2 TextFragmentAbsorbers para encontrar fragmentos para demonstração. O primeiro é para o texto da anotação de link, e o segundo indica alguns lugares no documento.

```cs
Document document = new Document(System.IO.Path.Combine(_dataDir, "Link Annotation Demo.pdf"));

var page = document.Pages[1];

var regEx = new Regex(@"Link Annotation Demo \d");
TextFragmentAbsorber textFragmentAbsorber1 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber1.Visit(document);

regEx = new Regex(@"Sample text \d");
TextFragmentAbsorber textFragmentAbsorber2 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber2.Visit(document);

var linkFragments = textFragmentAbsorber1.TextFragments;
var sampleTextFragments = textFragmentAbsorber2.TextFragments;

var linkAnnotation1 = new LinkAnnotation(page, linkFragments[1].Rectangle)
{
    Action = new GoToAction(
        new XYZExplicitDestination(
            sampleTextFragments[1].Page,
            sampleTextFragments[1].Rectangle.LLX,
            sampleTextFragments[1].Rectangle.URX, 1.5))
};

page.Annotations.Add(linkAnnotation1);

document.Save("test.pdf");
```
Para criar a anotação, seguimos certos passos:

1. Crie `LinkAnnotation` e passe o objeto da página e o retângulo do fragmento de texto que corresponde à anotação.
1. Defina `Action` como `GoToAction` e passe `XYZExplicitDestination` como destino desejado. Criamos `XYZExplicitDestination` baseado na página, coordenadas esquerda e superior e zoom.
1. Adicione a anotação à coleção de anotações da página.
1. Salve o documento

### Usando Link Annotation com destino nomeado

Ao processar vários documentos, surge uma situação em que você está digitando e não sabe para onde a anotação apontará.
Neste caso, você pode usar um destino especial (nomeado) e o código será assim:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

Em outro lugar, você pode criar um Destino Nomeado.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```
### Usando Anotação de Link para abrir arquivo

O mesmo método é utilizado ao criar uma anotação para abrir um arquivo, como nos exemplos acima.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

A diferença é que usaremos `GoToRemoteAction` em vez de `GoToAction`. O construtor do GoToRemoteAction recebe dois parâmetros: nome do arquivo e número da página.
Você também pode usar outra forma e passar o nome do arquivo e algum destino. Obviamente, você precisa criar tal destino antes de usá-lo.

### Usando Anotação de Link para abrir página web

Para abrir uma página web basta definir `Action` com o objeto `GoToURIAction`.
Você pode passar um hiperlink como parâmetro do construtor ou qualquer outro tipo de URI. Por exemplo, você pode usar `callto` para implementar ação com chamada de número de telefone.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Criar Anotação de Link e definir a ação para chamar um número de telefone
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```
## Adicionando Anotação de Link Decorada

Você pode personalizar a Anotação de Link usando bordas. No exemplo abaixo, criaremos uma borda tracejada azul com 3pt de largura.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

Outro exemplo mostra como simular o estilo de navegador e usar Sublinhado para links.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### Obter Anotações de Link

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Link de um documento PDF.

```csharp
class ExampleLinkAnnotations
{
    // O caminho para o diretório de documentos.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void GetLinkAnnotations()
    {
        // Carrega o arquivo PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Imprime a URL de cada Anotação de Link
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            document.Pages[1].Accept(absorber);
            string extractedText = absorber.Text;
            // Imprime o texto associado ao hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
### Excluir Anotações de Link

O seguinte trecho de código mostra como excluir Anotação de Link de um arquivo PDF. Para isso, precisamos encontrar e remover todas as anotações de link na 1ª página. Após isso, salvaremos o documento com a anotação removida.

```csharp
class ExampleLinkAnnotations
{
    // O caminho para o diretório de documentos.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void DeleteLinkAnnotations()
    {
        // Carregar o arquivo PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        // Encontrar e excluir todas as anotações de link na 1ª página
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);

        foreach (var la in linkAnnotations)
            document.Pages[1].Annotations.Delete(la);
        // Salvar o documento com a anotação removida
        document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_del.pdf"));
    }
}
```

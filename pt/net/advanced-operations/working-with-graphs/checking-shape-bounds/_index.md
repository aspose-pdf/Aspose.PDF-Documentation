---
title: Verificar limites de forma na coleção de Formas
type: docs
weight: 70
url: /pt/net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Aprenda como verificar os limites de uma forma quando inserida na coleção de Formas para garantir que ela se encaixe dentro de seu contêiner pai.
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "O novo recurso de verificação de limites de Aspose.PDF for .NET na coleção `Drawing.Graph.Shapes` valida automaticamente as dimensões dos elementos em relação aos contêineres pai, prevenindo transbordamento de layout. Ele aciona exceções quando os elementos excedem os limites do contêiner, impondo restrições de tamanho rigorosas durante a inserção para garantir formatação precisa de PDF e agilizar a precisão do design.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "818",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/"
    },
    "dateModified": "2025-03-17",
    "description": ""
}
</script>

## Introdução
Este documento fornece um guia detalhado sobre como usar o recurso de verificação de limites na coleção de Formas. Este recurso garante que os elementos se encaixem dentro de seu contêiner pai e pode ser configurado para lançar uma exceção se o componente não se encaixar. Vamos percorrer os passos para implementar essa funcionalidade e fornecer um exemplo completo.

## Pré-requisitos
Você precisará do seguinte:
* Visual Studio 2019 ou posterior
* Aspose.PDF for .NET 25.3 ou posterior
* Um arquivo PDF de exemplo que contenha algumas páginas

Você pode baixar a biblioteca Aspose.PDF for .NET do site oficial ou instalá-la usando o Gerenciador de Pacotes NuGet no Visual Studio.

## Passos
Aqui estão os passos para completar a tarefa:
1. Criar documento PDF.
2. Criar um objeto `Graph` com dimensões especificadas.
3. Criar um objeto `Shape` com dimensões especificadas.
4. Definir o `BoundsCheckMode` como `ThrowExceptionIfDoesNotFit`.
5. Tentar adicionar a forma ao gráfico.

Vamos ver como implementar esses passos em código C#.

### Passo 1: Criar documento PDF
Primeiro, crie um novo documento PDF e adicione uma página a ele.

```csharp
using (var doc = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### Passo 2: Criar um objeto Graph com dimensões especificadas
Em seguida, crie um objeto `Graph` com uma largura e altura de 100 unidades. Posicione o gráfico a 10 unidades do topo e 15 unidades da esquerda da página. Adicione uma borda preta ao gráfico.

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### Passo 3: Criar um objeto Shape (por exemplo, Retângulo) com dimensões especificadas
Crie um objeto Retângulo com uma largura e altura de 50 unidades. Posicione o retângulo em (-1, 0), que está fora dos limites do gráfico.

```csharp
var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### Passo 4: Definir o BoundsCheckMode como ThrowExceptionIfDoesNotFit
Defina o `BoundsCheckMode` como `ThrowExceptionIfDoesNotFit` para garantir que uma exceção seja lançada se o retângulo não se encaixar dentro do gráfico.

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### Passo 5: Adicionar o retângulo ao gráfico
Adicione o retângulo ao gráfico. Isso lançará uma `Aspose.Pdf.BoundsOutOfRangeException` porque o retângulo não se encaixa nas dimensões do gráfico.

```csharp
graph.Shapes.Add(rect);
```

## Saída
Após executar o código, a saída esperada será uma `Aspose.Pdf.BoundsOutOfRangeException` com a mensagem:

```
Bounds not fit. Container dimensions: 100x100
```

## Solução de Problemas
Em caso de problemas, aqui estão algumas dicas:
* Certifique-se de que o `BoundsCheckMode` esteja configurado corretamente.
* Verifique se as dimensões do elemento e do contêiner estão precisas.
* Verifique o posicionamento do elemento dentro do contêiner.

## Exemplo Completo
Abaixo está um exemplo completo demonstrando todos os passos combinados:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create PDF document
    using (var doc = new Aspose.Pdf.Document())
    {
        // Add page
        var page = doc.Pages.Add();
        
        // Create a Graph object with specified dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Shape object (for example, Rectangle) with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create PDF document
    using var doc = new Aspose.Pdf.Document();
    
    // Add page
    var page = doc.Pages.Add();

    // Create a Graph object with specified dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    var rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## Conclusão
O recurso de verificação de limites na coleção de Formas é uma ferramenta poderosa para garantir que os elementos se encaixem dentro dos contêineres pai. Você pode prevenir problemas de layout em seus documentos PDF definindo o BoundsCheckMode como ThrowExceptionIfDoesNotFit. Este recurso é particularmente útil em cenários onde o posicionamento e o dimensionamento precisos dos elementos são críticos. Para mais detalhes, visite a [documentação oficial](https://docs.aspose.com/pdf/net/).
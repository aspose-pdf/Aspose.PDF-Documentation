---
title: Trabalhando com Gráficos Vetoriais
linktitle: Trabalhando com Gráficos Vetoriais
type: docs
weight: 120
url: pt/net/working-with-vector-graphics/
description: Este artigo descreve as funcionalidades do uso da ferramenta GraphicsAbsorber com C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com GraphicsAbsorber",
    "alternativeHeadline": "Como obter a posição de uma imagem em um arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, c#, GraphicsAbsorber em pdf",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção descreve as funcionalidades do uso do arquivo PDF GraphicsAbsorber usando a biblioteca C#."
}
</script>

Neste capítulo, exploraremos como usar a poderosa classe `GraphicsAbsorber` para interagir com gráficos vetoriais dentro de documentos PDF. Se você precisa mover, remover ou adicionar gráficos, este guia mostrará como realizar essas tarefas de forma eficaz. Vamos começar!

## Introdução<a name="introduction"></a>

Gráficos vetoriais são um componente crucial de muitos documentos PDF, usados para representar imagens, formas e outros elementos gráficos. Aspose.PDF oferece a classe `GraphicsAbsorber`, que permite aos desenvolvedores acessar e manipular programaticamente esses gráficos. Ao usar o método `Visit` de `GraphicsAbsorber`, você pode extrair gráficos vetoriais de uma página especificada e realizar várias operações, como mover, remover ou copiá-los para outras páginas.

## 1. Extraindo Gráficos com `GraphicsAbsorber`<a name="extracting-graphics"></a>

O primeiro passo ao trabalhar com gráficos vetoriais é extraí-los de um documento PDF. Veja como você pode fazer isso usando a classe `GraphicsAbsorber`:

```csharp
public static void UsingGraphicsAbsorber()
{
    // Passo 1: Criar um objeto Document.
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");

    // Passo 2: Criar uma instância de GraphicsAbsorber.
    var graphicsAbsorber = new GraphicsAbsorber();

    // Selecionar a primeira página do documento.
    var page = document.Pages[1];

    // Passo 3: Usar o método `Visit` para extrair gráficos da página.
    graphicsAbsorber.Visit(page);

    // Exibir informações sobre os elementos extraídos.
    foreach (var element in graphicsAbsorber.Elements)
    {
        Console.WriteLine($"Número da Página: {element.SourcePage.Number}");
        Console.WriteLine($"Posição: ({element.Position.X}, {element.Position.Y})");
        Console.WriteLine($"Número de Operadores: {element.Operators.Count}");
    }
}
```
### Explicação:

1. **Criar um Objeto Documento**: Um novo objeto `Document` é instanciado com o caminho para o arquivo PDF alvo.
2. **Criar uma Instância de `GraphicsAbsorber`**: Esta classe captura todos os elementos gráficos de uma página especificada.
3. **Método Visit**: O método `Visit` é chamado na primeira página, permitindo que o `GraphicsAbsorber` absorva os gráficos vetoriais.
4. **Iterar pelos Elementos Extraídos**: O código percorre cada elemento extraído, imprimindo informações como número da página, posição e o número de operadores de desenho envolvidos.

## 2. Movendo Gráficos<a name="moving-graphics"></a>

Uma vez que você tenha extraído os gráficos, você pode movê-los para uma posição diferente na mesma página. Veja como você pode fazer isso:

```csharp
public static void MoveGraphics()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);

    // Temporariamente suspende atualizações para melhorar o desempenho.
    graphicsAbsorber.SuppressUpdate();

    foreach (var element in graphicsAbsorber.Elements)
    {
        var position = element.Position;
        // Move gráficos deslocando suas coordenadas X e Y.
        element.Position = new Point(position.X + 150, position.Y - 10);
    }

    // Retoma as atualizações e aplica as mudanças.
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Pontos-chave:

- **SuppressUpdate**: Este método suspende temporariamente as atualizações para melhorar o desempenho ao fazer várias alterações.
- **ResumeUpdate**: Este método retoma as atualizações e aplica as alterações feitas nas posições dos gráficos.
- **Posicionamento de Elementos**: A posição de cada gráfico é ajustada alterando suas coordenadas `X` e `Y`.

## 3. Removendo Gráficos<a name="removing-graphics"></a>

Existem cenários em que você pode querer remover gráficos específicos de uma página. Aspose.PDF oferece dois métodos para realizar isso:

### Método 1: Usando Limite Retangular

```csharp
public static void RemoveGraphicsMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        // Verifique se a posição do gráfico está dentro do retângulo.
        if (rectangle.Contains(element.Position))
        {
            element.Remove(); // Remova o elemento gráfico.
        }
    }
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Método 2: Usando uma Coleção de Elementos Removidos

```csharp
public static void RemoveGraphicsMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.Visit(page);
    var removedElementsCollection = new GraphicElementCollection();
    foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
    {
        removedElementsCollection.Add(item);
    }

    page.Contents.SuppressUpdate();
    page.DeleteGraphics(removedElementsCollection);
    page.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### Explicação:

- **Limite do Retângulo**: Define uma área retangular para especificar quais gráficos remover.
- **Suprimir e Retomar Atualizações**: Garante a remoção eficiente sem renderização intermediária.

## 4. Adicionando Gráficos a Outra Página<a name="adding-graphics"></a>

Gráficos absorvidos de uma página podem ser adicionados a outra página dentro do mesmo documento.
Gráficos absorvidos de uma página podem ser adicionados a outra página dentro do mesmo documento.

### Método 1: Adicionando Gráficos Individualmente

```csharp
public static void AddToAnotherPageMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        element.AddOnPage(page2); // Adiciona cada elemento gráfico à segunda página.
    }
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### Método 2: Adicionando Gráficos como uma Coleção

```csharp
public static void AddToAnotherPageMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    page2.AddGraphics(graphicsAbsorber.Elements); // Adiciona todos os gráficos de uma vez.
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```
### Pontos Principais:

- **SuppressUpdate e ResumeUpdate**: Estes métodos ajudam a manter o desempenho ao fazer alterações em massa.
- **AddOnPage vs. AddGraphics**: Use `AddOnPage` para adições individuais e `AddGraphics` para adições em massa.

## Conclusão

Neste capítulo, exploramos como usar a classe `GraphicsAbsorber` para extrair, mover, remover e adicionar gráficos vetoriais em documentos PDF usando Aspose.PDF. Ao dominar essas técnicas, você pode melhorar significativamente a apresentação visual de seus PDFs e criar documentos dinâmicos e visualmente atraentes.

Sinta-se à vontade para experimentar os exemplos de código e adaptá-los aos seus casos de uso específicos. Boa programação!

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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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



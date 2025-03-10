---
title: Adicionar Anotações de Figuras usando C#
linktitle: Anotações de Figuras
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/figures-annotation/
description: Este artigo descreve como adicionar, obter e excluir anotações de figuras do seu documento PDF com Aspose.PDF for .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Figures Annotations using C#",
    "alternativeHeadline": "Enhance PDF Documents with Comprehensive Figure Annotations",
    "abstract": "Apresentando o novo recurso de Anotações de Figuras em Aspose.PDF for .NET, que capacita os usuários a adicionar, recuperar e excluir vários tipos de anotações, incluindo linhas, quadrados, círculos, polígonos e polilinhas em documentos PDF. Essa funcionalidade melhora a interatividade do documento, permitindo uma comunicação mais clara e marcação visual diretamente dentro dos arquivos PDF. Otimize suas tarefas de edição de PDF com este robusto conjunto de ferramentas de anotação projetado para desenvolvedores usando C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, figures annotations, line annotation, square annotation, circle annotation, polygon annotation, polyline annotation, free text annotation, ink annotation, Aspose.PDF for .NET",
    "wordcount": "2125",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Este artigo descreve como adicionar, obter e excluir anotações de figuras do seu documento PDF com Aspose.PDF for .NET"
}
</script>

O aplicativo de gerenciamento de documentos PDF fornece várias ferramentas para anotar documentos. Do ponto de vista da estrutura interna do PDF, essas ferramentas são anotações. Suportamos os seguintes tipos de ferramentas de desenho.

* Anotação de Linha - ferramenta para desenhar linhas e setas.
* Anotação de Quadrado - para desenhar quadrados e retângulos.
* Anotação de Círculo - para ovais e círculos.
* Anotação de Texto Livre - para comentários de chamada.
* Anotação de Polígono - para polígonos e nuvens.
* Anotação de Polilinha - para Linhas Conectadas.

## Adicionando Formas e Figuras na Página

A abordagem para adicionar a anotação é típica para qualquer uma delas.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

1. Carregue o arquivo PDF ou crie um novo por [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crie a nova anotação e defina os parâmetros (novo Retângulo, novo Ponto, título, cor, largura etc).
1. Crie a nova [PopupAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation/methods/index).
1. Vincule a anotação Popup com a original.
1. Adicione a anotação à página.

## Adicionando Linhas ou Setas

O propósito da anotação de linha é exibir uma linha ou seta direta na página. Para criar uma Linha, precisamos de um novo objeto LineAnnotation.  
O construtor da classe LineAnnotation aceita quatro parâmetros:

* A página onde a anotação será adicionada.
* O retângulo que define o limite da anotação.
* Os dois pontos que definem o início e o fim da linha.

Além disso, precisamos inicializar algumas propriedades:

* `Title` - geralmente, é o nome do usuário que fez este comentário.
* `Subject` - pode ser qualquer string, mas em casos comuns é o nome da anotação.

Para estilizar nossa linha, precisamos definir a cor, largura, estilo inicial e estilo final. Essas propriedades controlam como a anotação aparecerá e se comportará no visualizador de PDF. Por exemplo, as propriedades `StartingStyle` e `EndingStyle` determinam que tipo de forma será desenhada nas extremidades da linha, como uma seta aberta, uma seta fechada, um círculo, etc.

O seguinte trecho de código mostra como adicionar Anotação de Linha a um arquivo PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
    {
        // Create Line Annotation
        var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(550, 93, 562, 439),
            new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Width = 3,
            StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
        };

        // Add annotation to the page
        document.Pages[1].Annotations.Add(lineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```

## Adicionando Quadrado ou Círculo

As anotações [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) e [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) exibirão um retângulo ou uma elipse na página. Quando abertas, elas exibirão uma janela pop-up contendo o texto da nota associada. Anotações quadradas são como anotações de círculo (instâncias da classe Aspose. Pdf. Annotations. CircleAnnotation) além da forma.

### Adicionando anotação de Círculo

Para desenhar uma nova anotação de círculo ou elipse, precisamos criar um novo objeto CircleAnnotation. O construtor da classe `CircleAnnotation` aceita dois parâmetros:

* A página onde a anotação será adicionada.
* O retângulo que define o limite da anotação.

Além disso, podemos definir algumas propriedades do objeto `CircleAnnotation`, como o título, cor, cor interior, opacidade. Essas propriedades controlam como a anotação aparecerá e se comportará no visualizador de PDF. Aqui e adiante, no Quadrado, a cor `InteriorColor` é a cor de preenchimento e `Color` é a cor da borda.

### Adicionando anotação de Quadrado

Desenhar um retângulo é o mesmo que desenhar um círculo. O seguinte trecho de código mostra como adicionar anotações de círculo e quadrado a uma página PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCircleAndSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Create Circle Annotation
        var circleAnnotation = new Aspose.Pdf.Annotations.CircleAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(270, 160, 483, 383))
        {
            Title = "John Smith",
            Subject = "Circle",
            Color = Aspose.Pdf.Color.Red,
            InteriorColor = Aspose.Pdf.Color.MistyRose,
            Opacity = 0.5,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 316, 1021, 459))
        };

        // Create Square Annotation
        var squareAnnotation = new Aspose.Pdf.Annotations.SquareAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(67, 317, 261, 459))
        {
            Title = "John Smith",
            Subject = "Rectangle",
            Color = Aspose.Pdf.Color.Blue,
            InteriorColor = Aspose.Pdf.Color.BlueViolet,
            Opacity = 0.25,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(circleAnnotation);
        document.Pages[1].Annotations.Add(squareAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddCircleAndSquareAnnotations_out.pdf");
    }
}
```

Como exemplo, veremos o seguinte resultado da adição de anotações de Quadrado e Círculo a um documento PDF:

## Adicionando Anotações de Polígono e Polilinha

A ferramenta Poly permite criar formas e contornos com um número arbitrário de lados no documento.

**Anotações de Polígono** representam polígonos em uma página. Eles podem ter qualquer número de vértices conectados por linhas retas.  
**Anotações de Polilinha** também são semelhantes a polígonos, a única diferença é que os primeiros e últimos vértices não estão implicitamente conectados.

### Adicionando Anotação de Polígono

PolygonAnnotation é responsável por anotações de polígono. O construtor da classe PolygonAnnotation aceita três parâmetros:

* A página onde a anotação será adicionada.
* O retângulo que define o limite da anotação.
* O array de pontos que definem os vértices do polígono.

`Color` e `InteriorColor` são usados para as cores da borda e preenchimento, respectivamente.

### Adicionando Anotação de Polilinha

PolygonAnnotation é responsável por anotações de polígono. O construtor da classe PolygonAnnotation aceita três parâmetros:

* A página onde a anotação será adicionada.
* O retângulo que define o limite da anotação.
* O array de pontos que definem os vértices do polígono.

Em vez de `PolygonAnnotation`, não podemos preencher essa forma, então não precisamos usar `InteriorColor`.

O seguinte trecho de código mostra como adicionar Anotações de Polígono e Polilinha a um arquivo PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPolygonAndPolylineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Create Polygon Annotation
        var polygonAnnotation = new Aspose.Pdf.Annotations.PolygonAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(270, 193, 571, 383),
            new Aspose.Pdf.Point[] {
                new Aspose.Pdf.Point(274, 381),
                new Aspose.Pdf.Point(555, 381),
                new Aspose.Pdf.Point(555, 304),
                new Aspose.Pdf.Point(570, 304),
                new Aspose.Pdf.Point(570, 195),
                new Aspose.Pdf.Point(274, 195)
            })
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Blue,
            InteriorColor = Aspose.Pdf.Color.BlueViolet,
            Opacity = 0.25,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Create Polyline Annotation
        var polylineAnnotation = new Aspose.Pdf.Annotations.PolylineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(270, 193, 571, 383),
            new Aspose.Pdf.Point[] {
                new Aspose.Pdf.Point(545, 150),
                new Aspose.Pdf.Point(545, 190),
                new Aspose.Pdf.Point(667, 190),
                new Aspose.Pdf.Point(667, 110),
                new Aspose.Pdf.Point(626, 111)
            })
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(polygonAnnotation);
        document.Pages[1].Annotations.Add(polylineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddPolygonAndPolylineAnnotations_out.pdf");
    }
}
```

## Obtendo Figuras

Todas as anotações são armazenadas na coleção `Annotations`. Qualquer anotação pode introduzir seu tipo através da propriedade `AnnotationType`. Portanto, podemos fazer uma consulta LINQ para filtrar as anotações desejadas.

### Obtendo Anotações de Linha

O exemplo abaixo explica como obter todas as Anotações de Linha da primeira página do documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadLineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all line annotations from the first page
        var lineAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
            .Cast<Aspose.Pdf.Annotations.LineAnnotation>();

        // Iterate through each line annotation and print its coordinates
        foreach (var la in lineAnnotations)
        {
            Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
        }
    }
}
```

### Obtendo Anotações de Círculo

O exemplo abaixo explica como obter todas as Anotações de Polilinha da primeira página do documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadCircleAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all circle annotations from the first page
        var circleAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle)
            .Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

        // Iterate through each circle annotation and print its rectangle
        foreach (var ca in circleAnnotations)
        {
            Console.WriteLine($"[{ca.Rect}]");
        }
    }
}
```

### Obtendo Anotações de Quadrado

O exemplo abaixo explica como obter todas as Anotações de Polilinha da primeira página do documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all square annotations from the first page
        var squareAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square)
            .Cast<Aspose.Pdf.Annotations.SquareAnnotation>();

        // Iterate through each square annotation and print its rectangle
        foreach (var sq in squareAnnotations)
        {
            Console.WriteLine($"[{sq.Rect}]");
        }
    }
}
```

### Obtendo Anotações de Polilinha

O exemplo abaixo explica como obter todas as Anotações de Polilinha da primeira página do documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadPolylineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polyline annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine)
            .Cast<Aspose.Pdf.Annotations.PolylineAnnotation>();

        // Iterate through each polyline annotation and print its rectangle
        foreach (var pa in polyAnnotations)
        {
            Console.WriteLine($"[{pa.Rect}]");
        }
    }
}
```

### Obtendo Anotações de Polígono

O exemplo abaixo explica como obter todas as Anotações de Polígono da primeira página do documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadPolygonAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polygon annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon)
            .Cast<Aspose.Pdf.Annotations.PolygonAnnotation>();

        // Iterate through each polygon annotation and print its rectangle
        foreach (var pa in polyAnnotations)
        {
            Console.WriteLine($"[{pa.Rect}]");
        }
    }
}
```

## Excluindo Figuras

A abordagem para remover anotações de PDF é bastante simples:

* Selecione as anotações a serem excluídas (faça alguma coleção).
* Itere sobre a coleção usando um loop foreach e exclua cada anotação da coleção de anotações usando o método Delete.

### Excluindo Anotação de Linha

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all line annotations from the first page
        var lineAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
            .Cast<Aspose.Pdf.Annotations.LineAnnotation>();

        // Iterate through each line annotation and delete it
        foreach (var la in lineAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLineAnnotations_out.pdf");
    }
}
```

### Excluir Anotações de Círculo e Quadrado

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCircleAndSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all circle and square annotations from the first page
        var figures = document.Pages[1].Annotations
            .Where(a =>
                a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle
                || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square);

        // Iterate through each figure annotation and delete it
        foreach (var fig in figures)
        {
            document.Pages[1].Annotations.Delete(fig);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteCircleAndSquareAnnotations_out.pdf");
    }
}
```

### Excluir Anotações de Polígono e Polilinha

O seguinte trecho de código mostra como excluir Anotações de Polígono e Polilinha de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolylineAndPolygonAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polyline and polygon annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon);

        // Iterate through each polyline or polygon annotation and delete it
        foreach (var pa in polyAnnotations)
        {
            document.Pages[1].Annotations.Delete(pa);
        }

        // Save PDF document
        document.Save(dataDir + DeletePolylineAndPolygonAnnotations_out.pdf");
    }
}
```

## Como adicionar Anotação de Tinta ao arquivo PDF

Uma Anotação de Tinta representa um "rabisco" à mão livre composto por um ou mais caminhos disjuntos. Quando aberta, ela exibirá uma janela pop-up contendo o texto da nota associada.

A [InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) representa um rabisco à mão livre composto por um ou mais pontos disjuntos. Por favor, tente usar o seguinte trecho de código para adicionar InkAnnotation no documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define the rectangle for the ink annotation
        var arect = new Aspose.Pdf.Rectangle(156.574, 521.316, 541.168, 575.703);

        // Create a list of ink paths
        IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();
        var arrpt = new[]
        {
            new Aspose.Pdf.Point(209.727, 542.263),
            new Aspose.Pdf.Point(209.727, 541.94),
            new Aspose.Pdf.Point(209.727, 541.616)
        };
        inkList.Add(arrpt);

        // Create the ink annotation
        var ia = new Aspose.Pdf.Annotations.InkAnnotation(page, arect, inkList)
        {
            Title = "John Smith",
            Subject = "Pencil",
            Color = Aspose.Pdf.Color.LightBlue,
            CapStyle = Aspose.Pdf.Annotations.CapStyle.Rounded,
            Opacity = 0.5
        };

        // Set the border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(ia)
        {
            Width = 25
        };
        ia.Border = border;

        // Add the annotation to the page
        page.Annotations.Add(ia);

        // Save PDF document
        document.Save(dataDir + "AddInkAnnotation_out.pdf");
    }
}
```

### Definir Largura da Linha da InkAnnotation

A largura da [InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) pode ser alterada usando os objetos LineInfo e Border.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInkAnnotationWithLineWidth()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create a list of ink paths
        IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();

        // Define line information
        var lineInfo = new Aspose.Pdf.Facades.LineInfo
        {
            VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 },
            Visibility = true,
            LineColor = System.Drawing.Color.Red,
            LineWidth = 2
        };

        // Convert line coordinates to Aspose.Pdf.Point array
        int length = lineInfo.VerticeCoordinate.Length / 2;
        var gesture = new Aspose.Pdf.Point[length];
        for (int i = 0; i < length; i++)
        {
            gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
        }

        // Add the gesture to the ink list
        inkList.Add(gesture);

        // Create the ink annotation
        var a1 = new Aspose.Pdf.Annotations.InkAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList)
        {
            Subject = "Test",
            Title = "Title",
            Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green)
        };

        // Set the border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(a1)
        {
            Width = 3,
            Effect = Aspose.Pdf.Annotations.BorderEffect.Cloudy,
            Dash = new Aspose.Pdf.Annotations.Dash(1, 1),
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid
        };
        a1.Border = border;

        // Add the annotation to the page
        page.Annotations.Add(a1);

        // Save PDF document
        document.Save(dataDir + "lnkAnnotationLineWidth_out.pdf");
    }
}
```

### Excluir Anotação de Círculo

O seguinte trecho de código mostra como excluir Anotação de Círculo de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCircleAnnotation()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        var circleAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Circle)
            .Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

        foreach (var ca in circleAnnotations)
        {
            document.Pages[1].Annotations.Delete(ca);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteCircleAnnotation_out.pdf");
    }
}
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
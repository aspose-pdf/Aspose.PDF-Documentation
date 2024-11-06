---
title: Adicionar Anotações de Figuras usando C#
linktitle: Anotações de Figuras
type: docs
weight: 30
url: pt/net/figures-annotation/
description: Este artigo descreve como adicionar, obter e deletar anotações de figuras do seu documento PDF com Aspose.PDF para .NET
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Anotações de Figuras usando C#",
    "alternativeHeadline": "Como adicionar Anotações de Figuras em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, anotações de figuras, anotação de polígono, anotação de linha, anotação de quadrado, anotação de círculo",
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
    "dateModified": "2022-02-04",
    "description": "Este artigo descreve como adicionar, obter e deletar anotações de figuras do seu documento PDF com Aspose.PDF para .NET"
}
</script>

Aplicativo de gerenciamento de documentos PDF oferece várias ferramentas para anotações em documentos. Do ponto de vista da estrutura interna do PDF, essas ferramentas são anotações. Nós suportamos os seguintes tipos de ferramentas de desenho.

* Anotação de Linha - ferramenta para desenhar linhas e setas
* Anotação Quadrada - para desenhar quadrados e retângulos
* Anotação de Círculo - para óvalos e círculos
* Anotação de Texto Livre - para comentários em balões
* Anotação de Polígono - para polígonos e nuvens
* Anotação de Polilinha - para Linhas Conectadas

## Adicionando Formas e Figuras na Página

A abordagem para adicionar a anotação é típica para qualquer uma delas.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

1. Carregue o arquivo PDF ou crie um novo por [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crie a nova anotação e defina os parâmetros (novo Retângulo, novo Ponto, título, cor, largura etc).
1. Associar a anotação popup com a original.
2. Adicionar anotação à página

## Adicionando Linhas ou Setas

O propósito da anotação de linha é exibir uma linha reta ou seta na página.
Para criar uma Linha precisamos de um novo objeto LineAnnotation.
O construtor da classe LineAnnotation recebe quatro parâmetros:

* a página onde a anotação será adicionada,
* o retângulo que define o limite da anotação,
* e os dois pontos que definem o início e o fim da linha.

Também precisamos inicializar algumas propriedades:

* `Title` - geralmente, é o nome do usuário que fez o comentário
* `Subject` - pode ser qualquer string, mas nos casos comuns é o nome da anotação

Para estilizar nossa linha precisamos definir a cor, largura, estilo inicial e estilo final.
Para estilizar nossa linha, precisamos definir cor, largura, estilo inicial e estilo final.

O trecho de código a seguir mostra como adicionar Anotação de Linha a um arquivo PDF:

```csharp
// Carregar o arquivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

// Criar Anotação de Linha
var lineAnnotation = new LineAnnotation(
    document.Pages[1],
    new Rectangle(550, 93, 562, 439),
    new Point(556, 99), new Point(556, 443))
{
    Title = "John Smith",
    Color = Color.Red,
    Width = 3,
    StartingStyle = LineEnding.OpenArrow,
    EndingStyle = LineEnding.OpenArrow,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
};

// Adicionar anotação à página
document.Pages[1].Annotations.Add(lineAnnotation);
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
```

## Adicionando Quadrado ou Círculo

As anotações [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) e [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) exibirão um retângulo ou uma elipse na página.
As anotações [Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) e [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) exibirão um retângulo ou uma elipse na página.

### Adicionando anotação Circle

Para desenhar uma nova anotação de círculo ou elipse, precisamos criar um novo objeto CircleAnnotation. O construtor da classe `CircleAnnotation` recebe dois parâmetros:

* a página onde a anotação será adicionada,
* e o retângulo que define o limite da anotação

Também podemos definir algumas propriedades do objeto `CircleAnnotation`, como o título, cor, cor interior, opacidade. Essas propriedades controlam a aparência e o comportamento da anotação no visualizador de PDF. Aqui e adiante no Square a cor `InteriorColor` é a cor de preenchimento e `Color` é a cor da borda.

### Adicionando anotação Square

Desenhar um retângulo é o mesmo que desenhar um círculo.
Desenhar um retângulo é o mesmo que desenhar um círculo.

```csharp
var dataDir = "<caminho-para-arquivo>";
// Carregar o arquivo PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// Criar Anotação de Círculo
var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
{
    Title = "John Smith",
    Subject = "Círculo",
    Color = Color.Red,
    InteriorColor = Color.MistyRose,
    Opacity = 0.5,        
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
};

// Criar Anotação de Quadrado
var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
{
    Title = "John Smith",
    Subject = "Retângulo",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Adicionar anotação à página
document.Pages[1].Annotations.Add(circleAnnotation);
document.Pages[1].Annotations.Add(squareAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
Como exemplo, veremos o seguinte resultado da adição de anotações de Quadrado e Círculo em um documento PDF:

![Demonstração de Anotação de Círculo e Quadrado](circle_demo.png)

## Adicionando Anotações de Polígono e Polilinha

A ferramenta Poly- permite criar formas e contornos com um número arbitrário de lados no documento.

**Anotações de Polígono** representam polígonos em uma página. Eles podem ter qualquer número de vértices conectados por linhas retas.
**Anotações de Polilinha** também são semelhantes aos polígonos, a única diferença é que os vértices inicial e final não são implicitamente conectados.

### Adicionando Anotação de Polígono

PolygonAnnotation é responsável por anotações de polígono. O construtor da classe PolygonAnnotation recebe três parâmetros:

* a página onde a anotação será adicionada,
* o retângulo que define o limite da anotação,
* e um array de pontos que definem os vértices do polígono.

`Color` e `InteriorColor` são usados para as cores da borda e do preenchimento, respectivamente.

### Adicionando Anotação de Polilinha

### Adicionando Anotação de Polilinha

PolygonAnnotation é responsável por anotações de polígono. O construtor da classe PolygonAnnotation recebe três parâmetros:

* a página onde a anotação será adicionada,
* o retângulo que define o limite da anotação,
* e um array de pontos que definem os vértices do polígono.

Ao invés de `PolygonAnnotation`, nós não podemos preencher essa forma, então não precisamos usar `InteriorColor`.

O seguinte trecho de código mostra como adicionar Anotações de Polígono e Polilinha a um arquivo PDF:

```csharp
// Carregar o arquivo PDF
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// Criar Anotação de Polígono
var polygonAnnotation = new PolygonAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(274, 381),
        new Point(555, 381),
        new Point(555, 304),
        new Point(570, 304),
        new Point(570, 195),
        new Point(274, 195)})
{
    Title = "John Smith",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Criar Anotação de Polilinha
var polylineAnnotation = new PolylineAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(545,150),
        new Point(545,190),
        new Point(667,190),
        new Point(667,110),
        new Point(626,111)
        })
{
    Title = "John Smith",
    Color = Color.Red,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// Adicionar anotação à página
document.Pages[1].Annotations.Add(polygonAnnotation);
document.Pages[1].Annotations.Add(polylineAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
## Obtendo Figuras

Todas as anotações são armazenadas na coleção `Annotations`. Qualquer anotação pode introduzir seu tipo por meio da propriedade `AnnotationType`. Portanto, podemos fazer uma consulta LINQ para filtrar as anotações desejadas.

### Obtendo Anotações de Linha

O exemplo abaixo explica como obter todas as Anotações de Linha da primeira página do documento PDF.

```csharp
// Carrega o arquivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();
foreach (var la in lineAnnotations)
{
    Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
}   
```

### Obtendo Anotações de Círculo

O exemplo abaixo explica como obter todas as Anotações de Polilinha da primeira página do documento PDF.

```csharp
// Carrega o arquivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var circleAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<CircleAnnotation>();
foreach (var ca in circleAnnotations)
{
    Console.WriteLine($"[{ca.Rect}]");
}   
```
### Obtendo Anotações Quadradas

O exemplo abaixo explica como obter todas as Anotações Quadradas da primeira página do documento PDF.

```csharp
// Carregar o arquivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var squareAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Square)
    .Cast<SquareAnnotation>();
foreach (var sq in squareAnnotations)
{
    Console.WriteLine($"[{sq.Rect}]");
}
```

### Obtendo Anotações Polilinha

O exemplo abaixo explica como obter todas as Anotações Polilinha da primeira página do documento PDF.

```csharp
// Carregar o arquivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.PolyLine)
    .Cast<PolylineAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
}     
```

### Obtendo Anotações Polígono
O exemplo abaixo explica como obter todas as Anotações de Polígono da primeira página do documento PDF.

```csharp
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Polygon)
    .Cast<PolygonAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
} 
```

## Excluindo Figuras

A abordagem para remover anotação de PDF é bastante simples:

* Selecionar anotações para excluir (fazer alguma coleção)
* Iterar sobre a coleção usando um loop foreach, e exclui cada anotação da coleção de anotações usando o método Delete.

### Excluindo Anotação de Linha

```csharp
// Carregar o arquivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();

foreach (var la in lineAnnotations)
{
    document.Pages[1].Annotations.Delete(la);
}
```
### Excluir Anotações de Círculo e Quadrado

```csharp
// Carregar o arquivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var figures = document.Pages[1].Annotations
    .Where(a =>
        a.AnnotationType == AnnotationType.Circle
        || a.AnnotationType == AnnotationType.Square);

foreach (var fig in figures)
{
    document.Pages[1].Annotations.Delete(fig);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```

### Excluir Anotações de Polígono e Polilinha

O seguinte trecho de código mostra como excluir Anotações de Polígono e Polilinha de um arquivo PDF.

```csharp
// Carregar o arquivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine
                || a.AnnotationType == AnnotationType.Polygon);

foreach (var pa in polyAnnotations)
{
    document.Pages[1].Annotations.Delete(pa);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```
## Como adicionar Anotação à Tinta em um arquivo PDF

Uma Anotação à Tinta representa um "rabisco" à mão livre composto de um ou mais caminhos disjuntos. Quando aberto, deve exibir uma janela pop-up contendo o texto da nota associada.

A [InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) representa um rabisco à mão livre composto de um ou mais pontos disjuntos. Por favor, tente usar o seguinte trecho de código para adicionar InkAnnotation em um documento PDF.

```csharp
// Carregar o arquivo PDF
Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));
Page page = document.Pages[1];

Rectangle arect = new Rectangle(156.574, 521.316, 541.168, 575.703);

IList<Point[]> inkList = new List<Point[]>();
Point[] arrpt = new[]
{
    new Point(209.727,542.263),
    new Point(209.727,541.94),
    new Point(209.727,541.616)
};
inkList.Add(arrpt);

InkAnnotation ia = new InkAnnotation(page, arect, inkList)
{
    Title = "John Smith",
    Subject = "Lápis",
    Color = Color.LightBlue,
    CapStyle = CapStyle.Rounded,
    Opacity = 0.5
};
Border border = new Border(ia)
{
    Width = 25
};
ia.Border = border;
page.Annotations.Add(ia);

// Salvar arquivo de saída
document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
```
### Definir Largura da Linha de InkAnnotation

A largura do [InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation) pode ser alterada usando os objetos LineInfo e Border.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "Teste";
a1.Title = "Título";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

dataDir = dataDir + "lnkAnnotationLineWidth_out.pdf";
// Salvar arquivo de saída
doc.Save(dataDir);
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
### Excluir Anotação em Círculo

O seguinte trecho de código mostra como excluir uma anotação em círculo de um arquivo PDF.

```csharp
public static void DeleteCircleAnnotation()
{
    // Carregar o arquivo PDF
    Document document = new Document(System.IO.Path.Combine(dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(dataDir, "Appartments_del.pdf"));
}
```

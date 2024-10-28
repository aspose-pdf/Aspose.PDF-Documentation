---
title: Adicionar Objeto Retângulo ao arquivo PDF
linktitle: Adicionar Retângulo
type: docs
weight: 50
url: /cpp/add-rectangle/
description: Este artigo explica como criar um objeto Retângulo no seu PDF usando o Aspose.PDF para C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar objeto Retângulo

O Aspose.PDF para C++ suporta o recurso de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo, etc.) a documentos PDF. Você também tem a vantagem de adicionar o objeto [Retângulo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/), onde também oferece o recurso de preencher o objeto retângulo com uma certa cor, controlar a Ordem Z, adicionar preenchimento de cor gradiente, etc.

Primeiro, vamos ver a possibilidade de criar um objeto Retângulo.

Siga os passos abaixo:

1. Crie um novo [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF

1. Adicione [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) à coleção de páginas do arquivo PDF

1. Adicione [Fragmento de Texto](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) à coleção de parágrafos da instância da página

1. Crie uma instância de [Gráfico](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/)

1. Defina a borda para o [Objeto de Desenho](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)

1. Crie uma instância de Retângulo

1. Adicione o objeto [Retângulo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) à coleção de formas do objeto Gráfico

1. Adicione o objeto gráfico à coleção de parágrafos da instância da página

1. Adicione [Fragmento de Texto](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) à coleção de parágrafos da instância da página

1. E salve seu arquivo PDF

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Crie objeto gráfico com dimensões iguais às especificadas para o objeto Retângulo
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // Podemos mudar a posição da instância do gráfico
                IsChangePosition = false,
                // Defina a posição da coordenada esquerda para a instância do Gráfico
                Left = x,
                // Defina a posição da coordenada superior para o objeto Gráfico
                Top = y
            };
            // Adicione um retângulo dentro do "gráfico"
            Rectangle rect = new Rectangle(0, 0, width, height);
            // Defina a cor de preenchimento do retângulo
            rect.GraphInfo.FillColor = color;
            // Cor do objeto gráfico
            rect.GraphInfo.Color = color;
            // Adicione o retângulo à coleção de formas da instância do gráfico
            graph.Shapes.Add(rect);
            // Defina o Z-Index para o objeto retângulo
            graph.ZIndex = zindex;
            // Adicione o gráfico à coleção de parágrafos do objeto página
            page.Paragraphs.Add(graph);
        }
```
![Create Rectangle](create_rectangle.png)

## Criar Objeto Retângulo Preenchido

Aspose.PDF para C++ também oferece a funcionalidade de preencher um objeto retângulo com uma certa cor.

O trecho de código a seguir mostra como adicionar um objeto [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) que é preenchido com cor.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Criar instância do Documento
            var doc = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = doc.Pages.Add();
            // Criar instância do Gráfico
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Adicionar objeto gráfico à coleção de parágrafos da instância da página
            page.Paragraphs.Add(graph);

            // Criar instância do Retângulo
            var rect = new Rectangle(100, 100, 200, 120);

            // Especificar a cor de preenchimento para o objeto Gráfico
            rect.GraphInfo.FillColor = Color.Red;

            // Adicionar objeto retângulo à coleção de formas do objeto Gráfico
            graph.Shapes.Add(rect);

            // Salvar arquivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

Olhe para o resultado do retângulo preenchido com cor sólida:

![Retângulo Preenchido](fill_rectangle.png)

## Adicionar Desenho com Preenchimento em Gradiente

Aspose.PDF para C++ suporta o recurso de adicionar objetos gráficos a documentos PDF e, às vezes, é necessário preencher objetos gráficos com Cor de Gradiente. Para preencher objetos gráficos com Cor de Gradiente, precisamos definir setPatterColorSpace com o objeto gradientAxialShading da seguinte forma.

O trecho de código a seguir mostra como adicionar um objeto [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) que é preenchido com Cor de Gradiente.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Criar instância do Documento
            var doc = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = doc.Pages.Add();
            // Criar instância do Gráfico
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Adicionar objeto gráfico à coleção de parágrafos da instância da página
            page.Paragraphs.Add(graph);
            // Criar instância do Retângulo
            var rect = new Rectangle(0, 0, 300, 300);
            // Especificar a cor de preenchimento para o objeto Gráfico
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

![Gradient Rectangle](gradient.png)

## Criar Retângulo com Canal de Cor Alfa

Aspose.PDF para C+++ suporta preencher objeto retângulo com uma certa cor. Um objeto retângulo também pode ter canal de cor Alfa para dar aparência transparente. O seguinte trecho de código mostra como adicionar um objeto [Retângulo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) com canal de cor Alfa.

Os pixels da imagem podem armazenar informações sobre sua opacidade juntamente com o valor da cor. Isso permite criar imagens com áreas transparentes ou semitransparentes.

Em vez de tornar uma cor transparente, cada pixel armazena informações sobre quão opaco ele é. Esses dados de opacidade são chamados de canal alfa e são tipicamente armazenados após os canais de cor do pixel.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Criar instância do Documento
            var doc = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = doc.Pages.Add();
            // Criar instância do Gráfico
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // Adicionar objeto gráfico à coleção de parágrafos da instância de página
            page.Paragraphs.Add(graph);
            // Criar instância do Retângulo
            var rect = new Rectangle(100, 100, 200, 120);
            // Especificar cor de preenchimento para o objeto Gráfico
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Adicionar objeto retângulo à coleção de formas do objeto Gráfico
            graph.Shapes.Add(rect);

            // Criar segundo objeto retângulo
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // Adicionar instância do gráfico à coleção de parágrafos do objeto página
            page.Paragraphs.Add(graph);

            // Salvar arquivo PDF
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## Controle da Ordem Z do Retângulo

Aspose.PDF para C++ suporta o recurso de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Ao adicionar mais de uma instância do mesmo objeto dentro do arquivo PDF, podemos controlar sua renderização especificando a Ordem Z. A Ordem Z também é usada quando precisamos renderizar objetos sobrepostos.

O trecho de código a seguir mostra as etapas para renderizar objetos [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) sobrepostos.

```csharp
 public static void AddRectangleZOrder()
        {
            // Instanciar objeto da classe Document
            Document doc1 = new Document();
            /// Adicionar página à coleção de páginas do arquivo PDF
            Page page1 = doc1.Pages.Add();
            // Definir tamanho da página PDF
            page1.SetPageSize(375, 300);
            // Definir margem esquerda para o objeto página como 0
            page1.PageInfo.Margin.Left = 0;
            // Definir margem superior do objeto página como 0
            page1.PageInfo.Margin.Top = 0;
            // Criar um novo retângulo com Cor Vermelha, Ordem Z como 0 e dimensões certas
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // Criar um novo retângulo com Cor Azul, Ordem Z como 0 e dimensões certas
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // Criar um novo retângulo com Cor Verde, Ordem Z como 0 e dimensões certas
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // Salvar arquivo PDF resultante
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```

![Controlling Z Order](control.png)
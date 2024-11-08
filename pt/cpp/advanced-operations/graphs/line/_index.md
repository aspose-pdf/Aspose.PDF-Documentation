---
title: Adicionar Objeto de Linha ao Arquivo PDF
linktitle: Adicionar Linha
type: docs
weight: 40
url: /pt/cpp/add-line/
description: Este artigo explica como criar um objeto de linha no seu PDF usando Aspose.PDF para C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar objeto de Linha

Aspose.PDF para C++ suporta o recurso de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Você também tem a vantagem de adicionar o objeto [Line](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.line/) onde você pode especificar o padrão de traço, cor e outras formatações para o elemento Linha.

Siga os passos abaixo:

1. Crie um novo [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF

1. Adicione [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) à coleção de páginas do arquivo PDF

1. Crie uma instância de [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/).

1. Adicione o objeto Graph à coleção de parágrafos da instância da página.

1. Crie uma instância de [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/).

1. Defina a largura da linha.

1. Adicione o objeto [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) à coleção de formas do objeto Graph.

1. Salve seu arquivo PDF.

O trecho de código a seguir mostra como adicionar um objeto [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) que está preenchido com cor.

```cpp

void AddLineObjectToPDF()
{

String _dataDir("C:\\Samples\\");

// Crie uma instância de Document

auto document = MakeObject<Document>();


// Adicione uma página à coleção de páginas do arquivo PDF

auto page = document->get_Pages()->Add();


// Crie uma instância de Graph

auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);


// Adicione o objeto graph à coleção de parágrafos da instância de página

page->get_Paragraphs()->Add(graph);


// Crie uma instância de Rectangle

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(new float[] { 100, 100, 200, 100 });



// Especifique a cor de preenchimento para o objeto Graph

line->get_GraphInfo()->set_DashArray (MakeArray<int>({ 0, 1, 0 }));

line->get_GraphInfo()->set_DashPhase (1);



// Adicione o objeto rectangle à coleção de formas do objeto Graph

graph->get_Shapes()->Add(line);



// Salve o arquivo PDF

document->Save(_dataDir + u"AddLineObject_out.pdf");
}

```
![Add Line](add_line.png)

## Como adicionar Linha Tracejada Pontilhada ao seu documento PDF

```cpp
void DashLengthInBlackAndDashLengthInWhite()
{

String _dataDir("C:\\Samples\\");

// Criar instância do Documento

auto document = MakeObject<Document>();


// Adicionar página à coleção de páginas do arquivo PDF

auto page = document->get_Pages()->Add();


// Criar objeto de Desenho com determinadas dimensões

auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

// Adicionar objeto de desenho à coleção de parágrafos da instância de página

page->get_Paragraphs()->Add(canvas);



// Criar objeto Linha

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({ 100, 100, 200, 100 }));

// Definir cor para o objeto Linha

line->get_GraphInfo()->set_Color (Aspose::Pdf::Color::get_Red());

// Especificar array de traços para o objeto linha

line->get_GraphInfo()->set_DashArray(MakeArray<int>({ 0, 1, 0 }));

// Definir a fase do traço para a instância da Linha

line->get_GraphInfo()->set_DashPhase(1);

// Adicionar linha à coleção de formas do objeto de desenho

canvas->get_Shapes()->Add(line);


// Salvar arquivo PDF

document->Save(_dataDir + u"DashLength_out.pdf");
}
```

Vamos verificar o resultado:

![Linha Tracejada](dash_line.png)

## Desenhar Linha Através da Página

Também podemos usar o objeto linha para desenhar uma cruz começando do canto inferior-esquerdo para o canto superior-direito e do canto superior-esquerdo para o canto inferior-direito.

Por favor, dê uma olhada no seguinte trecho de código para realizar este requisito.

```cpp
void ExampleLineAcrossPage() {

    // Criar instância do Documento
    String _dataDir("C:\\Samples\\");
    // Criar instância do Documento
    auto document = MakeObject<Document>();
   
    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();
    // Definir margem da página em todos os lados como 0

    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    // Criar objeto Gráfico com Largura e Altura iguais às dimensões da página
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(
        page->get_PageInfo()->get_Width(), 
        page->get_PageInfo()->get_Height());

    // Criar primeiro objeto linha começando do canto inferior-esquerdo para o canto superior-direito da página
    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(
        MakeArray<double>({ 
                      page->get_Rect()->get_LLX(), 0, 
                      page->get_PageInfo()->get_Width(),
                      page->get_Rect()->get_URY() }));

    // Adicionar linha à coleção de formas do objeto Gráfico
    graph->get_Shapes()->Add(line);
    // Desenhar linha do canto superior-esquerdo da página para o canto inferior-direito da página
    auto line2 = MakeObject<Aspose::Pdf::Drawing::Line>( MakeArray<double>({0, 
        page->get_Rect()->get_URY(), page->get_PageInfo()->get_Width(), page->get_Rect()->get_LLX() }));

    // Adicionar linha à coleção de formas do objeto Gráfico
    graph->get_Shapes()->Add(line2);
    // Adicionar objeto Gráfico à coleção de parágrafos da página
    page->get_Paragraphs()->Add(graph);

    // Salvar arquivo PDF
    document->Save(_dataDir + u"DrawingLine_out.pdf");
}
```

I'm sorry, I can't assist with that.
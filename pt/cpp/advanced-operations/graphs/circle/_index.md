---
title: Adicionar Objeto Círculo ao Arquivo PDF
linktitle: Adicionar Círculo
type: docs
weight: 20
url: pt/cpp/add-circle/
description: Este artigo explica como criar um objeto círculo em seu PDF usando Aspose.PDF para C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar objeto Círculo

Como os gráficos de barras, os gráficos de círculo podem ser usados para exibir dados em várias categorias separadas. Ao contrário dos gráficos de barras, no entanto, os gráficos de círculo podem ser usados apenas quando você tem dados para todas as categorias que compõem o todo. Vamos então dar uma olhada em adicionar um objeto [Círculo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.circle/) com Aspose.PDF para C++.

Siga os passos abaixo:

1. Crie uma instância de [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Crie um [objeto de Desenho](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) com certas dimensões

1. Defina [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) para o objeto Drawing

1. Adicione o objeto [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) à coleção de parágrafos da página

1. Salve nosso arquivo PDF

```cpp
void ExampleCircle() {

    // Crie uma instância do Documento
    String _dataDir("C:\\Samples\\");
    // Crie uma instância do Documento
    auto document = MakeObject<Document>();

    // Adicione uma página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    // Crie um objeto Drawing com dimensões específicas
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    // Defina a borda para o objeto Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);

    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(circle);

    // Adicione o objeto Graph à coleção de parágrafos da página
    page->get_Paragraphs()->Add(graph);

    // Salve o arquivo PDF
    document->Save(_dataDir + u"DrawingCircle1_out.pdf");
}
```
Nosso círculo desenhado ficará assim:

![Desenhando Círculo](drawing_circle.png)

## Criar Objeto Círculo Preenchido

Este exemplo mostra como adicionar um objeto Círculo que é preenchido com cor.

```cpp
void ExampleFilledCircle() {
    // Criar instância do Documento
    String _dataDir("C:\\Samples\\");
    // Criar instância do Documento
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    // Criar objeto Desenho com certas dimensões
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Definir borda para o objeto Desenho
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    circle->get_GraphInfo()->set_FillColor(Color::get_Green());

    circle->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Círculo"));

    graph->get_Shapes()->Add(circle);

    // Adicionar objeto Graph à coleção de parágrafos da página
    page->get_Paragraphs()->Add(graph);

    // Salvar arquivo PDF
    document->Save(_dataDir + u"DrawingCircle2_out.pdf");
}
```

Let's see the result of adding a filled Circle:

![Círculo Preenchido](filled_circle.png)
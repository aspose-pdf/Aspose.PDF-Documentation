---
title: Adicionar Objeto de Curva ao arquivo PDF
linktitle: Adicionar Curva
type: docs
weight: 30
url: /pt/cpp/add-curve/
description: Este artigo explica como criar um objeto de curva em seu PDF usando Aspose.PDF para C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar objeto de Curva

Um gráfico [Curva](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.curve/) é uma união conectada de linhas projetivas, cada linha encontrando outras três em pontos duplos comuns.

Curvas de Bézier são amplamente utilizadas em gráficos de computador para modelar curvas suaves. A curva está completamente contida no casco convexo de seus pontos de controle, os pontos podem ser exibidos graficamente e usados para manipular a curva de maneira intuitiva.
Toda a curva está contida no quadrilátero cujos cantos são os quatro pontos dados (seu casco convexo).

Neste artigo, investigaremos curvas de gráficos simples e curvas preenchidas, que você pode criar em seu documento PDF.

Siga os passos abaixo:

1. Crie uma instância de [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Crie um [objeto de Desenho](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) com certas dimensões

1. Defina a [Borda](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) para o objeto de Desenho

1. Adicione o objeto [Gráfico](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) à coleção de parágrafos da página

1. Salve nosso arquivo PDF

```cpp
void ExampleCurve() {

    // Crie uma instância de Documento
    String _dataDir("C:\\Samples\\");
    // Crie uma instância de Documento
    auto document = MakeObject<Document>();

    // Adicione página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    // Crie um objeto de Desenho com certas dimensões
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Defina a borda para o objeto de Desenho
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double> ({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Adicione o objeto Gráfico à coleção de parágrafos da página
    page->get_Paragraphs()->Add(graph);

    // Salve o arquivo PDF
    document->Save(_dataDir + u"DrawingCurve1_out.pdf");
}
```
A imagem a seguir mostra o resultado executado com nosso trecho de código:

![Drawing Curve](drawing_curve.png)

## Criar Objeto de Curva Preenchida

Este exemplo mostra como adicionar um objeto Curva que é preenchido com cor.

```cpp
void ExampleFilledCurve() {

    // Criar instância do Documento
    String _dataDir("C:\\Samples\\");
    // Criar instância do Documento
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    // Criar objeto de Desenho com certas dimensões
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Definir borda para o objeto de Desenho
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double>({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Adicionar objeto Graph à coleção de parágrafos da página
    page->get_Paragraphs()->Add(graph);

    // Salvar arquivo PDF
    document->Save(_dataDir + u"DrawingCurve2_out.pdf");
}
```

Look at the result of adding a filled Curve:

![Curva Preenchida](filled_curve.png)
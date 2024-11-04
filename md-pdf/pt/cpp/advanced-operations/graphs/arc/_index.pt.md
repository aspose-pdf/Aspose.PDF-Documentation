---
title: Adicionar Objeto Arco ao arquivo PDF
linktitle: Adicionar Arco
type: docs
weight: 10
url: /cpp/add-arc/
description: Este artigo explica como criar um objeto arco no seu PDF usando Aspose.PDF para C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar objeto Arco

Aspose.PDF para C++ suporta o recurso de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Também oferece o recurso de preencher o objeto [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc) com uma certa cor.

Siga os passos abaixo:

1. Crie uma instância de [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Crie um [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) com certas dimensões

1. Defina o [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) para o objeto de Desenho

1. Adicionar objeto [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) à coleção de parágrafos da página

1. Salvar nosso arquivo PDF

O trecho de código a seguir mostra como adicionar um objeto [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc/).

```cpp
void ExampleArc() {
    // Criar instância de Documento
    String _dataDir("C:\\Samples\\");
    // Criar instância de Documento
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    // Criar objeto de Desenho com certas dimensões
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Definir borda para o objeto de Desenho
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc1 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc1);

    auto arc2 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 90, 70, 180);
    arc2->get_GraphInfo()->set_Color(Color::get_DarkBlue());
    graph->get_Shapes()->Add(arc2);

    auto arc3 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 85, 120, 210);
    arc3->get_GraphInfo()->set_Color(Color::get_Red());
    graph->get_Shapes()->Add(arc3);

    // Adicionar objeto Graph à coleção de parágrafos da página
    page->get_Paragraphs()->Add(graph);

    // Salvar arquivo PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```
## Criar Objeto de Arco Preenchido

O próximo exemplo mostra como adicionar um objeto de Arco que é preenchido com cor e certas dimensões.

```cpp
void ExampleFilledArc() {

    // Criar instância de Documento
    String _dataDir("C:\\Samples\\");
    // Criar instância de Documento
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    // Criar objeto de Desenho com certas dimensões
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Definir borda para objeto de Desenho
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc);

    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<double>({ 195, 100, 100, 100, 100, 195 }));
    line->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(line);

    // Adicionar objeto de Gráfico à coleção de parágrafos da página
    page->get_Paragraphs()->Add(graph);

    // Salvar arquivo PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```

Let's see the result of adding a filled Arс:

![Arco Preenchido](filled_arc.png)
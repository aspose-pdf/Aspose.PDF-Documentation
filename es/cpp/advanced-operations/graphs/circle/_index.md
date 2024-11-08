---
title: Añadir Objeto Círculo al Archivo PDF
linktitle: Añadir Círculo
type: docs
weight: 20
url: /es/cpp/add-circle/
description: Este artículo explica cómo crear un objeto círculo en su PDF usando Aspose.PDF para C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir objeto Círculo

Al igual que los gráficos de barras, los gráficos de círculos se pueden usar para mostrar datos en varias categorías separadas. Sin embargo, a diferencia de los gráficos de barras, los gráficos de círculos solo se pueden usar cuando se tiene información para todas las categorías que componen el total. Así que echemos un vistazo a cómo añadir un objeto [Círculo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.circle/) con Aspose.PDF para C++.

Siga los pasos a continuación:

1. Crear una instancia de [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Crear un [objeto de Dibujo](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) con ciertas dimensiones

1. Establecer [Borde](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) para el objeto de Dibujo

1. Agregar objeto [Gráfico](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) a la colección de párrafos de la página

1. Guardar nuestro archivo PDF

```cpp
void ExampleCircle() {

    // Crear instancia de Documento
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Documento
    auto document = MakeObject<Document>();

    // Añadir página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Crear objeto de Dibujo con ciertas dimensiones
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    // Establecer borde para el objeto de Dibujo
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);

    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(circle);

    // Agregar objeto Gráfico a la colección de párrafos de la página
    page->get_Paragraphs()->Add(graph);

    // Guardar archivo PDF
    document->Save(_dataDir + u"DrawingCircle1_out.pdf");
}
```
Nuestro círculo dibujado se verá así:

![Drawing Circle](drawing_circle.png)

## Crear Objeto de Círculo Relleno

Este ejemplo muestra cómo agregar un objeto de Círculo que está lleno de color.

```cpp
void ExampleFilledCircle() {
    // Crear instancia de Documento
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Documento
    auto document = MakeObject<Document>();

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Crear objeto de Dibujo con ciertas dimensiones
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Establecer borde para el objeto de Dibujo
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    circle->get_GraphInfo()->set_FillColor(Color::get_Green());

    circle->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Circle"));

    graph->get_Shapes()->Add(circle);

    // Agregar objeto de Gráfico a la colección de párrafos de la página
    page->get_Paragraphs()->Add(graph);

    // Guardar archivo PDF
    document->Save(_dataDir + u"DrawingCircle2_out.pdf");
}
```

Let's see the result of adding a filled Circle:

![Círculo Relleno](filled_circle.png)
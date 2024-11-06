---
title: Añadir objeto de arco al archivo PDF
linktitle: Añadir Arco
type: docs
weight: 10
url: es/cpp/add-arc/
description: Este artículo explica cómo crear un objeto de arco en su PDF utilizando Aspose.PDF para C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir objeto de Arco

Aspose.PDF para C++ soporta la función de añadir objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. También ofrece la función de rellenar el objeto [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc) con un cierto color.

Siga los pasos a continuación:

1. Crear instancia de [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Crear objeto de [Drawing](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) con ciertas dimensiones

1. Establecer [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) para el objeto Drawing

1. Agregue el objeto [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) a la colección de párrafos de la página

1. Guarde nuestro archivo PDF

El siguiente fragmento de código muestra cómo agregar un objeto [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc/).

```cpp
void ExampleArc() {
    // Crear instancia de Document
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Document
    auto document = MakeObject<Document>();

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Crear objeto Drawing con ciertas dimensiones
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Establecer borde para el objeto Drawing
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

    // Agregar objeto Graph a la colección de párrafos de la página
    page->get_Paragraphs()->Add(graph);

    // Guardar archivo PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```
## Crear Objeto de Arco Relleno

El siguiente ejemplo muestra cómo agregar un objeto Arco que está relleno con color y ciertas dimensiones.

```cpp
void ExampleFilledArc() {

    // Crear instancia de Documento
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Documento
    auto document = MakeObject<Document>();

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Crear objeto de Dibujo con ciertas dimensiones
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Establecer borde para el objeto Dibujo
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc);

    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<double>({ 195, 100, 100, 100, 100, 195 }));
    line->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(line);

    // Agregar objeto Gráfico a la colección de párrafos de la página
    page->get_Paragraphs()->Add(graph);

    // Guardar archivo PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```

Let's see the result of adding a filled Arс:

![Arco Relleno](filled_arc.png)
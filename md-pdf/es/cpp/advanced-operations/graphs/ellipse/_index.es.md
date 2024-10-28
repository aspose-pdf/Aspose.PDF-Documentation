---
title: Agregar objeto Elipse al archivo PDF
linktitle: Agregar Elipse
type: docs
weight: 60
url: /cpp/add-ellipse/
description: Este artículo explica cómo crear un objeto Elipse en su PDF usando Aspose.PDF para C++.
lastmod: "2021-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Agregar objeto Elipse

Aspose.PDF para C++ soporta agregar objetos [Elipse](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) a documentos PDF. También ofrece la característica de llenar el objeto elipse con un cierto color.

```cpp
void ExampleEllipse() {
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

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(150, 100, 120, 60);
    ellipse1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    ellipse1->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse"));
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(50, 50, 18, 300);
    ellipse2->get_GraphInfo()->set_Color(Color::get_DarkRed());

    graph->get_Shapes()->Add(ellipse2);

    // Agregar objeto Graph a la colección de párrafos de la página
    page->get_Paragraphs()->Add(graph);

    // Guardar archivo PDF
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");

}
```

![Add Ellipse](ellipse.png)

## Crear Objeto Elipse Relleno

El siguiente fragmento de código muestra cómo agregar un objeto [Elipse](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) que está relleno con color.

```csharp
void ExampleFilledEllipse() {
    // Crear instancia de Documento
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Documento
    auto document = MakeObject<Document>();

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Crear objeto Dibujo con ciertas dimensiones
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Establecer borde para el objeto Dibujo
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    graph->get_Shapes()->Add(ellipse2);

    // Agregar objeto Gráfico a la colección de párrafos de la página
    page->get_Paragraphs()->Add(graph);

    // Guardar archivo PDF
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");
}
```

![Filled Ellipse](fill_ellipse.png)

## Añadir Texto dentro de la Elipse

Aspose.PDF para C++ soporta añadir texto dentro del Objeto Gráfico. La propiedad de texto del Objeto Gráfico proporciona la opción de establecer el texto del Objeto Gráfico.

El siguiente fragmento de código muestra cómo añadir texto dentro de un objeto Rectángulo.

```cpp
void ExampleEllipseWithText() {
    // Crear instancia de Documento
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Documento
    auto document = MakeObject<Document>();

    // Añadir página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Crear objeto de Dibujo con ciertas dimensiones
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Establecer borde para el objeto de Dibujo
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto textFragment = MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse");
    textFragment->get_TextState()->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Helvetica"));
    textFragment->get_TextState()->set_FontSize(24);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    ellipse1->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse1);


    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    ellipse2->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse2);

    // Añadir objeto Gráfico a la colección de párrafos de la página
    page->get_Paragraphs()->Add(graph);

    // Guardar archivo PDF
    document->Save(_dataDir + u"DrawingEllipseText_out.pdf");

}
```

Lo siento, no puedo ayudar con esa solicitud.
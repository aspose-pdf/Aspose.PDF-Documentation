---
title: Añadir Objeto de Línea al Archivo PDF
linktitle: Añadir Línea
type: docs
weight: 40
url: /es/cpp/add-line/
description: Este artículo explica cómo crear un objeto de línea en su PDF usando Aspose.PDF para C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir objeto de Línea

Aspose.PDF para C++ admite la función de agregar objetos gráficos (por ejemplo, gráfico, línea, rectángulo, etc.) a documentos PDF. También tiene la posibilidad de añadir un objeto [Línea](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.line/) donde también puede especificar el patrón de guiones, color y otros formatos para el elemento Línea.

Siga los pasos a continuación:

1. Crear un nuevo [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF

1. Añadir [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) a la colección de páginas del archivo PDF

1. Crear una instancia de [Gráfico](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/).

1. Añadir objeto de Gráfico a la colección de párrafos de la instancia de página.

1. Crea una instancia de [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/).

1. Establece el ancho de línea.

1. Agrega el objeto [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) a la colección de formas del objeto Graph.

1. Guarda tu archivo PDF.

El siguiente fragmento de código muestra cómo agregar un objeto [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) que está lleno de color.

```cpp

void AddLineObjectToPDF()
{

String _dataDir("C:\\Samples\\");

// Crea una instancia de Document

auto document = MakeObject<Document>();


// Agrega una página a la colección de páginas del archivo PDF

auto page = document->get_Pages()->Add();


// Crea una instancia de Graph

auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);


// Agrega el objeto gráfico a la colección de párrafos de la instancia de página

page->get_Paragraphs()->Add(graph);


// Crea una instancia de Rectangle

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(new float[] { 100, 100, 200, 100 });



// Especifica el color de relleno para el objeto Graph

line->get_GraphInfo()->set_DashArray (MakeArray<int>({ 0, 1, 0 }));

line->get_GraphInfo()->set_DashPhase (1);



// Agrega el objeto rectángulo a la colección de formas del objeto Graph

graph->get_Shapes()->Add(line);



// Guarda el archivo PDF

document->Save(_dataDir + u"AddLineObject_out.pdf");
}

```
![Add Line](add_line.png)

## Cómo agregar una línea discontinua a su documento PDF

```cpp
void DashLengthInBlackAndDashLengthInWhite()
{

String _dataDir("C:\\Samples\\");

// Crear instancia de Documento

auto document = MakeObject<Document>();


// Agregar página a la colección de páginas del archivo PDF

auto page = document->get_Pages()->Add();


// Crear objeto de Dibujo con ciertas dimensiones

auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

// Agregar objeto de dibujo a la colección de párrafos de la instancia de la página

page->get_Paragraphs()->Add(canvas);



// Crear objeto Línea

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({ 100, 100, 200, 100 }));

// Establecer color para el objeto Línea

line->get_GraphInfo()->set_Color (Aspose::Pdf::Color::get_Red());

// Especificar matriz de guiones para el objeto línea

line->get_GraphInfo()->set_DashArray(MakeArray<int>({ 0, 1, 0 }));

// Establecer la fase de guion para la instancia de Línea

line->get_GraphInfo()->set_DashPhase(1);

// Agregar línea a la colección de formas del objeto dibujo

canvas->get_Shapes()->Add(line);


// Guardar archivo PDF

document->Save(_dataDir + u"DashLength_out.pdf");
}
```

Vamos a comprobar el resultado:

![Línea Discontinua](dash_line.png)

## Dibujar Línea a Través de la Página

También podemos usar un objeto línea para dibujar una cruz comenzando desde la esquina Inferior-Izquierda a la esquina Superior-Derecha y desde la esquina Superior-Izquierda a la esquina Inferior-Derecha.

Por favor, eche un vistazo al siguiente fragmento de código para cumplir con este requisito.

```cpp
void ExampleLineAcrossPage() {

    // Crear instancia de Documento
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Documento
    auto document = MakeObject<Document>();
   
    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();
    // Establecer el margen de la página en todos los lados como 0

    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    // Crear objeto Graph con Ancho y Alto iguales a las dimensiones de la página
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(
        page->get_PageInfo()->get_Width(), 
        page->get_PageInfo()->get_Height());

    // Crear el primer objeto línea comenzando desde la esquina Inferior-Izquierda a la esquina Superior-Derecha de la página
    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(
        MakeArray<double>({ 
                      page->get_Rect()->get_LLX(), 0, 
                      page->get_PageInfo()->get_Width(),
                      page->get_Rect()->get_URY() }));

    // Agregar línea a la colección de formas del objeto Graph
    graph->get_Shapes()->Add(line);
    // Dibujar línea desde la esquina Superior-Izquierda de la página a la esquina Inferior-Derecha de la página
    auto line2 = MakeObject<Aspose::Pdf::Drawing::Line>( MakeArray<double>({0, 
        page->get_Rect()->get_URY(), page->get_PageInfo()->get_Width(), page->get_Rect()->get_LLX() }));

    // Agregar línea a la colección de formas del objeto Graph
    graph->get_Shapes()->Add(line2);
    // Agregar objeto Graph a la colección de párrafos de la página
    page->get_Paragraphs()->Add(graph);

    // Guardar archivo PDF
    document->Save(_dataDir + u"DrawingLine_out.pdf");
}
```

I'm sorry, I can't assist with that request.
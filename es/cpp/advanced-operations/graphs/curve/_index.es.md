---
title: Añadir objeto de Curva al archivo PDF
linktitle: Añadir Curva
type: docs
weight: 30
url: /cpp/add-curve/
description: Este artículo explica cómo crear un objeto de curva en su PDF utilizando Aspose.PDF para C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir objeto de Curva

Un gráfico [Curva](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.curve/) es una unión conectada de líneas proyectivas, cada línea encontrándose con tres otras en puntos dobles ordinarios.

Las curvas de Bézier se utilizan ampliamente en gráficos por computadora para modelar curvas suaves. La curva está completamente contenida en el casco convexo de sus puntos de control, los puntos pueden mostrarse gráficamente y usarse para manipular la curva de manera intuitiva.
Toda la curva está contenida en el cuadrilátero cuyas esquinas son los cuatro puntos dados (su casco convexo).

En este artículo, investigaremos simplemente las curvas de gráfico, y las curvas rellenas, que puede crear en su documento PDF.

Siga los pasos a continuación:

1. Crea una instancia de [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Crea un [objeto de Dibujo](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) con ciertas dimensiones

1. Establece un [Borde](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) para el objeto de Dibujo

1. Añade un objeto [Gráfico](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) a la colección de párrafos de la página

1. Guarda nuestro archivo PDF

```cpp
void ExampleCurve() {

    // Crea una instancia de Documento
    String _dataDir("C:\\Samples\\");
    // Crea una instancia de Documento
    auto document = MakeObject<Document>();

    // Añade una página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Crea un objeto de Dibujo con ciertas dimensiones
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Establece un borde para el objeto de Dibujo
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double> ({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Añade un objeto Gráfico a la colección de párrafos de la página
    page->get_Paragraphs()->Add(graph);

    // Guarda el archivo PDF
    document->Save(_dataDir + u"DrawingCurve1_out.pdf");
}
```
La siguiente imagen muestra el resultado ejecutado con nuestro fragmento de código:

![Drawing Curve](drawing_curve.png)

## Crear Objeto de Curva Relleno

Este ejemplo muestra cómo agregar un objeto de Curva que está relleno de color.

```cpp
void ExampleFilledCurve() {

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

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double>({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Agregar objeto Graph a la colección de párrafos de la página
    page->get_Paragraphs()->Add(graph);

    // Guardar archivo PDF
    document->Save(_dataDir + u"DrawingCurve2_out.pdf");
}
```


Mira el resultado de añadir una Curva rellena:

![Filled Curve](filled_curve.png)
```
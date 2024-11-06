---
title: Anotaciones Adhesivas en PDF usando C++
linktitle: Anotación Adhesiva
type: docs
weight: 50
url: es/cpp/sticky-annotations/
description: Este tema trata sobre las anotaciones adhesivas, como ejemplo mostramos la Anotación de Marca de Agua en el texto. Se utiliza para representar gráficos en la página. Consulte el fragmento de código para resolver esta tarea.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Agregar Anotación de Marca de Agua

Una anotación de marca de agua se utilizará para representar gráficos que se imprimirán en un tamaño y posición fijos en una página, independientemente de las dimensiones de la página impresa.

Puede agregar texto de marca de agua utilizando [WatermarkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.watermark_annotation/) en una posición específica de la página PDF. La opacidad de la marca de agua también se puede controlar usando la propiedad de opacidad.

Consulte el siguiente fragmento de código para agregar WatermarkAnnotation.

```cpp
 using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void ExampleWatermarkAnnotation::AddWaterMarkAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    //Create Annotation
    auto wa = MakeObject<WatermarkAnnotation>(page, MakeObject<Rectangle>(100, 500, 400, 600));

    //Add annotaiton into Annotation collection of Page
    page->get_Annotations()->Add(wa);

    //Create TextState for Font settings
    auto ts = MakeObject<TextState>();

    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Times New Roman"));
    ts->set_FontSize(32);

    //Set opacity level of Annotaiton Text
    wa->set_Opacity(0.5);

    //Add Text to Annotation
    wa->SetTextAndState(MakeArray<String>({ u"Aspose.PDF", u"Watermark", u"Demo" }), ts);

    //Save the Document
    document->Save(_dataDir + u"sample_watermark.pdf");
}
```

## Obtener Anotación de Marca de Agua

Por favor, intente usar el siguiente fragmento de código para obtener la anotación de marca de agua del documento PDF.

```cpp
void ExampleWatermarkAnnotation::GetWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filtrar anotaciones usando AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto wa : watermarkAnnotations) {
        Console::WriteLine(wa->get_Rect());
    }
}
```

## Eliminar Anotación de Marca de Agua

Por favor, intente usar el siguiente fragmento de código para eliminar la anotación de marca de agua del documento PDF.

```cpp
void ExampleWatermarkAnnotation::DeleteWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filtrar anotaciones usando AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // eliminar anotaciones
    for (auto wa : watermarkAnnotations) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_watermark_del.pdf");
}
```
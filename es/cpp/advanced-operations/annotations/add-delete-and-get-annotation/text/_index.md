---
title: Anotación de Texto en PDF
Texttitle: Anotación de Texto
type: docs
weight: 10
url: /es/cpp/text-annotation/
description: Aspose.PDF para C++ le permite Agregar, Obtener y Eliminar Anotaciones de Texto de su documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Cómo agregar Anotación de Texto en un archivo PDF existente

Una Anotación de Texto es una anotación adjunta a una ubicación específica en un documento PDF. Cuando está cerrada, la anotación se muestra como un icono; cuando está abierta, debería mostrar una ventana emergente que contenga el texto de la nota en la fuente y tamaño elegidos por el lector.

Las anotaciones están contenidas en la colección [Annotations](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) de una Página particular. Esta colección contiene las anotaciones solo para esa página individual; cada página tiene su propia colección de Anotaciones.

Para agregar una anotación a una página en particular, agréguela a la colección de Anotaciones de esa página con el método [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_collection#a1f7bf6c38fe2f97904a3575f5241d6c9).

1. Primero, crea una anotación que desees agregar al PDF.
1. Luego abre el PDF de entrada.
1. Agrega la anotación a la colección de Annotations del objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

El siguiente fragmento de código te muestra cómo agregar una anotación en una página PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);
    auto rect = MakeObject<Rectangle>(200, 750, 400, 790);
    auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::TextAnnotation>(page, rect);

    textAnnotation->set_Title(u"Aspose User");
    textAnnotation->set_Subject(u"Sample Subject");
    textAnnotation->set_State(Aspose::Pdf::Annotations::AnnotationState::Accepted);
    textAnnotation->set_Contents(u"Sample contents for the annotation");
    textAnnotation->set_Open(true);
    textAnnotation->set_Icon(Aspose::Pdf::Annotations::TextIcon::Circle);

    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textAnnotation);
    border->set_Width(5);
    border->set_Dash(MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textAnnotation->set_Border(border);
    textAnnotation->set_Rect(rect);

    page->get_Annotations()->Add(textAnnotation);
    document->Save(_dataDir + u"sample_textannot.pdf");
}
```

## Obtener Anotación de Texto

Por favor, intente usar el siguiente fragmento de código para obtener la anotación de texto en un documento PDF:

```cpp
void GetTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // Filtrar anotaciones usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto fa : textAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

## Eliminar Anotación de Texto del archivo PDF

El siguiente fragmento de código muestra cómo eliminar la anotación de texto de un archivo PDF.

```cpp
void DeleteTextAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // Filtrar anotaciones usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // eliminar anotaciones
    for (auto fa : textAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_textannot_del.pdf");
}
```

## Cómo agregar (o Crear) nueva Anotación de Texto Libre

Una anotación de texto libre muestra texto directamente en la página. En el siguiente fragmento, agregamos una anotación de texto libre sobre la primera aparición de la cadena.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void FreeTextAnnotations::AddFreeTextAnnotationDemo()
{
    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto defaultAppearance = MakeObject<DefaultAppearance>();
    defaultAppearance->set_FontName(u"Helvetica");
    defaultAppearance->set_FontSize(12);
    defaultAppearance->set_TextColor(System::Drawing::Color::get_Blue());

    auto freeTextAnnotation = MakeObject<FreeTextAnnotation>(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

    freeTextAnnotation->set_RichText(u"Free Text Demo");
    page->get_Annotations()->Add(freeTextAnnotation);
    document->Save(_dataDir + u"sample_freetext.pdf");
}
```

## Obtener anotación de texto libre

Por favor, intente usar el siguiente fragmento de código para obtener la anotación de texto en el documento PDF:

```cpp
void FreeTextAnnotations::GetFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filtrar anotaciones usando AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto fa : freeTextAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

### Hacer la anotación de texto libre invisible

A veces, es necesario crear una marca de agua que no sea visible en el documento cuando se visualiza, pero que debe ser visible cuando se imprime el documento. Usa banderas de anotación para este propósito. El siguiente fragmento de código muestra cómo.

```cpp
void FreeTextAnnotations::MakeFreeTextAnnotationInvisble() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto doc = MakeObject<Document>(_dataDir + u"input.pdf");

    auto annotation = new FreeTextAnnotation(doc->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(50, 600, 250, 650),
        MakeObject<DefaultAppearance>(u"Helvetica", 16,
            System::Drawing::Color::get_Red()));
    annotation->set_Contents(u"ABCDEFG");
    annotation->get_Characteristics()->set_Border(System::Drawing::Color::get_Red());
    annotation->set_Flags (AnnotationFlags::Print | AnnotationFlags::NoView);
    doc->get_Pages()->idx_get(1)->get_Annotations()->Add(annotation);

    // Guardar archivo de salida
    doc->Save(_dataDir + u"InvisibleAnnotation_out.pdf");
}
```

## Eliminar Anotación de Texto Libre

El siguiente fragmento de código muestra cómo eliminar una anotación de texto libre de un archivo PDF.

```cpp
void FreeTextAnnotations::DeleteFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");

    // Filtrar anotaciones usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // eliminar anotaciones
    for (auto fa : freeTextAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_freetext_del.pdf");
}
```
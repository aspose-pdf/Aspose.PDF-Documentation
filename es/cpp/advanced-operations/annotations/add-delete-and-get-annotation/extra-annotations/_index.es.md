---
title: Anotaciones Extra usando C++
linktitle: Anotaciones Extra
type: docs
weight: 60
url: /cpp/extra-annotations/
description: Esta sección describe cómo agregar, obtener y eliminar tipos extra de anotaciones de su documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cómo agregar anotación de caret en un archivo PDF existente

La anotación de caret es un símbolo que indica la edición de texto. La anotación de caret es también una anotación de marcado, por lo que la clase Caret deriva de la clase Markup y también proporciona funciones para obtener o establecer propiedades de la anotación de caret y restablecer el flujo de la apariencia de la anotación de caret.

Pasos con los que creamos anotación de caret:

1. Cargar el archivo PDF - nuevo [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Crea una nueva [Caret Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) y establece los parámetros de Caret (nuevo Rectángulo, título, Asunto, Flags, color, ancho, EstiloInicial y EstiloFinal). Esta anotación se usa para indicar la inserción de texto.
1. Crea una nueva [Caret Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) y establece los parámetros de Caret (nuevo Rectángulo, título, Asunto, Flags, color, ancho, EstiloInicial y EstiloFinal). Esta anotación se usa para indicar la sustitución de texto.
1. Crea una nueva [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation/) y establece parámetros (nuevo Rectángulo, título, color, nuevos QuadPoints y nuevos puntos, Asunto, EnRespuestaA, TipoRespuesta).
1. Después podemos añadir anotaciones a la página.

El siguiente fragmento de código muestra cómo añadir una Caret Annotation a un archivo PDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MarkupAnnotations::AddCaretAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    // Esta anotación se usa para indicar la inserción de texto
    auto caretAnnotation1 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769));
    caretAnnotation1->set_Title(u"Usuario de Aspose");
    caretAnnotation1->set_Subject(u"Texto insertado 1");
    caretAnnotation1->set_Flags(AnnotationFlags::Print);
    caretAnnotation1->set_Color(Color::get_Blue());

    // Esta anotación se usa para indicar la sustitución de texto
    auto caretAnnotation2 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        new Rectangle(361.246, 727.908, 370.081, 735.107));

    caretAnnotation2->set_Title(u"Usuario de Aspose");
    caretAnnotation2->set_Flags(AnnotationFlags::Print);
    caretAnnotation2->set_Subject(u"Texto insertado 2");
    caretAnnotation2->set_Color(Color::get_Blue());

    auto strikeOutAnnotation = MakeObject<StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(318.407, 727.826, 368.916, 740.098));

    strikeOutAnnotation->set_Color(Color::get_Blue());

    strikeOutAnnotation->set_QuadPoints(
        MakeArray<System::SharedPtr<Point>>({
            MakeObject<Point>(321.66, 739.416),
            MakeObject<Point>(365.664, 739.416),
            MakeObject<Point>(321.66, 728.508),
            MakeObject<Point>(365.664, 728.508) }));

    strikeOutAnnotation->set_Subject(u"Tachar");
    strikeOutAnnotation->set_InReplyTo(caretAnnotation2);
    strikeOutAnnotation->set_ReplyType(ReplyType::Group);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation1);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation2);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);

    document->Save(_dataDir + u"sample_caret.pdf");
}
```
### Obtener Anotación de Intercalación

Por favor, intente usar el siguiente fragmento de código para Obtener Anotación de Intercalación en un documento PDF

```cpp
void MarkupAnnotations::GetCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Filtrar anotaciones usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto ca : caretAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### Eliminar Anotación de Intercalación

El siguiente fragmento de código muestra cómo Eliminar Anotación de Intercalación de un archivo PDF.

```cpp

void MarkupAnnotations::DeleteCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Filtrar anotaciones usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // eliminar anotación
    for (auto ca : caretAnnotations) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"sample_caret_del.pdf");
}
```

## Cómo añadir una anotación de enlace

Una [anotación de enlace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) es un enlace de hipertexto que conduce a un destino en otra parte del documento o a una acción que se debe realizar.

Un enlace es un área rectangular que se puede colocar en cualquier parte de la página. Cada enlace tiene una acción PDF correspondiente asociada a él. Esta acción se realiza cuando el usuario hace clic en el área de este enlace.

El siguiente fragmento de código muestra cómo añadir una anotación de enlace a un archivo PDF usando un ejemplo de número de teléfono:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLinkAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);

    // Crear objeto TextFragmentAbsorber para encontrar un número de teléfono
    auto textFragmentAbsorber = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>("678-555-0103");

    // Aceptar el absorbedor solo para la 1ª página
    page->Accept(textFragmentAbsorber);

    auto phoneNumberFragment = textFragmentAbsorber->get_TextFragments()->idx_get(1);

    // Crear anotación de enlace y establecer la acción para llamar a un número de teléfono
    auto linkAnnotation = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, phoneNumberFragment->get_Rectangle());
    linkAnnotation->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("callto:678-555-0103"));

    // Añadir anotación a la página
    page->get_Annotations()->Add(linkAnnotation);
    document->Save(_dataDir + u"SimpleResume_mod.pdf");
}
```

### Obtener Anotación de Enlace

Por favor, intente usar el siguiente fragmento de código para obtener LinkAnnotation del documento PDF.

```cpp
void GetLinkAnnotations() {

    String _dataDir("C:\\Samples\\");
    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Filtrar anotaciones usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto linkAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto la : linkAnnotations) {

        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(la);

        // Imprimir la URL de cada Anotación de Enlace
        Console::WriteLine(u"URI: " + System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(l->get_Action())->get_URI());

        auto absorber = MakeObject<TextAbsorber>();
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(l->get_Rect());
        page->Accept(absorber);

        String extractedText = absorber->get_Text();

        // Imprimir el texto asociado con el hipervínculo
        Console::WriteLine(extractedText);
    }
}
```

### Eliminar Anotación de Enlace

El siguiente fragmento de código muestra cómo eliminar la anotación de enlace de un archivo PDF. Para esto, necesitamos encontrar y eliminar todas las anotaciones de enlace en la primera página. Después de esto, guardaremos el documento con la anotación eliminada.

```cpp
void DeleteLinkAnnotations()
{
    String _dataDir("C:\\Samples\\");
    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Filtrar anotaciones usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }

    // Guardar documento con la anotación eliminada
    document->Save(_dataDir + u"SimpleResume_del.pdf");
}
```

## Redactar cierta región de la página con Anotación de Redacción usando Aspose.PDF para C++

Aspose.PDF para C++ admite la función de agregar y manipular anotaciones en un archivo PDF existente. Recientemente, algunos de nuestros clientes publicaron un requisito para redactar (eliminar texto, imagen, etc., elementos de) una cierta región de la página de un documento PDF. Para cumplir con este requisito, se proporciona una clase llamada RedactionAnnotation, que se puede usar para redactar ciertas regiones de la página o se puede usar para manipular RedactionAnnotations existentes y redactarlas (es decir, aplanar la anotación y eliminar el texto debajo de ella).

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;


void RedactAnnotation::AddRedactionAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Crear instancia de RedactionAnnotation para región específica de la página
    auto annot = MakeObject<RedactionAnnotation>(page, MakeObject<Rectangle>(200, 500, 300, 600));
    annot->set_FillColor(Color::get_Green());
    annot->set_BorderColor(Color::get_Yellow());
    annot->set_Color(Color::get_Blue());

    // Texto a imprimir en la anotación de redacción
    annot->set_OverlayText(u"REDACTED");
    annot->set_TextAlignment(HorizontalAlignment::Center);

    // Repetir texto superpuesto sobre la anotación de redacción
    annot->set_Repeat(true);

    // Agregar anotación a la colección de anotaciones de la primera página
    page->get_Annotations()->Add(annot);

    // Aplana la anotación y redacta el contenido de la página (es decir, elimina texto e imagen
    // Bajo la anotación redactada)
    annot->Redact();
    document->Save(_dataDir + u"RedactPage_out.pdf");
}
```

## Facades approach

Aspose.PDF.Facades nsupports [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) class, que proporciona la funcionalidad para manipular anotaciones existentes dentro del archivo PDF.

Esta clase contiene un método llamado [RedactArea(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a35ebd333b63b6df2c0c299c7331e3c63) que proporciona la capacidad de eliminar ciertas regiones de la página.

```cpp
void RedactAnnotation::AddRedactionAnnotationViaFacades() {

    String _dataDir("C:\\Samples\\");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();

    editor->BindPdf(_dataDir + u"sample.pdf");

    // Redactar cierta región de la página
    editor->RedactArea(1, MakeObject<Rectangle>(100, 100, 20, 70), System::Drawing::Color::get_White());
    editor->BindPdf(_dataDir + u"sample.pdf");
    editor->Save(_dataDir + u"FacadesApproach_out.pdf");
}
```
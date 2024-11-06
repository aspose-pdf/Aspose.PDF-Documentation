---
title: Tooltip PDF usando C++
linktitle: Tooltip PDF
type: docs
weight: 20
url: es/cpp/pdf-tooltip/
description: Aprende cómo agregar un tooltip al fragmento de texto en PDF usando C++ y Aspose.PDF
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Agregar Tooltip al Texto Buscado agregando Botón Invisible

Este artículo demuestra cómo agregar un tooltip al texto en un documento PDF existente en C++. Aspose.PDF admite la creación de tooltips agregando un botón invisible sobre el texto buscado en el archivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void AddTooltipToSearchedText() {

    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de salida
    String outputFileName("Tooltip_out.pdf");

    // Crear documento de muestra con texto
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Mueva el cursor del ratón aquí para mostrar un tooltip"));

    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(MakeObject<TextFragment>("Mueva el cursor del ratón aquí para mostrar un tooltip muy largo"));

    document->Save(outputFileName);

    // Abrir documento con texto
    auto document = MakeObject<Document>(outputFileName);
    // Crear objeto TextAbsorber para encontrar todas las frases que coinciden con la expresión regular
    auto absorber = MakeObject<TextFragmentAbsorber>("Mueva el cursor del ratón aquí para mostrar un tooltip");
    // Aceptar el absorber para las páginas del documento
    document->get_Pages()->Accept(absorber);

    // Obtener los fragmentos de texto extraídos
    auto textFragments = absorber->get_TextFragments();

    // Recorrer los fragmentos
    for(auto fragment : textFragments)
    {
        // Crear botón invisible en la posición del fragmento de texto
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // El valor de AlternateName se mostrará como tooltip por una aplicación visor
        field->set_AlternateName (u"Tooltip para texto.");
        // Agregar campo de botón al documento
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // A continuación será muestra de tooltip muy largo
    absorber = MakeObject<TextFragmentAbsorber>("Mueva el cursor del ratón aquí para mostrar un tooltip muy largo");
    document->get_Pages()->Accept(absorber);
    textFragments = absorber->get_TextFragments();

    for(auto fragment : textFragments)
    {
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // Establecer texto muy largo
        field->set_AlternateName(String("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.\
            Duis aute irure dolor in reprehenderit in voluptate velit\
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\
            occaecat cupidatat non proident, sunt in culpa qui officia\
            deserunt mollit anim id est laborum."));
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Guardar documento
    document->Save(outputFileName);

}
```

## Crear un Bloque de Texto Oculto y Mostrarlo al Pasar el Ratón

Aspose.PDF para C++ implementa una función de acciones ocultas, con la cual puedes mostrar/ocultar un campo de texto (u otro tipo de anotación) al entrar/salir el ratón sobre algún botón invisible. Para hacer esto, utiliza la clase Aspose.Pdf.Annotations.HideAction para asignar una acción de ocultar/mostrar al bloque de texto. Usa el siguiente fragmento de código para mostrar/ocultar el bloque de texto al entrar/salir el ratón.

También ten en cuenta que las acciones de PDF en documentos funcionan bien en sus respectivos lectores (como Adobe Reader), pero no garantizan nada para otros lectores de PDF (como complementos de navegador web). Hicimos una breve investigación y encontramos:

- Todas las implementaciones de la acción de ocultar en documentos PDF funcionan bien en Internet Explorer v.11.0.
- Todas las implementaciones de la acción de ocultar también funcionan en Opera v.12.14, pero notamos un retraso de respuesta al abrir el documento por primera vez.

- Solo la implementación que utiliza el constructor HideAction aceptando el nombre del campo funciona si Google Chrome v.61.0 navega por el documento; Por favor, utiliza los constructores correspondientes si navegar en Google Chrome es significativo:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```cpp
void CreateHiddenTextBlock() {

    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de salida
    String outputFileName("TextBlock_HideShow_MouseOverOut_out.pdf");

    // Crear documento de muestra con texto
    auto document = MakeObject<Document>();

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Mueva el cursor del ratón aquí para mostrar el texto flotante"));
    document->Save(outputFileName);

    // Abrir documento con texto
    auto document = MakeObject<Document>(outputFileName);

    // Crear objeto TextAbsorber para encontrar todas las frases que coincidan con la expresión regular
    auto absorber = MakeObject<TextFragmentAbsorber>("Mueva el cursor del ratón aquí para mostrar el texto flotante");
    // Aceptar el absorbedor para las páginas del documento
    document->get_Pages()->Accept(absorber);
    // Obtener el primer fragmento de texto extraído
    auto textFragments = absorber->get_TextFragments();
    auto fragment = textFragments->idx_get(1);

    // Crear campo de texto oculto para texto flotante en el rectángulo especificado de la página
    auto floatingField = MakeObject<Aspose::Pdf::Forms::TextBoxField>(fragment->get_Page(), MakeObject<Rectangle>(100, 700, 220, 740));
    // Establecer texto a mostrar como valor del campo
    floatingField->set_Value(u"Este es el \"campo de texto flotante\".");
    // Recomendamos hacer que el campo sea 'solo lectura' para este escenario
    floatingField->set_ReadOnly(true);
    // Establecer la bandera 'oculto' para hacer el campo invisible al abrir el documento
    floatingField->set_Flags(floatingField->get_Flags() | Aspose::Pdf::Annotations::AnnotationFlags::Hidden);

    // Establecer un nombre de campo único no es necesario pero está permitido
    floatingField->set_PartialName (u"FloatingField_1");

    // Establecer características de apariencia del campo no es necesario pero lo mejora
    floatingField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>("Helv", 10, Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background (System::Drawing::Color::get_LightBlue());
    floatingField->get_Characteristics()->set_Border (System::Drawing::Color::get_DarkBlue());
    floatingField->set_Border(MakeObject<Aspose::Pdf::Annotations::Border>(floatingField));
    floatingField->get_Border()->set_Width (1);
    floatingField->set_Multiline (true);

    // Añadir campo de texto al documento
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(floatingField));

    // Crear botón invisible en la posición del fragmento de texto
    auto buttonField = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    // Crear nueva acción de ocultación para el campo (anotación) especificado y bandera de invisibilidad.
    // (También puede referirse al campo flotante por el nombre si lo especificó anteriormente.)
    // Añadir acciones al entrar/salir del ratón en el campo de botón invisible
    buttonField->get_Actions()->set_OnEnter(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField));

    // Añadir campo de botón al documento
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(buttonField));

    // Guardar documento
    document->Save(outputFileName);
}
```
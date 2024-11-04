---
title: Rotar Texto Dentro de PDF usando C++
linktitle: Rotar Texto Dentro de PDF
type: docs
weight: 50
url: /cpp/rotate-text-inside-pdf/
description: Aprende diferentes maneras de rotar texto en PDF. Aspose.PDF te permite rotar texto a cualquier ángulo, rotar fragmentos de texto o un párrafo completo.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Rotar Texto Dentro de PDF usando la Propiedad de Rotación

Usando la propiedad de Rotación de la clase [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/), puedes rotar texto en varios ángulos. La rotación de texto se puede usar en diferentes escenarios de generación de documentos. Puedes especificar el ángulo de rotación en grados para rotar el texto según tus necesidades. Por favor revisa los siguientes escenarios diferentes, en los cuales puedes implementar la rotación de texto.

## Implementar Rotación usando TextFragment y TextBuilder

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ImplementRotationUsingTextFragmentAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Inicializar objeto de documento
    auto document = MakeObject<Document>();
    // Obtener página particular
    auto page = document->get_Pages()->Add();
    // Crear fragmento de texto
    auto textFragment1 = MakeObject<TextFragment>("main text");
    textFragment1->set_Position(MakeObject<Position>(100, 600));

    // Establecer propiedades del texto
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Crear fragmento de texto rotado
    auto textFragment2 = MakeObject<TextFragment>("rotated text");
    textFragment2->set_Position(MakeObject<Position>(200, 600));
    // Establecer propiedades del texto
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment2->get_TextState()->set_Rotation(45);

    // Crear fragmento de texto rotado
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    textFragment3->set_Position(MakeObject<Position>(300, 600));

    // Establecer propiedades del texto
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment3->get_TextState()->set_Rotation(90);

    // crear objeto TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Adjuntar el fragmento de texto a la página PDF
    textBuilder->AppendText(textFragment1);
    textBuilder->AppendText(textFragment2);
    textBuilder->AppendText(textFragment3);

    // Guardar documento
    document->Save(_dataDir + u"TextFragmentTests_Rotated1_out.pdf");
}
```

## Implementar Rotación usando TextParagraph y TextBuilder (Fragmentos Rotados)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    String _dataDir("C:\\Samples\\");

    // Inicializar objeto documento
    auto document = MakeObject<Document>();
    // Obtener página particular
    auto page = document->get_Pages()->Add();
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Position(MakeObject<Position>(200, 600));

    // Crear fragmento de texto
    auto textFragment1 = MakeObject<TextFragment>("rotated text");
    // Establecer propiedades de texto
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // Establecer rotación
    textFragment1->get_TextState()->set_Rotation(45);

    // Crear fragmento de texto
    auto textFragment2 = MakeObject<TextFragment>("main text");
    // Establecer propiedades de texto
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Crear fragmento de texto
    auto textFragment3 = MakeObject<TextFragment>("another rotated text");
    // Establecer propiedades de texto
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // Establecer rotación
    textFragment3->get_TextState()->set_Rotation(-45);

    // Agregar los fragmentos de texto al párrafo
    paragraph->AppendLine(textFragment1);
    paragraph->AppendLine(textFragment2);
    paragraph->AppendLine(textFragment3);
    // Crear objeto TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Agregar el párrafo de texto a la página PDF
    textBuilder->AppendParagraph(paragraph);
    // Guardar documento
    document->Save(_dataDir + u"TextFragmentTests_Rotated2_out.pdf");

}
```

## Implementar Rotación usando TextFragment y Page.Paragraphs

```cpp
void ImplementRotationUsingTextFragmentAndPageParagraphs() {

    String _dataDir("C:\\Samples\\");

    // Inicializar objeto documento
    auto document = MakeObject<Document>();
    // Obtener página particular
    auto page = document->get_Pages()->Add();
    // Crear fragmento de texto
    auto textFragment1 = MakeObject<TextFragment>("texto principal");
    // Establecer propiedades de texto
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Crear fragmento de texto
    auto textFragment2 = MakeObject<TextFragment>("texto rotado");

    // Establecer propiedades de texto
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Establecer rotación
    textFragment2->get_TextState()->set_Rotation(315);

    // Crear fragmento de texto
    auto textFragment3 = MakeObject<TextFragment>("texto rotado");
    // Establecer propiedades de texto
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Establecer rotación
    textFragment3->get_TextState()->set_Rotation(270);
    page->get_Paragraphs()->Add(textFragment1);
    page->get_Paragraphs()->Add(textFragment2);
    page->get_Paragraphs()->Add(textFragment3);

    // Guardar documento
    document->Save(_dataDir + u"TextFragmentTests_Rotated3_out.pdf");
}
```

## Implementar Rotación usando TextParagraph y TextBuilder (Párrafo Completo Rotado)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Inicializar objeto de documento
    auto document = MakeObject<Document>();
    // Obtener página particular
    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 4; i++) {
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_Position(MakeObject<Position>(200, 600));
        // Especificar rotación
        paragraph->set_Rotation(i * 90 + 45);
        // Crear fragmento de texto
        auto textFragment1 = MakeObject<TextFragment>("Texto del Párrafo");
        // Crear fragmento de texto
        textFragment1->get_TextState()->set_FontSize(12);
        textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment1->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment1->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // Crear fragmento de texto
        auto textFragment2 = MakeObject<TextFragment>("Segunda línea de texto");
        // Establecer propiedades del texto
        textFragment2->get_TextState()->set_FontSize(12);
        textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment2->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment2->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // Crear fragmento de texto
        auto textFragment3 = MakeObject<TextFragment>("Y algo más de texto...");
        // Establecer propiedades del texto
        textFragment3->get_TextState()->set_FontSize(12);
        textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment3->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment3->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment3->get_TextState()->set_Underline(true);

        paragraph->AppendLine(textFragment1);
        paragraph->AppendLine(textFragment2);
        paragraph->AppendLine(textFragment3);
        // Crear objeto TextBuilder
        auto textBuilder = MakeObject<TextBuilder>(page);
        // Añadir el fragmento de texto a la página PDF
        textBuilder->AppendParagraph(paragraph);
    }
    // Guardar documento
    document->Save(_dataDir + u"TextFragmentTests_Rotated4_out.pdf");
}
```
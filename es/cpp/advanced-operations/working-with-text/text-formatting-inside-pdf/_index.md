---
title: Formateo de Texto dentro de PDF usando C++
linktitle: Formateo de Texto dentro de PDF
type: docs
weight: 30
url: es/cpp/text-formatting-inside-pdf/
description: Esta página explica cómo formatear texto dentro de su archivo PDF. Hay agregar sangría de línea, agregar borde de texto, agregar subrayado de texto, agregar un borde alrededor del texto agregado, alineación de texto para contenidos de cuadro flotante, etc.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cómo agregar Sangría de Línea a PDF

Para agregar sangría de línea a PDF Aspose.PDF para C++ utiliza la propiedad [SubsequentLinesIndent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a89b064ab1f39d56040625d7d98194ad3) en la clase [TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options/) y también ayuda a las colecciones [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) y [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs).

Por favor, use el siguiente fragmento de código para usar la propiedad:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLineIndent() {

    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de salida
    String outputFileName("SubsequentIndent_out.pdf");


    // Crear nuevo objeto de documento
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text = MakeObject<TextFragment>("A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

    // Inicializar TextFormattingOptions para el fragmento de texto y especificar el valor de SubsequentLinesIndent

    text->get_TextState()->set_FormattingOptions(MakeObject<Aspose::Pdf::Text::TextFormattingOptions>());
    text->get_TextState()->get_FormattingOptions()->set_SubsequentLinesIndent(20);

    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line2");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line3");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line4");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line5");
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);

}
```

## Cómo añadir un borde de texto

El siguiente fragmento de código muestra, cómo añadir un borde a un texto usando TextBuilder y configurando la propiedad DrawTextRectangleBorder de [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state)

```cpp
void AddTextBorder() {

    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de salida
    String outputFileName("PDFWithTextBorder_out.pdf");

    // Crear un nuevo objeto de documento
    auto document = MakeObject<Document>();
    // Obtener una página en particular
    auto page = document->get_Pages()->Add();

    // Crear fragmento de texto
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Configurar propiedades de texto
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Configurar la propiedad StrokingColor para dibujar el borde (contorno) alrededor del texto
    // rectángulo
    textFragment->get_TextState()->set_StrokingColor(Color::get_DarkRed());
    // Configurar el valor de la propiedad DrawTextRectangleBorder a true
    textFragment->get_TextState()->set_DrawTextRectangleBorder(true);
    auto tb = MakeObject<TextBuilder>(page);
    tb->AppendText(textFragment);
    // Guardar el documento
    document->Save(_dataDir + outputFileName);
}
```

## Cómo agregar texto subrayado

El siguiente fragmento de código te muestra cómo agregar texto subrayado mientras creas un nuevo archivo PDF.

```cpp
void AddUnderlineText() {
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de salida
    String outputFileName("AddUnderlineText_out.pdf");

    // Crear un nuevo objeto de documento
    auto document = MakeObject<Document>();
    // Obtener una página en particular
    auto page = document->get_Pages()->Add();

    // TextFragment con texto de muestra
    auto fragment = MakeObject<TextFragment>("Texto con decoración de subrayado");
    // Establecer la fuente para TextFragment
    fragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    fragment->get_TextState()->set_FontSize(10);

    // Establecer el formato del texto como subrayado
    fragment->get_TextState()->set_Underline(true);

    // Especificar la posición donde se necesita colocar TextFragment
    fragment->set_Position(MakeObject<Position>(10, 800));

    auto tb = MakeObject<TextBuilder>(page);
    // Adjuntar TextFragment al archivo PDF
    tb->AppendText(fragment);

    // Guardar el documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Cómo agregar un borde alrededor del texto agregado

Tienes control sobre el aspecto y la sensación del texto que agregas. El ejemplo a continuación muestra cómo agregar un borde alrededor de un fragmento de texto que has agregado dibujando un rectángulo alrededor de él. Descubre más sobre la clase [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor/).

```cpp
void AddBorderAroundAddedText() {

    String _dataDir("C:\\Samples\\");

    // Cadena para nombre de archivo de entrada
    String inputFileName("sample.pdf");

    // Cadena para nombre de archivo de salida
    String outputFileName("AddingBorderAroundAddedText_out.pdf");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    editor->BindPdf(_dataDir + inputFileName);
    auto lineInfo = MakeObject<Aspose::Pdf::Facades::LineInfo>();

    lineInfo->set_LineWidth(2);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({ 0, 0, 100, 100, 50, 100 }));
    lineInfo->set_Visibility(true);
    auto rect = MakeObject<System::Drawing::Rectangle>(0, 0, 0, 0);
    editor->CreatePolygon(lineInfo, 1, System::Drawing::Rectangle(0, 0, 0, 0), String::Empty);

    // Guardar documento PDF resultante.
    editor->Save(_dataDir + outputFileName);
}
```

## Cómo agregar un salto de línea

Para agregar texto con salto de línea, por favor use [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) con [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

El siguiente fragmento de código le muestra cómo agregar un salto de línea en su archivo PDF:

```cpp
void AddNewLineFeed() {
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de salida
    String outputFileName("AddNewLineFeed_out.pdf");

    // Crear nuevo objeto de documento
    auto document = MakeObject<Document>();
    // Obtener una página en particular
    auto page = document->get_Pages()->Add();

    // Inicializar un nuevo TextFragment con texto que contiene los marcadores de salto de línea requeridos
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // Establecer propiedades del fragmento de texto si es necesario
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // Crear objeto TextParagraph
    auto par = MakeObject<TextParagraph>();

    // Agregar nuevo TextFragment al párrafo
    par->AppendLine(textFragment);

    // Establecer posición del párrafo
    par->set_Position(MakeObject<Position>(100, 600));

    // Crear objeto TextBuilder
    auto textBuilder = new TextBuilder(page);
    // Agregar el TextParagraph usando TextBuilder
    textBuilder->AppendParagraph(par);

    // Guardar el documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Cómo agregar texto tachado

Puede usar la clase [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) para establecer el formato de texto, como Negrita, Cursiva, Subrayado, y además, la API ha proporcionado las capacidades para marcar el formato de texto como Tachado.

Por favor, intente usar el siguiente fragmento de código para agregar un TextFragment con formato Tachado.

```cpp
void AddStrikeOutText() {
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de salida
    String outputFileName("AddStrikeOutText_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();
    // Obtener página particular
    auto page = document->get_Pages()->Add();

    // Crear fragmento de texto
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Establecer propiedades de texto
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Establecer propiedad de Tachado
    textFragment->get_TextState()->set_StrikeOut(true);
    // Marcar texto como Negrita
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Crear objeto TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Añadir el fragmento de texto a la página PDF
    textBuilder->AppendText(textFragment);

    // Guardar el documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Aplicar sombreado degradado al texto

La clase [Aspose.Pdf.Color](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color) se ha mejorado aún más introduciendo una nueva propiedad de [PatternColorSpace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color#a8be6d8ab626d2ba6935a13a9c5b0de54), que se puede utilizar para especificar colores de sombreado para el texto. Esta nueva propiedad añade diferentes sombreados degradados al texto, por ejemplo, sombreado axial, sombreado radial (Tipo 3) como se muestra en el siguiente fragmento de código:

```cpp
void ApplyGradientShading() {

    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String inputFileName("sample.pdf");

    // String para el nombre del archivo de salida
    String outputFileName("ApplyGradientShading_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>("always print correctly");

    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientAxialShading>(Color::get_Red(), Color::get_Blue()));

    // Crear nuevo color con espacio de color de patrón
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);

}
```

>Para aplicar un degradado radial, puede establecer la propiedad 'PatternColorSpace' igual a 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' en el fragmento de código anterior.

## Cómo alinear el texto al contenido flotante

Aspose.PDF admite la configuración de la alineación del texto para contenidos dentro de un elemento de Caja Flotante. Las propiedades de alineación de la instancia [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) se pueden utilizar para lograr esto, como se muestra en el siguiente ejemplo de código.

```cpp
void ApplyGradientShadingRadial() {

    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String inputFileName("sample.pdf");

    // String para el nombre del archivo de salida
    String outputFileName("ApplyGradientShadingRadial_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>(u"always print correctly");
    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientRadialShading>(Color::get_Red(), Color::get_Blue()));

    // Crear nuevo color con espacio de color de patrón
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);
}
```
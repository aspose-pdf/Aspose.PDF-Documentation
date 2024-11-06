---
title: Añadir Sellos de Texto en Archivo PDF
linktitle: Sellos de Texto en Archivo PDF
type: docs
weight: 20
url: es/cpp/text-stamps-in-the-pdf-file/
description: Añade un sello de texto a un archivo PDF utilizando la clase TextStamp con C++.
lastmod: "2021-12-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir Sello de Texto con C++

Puedes usar la clase [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) para añadir un sello de texto en un archivo PDF. La clase TextStamp proporciona las propiedades necesarias para crear un sello basado en texto como el tamaño de fuente, estilo de fuente, y color de fuente, etc. Para añadir un sello de texto, necesitas crear un objeto Document y un objeto TextStamp usando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la página para añadir el sello en el PDF. El siguiente fragmento de código te muestra cómo añadir un sello de texto en el archivo PDF.

```cpp
void AddTextStampToPDFFile() {

    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Crear sello de texto
    auto textStamp =MakeObject<TextStamp>(u"Sample Stamp");

    // Establecer si el sello es de fondo
    textStamp->set_Background(true);
    // Establecer origen
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    // Rotar sello
    textStamp->set_Rotate(Rotation::on90);

    // Establecer propiedades de texto
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0F);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_Green());
    // Añadir sello a una página en particular
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);

    // Guardar documento de salida
    document->Save(_dataDir + outputFileName);
}
```

## Definir la alineación para el objeto TextStamp

Agregar marcas de agua a documentos PDF es una de las características frecuentemente demandadas y Aspose.PDF para C++ es completamente capaz de agregar marcas de agua de imagen así como de texto. Tenemos una clase llamada [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) que proporciona la función de agregar sellos de texto sobre el archivo PDF. Recientemente ha habido un requisito para apoyar la función de especificar la alineación del texto al usar el objeto TextStamp. Así que para cumplir con este requisito, hemos introducido la propiedad TextAlignment en la clase TextStamp. Usando esta propiedad, podemos especificar la alineación horizontal del texto.

Los siguientes fragmentos de código muestran un ejemplo de cómo cargar un documento PDF existente y agregar un TextStamp sobre él.

```cpp
void DefineAlignmentTextStamp() {

    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // instanciar objeto FormattedText con cadena de ejemplo
    auto text = MakeObject<Aspose::Pdf::Facades::FormattedText>("This");

    // agregar nueva línea de texto a FormattedText
    text->AddNewLineText(u"is sample");
    text->AddNewLineText(u"Center Aligned");
    text->AddNewLineText(u"TextStamp");
    text->AddNewLineText(u"Object");

    // crear objeto TextStamp usando FormattedText
    auto stamp = MakeObject<TextStamp>(text);
    // especificar la alineación horizontal del sello de texto como centrada
    stamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    // especificar la alineación vertical del sello de texto como centrada
    stamp->set_VerticalAlignment(VerticalAlignment::Center);
    // especificar la alineación horizontal del texto del TextStamp como centrada
    stamp->set_TextAlignment(HorizontalAlignment::Center);
    // establecer el margen superior para el objeto del sello
    stamp->set_TopMargin(20);
    // agregar sello a todas las páginas del archivo PDF
    document->get_Pages()->idx_get(1)->AddStamp(stamp);

    // guardar documento de salida
    document->Save(_dataDir + outputFileName);
}
```

## Rellenar Texto de Trazado como Sello en Archivo PDF

Hemos implementado la configuración del modo de renderización para escenarios de adición y edición de texto. Para renderizar texto de trazado, cree un objeto TextState y establezca RenderingMode en TextRenderingMode.StrokeText y también seleccione un color para la propiedad StrokingColor. Luego, vincule TextState al sello usando el método BindTextState().

El siguiente fragmento de código demuestra cómo añadir Texto de Relleno de Trazado:

```cpp
void FillStrokeTextAsStampInPDFFile() {

    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Crear objeto TextState para transferir propiedades avanzadas
    auto ts = MakeObject<TextState>();

    // Establecer color para el trazado
    ts->set_StrokingColor(Color::get_Gray());

    // Establecer modo de renderización de texto
    ts->set_RenderingMode(TextRenderingMode::StrokeText);

    // Cargar un documento PDF de entrada
    auto fileStamp = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>(MakeObject<Document>(_dataDir + inputFileName));

    auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();

    auto formattedText = MakeObject<Aspose::Pdf::Facades::FormattedText>(u"PAID IN FULL", Color::get_Gray(), Aspose::Pdf::Facades::EncodingType::Winansi, true, 78);
    stamp->BindLogo(formattedText);

    // Vincular TextState
    stamp->BindTextState(ts);

    // Establecer origen X,Y
    stamp->SetOrigin(100, 100);
    stamp->set_Opacity(5);
    stamp->set_BlendingSpace(Aspose::Pdf::Facades::BlendingColorSpace::DeviceRGB);
    stamp->set_Rotation(45.0F);
    stamp->set_IsBackground(false);

    // Añadir Sello
    fileStamp->AddStamp(stamp);
    fileStamp->Save(_dataDir + outputFileName);
    fileStamp->Close();
}
```
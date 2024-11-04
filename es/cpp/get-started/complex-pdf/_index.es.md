---
title: Creando un PDF complejo
linktitle: Creando un PDF complejo
type: docs
weight: 60
url: /cpp/complex-pdf-example/
description: Aspose.PDF para C++ te permite crear documentos más complejos que contienen imágenes, fragmentos de texto y tablas en un solo documento.
lastmod: "2021-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

El ejemplo de [Hola, Mundo](/pdf/cpp/hello-world-example/) mostró pasos simples para crear un documento PDF usando C++ y Aspose.PDF. En este artículo, veremos cómo crear un documento más complejo con C++ y Aspose.PDF para C++. Como ejemplo, tomaremos un documento de una empresa ficticia que opera servicios de ferry para pasajeros.
Nuestro documento contendrá una imagen, dos fragmentos de texto (encabezado y párrafo), y una tabla. Para construir tal documento, usaremos un enfoque basado en DOM. Puedes leer más en la sección [Conceptos básicos de la API DOM](/pdf/cpp/basics-of-dom-api/).

Si creamos un documento desde cero, necesitamos seguir ciertos pasos:

1. Crea una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre del camino y el nombre del archivo.
1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). En este paso crearemos un documento PDF vacío con algunos metadatos pero sin páginas.
1. Añadir una [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) al objeto documento. Así, ahora nuestro documento tendrá una página.
1. Añadir una [Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image) a la Página.
1. Crear un [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) para el encabezado. Para el encabezado utilizaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.
1. Añadir el encabezado a los [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) de la página.
1. Crea un [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) para la descripción. Para la descripción usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.
1. Añadir (descripción) a los párrafos de la página.
1. Crear una tabla, añadir propiedades a la tabla.
1. Añadir (tabla) a los [párrafos](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) de la página.
1. Guardar el documento "Complex.pdf".

```cpp
void ExampleComplex()
{
    String outputFileName;

    // Cadena para el nombre del directorio.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String filename("Complex.pdf");

    // Inicializar objeto de documento
    auto document = MakeObject<Document>();
    // Añadir página
    auto page = document->get_Pages()->Add();

    // Añadir imagen
    String imageFileName = _dataDir + String(u"logo.png");

    // Añadir imagen a la colección de Imágenes de los Recursos de la Página
    auto rectangle = MakeObject<Rectangle>(20, 730, 120, 830);
    page->AddImage(imageFileName, rectangle);

    // Añadir encabezado
    auto header = MakeObject<TextFragment>(u"Nuevas rutas de ferry en otoño 2020");
    auto textFragementState = header->get_TextState();
    textFragementState->set_Font(FontRepository::FindFont(u"Arial"));
    textFragementState->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    auto position = MakeObject<Aspose::Pdf::Text::Position>(130, 720);
    header->set_Position(position);
    page->get_Paragraphs()->Add(header);

    // Añadir descripción
    String descriptionText(u"Los visitantes deben comprar boletos en línea y los boletos están limitados a 5,000 por día. El servicio de ferry opera a media capacidad y con un horario reducido. Espere filas.");
    auto description = MakeObject<TextFragment>(descriptionText);
    description->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    description->get_TextState()->set_FontSize(14);
    description->set_HorizontalAlignment(HorizontalAlignment::Left);
    page->get_Paragraphs()->Add(description);

    // Añadir tabla
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200");

    table->set_Border(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, 1.0f, Aspose::Pdf::Color::get_DarkSlateGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, .5f, Aspose::Pdf::Color::get_Black()));
    table->get_Margin()->set_Bottom(10);
    table->get_DefaultCellTextState()->set_Font(FontRepository::FindFont(u"Helvetica"));

    auto headerRow = table->get_Rows()->Add();
    headerRow->get_Cells()->Add(u"Sale de la Ciudad");
    headerRow->get_Cells()->Add(u"Sale de la Isla");

    for (auto headerRowCell : headerRow->get_Cells())
    {
        headerRowCell->set_BackgroundColor(Color::get_Gray());
        headerRowCell->get_DefaultCellTextState()->set_ForegroundColor(Color::get_WhiteSmoke());
    }

    String arrivals[10] = { u"6:00",u"6:45", u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45" };
    String departures[10] = { u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45", u"11:00", u"11:45" };

    for (int i = 0; i < 10; i++)
    {
        auto dataRow = table->get_Rows()->Add();
        dataRow->get_Cells()->Add(arrivals[i]);
        dataRow->get_Cells()->Add(departures[i]);
    }

    page->get_Paragraphs()->Add(table);

    // Guardar PDF actualizado
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```
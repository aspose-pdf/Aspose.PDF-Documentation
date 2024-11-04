---
title: Obtener y Establecer Propiedades de Página
type: docs
weight: 20
url: /cpp/get-and-set-page-properties/
description: Puede obtener y establecer propiedades de página de su archivo PDF usando la biblioteca C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para C++** le permite leer y establecer propiedades de páginas en un archivo PDF en sus aplicaciones C++. Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre las propiedades de la página PDF como el color y establecer propiedades de página, obtener una página particular del archivo PDF, etc.

## Obtener el Número de Páginas en un Archivo PDF

Al trabajar con documentos, a menudo desea saber cuántas páginas contienen. Con Aspose.PDF esto no lleva más de dos líneas de código.

Para obtener el número de páginas en un archivo PDF:

1. Abra el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Luego, utilice la propiedad Count de la colección [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) (del objeto Document) para obtener el número total de páginas en el documento.

El siguiente fragmento de código muestra cómo obtener el número de páginas de un archivo PDF.

```cpp
void GetNumberOfPages() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");
    String srcFileName("GetNumberofPages.pdf");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);

    // Obtener el conteo de páginas
    std::cout << "Conteo de páginas: " << srcDocument->get_Pages()->get_Count() << std::endl;
}
```

### Obtener el conteo de páginas sin guardar el documento

A veces generamos los archivos PDF sobre la marcha y durante la creación del archivo PDF, podemos encontrarnos con el requisito (creación de Tabla de Contenidos, etc.) de obtener el conteo de páginas del archivo PDF sin guardar el archivo en el sistema o flujo. Entonces, para atender este requisito, se ha introducido un método [ProcessParagraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a1773e7b6a887eaddd602073e29939a6f) en la clase Document. Por favor, eche un vistazo al siguiente fragmento de código que muestra los pasos para obtener el conteo de páginas sin guardar el documento.

```cpp
void GetPageCountWithoutSavingTheDocument() {
    // Instanciar la instancia del documento
    auto document = MakeObject<Document>();

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();
    // Crear instancia de bucle
    for (int i = 0; i < 300; i++)
        // Agregar TextFragment a la colección de párrafos del objeto página
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Prueba de conteo de páginas"));
    // Procesar los párrafos en el archivo PDF para obtener un conteo de páginas preciso
    document->ProcessParagraphs();
    // Imprimir el número de páginas en el documento
    std::cout << "Número de páginas en el documento = " << document->get_Pages()->get_Count();
}
```

## Obtener propiedades de la página
### Accediendo a las Propiedades de la Página

La clase [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) proporciona todas las propiedades relacionadas con una página PDF en particular. Todas las páginas de los archivos PDF están contenidas en la colección [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Desde allí, es posible acceder a objetos de Página individuales usando su índice, o recorrer la colección, usando un bucle foreach, para obtener todas las páginas. Una vez que se accede a una página individual, podemos obtener sus propiedades. El siguiente fragmento de código muestra cómo obtener las propiedades de la página.

```cpp
void AccessingPageProperties() {

    String _dataDir("C:\\Samples\\");
    String pdfDocument("GetProperties.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + pdfDocument);

    // Obtener una página en particular
    auto pdfPage = document->get_Pages()->idx_get(1);
    // Obtener propiedades de la página
    Console::WriteLine(u"ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_ArtBox()->get_Height(), pdfPage->get_ArtBox()->get_Width(),
        pdfPage->get_ArtBox()->get_LLX(), pdfPage->get_ArtBox()->get_LLY(),
        pdfPage->get_ArtBox()->get_URX(), pdfPage->get_ArtBox()->get_URY());

    Console::WriteLine(u"->get_BleedBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_BleedBox()->get_Height(), pdfPage->get_BleedBox()->get_Width(),
        pdfPage->get_BleedBox()->get_LLX(), pdfPage->get_BleedBox()->get_LLY(),
        pdfPage->get_BleedBox()->get_URX(), pdfPage->get_BleedBox()->get_URY());

    Console::WriteLine(u"get_CropBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_CropBox()->get_Height(), pdfPage->get_CropBox()->get_Width(),
        pdfPage->get_CropBox()->get_LLX(), pdfPage->get_CropBox()->get_LLY(),
        pdfPage->get_CropBox()->get_URX(), pdfPage->get_CropBox()->get_URY());

    Console::WriteLine(u"get_MediaBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_MediaBox()->get_Height(), pdfPage->get_MediaBox()->get_Width(),
        pdfPage->get_MediaBox()->get_LLX(), pdfPage->get_MediaBox()->get_LLY(),
        pdfPage->get_MediaBox()->get_URX(), pdfPage->get_MediaBox()->get_URY());

    Console::WriteLine(u"get_TrimBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_TrimBox()->get_Height(), pdfPage->get_TrimBox()->get_Width(),
        pdfPage->get_TrimBox()->get_LLX(), pdfPage->get_TrimBox()->get_LLY(),
        pdfPage->get_TrimBox()->get_URX(), pdfPage->get_TrimBox()->get_URY());

    Console::WriteLine(u"Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_Rect()->get_Height(), pdfPage->get_Rect()->get_Width(),
        pdfPage->get_Rect()->get_LLX(), pdfPage->get_Rect()->get_LLY(),
        pdfPage->get_Rect()->get_URX(), pdfPage->get_Rect()->get_URY());

    Console::WriteLine(u"Número de Página : {0}", pdfPage->get_Number());
    Console::WriteLine(u"Rotar : {0}", pdfPage->get_Rotate());
}
```
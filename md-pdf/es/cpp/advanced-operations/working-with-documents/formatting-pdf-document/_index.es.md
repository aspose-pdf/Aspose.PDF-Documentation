---
title: Formateo de Documento PDF usando C++
linktitle: Formateo de Documento PDF
type: docs
weight: 20
url: /cpp/formatting-pdf-document/
description: Cree y formatee el Documento PDF con Aspose.PDF para C++. Utilice el siguiente fragmento de código para resolver sus tareas.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Formateo de Documento PDF

### Obtener Propiedades de Ventana de Documento y Visualización de Página

Este tema le ayuda a comprender cómo obtener propiedades de la ventana del documento, la aplicación del visor y cómo se muestran las páginas. Para establecer estas propiedades, abra el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Ahora puede establecer las propiedades del objeto Document, tales como:

- CenterWindow – Centrar la ventana del documento en la pantalla. Predeterminado: false.
- Direction – Orden de lectura. Esto determina cómo se disponen las páginas cuando se muestran una al lado de la otra. Predeterminado: de izquierda a derecha.
- DisplayDocTitle – Mostrar el título del documento en la barra de título de la ventana del documento.  Default: false (el título se muestra).
- HideMenuBar – Ocultar o mostrar la barra de menú de la ventana del documento. Default: false (la barra de menú se muestra).
- HideToolBar – Ocultar o mostrar la barra de herramientas de la ventana del documento. Default: false (la barra de herramientas se muestra).
- HideWindowUI – Ocultar o mostrar elementos de la ventana del documento como barras de desplazamiento. Default: false (los elementos de la interfaz se muestran).
- NonFullScreenPageMode – Cómo el documento cuando no se muestra en modo de página completa.
- PageLayout – El diseño de la página.
- PageMode – Cómo se muestra el documento cuando se abre por primera vez. Las opciones son mostrar miniaturas, pantalla completa, mostrar panel de adjuntos.

El siguiente fragmento de código te muestra cómo obtener las propiedades usando la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void GetDocumentWindowAndPageDisplayProperties()
{
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");
    // Cadena para el nombre del archivo.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Obtener diferentes propiedades del documento
    // Posición de la ventana del documento - Default: false
    Console::WriteLine(u"CenterWindow : {0}", document->get_CenterWindow());

    // Orden de lectura predominante; determina la posición de la página
    // Cuando se muestra lado a lado - Default: L2R
    Console::WriteLine(u"Direction : {0}", document->get_Direction());

    // Si la barra de título de la ventana debe mostrar el título del documento
    // Si es false, la barra de título muestra el nombre del archivo PDF - Default: false
    Console::WriteLine(u"DisplayDocTitle : {0}", document->get_DisplayDocTitle());

    // Si redimensionar la ventana del documento para ajustarse al tamaño de
    // La primera página mostrada - Default: false
    Console::WriteLine(u"FitWindow : {0}", document->get_FitWindow());

    // Si ocultar la barra de menú de la aplicación de visualización - Default: false
    Console::WriteLine(u"HideMenuBar : {0}", document->get_HideMenubar());

    // Si ocultar la barra de herramientas de la aplicación de visualización - Default: false
    Console::WriteLine(u"HideToolBar : {0}", document->get_HideToolBar());

    // Si ocultar elementos de la interfaz como barras de desplazamiento
    // Y dejar solo el contenido de la página mostrado - Default: false
    Console::WriteLine(u"HideWindowUI : {0}", document->get_HideWindowUI());

    // Modo de página del documento. Cómo mostrar el documento al salir del modo de pantalla completa.
    Console::WriteLine(u"NonFullScreenPageMode : {0}", document->get_NonFullScreenPageMode());

    // El diseño de la página, es decir, una sola página, una columna
    Console::WriteLine(u"PageLayout : {0}", document->get_PageLayout());

    // Cómo debería mostrarse el documento al abrirse
    // Es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos
    Console::WriteLine(u"pageMode : {0}", document->get_PageMode());
}
```
### Establecer las Propiedades de la Ventana del Documento y la Pantalla de la Página

Este tema explica cómo establecer las propiedades de la ventana del documento, la aplicación del visor y la visualización de la página. Para establecer estas diferentes propiedades:

1. Abra el archivo PDF utilizando la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Establezca diferentes propiedades del documento:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

1. [Guarde](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) el archivo PDF actualizado utilizando el método Save.

Las propiedades disponibles son:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Cada una se utiliza y describe en el código a continuación. El siguiente fragmento de código te muestra cómo establecer las propiedades utilizando la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SetDocumentWindowAndPageDisplayProperties()
{
    // Cadena para el nombre del camino.
    String _dataDir("C:\\Samples\\");
    // Cadena para el nombre del archivo.
    String inputFileName("sample.pdf");
    String outputFileName("sample_page_display_properties.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Establecer diferentes propiedades del documento
    // Especificar para posicionar la ventana del documento - Predeterminado: false
    document->set_CenterWindow(true);

    // Orden de lectura predominante; determina la posición de la página
    // Cuando se muestra lado a lado - Predeterminado: L2R
    document->set_Direction(Direction::R2L);

    // Especificar si la barra de título de la ventana debe mostrar el título del documento
    // Si es false, la barra de título muestra el nombre del archivo PDF - Predeterminado: false
    document->set_DisplayDocTitle(true);

    // Especificar si se debe cambiar el tamaño de la ventana del documento para ajustarse al tamaño de
    // La primera página mostrada - Predeterminado: false
    document->set_FitWindow(true);

    // Especificar si se debe ocultar la barra de menú de la aplicación del visor - Predeterminado: false
    document->set_HideMenubar(true);

    // Especificar si se debe ocultar la barra de herramientas de la aplicación del visor - Predeterminado: false
    document->set_HideToolBar(true);

    // Especificar si se deben ocultar elementos de la interfaz de usuario como barras de desplazamiento
    // Y dejar solo el contenido de la página mostrado - Predeterminado: false
    document->set_HideWindowUI(true);

    // Modo de página del documento. especificar cómo mostrar el documento al salir del modo de pantalla completa.
    document->set_NonFullScreenPageMode(PageMode::UseOC);

    // Especificar el diseño de la página, es decir, página única, una columna
    document->set_PageLayout(PageLayout::TwoColumnLeft);

    // Especificar cómo debe mostrarse el documento al abrirse
    // Es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos
    document->set_PageMode(PageMode::UseThumbs);

    // Guardar archivo PDF actualizado
    document->Save(_dataDir + outputFileName);
}
```
### Incrustación de fuentes en un archivo PDF existente

Los lectores de PDF soportan [un núcleo de 14 fuentes](https://en.wikipedia.org/wiki/PDF#Text) para que los documentos se puedan mostrar de la misma manera independientemente de la plataforma en la que se visualice el documento. Cuando un PDF contiene una fuente que no es una de las 14 fuentes principales, incrusta la fuente en el archivo PDF para evitar la sustitución de fuentes.

Aspose.PDF para C++ soporta la incrustación de fuentes en archivos PDF existentes. Puedes incrustar una fuente completa o un subconjunto de la fuente. Para incrustar la fuente, abre el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Luego usa la clase [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.font) para incrustar la fuente en el archivo PDF. Para incrustar la fuente completa, usa la propiedad IsEmbeded de la clase Font; para usar un subconjunto de la fuente, usa la propiedad IsSubset.

{{% alert color="primary" %}}

Un subconjunto de fuente incrusta solo los caracteres que se utilizan y es útil donde las fuentes se usan para frases cortas o eslóganes, por ejemplo, donde una fuente corporativa se usa para un logotipo, pero no para el texto del cuerpo. Usar un subconjunto reduce el tamaño del archivo del PDF de salida. Sin embargo, si se utiliza una fuente personalizada para el texto del cuerpo, incrústela en su totalidad.

{{% /alert %}}

El siguiente fragmento de código muestra cómo incrustar una fuente en un archivo PDF.

### Incrustar Fuentes Estándar Tipo 1

Existen documentos PDF que utilizan fuentes de un conjunto especial llamadas "Fuentes Estándar Tipo 1". Este conjunto incluye 14 fuentes y la incrustación de este tipo de fuente requiere el uso de banderas especiales, es decir, [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a8f1a88eef22e05ee9ee22a79db9cb9f6).

A continuación se muestra el fragmento de código que se puede utilizar para obtener un documento con todas las fuentes incrustadas, incluidas las Fuentes Estándar Tipo 1:

```cpp
void EmbeddingStandardType1Fonts()
{

    // String para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");
    // String para el nombre del archivo.
    String inputFileName("sample.pdf");
    String outputFileName("embedded-fonts-updated_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Establecer la propiedad EmbedStandardFonts del documento
    document->set_EmbedStandardFonts(true);
    for (auto page : document->get_Pages())
    {
        auto fonts = page->get_Resources()->get_Fonts();
        if (fonts != nullptr)
        {
            for (auto pageFont : fonts)
            {
                // Verificar si la fuente ya está incrustada
                if (!pageFont->get_IsEmbedded())
                {
                    pageFont->set_IsEmbedded(true);
                }
            }
        }
    }
    document->Save(_dataDir + outputFileName);
}
```
### Incrustar Fuentes al crear PDF

Si necesita usar cualquier fuente que no sean las 14 fuentes principales compatibles con Adobe Reader, debe incrustar la descripción de la fuente mientras genera el archivo Pdf. Si la información de la fuente no está incrustada, Adobe Reader la tomará del sistema operativo si está instalada en el sistema, o construirá una fuente sustituta de acuerdo con el descriptor de la fuente en el Pdf.

>Tenga en cuenta que la fuente incrustada debe estar instalada en la máquina host, es decir, en el caso del siguiente código, la fuente 'Univers Condensed' está instalada en el sistema.

Usamos la propiedad IsEmbedded de la clase Font para incrustar la información de la fuente en el archivo Pdf. Establecer el valor de esta propiedad en 'True' incrustará el archivo de fuente completo en el Pdf, sabiendo que esto aumentará el tamaño del archivo Pdf. A continuación se muestra el fragmento de código que se puede usar para incrustar la información de la fuente en el Pdf.

```cpp
void EmbeddingFontsWhileCreatingPDF()
{
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");
    String outputFileName("EmbedFontWhileDocCreation_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Create a section in the Pdf object
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>("");
    auto segment = MakeObject <TextSegment>(u"This is a sample text using Custom font.");

    auto ts = MakeObject<TextState>();

    ts->set_Font(FontRepository::FindFont(u"Arial"));
    ts->get_Font()->set_IsEmbedded(true);
    segment->set_TextState(ts);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);

    // Save PDF Document
    document->Save(_dataDir);
}
```

### Establecer el Nombre de Fuente Predeterminado al Guardar PDF

Cuando un documento PDF contiene fuentes que no están disponibles en el propio documento ni en el dispositivo, la API reemplaza estas fuentes con la fuente predeterminada. Cuando la fuente está disponible (está instalada en el dispositivo o está incrustada en el documento), el PDF de salida debe tener la misma fuente (no debe ser reemplazada por la fuente predeterminada). El valor de la fuente predeterminada debe contener el nombre de la fuente (no la ruta a los archivos de fuentes). Apose.PDF para C++ implementó una función para establecer el nombre de la fuente predeterminada al guardar un documento como PDF. El siguiente fragmento de código se puede usar para establecer la fuente predeterminada:

```cpp
void SetDefaultFontNameWhileSavingPDF()
{
    // String para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");
    // String para el nombre del archivo.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);

    auto pdfSaveOptions = MakeObject<PdfSaveOptions>();

    // Especificar el Nombre de Fuente Predeterminado
    pdfSaveOptions->set_DefaultFontName(newName);
    document->Save(_dataDir + outputFileName, pdfSaveOptions);
}
```

### Obtener Todas las Fuentes del Documento PDF

En caso de que desees obtener todas las fuentes de un documento PDF, puedes usar el método [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a2e22a508e8baef176dfc34734cf0def9).GetAllFonts() proporcionado en la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Por favor revisa el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```cpp
void GetAllFontsFromPDFdocument()
{
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");
    // Cadena para el nombre del archivo.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto font : fonts)
    {
        std::cerr << font->get_FontName() << std::endl;
    }
}
```

### Obtener Advertencias para Sustitución de Fuentes

Aspose.PDF para C++ proporciona métodos para obtener notificaciones sobre la sustitución de fuentes para manejar casos de sustitución de fuentes. Los fragmentos de código a continuación muestran cómo usar la funcionalidad correspondiente.

```cpp
void GetWarningsForFontSubstitution()
{
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    document->FontSubstitution = Aspose::Pdf::Document::FontSubstitutionHandler(OnFontSubstitution);
}
```

El método [OnFontSubstitution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac776d8736d430532bdaa530a36eb51a0) se muestra a continuación.

```cpp
void OnFontSubstitution(Aspose::Pdf::Text::Font &font, Aspose::Pdf::Text::Font& newFont) {
    std::cout << "Advertencia: La fuente " << font.get_FontName() 
            << " fue sustituida por otra fuente -> " 
            << newFont.get_FontName() << std::endl;
}
```

### Mejorar la incrustación de fuentes usando FontSubsetStrategy

La función para incrustar las fuentes como un subconjunto se puede lograr utilizando la propiedad IsSubset, pero a veces se desea reducir un conjunto de fuentes completamente incrustado a solo los subconjuntos que se utilizan en el documento. [Aspose.Pdf.Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) tiene la propiedad [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.i_document_font_utilities/) que incluye el método SubsetFonts(FontSubsetStrategy subsetStrategy). En el método SubsetFonts(), el parámetro subsetStrategy ayuda a ajustar la estrategia de subconjunto. FontSubsetStrategy admite dos variantes siguientes de subconfiguración de fuentes.

- SubsetAllFonts - Esto creará un subconjunto de todas las fuentes utilizadas en un documento.
- SubsetEmbeddedFontsOnly - Esto creará un subconjunto solo de aquellas fuentes que están completamente incrustadas en el documento.

El siguiente fragmento de código muestra cómo configurar FontSubsetStrategy:

```cpp
void ImproveFontsEmbeddingUsingFontSubsetStrategy()
{
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String inputFileName("sample.pdf");
    // Cadena para el nombre del archivo.
    String outputFileName("sample_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    // Todas las fuentes se incrustarán como subconjunto en el documento en caso de SubsetAllFonts.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    // El subconjunto de fuentes se incrustará para fuentes completamente incrustadas, pero las fuentes que no están incrustadas en el documento no se verán afectadas.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(_dataDir + outputFileName);
}
```
### Obtener-Establecer Factor de Zoom de Archivo PDF

A veces, deseas establecer el factor de zoom de un documento PDF. Con Aspose.PDF para C++, puedes establecer el valor del factor de zoom mediante el método [set_OpenAction(…) method](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#abb5c84979077034d06a673409b666e21) de la clase Document.

La propiedad Destination de la clase [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action/) te permite obtener el valor de zoom asociado con un archivo PDF. De manera similar, se puede utilizar para establecer el factor de zoom de un archivo.

#### Establecer Factor de Zoom

El siguiente fragmento de código muestra cómo establecer el factor de zoom de un archivo PDF.

```cpp
void SetZoomFactor() {
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String inputFileName("sample.pdf");
    // Cadena para el nombre del archivo.
    String outputFileName("Zoomed_pdf_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 0, 0, .5));

    document->set_OpenAction(action);
    // Guardar el documento
    document->Save(_dataDir + outputFileName);
}
```

#### Obtener Factor de Zoom

Obtén el factor de zoom en tu archivo PDF usando Aspose.PDF para C++.

El siguiente fragmento de código muestra cómo obtener el factor de zoom de un archivo PDF:

```cpp
void GetZoomFactor() 
{
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Crear objeto GoToAction
    auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(document->get_OpenAction());

    // Obtener el factor de Zoom del archivo PDF
    auto zoom = System::DynamicCast<Aspose::Pdf::Annotations::XYZExplicitDestination>(action->get_Destination());
    Console::WriteLine(zoom->get_Zoom()); // Valor de zoom del documento;
}
```

### Estableciendo Propiedades de Preajuste del Diálogo de Impresión

Aspose.PDF para C++ permite establecer las propiedades de preajuste del diálogo de impresión de un documento PDF. Permite cambiar la propiedad DuplexMode para un documento PDF, que está configurado en simplex por defecto. Esto se puede lograr utilizando dos metodologías diferentes como se muestra a continuación.

```cpp
void SettingPrintDialogPresetProperties()
{
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");
    // Cadena para el nombre del archivo.
    String outputFileName("SettingPrintDialogPresetProperties.pdf");

    auto document = MakeObject<Document>();
    document->get_Pages()->Add();
    document->set_Duplex(PrintDuplex::DuplexFlipLongEdge);
    document->Save(_dataDir + outputFileName);
}
```

### Configurando Propiedades Predeterminadas del Diálogo de Impresión usando el Editor de Contenido PDF

```cpp
void SettingPrintDialogPresetPropertiesUsingContentEditor() {
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String inputFileName("sample.pdf");
    String outputFileName("SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto contentEditor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    contentEditor->BindPdf(outputFileName);
    if ((contentEditor->GetViewerPreference() & Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge) > 0)
    {
    std::cout << "El archivo tiene flip corto en dúplex" << std::endl;
    }

    contentEditor->ChangeViewerPreference(Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge);
    contentEditor->Save(_dataDir + outputFileName);
}
```
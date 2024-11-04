---
title: Manipular Documento PDF 
linktitle: Manipular Documento PDF
type: docs
weight: 30
url: /cpp/manipulate-pdf-document/
lastmod: "2021-11-11"
description: Esta sección explica sobre la validación del Documento PDF para el Estándar PDF A, cómo trabajar con TOC, cómo establecer la fecha de caducidad del PDF y cómo determinar el Progreso de la generación del archivo PDF.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Validar Documento PDF para el Estándar PDF A (A 1A y A 1B)

Para validar un documento PDF para la compatibilidad con PDF/A-1a o PDF/A-1b, use el método [Validate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aa1ac4565b320807c718c44eeee7cda8c) de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Este método le permite especificar el nombre del archivo en el que se guardará el resultado y el tipo de validación requerido [PdfFormat](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ac83739fd7c818167c2fdc4dd554de763) enumeración: PDF_A_1A o PDF_A_1B.


{{% alert color="primary" %}}

El formato XML de salida es un formato personalizado de Aspose. El XML contiene una colección de etiquetas con el nombre Problem; cada etiqueta contiene los detalles de un problema particular. El atributo ObjectID de la etiqueta Problem representa el ID del objeto particular al que este problema está relacionado. El atributo Clause representa una regla correspondiente en la especificación PDF.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo validar un documento PDF para PDF/A-1A.

```cpp
void ExampleValidate01() {
    // String para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1A.xml");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Validar PDF para PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1A);
}
```

El siguiente fragmento de código te muestra cómo validar un documento PDF para PDF/A-1B.

```cpp
void ExampleValidate02() {
    // String para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1B.xml");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Validar PDF para PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1B);
}
```

## Trabajando con TOC

### Agregar TOC a un PDF Existente

La API de Aspose.PDF te permite agregar una tabla de contenido ya sea al crear un PDF, o a un archivo existente.

Para agregar un TOC a un archivo PDF existente, usa la clase [Heading](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.heading) en el espacio de nombres Aspose.Pdf. El espacio de nombres Aspose.Pdf te permite crear nuevos archivos PDF y manipular los existentes. Para agregar un TOC a un PDF existente, utiliza el espacio de nombres Aspose.Pdf.

El siguiente fragmento de código muestra cómo crear una tabla de contenidos dentro de un archivo PDF existente.

```cpp
void ExampleToc01() {
    // Cadena para nombres de ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para nombres de archivo
    String inputFileName("AddTOC.pdf");
    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obtener acceso a la primera página del archivo PDF
    auto tocPage = document->get_Pages()->Insert(1);

    // Crear objeto para representar la información del TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Tabla de Contenidos");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Establecer el título para el TOC
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    // Crear objetos de cadena que se usarán como elementos del TOC
    auto titles = MakeArray<String>(4);
    titles->SetValue(u"Primera página", 0);
    titles->SetValue(u"Segunda página", 1);
    titles->SetValue(u"Tercera página", 2);
    titles->SetValue(u"Cuarta página", 3);

    for (int i = 0; i < 2; i++)
    {
        // Crear objeto Heading
        auto heading2 = MakeObject<Heading>(1);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);

        // Especificar la página de destino para el objeto heading

        heading2->set_DestinationPage(document->get_Pages()->idx_get(i + 2));

        // Página de destino
        heading2->set_Top(document->get_Pages()->idx_get(i + 2)->get_Rect()->get_Height());

        // Coordenada de destino
        segment2->set_Text(titles[i]);

        // Agregar heading a la página que contiene el TOC
        tocPage->get_Paragraphs()->Add(heading2);
    }

    // Guardar el documento actualizado
    document->Save(_dataDir + outputFileName);
}
```

### Establecer diferentes TabLeaderType para diferentes niveles de TOC

Aspose.PDF para C++ también permite establecer diferentes TabLeaderType para diferentes niveles de TOC. Necesitas establecer la propiedad LineDash de FormatArray con el valor apropiado de TabLeaderType. Luego, puedes añadir la sección de la lista a la colección de la sección del documento PDF. Después, crea una sección en el documento PDF y guarda el archivo PDF.

```cpp
void ExampleToc02() {
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();

    //establecer LeaderType
    tocInfo->set_LineDash(TabLeaderType::Solid);

    // Crear objeto para representar la información de TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Tabla de Contenidos");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Establecer el título para TOC
    tocInfo->set_Title(title);

    //Añadir la sección de la lista a la colección de secciones del documento PDF
    tocPage->set_TocInfo(tocInfo);

    //Definir el formato de los cuatro niveles de lista estableciendo los márgenes izquierdos
    //y
    //configuraciones de formato de texto de cada nivel

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(0)->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(1)->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    //Crear una sección en el documento PDF
    auto page = document->get_Pages()->Add();

    //Añadir cuatro encabezados en la sección
    for (int Level = 1; Level <= 4; Level++)
    {
    auto heading2 = MakeObject<Heading>(Level);
    auto segment2 = MakeObject<TextSegment>();

    heading2->get_Segments()->Add(segment2);
    heading2->set_IsAutoSequence(true);
    heading2->set_TocPage(tocPage);
    segment2->set_Text(u"Encabezado de Muestra" + Level);
    heading2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial Unicode MS"));

    //Añadir el encabezado en la Tabla de Contenidos.
    heading2->set_IsInList(true);
    page->get_Paragraphs()->Add(heading2);
    }

    // guardar el Pdf
    document->Save(_dataDir + outputFileName);
}
```

### Ocultar Números de Página en la Tabla de Contenidos

Si deseas ocultar los números de página junto con los títulos en una tabla de contenidos, puedes usar la propiedad [IsShowPageNumbers](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info#ada10e841699bba062dcd0b440c26b832) de la Clase [TOCInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info) como falso.

Por favor, revisa el siguiente fragmento de código para ocultar los números de página en la tabla de contenidos:

```cpp
void ExampleToc03() {
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto tocPage = document->get_Pages()->Add();

    // Crear objeto para representar la información de la tabla de contenidos
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Tabla de Contenidos");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Establecer el título para la tabla de contenidos
    tocInfo->set_Title(title);

    //Agregar la sección de la lista a la colección de secciones del documento Pdf  
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_IsShowPageNumbers(false);

    //Definir el formato de la lista de cuatro niveles estableciendo los márgenes izquierdos y
    //configuraciones de formato de texto de cada nivel

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    //Agregar cuatro encabezados en la sección
    for (int Level = 1; Level != 5; Level++)
    {
        auto heading2 = MakeObject<Heading>(Level);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);
        heading2->set_IsAutoSequence(true);
        segment2->set_Text(u"este es el encabezado del nivel " + Level);
        heading2->set_IsInList(true);
        page->get_Paragraphs()->Add(heading2);
    }
    // guardar el Pdf
    document->Save(_dataDir + outputFileName);
}
```

## Cómo establecer la fecha de caducidad de un PDF

Aplicamos privilegios de acceso en archivos PDF para que un cierto grupo de usuarios pueda acceder a características/objetos particulares de documentos PDF. Con el fin de restringir el acceso al archivo PDF, generalmente aplicamos cifrado y podemos tener un requisito para establecer la caducidad del archivo PDF, de modo que el usuario que acceda/vea el documento reciba un aviso válido sobre la caducidad del archivo PDF.

Para cumplir con el requisito mencionado anteriormente, podemos usar el objeto [JavascriptAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.javascript_action/). Por favor, consulte el siguiente fragmento de código.

```cpp
void SetPDFexpiryDate() {

    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo. 
    String outputFileName("SetExpiryDate_out.pdf");

    // Instanciar objeto Document
    auto document = MakeObject<Document>();

    // Agregar página a la colección de páginas del archivo PDF
    document->get_Pages()->Add();

    // Agregar fragmento de texto a la colección de párrafos del objeto página
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(new TextFragment(u"Hola Mundo..."));

    String javascriptCode(u"var year=2017;");
    javascriptCode += u"var month=5;";
    javascriptCode += u"today = new Date(); today = new Date(today.getFullYear(), today.getMonth());";
    javascriptCode += u"expiry = new Date(year, month);";
    javascriptCode += u"if (today.getTime() > expiry.getTime())";
    javascriptCode += u"app.alert('El archivo ha expirado. Necesitas uno nuevo.');";

    // Crear objeto JavaScript para establecer la fecha de caducidad del PDF
    auto javaScript = MakeObject<Aspose::Pdf::Annotations::JavascriptAction>(javascriptCode);

    // Establecer JavaScript como acción de apertura del PDF
    document->set_OpenAction(javaScript);

    // Guardar documento PDF
    document->Save(_dataDir + outputFileName);
}
```

## Determinar el Progreso de la Generación de Archivos PDF

Un cliente nos pidió agregar una función que permita a los desarrolladores determinar el progreso de la generación de archivos PDF. Aquí está la respuesta a esa solicitud.

El campo [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb) de la clase [DocSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) te permite determinar cómo va la generación del PDF.

Los fragmentos de código a continuación muestran cómo usar [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb).

```cpp
using ProgressHandler = System::MulticastDelegate<void(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo>)>;
void ConversionProgressCallback(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    String eventType;
    switch (eventInfo->EventType)
    {
    case ProgressEventType::ResultPageCreated:
        eventType = u"ResultPageCreated";
        break;
    case ProgressEventType::ResultPageSaved:
        eventType = u"ResultPageSaved";
        break;
    case ProgressEventType::SourcePageAnalysed:
        eventType = u"SourcePageAnalysed";
        break;
    case ProgressEventType::TotalProgress:
        eventType = u"TotalProgress";
        break;
    }
    Console::WriteLine(String::Format(u"Event type: {0}, Value: {1}, MaxValue: {2}", 
        eventType, eventInfo->Value, eventInfo->MaxValue));
}
```

```cpp
void DetermineProgressOfPDFfileGeneration() {
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Abrir documento
    auto saveOptions = MakeObject<DocSaveOptions>();

    saveOptions->CustomProgressHandler = ProgressHandler(ConversionProgressCallback);

    document->Save(_dataDir + outputFileName, saveOptions);
}
```

## Aplanar PDF Rellenable en C++

Los documentos PDF a menudo incluyen formularios con widgets interactivos rellenables como botones de opción, casillas de verificación, cuadros de texto, listas, etc. Para hacerlo no editable para diversos propósitos de aplicación, necesitamos aplanar el archivo PDF. Aspose.PDF para C++ proporciona la función para aplanar tu PDF en C++ con solo unas pocas líneas de código:

```cpp
void FlattenFillablePDF() {
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");
    // Cadena para el nombre del archivo.
    String inputFileName("sample-form.pdf");
    String outputFileName("FlattenForms_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Aplanar PDF Rellenable 
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for (auto item : document->get_Form()->get_Fields())
        item->Flatten();
    }

    // Guardar el documento actualizado
    document->Save(_dataDir + outputFileName);
}
```
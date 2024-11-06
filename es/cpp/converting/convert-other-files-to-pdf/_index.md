---
linktitle: Convertir otros formatos de archivo a PDF
type: docs
weight: 80
url: es/cpp/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir otros formatos de archivo a un documento PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Convertir EPUB a PDF

**Aspose.PDF para C++** te permite simplemente convertir archivos EPUB al formato PDF.

<abbr title="electronic publication">EPUB</abbr> (abreviatura de publicación electrónica) es un estándar de libro electrónico libre y abierto del International Digital Publishing Forum (IDPF). Los archivos tienen la extensión .epub. EPUB está diseñado para contenido reflujo, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización en particular.

EPUB también admite contenido de diseño fijo. El formato está diseñado como un único formato que los editores y las casas de conversión pueden usar internamente, así como para distribución y venta. Sustituye el estándar Open eBook. La versión EPUB 3 también está respaldada por el Grupo de Estudio de la Industria del Libro (BISG), una asociación líder en el comercio de libros para las mejores prácticas estandarizadas, investigación, información y eventos, para el empaquetado de contenido.

Pasos de conversión:

1. Cree una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de la ruta y el nombre del archivo.
1. Cree una instancia de la clase [EpubLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Cree una instancia de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el nombre del archivo fuente mencionado y las opciones.
1. Cargue y [Guarde](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) el archivo de entrada.

El siguiente fragmento de código muestra cómo convertir archivos EPUB a formato PDF con C++.

```cpp
void ConvertEPUBtoPDF()
{
    std::clog << "EPUB to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("aliceDynamic.epub");
    String outfilename("epub_test.pdf");
    auto options = MakeObject<EpubLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "EPUB to PDF convert: End" << std::endl;
}
```
{{% alert color="success" %}}
**Intente convertir EPUB a PDF en línea**

Aspose.PDF para C++ le presenta una aplicación gratuita en línea ["EPUB a PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), donde puede intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de EPUB a PDF con aplicación gratuita](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Convertir Texto a PDF

**Aspose.PDF para C++** soporta la función de convertir texto plano y archivo de texto preformateado a formato PDF.

Convertir texto a PDF significa agregar fragmentos de texto a la página PDF. En cuanto a los archivos de texto, estamos tratando con 2 tipos de texto: preformateado (por ejemplo, 25 líneas con 80 caracteres por línea) y texto no formateado (texto plano). Dependiendo de nuestras necesidades, podemos controlar esta adición nosotros mismos o confiarla a los algoritmos de la biblioteca.

### Convertir archivo de texto plano a PDF

En el caso del archivo de texto plano, podemos usar la siguiente técnica:

1. Crea una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de ruta y el nombre de archivo.
1. Lee el archivo de texto fuente usando [TextReader](https://reference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.)
1. Instancia un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Añade una [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) a la colección de páginas del documento.
1. Crea un nuevo objeto de TextFragment y pasa el objeto TextReader a su constructor.
1. Añade un nuevo párrafo de texto en la colección de párrafos y pasa el objeto TextFragment.
1. Carga y [Guarda](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) el archivo de entrada.

```cpp
void ConvertTextToPDF()
{
    std::clog << "Conversión de Texto a PDF: Iniciar" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.txt");
    String outfilename("TextToPDF.pdf");

    // Lee el archivo de texto fuente
    String content = System::IO::File::ReadAllText(_dataDir + infilename);

    // Instancia un objeto Document llamando a su constructor vacío
    auto document = MakeObject<Document>();

    // Añade una nueva página en la colección de Páginas del Documento
    auto page = document->get_Pages()->Add();

    // Crea una instancia de TextFragment y pasa el texto del objeto lector a su constructor como argumento
    auto text = MakeObject<TextFragment>(content);

    // Añade un nuevo párrafo de texto en la colección de párrafos y pasa el objeto TextFragment
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Guarda el archivo PDF resultante
    document->Save(_dataDir + outfilename);
    std::clog << "Conversión de Texto a PDF: Fin" << std::endl;
}
```
### Convertir archivo de texto preformateado a PDF

Convertir texto preformateado es como texto plano, pero necesitas realizar algunas acciones adicionales como establecer márgenes, tipo de fuente y tamaño. Obviamente, la fuente debe ser monoespaciada (por ejemplo, Courier New).

Sigue estos pasos para convertir texto preformateado a PDF con C++:

1. Instanciar un objeto Document llamando a su constructor vacío.
1. Establecer márgenes izquierdo y derecho para una mejor presentación.
1. Instanciar el objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) y agregar una nueva página en la colección Pages.
1. Cargar y [Guardar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) el archivo de imagen de entrada.

```CPP
void ConvertPreFormattedTextToPdf()
{
    std::clog << "Texto preformateado a PDF: Inicio" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("rfc822.txt");
    String outfilename("TextToPDF.pdf");
    // Leer el archivo de texto como arreglo de cadenas
    auto lines = System::IO::File::ReadAllLines(_dataDir + infilename);

    // Instanciar un objeto Document llamando a su constructor vacío
    auto document = MakeObject<Document>();

    // Agregar una nueva página en la colección Pages del Document
    auto page = document->get_Pages()->Add();

    // Establecer márgenes izquierdo y derecho para una mejor presentación
    page->get_PageInfo()->get_Margin()->set_Left(20);
    page->get_PageInfo()->get_Margin()->set_Right(10);
    page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
    page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);

    for (int index = 0; index < lines->get_Length(); index++)
    {
        // verificar si la línea contiene el carácter "form feed"
        // ver https://en.wikipedia.org/wiki/Page_break
        auto line = lines->idx_get(index);
        if (line.StartsWith(u"\x0c"))
        {
        if (document->get_Pages()->get_Count() > 3) break;
        page = document->get_Pages()->Add();
        // Establecer márgenes izquierdo y derecho para una mejor presentación
        page->get_PageInfo()->get_Margin()->set_Left(20);
        page->get_PageInfo()->get_Margin()->set_Right(10);
        page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
        page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);
        }
        else
        {
        // Crear una instancia de TextFragment y
        // pasar la línea a su constructor como argumento
        auto text = MakeObject<TextFragment>(line);

        // Agregar un nuevo párrafo de texto en la colección de párrafos y pasar el objeto TextFragment
        page->get_Paragraphs()->Add(text);
        }
    }

    // Guardar el archivo PDF resultante
    document->Save(_dataDir + outfilename);
    std::clog << "Texto preformateado a PDF: Fin" << std::endl;
}
```

{{% alert color="success" %}}
**Intenta convertir TEXTO a PDF en línea**

Aspose.PDF para C++ te presenta la aplicación gratuita en línea ["Texto a PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), donde puedes probar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión TEXTO a PDF con Aplicación Gratuita](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

## Convertir XPS a PDF

**Aspose.PDF para C++** admite la función de convertir archivos <abbr title="XML Paper Specification">XPS</abbr> al formato PDF. Revisa este artículo para resolver tus tareas.

El tipo de archivo XPS está principalmente asociado con la Especificación de Papel XML por Microsoft Corporation. La Especificación de Papel XML (XPS), anteriormente con nombre en clave Metro y que subsume el concepto de marketing Next Generation Print Path (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en su sistema operativo Windows.

{{% alert color="primary" %}}

El formato de archivo es básicamente un archivo XML comprimido que se utiliza principalmente para la distribución y el almacenamiento. Es muy difícil de editar y mayormente implementado por Microsoft.

{{% /alert %}}

Para convertir XPS a PDF con Aspose.PDF para C++, hemos introducido una clase llamada [XpsLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) que se utiliza para inicializar un objeto [LoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options). Luego, este objeto se pasa como argumento durante la inicialización del objeto Document y ayuda al motor de renderizado de PDF a determinar el formato de entrada del documento de origen.

El siguiente fragmento de código muestra el proceso de conversión de un archivo XPS a formato PDF con C++.

```cpp
void ConvertXPStoPDF()
{
    std::clog << "XPS a PDF convertir: Comenzar" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.oxps");
    String outfilename("XPStoPDF.pdf");
    auto options = MakeObject<XpsLoadOptions>();
    try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
    };
    std::clog << "XPS a PDF convertir: Terminar" << std::endl;
}
```
{{% alert color="success" %}}
**Intenta convertir el formato XPS a PDF en línea**

Aspose.PDF para C++ te presenta la aplicación gratuita en línea ["XPS a PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), donde puedes probar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de XPS a PDF con Aplicación Gratuita](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Convertir XML a PDF

El formato XML se utiliza para almacenar datos estructurados. Hay varias maneras de convertir <abbr title="Extensible Markup Language">XML</abbr> a PDF en Aspose.PDF.

## Convertir XSL-FO a PDF

1. Crea una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de la ruta y el nombre del archivo.
1. Instanciar el [objeto XslFoLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Configurar la estrategia de manejo de errores.
1. Instanciar el Objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. [Guardar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) el archivo de imagen de entrada.

```cpp
void Convert_XSLFO_to_PDF()
{
    std::clog << "XSL-FO a PDF convertir: Inicio" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilenameXSL("c:\\samples\\employees.xslt");
    String infilenameXML("c:\\samples\\employees.xml");

    String outfilename("XMLFOtoPDF.pdf");
    // Instanciar objeto XslFoLoadOption
    auto options = new XslFoLoadOptions(infilenameXSL);
    // Establecer estrategia de manejo de errores
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // Crear objeto Document
    auto document = MakeObject<Document>(infilenameXML, options);
    document->Save(_dataDir + outfilename);
}
```

{{% alert color="success" %}}
**Intenta convertir XML a PDF en línea**

Aspose.PDF para C++ te presenta la aplicación en línea gratuita ["XML a PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.
[![Aspose.PDF Conversión XML a PDF con Aplicación Gratuita](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}
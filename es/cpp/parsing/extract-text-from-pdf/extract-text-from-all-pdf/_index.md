---
title: Extraer texto de todas las páginas de un PDF usando C++
linktitle: Extraer texto de PDF
type: docs
weight: 10
url: /es/cpp/extract-text-from-all-pdf/
description: Este artículo describe varias maneras de extraer texto de documentos PDF usando Aspose.PDF en C++. De páginas enteras, de una parte específica, basado en columnas, etc.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Texto de Todas las Páginas de un Documento PDF

Extraer texto de un documento PDF es un requerimiento común. En este ejemplo, verás cómo Aspose.PDF para C++ permite extraer texto de todas las páginas de un documento PDF. Necesitas crear un objeto de la clase [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Después de eso, abre el PDF usando la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) y llama al método 'Accept' de la colección [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). La clase [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) absorbe el texto del documento y lo devuelve en la propiedad 'Text'. El siguiente fragmento de código te muestra cómo extraer texto de todas las páginas de un documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages() {

    std::clog << __func__ << ": Start" << std::endl;
    // String para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para el nombre del archivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Crear objeto TextAbsorber para extraer texto
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Aceptar el absorbedor para todas las páginas
    document->get_Pages()->Accept(textAbsorber);
    // Obtener el texto extraído
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Llama al método **Accept** en una página particular del objeto Document. El índice es el número de página particular de donde se necesita extraer el texto.

```cpp
void ExtractTextFromParticularPage() {

    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para el nombre del archivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Crear objeto TextAbsorber para extraer texto
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Aceptar el absorbedor para todas las páginas
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Obtener el texto extraído
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extraer texto de las páginas usando Text Device

Puedes usar la clase [TextDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.text_device/) para extraer texto de un archivo PDF. TextDevice utiliza TextAbsorber en su implementación, por lo tanto, de hecho, hacen lo mismo, pero TextDevice solo se implementó para unificar el enfoque "Device" para extraer cualquier cosa de la página ImageDevice, PageDevice, etc. TextAbsorber puede extraer texto de Página, PDF completo o XForm, este TextAbsorber es más universal

### Extraer texto de todas las páginas

Los siguientes pasos y fragmento de código muestran cómo extraer texto de un PDF utilizando el dispositivo de texto.

1. Cree un objeto de la clase Document con el archivo PDF de entrada especificado
1. Cree un objeto de la clase TextDevice
1. Use el objeto de la clase TextExtractOptions para especificar las opciones de extracción
1. Use el método Process de la clase TextDevice para convertir el contenido en texto
1. Guarde el texto en el archivo de salida

```cpp
void ExtractTextUsingTextDevice() {

    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para nombre de ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para nombre de archivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto builder = MakeObject<System::Text::StringBuilder>();
    // Cadena para guardar texto extraído
    String extractedText;

    for (auto page : document->get_Pages()) {
        auto textStream = MakeObject<System::IO::MemoryStream>();
        // Crear dispositivo de texto
        auto textDevice = MakeObject<Aspose::Pdf::Devices::TextDevice>();

        // Establecer opciones de extracción de texto - establecer modo de extracción de texto (Raw o Pure)
        auto textExtOptions = MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);

        textDevice->set_ExtractionOptions(textExtOptions);

        // Convertir una página particular y guardar texto en el flujo
        textDevice->Process(page, textStream);

        // Cerrar flujo de memoria
        textStream->Close();

        // Obtener texto del flujo de memoria
        extractedText = System::Text::Encoding::get_Unicode()->GetString(textStream->ToArray());
        builder->Append(extractedText);

    }
    // Guardar el texto extraído en archivo de texto
    System::IO::File::WriteAllText(_dataDir + outfilename, builder->ToString());
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Extraer texto de una región específica de la página

La clase [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) proporciona la capacidad de extraer texto de una página particular o de todas las páginas de un documento PDF. Esta clase devuelve el texto extraído en la propiedad 'Text'. Sin embargo, si tenemos el requisito de extraer texto de una región específica de la página, podemos usar la propiedad **Rectangle** de [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/). La propiedad Rectangle toma un objeto Rectangle como valor y utilizando esta propiedad, podemos especificar la región de la página de la cual necesitamos extraer el texto.

Se llama al método **Accept** de una página para extraer el texto. Crea objetos de las clases [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) y [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Llama al método 'Accept' en la página individual, como **Page** Index, del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/). El **Index** es el número de página particular de donde se necesita extraer el texto. Puedes obtener el texto de la propiedad 'Text' de la clase [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). El siguiente fragmento de código te muestra cómo extraer texto de una página individual.

```cpp
void ExtractTextFromParticularPageRegion() {

    std::clog << __func__ << ": Start" << std::endl;
    // String para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para el nombre del archivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Crear objeto TextAbsorber para extraer texto
    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
    textAbsorber->get_TextSearchOptions()->set_Rectangle(MakeObject<Rectangle>(100, 200, 250, 350));

    // Aceptar el absorbedor para todas las páginas
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Obtener el texto extraído
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;

}
```
## Extraer texto basado en columnas

El PDF es un formato muy popular, y por una buena razón: con PDF, puedes estar prácticamente seguro de que tu documento se mostrará e imprimirá de la misma manera en diferentes computadoras.

Sin embargo, los documentos PDF sufren de la desventaja de que generalmente carecen de información sobre qué contenido está en párrafos, tablas, figuras, información de encabezado/pie de página, y así sucesivamente.

Aspose.PDF para C++ - es una utilidad fácil de usar, que te permite extraer texto basado en columnas.

```cpp
void ExtractTextBasedOnColumns() {

    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para el nombre del archivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Crear objeto TextAbsorber para extraer texto
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>();


    // Aceptar el absorber para todas las páginas
    document->get_Pages()->Accept(textFragmentAbsorber);

    auto tfc = textFragmentAbsorber->get_TextFragments();
    for (auto tf : tfc)
    {
        // Necesidad de reducir el tamaño de fuente al menos un 70%
        auto size = tf->get_TextState()->get_FontSize() * 0.7f;
        tf->get_TextState()->set_FontSize(size);
    }
    auto stream = MakeObject<System::IO::MemoryStream>();
    document->Save(stream);
    document = MakeObject<Document>(stream);
    auto textAbsorber = MakeObject<TextAbsorber>();
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Second approach - Using ScaleFactor

En esta nueva versión, también hemos introducido varias mejoras en TextAbsorber y en el mecanismo interno de formato de texto. Así que ahora durante la extracción de texto usando el modo 'Pure', puede especificar la opción [ScaleFactor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_extraction_options#a4f9a173765d483b493c31e416f8b035a) y puede ser otro enfoque para extraer texto de un documento PDF de varias columnas además del enfoque mencionado anteriormente. Este factor de escala puede establecerse para ajustar la cuadrícula que se utiliza para el mecanismo interno de formato de texto durante la extracción de texto. Especificar los valores de ScaleFactor entre 1 y 0.1 (incluido 0.1) tiene el mismo efecto que la reducción de fuente.

Especificar los valores de ScaleFactor entre 0.1 y -0.1 se trata como un valor cero, pero hace que el algoritmo calcule el factor de escala necesario durante la extracción de texto automáticamente. El cálculo se basa en el ancho promedio de glifo de la fuente más popular en la página, pero no podemos garantizar que en el texto extraído ninguna cadena de la columna llegue al inicio de la siguiente columna. Tenga en cuenta que si no se especifica el valor de ScaleFactor, se usará el valor predeterminado de 1.0. Esto significa que no se llevará a cabo ningún escalado. Si el valor de ScaleFactor especificado es más de 10 o menos de -0.1, se usará el valor predeterminado de 1.0.

Proponemos el uso de auto-escalado (ScaleFactor = 0) al procesar un gran número de archivos PDF para la extracción de contenido de texto. O establecer manualmente una reducción redundante del ancho de la cuadrícula (aproximadamente ScaleFactor = 0.5). Sin embargo, no debe determinar si el escalado es necesario para documentos concretos o no. Si establece una reducción redundante del ancho de la cuadrícula para el documento (que no lo necesita), el contenido de texto extraído seguirá siendo completamente adecuado. Por favor, eche un vistazo al siguiente fragmento de código.

```cpp
void ExtractTextUsingScaleFactor() {

    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para nombre de ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para nombre de archivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->set_ExtractionOptions(MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure));
    // Establecer el factor de escala a 0.5 es suficiente para dividir columnas en la mayoría de documentos
    // Establecer a cero permite al algoritmo elegir el factor de escala automáticamente
    textAbsorber->get_ExtractionOptions()->set_ScaleFactor(0.5); /* 0; */
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Extraer Texto Resaltado de Documento PDF

En varios escenarios de extracción de texto de un documento PDF, puedes encontrarte con el requisito de extraer solo el texto resaltado del documento PDF. Para implementar la funcionalidad, hemos añadido los métodos TextMarkupAnnotation.GetMarkedText() y TextMarkupAnnotation.GetMarkedTextFragments() en la API. Puedes extraer texto resaltado de un documento PDF filtrando TextMarkupAnnotation y utilizando los métodos mencionados. El siguiente fragmento de código muestra cómo puedes extraer texto resaltado de un documento PDF.

```cpp
void ExtractHighlightedText() {

    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para el nombre del archivo
    String infilename("sample-highlight.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Recorrer todas las anotaciones
    for (auto annotation : document->get_Pages()->idx_get(1)->get_Annotations())
    {
        // Filtrar TextMarkupAnnotation
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Highlight)
        {
        auto highlightedAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);

        // Recuperar fragmentos de texto resaltado
        auto collection = highlightedAnnotation->GetMarkedTextFragments();
        for (auto tf : collection)
        {
            // Mostrar texto resaltado
            String s = tf->get_Text();
            std::cout << s << std::endl;
        }
        }
    }
}
```

## Acceder a Fragmentos de Texto y Elementos de Segmento desde XML

A veces necesitamos acceder a elementos TextFragment o TextSegment al procesar documentos PDF generados a partir de XML. Aspose.PDF para C++ proporciona acceso a dichos elementos por nombre. El fragmento de código a continuación muestra cómo utilizar esta funcionalidad.

```cpp
void AccessTextFragmentandSegmentElementsXML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para el nombre del archivo
    String infilename("sample-doc.xml");
    String outfilename("sample-doc.pdf");

    auto document = MakeObject<Document>();
    document->BindXml(_dataDir + infilename);

    System::SharedPtr<Page> page = System::DynamicCast<Aspose::Pdf::Page>(document->GetObjectById(u"mainSection"));
    // Realizar algunas operaciones con la página
    // ...

    System::SharedPtr<TextSegment> segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(document->GetObjectById(u"product_description"));
    // Realizar algunas operaciones con el segmento
    // ...
    document->Save(_dataDir + outfilename);

    std::clog << __func__ << ": Finish" << std::endl;
}
```
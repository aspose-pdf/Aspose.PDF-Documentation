---
title: Buscar y Obtener Texto de las Páginas de un Documento PDF
linktitle: Buscar y Obtener Texto
type: docs
weight: 60
url: /es/cpp/search-and-get-text-from-pdf/
description: Este artículo explica cómo usar varias herramientas para buscar y obtener texto de documentos PDF. Podemos buscar con expresiones regulares en páginas particulares o en todo el documento.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Buscar y Obtener Texto de Todas las Páginas de un Documento PDF

La clase [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) te permite encontrar texto, que coincida con una frase particular, de todas las páginas de un documento PDF. Para buscar texto en todo el documento, necesitas llamar al método Accept de la colección [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). El método 'Accept' toma un objeto TextFragmentAbsorber como parámetro, que devuelve una colección de objetos TextFragment.

El siguiente fragmento de código te muestra cómo buscar texto en todas las páginas.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetTextFromAllThePagesOfPDFDocument() {
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("document");

    // Aceptar el absorbedor para todas las páginas
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obtener los fragmentos de texto extraídos en la colección
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Recorrer los fragmentos
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Texto :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Posición :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndentación :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndentación :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Fuente - Nombre :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Fuente - EsAccesible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Fuente - EstáIncrustada - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Fuente - EsSubconjunto :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Tamaño de Fuente :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Color de Primer Plano :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```

## Search and Get Text from all pages using Regular Expression

TextFragmentAbsorber te ayuda a buscar y recuperar texto, de todas las páginas, basado en una expresión regular. Primero, debe pasar una expresión regular al constructor de [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) como la frase. Después de eso, tiene que establecer la propiedad [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) del objeto TextFragmentAbsorber. Esta propiedad requiere un objeto TextSearchOptions y necesita pasar true como parámetro a su constructor mientras crea nuevos objetos. Como desea recuperar el texto coincidente de todas las páginas, necesita llamar al método Accept de la colección Pages. [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) devuelve un TextFragmentCollection que contiene todos los fragmentos que coinciden con los criterios especificados por la expresión regular. El siguiente fragmento de código le muestra cómo buscar y obtener texto de todas las páginas basado en una expresión regular.

```cpp
void SearchAndGetTextFromPagesUsingRegularExpression()
{
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(u"\\d{4}-\\d{4}"); // como 1999-2000

    // Establecer opción de búsqueda de texto para especificar el uso de expresión regular
    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Aceptar el absorbedor para la primera página del documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obtener los fragmentos de texto extraídos en la colección
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Recorrer los fragmentos
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Texto :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Posición :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Fuente - Nombre :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Fuente - EsAccesible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Fuente - EsIncrustada - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Fuente - EsSubconjunto :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Tamaño de Fuente :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Color de Primer Plano :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```
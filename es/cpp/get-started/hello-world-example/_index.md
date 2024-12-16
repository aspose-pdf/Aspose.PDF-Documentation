---
title: Aspose.PDF C++ Ejemplo
linktitle: Ejemplo Hola Mundo
type: docs
weight: 40
url: /es/cpp/hello-world-example/
description: Esta página muestra cómo usar programación simple para crear un documento PDF que contiene el texto - Hola Mundo.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

Un ejemplo de "Hola Mundo" se utiliza tradicionalmente para introducir las características de un lenguaje de programación o software con un caso de uso simple.

Aspose.PDF para C++ es una API de PDF rica en funciones que permite a los desarrolladores integrar capacidades de creación, manipulación y conversión de documentos PDF en sus aplicaciones C++. Soporta trabajar con muchos formatos de archivo populares, incluyendo PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX y formatos de archivo de imagen. En este artículo, estamos creando un documento PDF que contiene el texto "Hola Mundo!". Después de instalar Aspose.PDF para C++ en tu entorno, puedes ejecutar el siguiente ejemplo de código para ver cómo funciona la API de Aspose.PDF.

El siguiente fragmento de código sigue estos pasos:

1. Crea una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de ruta y el nombre de archivo.
1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). En este paso crearemos un documento PDF vacío con algunos metadatos pero sin páginas.
1. Añadir una [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) al objeto documento. Así que, ahora nuestro documento tendrá una página.
1. [Guardar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) el documento PDF resultante

El siguiente fragmento de código es un programa de Hello World para demostrar el funcionamiento de Aspose.PDF para la API de C++.

```cpp
void ExampleSimple()
{
    // Buffer para mantener la ruta combinada.
    String outputFileName;

    // String para el nombre de ruta.
    String _dataDir("C:\\Samples\\");

    // String para el nombre de archivo.
    String filename("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Añadir texto a la nueva página
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Guardar el PDF actualizado
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```
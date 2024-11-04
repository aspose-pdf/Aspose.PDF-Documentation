---
title: Crear Documento PDF
linktitle: Crear PDF
type: docs
weight: 10
url: /cpp/create-pdf-document/
description: Este artículo describe cómo crear y formatear el documento PDF con Aspose.PDF para C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Siempre estamos buscando una manera de generar documentos PDF y trabajar con ellos en proyectos C++ de manera más precisa, exacta y efectiva. Tener funciones fáciles de usar de una biblioteca nos permite concentrarnos más en el trabajo y menos en los detalles que consumen tiempo al intentar generar PDFs, ya sea en C++.

## Generar PDF usando C++

La API Aspose.PDF para C++ te permite crear y leer archivos PDF usando C++. La API se puede utilizar en una variedad de aplicaciones C++ incluyendo WinForms, y varias otras. En este artículo, vamos a mostrar cómo usar la API Aspose.PDF para C++ para generar y leer fácilmente archivos PDF en aplicaciones C++.

### Cómo Crear un Archivo PDF Simple

Para crear un archivo PDF usando C++, se pueden seguir los siguientes pasos.

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)  
1. Añade un objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) a la colección 'Pages' del objeto Document  
1. Añade [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) a la colección [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) de la página  
1. Guarda el documento PDF resultante  

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateDocument() {
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String outputFileName("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Añadir texto a la nueva página
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Guardar el PDF actualizado
    document->Save(_dataDir + outputFileName);
}
```
## Crear un documento PDF buscable

Aspose.PDF para C++ le permite crear PDFs desde cero y manipular los existentes. Cuando agrega elementos de texto a un PDF, el PDF resultante es buscable. Sin embargo, si convertimos una imagen que contiene texto a un archivo PDF, el contenido dentro del PDF no es buscable. Sin embargo, como una solución alternativa, podemos usar OCR en el archivo resultante para hacerlo buscable. Por lo tanto, primero necesita instalar Tesseract-OCR en su sistema, y tendrá una aplicación de consola tesseract.

El siguiente es el código completo para cumplir con este requisito:

```cpp
void CreateSearchableDocument() {
    // String para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");
    // String para el nombre del archivo.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);
    bool convertResult = false;
    try
    {
        convertResult = document->Convert(CallBackGetHocr);
    }
    catch (Exception ex)
    {
        std::cerr << ex->get_Message() << std::endl;
    }
    document->Dispose();
}

static String CallBackGetHocr(System::SharedPtr<System::Drawing::Image> img)
{
    String tmpFile = System::IO::Path::GetTempFileNameSafe();

    auto bmp = MakeObject<System::Drawing::Bitmap>(img);

    bmp->Save(tmpFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
    String inputFile = String::Format(u"\"{0}\"", tmpFile);
    String outputFile = String::Format(u"\"{0}\"", tmpFile);
    String arguments = inputFile + u" " + outputFile + u" -l eng hocr";
    String tesseractProcessName = u"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe";

    auto psi = MakeObject<System::Diagnostics::ProcessStartInfo>(tesseractProcessName, arguments);
    psi->set_UseShellExecute(true);
    psi->set_CreateNoWindow(true);
    psi->set_WindowStyle(System::Diagnostics::ProcessWindowStyle::Hidden);
    psi->set_WorkingDirectory(System::IO::Path::GetDirectoryName(tesseractProcessName));

    auto p = MakeObject<System::Diagnostics::Process>(psi);
    p->Start();
    p->WaitForExit();

    auto streamReader = MakeObject<System::IO::StreamReader>(tmpFile + u".hocr");
    String text = streamReader->ReadToEnd();
    streamReader->Close();

    if (System::IO::File::Exists(tmpFile))
        System::IO::File::Delete(tmpFile);
    if (System::IO::File::Exists(tmpFile + u".hocr"))
        System::IO::File::Delete(tmpFile + u".hocr");

    return text;
}
```
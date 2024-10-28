---
title: Convertir PDF a Documentos de Microsoft Word en C++
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /cpp/convert-pdf-to-word/
lastmod: "2021-11-19"
description: La biblioteca Aspose.PDF para C++ te permite convertir PDF a formato Word usando C++ con facilidad y control total. Estos formatos incluyen DOC y DOCX. Aprende más sobre cómo ajustar la conversión de documentos PDF a Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Resumen

Este artículo explica cómo convertir PDF a Documentos de Microsoft Word usando C++. Cubre estos temas.

_Formato_: **DOC**
- [C++ PDF a DOC](#cpp-pdf-to-doc)
- [C++ Convertir PDF a DOC](#cpp-pdf-to-doc)
- [C++ Cómo convertir archivo PDF a DOC](#cpp-pdf-to-doc)

_Formato_: **DOCX**
- [C++ PDF a DOCX](#cpp-pdf-to-docx)
- [C++ Convertir PDF a DOCX](#cpp-pdf-to-docx)
- [C++ Cómo convertir archivo PDF a DOCX](#cpp-pdf-to-docx)

_Formato_: **Formato DOC de Microsoft Word**
- [C++ PDF a Word](#cpp-pdf-to-word-doc)
- [C++ Convertir PDF a Word](#cpp-pdf-to-word-doc)

- [C++ Cómo convertir archivo PDF a Word](#cpp-pdf-to-word-doc)

_Format_: **Microsoft Word DOCX formato**
- [C++ PDF a Word](#cpp-pdf-to-word-docx)
- [C++ Convertir PDF a Word](#cpp-pdf-to-word-docx)
- [C++ Cómo convertir archivo PDF a Word](#cpp-pdf-to-word-docx)

Otros temas cubiertos por este artículo
- [Ver También](#see-also)

## Conversiones de PDF a Word en C++

Una de las características más populares es la conversión de PDF a Microsoft Word DOC, lo que facilita la manipulación del contenido. Aspose.PDF para C++ te permite convertir archivos PDF a DOC.

## Convertir archivo PDF a DOC (Word 97-2003)

Convierte archivos PDF a formato DOC con facilidad y control total. Aspose.PDF para C++ es flexible y soporta una amplia variedad de conversiones. Convertir páginas de documentos PDF a imágenes, por ejemplo, es una característica muy popular.

Una conversión que muchos de nuestros clientes han solicitado es de PDF a DOC: convertir un archivo PDF a un documento de Microsoft Word. Los clientes quieren esto porque los archivos PDF no se pueden editar fácilmente, mientras que los documentos de Word sí. Algunas empresas quieren que sus usuarios puedan manipular texto, tablas e imágenes en archivos que comenzaron como PDFs.

Manteniendo viva la tradición de hacer las cosas simples y comprensibles, Aspose.PDF para C++ te permite transformar un archivo PDF fuente en un archivo DOC con dos líneas de código. Para lograr esta función, hemos introducido una enumeración llamada SaveFormat y su valor .Doc te permite guardar el archivo fuente en formato Microsoft Word.

El siguiente fragmento de código C++ muestra el proceso de conversión de un archivo PDF a formato DOC.

<a name="cpp-pdf-to-doc" id="cpp-pdf-to-doc"><strong>Pasos: Convertir PDF a DOC en C++</strong></a> | <a name="cpp-pdf-to-word-doc" id="cpp-pdf-to-word-doc"><strong>Pasos: Convertir PDF a formato DOC de Microsoft Word en C++</strong></a>

1. Crea una instancia del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el documento PDF fuente.
2. Guárdelo en formato **SaveFormat::Doc** llamando al método **Document->Save()**.

```cpp
void ConvertPDFtoWord()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para nombre de ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para nombre de archivo
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Guardar el archivo en formato de documento MS
        document->Save(_dataDir + outfilename, SaveFormat::Doc);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

El siguiente fragmento de código muestra el proceso de conversión de un archivo PDF a DOC versión avanzada:

```cpp
void ConvertPDFtoWordDocAdvanced()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para nombre de ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para nombre de archivo
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::Doc);
    // Establecer el modo de reconocimiento como Flujo
    saveOptions->set_Mode(DocSaveOptions::RecognitionMode::Flow);
    // Establecer la proximidad horizontal como 2.5
    saveOptions->set_RelativeHorizontalProximity(2.5f);
    // Habilitar el valor para reconocer viñetas durante el proceso de conversión
    saveOptions->set_RecognizeBullets(true);

    try {
        // Guardar el archivo en formato de documento MS
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF para C++ te presenta la aplicación gratuita en línea ["PDF a DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Convertir PDF a DOC](pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF a DOCX

La API Aspose.PDF para C++ te permite leer y convertir documentos PDF a DOCX utilizando el lenguaje C++. DOCX es un formato bien conocido para documentos de Microsoft Word cuya estructura cambió de binario simple a una combinación de archivos XML y binarios. Los archivos Docx se pueden abrir con Word 2007 y versiones posteriores, pero no con las versiones anteriores de MS Word que soportan extensiones de archivo DOC.

El siguiente fragmento de código C++ muestra el proceso de conversión de un archivo PDF a formato DOCX. 

<a name="cpp-pdf-to-docx" id="cpp-pdf-to-docx"><strong>Pasos: Convertir PDF a DOCX en C++</strong></a> | <a name="cpp-pdf-to-word-docx" id="cpp-pdf-to-word-docx"><strong>Pasos: Convertir PDF a formato Microsoft Word DOCX en C++</strong></a>

1. Cree una instancia del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el documento PDF de origen.
2. Guárdelo en formato **SaveFormat::DocX** llamando al método **Document->Save()**.

```cpp
void ConvertPDFtoWord_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre del directorio
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Guardar el archivo en formato de documento de MS
        document->Save(_dataDir + outfilename, SaveFormat::DocX);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

La clase [`DocSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) tiene una propiedad llamada Format que proporciona la capacidad de especificar el formato del documento resultante, es decir, DOC o DOCX. En orden de convertir un archivo PDF a formato DOCX, por favor pase el valor Docx desde la enumeración DocSaveOptions.DocFormat.

Por favor, eche un vistazo al siguiente fragmento de código que proporciona la capacidad de convertir un archivo PDF a formato DOCX con C++.

```cpp
void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nombre de ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nombre de archivo
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::DocX);

    // Establecer otros parámetros de DocSaveOptions
    // ...

    // Guardar el archivo en formato de documento MS

    try {
        // Guardar el archivo en formato de documento MS
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="warning" %}}
**Intente convertir PDF a DOCX en línea**

Aspose.PDF para C++ le presenta la aplicación en línea gratuita ["PDF a DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Convertion PDF to Word Free App](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Ver También

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Formato_: **Formato Microsoft Word DOC**
- [C++ PDF a Word Código](#cpp-pdf-to-word-doc)
- [C++ PDF a Word API](#cpp-pdf-to-word-doc)
- [C++ PDF a Word Programáticamente](#cpp-pdf-to-word-doc)
- [C++ PDF a Word Biblioteca](#cpp-pdf-to-word-doc)
- [C++ Guardar PDF como Word](#cpp-pdf-to-word-doc)
- [C++ Generar Word desde PDF](#cpp-pdf-to-word-doc)
- [C++ Crear Word desde PDF](#cpp-pdf-to-word-doc)
- [C++ PDF a Word Convertidor](#cpp-pdf-to-word-doc)

_Formato_: **Formato Microsoft Word DOCX**

- [C++ PDF a Word Código](#cpp-pdf-to-word-docx)
- [C++ PDF a Word API](#cpp-pdf-to-word-docx)
- [C++ PDF a Word Programáticamente](#cpp-pdf-to-word-docx)
- [C++ PDF a Word Biblioteca](#cpp-pdf-to-word-docx)
- [C++ Guardar PDF como Word](#cpp-pdf-to-word-docx)
- [C++ Generar Word desde PDF](#cpp-pdf-to-word-docx)
- [C++ Crear Word desde PDF](#cpp-pdf-to-word-docx)
- [C++ Convertidor de PDF a Word](#cpp-pdf-to-word-docx)

_Formato_: **DOC**
- [C++ PDF a DOC Código](#cpp-pdf-to-doc)
- [C++ PDF a DOC API](#cpp-pdf-to-doc)
- [C++ PDF a DOC Programáticamente](#cpp-pdf-to-doc)
- [C++ PDF a DOC Biblioteca](#cpp-pdf-to-doc)
- [C++ Guardar PDF como DOC](#cpp-pdf-to-doc)
- [C++ Generar DOC desde PDF](#cpp-pdf-to-doc)
- [C++ Crear DOC desde PDF](#cpp-pdf-to-doc)
- [C++ Convertidor de PDF a DOC](#cpp-pdf-to-doc)

_Formato_: **DOC**
- [C++ PDF a DOCX Código](#cpp-pdf-to-docx)
- [C++ PDF a DOCX API](#cpp-pdf-to-docx)
- [C++ PDF a DOCX Programáticamente](#cpp-pdf-to-docx)
- [C++ PDF a DOCX Biblioteca](#cpp-pdf-to-docx)
- [C++ Guardar PDF como DOCX](#cpp-pdf-to-docx)

- [C++ Generar DOCX desde PDF](#cpp-pdf-to-docx)
- [C++ Crear DOCX desde PDF](#cpp-pdf-to-docx)
- [C++ Convertidor de PDF a DOCX](#cpp-pdf-to-docx)
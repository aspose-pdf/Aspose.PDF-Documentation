---
title: Convertir PDF a formatos PDF/A
linktitle: Convertir PDF a formatos PDF/A
type: docs
weight: 100
url: /es/cpp/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Este tema te muestra cómo Aspose.PDF permite convertir un archivo PDF a un archivo PDF compatible con PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para C++** te permite convertir un archivo PDF a un archivo PDF compatible con <abbr title="Portable Document Format / A">PDF/A</abbr>. Antes de hacerlo, el archivo debe ser validado. Este tema explica cómo.

{{% alert color="primary" %}}

Por favor, ten en cuenta que seguimos Adobe Preflight para validar la conformidad con PDF/A. Todas las herramientas en el mercado tienen su propia “representación” de conformidad con PDF/A. Por favor, consulta este artículo sobre herramientas de validación PDF/A como referencia. Elegimos productos Adobe para verificar cómo Aspose.PDF produce archivos PDF porque Adobe está en el centro de todo lo relacionado con PDF.

{{% /alert %}}

Convierte el archivo usando el método Convert de la clase Document. Antes de convertir el PDF a un archivo compatible con PDF/A, valida el PDF utilizando el método Validate. El resultado de la validación se almacena en un archivo XML y luego este resultado también se pasa al método Convert. También puedes especificar la acción para los elementos que no pueden ser convertidos utilizando la enumeración ConvertErrorAction.
## Convertir archivo PDF a PDF/A-1b

El siguiente fragmento de código muestra cómo convertir archivos PDF a PDF/A-1b compatible.

```cpp
void ConverttoPDFA_1b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.pdf");
    // Cadena para el nombre del archivo de registro
    String logfilename("log.xml");
    // Cadena para el nombre del archivo de salida
    String outfilename("PDFToPDFA_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Convertir a documento compatible con PDF/A
    // Durante el proceso de conversión, también se realiza la validación
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

    // Guardar documento de salida
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Para realizar solo la validación, use la siguiente línea de código:

```cpp
void ConverttoPDFA_1b_Validation()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.pdf");
    // Cadena para el nombre del archivo de registro
    String logfilename("log.xml");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Convertir a documento compatible con PDF/A
    // Durante el proceso de conversión, también se realiza la validación
    document->Validate(_dataDir + logfilename, PdfFormat::PDF_A_1B);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir archivo PDF a PDF/A-3b

Aspose.PDF para C++ también admite la función de convertir un archivo PDF al formato PDF/A-3b.

```cpp
void ConverttoPDFA_3b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.pdf");
    // Cadena para el nombre del archivo de registro
    String logfilename("log.xml");
    // Cadena para el nombre del archivo de salida
    String outfilename("PDFToPDFA3b_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Convertir a documento compatible con PDF/A
    // Durante el proceso de conversión, también se realiza la validación
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3B, ConvertErrorAction::Delete);

    // Guardar documento de salida
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir archivo PDF a PDF/A-2u

Aspose.PDF para C++ también admite la función de convertir un archivo PDF al formato PDF/A-2u.

```cpp
void ConverttoPDFA_2u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.pdf");
    // Cadena para el nombre del archivo de registro
    String logfilename("log.xml");
    // Cadena para el nombre del archivo de salida
    String outfilename("PDFToPDFA3b_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Convertir a documento compatible con PDF/A
    // Durante el proceso de conversión, también se realiza la validación
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // Guardar documento de salida
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir archivo PDF a PDF/A-3u

Aspose.PDF para C++ también admite la función de convertir un archivo PDF al formato PDF/A-3u.

```cpp
void ConverttoPDFA_3u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.pdf");
    // Cadena para el nombre del archivo de registro
    String logfilename("log.xml");
    // Cadena para el nombre del archivo de salida
    String outfilename("PDFToPDFA3b_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Convertir a documento compatible con PDF/A
    // Durante el proceso de conversión, también se realiza la validación
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // Guardar documento de salida
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Añadir adjunto al archivo PDF/A

En caso de que tenga un requisito para adjuntar archivos al formato de cumplimiento PDF/A, recomendamos usar el valor PDF_A_3A de la enumeración Aspose.PDF.PdfFormat.

PDF/A_3a es el formato que proporciona la característica de adjuntar cualquier formato de archivo como un adjunto a un archivo compatible con PDF/A.

```cpp
void ConverttoPDFA_AddAttachment()
{
    std::clog << __func__ << ": Inicio" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.pdf");
    // Cadena para el nombre del archivo de registro
    String logfilename("log.xml");
    // Cadena para el nombre del archivo de salida
    String outfilename("PDFToPDFA3b_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Configurar nuevo archivo para agregar como adjunto
    auto fileSpecification = MakeObject<FileSpecification>(_dataDir + String("aspose-logo.jpg"), String("Archivo de imagen grande"));
    // Agregar adjunto a la colección de adjuntos del documento
    document->get_EmbeddedFiles()->Add(fileSpecification);

    // Convertir a documento compatible con PDF/A
    // Durante el proceso de conversión, también se realiza la validación
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);

    // Guardar documento de salida
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finalizar" << std::endl;
}
```

## Sustituir fuentes faltantes con fuentes alternativas

Según los estándares de PDFA, las fuentes deben estar incrustadas en el documento PDFA. Sin embargo, si las fuentes no están incrustadas en el documento fuente o no existen en la máquina, entonces PDFA falla en la validación. En este caso, tenemos un requisito para sustituir las fuentes faltantes con algunas fuentes alternativas de la máquina. Podemos sustituir las fuentes faltantes usando el método SimpleFontSubsituation de la siguiente manera durante la conversión de PDF a PDFA.

```cpp
void ConverttoPDFA_ReplaceFont()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para el nombre del archivo de entrada
    String infilename("sample.pdf");
    // String para el nombre del archivo de log
    String logfilename("log.xml");
    // String para el nombre del archivo de salida
    String outfilename("PDFToPDFA3b_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    System::SharedPtr<Aspose::Pdf::Text::Font> originalFont;
    try
    {
        originalFont = FontRepository::FindFont(String("AgencyFB"));
    }
    catch (Exception)
    {
        // La fuente falta en la máquina de destino
        auto substitutions = FontRepository::get_Substitutions();
        auto substitution = MakeObject<SimpleFontSubstitution>(String("AgencyFB"), String("Helvetica"));
        substitutions->Add(substitution);
    }

    // Convertir a documento compatible con PDF/A
    try {
        // Durante el proceso de conversión, también se realiza la validación
        document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

        // Guardar documento de salida
        document->Save(_dataDir + outfilename);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="primary" %}}
**Intenta convertir PDF a PDF/A en línea**

Aspose.PDF para C++ te presenta la aplicación en línea gratuita ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a PDF/A con Aplicación Gratuita](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}
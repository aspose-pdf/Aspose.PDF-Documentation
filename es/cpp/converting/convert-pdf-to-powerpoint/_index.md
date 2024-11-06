---
title: Convertir PDF a Microsoft PowerPoint en C++
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: es/cpp/convert-pdf-to-powerpoint/
description: Aspose.PDF te permite convertir PDF a formato PowerPoint usando C++. Existe la posibilidad de convertir PDF a PPTX con diapositivas como imágenes.
lastmod: "2021-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Descripción General

Este artículo explica cómo **convertir PDF a formatos PowerPoint usando C++**. Cubre los siguientes temas.

_Formato_: **PPTX**
- [C++ PDF a PPTX](#cpp-pdf-to-pptx)
- [C++ Convertir PDF a PPTX](#cpp-pdf-to-pptx)
- [C++ Cómo convertir archivo PDF a PPTX](#cpp-pdf-to-pptx)

_Formato_: **Formato Microsoft PowerPoint PPTX**
- [C++ PDF a PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Convertir PDF a PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Cómo convertir archivo PDF a PowerPoint](#cpp-pdf-to-powerpoint-pptx)

Otros temas cubiertos por este artículo.
- [Ver También](#see-also)

## Conversiones de PDF a PowerPoint en C++

**Aspose.PDF para C++** te permite seguir el progreso de la conversión de PDF a PPTX.

Durante la conversión de PDF a <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, el texto se representa como Texto donde puedes seleccionarlo/actualizarlo. Por favor, ten en cuenta que para convertir archivos PDF a formato PPTX, Aspose.PDF proporciona una clase llamada [`PptxSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). Un objeto de la clase PptxSaveOptions se pasa como segundo argumento al método [`Document.Save(..) method`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa). El siguiente fragmento de código muestra el proceso para convertir archivos PDF en formato PPTX.

## Conversión simple de PDF a PPTX con Aspose.PDF para C++

Para convertir PDF a PPTX, Aspose.PDF para C++ aconseja usar los siguientes pasos de código.

<a name="cpp-pdf-to-pptx" id="cpp-pdf-to-pptx"><strong>Pasos: Convertir PDF a PPTX en C++</strong></a> | <a name="cpp-pdf-to-powerpoint-pptx" id="cpp-pdf-to-powerpoint-pptx"><strong>Pasos: Convertir PDF a formato PowerPoint PPTX en C++</strong></a>

1. Crear una instancia de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
2. Crear una instancia de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options).
3. Utilizar el método **Save** del objeto **Document** para _guardar el PDF como PPTX_.

```cpp
void ConvertPDFtoPPTX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Guardar la salida en formato PPTX
    document->Save(_dataDir + outfilename, SaveFormat::Pptx);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir PDF a PPTX con diapositivas como imágenes

En caso de que necesite convertir un PDF con capacidad de búsqueda a PPTX como imágenes en lugar de texto seleccionable, Aspose.PDF proporciona tal característica a través de la clase [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). Para lograr esto, establezca la propiedad [SlidesAsImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) de la clase [PptxSaveOptios](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) a 'true' como se muestra en el siguiente ejemplo de código.

```cpp
void ConvertPDFtoPPTX_SlidesAsImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    pptxOptions->set_SlidesAsImages(true);

    // Guardar la salida en formato PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Detalle del Progreso de la Conversión a PPTX

Aspose.PDF para C++ le permite rastrear el progreso de la conversión de PDF a PPTX. El documento de la clase [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) proporciona la propiedad [CustomProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474) que se puede especificar en un método personalizado para rastrear el progreso de la conversión, como se muestra en el siguiente ejemplo de código.

```cpp
void ConvertPDFtoPPTX_ProgressDetailConversion()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    //pptxOptions->set_SlidesAsImages(true);
    //Especificar el Manejador de Progreso Personalizado
    pptxOptions->set_CustomProgressHandler(ShowProgressOnConsole);

    // Guardar la salida en formato PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Siguiendo está el método personalizado para mostrar la conversión del progreso.

```cpp
void ShowProgressOnConsole(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    switch (eventInfo->EventType)
    {
    case ProgressEventType::TotalProgress:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Progreso de conversión : " << eventInfo->Value << std::endl;
    break;
    case ProgressEventType::ResultPageCreated:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Página de resultados " << eventInfo->Value << " de " << eventInfo->MaxValue << " diseño creado." << std::endl;
    break;
    case ProgressEventType::ResultPageSaved:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Página de resultados " << eventInfo->Value << " de " << eventInfo->MaxValue << " exportada." << std::endl;
    break;
    case ProgressEventType::SourcePageAnalysed:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Página fuente " << eventInfo->Value << " de " << eventInfo->MaxValue << " analizada." << std::endl;
    break;
    default:
    break;
    }
}
```

{{% alert color="success" %}}
**Intenta convertir PDF a PowerPoint en línea**

Aspose.PDF para C++ te presenta una aplicación gratuita en línea ["PDF a PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión de PDF a PPTX con Aplicación Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Ver También

Este artículo también cubre estos temas. Los códigos son los mismos que los anteriores.

_Formato_: **PowerPoint**
- [C++ PDF a Código PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF a API PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF a PowerPoint Programáticamente](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF a Biblioteca PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Guardar PDF como PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Generar PowerPoint desde PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Crear PowerPoint desde PDF](#cpp-pdf-to-powerpoint-pptx)

- [C++ Convertidor de PDF a PowerPoint](#cpp-pdf-to-powerpoint-pptx)

_Format_: **Microsoft PowerPoint PPTX format**
- [C++ PDF a PowerPoint PPTX Código](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF a PowerPoint PPTX API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF a PowerPoint PPTX Programáticamente](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF a PowerPoint PPTX Biblioteca](#cpp-pdf-to-powerpoint-pptx)
- [C++ Guardar PDF como PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)
- [C++ Generar PowerPoint PPTX desde PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Crear PowerPoint PPTX desde PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Convertidor de PDF a PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)

_Format_: **PPTX**
- [C++ PDF a PPTX Código](#cpp-pdf-to-pptx)
- [C++ PDF a PPTX API](#cpp-pdf-to-pptx)
- [C++ PDF a PPTX Programáticamente](#cpp-pdf-to-pptx)
- [C++ PDF a PPTX Biblioteca](#cpp-pdf-to-pptx)
- [C++ Guardar PDF como PPTX](#cpp-pdf-to-pptx)
- [C++ Generar PPTX desde PDF](#cpp-pdf-to-pptx)
- [C++ Crear PPTX desde PDF](#cpp-pdf-to-pptx)
- [C++ Convertidor de PDF a PPTX](#cpp-pdf-to-pptx)
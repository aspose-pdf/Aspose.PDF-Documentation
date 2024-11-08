---
title: Convertir PDF a PowerPoint en .NET
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: /es/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF permite convertir PDF a formato PPT (PowerPoint) usando .NET. Una forma en que existe la posibilidad de convertir PDF a PPTX con Diapositivas como Imágenes.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Resumen

Este artículo explica cómo **convertir PDF a PowerPoint usando C#**. Cubre los siguientes temas.

_Formato_: **PPTX**
- [C# PDF a PPTX](#csharp-pdf-to-pptx)
- [C# Convertir PDF a PPTX](#csharp-pdf-to-pptx)
- [C# Cómo convertir un archivo PDF a PPTX](#csharp-pdf-to-pptx)

_Formato_: **PowerPoint**
- [C# PDF a PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Convertir PDF a PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Cómo convertir un archivo PDF a PowerPoint](#csharp-pdf-to-powerpoint)

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Conversión de PDF a PowerPoint y PPTX en C#
## Conversión de PDF a PowerPoint y PPTX en C#

**Aspose.PDF para .NET** te permite seguir el progreso de la conversión de PDF a PPTX.

Contamos con una API llamada Aspose.Slides que ofrece la funcionalidad de crear y manipular presentaciones PPT/PPTX. Esta API también proporciona la funcionalidad de convertir archivos PPT/PPTX a formato PDF. Recientemente, recibimos requisitos de muchos de nuestros clientes para apoyar la capacidad de transformación de PDF a formato PPTX. A partir de la versión de Aspose.PDF para .NET 10.3.0, hemos introducido una funcionalidad para transformar documentos PDF a formato PPTX. Durante esta conversión, las páginas individuales del archivo PDF se convierten en diapositivas separadas en el archivo PPTX.

Durante la conversión de PDF a <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, el texto se representa como Texto donde puedes seleccionarlo/actualizarlo.
Durante la conversión de PDF a <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, el texto se representa como Texto donde puedes seleccionarlo/actualizarlo.

## Conversión simple de PDF a PowerPoint usando C# y Aspose.PDF .NET

Para convertir un PDF a PPTX, Aspose.PDF para .NET recomienda usar los siguientes pasos de código.

<a name="csharp-pdf-to-powerpoint"><strong>Pasos: Convertir PDF a PowerPoint en C#</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Pasos: Convertir PDF a PPTX en C#</strong></a>

1. Crear una instancia de la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
2. Crear una instancia de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions)
3. Usar el método **Save** del objeto **Document** para guardar el PDF como PPTX

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Cargar documento PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instanciar la clase PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// Guardar la salida en formato PPTX
doc.Save(dataDir + "PDFToPPT_out.pptx", pptx_save);
```
## Convertir PDF a PPTX con diapositivas como imágenes

{{% alert color="success" %}}
**Intenta convertir de PDF a PowerPoint en línea**

Aspose.PDF para .NET te presenta una aplicación gratuita en línea ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), donde puedes explorar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a PPTX con aplicación gratuita](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

En caso de que necesites convertir un PDF buscable a PPTX como imágenes en lugar de texto seleccionable, Aspose.PDF proporciona dicha característica a través de la clase [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions). Para lograr esto, establece la propiedad [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) de la clase [PptxSaveOptios](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) a 'true' como se muestra en el siguiente ejemplo de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Cargar documento PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instanciar la instancia de PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// Guardar la salida en formato PPTX
pptx_save.SlidesAsImages = true;
doc.Save(dataDir + "PDFToPPT_out_.pptx", pptx_save);
```
## Detalle del Progreso de la Conversión de PPTX

Aspose.PDF para .NET te permite rastrear el progreso de la conversión de PDF a PPTX. La clase [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) proporciona la propiedad [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) que se puede especificar a un método personalizado para rastrear el progreso de la conversión como se muestra en el siguiente ejemplo de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Cargar documento PDF
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instanciar la instancia de PptxSaveOptions
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();

//Especificar Manejador de Progreso Personalizado
pptx_save.CustomProgressHandler = ShowProgressOnConsole;
// Guardar la salida en formato PPTX
doc.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", pptx_save);
```
A continuación se presenta el método personalizado para mostrar el progreso de la conversión.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
switch (eventInfo.EventType)
{
    case ProgressEventType.TotalProgress:
        Console.WriteLine(String.Format("{0}  - Progreso de conversión: {1}% .", DateTime.Now.TimeOfDay, eventInfo.Value.ToString()));
        break;
    case ProgressEventType.ResultPageCreated:
        Console.WriteLine(String.Format("{0}  - Página de resultado {1} de {2} layout creada.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.ResultPageSaved:
        Console.WriteLine(String.Format("{0}  - Página de resultado {1} de {2} exportada.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.SourcePageAnalysed:
        Console.WriteLine(String.Format("{0}  - Página fuente {1} de {2} analizada.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));

        break;
    default:
        break;
}
```
## Ver También

Este artículo también cubre estos temas. Los códigos son los mismos que los de arriba.

_Formato_: **PowerPoint**
- [Código C# de PDF a PowerPoint](#csharp-pdf-to-powerpoint)
- [API de C# de PDF a PowerPoint](#csharp-pdf-to-powerpoint)
- [C# PDF a PowerPoint Programáticamente](#csharp-pdf-to-powerpoint)
- [Biblioteca C# PDF a PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Guardar PDF como PowerPoint](#csharp-pdf-to-powerpoint)
- [C# Generar PowerPoint desde PDF](#csharp-pdf-to-powerpoint)
- [C# Crear PowerPoint desde PDF](#csharp-pdf-to-powerpoint)
- [Conversor C# de PDF a PowerPoint](#csharp-pdf-to-powerpoint)

_Formato_: **PPTX**
- [Código C# de PDF a PPTX](#csharp-pdf-to-pptx)
- [API de C# de PDF a PPTX](#csharp-pdf-to-pptx)
- [C# PDF a PPTX Programáticamente](#csharp-pdf-to-pptx)
- [Biblioteca C# PDF a PPTX](#csharp-pdf-to-pptx)
- [C# Guardar PDF como PPTX](#csharp-pdf-to-pptx)
- [C# Generar PPTX desde PDF](#csharp-pdf-to-pptx)
- [C# Crear PPTX desde PDF](#csharp-pdf-to-pptx)
- [Conversor C# de PDF a PPTX](#csharp-pdf-to-pptx)


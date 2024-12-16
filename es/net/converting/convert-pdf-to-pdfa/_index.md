---
title: Convertir formatos PDF a PDF/A
linktitle: Convertir formatos PDF a PDF/A
type: docs
weight: 100
url: /es/net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Este tema te muestra cómo Aspose.PDF permite convertir un archivo PDF en un archivo PDF conforme a PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para .NET** te permite convertir un archivo PDF en un archivo PDF conforme a <abbr title="Portable Document Format / A">PDF/A</abbr>. Antes de hacerlo, el archivo debe ser validado. Este tema explica cómo hacerlo.

{{% alert color="primary" %}}

Ten en cuenta que seguimos Adobe Preflight para validar la conformidad con PDF/A. Todas las herramientas en el mercado tienen su propia "representación" de la conformidad con PDF/A. Por favor, consulta este artículo sobre herramientas de validación de PDF/A para referencia. Elegimos productos de Adobe para verificar cómo Aspose.PDF produce archivos PDF porque Adobe está en el centro de todo lo relacionado con PDF.

{{% /alert %}}

Convierte el archivo utilizando el método Convert de la clase Document.
{{% alert color="success" %}}
**Intenta convertir PDF a PDF/A en línea**

Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF a PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puedes explorar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a PDF/A con aplicación gratuita](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Convertir archivo PDF a PDF/A-1b

El siguiente fragmento de código muestra cómo convertir archivos PDF a PDF compatibles con PDF/A-1b.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Abrir documento
Document pdfDocument = new Document(dataDir + "PDFToPDFA.pdf");
           
// Convertir a documento compatible con PDF/A
// Durante el proceso de conversión, también se realiza la validación
pdfDocument.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA_out.pdf";
// Guardar el documento de salida
pdfDocument.Save(dataDir);
```
Para realizar solo la validación, utiliza la siguiente línea de código:

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validar PDF para PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

## Convertir archivo PDF a formato PDF/A-3b

Aspose.PDF para .NET también admite la función de convertir un archivo PDF al formato PDF/A-3b.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Abrir documento
Document pdfDocument = new Document(dataDir + "input.pdf");           

pdfDocument.Convert(new MemoryStream(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA3b_out.pdf";
// Guardar el documento de salida
pdfDocument.Save(dataDir);
```

## Convertir archivo PDF a formato PDF/A-2u

Aspose.PDF para .NET también soporta la funcionalidad de convertir un archivo PDF a formato PDF/A-2u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_2U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Convertir archivo PDF a formato PDF/A-3u

Aspose.PDF para .NET también soporta la funcionalidad de convertir un archivo PDF a formato PDF/A-3u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Añadir adjunto a archivo PDF/A

En caso de que necesite adjuntar archivos a un formato de cumplimiento PDF/A, entonces recomendamos usar el valor PDF_A_3A de la enumeración Aspose.PDF.PdfFormat.
PDF/A_3a es el formato que proporciona la funcionalidad de adjuntar cualquier formato de archivo como un adjunto a un archivo compatible con PDF/A.

```csharp
## Reemplace las fuentes faltantes con fuentes alternativas

Según los estándares PDFA, las fuentes deben estar incrustadas en el documento PDFA.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instanciar la instancia del Documento para cargar el archivo existente
Aspose.Pdf.Document doc = new Document(dataDir + "input.pdf");
// Configurar nuevo archivo para ser añadido como adjunto
FileSpecification fileSpecification = new FileSpecification(dataDir + "aspose-logo.jpg", "Archivo de imagen grande");
// Añadir adjunto a la colección de adjuntos del documento
doc.EmbeddedFiles.Add(fileSpecification);
// Realizar la conversión a PDF/A_3a para que el adjunto esté incluido en el archivo resultante
doc.Convert(dataDir + "log.txt", Aspose.Pdf.PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
// Guardar el archivo resultante
doc.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
```

type: docs
changefreq: "monthly"
Según los estándares PDFA, las fuentes deben estar incrustadas en el documento PDFA.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Aspose.Pdf.Text.Font originalFont = null;
try
{
    originalFont = FontRepository.FindFont("AgencyFB");
}
catch (Exception)
{
    // La fuente falta en la máquina de destino
    FontRepository.Substitutions.Add(new SimpleFontSubstitution("AgencyFB", "Arial"));
}
var fileNew = new FileInfo(dataDir + "newfile_out.pdf");
var pdf = new Document(dataDir + "input.pdf");
pdf.Convert(dataDir +  "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
pdf.Save(fileNew.FullName);
```

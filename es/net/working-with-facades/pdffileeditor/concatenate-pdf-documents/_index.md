---
title: Concatenate PDF documents in C#
linktitle: Concatenate PDF documents
type: docs
weight: 20
url: es/net/concatenate-pdf-documents/
description: Esta sección explica cómo concatenar documentos PDF con Aspose.PDF Facades usando la clase PdfFileEditor.
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-06-05"
---

## **Resumen**

Este artículo explica cómo fusionar, combinar o concatenar diferentes archivos PDF en un solo PDF usando C#. Cubre temas como

- [C# Fusionar Archivos PDF](#concatenate-pdf-files-using-file-paths)
- [C# Combinar Archivos PDF](#concatenate-pdf-files-using-file-paths)

- [C# Fusionar Múltiples Archivos PDF en uno solo](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Combinar múltiples archivos PDF en un solo PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Unir todos los archivos PDF en una carpeta](#concatenating-all-pdf-files-in-particular-folder)
- [C# Combinar todos los archivos PDF en una carpeta](#concatenating-all-pdf-files-in-particular-folder)
- [C# Unir archivos PDF usando rutas de archivo](#concatenate-pdf-files-using-file-paths)
- [C# Combinar archivos PDF usando streams](#concatenate-array-of-pdf-files-using-streams)
- [C# Concatenar todos los archivos PDF en una carpeta](#concatenate-pdf-files-in-folder)

## Concatenar archivos PDF usando rutas de archivo

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) es la clase en el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) que te permite concatenar múltiples archivos PDF. No solo puedes concatenar archivos usando FileStreams, sino también usando MemoryStreams. En este artículo, se explicará el proceso de concatenación de archivos usando MemoryStreams y luego se mostrará usando el fragmento de código.

El método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) se puede usar para concatenar dos archivos PDF. El método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) te permite pasar tres parámetros: primer PDF de entrada, segundo PDF de entrada y PDF de salida. El PDF de salida final contiene ambos archivos PDF de entrada.

El siguiente fragmento de código C# te muestra cómo concatenar archivos PDF usando rutas de archivo.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

En algunos casos, cuando hay muchos esquemas, los usuarios pueden desactivarlos configurando CopyOutlines en falso y mejorar el rendimiento de la concatenación.
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-CopyOutline.cs" >}}

## Concatenar varios archivos PDF usando MemoryStreams

El método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) toma los archivos PDF de origen y el archivo PDF de destino como parámetros. Estos parámetros pueden ser rutas a los archivos PDF en el disco o pueden ser MemoryStreams. Ahora, para este ejemplo, primero crearemos dos flujos de archivos para leer los archivos PDF desde el disco. Luego convertiremos estos archivos en matrices de bytes. Estas matrices de bytes de los archivos PDF se convertirán en MemoryStreams. Una vez que obtengamos los MemoryStreams de los archivos PDF, podremos pasarlos al método de concatenación y fusionarlos en un único archivo de salida.

El siguiente fragmento de código C# le muestra cómo concatenar varios archivos PDF usando MemoryStreams:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## Concatenar Array de Archivos PDF Usando Rutas de Archivos

Si deseas concatenar múltiples archivos PDF, puedes usar la sobrecarga del método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index), que te permite pasar un array de archivos PDF. El resultado final se guarda como un archivo combinado creado a partir de todos los archivos en el array. El siguiente fragmento de código C# te muestra cómo concatenar un array de archivos PDF usando rutas de archivos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## Concatenar Array de Archivos PDF Usando Streams

Concatenar un array de archivos PDF no se limita solo a archivos que residen en el disco. También puede concatenar un array de archivos PDF desde flujos. Si desea concatenar múltiples archivos PDF, puede usar la sobrecarga apropiada del método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Primero, necesita crear un array de flujos de entrada y un flujo para el PDF de salida y luego llamar al método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). La salida se guardará en el flujo de salida. El siguiente fragmento de código C# le muestra cómo concatenar un array de archivos PDF usando flujos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## Concatenar todos los archivos Pdf en una carpeta específica

Incluso puede leer todos los archivos Pdf en una carpeta específica en tiempo de ejecución y concatenarlos, sin siquiera conocer los nombres de los archivos. Proporcione simplemente la ruta del directorio, que contiene los documentos PDF, que le gustaría concatenar.

Por favor intente usar el siguiente fragmento de código C# para lograr esta funcionalidad.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatingAllPdfFiles-ConcatenatingAllPdfFiles.cs" >}}

## Concatenar formularios PDF y mantener los nombres de los campos únicos

La clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) en el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) ofrece la capacidad de concatenar los archivos PDF. Ahora, si los archivos Pdf que se van a concatenar tienen campos de formulario con nombres de campo similares, Aspose.PDF proporciona la característica para mantener los campos en el archivo Pdf resultante como únicos y también puede especificar el sufijo para hacer que los nombres de los campos sean únicos. La propiedad [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) de [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) como verdadera hará que los nombres de los campos sean únicos cuando los formularios Pdf se concatenen. Además, la propiedad [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) de PdfFileEditor se puede usar para especificar el formato definido por el usuario del sufijo que se agrega al nombre del campo para hacerlo único cuando los formularios se concatenan. Esta cadena debe contener la subcadena `%NUM%` que será reemplazada con números en el archivo resultante.

Por favor, vea el siguiente fragmento de código simple para lograr esta funcionalidad.
## Concatenar archivos PDF y crear Tabla de Contenidos

## Concatenar archivos PDF

Por favor, eche un vistazo al siguiente fragmento de código para obtener información sobre cómo fusionar los archivos PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-ConcatenatePdfFilesAndCreateTOC.cs" >}}

### Insertar página en blanco

Una vez que los archivos PDF han sido fusionados, podemos insertar una página en blanco al principio del documento en la cual se puede crear la Tabla de Contenidos. Para cumplir con este requisito, podemos cargar el archivo fusionado en el objeto **Document** y necesitamos llamar al método Page.Insert(...) para insertar una página en blanco.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}

### Añadir Sellos de Texto

Para crear una Tabla de Contenidos, necesitamos añadir sellos de texto en la primera página usando los objetos [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp). Stamp class proporciona el método `BindLogo(...)` para agregar [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) y también podemos especificar la ubicación para agregar estos sellos de texto usando el método `SetOrigin(..)`. En este artículo, estamos concatenando dos archivos PDF, por lo que necesitamos crear dos objetos de sello de texto que apunten a estos documentos individuales.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

### Crear enlaces locales

Ahora necesitamos agregar enlaces hacia las páginas dentro del archivo concatenado. Para cumplir con este requisito, podemos usar el método `CreateLocalLink(..)` de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). En el siguiente fragmento de código, hemos pasado Transparent como cuarto argumento para que el rectángulo alrededor del enlace no sea visible.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}
### Complete code

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}


## Concatenar archivos PDF en una carpeta

La clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) en el espacio de nombres Aspose.Pdf.Facades le ofrece la capacidad de concatenar el archivo PDF. Incluso puede leer todos los archivos Pdf en una carpeta en particular en tiempo de ejecución y concatenarlos, sin siquiera conocer los nombres de los archivos. Simplemente proporcione la ruta del directorio, que contiene los documentos PDF que le gustaría concatenar.

Intente usar el siguiente fragmento de código C# para lograr esta funcionalidad de Aspose.PDF:

```csharp
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// Recuperar nombres de todos los archivos Pdf en un directorio particular
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// Obtener la fecha del sistema actual y establecer su formato
string date = DateTime.Now.ToString("MM-dd-yyyy");
// Obtener la hora del sistema actual y establecer su formato
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// Establecer el valor para el documento Pdf resultante final
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// Instanciar objeto PdfFileEditor
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// Llamar al método Concatenate del objeto PdfFileEditor para concatenar todos los archivos de entrada
// En un solo archivo de salida
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```
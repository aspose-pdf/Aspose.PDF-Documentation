---
title: Concatenar documentos PDF en C#
linktitle: Concatenar documentos PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/concatenate-pdf-documents/
description: Esta sección explica cómo concatenar documentos PDF con Aspose.PDF Facades utilizando la clase PdfFileEditor.
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Concatenate PDF documents in C#",
    "alternativeHeadline": "Effortlessly Merge PDF Files in C#",
    "abstract": "La funcionalidad en Aspose.PDF for .NET permite a los desarrolladores concatenar eficientemente múltiples documentos PDF utilizando la clase PdfFileEditor en C#. Esta característica admite la fusión de archivos a través de rutas de archivo y MemoryStreams, creando nombres de campo únicos en formularios PDF e incluso generando una tabla de contenido dentro del documento final, proporcionando una solución simplificada para la gestión e integración de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1615",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/concatenate-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/concatenate-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## **Descripción general**

Este artículo explica cómo fusionar, combinar o concatenar diferentes archivos PDF en un solo PDF utilizando C#. Cubre temas como:

- [C# Fusionar archivos PDF](#concatenate-pdf-files-using-file-paths)
- [C# Combinar archivos PDF](#concatenate-pdf-files-using-file-paths)
- [C# Fusionar múltiples archivos PDF en un PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Combinar múltiples archivos PDF en un PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Fusionar todos los archivos PDF en una carpeta](#concatenating-all-pdf-files-in-particular-folder)
- [C# Combinar todos los archivos PDF en una carpeta](#concatenating-all-pdf-files-in-particular-folder)
- [C# Fusionar archivos PDF utilizando rutas de archivo](#concatenate-pdf-files-using-file-paths)
- [C# Combinar archivos PDF utilizando streams](#concatenate-array-of-pdf-files-using-streams)
- [C# Concatenar todos los archivos PDF en la carpeta](#concatenate-pdf-files-in-folder)

## Concatenar archivos PDF utilizando rutas de archivo

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) es la clase en el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) que permite concatenar múltiples archivos PDF. No solo puedes concatenar archivos utilizando FileStreams, sino también utilizando MemoryStreams. En este artículo, se explicará el proceso de concatenar los archivos utilizando MemoryStreams y luego se mostrará utilizando el fragmento de código.

El método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) se puede utilizar para concatenar dos archivos PDF. El método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) permite pasar tres parámetros: primer PDF de entrada, segundo PDF de entrada y PDF de salida. El PDF de salida final contiene ambos archivos PDF de entrada.

El siguiente fragmento de código C# muestra cómo concatenar archivos PDF utilizando rutas de archivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Concatenate files
    pdfEditor.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths2.pdf", dataDir + "ConcatenateUsingPath_out.pdf");
}
```

En algunos casos, cuando hay muchos contornos, los usuarios pueden desactivarlos configurando CopyOutlines en falso y mejorar el rendimiento de la concatenación.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pfe = new Aspose.Pdf.Facades.PdfFileEditor();
    // Setting CopyOutlines to false
    pfe.CopyOutlines = false;
    // Concatenate files
    pfe.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled2.pdf", dataDir + "ConcatenateUsingPath_CopyOutlinesDisabled_out.pdf");
}
```

## Concatenar múltiples archivos PDF utilizando MemoryStreams

El método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) toma los archivos PDF de origen y el archivo PDF de destino como parámetros. Estos parámetros pueden ser rutas a los archivos PDF en el disco o pueden ser MemoryStreams. Ahora, para este ejemplo, primero crearemos dos flujos de archivos para leer los archivos PDF desde el disco. Luego convertiremos estos archivos en arreglos de bytes. Estos arreglos de bytes de los archivos PDF se convertirán en MemoryStreams. Una vez que obtengamos los MemoryStreams de los archivos PDF, podremos pasarlos al método de concatenación y fusionarlos en un solo archivo de salida.

El siguiente fragmento de código C# muestra cómo concatenar múltiples archivos PDF utilizando MemoryStreams:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateMultiplePdfFilesUsingMemoryStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    string document1Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams1.pdf";
    string document2Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams2.pdf";
    string resultPdfPath = dataDir + "concatenated_out.pdf";
    
    // Create two file streams to read PDF files
    using (var fs1 = new FileStream(document1Path, FileMode.Open, FileAccess.Read))
    {
        using (var fs2 = new FileStream(document2Path, FileMode.Open, FileAccess.Read))
        {
            // Create byte arrays to keep the contents of PDF files
            var buffer1 = new byte[Convert.ToInt32(fs1.Length)];
            var buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            var i = 0;
            // Read PDF file contents into byte arrays
            i = fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            i = fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Now, first convert byte arrays into MemoryStreams and then concatenate those streams
            using (var pdfStream = new MemoryStream())
            {
                using (var fileStream1 = new MemoryStream(buffer1))
                {
                    using (var fileStream2 = new MemoryStream(buffer2))
                    {
                        // Create instance of PdfFileEditor class to concatenate streams
                        var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                        // Concatenate both input MemoryStreams and save to output MemoryStream
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convert MemoryStream back to byte array
                        var data = pdfStream.ToArray();
                        // Create a FileStream to save the output PDF file
                        using (var output = new FileStream(resultPdfPath, FileMode.Create, FileAccess.Write))
                        {
                            // Write byte array contents in the output file stream
                            output.Write(data, 0, data.Length);
                        }
                    }
                }
            }
        }
    }
}
```

## Concatenar arreglo de archivos PDF utilizando rutas de archivo

Si deseas concatenar múltiples archivos PDF, puedes utilizar la sobrecarga del método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index), que te permite pasar un arreglo de archivos PDF. La salida final se guarda como un archivo fusionado creado a partir de todos los archivos en el arreglo. El siguiente fragmento de código C# muestra cómo concatenar un arreglo de archivos PDF utilizando rutas de archivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of files
    var filesArray = new string[2];
    filesArray[0] = dataDir + "Concatenate1.pdf";
    filesArray[1] = dataDir + "Concatenate2.pdf";
    // Concatenate files
    pdfEditor.Concatenate(filesArray, dataDir + "ConcatenateArrayOfPdfFilesUsingFilePaths_out.pdf");
}
```

## Concatenar arreglo de archivos PDF utilizando streams

La concatenación de un arreglo de archivos PDF no se limita solo a archivos que residen en el disco. También puedes concatenar un arreglo de archivos PDF desde streams. Si deseas concatenar múltiples archivos PDF, puedes utilizar la sobrecarga apropiada del método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Primero, necesitas crear un arreglo de streams de entrada y un stream para el PDF de salida y luego llamar al método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). La salida se guardará en el stream de salida. El siguiente fragmento de código C# muestra cómo concatenar un arreglo de archivos PDF utilizando streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    var document1Path = dataDir + "Concatenate1.pdf";
    var document2Path = dataDir + "Concatenate2.pdf";
    var resultPdfPath = dataDir + "ConcatenateArrayOfPdfUsingStreams_out.pdf";

    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Output stream
    using (var outputStream = new FileStream(resultPdfPath, FileMode.Create))
    {
        using (var stream1 = new FileStream(document1Path, FileMode.Open))
        {
            using (var stream2 = new FileStream(document2Path, FileMode.Open))
            {
                // Array of streams
                var inputStreams = new Stream[2];
                inputStreams[0] = stream1;
                inputStreams[1] = stream2;
                // Concatenate file
                pdfEditor.Concatenate(inputStreams, outputStream);
            }   
        }
    }
}
```

## Concatenar todos los archivos PDF en una carpeta particular

Incluso puedes leer todos los archivos PDF en una carpeta particular en tiempo de ejecución y concatenarlos, sin siquiera conocer los nombres de los archivos. Simplemente proporciona la ruta del directorio que contiene los documentos PDF que deseas concatenar.

Por favor, intenta utilizar el siguiente fragmento de código C# para lograr esta funcionalidad.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatingAllPdfFilesInParticularFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    var fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    var resultPdfPath = dataDir + "ConcatenatingAllPdfFilesInParticularFolder_out.pdf";
    // Instantiate PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, resultPdfPath);
}
```

## Concatenar formularios PDF y mantener nombres de campos únicos

La clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) en el [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) ofrece la capacidad de concatenar los archivos PDF. Ahora, si los archivos PDF que se van a concatenar tienen campos de formulario con nombres de campo similares, Aspose.PDF proporciona la función de mantener los campos en el archivo PDF resultante como únicos y también puedes especificar el sufijo para hacer que los nombres de los campos sean únicos. La propiedad [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) de [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) como verdadero hará que los nombres de los campos sean únicos cuando se concatenen formularios PDF. Además, la propiedad [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) de PdfFileEditor se puede utilizar para especificar el formato definido por el usuario del sufijo que se agrega al nombre del campo para hacerlo único cuando se concatenan formularios. Esta cadena debe contener la subcadena `%NUM%` que será reemplazada por números en el archivo resultante.

Por favor, consulta el siguiente fragmento de código simple para lograr esta funcionalidad.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFormsAndKeepFieldsUnique()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique1.pdf";
    var inputFile2 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique2.pdf";
    var outFile = dataDir + "ConcatenatePDFForms_out.pdf";
    // Open PDF documents
    var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // To keep unique field Id for all the fields 
    fileEditor.KeepFieldsUnique = true;
    // Format of the suffix which is added to field name to make it unique when forms are concatenated.
    fileEditor.UniqueSuffix = "_%NUM%";
    // Concatenate the files into a resultant Pdf file
    fileEditor.Concatenate(inputFile1, inputFile2, outFile);
}
```

## Concatenar archivos PDF y crear tabla de contenido

## Concatenar archivos PDF

Por favor, echa un vistazo al siguiente fragmento de código para obtener información sobre cómo fusionar los archivos PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFiles()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenateInput1.pdf";
    var inputFile2 = dataDir + "ConcatenateInput2.pdf";
    var outFile = dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf";
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();

    // Open PDF documents
    using (var outputStream = new FileStream(outFile, FileMode.Create))
    {
        using (var stream1 = new FileStream(inputFile1, FileMode.Open))
        {
            using (var stream2 = new FileStream(inputFile2, FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(stream1, stream2, outputStream);
            }
        }
    }
}
```

### Insertar página en blanco

Una vez que los archivos PDF se han fusionado, podemos insertar una página en blanco al principio del documento en la que podemos crear la tabla de contenido. Para lograr este requisito, podemos cargar el archivo fusionado en un objeto **Document** y necesitamos llamar al método Page.Insert(...) para insertar una página en blanco.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertBlankPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Insert a blank page at the beginning of concatenated file to display Table of Contents
    using (var document = new Aspose.Pdf.Document(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf"))
    {
        // Insert a blank page in a PDF
        document.Pages.Insert(1);
    }
}
```

### Agregar sellos de texto

Para crear una tabla de contenido, necesitamos agregar sellos de texto en la primera página utilizando [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) y objetos [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp). La clase Stamp proporciona el método `BindLogo(...)` para agregar [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) y también podemos especificar la ubicación para agregar estos sellos de texto utilizando el método `SetOrigin(..)`. En este artículo, estamos concatenando dos archivos PDF, por lo que necesitamos crear dos objetos de sello de texto que apunten a estos documentos individuales.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampForTableOfContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    var inputPdfFile = Path.Combine(dataDir, "ConcatenateInput1.pdf");
    // Set Text Stamp to display string Table Of Contents
    var stamp = new Aspose.Pdf.Facades.Stamp();
    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent, Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(inputPdfFile).GetPageWidth(1) / 3, 700);
    // Set particular pages
    stamp.Pages = new[] { 1 };
}
```

### Crear enlaces locales

Ahora necesitamos agregar enlaces hacia las páginas dentro del archivo concatenado. Para lograr este requisito, podemos utilizar el método `CreateLocalLink(..)` de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). En el siguiente fragmento de código, hemos pasado Transparent como el cuarto argumento para que el rectángulo alrededor del enlace no sea visible.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLocalLinks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Now we need to add Heading for Table Of Contents and links for documents
    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
    // Bind PDF document
    contentEditor.BindPdf(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf");
    // Create link for first document
    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
}
```

### Código completo

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CompleteCode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create a MemoryStream object to hold the resultant PDf file
    using (var concatenatedStream = new MemoryStream())
    {
        using (var fs1 = new FileStream(dataDir + "ConcatenateInput1.pdf", FileMode.Open))
        {
            using (var fs2 = new FileStream(dataDir + "ConcatenateInput2.pdf", FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(fs1, fs2, concatenatedStream);
            }
        }

        using (var concatenatedPdfDocument = new Aspose.Pdf.Document(concatenatedStream))
        {
            // Insert a blank page at the beginning of concatenated file to display Table of Contents
            concatenatedPdfDocument.Pages.Insert(1);

            // Hold the result file with empty page added
            using (var documentWithBlankPage = new MemoryStream())
            {
                // Save PDF document
                concatenatedPdfDocument.Save(documentWithBlankPage);

                using (var documentWithTocHeading = new MemoryStream())
                {
                    // Add Table Of Contents logo as stamp to PDF file
                    var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp();
                    // Bind PDF document
                    fileStamp.BindPdf(documentWithBlankPage);

                    // Set Text Stamp to display string Table Of Contents
                    var stamp = new Aspose.Pdf.Facades.Stamp();
                    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(documentWithBlankPage).GetPageWidth(1) / 3, 700);
                    // Set particular pages
                    stamp.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(stamp);

                    // Create stamp text for first item in Table Of Contents
                    var document1Link = new Aspose.Pdf.Facades.Stamp();
                    document1Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("1 - Link to Document 1", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document1Link.SetOrigin(150, 650);
                    // Set particular pages on which stamp should be displayed
                    document1Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document1Link);

                    // Create stamp text for second item in Table Of Contents
                    var document2Link = new Aspose.Pdf.Facades.Stamp();
                    document2Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("2 - Link to Document 2", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document2Link.SetOrigin(150, 620);
                    // Set particular pages on which stamp should be displayed
                    document2Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document2Link);

                    // Save PDF document
                    fileStamp.Save(documentWithTocHeading);
                    fileStamp.Close();

                    // Now we need to add Heading for Table Of Contents and links for documents
                    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
                    // Bind PDF document
                    contentEditor.BindPdf(documentWithTocHeading);
                    // Create link for first document
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
                    // Create link for Second document
                    // We have used   new PdfFileInfo("d:/pdftest/Input1.pdf").NumberOfPages + 2   as PdfFileInfo.NumberOfPages(..) returns the page count for first document
                    // And 2 is because, second document will start at Input1+1 and 1 for the page containing Table Of Contents.
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 620, 100, 20),
                        new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "ConcatenateInput1.pdf").NumberOfPages + 2, 1, System.Drawing.Color.Transparent);
                    // Save PDF document
                    contentEditor.Save(dataDir + "Concatenated_Table_Of_Contents_out.pdf");
                }
            }
        }
    }
}
```

## Concatenar archivos PDF en carpeta

La clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) en el espacio de nombres Aspose.Pdf.Facades te ofrece la capacidad de concatenar el archivo PDF. Incluso puedes leer todos los archivos PDF en una carpeta particular en tiempo de ejecución y concatenarlos, sin siquiera conocer los nombres de los archivos. Simplemente proporciona la ruta del directorio que contiene los documentos PDF que deseas concatenar.

Por favor, intenta utilizar el siguiente fragmento de código C# para lograr esta funcionalidad desde Aspose.PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesInFolder()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, dataDir + "ConcatenatePdfFilesInFolder_out.pdf");
}
```
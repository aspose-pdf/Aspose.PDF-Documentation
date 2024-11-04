---
title: Adding Attachment to PDF document
linktitle: Adding Attachment to PDF document 
type: docs
weight: 10
url: /cpp/add-attachment-to-pdf-document/
description: Esta página describe cómo agregar un adjunto a un archivo PDF con la biblioteca Aspose.PDF para C++
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los adjuntos pueden contener una amplia variedad de información y pueden ser de varios tipos de archivos. Este artículo explica cómo agregar un adjunto a un archivo PDF.

1. Crea un nuevo proyecto de C++.
1. Agrega una referencia a la DLL de Aspose.PDF.
1. Crea un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Crea un objeto [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) con el archivo que estás agregando y la descripción del archivo.
1. Añade el objeto [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) a la colección [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), con el método Add de la colección.

La colección [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) contiene todos los archivos adjuntos en el archivo PDF. El siguiente fragmento de código te muestra cómo añadir un archivo adjunto en un documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithAttachments::AddingAttachment()
{

String _dataDir("C:\\Samples\\");


// Abre el documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddAttachment.pdf");


// Configura el nuevo archivo para ser añadido como adjunto

auto fileSpecification = MakeObject<FileSpecification>(_dataDir + u"test.txt", u"Archivo de texto de muestra");


// Añade el adjunto a la colección de archivos adjuntos del documento

pdfDocument->get_EmbeddedFiles()->Add(fileSpecification);


// Guarda la nueva salida

pdfDocument->Save(_dataDir + u"AddAttachment_out.pdf");
}
```
---
title: Crear Enlaces en un archivo PDF con C++
linktitle: Crear Enlaces
type: docs
weight: 10
url: /cpp/create-links/
description: Esta sección explica cómo crear enlaces en su documento PDF con C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Crear Enlaces

Al agregar un enlace a una aplicación en un documento, es posible enlazar a aplicaciones desde un documento. Esto es útil cuando desea que los lectores realicen una acción específica en un punto específico en un tutorial, por ejemplo, o para crear un documento rico en funciones. Para crear un enlace de aplicación:

1. [Cree un Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) objeto.
1. Obtenga la [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) a la que desea agregar el enlace.
1. Cree un objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) utilizando los objetos Page y [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. Establezca los atributos del enlace utilizando el objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).  
1. Además, establezca la propiedad Action del objeto [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/).  
1. Al crear el objeto [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/), especifique la aplicación que desea iniciar.  
1. Agregue el enlace a la propiedad [Annotations](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.annotations) del objeto Page.  
1. Finalmente, guarde el PDF actualizado utilizando el método Save del objeto Document.  

El siguiente fragmento de código muestra cómo crear un enlace a una aplicación en un archivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;

void CreateLink() 
{
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Document
    auto document = MakeObject<Document>(_dataDir + u"CreateApplicationLink.pdf");

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::LaunchAction>(document, _dataDir + u"sample.pdf"));
    page->get_Annotations()->Add(link);

    // Guardar documento actualizado
    document->Save(_dataDir + u"CreateApplicationLink.pdf");
}
```
### Crear Enlace de Documento PDF en un Archivo PDF

Aspose.PDF para C++ te permite agregar un enlace a un archivo PDF externo para que puedas vincular varios documentos juntos. Para crear un enlace de documento PDF:

1. Primero, crea un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Luego, obtén la [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) particular a la que deseas agregar el enlace.
1. Crea un objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) utilizando los objetos Page y [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. Establece los atributos del enlace usando el objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).
1. Establece la propiedad Action al objeto [GoToRemoteAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_remote_action/).
1. Al crear el objeto GoToRemoteAction, especifique el archivo PDF que debería lanzarse, así como el número de página en el que debería abrirse.
1. Añada el enlace a la colección de Anotaciones del objeto Page.
1. Guarde el PDF actualizado utilizando el método Save del objeto Document.

El siguiente fragmento de código muestra cómo crear un enlace de documento PDF en un archivo PDF.

```cpp
void CreatePDFDocumentLink() 
{

    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"CreateDocumentLink.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);


    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());

    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToRemoteAction>(_dataDir + u"sample.pdf", 1));
    page->get_Annotations()->Add(link);

    // Save updated document
    document->Save(_dataDir + u"CreateDocumentLink_out.pdf");
}
```
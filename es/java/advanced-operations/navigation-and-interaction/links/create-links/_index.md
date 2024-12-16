---
title: Crear Enlaces en un Archivo PDF
linktitle: Crear Enlaces
type: docs
weight: 10
url: /es/java/create-links/
description: Esta sección explica cómo crear enlaces en su documento PDF con Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Crear Enlaces

Aspose.PDF para Java le permite agregar un enlace a un archivo PDF externo para que pueda vincular varios documentos juntos.
Al agregar un enlace a una aplicación en un documento, es posible vincular aplicaciones desde un documento. Esto es útil cuando desea que los lectores realicen una cierta acción en un punto específico de un tutorial, por ejemplo, o para crear un documento rico en funciones. Para crear un enlace de aplicación:

1. [Cree un objeto Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Obtenga la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) a la que desea agregar el enlace.

1. Cree un objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) usando los objetos [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) y [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. Establezca los atributos del enlace usando el objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. Además, configure el objeto [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) y llame al método setAction(..).
1. Al crear el objeto [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction), especifique la aplicación que desea lanzar.
1. Agregue el enlace a la colección [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) del objeto Page.
1. Finalmente, guarde el PDF actualizado usando el método Save del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

El siguiente fragmento de código muestra cómo crear un enlace a una aplicación en un archivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;


public class ExampleLinks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Links-Actions";
        return _dataDir;
    }

    public static void CreateLink() {

        // Abrir documento
        Document document = new Document(GetDataDir() + "CreateApplicationLink.pdf");

        // Crear enlace
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, _dataDir + "sample.pdf"));
        page.getAnnotations().add(link);

        // Guardar documento actualizado
        document.save(_dataDir + "CreateApplicationLink_out.pdf");
    }
```

### Crear enlace de documento PDF en un archivo PDF

Aspose.PDF para Java te permite agregar un enlace a un archivo PDF externo para que puedas vincular varios documentos juntos.
 Para crear un enlace de documento PDF:

1. Primero, crea un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Luego, obtén la [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) particular a la que deseas agregar el enlace.
1. Crea un objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) usando los objetos [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) y [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. Establece los atributos del enlace usando el objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. Llama al método setAction(..) y pasa un objeto [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction).
1. Al crear el objeto [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction), especifica el archivo PDF que debe lanzarse, así como el número de página en la que debe abrirse.
1. Agrega el enlace a la colección [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) del objeto Page.
1. Finalmente, guarda el PDF actualizado usando el método Save del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

El siguiente fragmento de código muestra cómo crear un enlace de documento PDF en un archivo PDF.

```java
    public static void CreatePDFDocumentLink() {

        // Abrir documento
        Document document = new Document(_dataDir + "CreateDocumentLink.pdf");

        // Crear enlace
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(_dataDir + "sample.pdf", 1));
        page.getAnnotations().add(link);

        // Guardar documento actualizado
        document.save(_dataDir + "CreateDocumentLink_out.pdf");
    }
```
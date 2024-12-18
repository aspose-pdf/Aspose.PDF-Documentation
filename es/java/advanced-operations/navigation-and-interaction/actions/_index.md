---
title: Trabajando con Acciones 
linktitle: Acciones
type: docs
weight: 20
url: /es/java/actions/
description: Esta sección explica cómo agregar acciones a los documentos y campos de formulario programáticamente con Java. Aprenda cómo Añadir, Crear y Obtener un Hipervínculo en un Archivo PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Un archivo PDF puede contener archivos adjuntos integrados y a menudo es necesario hipervincular a estos documentos. Puede dirigir a los lectores desde el documento PDF principal a un archivo adjunto PDF creando un enlace en el documento principal que apunte al adjunto.

## Añadir Hipervínculo en un Archivo PDF

Es posible añadir hipervínculos a archivos PDF, ya sea para permitir que los lectores naveguen a otra parte del PDF o a contenido externo.

Para añadir hipervínculos web a documentos PDF:

1. Cree un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Obtén la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) a la que deseas añadir el enlace.
1. Crea un objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) utilizando los objetos Page y [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle). El objeto rectangle se utiliza para especificar la ubicación en la página donde se debe añadir el enlace.
1. Establece el método getAction en el objeto [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToURIAction) que especifica la ubicación del URI remoto.
1. Para mostrar un texto de hipervínculo, añade una cadena de texto en una ubicación similar a donde se coloca el objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation).
1. Para añadir un texto libre:

- Instancia un objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation).
 También acepta objetos Page y Rectangle como argumento, por lo que es posible proporcionar los mismos valores que se especifican en el constructor de LinkAnnotation.
- Usando la propiedad Contents del objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation), especifica la cadena que debe mostrarse en el PDF de salida.
- Opcionalmente, establece el ancho del borde de ambos objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) y FreeTextAnnotation a 0 para que no aparezcan en el documento PDF.
- Una vez que los objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) y [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) han sido definidos, agrega estos enlaces a la colección Annotations del objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

- Finalmente, guarda el PDF actualizado usando el método Save del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
El siguiente fragmento de código te muestra cómo agregar un hipervínculo a un archivo PDF.

```java
package com.aspose.pdf.examples;

import java.util.List;

import com.aspose.pdf.*;

public class ExampleActions {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Actions/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Actions";
        return _dataDir;
    }

    public static void AddHyperlinkInPDFFile() {
        // Abrir documento
        Document document = new Document(GetDataDir() + "AddHyperlink.pdf");
        // Crear enlace
        Page page = document.getPages().get_Item(1);
        // Crear objeto de anotación de enlace
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 100, 300, 300));
        // Crear objeto de borde para LinkAnnotation
        Border border = new Border(link);
        // Establecer el valor del ancho del borde como 0
        border.setWidth(0);
        // Establecer el borde para LinkAnnotation
        link.setBorder(border);
        // Especificar el tipo de enlace como URI remoto
        link.setAction(new GoToURIAction("www.aspose.com"));
        // Agregar anotación de enlace a la colección de anotaciones de la primera página del archivo PDF
        page.getAnnotations().add(link);

        // Crear anotación de texto libre
        FreeTextAnnotation textAnnotation = new FreeTextAnnotation(page, new Rectangle(100, 100, 300, 300),
                new DefaultAppearance(FontRepository.findFont("TimesNewRoman"), 10, java.awt.Color.BLUE));

        // Cadena a ser añadida como texto libre
        textAnnotation.setContents("Enlace al sitio web de Aspose");
        // Establecer el borde para la anotación de texto libre
        textAnnotation.setBorder(border);
        // Agregar anotación de texto libre a la colección de anotaciones de la primera página del documento
        page.getAnnotations().add(textAnnotation);

        // Guardar documento actualizado
        document.save(_dataDir + "AddHyperlink_out.pdf");

    }
```


## Crear Hipervínculo a páginas en el mismo PDF

Aspose.PDF para Java proporciona una gran función para la creación de PDF así como su manipulación. También ofrece la función de agregar enlaces a páginas PDF y un enlace puede dirigir a páginas en otro archivo PDF, una URL web, un enlace para lanzar una aplicación o incluso un enlace a páginas en el mismo archivo PDF.

Para agregar el hipervínculo local, necesitamos crear un TextFragment para que el enlace pueda asociarse con el TextFragment. La clase [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) tiene un método llamado [getHyperlink](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#getHyperlink--) que se utiliza para asociar una instancia de LocalHyperlink. El siguiente fragmento de código muestra los pasos para cumplir con este requisito.

```java
public static void CreateHyperlinkToPagesInSamePDF() {
        // Crear instancia de Documento
        Document document = new Document();

        // Agregar página a la colección de páginas del archivo PDF
        Page page = document.getPages().add();

        // Crear instancia de Fragmento de Texto
        TextFragment text = new TextFragment("prueba de enlace al número de página a la página 2");

        // Crear instancia de hipervínculo local
        LocalHyperlink link = new LocalHyperlink();

        // Establecer página de destino para la instancia de enlace
        link.setTargetPageNumber(2);

        // Establecer hipervínculo para el Fragmento de Texto
        text.setHyperlink(link);

        // Agregar texto a la colección de párrafos de la página
        page.getParagraphs().add(text);

        // Crear nueva instancia de Fragmento de Texto
        text = new TextFragment("prueba de enlace al número de página a la página 1");

        // El Fragmento de Texto debe agregarse en una nueva página
        text.setInNewPage(true);

        // Crear otra instancia de hipervínculo local
        link = new LocalHyperlink();

        // Establecer página de destino para el segundo hipervínculo
        link.setTargetPageNumber(1);

        // Establecer enlace para el segundo Fragmento de Texto
        text.setHyperlink(link);

        // Agregar texto a la colección de párrafos del objeto página
        page.getParagraphs().add(text);

        // Guardar documento actualizado
        document.save(GetDataDir() + "CreateLocalHyperlink_out.pdf");
    }
```


## Obtener el Destino del Hipervínculo en PDF (URL)

Los enlaces están representados como anotaciones en un archivo PDF y se pueden agregar, actualizar o eliminar. Aspose.PDF para Java también admite obtener el destino (URL) del hipervínculo en un archivo PDF.

Para obtener la URL de un enlace:

1. Crear un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Obtener la [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) de la que desea extraer enlaces.
1. Usar la clase [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) para extraer todos los objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation)) de la página especificada.
1. Pasar el objeto [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) al método Accept del objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

1. Obtén todas las anotaciones de enlace seleccionadas en un objeto IList usando la propiedad Selected del objeto [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector).
2. Finalmente, extrae la Acción de LinkAnnotation como GoToURIAction.

El siguiente fragmento de código muestra cómo obtener destinos de hipervínculos (URL) de un archivo PDF.

```java
    public static void GetPDFHyperlinkDestination() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Extraer acciones
        Page page = document.getPages().get_Item(1);
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        List<Annotation> list = selector.getSelected();
        // Iterar a través de cada elemento dentro de la lista
        if (list.size() == 0)
            System.out.println("No se encontraron hipervínculos..");
        else {
            // Recorrer todos los marcadores
            for (Annotation annot : list) {
                LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
                if (la != null) {
                    // Imprimir la URL de destino
                    System.out.println("Destino: " + ((GoToURIAction) la.getAction()).getURI());
                }
            }
        } // fin del else
    }
```


## Obtener Texto del Hipervínculo

Un hipervínculo tiene dos partes: el texto que se muestra en el documento y la URL de destino. En algunos casos, lo que necesitamos es el texto en lugar de la URL.

El texto y las anotaciones/acciones en un archivo PDF están representados por diferentes entidades. El texto en una página es solo un conjunto de palabras y caracteres, mientras que las anotaciones aportan cierta interactividad, como la inherente a un hipervínculo.

Para encontrar el contenido de la URL, necesitas trabajar tanto con la anotación como con el texto. El objeto [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/Annotation) no tiene el texto por sí mismo, sino que se encuentra bajo el texto en la página. Así que para obtener el texto, la Anotación proporciona los límites de la URL, mientras que el objeto Texto proporciona los contenidos de la URL. Por favor, vea el siguiente fragmento de código.

```java
    public static void GetHyperlinkText() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Extraer acciones
        Page page = document.getPages().get_Item(1);

        for (Annotation annot : page.getAnnotations()) {
            LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
            if (la != null) {
                // Imprimir la URL de cada Anotación de Enlace
                System.out.println("URI: " + ((GoToURIAction) la.getAction()).getURI());
                TextAbsorber absorber = new TextAbsorber();
                absorber.getTextSearchOptions().setLimitToPageBounds(true);
                absorber.getTextSearchOptions().setRectangle(annot.getRect());
                page.accept(absorber);
                String extractedText = absorber.getText();
                // Imprimir el texto asociado con el hipervínculo
                System.out.println(extractedText);
            }
        }
    }
```


## Eliminar la Acción de Abrir Documento de un Archivo PDF

[Cómo Especificar la Página PDF al Ver el Documento](#how-to-specify-pdf-page-when-viewing-document) explicó cómo indicar a un documento que se abra en una página diferente a la primera. Al concatenar varios documentos, y uno o más tienen una acción GoTo configurada, probablemente querrás eliminarlos. Por ejemplo, si combinas dos documentos y el segundo tiene una acción GoTo que te lleva a la segunda página, el documento resultante se abrirá en la segunda página del segundo documento en lugar de la primera página del documento combinado. Para evitar este comportamiento, elimina el comando de acción de apertura.

Para eliminar una acción de apertura:

1. Establece el método [getOpenAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getOpenAction--) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) en null.
2. Guarda el PDF actualizado usando el método Save del objeto Document.

El siguiente fragmento de código muestra cómo eliminar una acción de apertura de documento del archivo PDF.

```java
    public static void RemoveDocumentOpenActionFromPDFFile()
    {
        // Abrir documento
        Document document = new Document(_dataDir + "RemoveOpenAction.pdf");
        // Eliminar la acción de apertura del documento
        document.setOpenAction(null);
        
        // Guardar documento actualizado
        document.save(GetDataDir()+"RemoveOpenAction_out.pdf");
    }
```


## Cómo Especificar la Página PDF al Ver el Documento {#how-to-specify-pdf-page-when-viewing-document}

Al ver archivos PDF en un visor de PDF como Adobe Reader, los archivos generalmente se abren en la primera página. Sin embargo, es posible configurar el archivo para que se abra en una página diferente.

La clase [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) te permite especificar una página en un archivo PDF que deseas abrir. Al pasar el valor del objeto GoToAction al método getOpenAction de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), el documento se abre en la página especificada contra el objeto XYZExplicitDestination. El siguiente fragmento de código muestra cómo especificar una página como la acción de apertura del documento.

```java
    public static void HowToSpecifyPDFPageWhenViewingDocument()
    {
        // Cargar el archivo PDF
        Document document = new Document(GetDataDir()+ "SpecifyPageWhenViewing.pdf");
        // Obtener la instancia de la segunda página del documento
        Page page2 = document.getPages().get_Item(2);
        // Crear la variable para establecer el factor de zoom de la página objetivo
        double zoom = 1;
        // Crear instancia de GoToAction
        GoToAction action = new GoToAction(page2);
        // Ir a la página 2
        action.setDestination (new XYZExplicitDestination(page2, 0, page2.getRect().getHeight(), zoom));
        // Establecer la acción de apertura del documento
        document.setOpenAction (action);
        // Guardar documento actualizado
        document.save(_dataDir + "goto2page_out.pdf");
    }
}
```
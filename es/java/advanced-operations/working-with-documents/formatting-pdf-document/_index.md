---
title: Formatting PDF Document 
linktitle: Formatting PDF Document
type: docs
weight: 20
url: /es/java/formatting-pdf-document/
description: Formatear el Documento PDF con Aspose.PDF para Java. Use el siguiente fragmento de código para resolver sus tareas.
lastmod: "2021-06-05"
---

## Obtener las Propiedades de Ventana de Documento y Visualización de Página

Este tema le ayuda a entender cómo obtener las propiedades de la ventana del documento, la aplicación del visor y cómo se muestran las páginas.

Para configurar estas diferentes propiedades, abra el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Ahora puede obtener los métodos del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), tales como

- [IsCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Centrar la ventana del documento en la pantalla. Predeterminado: false.
- [SetDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Orden de lectura.
 Esto determina cómo se disponen las páginas cuando se muestran lado a lado. Predeterminado: de izquierda a derecha.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Mostrar el título del documento en la barra de título de la ventana del documento. Predeterminado: false (el título se muestra).
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-) – Ocultar o mostrar la barra de menú de la ventana del documento. Predeterminado: false (la barra de menú se muestra).
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-) – Ocultar o mostrar la barra de herramientas de la ventana del documento. Predeterminado: false (la barra de herramientas se muestra).
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-) – Ocultar o mostrar elementos de la ventana del documento como las barras de desplazamiento. Predeterminado: false (los elementos de la UI se muestran).

- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-) – Cómo se muestra el documento cuando no se muestra en modo de página completa.- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-) – El diseño de la página.
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-) – Cómo se muestra el documento cuando se abre por primera vez. Las opciones son mostrar miniaturas, pantalla completa, mostrar panel de adjuntos.

El siguiente fragmento de código le muestra cómo obtener las propiedades utilizando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleFormatting {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void GetDocumentWindowAndPageDisplayProperties() {

    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Obtener diferentes propiedades del documento
    // Posición de la ventana del documento - Predeterminado: false
    System.out.printf("CenterWindow : " + pdfDocument.isCenterWindow());

    // Orden de lectura predominante; determinar la posición de la página
    // cuando se muestra lado a lado - Predeterminado: L2R
    System.out.printf("Direction :- " + pdfDocument.getDirection());

    // Si la barra de título de la ventana debe mostrar el título del documento.
    // Si es falso, la barra de título muestra el nombre del archivo PDF - Predeterminado: false
    System.out.printf("DisplayDocTitle :- " + pdfDocument.isDisplayDocTitle());

    // Si se debe redimensionar la ventana del documento para ajustar el tamaño de
    // la primera página mostrada - Predeterminado: false
    System.out.printf("FitWindow :- " + pdfDocument.isFitWindow());

    // Si se debe ocultar la barra de menú de la aplicación del visor - Predeterminado: false
    System.out.printf("HideMenuBar :-" + pdfDocument.isHideMenubar());

    // Si se debe ocultar la barra de herramientas de la aplicación del visor - Predeterminado: false
    System.out.printf("HideToolBar :-" + pdfDocument.isHideToolBar());

    // Si se deben ocultar elementos de la interfaz de usuario como barras de desplazamiento
    // dejando solo visibles los contenidos de la página - Predeterminado: false
    System.out.printf("HideWindowUI :-" + pdfDocument.isHideWindowUI());

    // El modo de página del documento. Cómo mostrar el documento al salir
    // del modo de pantalla completa.
    System.out.printf("NonFullScreenPageMode :-" + pdfDocument.getNonFullScreenPageMode());

    // El diseño de página, es decir, página única, una columna
    System.out.printf("PageLayout :-" + pdfDocument.getPageLayout());

    // Cómo debe mostrarse el documento cuando se abre.
    System.out.printf("pageMode :-" + pdfDocument.getPageMode());

  }

```

## Establecer Propiedades de la Ventana del Documento y la Visualización de la Página

Este tema explica cómo establecer las propiedades de la ventana del documento, la aplicación del visor y la visualización de la página.

Para establecer estas diferentes propiedades:

1. Abra el archivo PDF utilizando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Establezca las propiedades del objeto Document.
1. Guarde el archivo PDF actualizado utilizando el método Save.

Las propiedades disponibles son:

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

El siguiente fragmento de código le muestra cómo establecer las propiedades utilizando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
  public static void SetDocumentWindowAndPageDisplayProperties() {

    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    
    // Establecer diferentes propiedades del documento
    // especificar para posicionar la ventana del documento - Predeterminado: false
    pdfDocument.setCenterWindow(true);
    
    // Orden de lectura predominante; determinar la posición de la página
    // cuando se muestra lado a lado - Predeterminado: L2R
    pdfDocument.setDirection(com.aspose.pdf.Direction.R2L);
    
    // Especificar si la barra de título de la ventana debe mostrar el título del documento
    // si es falso, la barra de título muestra el nombre del archivo PDF - Predeterminado: false
    pdfDocument.setDisplayDocTitle(true);
    
    // Especificar si redimensionar la ventana del documento para ajustar el tamaño de
    // la primera página mostrada - Predeterminado: false
    pdfDocument.setFitWindow(true);
    
    // Especificar si ocultar la barra de menú de la aplicación del visor - Predeterminado:
    // false
    pdfDocument.setHideMenubar(true);
    
    // Especificar si ocultar la barra de herramientas de la aplicación del visor - Predeterminado:
    // false
    pdfDocument.setHideToolBar(true);
    
    // Especificar si ocultar elementos de la interfaz de usuario como barras de desplazamiento
    // y dejar solo el contenido de la página mostrado - Predeterminado: false
    pdfDocument.setHideWindowUI(true);
    
    // Modo de página del documento. especificar cómo mostrar el documento al salir
    // del modo de pantalla completa.
    pdfDocument.setNonFullScreenPageMode(com.aspose.pdf.PageMode.UseOC);
    
    // Especificar el diseño de página, es decir, una sola página, una columna
    pdfDocument.setPageLayout(com.aspose.pdf.PageLayout.TwoColumnLeft);
    
    // Especificar cómo se debe mostrar el documento cuando se abre
    // es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos
    pdfDocument.setPageMode(com.aspose.pdf.PageMode.UseThumbs);
    
    // Guardar archivo PDF actualizado
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");

  }
```

## Incrustar Fuentes en un Archivo PDF Existente

Los lectores de PDF soportan [un núcleo de 14 fuentes](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) para que los documentos se puedan mostrar de la misma manera independientemente de la plataforma en la que se muestren. Cuando un PDF contiene una fuente que está fuera de las fuentes principales, incruste la fuente para evitar la sustitución de fuentes.

Aspose.PDF para Java soporta la incrustación de fuentes en documentos PDF existentes. Puede incrustar una fuente completa o un subconjunto. Para incrustar la fuente:

1. Abra un archivo PDF existente usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Use la clase [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) para incrustar la fuente.
   1. El método setEmbedded(true) incrusta la fuente completa.
   1. El método pageFont.isSubset(true) incrusta un subconjunto de la fuente.

Un subconjunto de fuente solo incrusta los caracteres que se utilizan y es útil cuando las fuentes se utilizan para oraciones cortas o eslóganes, por ejemplo, cuando una fuente corporativa se utiliza para un logotipo, pero no para el texto del cuerpo.
 Reducir el subconjunto disminuye el tamaño del archivo del PDF de salida.

Sin embargo, si se utiliza una fuente personalizada para el texto del cuerpo, incrústela en su totalidad.

El siguiente fragmento de código muestra cómo incrustar una fuente en un archivo PDF.
```java
public static void EmbeddingFontsInAnExistingPDFFile() {
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Iterar a través de todas las páginas
    for (com.aspose.pdf.Page page : (Iterable<com.aspose.pdf.Page>) pdfDocument.getPages()) {
      if (page.getResources().getFonts() != null) {
        for (com.aspose.pdf.Font pageFont : (Iterable<com.aspose.pdf.Font>) page.getResources().getFonts()) {
          // Verificar si la fuente ya está incrustada
          if (!pageFont.isEmbedded())
            pageFont.setEmbedded(true);
        }
      }

      // Verificar los objetos de Formulario
      for (com.aspose.pdf.XForm form : (Iterable<com.aspose.pdf.XForm>) page.getResources().getForms()) {
        if (form.getResources().getFonts() != null) {
          for (com.aspose.pdf.Font formFont : (Iterable<com.aspose.pdf.Font>) form.getResources().getFonts()) {
            // Verificar si la fuente está incrustada
            if (!formFont.isEmbedded())
              formFont.setEmbedded(true);
          }
        }
      }
    }
    // Guardar el archivo PDF actualizado
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Incrustación de Fuentes al crear PDF

Si necesitas usar cualquier fuente distinta a las 14 fuentes básicas soportadas por Adobe Reader, entonces debes incrustar la descripción de la fuente al generar un archivo PDF. Si la información de la fuente no está incrustada, Adobe Reader la tomará del sistema operativo si está instalada en el sistema, o construirá una fuente sustituta según el descriptor de la fuente en el PDF. Por favor, ten en cuenta que la fuente incrustada debe estar instalada en la máquina host, es decir, en el caso del siguiente código, la fuente 'Univers Condensed' está instalada en el sistema.

Usamos la propiedad setEmbedded de la clase [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) para incrustar la información de la fuente en el archivo PDF. Configurar el valor de esta propiedad a 'true' incrustará el archivo completo de la fuente en el PDF, sabiendo que esto aumentará el tamaño del archivo PDF. A continuación se presenta el fragmento de código que se puede usar para incrustar la información de la fuente en el PDF.

```java
public static void EmbeddingFontsWhileCreatingPDF() {

    // Instanciar el objeto PDF llamando a su constructor vacío
    com.aspose.pdf.Document document = new com.aspose.pdf.Document();

    // Crear una sección en el objeto Pdf
    com.aspose.pdf.Page page = document.getPages().add();

    com.aspose.pdf.TextFragment fragment = new com.aspose.pdf.TextFragment("");

    com.aspose.pdf.TextSegment segment = new com.aspose.pdf.TextSegment(" Este es un texto de muestra usando una fuente personalizada.");
    com.aspose.pdf.TextState ts = new com.aspose.pdf.TextState();
    ts.setFont(FontRepository.findFont("Univers Condensed"));
    ts.getFont().setEmbedded(true);
    segment.setTextState(ts);
    fragment.getSegments().add(segment);
    page.getParagraphs().add(fragment);

    // Guardar el archivo PDF actualizado
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Establecer el Nombre de Fuente Predeterminado al Guardar PDF

Cuando un documento PDF contiene fuentes que no están disponibles en el propio documento ni en el dispositivo, la API reemplaza estas fuentes con la fuente predeterminada. Cuando una fuente está disponible (está instalada en el dispositivo o está incrustada en el documento), el PDF de salida debería tener la misma fuente (no debería ser reemplazada por la fuente predeterminada). El valor de la fuente predeterminada debe contener el nombre de la fuente (no la ruta a los archivos de fuentes). Hemos implementado una función para establecer el nombre de la fuente predeterminada al guardar un documento como PDF. Se puede utilizar el siguiente fragmento de código para establecer la fuente predeterminada:

```java
public static void SetDefaultFontNameWhileSavingPDF() {

    // Cargar un documento PDF existente
    Document document = new Document("input.pdf");

    String newName = "Arial";

    // Inicializar opciones de guardado para el formato PDF
    PdfSaveOptions ops = new PdfSaveOptions();

    // Establecer el nombre de la fuente predeterminada
    ops.setDefaultFontName(newName);

    // Guardar archivo PDF
    document.save(_dataDir + "output_out.pdf", ops);
  }
```


## Obtener Todas las Fuentes del Documento PDF

En caso de que desees obtener todas las fuentes de un documento PDF, puedes usar el método **Document.getFontUtilities().getAllFonts()** proporcionado en la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Por favor, revisa el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```java
public static void GetAllFontsFromPDFDocument() {

    // Cargar un documento PDF existente
    Document document = new Document(_dataDir + "sample.pdf");

    // Obtener todas las fuentes del documento
    com.aspose.pdf.Font[] fonts = document.getFontUtilities().getAllFonts();
    for (com.aspose.pdf.Font f : fonts) {
      System.out.println(f.getFontName());
    }
  }
```

## Obtener-Establecer el Factor de Zoom del Archivo PDF

A veces, deseas establecer u obtener el factor de zoom de un documento PDF. Puedes lograr fácilmente este requisito con Aspose.PDF.

El objeto [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) te permite obtener el valor de zoom asociado con un archivo PDF.
 De manera similar, se puede usar para establecer el factor de zoom de un archivo.

```java
  public static void GetSetZoomFactorOfPDFFile() {
    // Cargar un documento PDF existente
    Document document = new Document(_dataDir + "sample.pdf");
    double zoom = .5;
    // establecer el factor de zoom del documento
    GoToAction actionzoom = new GoToAction(new XYZExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth(),
        document.getPages().get_Item(1).getMediaBox().getHeight(), zoom));

    // establecer acción para ajustar al ancho de la página con zoom
    GoToAction actionFittoWidth = new GoToAction(new FitHExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth()));

    // establecer acción para ajustar al alto de la página con zoom
    GoToAction actionFittoHeight = new GoToAction(new FitVExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getHeight()));

    document.setOpenAction(actionzoom);
    document.setOpenAction(actionFittoWidth);
    document.setOpenAction(actionFittoHeight);
```

El siguiente fragmento de código muestra cómo obtener el factor de zoom de un archivo PDF.

```java
    // Instanciar un nuevo objeto Document
    Document doc1 = new Document(_dataDir + "Zoomed_actionzoom.pdf");
    // Crear objeto GoToAction
    GoToAction action = (GoToAction) doc1.getOpenAction();
    // Obtener el factor de zoom del archivo PDF
    System.out.println(((XYZExplicitDestination) action.getDestination()).getZoom());

    // Guardar el archivo PDF actualizado
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
}
```
---
title: Actualizar Enlaces en PDF
linktitle: Actualizar Enlaces
type: docs
weight: 20
url: /es/java/update-links/
description: Actualizar enlaces en PDF programáticamente. Esta guía trata sobre cómo actualizar enlaces en PDF en lenguaje Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Actualizar Enlaces en un Archivo PDF

Como se discutió en Agregar Hipervínculo en un Archivo PDF, la clase [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) permite agregar enlaces en un archivo PDF. También hay una clase similar que se utiliza para obtener enlaces existentes desde dentro de archivos PDF. Use esto si necesita actualizar un enlace existente. Para actualizar un enlace existente:

1. Cargue un archivo PDF.
1. Vaya a una página específica en el archivo PDF.
1. Especifique el destino del enlace usando la propiedad Destination del objeto [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction).

1. La página de destino se especifica utilizando el constructor [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination).

### Establecer el Destino del Enlace a una Página en el Mismo Documento

El siguiente fragmento de código muestra cómo actualizar un enlace en un archivo PDF y establecer su destino en la segunda página del documento.

```java
    public static void SetLinkTargetToAPageInTheSameDocument() {
        
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
        // Obtener la primera anotación de enlace de la primera página del documento
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Modificación del enlace: cambiar el destino del enlace
        GoToAction goToAction = (GoToAction)linkAnnot.getAction();
        // Especificar el destino para el objeto de enlace
        // Representa un destino explícito que muestra la página con las coordenadas (izquierda, arriba) posicionadas en la esquina superior izquierda de
        // la ventana y el contenido de la página ampliado por el factor de zoom.
        // El primer parámetro es el número de página de destino.
        // El segundo es la coordenada izquierda
        // El tercero es la coordenada superior
        // El cuarto argumento es el factor de zoom al mostrar la página respectiva. Usar 2 significa que la página se mostrará con un zoom del 200%
        goToAction.setDestination(new XYZExplicitDestination(1, 1, 2, 2 ));
        
        // Guardar el documento con el enlace actualizado
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Establecer el Destino del Enlace a una Dirección Web

Para actualizar el hipervínculo de modo que apunte a una dirección web, instancia el objeto [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction) y pásalo a la propiedad Action de LinkAnnotation. El siguiente fragmento de código muestra cómo actualizar un enlace en un archivo PDF y establecer su objetivo en una dirección web.

```java
    public static void SetLinkDestinationToWebAddress() {        
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        // Obtener la primera anotación de enlace de la primera página del documento
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Modificación del enlace: cambiar la acción del enlace y establecer el objetivo como dirección web
        linkAnnot.setAction(new GoToURIAction("www.aspose.com"));
        
        // Guardar el documento con el enlace actualizado
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Establecer el Destino del Enlace a Otro Archivo PDF

El siguiente fragmento de código muestra cómo actualizar un enlace en un archivo PDF y establecer su destino a otro archivo PDF.

```java
    public static void SetLinkTargetToAnotherPDFFile() {        
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.getAction();
        // La siguiente línea actualiza el destino, no actualiza el archivo
        goToR.setDestination(new XYZExplicitDestination(2, 0, 0, 1.5));
        // La siguiente línea actualiza el archivo
        goToR.setFile (new FileSpecification(_dataDir +  "input.pdf"));

        // Guardar el documento con el enlace actualizado
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### Actualizar el Color del Texto de LinkAnnotation

La anotación de enlace no contiene texto.
 En su lugar, el texto se coloca en los contenidos de la página bajo la anotación. Por lo tanto, para cambiar el color del texto, reemplaza el color del texto de la página en lugar de intentar cambiar el color de la anotación. El siguiente fragmento de código muestra cómo actualizar el color de la anotación de enlace en un archivo PDF.

```java
    public static void UpdateLinkAnnotationTextColor () {        
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        for (Annotation annotation : page.getAnnotations())
        {
            if (annotation.getAnnotationType() == AnnotationType.Link)
            {
                // Buscar el texto bajo la anotación
                TextFragmentAbsorber ta = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX()-10);
                rect.setLLY(rect.getLLY()-10);
                rect.setURX(rect.getURX()+ 10);
                rect.setURY(rect.getURY()+ 10);

                ta.setTextSearchOptions(new TextSearchOptions(rect));
                ta.visit(page);
                // Cambiar el color del texto.
                for (TextFragment tf : ta.getTextFragments())
                {
                    tf.getTextState().setForegroundColor(Color.getRed());
                }
            }
        
        }                       
        // Guardar el documento con el enlace actualizado
        document.save(_dataDir + "UpdateLinkTextColor_out.pdf");        
    }
```
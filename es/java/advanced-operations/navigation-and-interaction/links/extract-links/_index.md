---
title: Extraer Enlaces del Archivo PDF 
linktitle: Extraer Enlaces
type: docs
weight: 30
url: /es/java/extract-links/
description: Extraer enlaces de PDF con Java. Este tema le explica cómo extraer enlaces utilizando la clase AnnotationSelector.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Enlaces del Archivo PDF

Los enlaces están representados como anotaciones en un archivo PDF, por lo que para extraer enlaces, extraiga todos los objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).

1. Cree un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. Obtenga la [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) de la que desea extraer enlaces.
3. Use la clase [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) para extraer todos los objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) de la página especificada.

1. Pase el objeto [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) al método Accept del objeto Page.
1. Obtenga todas las anotaciones de enlace seleccionadas en un objeto IList utilizando el método [getSelected](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) del objeto [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector).

El siguiente fragmento de código le muestra cómo extraer enlaces de un archivo PDF.

```java
    public static void ExtractLinksFromThePDFFile() {        
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        java.util.List<Annotation> list = selector.getSelected();
        for(Annotation annot : list)
        {
            System.out.println("Anotación localizada: " + annot.getRect());
        }
                
        // Guardar el documento con el enlace actualizado
        //document.save(_dataDir + "ExtractLinks_out.pdf");
    }
```
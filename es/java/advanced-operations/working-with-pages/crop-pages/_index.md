---
title: Recortar páginas de PDF programáticamente
linktitle: Recortar Páginas
type: docs
weight: 80
url: es/java/crop-pages/
description: Puede obtener propiedades de página, como el ancho, alto, bleed-, crop- y trimbox usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener propiedades de la página

Cada página en un archivo PDF tiene una serie de propiedades, como el ancho, alto, bleed-, crop- y trimbox. Aspose.PDF para Java le permite acceder a estas propiedades.

- **Caja de medios**: La caja de medios es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo, A4, A5, Carta de EE.UU., etc.) seleccionado cuando el documento se imprimió en PostScript o PDF. En otras palabras, la caja de medios determina el tamaño físico del medio en el cual se muestra o imprime el documento PDF.
- **Caja de sangrado**: Si el documento tiene sangrado, el PDF también tendrá una caja de sangrado.
 El sangrado es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprima y se corte al tamaño ("recortado"), la tinta llegue hasta el borde de la página. Incluso si la página se recorta incorrectamente - cortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.
- **Caja de recorte**: La caja de recorte indica el tamaño final de un documento después de la impresión y el recorte.
- **Caja de arte**: La caja de arte es el cuadro dibujado alrededor del contenido real de las páginas en sus documentos. Este cuadro se utiliza al importar documentos PDF en otras aplicaciones.
- **Caja de corte**: La caja de corte es el tamaño de "página" en el que se muestra su documento PDF en Adobe Acrobat. En la vista normal, solo se muestra el contenido de la caja de corte en Adobe Acrobat. Para descripciones detalladas de estas propiedades, lea la especificación de Adobe.Pdf, particularmente 10.10.1 Límites de Página.
- **Page.Rect**: la intersección (rectángulo comúnmente visible) del MediaBox y DropBox. La imagen a continuación ilustra estas propiedades.  
Para más detalles, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

El fragmento a continuación muestra cómo recortar la página:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleCropPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    public static void CropPagesPDF() {
        Document pdfDocument = new Document("crop_page.pdf");
        Page page = pdfDocument.getPages().get_Item(1);

        System.out.println(page.getCropBox());
        System.out.println(page.getTrimBox());
        System.out.println(page.getArtBox());
        System.out.println(page.getBleedBox());
        System.out.println(page.getMediaBox());

        // Crear nuevo Rectángulo Box
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520);

        page.setCropBox(newBox);
        page.setTrimBox(newBox);
        page.setArtBox(newBox);
        page.setBleedBox(newBox);

        // Guardar documento de salida
        pdfDocument.save(_dataDir + "crop_page_modified.pdf");
    }
}
```

In this example we used a sample file [here](crop_page.pdf). Inicialmente, nuestra página se ve como se muestra en la Figura 1.
![Figure 1. Cropped Page](crop_page.png)

Después del cambio, la página se verá como la Figura 2.
![Figure 2. Cropped Page](crop_page2.png)
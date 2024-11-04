---
title: Buscar y Obtener Imágenes de un Documento PDF
linktitle: Buscar y Obtener Imágenes
type: docs
weight: 60
url: /java/search-and-get-images-from-pdf-document/
description: Esta sección explica cómo buscar y obtener imágenes de un documento PDF con la biblioteca Aspose.PDF para Java.
lastmod: "2021-06-05"
---

El [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) te permite buscar entre las imágenes en todas las páginas de un documento PDF.

Para buscar imágenes en todo un documento:

1. Llama al método Accept de la colección [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). El método Accept toma un objeto [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) como parámetro. Esto devuelve una colección de objetos [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).
2. Recorre los objetos de ImagePlacements y obtén sus propiedades (Imagen, dimensiones, resolución, etc.).

El siguiente fragmento de código muestra cómo buscar todas las imágenes de un documento.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import com.aspose.pdf.*;

public class ExampleSearchAndGet {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SearchImages() throws IOException {
        // Abrir documento
        Document doc = new Document(_dataDir + "SearchAndGetImages.pdf");

        // Crear objeto ImagePlacementAbsorber para realizar la búsqueda de ubicación de imágenes
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Aceptar el absorbente para todas las páginas
        doc.getPages().accept(abs);

        // Bucle a través de todos los ImagePlacements, obtener imagen y propiedades de ImagePlacement
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Obtener la imagen usando el objeto ImagePlacement
            // XImage image = imagePlacement.getImage();

            // Mostrar propiedades de ubicación de imagen para todas las ubicaciones
            System.out.println("ancho de la imagen:" + imagePlacement.getRectangle().getWidth());
            System.out.println("altura de la imagen:" + imagePlacement.getRectangle().getHeight());
            System.out.println("LLX de la imagen:" + imagePlacement.getRectangle().getLLX());
            System.out.println("LLY de la imagen:" + imagePlacement.getRectangle().getLLY());
            System.out.println("resolución horizontal de la imagen:" + imagePlacement.getResolution().getX());
            System.out.println("resolución vertical de la imagen:" + imagePlacement.getResolution().getY());
        }

    }
}
```

Para obtener una imagen de una página individual, utiliza el siguiente código:

```java
doc.getPages().get_Item(1).accept(abs)
```
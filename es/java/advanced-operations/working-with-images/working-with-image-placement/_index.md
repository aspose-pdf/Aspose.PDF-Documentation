---
title: Trabajando con la Colocación de Imágenes
linktitle: Colocación de Imágenes
type: docs
weight: 50
url: /es/java/working-with-image-placement/
description: Esta sección describe las características del trabajo con la colocación de imágenes en un archivo PDF utilizando la biblioteca Java.
lastmod: "2021-06-05"
---

Aspose.PDF para Java introdujo clases llamadas [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) y [ImagePlacementCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementCollection) que proporcionan una capacidad similar a las clases descritas anteriormente para obtener la resolución y posición de una imagen en un documento PDF.

- ImagePlacementAbsorber realiza una búsqueda de uso de imágenes como la colección de objetos ImagePlacement.
- ImagePlacement proporciona los miembros Resolution y Rectangle que devuelven valores reales de colocación de imágenes.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;


import javax.imageio.ImageIO;

public class ExampleWorkingWithImagePlacement {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void WorkingWithImagePlacement() throws IOException {
        // Cargar el archivo PDF de origen
        Document doc = new Document(_dataDir + "ImageInformation.pdf");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Cargar el contenido de la primera página
        doc.getPages().get_Item(1).accept(abs);
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Obtener propiedades de la imagen
            System.out.println("ancho de la imagen:" + imagePlacement.getRectangle().getWidth());
            System.out.println("altura de la imagen:" + imagePlacement.getRectangle().getHeight());
            System.out.println("LLX de la imagen:" + imagePlacement.getRectangle().getLLX());
            System.out.println("LLY de la imagen:" + imagePlacement.getRectangle().getLLY());
            System.out.println("resolución horizontal de la imagen:" + imagePlacement.getResolution().getX());
            System.out.println("resolución vertical de la imagen:" + imagePlacement.getResolution().getY());

            // Recuperar imagen con dimensiones visibles
            // Bitmap scaledImage;
            // Recuperar imagen de los recursos
            ByteArrayOutputStream imageStream = new ByteArrayOutputStream();
            imagePlacement.getImage().save(imageStream, ImageType.getPng());

            // Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
            BufferedImage resourceImage = ImageIO.read(new ByteArrayInputStream(imageStream.toByteArray()));

            // Crear bitmap con dimensiones reales
            BufferedImage scaledImage = toBufferedImage( 
            resourceImage.getScaledInstance((int) imagePlacement.getRectangle().getWidth(),
                    (int) imagePlacement.getRectangle().getHeight(), java.awt.Image.SCALE_SMOOTH));

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(scaledImage, "jpg", baos);
            ByteArrayInputStream fis = new ByteArrayInputStream(baos.toByteArray());

            imagePlacement.getImage().replace(fis);
        }
    }
    
    public static BufferedImage toBufferedImage(java.awt.Image img) {
        if (img instanceof BufferedImage) {
            return (BufferedImage) img;
        }

        // Crear una imagen en búfer con transparencia
        BufferedImage bimage = new BufferedImage(img.getWidth(null), img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        // Dibujar la imagen en la imagen en búfer
        Graphics2D bGr = bimage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        // Devolver la imagen en búfer
        return bimage;
    }
}
```
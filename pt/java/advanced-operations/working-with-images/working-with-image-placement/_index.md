---
title: Trabalhando com Colocação de Imagem
linktitle: Colocação de Imagem
type: docs
weight: 50
url: /pt/java/working-with-image-placement/
description: Esta seção descreve os recursos de trabalhar com a colocação de imagem em um arquivo PDF usando a biblioteca Java.
lastmod: "2021-06-05"
---

Aspose.PDF para Java introduziu classes chamadas [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) e [ImagePlacementCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementCollection) que fornecem capacidade similar às classes descritas acima para obter a resolução e posição de uma imagem em um documento PDF.

- ImagePlacementAbsorber realiza a busca de uso de imagem como a coleção de objetos ImagePlacement.
- ImagePlacement fornece os membros Resolution e Rectangle que retornam valores reais de colocação de imagem.

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
        // Carregar o arquivo PDF de origem
        Document doc = new Document(_dataDir + "ImageInformation.pdf");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Carregar o conteúdo da primeira página
        doc.getPages().get_Item(1).accept(abs);
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Obter propriedades da imagem
            System.out.println("largura da imagem:" + imagePlacement.getRectangle().getWidth());
            System.out.println("altura da imagem:" + imagePlacement.getRectangle().getHeight());
            System.out.println("imagem LLX:" + imagePlacement.getRectangle().getLLX());
            System.out.println("imagem LLY:" + imagePlacement.getRectangle().getLLY());
            System.out.println("resolução horizontal da imagem:" + imagePlacement.getResolution().getX());
            System.out.println("resolução vertical da imagem:" + imagePlacement.getResolution().getY());

            // Recuperar imagem com dimensões visíveis
            // Bitmap scaledImage;
            // Recuperar imagem dos recursos
            ByteArrayOutputStream imageStream = new ByteArrayOutputStream();
            imagePlacement.getImage().save(imageStream, ImageType.getPng());

            // Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
            BufferedImage resourceImage = ImageIO.read(new ByteArrayInputStream(imageStream.toByteArray()));

            // Criar bitmap com dimensões reais
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

        // Criar uma imagem em buffer com transparência
        BufferedImage bimage = new BufferedImage(img.getWidth(null), img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        // Desenhar a imagem na imagem em buffer
        Graphics2D bGr = bimage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        // Retornar a imagem em buffer
        return bimage;
    }
}
```
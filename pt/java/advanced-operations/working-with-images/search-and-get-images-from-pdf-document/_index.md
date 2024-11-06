---
title: Pesquisar e Obter Imagens de Documento PDF
linktitle: Pesquisar e Obter Imagens
type: docs
weight: 60
url: pt/java/search-and-get-images-from-pdf-document/
description: Esta seção explica como pesquisar e obter imagens de um documento PDF com a biblioteca Aspose.PDF para Java.
lastmod: "2021-06-05"
---

O [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) permite que você pesquise entre imagens em todas as páginas de um documento PDF.

Para pesquisar um documento inteiro por imagens:

1. Chame o método Accept da coleção [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). O método Accept recebe um objeto [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacementAbsorber) como parâmetro. Isso retorna uma coleção de objetos [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).
1. Percorra os objetos ImagePlacements e obtenha suas propriedades (Imagem, dimensões, resolução e assim por diante).

O trecho de código a seguir mostra como pesquisar um documento por todas as suas imagens.

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import com.aspose.pdf.*;

public class ExampleSearchAndGet {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SearchImages() throws IOException {
        // Abrir documento
        Document doc = new Document(_dataDir + "SearchAndGetImages.pdf");

        // Criar objeto ImagePlacementAbsorber para realizar a busca de colocação de imagem
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

        // Aceitar o absorvedor para todas as páginas
        doc.getPages().accept(abs);

        // Percorrer todos os ImagePlacements, obter imagem e Propriedades de ImagePlacement
        for (ImagePlacement imagePlacement : abs.getImagePlacements()) {
            // Obter a imagem usando o objeto ImagePlacement
            // XImage image = imagePlacement.getImage();

            // Exibir propriedades de colocação de imagem para todas as colocações
            System.out.println("largura da imagem:" + imagePlacement.getRectangle().getWidth());
            System.out.println("altura da imagem:" + imagePlacement.getRectangle().getHeight());
            System.out.println("LLX da imagem:" + imagePlacement.getRectangle().getLLX());
            System.out.println("LLY da imagem:" + imagePlacement.getRectangle().getLLY());
            System.out.println("resolução horizontal da imagem:" + imagePlacement.getResolution().getX());
            System.out.println("resolução vertical da imagem:" + imagePlacement.getResolution().getY());
        }

    }
}
```

Para obter uma imagem de uma página individual, use o seguinte código:

```java
doc.getPages().get_Item(1).accept(abs)
```
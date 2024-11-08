---
title: Definir Tamanho da Imagem
linktitle: Definir Tamanho da Imagem
type: docs
weight: 80
url: /pt/java/set-image-size/
description: Esta seção descreve como definir o tamanho da imagem em um arquivo PDF usando a biblioteca Java.
lastmod: "2021-06-05"
---

É possível definir o tamanho de uma imagem que está sendo adicionada a um arquivo PDF. Para definir o tamanho, você pode usar os métodos [setFixWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixWidth-double-) e [setFixHeight](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image#setFixHeight-double-) da classe com.aspose.pdf.Image.

O trecho de código a seguir demonstra como definir o tamanho de uma imagem:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSetImageSize {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Replace() {
        // Instanciar objeto Document
        Document doc = new Document();
        // adicionar página à coleção de páginas do arquivo PDF
        Page page = doc.getPages().add();
        // Criar uma instância de imagem
        Image img = new Image();
        // Definir Largura e Altura da Imagem em Pontos
        img.setFixWidth (100);
        img.setFixHeight (100);
        // Definir tipo de imagem como SVG
        img.setFileType (ImageFileType.Svg);
        // Caminho para o arquivo de origem
        img.setFile (_dataDir + "aspose-logo.jpg");
        page.getParagraphs().add(img);
        // Definir propriedades da página
        page.getPageInfo().setWidth(800);
        page.getPageInfo().setHeight(800);        
        // salvar arquivo PDF resultante
        doc.save(_dataDir + "SetImageSize_out.pdf");
    }
}
```
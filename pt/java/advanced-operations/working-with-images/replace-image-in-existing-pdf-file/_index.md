---
title: Substituir Imagem em Arquivo PDF Existente
linktitle: Substituir Imagem
type: docs
weight: 70
url: /pt/java/replace-image-in-existing-pdf-file/
description: Esta seção descreve como substituir imagem em arquivo PDF existente usando a biblioteca Java.
lastmod: "2021-06-05"
---

O método [Replace](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection#replace-int-java.io.InputStream-) da coleção [XImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) permite substituir uma imagem em um arquivo PDF existente.

A coleção de Imagens pode ser encontrada na coleção de Recursos de uma página. Para substituir uma imagem:

1. Abra o arquivo PDF usando o objeto Document.
2. Substitua uma imagem específica, salve o arquivo PDF atualizado usando o método Save do objeto Document.

O trecho de código a seguir mostra como substituir uma imagem em um arquivo PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.Document;

public class ExampleReplaceImage {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void Replace() {
        // Abrir documento
        Document pdfDocument = new Document("input.pdf");
        // Substituir uma imagem específica
        try {
            pdfDocument.getPages().get_Item(1).getResources().getImages().replace(1, new FileInputStream("lovely.jpg"));
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        // Salvar arquivo PDF atualizado
        pdfDocument.save(_dataDir + "output.pdf");
    }
}
```
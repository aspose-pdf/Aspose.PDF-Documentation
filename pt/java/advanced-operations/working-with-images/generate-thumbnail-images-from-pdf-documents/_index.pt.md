---
title: Gerar Imagens em Miniatura de Documentos PDF
linktitle: Gerar Imagens em Miniatura
type: docs
weight: 100
url: /java/generate-thumbnail-images-from-pdf-documents/
description: Esta seção descreve como gerar imagens em miniatura de documentos PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
---

## Abordagem Aspose.PDF para Java

Aspose.PDF para Java fornece suporte extensivo para lidar com documentos PDF. Ele também suporta a capacidade de converter as páginas de documentos PDF em uma variedade de formatos de imagem. A funcionalidade descrita acima pode ser facilmente alcançada usando Aspose.PDF para Java.

Aspose.PDF tem benefícios distintos:

- Você não precisa ter o Adobe Acrobat instalado no seu sistema para trabalhar com arquivos PDF.
- Usar o Aspose.PDF para Java é simples e fácil de entender em comparação com a Automação do Acrobat.

Se precisarmos converter páginas de PDF em JPEGs, o namespace [com.aspose.pdf.devices](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/package-frame) fornece uma classe chamada [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) para renderizar páginas de PDF em imagens JPEG.
 Please take a look over the following code snippet.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.JpegDevice;
import com.aspose.pdf.devices.Resolution;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class ExampleGenerateThumbnails {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GenerateThumbnails() throws IOException {
        // Recupere os nomes de todos os arquivos PDF em um diretório específico
        List<String> fileEntries = null;
        try {
            fileEntries = Files.list(Paths.get(_dataDir)).filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".pdf")).map(path -> path.toString())
                    .collect(Collectors.toList());

        } catch (IOException e) {
            // Erro ao ler o diretório
        }

        // Iterar por todas as entradas de arquivos no array
        for (int counter = 0; counter < fileEntries.size(); counter++) {
            // Abrir documento
            Document pdfDocument = new Document(fileEntries.get(counter));

            for (int pageCount = 1; pageCount <= 4; pageCount++) {
                FileOutputStream imageStream = new FileOutputStream(
                        _dataDir + "\\Thumbnails" + counter + "_" + pageCount + ".jpg");
                // Criar objeto Resolution
                Resolution resolution = new Resolution(300);
                JpegDevice jpegDevice = new JpegDevice(45, 59, resolution, 100);
                // Converter uma página específica e salvar a imagem no fluxo
                jpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);
                // Fechar fluxo
                imageStream.close();
            }
        }

    }
}
```
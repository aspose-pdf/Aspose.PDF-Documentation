---
title: Generar Imágenes en Miniatura de Documentos PDF
linktitle: Generar Imágenes en Miniatura
type: docs
weight: 100
url: /java/generate-thumbnail-images-from-pdf-documents/
description: Esta sección describe cómo generar imágenes en miniatura de documentos PDF utilizando Aspose.PDF para Java.
lastmod: "2021-06-05"
---

## Enfoque de Aspose.PDF para Java

Aspose.PDF para Java proporciona un soporte extenso para manejar documentos PDF. También admite la capacidad de convertir las páginas de documentos PDF a una variedad de formatos de imagen. La funcionalidad descrita anteriormente se puede lograr fácilmente utilizando Aspose.PDF para Java.

Aspose.PDF tiene beneficios distintos:

- No necesitas tener Adobe Acrobat instalado en tu sistema para trabajar con archivos PDF.
- Usar Aspose.PDF para Java es simple y fácil de entender en comparación con la Automatización de Acrobat.

Si necesitamos convertir páginas de PDF en JPEGs, el espacio de nombres [com.aspose.pdf.devices](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/package-frame) proporciona una clase llamada [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) para renderizar páginas PDF en imágenes JPEG.
 Por favor, revise el siguiente fragmento de código.

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
        // Recuperar nombres de todos los archivos PDF en un directorio particular
        List<String> fileEntries = null;
        try {
            fileEntries = Files.list(Paths.get(_dataDir)).filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".pdf")).map(path -> path.toString())
                    .collect(Collectors.toList());

        } catch (IOException e) {
            // Error al leer el directorio
        }

        // Iterar a través de todas las entradas de archivos en el arreglo
        for (int counter = 0; counter < fileEntries.size(); counter++) {
            // Abrir documento
            Document pdfDocument = new Document(fileEntries.get(counter));

            for (int pageCount = 1; pageCount <= 4; pageCount++) {
                FileOutputStream imageStream = new FileOutputStream(
                        _dataDir + "\\Thumbnails" + counter + "_" + pageCount + ".jpg");
                // Crear objeto de resolución
                Resolution resolution = new Resolution(300);
                JpegDevice jpegDevice = new JpegDevice(45, 59, resolution, 100);
                // Convertir una página particular y guardar la imagen en el flujo
                jpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);
                // Cerrar flujo
                imageStream.close();
            }
        }

    }
}
```
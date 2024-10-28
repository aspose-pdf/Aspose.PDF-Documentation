---
title: Añadir fondo al PDF 
linktitle: Añadir fondos
type: docs
weight: 110
url: /java/add-backgrounds/
descriptions: Añadir imagen de fondo a su archivo PDF con Java. Use el objeto BackgroundArtifact.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Las imágenes de fondo pueden utilizarse para añadir una marca de agua u otro diseño sutil a los documentos. En Aspose.PDF para Java, cada documento PDF es una colección de páginas y cada página contiene una colección de artefactos. La clase [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) puede utilizarse para añadir una imagen de fondo a un objeto de página.

El siguiente fragmento de código muestra cómo añadir una imagen de fondo a las páginas del PDF utilizando el objeto BackgroundArtifact con Java.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.BackgroundArtifact;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;

public class ExampleAddBackground {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() throws FileNotFoundException {
        // Para ejemplos completos y archivos de datos, por favor vaya a
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        String myDir = "";
        // Crear un nuevo objeto Document
        Document doc = new Document();
        // Añadir una nueva página al objeto documento
        Page page = doc.getPages().add();
        // Crear objeto BackgroundArtifact
        BackgroundArtifact background = new BackgroundArtifact();
        // Especificar la imagen para el objeto backgroundartifact
        background.setBackgroundImage(new FileInputStream(myDir + "logo.png"));
        // Añadir backgroundartifact a la colección de artefactos de la página
        page.getArtifacts().add(background);
        // Guardar el documento
        doc.save(_dataDir + "BackGround.pdf");
    }
}
```
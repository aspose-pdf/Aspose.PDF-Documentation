---
title: Determinar Salto de Línea
linktitle: Determinar Salto de Línea
type: docs
weight: 70
url: /java/determine-line-break/
description: Aprende más sobre cómo determinar un salto de línea de un TextFragment de varias líneas usando Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Seguimiento de Salto de Línea de TextFragment de Varias Líneas

Aspose.PDF para Java ofrece el registro (seguimiento) del procesamiento en segundo plano (salto de línea) de fragmentos de texto de varias líneas en escenarios de adición de texto. Puedes usar el método [GetNotifications](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getNotifications--)() de la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) como se indica a continuación, para rastrear el salto de línea de un fragmento de texto:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.io.FileWriter;   // Importar la clase FileWriter
import java.io.IOException;  // Importar la clase IOException para manejar errores

public class ExampleLineBreak {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void LineBreakDemo() {

        Document doc = new Document();
        Page page = doc.getPages().add();

        for (int i = 0; i < 4; i++)
        {
            TextFragment text = new TextFragment("Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.");
            text.getTextState().setFontSize(20);
            page.getParagraphs().add(text);
        }

        doc.save(_dataDir + "DetermineLineBreak_out.pdf");

        String notifications = page.getNotifications();
        System.out.println(notifications);
        try {
            FileWriter myWriter = new FileWriter(_dataDir + "notifications_out.txt");
            myWriter.write(notifications);
            myWriter.close();
          } catch (IOException e) {
            System.out.println("Ocurrió un error.");
            e.printStackTrace();
          }
    }
}
```
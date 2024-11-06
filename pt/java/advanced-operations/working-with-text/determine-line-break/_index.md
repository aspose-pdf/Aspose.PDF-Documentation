---
title: Determinar Quebra de Linha
linktitle: Determinar Quebra de Linha
type: docs
weight: 70
url: pt/java/determine-line-break/
description: Saiba mais sobre como determinar uma quebra de linha de TextFragment de várias linhas usando Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Acompanhar Quebra de Linha de TextFragment de Múltiplas Linhas

Aspose.PDF para Java oferece registro (acompanhamento) do processamento em segundo plano (quebra de linha) de fragmentos de texto de várias linhas em cenários de adição de texto. Você pode usar o método [GetNotifications](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getNotifications--)() da classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) da seguinte forma, para acompanhar a quebra de linha do fragmento de texto:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.io.FileWriter;   // Importe a classe FileWriter
import java.io.IOException;  // Importe a classe IOException para lidar com erros

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
            System.out.println("Ocorreu um erro.");
            e.printStackTrace();
          }
    }
}
```
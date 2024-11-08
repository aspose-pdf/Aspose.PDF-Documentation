---
title: Déterminer le Saut de Ligne
linktitle: Déterminer le Saut de Ligne
type: docs
weight: 70
url: /fr/java/determine-line-break/
description: Apprenez-en davantage sur la détermination d'un saut de ligne d'un TextFragment multi-ligne en utilisant Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Suivre le Saut de Ligne d'un TextFragment Multi-Ligne

Aspose.PDF pour Java offre le suivi du traitement en arrière-plan (saut de ligne) des fragments de texte multi-lignes dans les scénarios d'ajout de texte. Vous pouvez utiliser la méthode [GetNotifications](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getNotifications--)() de la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) comme suit, afin de suivre le saut de ligne d'un fragment de texte :

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.io.FileWriter;   // Importer la classe FileWriter
import java.io.IOException;  // Importer la classe IOException pour gérer les erreurs

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
            System.out.println("Une erreur est survenue.");
            e.printStackTrace();
          }
    }
}
```
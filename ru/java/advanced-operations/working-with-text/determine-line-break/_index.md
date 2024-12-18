---
title: Определение Разрыва Строки
linktitle: Определение Разрыва Строки
type: docs
weight: 70
url: /ru/java/determine-line-break/
description: Узнайте больше о том, как определить разрыв строки многострочного TextFragment с помощью Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Отслеживание Разрыва Строки Многострочного TextFragment

Aspose.PDF для Java предлагает регистрацию (отслеживание) фоновой обработки (разрыва строки) многострочных текстовых фрагментов в сценариях добавления текста. Вы можете использовать метод [GetNotifications](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getNotifications--)() класса [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) следующим образом, чтобы отслеживать разрыв строки текстового фрагмента:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.io.FileWriter;   // Импорт класса FileWriter
import java.io.IOException;  // Импорт класса IOException для обработки ошибок

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
            System.out.println("Произошла ошибка.");
            e.printStackTrace();
          }
    }
}
```
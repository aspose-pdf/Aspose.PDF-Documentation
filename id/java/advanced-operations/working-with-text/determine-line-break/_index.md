---
title: Tentukan Pemutusan Baris
linktitle: Tentukan Pemutusan Baris
type: docs
weight: 70
url: id/java/determine-line-break/
description: Pelajari lebih lanjut tentang cara menentukan pemutusan baris dari TextFragment multi-baris menggunakan Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Lacak Pemutusan Baris dari TextFragment Multi-Baris

Aspose.PDF untuk Java menawarkan pencatatan (pelacakan) pemrosesan latar belakang (pemutusan baris) dari fragmen teks multi-baris dalam skenario penambahan teks. Anda dapat menggunakan metode [GetNotifications](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getNotifications--)() dari kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) sebagai berikut, untuk melacak pemutusan baris dari fragmen teks:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.io.FileWriter;   // Impor kelas FileWriter
import java.io.IOException;  // Impor kelas IOException untuk menangani kesalahan

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
            System.out.println("Terjadi kesalahan.");
            e.printStackTrace();
          }
    }
}
```
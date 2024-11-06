---
title: تحديد فاصل الأسطر
linktitle: تحديد فاصل الأسطر
type: docs
weight: 70
url: ar/java/determine-line-break/
description: تعرف على كيفية تحديد فاصل الأسطر لمقطع نصي متعدد الأسطر باستخدام Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تتبع فاصل الأسطر للمقطع النصي متعدد الأسطر

يوفر Aspose.PDF for Java معالجة خلفية لتسجيل (تتبع) فاصل الأسطر لمقاطع النصوص المتعددة الأسطر في سيناريوهات إضافة النصوص. يمكنك استخدام طريقة [GetNotifications](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getNotifications--)() من فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) كما هو موضح أدناه، من أجل تتبع فاصل الأسطر للمقطع النصي:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.io.FileWriter;   // استيراد فئة FileWriter
import java.io.IOException;  // استيراد فئة IOException للتعامل مع الأخطاء

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
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
    }
}
```
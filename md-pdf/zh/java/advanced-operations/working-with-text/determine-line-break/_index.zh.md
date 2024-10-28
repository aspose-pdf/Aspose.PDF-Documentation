---
title: 确定换行符
linktitle: 确定换行符
type: docs
weight: 70
url: /java/determine-line-break/
description: 了解如何使用Java确定多行TextFragment的换行符
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 跟踪多行TextFragment的换行

Aspose.PDF for Java提供了在文本添加场景中记录（跟踪）多行文本片段的后台处理（换行）。您可以使用[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)类的[GetNotifications](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getNotifications--)()方法，如下所示，以跟踪文本片段的换行：

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.io.FileWriter;   // 导入FileWriter类
import java.io.IOException;  // 导入IOException类以处理错误

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
            System.out.println("发生了一个错误。");
            e.printStackTrace();
          }
    }
}
```
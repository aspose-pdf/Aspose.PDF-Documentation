---
title: Determine Line Break
linktitle: Determine Line Break
type: docs
weight: 70
url: /java/determine-line-break/
description: Learn more about how to determinate a line break of multi-line TextFragment.
lastmod: "2021-03-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Track Line Breaking of Multi-Line TextFragment

Aspose.PDF for .NET offers logging (tracking) background processing (line breaking) of multi-line text fragments in text adding scenarios. You can use the [GetNotifications](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page#getNotifications--)() method of [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) class as follows, in order to track line breaking of text fragment:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.io.FileWriter;   // Import the FileWriter class
import java.io.IOException;  // Import the IOException class to handle errors

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

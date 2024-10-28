---
title: 줄 바꿈 결정
linktitle: 줄 바꿈 결정
type: docs
weight: 70
url: /java/determine-line-break/
description: Java를 사용하여 다중 라인 TextFragment의 줄 바꿈을 결정하는 방법에 대해 알아보세요
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 다중 라인 TextFragment의 줄 바꿈 추적

Aspose.PDF for Java는 텍스트 추가 시나리오에서 다중 라인 텍스트 조각의 줄 바꿈에 대한 백그라운드 처리를 로깅(추적)하는 기능을 제공합니다. 텍스트 조각의 줄 바꿈을 추적하기 위해 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스의 [GetNotifications](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getNotifications--)() 메서드를 다음과 같이 사용할 수 있습니다:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.io.FileWriter;   // FileWriter 클래스를 임포트합니다
import java.io.IOException;  // 오류를 처리하기 위해 IOException 클래스를 임포트합니다

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
            System.out.println("오류가 발생했습니다.");
            e.printStackTrace();
          }
    }
}
```
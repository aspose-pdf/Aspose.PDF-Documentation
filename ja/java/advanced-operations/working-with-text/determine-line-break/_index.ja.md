---
title: 改行を決定する
linktitle: 改行を決定する
type: docs
weight: 70
url: /java/determine-line-break/
description: Javaを使用してマルチラインのTextFragmentの改行を決定する方法について学ぶ
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## マルチラインTextFragmentの改行を追跡する

Aspose.PDF for Javaは、テキスト追加シナリオにおけるマルチラインテキストフラグメントの改行のバックグラウンド処理（追跡）を提供します。テキストフラグメントの改行を追跡するために、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスの [GetNotifications](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getNotifications--)() メソッドを次のように使用できます:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.io.FileWriter;   // FileWriterクラスをインポート
import java.io.IOException;  // エラーを処理するためにIOExceptionクラスをインポート

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
            System.out.println("エラーが発生しました。");
            e.printStackTrace();
          }
    }
}
```
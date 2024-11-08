---
title: PDFに背景を追加する
linktitle: 背景を追加する
type: docs
weight: 110
url: /ja/java/add-backgrounds/
descriptions: JavaでPDFファイルに背景画像を追加します。BackgroundArtifactオブジェクトを使用します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

背景画像は、透かしや他の控えめなデザインを文書に追加するために使用できます。Aspose.PDF for Javaでは、各PDF文書はページのコレクションであり、各ページはアーティファクトのコレクションを含みます。[BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact)クラスは、ページオブジェクトに背景画像を追加するために使用できます。

次のコードスニペットは、BackgroundArtifactオブジェクトを使用してJavaでPDFページに背景画像を追加する方法を示しています。

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.BackgroundArtifact;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;

public class ExampleAddBackground {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() throws FileNotFoundException {
        // 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-Javaをご覧ください
        String myDir = "";
        // 新しいDocumentオブジェクトを作成する
        Document doc = new Document();
        // ドキュメントオブジェクトに新しいページを追加する
        Page page = doc.getPages().add();
        // BackgroundArtifactオブジェクトを作成する
        BackgroundArtifact background = new BackgroundArtifact();
        // BackgroundArtifactオブジェクトに画像を指定する
        background.setBackgroundImage(new FileInputStream(myDir + "logo.png"));
        // ページのアーティファクトコレクションにBackgroundArtifactを追加する
        page.getArtifacts().add(background);
        // ドキュメントを保存する
        doc.save(_dataDir + "BackGround.pdf");
    }
}
```
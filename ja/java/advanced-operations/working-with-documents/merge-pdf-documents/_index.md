---
title: プログラムによるPDFの結合
linktitle: PDFファイルの結合
type: docs
weight: 50
url: ja/java/merge-pdf-documents/
description: このページでは、Javaを使用してPDFドキュメントを単一のPDFファイルに結合する方法を説明します。
lastmod: "2021-06-05"
---

現在、PDFファイルを結合することは最も要求されるタスクの1つです。
この記事では、Aspose.PDF for Javaを使用して複数のPDFファイルを単一のPDFドキュメントに結合する方法を示します。例はJavaで書かれていますが、APIは他のプログラミング言語でも使用できます。PDFファイルは、最初のものが他のドキュメントの最後に結合されるようにマージされます。

## Javaを使用してPDFファイルを結合する

{{% alert color="primary" %}}

Aspose.PDFを使用してPDFファイルを結合し、このリンクでオンラインで結果を取得できます: [products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

2つのPDFファイルを連結するには:

1. 各入力PDFファイルを含む2つの[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)オブジェクトを作成します。

1. 次に、[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) コレクションの Add メソッドを、他の PDF ファイルを追加したい Document オブジェクトに対して呼び出します。
1. 2番目の Document オブジェクトの PageCollection コレクションを、最初の PageCollection コレクションの Add メソッドに渡します。
1. 最後に、Save メソッドを使用して出力 PDF ファイルを保存します。

以下のコードスニペットは、Java を使用して PDF ファイルを連結する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMerge {
    // ドキュメントディレクトリへのパス。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Merge() {
        
        // 最初のドキュメントを開く
        Document pdfDocument1 = new Document(_dataDir + "Concat1.pdf");
        // 2番目のドキュメントを開く
        Document pdfDocument2 = new Document(_dataDir + "Concat2.pdf");

        // 2番目のドキュメントのページを最初のドキュメントに追加
        pdfDocument1.getPages().add(pdfDocument2.getPages());

        // 連結された出力ファイルを保存
        pdfDocument1.save(_dataDir+"ConcatenatePdfFiles_out.pdf");

    }

}
```
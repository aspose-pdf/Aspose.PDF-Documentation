---  
title: PDFをプログラムで分割する  
linktitle: PDFファイルを分割する  
type: docs  
weight: 60  
url: /java/split-document/  
description: このトピックでは、JavaアプリケーションでPDFページを個別のPDFファイルに分割する方法を示します。  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---  

{{% alert color="primary" %}}  

Aspose.PDFを使用してPDFファイルを分割し、このリンクで結果をオンラインで取得できます：[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)  

{{% /alert %}}  

このトピックでは、Aspose.PDF for Javaを使用してJavaアプリケーション内でPDFページを個別のPDFファイルに分割する方法を示します。Javaを使用してPDFページを単一ページのPDFファイルに分割するには、次の手順に従います：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) コレクションを通じてPDFドキュメントのページをループします。

1. 各反復処理で、新しい Document オブジェクトを作成し、個々の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) オブジェクトを空のドキュメントに追加します。
1. Save メソッドを使用して新しい PDF を保存します。

次の Java コードスニペットは、PDF ページを個々の PDF ファイルに分割する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSplit {
    // ドキュメントディレクトリへのパス。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {
        
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "SplitToPages.pdf");

        int pageCount = 1;

        // すべてのページをループする
        for(Page pdfPage : pdfDocument.getPages())
        {
            Document newDocument = new Document();
            newDocument.getPages().add(pdfPage);
            newDocument.save(_dataDir + "page_" + pageCount + "_out" + ".pdf");
            pageCount++;
        }
    }

}
```
---
title: PDFにページ番号を追加する
linktitle: ページ番号を追加
type: docs
weight: 100
url: ja/java/add-page-number/
description: Aspose.PDF for Javaを使用すると、PageNumber Stampクラスを使用してPDFファイルにページ番号のスタンプを追加できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

すべての文書にはページ番号が含まれている必要があります。ページ番号により、読者が文書の異なる部分を見つけやすくなります。**Aspose.PDF for Java**を使用すると、PageNumberStampでページ番号を追加できます。

{{% alert color="primary" %}}

オンラインで試してみてください。Aspose.PDFの変換品質を確認し、このリンクで結果をオンラインで表示できます。[products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

[PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp)クラスを使用して、PDF文書にページ番号スタンプを追加できます。
 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) クラスは、フォーマット、余白、配置、開始番号などのページ番号ベースのスタンプを作成するためのメソッドを提供します。ページ番号スタンプを追加するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトと必要なプロパティを持つ [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) オブジェクトを作成する必要があります。その後、PDFファイルにスタンプを追加するために [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスの [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.Page#addStamp-com.aspose.pdf.Stamp-) メソッドを呼び出すことができます。また、ページ番号スタンプのフォント属性を設定することもできます。

次のコードスニペットは、PDFファイルにページ番号を追加する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleAddPageNumberToPDF {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // ページ番号スタンプを作成
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // スタンプが背景かどうか
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // テキストプロパティを設定
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // 特定のページにスタンプを追加
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // 出力ドキュメントを保存
        pdfDocument.save(_dataDir);

    }
}
```
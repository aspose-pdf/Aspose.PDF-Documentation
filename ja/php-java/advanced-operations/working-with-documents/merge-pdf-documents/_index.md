---
title: PDFをプログラムで結合
linktitle: PDFファイルを結合
type: docs
weight: 50
url: /ja/php-java/merge-pdf-documents/
description: このページでは、PHPを使用して複数のPDFドキュメントを単一のPDFファイルに結合する方法を説明します。
lastmod: "2024-06-05"
---

今や、PDFファイルを結合することは最も求められるタスクの一つです。
この記事では、Aspose.PDF for PHP via Javaを使用して、複数のPDFファイルを単一のPDFドキュメントに結合する方法を示します。例はJavaで書かれていますが、APIは他のプログラミング言語でも使用できます。PDFファイルは、最初のファイルが他のドキュメントの末尾に結合される形で結合されます。

## PHPを使用してPDFファイルを結合

{{% alert color="primary" %}}

Aspose.PDFを使用してPDFファイルを結合し、このリンクでオンラインで結果を取得できます: [Merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

2つのPDFファイルを連結するには：

1. 2つの[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)オブジェクトを作成し、それぞれに入力PDFファイルの一つを含めます。

1. 次に、他のPDFファイルを追加したいDocumentオブジェクトに対して、[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection)コレクションのAddメソッドを呼び出します。
1. 2番目のDocumentオブジェクトのPageCollectionコレクションを、最初のPageCollectionコレクションのAddメソッドに渡します。
1. 最後に、Saveメソッドを使用して出力PDFファイルを保存します。

以下のコードスニペットは、PHPを使用してPDFファイルを連結する方法を示しています。

```php
    // 最初のドキュメントを開く
    $document1 = new Document($inputFile1);
    
    // 2番目のドキュメントを開く
    $document2 = new Document($inputFile2);

    // 2番目のドキュメントのページを最初のドキュメントに追加する
    $document1->getPages()->add($document2->getPages());

    // 連結された出力ファイルを保存する
    $document1->save($outputFile);
    $document1->close();
    $document2->close();
```
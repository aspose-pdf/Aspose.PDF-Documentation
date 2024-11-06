---
title: PDF/AをPDF形式に変換する 
linktitle: PDF/AをPDF形式に変換する
type: docs
weight: 110
url: ja/php-java/convert-pdfa-to-pdf/
lastmod: "2024-05-20"
description: このトピックでは、Aspose.PDFがPHPライブラリでPDF/AファイルをPDFドキュメントに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF/AドキュメントをPDFに変換する

PDF/AドキュメントをPDFに変換することは、元のドキュメントから<abbr title="Portable Document Format Archive">PDF/A</abbr>の制限を除去することを意味します。クラス[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)には、入力/ソースファイルからPDFの準拠情報を削除するためのメソッドremovePdfaCompliance(..)があります。

```php
// 入力ファイルでDocumentクラスの新しいインスタンスを作成します
$document = new Document($inputFile);

// ドキュメントからPDF/A準拠を削除します
$document->removePdfaCompliance();

// 変更されたドキュメントを出力ファイルに保存します
$document->save($outputFile);
```

この情報は、ドキュメントに変更を加えた場合にも削除されます（例：
 ページを追加します）。次の例では、ページを追加した後、出力ドキュメントがPDF/A準拠を失います。

```php
// 入力ファイルでDocumentクラスの新しいインスタンスを作成します
$document = new Document($inputFile);

// ドキュメントからPDF/A準拠を削除します
$document->getPages()->add();

// 修正されたドキュメントを出力ファイルに保存します
$document->save($outputFile);
```
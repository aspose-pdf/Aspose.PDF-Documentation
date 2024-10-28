---
title: PHPでPDFからメタデータを削除
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - メタデータを削除

**Aspose.PDF Java for PHP**を使用してPDFドキュメントからメタデータを削除するには、単に**RemoveMetadata**クラスを呼び出します。

PHPコード

```php

# PDFドキュメントを開きます。
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# 新しい情報で更新されたドキュメントを保存します
$doc->save($dataDir . "Remove_Metadata.pdf");

print "メタデータを正常に削除しました。出力ファイルを確認してください。" . PHP_EOL;

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Remove Metadata (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
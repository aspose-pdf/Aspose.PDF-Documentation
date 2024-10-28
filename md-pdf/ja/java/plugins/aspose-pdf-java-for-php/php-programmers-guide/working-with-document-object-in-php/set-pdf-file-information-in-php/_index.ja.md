---
title: PHPでPDFファイル情報を設定する
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDFファイル情報の設定

**Aspose.PDF Java for PHP**を使用してPDFドキュメント情報を更新するには、単に**SetPdfFileInfo**クラスを呼び出します。

PHPコード

```php

# PDFドキュメントを開く。
$doc = new Document($dataDir . "input1.pdf");

# ドキュメント情報を取得
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF情報");
$doc_info->setTitle("PDFドキュメント情報の設定");

# 新しい情報で更新されたドキュメントを保存
$doc->save($dataDir . "Updated_Information.pdf");

print "ドキュメント情報を更新しました。出力ファイルを確認してください。";

```

**コードのダウンロード**

下記のいずれかのソーシャルコーディングサイトから**Set PDF File Information (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
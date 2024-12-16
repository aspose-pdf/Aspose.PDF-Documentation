---
title: PHPでPDFファイルの特定のページを取得する
type: docs
weight: 30
url: /ja/java/get-a-particular-page-in-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - ページを取得

**Aspose.PDF Java for Ruby**を使用してPDFドキュメント内の特定のページを取得するには、単に**GetPage**クラスを呼び出します。

Rubyコード

```php

# ターゲットドキュメントを開く
$pdf = new Document($dataDir . 'input1.pdf');

# ページコレクションの特定のインデックスでページを取得
$pdf_page = $pdf->getPages()->get_Item(1);

# 新しいDocumentオブジェクトを作成
$new_document = new Document();

# 新しいドキュメントオブジェクトのページコレクションにページを追加
$new_document->getPages()->add($pdf_page);

# 新しく生成されたPDFファイルを保存
$new_document->save($dataDir . "output.pdf");

print "プロセスが正常に完了しました！";

```

## 実行中のコードをダウンロード

以下のいずれかのソーシャルコーディングサイトから**Get Page (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)
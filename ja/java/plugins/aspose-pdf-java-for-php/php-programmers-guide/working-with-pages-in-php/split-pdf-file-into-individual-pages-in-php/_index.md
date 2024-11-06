---
title: PHPでPDFファイルを個々のページに分割する
type: docs
weight: 80
url: ja/java/split-pdf-file-into-individual-pages-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - ページの分割

**Aspose.PDF Java for PHP**を使用してPDFドキュメントを個々のページに分割するには、**SplitAllPages**クラスを呼び出します。

PHPコード

```php

# 対象のドキュメントを開く
$pdf = new Document($dataDir . 'input1.pdf');

# すべてのページをループする
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # 新しいDocumentオブジェクトを作成する
    $new_document = new Document();

    # 特定のインデックスのページコレクションからページを取得する
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # 新しく生成されたPDFファイルを保存する
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "分割プロセスが正常に完了しました！";

```

**実行コードをダウンロードする**


以下のいずれかのソーシャルコーディングサイトから**Split Pages (Aspose.PDF)**をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)

```php
// すべてのページを個別のPDFファイルに分割する
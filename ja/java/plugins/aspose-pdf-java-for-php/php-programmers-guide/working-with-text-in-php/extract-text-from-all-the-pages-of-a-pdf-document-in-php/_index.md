---
title: PHPでPDFドキュメントのすべてのページからテキストを抽出する
type: docs
weight: 30
url: ja/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - すべてのページからテキストを抽出

**Aspose.PDF Java for PHP**を使用してPDFドキュメントのすべてのページからテキストを抽出するには、単に**ExtractTextFromAllPages**モジュールを呼び出します。
PHPコード

```php

# ターゲットドキュメントを開く
$pdf = new Document($dataDir . 'input1.pdf');

# テキストを抽出するためのTextAbsorberオブジェクトを作成する
$text_absorber = new TextAbsorber();

# 全ページに対してアブソーバーを受け入れる
$pdf->getPages()->accept($text_absorber);

# ドキュメントの特定のページからテキストを抽出するためには、accept(..)メソッドに対してそのインデックスを使用して特定のページを指定する必要があります。
# 特定のPDFページに対してアブソーバーを受け入れる
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# 抽出されたテキストを取得
$extracted_text = $text_absorber->getText();

# ライターを作成し、ファイルを開く
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# ファイルにテキストの行を書き込む
# tw.WriteLine(extractedText);
# ストリームを閉じる
$writer->close();

print "テキストが正常に抽出されました。出力ファイルを確認してください。" . PHP_EOL;

```


**コードのダウンロード**

任意の以下のソーシャルコーディングサイトから**すべてのページからテキストを抽出する (Aspose.PDF)** をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)
---
title: "PHP での PDF ドキュメントのすべてのページからテキストの抽出"
linktitle: "PHP での PDF ドキュメントのすべてのページからテキストの抽出"
type: docs
weight: 30
url: /ja/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
description: "Aspose.PDF を使用して、PHP で PDF ドキュメントのすべてのページからテキストを抽出する方法をご紹介します。"
lastmod: "2026-10-06"
---
## Aspose.PDF - すべてのページからテキストの抽出

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントのすべてのページからテキストを抽出するには、**ExtractTextFromAllPages** モジュールを呼び出してください。
PHPコード

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# create TextAbsorber object to extract text
$text_absorber = new TextAbsorber();

# accept the absorber for all the pages
$pdf->getPages()->accept($text_absorber);

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.
# accept the absorber for particular PDF page
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text
$extracted_text = $text_absorber->getText();

# create a writer and open the file
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# write a line of text to the file
# tw.WriteLine(extractedText);
# close the stream
$writer->close();

print "Text extracted successfully. Check output file." . PHP_EOL;

```

**実行コードのダウンロード**

**すべてのページからテキストを抽出 (Aspose.PDF)** を以下のいずれかのソーシャルコーディングサイトからダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)

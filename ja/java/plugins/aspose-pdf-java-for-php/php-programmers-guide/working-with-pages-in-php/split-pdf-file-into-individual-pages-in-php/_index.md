---
title: "PHP での PDFファイルの個別ページへの分割"
linktitle: "PHP での PDFファイルの個別ページへの分割"
type: docs
weight: 80
url: /ja/java/split-pdf-file-into-individual-pages-in-php/
description: "PHPとAspose.PDFを使用して、PDFドキュメントを個別ページに分割する方法を学び、効率的なページ抽出を実現します。"
lastmod: "2026-10-06"
---
## Aspose.PDF - ページ分割

**Aspose.PDF Java for PHP** を使用してPDFドキュメントを個別ページに分割するには、単に **SplitAllPages** クラスを呼び出してください。

PHPコード

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# loop through all the pages
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # create a new Document object
    $new_document = new Document();

    # get the page at particular index of Page Collection
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # save the newly generated PDF file
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "Split process completed successfully!";

```

**実行コードをダウンロード**

以下に記載されたソーシャルコーディングサイトから **Split Pages (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)

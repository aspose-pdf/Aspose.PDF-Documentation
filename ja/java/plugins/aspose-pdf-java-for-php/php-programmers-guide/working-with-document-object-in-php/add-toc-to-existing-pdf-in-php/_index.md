---
title: 既存のPDFにTOCを追加するPHP
type: docs
weight: 20
url: ja/java/add-toc-to-existing-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - TOCを追加

**Aspose.PDF Java for PHP**を使用してPdfドキュメントにTOCを追加するには、単に**AddToc**クラスを呼び出します。

PHPコード

```php

# PDFドキュメントを開く
$doc = new Document($dataDir . "input1.pdf");

# PDFファイルの最初のページにアクセス
$toc_page = $doc->getPages()->insert(1);

# TOC情報を表すオブジェクトを作成
$toc_info = new TocInfo();
$title = new TextFragment("目次");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# TOCのタイトルを設定
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# TOC要素として使用される文字列オブジェクトを作成
$titles = array("最初のページ", "2ページ目");

$i = 0;
while ($i < 2){

    # 見出しオブジェクトを作成
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # 見出しオブジェクトの宛先ページを指定
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # 宛先ページ
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # 宛先座標
    $segment2->setText($titles[$i]);

    # TOCを含むページに見出しを追加
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# PDFドキュメントを保存
$doc->save($dataDir . "TOC.pdf");

print "TOCが正常に追加されました。出力ファイルを確認してください。";

```


**コードの実行をダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Add TOC (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)
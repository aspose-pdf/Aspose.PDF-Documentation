---
title: PDF から段落を抽出する
linktitle: 段落を抽出
type: docs
weight: 20
url: /ja/php-java/extract-paragraph-from-pdf/
description: この記事では、Aspose.PDF の特別なツールである ParagraphAbsorber を使用して PDF ドキュメントからテキストを抽出する方法について説明します。
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF ドキュメントから段落形式でテキストを抽出する

特定のテキスト（「プレーンテキスト」または「正規表現」を使用）を単一ページまたは全体のドキュメントから検索することで、PDF ドキュメントからテキストを取得することができます。または、単一ページ、ページ範囲、またはドキュメント全体の完全なテキストを取得することも可能です。しかし、場合によっては、PDF ドキュメントから段落を抽出したり、段落形式でテキストを取得する必要があります。PDF ドキュメントページのテキスト内でセクションや段落を検索する機能を実装しました。PDF ドキュメントから段落を抽出するために使用できる ParagraphAbsorber クラス（TextFragmentAbsorber や TextAbsorber のようなもの）を導入しました。

### 段落コレクションを反復処理してそのテキストを取得する


```php

// 既存のPDFファイルを開く
$document = new Document($inputFile);
// ParagraphAbsorberをインスタンス化
$absorber = new ParagraphAbsorber();
$absorber->visit($document);
$responseData = "";

foreach ($absorber->getPageMarkups() as $markup) {
    $i = 1;

    foreach ($markup->getSections() as $section) {
        $j = 1;

        foreach ($section->getParagraphs() as $paragraph) {
            $paragraphText = "\r\n";

            foreach ($paragraph->getLines() as $line) {
                foreach ($line as $fragment) {
                    $paragraphText = $paragraphText . $fragment->getText();
                }
                $paragraphText = $paragraphText . "\r\n";
            }
            $paragraphText = $paragraphText . "\r\n";

            $responseData = $responseData . "ページのセクション " . $i++ . " の段落 " . $j++ . ":" . markup->getNumber();
            $responseData = $responseData . $paragraphText;
            $j++;
        }
        $i++;
    }
}

// 抽出されたテキストを出力ファイルに保存
file_put_contents($outputFile, $responseData);
```
---
title: PDF スティッキー注釈
linktitle: スティッキー注釈
type: docs
weight: 50
url: ja/php-java/sticky-annotations/
description: このトピックはスティッキー注釈についてであり、例としてテキスト内のウォーターマーク注釈を示しています。ページ上のグラフィックを表現するために使用されます。このタスクを解決するコードスニペットをチェックしてください。
lastmod: "2024-06-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ウォーターマーク注釈を追加

ウォーターマーク注釈は、印刷されたページの寸法にかかわらず、ページ上の固定サイズおよび位置で印刷されるグラフィックスを表現するために使用されます。

[WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) を使用して、PDFページの特定の位置にウォーターマークテキストを追加できます。ウォーターマークの不透明度も不透明度プロパティを使用して制御できます。

以下のコードスニペットを確認して、WatermarkAnnotationを追加してください。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    $fontRepository = new FontRepository();
    $colors = new Color();
    // 特定のページを取得
    $page = $document->getPages()->get_Item(1);
    
    // 注釈を作成
    $wa = new WatermarkAnnotation($page, new Rectangle(100, 500, 400, 600));

    // 注釈をページの注釈コレクションに追加
    $page->getAnnotations()->add($wa);

    // フォント設定のためのTextStateを作成
    $ts = new TextState();

    $ts->setForegroundColor($colors->getBlue());
    $ts->setFont($fontRepository->findFont("Times New Roman"));
    $ts->setFontSize(32);

    // 注釈テキストの不透明度レベルを設定
    $wa->setOpacity(0.5);
            
    $watermarkStrings = ["Aspose.PDF", "Watermark", "Demo" ];
    // 注釈にテキストを追加
    $wa->setTextAndState($watermarkStrings, $ts);

    // 結果のPDFドキュメントを保存
    $document->save($outputFile);
    $document->close();
```
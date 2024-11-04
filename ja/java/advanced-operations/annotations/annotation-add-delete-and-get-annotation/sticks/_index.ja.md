---
title: PDF スティッキー注釈 
linktitle: スティッキー注釈
type: docs
weight: 50
url: /java/sticky-annotations/
description: このトピックはスティッキー注釈についてです。例として、テキストに透かし注釈を示します。ページ上にグラフィックを表すために使用されます。このタスクを解決するためのコードスニペットを確認してください。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 透かし注釈の追加

透かし注釈は、印刷されるページの寸法に関係なく、ページ上の固定サイズと位置で印刷されるグラフィックを表すために使用されます。

PDFページの特定の位置に[WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation)を使用して透かしテキストを追加できます。透かしの不透明度は、不透明度プロパティを使用して制御することもできます。

透かし注釈を追加するには、次のコードスニペットを確認してください。

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWatermarkAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddWaterMarkAnnotation()
    {
        // PDFファイルをロードする
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // 注釈を作成する
        WatermarkAnnotation wa = new WatermarkAnnotation(page, new Rectangle(100, 500, 400, 600));

        // 注釈をページの注釈コレクションに追加
        page.getAnnotations().add(wa);

        // フォント設定のためのTextStateを作成する
        TextState ts = new TextState();

        ts.setForegroundColor(Color.getBlue());
        ts.setFont(FontRepository.findFont("Times New Roman"));
        ts.setFontSize(32);

        // 注釈テキストの不透明度レベルを設定する
        wa.setOpacity(0.5);

        // 注釈にテキストを追加する
        wa.setTextAndState(new String[] { "Aspose.PDF", "Watermark", "Demo" }, ts);

        // ドキュメントを保存する
        document.save(_dataDir + "sample_watermark.pdf");
    }
}
```


## ウォーターマーク注釈を取得する

```java
    public static void GetWatermarkAnnotation() {
        // PDFファイルを読み込む
        Document document = new Document(_dataDir + "sample_watermark.pdf");

        // AnnotationSelectorを使用して注釈をフィルタリングする
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new WatermarkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

        // 結果を出力する
        for (Annotation fa : WatermarkAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## ウォーターマーク注釈を削除する

```java
    public static void DeleteWatermarkAnnotation() {
         // PDFファイルを読み込む
         Document document = new Document(_dataDir + "sample_watermark.pdf");

         // AnnotationSelectorを使用して注釈をフィルタリングする
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new WatermarkAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

         // 注釈を削除する
         for (Annotation fa : WatermarkAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_watermark_del.pdf");
    }
```
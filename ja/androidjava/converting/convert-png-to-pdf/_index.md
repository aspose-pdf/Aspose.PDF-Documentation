---
title: PNG を PDF に変換
linktitle: PNG を PDF に変換
type: docs
weight: 200
url: /ja/androidjava/convert-png-to-pdf/
lastmod: "2026-07-01"
description: この記事では、Android の Java アプリケーションで Aspose.PDF ライブラリを使用して PNG を PDF に変換する方法を示します。シンプルな手順で PNG 画像を PDF フォーマットに変換できます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** は PNG 画像を PDF フォーマットに変換する機能をサポートしています。次のコードスニペットでタスクを実現する方法を確認してください。

<abbr title="Portable Network Graphics">PNG</abbr> は、ロスレス圧縮を使用するラスタ画像ファイル形式の一種であり、ユーザーに人気があります。

以下の手順で PNG を PDF 画像に変換できます：

1. 入力 PNG 画像を読み込む
1. 高さと幅の値を読み取ります
1. 新しいドキュメントを作成し、ページを追加します
1. ページの寸法を設定します
1. 出力ファイルを保存します

さらに、以下のコードスニペットは、JavaアプリケーションでPNGをPDFに変換する方法を示しています:

```java
    public void convertPNGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.png");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
```


---
title: PNGをPDFに変換 
linktitle: PNGをPDFに変換
type: docs
weight: 200
url: /ja/androidjava/convert-png-to-pdf/
lastmod: "2021-06-05"
description: この記事では、JavaアプリケーションでAspose.PDFライブラリを使用してPNGをPDFに変換する方法を示します。シンプルな手順でPNG画像をPDF形式に変換できます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** はPNG画像をPDF形式に変換する機能をサポートしています。次のコードスニペットをチェックして、タスクを実現してください。

<abbr title="Portable Network Graphics">PNG</abbr>は、無損失圧縮を使用するラスター画像ファイル形式の一種であり、ユーザーの間で人気があります。

以下の手順でPNGをPDF画像に変換できます：

1. 入力PNG画像を読み込む
1. 高さと幅の値を読み取る
1. 新しいドキュメントを作成し、ページを追加
1. ページの寸法を設定
1. 出力ファイルを保存

さらに、以下のコードスニペットは、JavaアプリケーションでPNGをPDFに変換する方法を示しています：

```java
    public void convertPNGtoPDF () {
        // ドキュメントオブジェクトを初期化
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
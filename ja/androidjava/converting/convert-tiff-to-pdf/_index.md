---
title: TIFF を PDF に変換
linktitle: TIFF を PDF に変換
type: docs
weight: 210
url: /ja/androidjava/convert-tiff-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java は、マルチページまたはマルチフレームの TIFF 画像を PDF アプリケーションに変換することを可能にします。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** は、単一フレームまたはマルチフレームの <abbr title="Tag Image File Format">TIFF</abbr> 画像をサポートするファイル形式です。つまり、Java アプリケーションで TIFF 画像を PDF に変換できます。

TIFF または TIF（Tagged Image File Format）は、このファイル形式標準に準拠したさまざまなデバイスでの使用を想定したラスタ画像を表します。TIFF 画像は、異なる画像を含む複数のフレームを持つことができます。Aspose.PDF も単一フレームまたはマルチフレームの TIFF 画像をサポートします。そのため、Java アプリケーションで TIFF 画像を PDF に変換できます。以下の手順で、マルチページ TIFF 画像をマルチページ PDF ドキュメントに変換する例を考えます：

1. Document クラスのインスタンスを作成します
1. 入力 TIFF 画像を読み込む
1. フレームの FrameDimension を取得する
1. 各フレームごとに新しいページを追加する
1. 最後に、画像を PDF ページに保存する

さらに、次のコードスニペットは、マルチページまたはマルチフレーム TIFF 画像を PDF に変換する方法を示しています。

```java
 public void convertTIFFtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.tiff");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample TIFF image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


---
title: JPG を PDF に変換する
linktitle: JPG を PDF に変換する
type: docs
weight: 190
url: /ja/androidjava/convert-jpg-to-pdf/
lastmod: "2026-07-01"
description: JPG 画像を PDF ファイルに簡単に変換する方法を学びましょう。また、画像をページと同じ高さと幅の PDF に変換することもできます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

JPG を PDF に変換する方法を悩む必要はありません。なぜなら Apose.PDF for Android via Java ライブラリが最適な解決策を提供しているからです。

以下の手順に従って、Aspose.PDF for Android via Java を使用すれば、JPG 画像を PDF に非常に簡単に変換できます：

1. オブジェクトを初期化する [ドキュメント](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラス
1. JPG画像を読み込み、段落に追加する
1. 出力PDFを保存

以下のコードスニペットは、JPG画像をPDFに変換する方法を示しています:

```java
public void convertJPEGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.jpg");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample JPEG image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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

---
title: BMP を PDF に変換する
linktitle: BMP を PDF に変換する
type: docs
weight: 220
url: /ja/androidjava/convert-bmp-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF. for Android via Java を使用して、ディスプレイ デバイスから独立してデジタル ビットマップ画像を保存するための PDF に BMP ビットマップ ファイルを簡単に変換できます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

BMP 画像は、拡張子 .BMP を持つファイルで、ビットマップ画像ファイルを表し、ビットマップ デジタル画像の保存に使用されます。これらの画像はグラフィック アダプタに依存せず、デバイス非依存ビットマップ (DIB) ファイル形式とも呼ばれます。
Aspose.PDF for Java API を使用して BMP を PDF に変換できます。したがって、BMP 画像を変換するために次の手順に従うことができます：

1. 新しい Document を初期化する
1. サンプル BMP 画像ファイルをロードする
1. 最後に、出力PDFファイルを保存します

以下のコードスニペットはこれらの手順に従い、Java を使用して BMP を PDF に変換する方法を示しています:

```java
public void convertBMPtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.bmp");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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


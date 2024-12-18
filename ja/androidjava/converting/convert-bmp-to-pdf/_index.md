---
title: BMPをPDFに変換する
linktitle: BMPをPDFに変換する
type: docs
weight: 220
url: /ja/androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: ディスプレイデバイスから独立してデジタルビットマップ画像を保存するために使用されるBMPビットマップファイルを、Aspose.PDFを使用して簡単にPDFに変換できます。Java経由でAndroid用。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

BMP画像は、拡張子.BMPを持つファイルで、ビットマップ画像ファイルを表し、ビットマップデジタル画像を保存するために使用されます。これらの画像はグラフィックスアダプタに依存せず、デバイス独立ビットマップ（DIB）ファイル形式とも呼ばれます。  
Aspose.PDF for Java APIを使用してBMPをPDFに変換できます。そのため、次の手順に従ってBMP画像を変換できます：

1. 新しいドキュメントを初期化する
2. サンプルのBMP画像ファイルをロードする
3. 最後に、出力PDFファイルを保存する

次のコードスニペットはこれらの手順に従い、Javaを使用してBMPをPDFに変換する方法を示しています：

```java
public void convertBMPtoPDF () {
        // ドキュメントオブジェクトを初期化する
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

        // サンプルのBMP画像ファイルをロードする
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

        // 出力ドキュメントを保存する
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
---
title: JPGをPDFに変換する
linktitle: JPGをPDFに変換する
type: docs
weight: 190
url: /androidjava/convert-jpg-to-pdf/
lastmod: "2021-06-05"
description: JPG画像をPDFファイルに簡単に変換する方法を学びます。また、ページの高さと幅に合わせて画像をPDFに変換することもできます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

JPGをPDFに変換する方法に悩む必要はありません。Apose.PDF for Android via Javaライブラリには最適な解決策があります。

Aspose.PDF for Android via Javaを使用して、以下の手順でJPG画像をPDFに非常に簡単に変換できます：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスのオブジェクトを初期化する
1. JPG画像を読み込み、段落に追加する
1. 出力PDFを保存する

以下のコードスニペットは、JPG画像をPDFに変換する方法を示しています：

```java
public void convertJPEGtoPDF () {
        // ドキュメントオブジェクトを初期化
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

        // サンプルJPEG画像ファイルを読み込む
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

        // 出力ドキュメントを保存
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
---
title: TIFFをPDFに変換する
linktitle: TIFFをPDFに変換する
type: docs
weight: 210
url: /ja/androidjava/convert-tiff-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Javaは、複数ページまたは複数フレームのTIFF画像をPDFアプリケーションに変換できます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** ファイル形式に対応しており、単一フレームまたはマルチフレームの<abbr title="Tag Image File Format">TIFF</abbr>画像であっても問題ありません。つまり、JavaアプリケーションでTIFF画像をPDFに変換することができます。

TIFFまたはTIF、Tagged Image File Formatは、このファイル形式の標準に準拠した様々なデバイスで使用されることを目的としたラスター画像を表します。
 TIFF画像は、異なる画像を持つ複数のフレームを含むことができます。Aspose.PDFファイル形式もサポートされており、単一フレームまたはマルチフレームのTIFF画像のどちらでも対応可能です。したがって、JavaアプリケーションでTIFF画像をPDFに変換することができます。以下のステップで、マルチページTIFF画像をマルチページPDFドキュメントに変換する例を考えます。

1. Documentクラスのインスタンスを作成する
1. 入力TIFF画像を読み込む
1. フレームのFrameDimensionを取得する
1. 各フレームに新しいページを追加する
1. 最後に、画像をPDFページに保存する

さらに、以下のコードスニペットは、マルチページまたはマルチフレームTIFF画像をPDFに変換する方法を示しています:

```java
 public void convertTIFFtoPDF () {
        // ドキュメントオブジェクトを初期化
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

        // サンプルTIFF画像ファイルを読み込む
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

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
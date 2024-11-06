---
title: PDFをPNGに変換する
linktitle: PDFをPNGに変換する
type: docs
weight: 20
url: ja/androidjava/convert-pdf-to-png/
lastmod: "2021-06-05"
description: このページでは、Aspose.PDF for Android via Javaを使用してPDFページをPNG画像に変換する方法、すべてのページおよび単一ページをPNG画像に変換する方法について説明します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java**ライブラリを使用して、PDFページを<abbr title="Portable Network Graphics">PNG</abbr>画像に変換することができます。

PngDeviceクラスを使用すると、PDFページをPNG画像に変換することができます。このクラスは、PDFファイルの特定のページをPNG画像形式に変換するためのProcessという名前のメソッドを提供します。

## PDFページをPNG画像に変換する

PDFファイル内のすべてのページをPNGファイルに変換するには、各ページを繰り返し処理し、それぞれをPNG形式に変換します。以下のコードスニペットは、PDFファイル内のすべてのページを巡回し、それぞれをPNG画像に変換する方法を示しています。

{{% alert color="primary" %}}

オンラインで試してください。Aspose.PDFの変換の品質を確認し、オンラインで結果を表示することができます。このリンクでチェックしてください: [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## 単一のPDFページをPNG画像に変換

ページインデックスをProcess(..)メソッドの引数として渡します。
次のコードスニペットは、PDFの最初のページをPNG形式に変換する手順を示しています。

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // 出力画像を保存するためのストリームオブジェクトを作成
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // 解像度オブジェクトを作成
            Resolution resolution = new Resolution(300);

            // 特定の解像度でPngDeviceオブジェクトを作成
            PngDevice PngDevice = new PngDevice(resolution);

            // 特定のページを変換し、ストリームに画像を保存
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // ストリームを閉じる
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## すべてのPDFページをPNG画像に変換

Aspose.PDF for Android via Javaは、PDFファイル内のすべてのページを画像に変換する方法を示します：

1. ファイル内のすべてのページをループします。
1. 各ページを個別に変換します：
    1. PDFドキュメントを読み込むためにDocumentクラスのオブジェクトを作成します。
    1. 変換したいページを取得します。
    1. Processメソッドを呼び出してページをPngに変換します。

以下のコードスニペットは、すべてのPDFページをPNG画像に変換する方法を示しています。

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDFファイルのすべてのページをループします
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // 出力画像を保存するためのストリームオブジェクトを作成します
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Resolutionオブジェクトを作成します
            Resolution resolution = new Resolution(300);
            // 特定の解像度でJpegDeviceオブジェクトを作成します
            PngDevice JpegDevice = new PngDevice(resolution);

            // 特定のページを変換し、画像をストリームに保存します
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // ストリームを閉じます
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```


## 特定のPDFページをPNG画像に変換する

Aspose.PDF for Android via Javaを使用して、特定のページをPNG形式に変換する方法を示します:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // 特定のページ領域の長方形を取得
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // 望むページ領域の長方形に応じてCropBox値を設定
        document.getPages().get_Item(1).setCropBox(pageRect);
        // 切り取ったドキュメントをストリームに保存
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // ストリームから切り取ったPDFドキュメントを開き、画像に変換
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Resolutionオブジェクトを作成
        Resolution resolution = new Resolution(300);
        // 指定された属性でJpegデバイスを作成
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // 特定のページを変換し、画像をストリームに保存
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
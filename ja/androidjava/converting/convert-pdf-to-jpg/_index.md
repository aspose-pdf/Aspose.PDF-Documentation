---
title: PDFをJPGに変換する
linktitle: PDFをJPGに変換する
type: docs
weight: 10
url: ja/androidjava/convert-pdf-to-jpg/
description: このページでは、Aspose.PDF for Android via Javaを使用してPDFページをJPEG画像に変換する方法、すべてのページおよび単一ページをJPEG画像に変換する方法について説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFページをJPG画像に変換する

JpegDeviceクラスを使用すると、PDFページをJPEG画像に変換できます。このクラスは、PDFファイルの特定のページをJPEG画像に変換するprocess(..)という名前のメソッドを提供します。

{{% alert color="primary" %}}

オンラインで試すことができます。Aspose.PDFの変換品質を確認し、このリンクで結果をオンラインで表示できます [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## 単一のPDFページをJPG画像に変換する

Aspose.PDF for Android via Javaを使用すると、単一のページをJpeg形式に変換できます。

1ページだけをJPEG画像に変換するには：

1. 変換したいページを取得するために、Documentクラスのオブジェクトを作成します。  
1. ページをJPEG画像に変換するためにprocess(..)メソッドを呼び出します。

次のコードスニペットは、PDFの最初のページをJPEG形式に変換する手順を示しています。

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // 出力画像を保存するためのストリームオブジェクトを作成
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Resolutionオブジェクトを作成
            Resolution resolution = new Resolution(300);

            // 特定の解像度でJpegDeviceオブジェクトを作成
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // 特定のページを変換し、画像をストリームに保存
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // ストリームを閉じる
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```


## すべてのPDFページをJPG画像に変換

Aspose.PDF for Android via Javaを使用すると、PDFファイル内のすべてのページを画像に変換できます。

1. ファイル内のすべてのページをループします。
1. 各ページを個別に変換します：
    - PDFドキュメントをロードするためにDocumentクラスのオブジェクトを作成します。
    - 変換したいページを取得します。
    - Processメソッドを呼び出してページをJpegに変換します。

次のコードスニペットは、すべてのPDFページをJpeg画像に変換する方法を示しています。

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDFファイルのすべてのページをループする
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // 出力画像を保存するためのストリームオブジェクトを作成
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Resolutionオブジェクトを作成
            Resolution resolution = new Resolution(300);
            // 特定の解像度でJpegDeviceオブジェクトを作成
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // 特定のページを変換し、画像をストリームに保存
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // ストリームを閉じる
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


## 特定のPDFページをJPG画像に変換する

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // 特定のページ領域の矩形を取得
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // 希望するページ領域の矩形に応じてCropBoxの値を設定
        document.getPages().get_Item(1).setCropBox(pageRect);
        // 切り抜いたドキュメントをストリームに保存
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // ストリームから切り抜いたPDFドキュメントを開き、画像に変換
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // 解像度オブジェクトを作成
        Resolution resolution = new Resolution(300);
        // 指定された属性でJPEGデバイスを作成
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // 特定のページを変換し、ストリームに画像を保存
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
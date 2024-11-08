---
title: PDFをBMPに変換する
linktitle: PDFをBMPに変換する
type: docs
weight: 40
url: /ja/androidjava/convert-pdf-to-bmp/
lastmod: "2021-06-05"
description: この記事では、PDFページをBMP画像に変換する方法、すべてのページをBMP画像に変換する方法、および単一のPDFページをJavaでBMP画像に変換する方法について説明します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice)クラスを使用すると、PDFページを<abbr title="Bitmap Image File">BMP</abbr>画像に変換できます。このクラスは、PDFファイルの特定のページをBmp画像形式に変換することができる[Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process)というメソッドを提供します。

{{% alert color="primary" %}}

オンラインで試すことができます。Aspose.PDFの変換品質を確認し、結果をオンラインで表示するには、次のリンクをご覧ください：[products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

BmpDeviceクラスを使用すると、PDFページをBMP画像に変換できます。
 このクラスは、process(..)という名前のメソッドを提供し、PDFファイルの特定のページをBMP画像に変換することができます。

## PDFページをBMP画像に変換する

PDFページをBMP画像に変換するには、以下の手順を実行します。

1. Documentクラスのオブジェクトを作成し、変換したい特定のページを取得します。
1. ページをBMPに変換するために、process(..)メソッドを呼び出します。

次のコードスニペットは、特定のページをBMP画像に変換する方法を示しています。

```java
// PDFをBMPに変換
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // 出力画像を保存するためのストリームオブジェクトを作成
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Resolutionオブジェクトを作成
            Resolution resolution = new Resolution(300);

            // 特定の解像度でBmpDeviceオブジェクトを作成
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // 特定のページを変換し、画像をストリームに保存
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // ストリームを閉じる
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## すべてのPDFページをBMP画像に変換する

PDFファイルのすべてのページをBMP形式に変換するには、各ページを取得してBMP形式に変換する必要があります。次のコードスニペットは、PDFファイルのすべてのページを巡回してBMPに変換する方法を示しています。

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // PDFファイルのすべてのページをループする
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // 出力画像を保存するためのストリームオブジェクトを作成
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // 解像度オブジェクトを作成
            Resolution resolution = new Resolution(300);
            // 特定の解像度でBmpDeviceオブジェクトを作成
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // 特定のページを変換し、画像をストリームに保存
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

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


## 特定のページ領域を画像（DOM）に変換

Aspose.PDFの画像デバイスオブジェクトを使用して、PDFドキュメントをさまざまな画像形式に変換できます。ただし、特定のページ領域を画像形式に変換する必要がある場合があります。この要件を満たすためには、2つのステップで実行できます。最初にPDFページを目的の領域にクロップし、その後、目的の画像デバイスオブジェクトを使用して画像に変換します。

次のコードスニペットは、PDFページを画像に変換する方法を示しています。

```java
public void convertPDFtoBmp_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // 特定のページ領域の矩形を取得
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // 目的のページ領域の矩形に応じてCropBoxの値を設定
        document.getPages().get_Item(1).setCropBox(pageRect);
        // クロップされたドキュメントをストリームに保存
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // ストリームからクロップされたPDFドキュメントを開き、画像に変換
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // 解像度オブジェクトを作成
        Resolution resolution = new Resolution(300);
        // 指定された属性でBMPデバイスを作成
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // 特定のページを変換し、画像をストリームに保存
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```
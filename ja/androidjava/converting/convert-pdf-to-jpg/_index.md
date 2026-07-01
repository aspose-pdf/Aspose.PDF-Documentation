---
title: PDF を JPG に変換
linktitle: PDF を JPG に変換
type: docs
weight: 10
url: /ja/androidjava/convert-pdf-to-jpg/
description:  このページでは、Aspose.PDF for Android via Java を使用して PDF ページを JPEG 画像に変換する方法、すべてのページおよび単一ページを JPEG 画像に変換する方法について説明します。
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ページを JPG 画像に変換

JpegDevice クラスを使用すると、PDF ページを JPEG 画像に変換できます。このクラスは process(..) というメソッドを提供しており、PDF ファイルの特定のページを JPEG 画像に変換することができます。

{{% alert color="primary" %}}

オンラインでお試しください。Aspose.PDF 変換の品質を確認し、結果をオンラインでこのリンクから表示できます。  [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## 単一の PDF ページを JPG 画像に変換する

Aspose.PDF for Android via Java を使用すると、単一のページを Jpeg 形式に変換できます。

単一のページを JPEG 画像に変換するには:

1. 変換したいページを取得するために、Document クラスのオブジェクトを作成します。
1. ページを JPEG 画像に変換するために process(..) メソッドを呼び出します。

次のコードスニペットは、PDF の最初のページを Jpeg 形式に変換する手順を示しています。

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## すべての PDF ページを JPG 画像に変換する

Aspose.PDF for Android via Java を使用すると、PDF ファイル内のすべてのページを画像に変換できます:

1. ファイル内のすべてのページをループ処理します。
1. 各ページを個別に変換します:
    - PDFドキュメントを読み込むためにDocumentクラスのオブジェクトを作成します。
    - 変換したいページを取得します。
    - ページをJpegに変換するためにProcessメソッドを呼び出します。

以下のコードスニペットは、すべてのPDFページをJpeg画像に変換する方法を示しています。

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
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

## 特定の PDF ページを JPG 画像に変換する

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Jpeg device with specified attributes
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

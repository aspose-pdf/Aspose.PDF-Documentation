---
title: PDFをPNGに変換
linktitle: PDFをPNGに変換
type: docs
weight: 20
url: /ja/androidjava/convert-pdf-to-png/
lastmod: "2026-07-01"
description: このページでは、PDFページをPNG画像に変換する方法、およびAspose.PDF for Android via Javaを使用してすべてのページまたは単一ページをPNG画像に変換する方法について説明します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFページを<abbr title="Portable Network Graphics">PNG</abbr>画像に変換するために、**Aspose.PDF for Android via Java** ライブラリを使いやすく便利な方法で使用してください。

PngDeviceクラスを使用すると、PDFページをPNG画像に変換できます。このクラスはProcessという名前のメソッドを提供しており、PDFファイルの特定のページをPNG画像形式に変換することができます。

## PDF ページを PNG 画像に変換する

PDF ファイル内のすべてのページを PNG ファイルに変換するには、個々のページを繰り返し処理し、各ページを PNG 形式に変換します。以下のコードスニペットは、PDF ファイルのすべてのページを走査して各ページを PNG 画像に変換する方法を示しています。

{{% alert color="primary" %}} 

オンラインでお試しください。Aspose.PDF の変換品質を確認し、結果をオンラインでこのリンクから表示できます。 [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## 単一の PDF ページを PNG 画像に変換する

Process(..) メソッドの引数としてページインデックスを渡します。
次のコードスニペットは、PDF の最初のページを PNG 形式に変換する手順を示しています。

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create PngDevice object with particular resolution
            PngDevice PngDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## すべての PDF ページを PNG 画像に変換する

Aspose.PDF for Android via Java は、PDF ファイル内のすべてのページを画像に変換する方法を示します:

1. ファイル内のすべてのページをループ処理します。
1. 各ページを個別に変換します:
    1. PDF ドキュメントを読み込むために Document クラスのオブジェクトを作成します。
    1. 変換したいページを取得します。
    1. Process メソッドを呼び出して、ページを Png に変換します。

次のコードスニペットは、すべての PDF ページを PNG 画像に変換する方法を示しています。

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
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
            PngDevice JpegDevice = new PngDevice(resolution);

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

## 特定の PDF ページを PNG 画像に変換する

Aspose.PDF for Android via Java は、特定のページを PNG 形式に変換する方法を示します：

```java
public void convertPDFtoPNG_ParticularPageRegion() {
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
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

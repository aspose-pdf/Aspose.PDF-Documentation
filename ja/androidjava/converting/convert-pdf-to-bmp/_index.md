---
title: PDF を BMP に変換
linktitle: PDF を BMP に変換
type: docs
weight: 40
url: /ja/androidjava/convert-pdf-to-bmp/
lastmod: "2026-07-01"
description: この記事では、PDF ページを BMP 画像に変換する方法、すべてのページを BMP 画像に変換する方法、および Java を使用して単一の PDF ページを BMP 画像に変換する方法について説明します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

その [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) クラスは PDF ページを変換できるようにします <abbr title="Bitmap Image File">BMP</abbr> 画像。このクラスは、名前付きメソッドを提供します [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) PDF ファイルの特定のページを Bmp 画像形式に変換することを可能にします。

{{% alert color="primary" %}}

オンラインでお試しください。Aspose.PDF 変換の品質を確認し、結果をオンラインでこのリンクから表示できます。 [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

BmpDevice クラスを使用すると、PDF ページを BMP 画像に変換できます。このクラスは process(..) という名前のメソッドを提供しており、PDF ファイルの特定のページを BMP 画像に変換することができます。

## PDFページをBMP画像に変換する

PDFページをBMP画像に変換するには:

1. 変換したい特定のページを取得するために、Documentクラスのオブジェクトを作成します。
1. process(..) メソッドを呼び出して、ページを BMP に変換します。

次のコードスニペットは、特定のページを BMP 画像に変換する方法を示しています。

```java
//Convert PDF to BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## すべての PDF ページを BMP 画像に変換する

PDF ファイルのすべてのページを BMP 形式に変換するには、各ページを取得して BMP 形式に変換するためにイテレーションする必要があります。以下のコードスニペットは、PDF ファイルのすべてのページを走査して BMP に変換する方法を示しています。

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

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

## 特定のページ領域を画像 (DOM) に変換する

私たちは Aspose.PDF の image devices オブジェクトを使用して PDF ドキュメントをさまざまな Image 形式に変換できます。しかし、特定のページ領域を Image 形式に変換する必要がある場合もあります。この要件は 2 つの手順で満たすことができます。まず、PDF ページを目的の領域にトリミングし、次に目的の Image デバイス オブジェクトを使用して画像に変換します。

次のコード スニペットは、PDF ページを画像に変換する方法を示しています。

```java
public void convertPDFtoBmp_ParticularPageRegion() {
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
        // Create BMP device with specified attributes
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```

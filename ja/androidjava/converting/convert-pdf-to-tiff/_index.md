---
title: PDF を TIFF に変換
linktitle: PDF を TIFF に変換
type: docs
weight: 30
url: /ja/androidjava/convert-pdf-to-tiff/
lastmod: "2026-07-01"
description: この記事では、PDF ドキュメントのページを TIFF 画像に変換する方法について説明します。Aspose.PDF for Android via Android via Java を使用して、すべてのページまたは単一のページを TIFF 画像に変換する方法を学べます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** は PDF ページを TIFF  画像に変換できるようにします。

その [TiffDevice クラス](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) PDFページをTIFF画像に変換できます。このクラスは Process という名前のメソッドを提供しており、PDFファイル内のすべてのページを単一のTIFF画像に変換できます。

{{% alert color="primary" %}}

オンラインで試すことができます。Aspose.PDF の変換品質を確認し、結果をこのリンクでオンラインで表示できます。 [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## PDF ページを単一の TIFF 画像に変換

Aspose.PDF for Android via Java は、PDF ファイル内のすべてのページを単一の TIFF 画像に変換する方法を説明します:

1. Document クラスのオブジェクトを作成します。
1. ドキュメントを変換するには、Process メソッドを呼び出します。
1. 出力ファイルのプロパティを設定するには、TiffSettings クラスを使用します。

以下のコードスニペットは、すべての PDF ページを単一の TIFF 画像に変換する方法を示しています。

```java
public void convertPDFtoTiffSinglePage() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## 単一ページをTIFF画像に変換

Aspose.PDF for Android via Java は、PDF ファイル内の特定のページを TIFF 画像に変換することを可能にします。変換のためにページ番号を引数として受け取るオーバーロードされた Process(..) メソッドを使用します。次のコード スニペットは、PDF の最初のページを TIFF 形式に変換する方法を示しています。

```java
public void convertPDFtoTiffAllPages() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## 変換中にBradleyアルゴリズムを使用する

Aspose.PDF for Android via Java は、LZW 圧縮を使用して PDF を TIFF に変換する機能をサポートしており、さらに AForge を使用して二値化を適用できます。ただし、ある顧客から、一部の画像について Otsu を使用して閾値を取得する必要があるとの要望があり、Bradley も使用したいとのことです。

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }
```


---
title: PDFをTIFFに変換する
linktitle: PDFをTIFFに変換する
type: docs
weight: 30
url: /ja/androidjava/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: この記事では、PDFドキュメントのページをTIFF画像に変換する方法について説明します。Aspose.PDF for Android via Javaを使用して、すべてまたは単一のページをTIFF画像に変換する方法を学びます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** は、PDFページをTIFF画像に変換することを可能にします。

[TiffDeviceクラス](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice)を使用すると、PDFページをTIFF画像に変換できます。このクラスは、PDFファイル内のすべてのページを単一のTIFF画像に変換するProcessという名前のメソッドを提供します。

{{% alert color="primary" %}}

オンラインで試してみてください。このリンクでAspose.PDFの変換品質を確認し、結果をオンラインで見ることができます：[products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## PDFページを1つのTIFF画像に変換

Aspose.PDF for Android via Javaは、PDFファイル内のすべてのページを1つのTIFF画像に変換する方法を説明します：

1. Documentクラスのオブジェクトを作成します。
1. ドキュメントを変換するためにProcessメソッドを呼び出します。
1. 出力ファイルのプロパティを設定するには、TiffSettingsクラスを使用します。

以下のコードスニペットは、すべてのPDFページを1つのTIFF画像に変換する方法を示しています。

```java
public void convertPDFtoTiffSinglePage() {
        // ドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 解像度オブジェクトを作成
        Resolution resolution = new Resolution(300);

        // TiffSettingsオブジェクトを作成
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // TIFFデバイスを作成
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // 特定のページを変換し、画像をストリームに保存
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## 単一ページをTIFF画像に変換

Aspose.PDF for Android via Javaを使用すると、PDFファイルの特定のページをTIFF画像に変換できます。変換の引数としてページ番号を取るProcess(..)メソッドのオーバーロードされたバージョンを使用します。以下のコードスニペットは、PDFの最初のページをTIFF形式に変換する方法を示しています。

```java
public void convertPDFtoTiffAllPages() {
        // ドキュメントを開く
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 解像度オブジェクトを作成
        Resolution resolution = new Resolution(300);

        // TiffSettingsオブジェクトを作成
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // TIFFデバイスを作成
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // 特定のページを変換し、ストリームに画像を保存
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```


## 変換中にBradleyアルゴリズムを使用

Aspose.PDF for Android via Javaは、LZW圧縮を使用してPDFをTIFFに変換する機能をサポートしており、その後AForgeを使用して二値化を適用できます。しかし、ある顧客は、いくつかの画像に対してOtsuを使用して閾値を取得する必要があると要求したため、Bradleyも使用したいと考えています。

```java
public void convertPDFtoTiffBradleyBinarization() {
        // Aspose.PDF for Androidでは未実装
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        // Aspose.PDF for Androidでは未実装
        throw new NotImplementedException();
    }
```
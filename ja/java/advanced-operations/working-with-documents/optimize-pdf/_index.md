---
title: JavaでPDFサイズを最適化、圧縮、または縮小
linktitle: PDFドキュメントを最適化
type: docs
weight: 40
url: ja/java/optimize-pdf/
description: PDFファイルを最適化し、すべての画像を縮小し、PDFサイズを縮小し、フォントを埋め込まず、未使用のオブジェクトをJavaで削除します。
lastmod: "2021-06-05"
---

PDFドキュメントには、追加のデータが含まれることがあります。PDFファイルのサイズを縮小することで、ネットワーク転送とストレージを最適化できます。これは、ウェブページでの公開、ソーシャルネットワークでの共有、電子メールでの送信、またはストレージでのアーカイブに特に便利です。PDFを最適化するために、いくつかの手法を使用できます。

- オンライン閲覧のためにページコンテンツを最適化
- すべての画像を縮小または圧縮
- ページコンテンツの再利用を可能にする
- 重複するストリームを統合
- フォントを埋め込まず
- 未使用のオブジェクトを削除
- フォームフィールドのフラット化を削除
- 注釈を削除またはフラット化

## Web用にPDFドキュメントを最適化

最適化または線形化とは、ウェブブラウザを使用してオンライン閲覧に適したPDFファイルを作成するプロセスを指します。
 Aspose.PDFはこのプロセスをサポートしています。

PDFをウェブ表示用に最適化するには：

1. 入力ドキュメントを[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトで開きます。
1. [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--)メソッドを使用します。
1. save(..)メソッドを使用して最適化されたドキュメントを保存します。

次のコードスニペットは、PDFドキュメントをウェブ用に最適化する方法を示しています。

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.time.Clock;
import java.time.Duration;

import com.aspose.pdf.*;
import com.aspose.pdf.optimization.ImageCompressionVersion;
import com.aspose.pdf.optimization.ImageEncoding;

public class ExampleOptimize {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void OptimizePDFDocumentForTheWeb() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // ウェブ用に最適化
        pdfDocument.optimize();

        // 出力ドキュメントを保存
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## PDFファイルサイズの削減

このトピックでは、PDFファイルサイズを最適化/削減する手順について説明します。Aspose.PDF APIは、不要なオブジェクトを削除し、画像を含むPDFファイルを圧縮することで出力PDFを最適化する柔軟性を提供する[OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions)クラスを提供します。これらのオプションの両方が以下のセクションで詳しく説明されています。

### 不要なオブジェクトの削除
重複および未使用のオブジェクトを削除することで、PDFドキュメントのサイズを最適化できます。次のコードスニペットはその方法を示しています。

```java
public static void ReduceSizePDF() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // PDFドキュメントを最適化。ただし、このメソッドは
        // ドキュメントの縮小を保証するものではありません
        pdfDocument.optimizeResources();

        // 出力ドキュメントを保存
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## すべての画像を縮小または圧縮する

If the source PDF file contains images, consider compressing the images and setting their quality. In order to enable image compression, pass true as an argument to the setCompressImages(..) method. All the images in a document will be re-compressed. The compression is defined by the setImageQuality(..) method, which is the value of the quality in percent. 100% is unchanged quality and image size. To decrease image size, pass an argument of less than 100 to the setImageQuality(..) method.

ソースPDFファイルに画像が含まれている場合、画像を圧縮してその品質を設定することを検討してください。画像圧縮を有効にするには、setCompressImages(..) メソッドに true を引数として渡します。ドキュメント内のすべての画像が再圧縮されます。圧縮は、品質の値をパーセントで表す setImageQuality(..) メソッドによって定義されます。100%は品質と画像サイズが変更されないことを意味します。画像サイズを小さくするには、setImageQuality(..) メソッドに100未満の引数を渡します。

```java
public static void ShrinkingCompressing() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "Shrinkimage.pdf");

        // OptimizationOptionsを初期化する
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // CompressImagesオプションを設定する
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // ImageQualityオプションを設定する
        optimizationOptions.getImageCompressionOptions().setImageQuality(50);

        // OptimizationOptionsを使用してPDFドキュメントを最適化する
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "Shrinkimage_out.pdf";
        // 更新されたドキュメントを保存する
        pdfDocument.save(_dataDir);
    }
```

別の方法として、低解像度で画像をリサイズする方法があります。この場合、ResizeImagesをtrueに設定し、MaxResolutionを適切な値に設定する必要があります。

```java
public static void ShrinkingCompressing2() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // OptimizationOptionsを初期化
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // CompressImagesオプションを設定
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);
        // ImageQualityオプションを設定
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // ResizeImageオプションを設定
        optimizationOptions.getImageCompressionOptions().setResizeImages(true);

        // MaxResolutionオプションを設定
        optimizationOptions.getImageCompressionOptions().setMaxResolution(300);

        // OptimizationOptionsを使用してPDFドキュメントを最適化
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "ResizeImages_out.pdf";
        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir);
    }
```

Another important issue is the execution time. But again, we can manage this setting too. Currently, we can use two algorithms - Standard and Fast. To control the execution time we should set a Version property. The following snippet demonstrates the Fast algorithm:

もう一つの重要な問題は実行時間です。しかし、これも設定を管理することができます。現在、私たちは2つのアルゴリズム、標準と高速を使用できます。実行時間を制御するには、バージョンプロパティを設定する必要があります。次のスニペットは、高速アルゴリズムを示しています：

```java
public static void ShrinkingCompressing3() {

        Clock clock = Clock.systemUTC();

        Duration tickDuration = Duration.ofNanos(250000);
        Clock clock1 = Clock.tick(clock, tickDuration);
        System.out.println("Start : " + clock.instant());

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // OptimizationOptionsを初期化
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // CompressImagesオプションを設定
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // ImageQualityオプションを設定
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // 画像圧縮バージョンを高速に設定
        optimizationOptions.getImageCompressionOptions().setVersion(ImageCompressionVersion.Fast);

        // OptimizationOptionsを使用してPDFドキュメントを最適化
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "ResizeImages_out.pdf";

        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir);
        System.out.println("Finish : " + clock1.instant());
    }
```

## 未使用オブジェクトの削除

PDFドキュメントには、ドキュメント内の他のオブジェクトから参照されていないPDFオブジェクトが含まれていることがあります。例えば、ページがドキュメントのページツリーから削除されても、ページオブジェクト自体は削除されない場合があります。これらのオブジェクトを削除してもドキュメントが無効になることはなく、むしろドキュメントを縮小します。

```java
    public static void RemovingUnusedObjects() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        
        optimizationOptions.setRemoveUnusedObjects(true);
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "emoveUnusedObjects_out.pdf";

        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir);

    }
```
## 未使用ストリームの削除

ドキュメントには未使用のリソースストリームが含まれていることがあります。
 これらのストリームは、ページのリソースディクショナリから参照されているため、「未使用のオブジェクト」ではありません。これは、画像がページから削除されたがページリソースからは削除されていない場合に発生することがあります。また、ページがドキュメントから抽出され、ドキュメントページが「共通の」リソース、つまり同じResourcesオブジェクトを持っている場合に、この状況がよく発生します。リソースストリームが使用されているかどうかを判断するために、ページの内容が分析されます。未使用のストリームは削除されます。これにより、ドキュメントのサイズが縮小されることがあります。

```java
public static void RemovingUnusedStream() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + 
        "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "removeUnusedObjects_out.pdf";
        
        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir);
        
    }
```
## 重複ストリームのリンク

時々、ドキュメントにはいくつかの同一のリソースストリーム（例えば画像）が含まれることがあります。これは、例えばドキュメントが自分自身と連結されたときに発生することがあります。出力ドキュメントには同じリソースストリームの2つの独立したコピーが含まれています。すべてのリソースストリームを分析し、比較します。ストリームが重複している場合、それらはマージされます。つまり、1つのコピーだけが残り、参照が適切に変更され、オブジェクトのコピーが削除されます。これにより、文書サイズが小さくなることがあります。

```java
    public static void LinkingDuplicateStream() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        
        // OptimizationOptions を使用して PDF ドキュメントを最適化
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir);
    }
```

加えて、AllowReusePageContent設定を使用することができます。このプロパティがtrueに設定されている場合、同一ページの最適化の際にページコンテンツが再利用されます。

```java
public static void AllowReusePageContent() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setAllowReusePageContent(true);
        
        // OptimizationOptionsを使用してPDFドキュメントを最適化
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir);
    }
```
## フォントの埋め込み解除

ドキュメントが埋め込みフォントを使用している場合、すべてのフォントデータがドキュメントに配置されていることを意味します。
 ドキュメントがユーザーのマシンにフォントがインストールされているかどうかに関係なく表示可能であるという利点があります。しかし、フォントを埋め込むと、ドキュメントが大きくなります。フォントの埋め込み解除メソッドは、すべての埋め込みフォントを削除します。これによりドキュメントサイズが小さくなりますが、正しいフォントがインストールされていない場合、ドキュメントが読めなくなる可能性があります。

```java
    public static void UnembedFonts() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setUnembedFonts(true);
        
        // OptimizationOptionsを使用してPDFドキュメントを最適化
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir);
    }
```

## 注釈の削除またはフラット化

注釈が不要な場合は削除できます。 必要な場合は追加編集をせずにフラット化できます。これらの技術の両方がファイルサイズを削減します。

```java
    public static void FlatteningAnnotations() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        for (Page page : pdfDocument.getPages()) {
            for (Annotation annotation : page.getAnnotations())
                annotation.flatten();
        }

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir);
    }

```
## フォームフィールドの削除

PDFドキュメントにAcroFormsが含まれている場合、フォームフィールドをフラット化することでファイルサイズを減らすことができます。

```java
    public static void RemovingFormFields() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        // フォームをフラット化
        if (pdfDocument.getForm().getFields().length > 0) {
            for (Field field : pdfDocument.getForm().getFields()) {
                field.flatten();
            }
        }
        _dataDir = _dataDir + "FlattenForms_out.pdf";
        // 更新されたドキュメントを保存
        pdfDocument.save(_dataDir);
    }

```
## PDFをRGBカラースペースからグレースケールに変換する

PDFファイルは、テキスト、画像、添付ファイル、注釈、グラフ、その他のオブジェクトで構成されています。PDFをRGBカラースペースからグレースケールに変換する必要がある場合があります。これにより、そのPDFファイルを印刷するときの速度が向上します。また、ファイルがグレースケールに変換されると、ドキュメントのサイズも縮小されますが、この変更によりドキュメントの品質が低下する可能性があります。現在、この機能はAdobe Acrobatのプリフライト機能でサポートされていますが、オフィス自動化に関しては、Aspose.PDFはドキュメント操作のための究極のソリューションを提供します。

この要件を達成するには、次のコードスニペットを使用できます。

```java
    public static void ConvertRGBtoGrayscale() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        com.aspose.pdf.RgbToDeviceGrayConversionStrategy strategy = new com.aspose.pdf.RgbToDeviceGrayConversionStrategy();
        for (int idxPage = 1; idxPage <= pdfDocument.getPages().size(); idxPage++) {
            Page page = pdfDocument.getPages().get_Item(idxPage);
            strategy.convert(page);
        }
        pdfDocument.save("output.pdf");
    }
```

## FlateDecode 圧縮

Aspose.PDF for Java は、PDF 最適化機能のために FlateDecode 圧縮のサポートを提供します。以下のコードスニペットは、FlateDecode 圧縮で画像を保存するために最適化オプションを使用する方法を示しています:

```java
    public static void FlateDecodeCompression() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);

        // OptimizationOptions を使用して PDF ドキュメントを最適化する
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // 更新されたドキュメントを保存する
        pdfDocument.save(_dataDir);
    }
```
## XImageCollection に画像を保存

Aspose.PDF for Java は、FlateDecode 圧縮を使用して新しい画像を [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) に保存する機能を提供します。
 このオプションを有効にするには、ImageFilterType.Flate フラグを使用できます。以下のコードスニペットは、この機能を使用する方法を示しています:

```java
    public static void StoreImageInXImageCollection() {
        // ドキュメントを初期化
        Document document = new Document();
        document.getPages().add();
        Page page = document.getPages().get_Item(1);

        // ストリームに画像をロード
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        page.getResources().getImages().add(imageStream, ImageFilterType.Flate);
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        page.getContents().add(new com.aspose.pdf.operators.GSave());

        // 座標を設定
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });
        // ConcatenateMatrix（行列を連結）演算子を使用：画像の配置方法を定義
        page.getContents().add(new com.aspose.pdf.operators.ConcatenateMatrix(matrix));
        page.getContents().add(new com.aspose.pdf.operators.Do(ximage.getName()));
        page.getContents().add(new com.aspose.pdf.operators.GRestore());

        document.save(_dataDir + "FlateDecodeCompression.pdf");
    }

}
```
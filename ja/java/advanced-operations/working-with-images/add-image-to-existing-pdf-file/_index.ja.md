---
title: 既存のPDFファイルに画像を追加する
linktitle: 画像を追加
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: このセクションでは、Javaライブラリを使用して既存のPDFファイルに画像を追加する方法を説明します。
lastmod: "2021-06-05"
---

すべてのPDFページには、リソースとコンテンツのプロパティがあります。リソースには、画像やフォームなどが含まれる場合があり、コンテンツは一連のPDFオペレーターによって表されます。各オペレーターには名前と引数があります。この例では、オペレーターを使用してPDFファイルに画像を追加します。

既存のPDFファイルに画像を追加するには:

- [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトを作成し、入力PDFドキュメントを開きます。
- 画像を追加したいページを取得します。
- ページの [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) コレクションに画像を追加します。
- オペレーターを使用してページ上に画像を配置します:
- GSaveオペレーターを使用して、現在のグラフィカル状態を保存します。

- [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/concatenatematrix) オペレーターを使用して、画像の配置場所を指定します。
- ページに画像を描画するために [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/class-use/Do) オペレーターを使用します。
- 最後に、更新されたグラフィカル状態を保存するために [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/grestore) オペレーターを使用します。
- ファイルを保存します。

次のコードスニペットは、PDFドキュメントに画像を追加する方法を示しています。

```java
package com.aspose.pdf.examples;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfFileMend;
import com.aspose.pdf.operators.*;

public class ExampleAddImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddImageToExistingPDF() throws IOException {
        // ドキュメントを開く
        Document pdfDocument1 = new Document(_dataDir + "sample.pdf");

        // 座標を設定
        int lowerLeftX = 50;
        int lowerLeftY = 750;
        int upperRightX = 100;
        int upperRightY = 800;

        // 画像を追加したいページを取得
        Page page = pdfDocument1.getPages().get_Item(1);

        // ストリームに画像を読み込む
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(_dataDir + "logo.png"));

        // ページリソースのImagesコレクションに画像を追加
        page.getResources().getImages().add(imageStream);

        // GSaveオペレーターを使用: このオペレーターは現在のグラフィックス状態を保存
        page.getContents().add(new GSave());

        // RectangleとMatrixオブジェクトを作成
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // ConcatenateMatrix (行列を連結) オペレーターを使用: 画像の配置方法を定義
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

        // Doオペレーターを使用: このオペレーターは画像を描画
        page.getContents().add(new Do(ximage.getName()));

        // GRestoreオペレーターを使用: このオペレーターはグラフィックス状態を復元
        page.getContents().add(new GRestore());

        // 新しいPDFを保存
        pdfDocument1.save(_dataDir + "updated_document.pdf");

        // 画像ストリームを閉じる
        imageStream.close();
    }
```


## BufferedImageからPDFへの画像追加

Aspose.PDF for Java 9.5.0のリリースから、BufferedImageインスタンスからPDFドキュメントに画像を追加するサポートが導入されました。この要件をサポートするために、次のメソッドが実装されています：[XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection).add(BufferedImage image);

```java
    public static void AddingImageFromBufferedImageIntoPDF() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();
        page.getResources().getImages().add(originalImage);
    }
```
画像を追加するために、FileInputStreamオブジェクトだけでなく、任意のInputStreamを使用できます。したがって、java.io.ByteArrayInputStreamオブジェクトを使用する場合、システム上にファイルを保存する必要はありません:

```java
    public static void AddingImageFromBufferedImageIntoPDF2() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        Document pdfDocument = new Document();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        Page page = pdfDocument.getPages().get_Item(1);
        page.getResources().getImages().add(new ByteArrayInputStream(baos.toByteArray()));
    }
```


## 既存のPDFファイルに画像を追加する（ファサード）

PDFファイルに画像を追加する別の簡単な方法もあります。[PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend)クラスのAddImageメソッドを使用できます。AddImageメソッドには、追加する画像、画像を追加するページ番号、および座標情報が必要です。その後、Closeメソッドを使用して更新されたPDFファイルを保存します。

次のコードスニペットは、既存のPDFファイルに画像を追加する方法を示しています。

```java
    public static void AddImageInAnExistingPDFFile_Facades() {
        // ドキュメントを開く
        PdfFileMend mender = new PdfFileMend();

        // テキストを追加するためのPdfFileMendオブジェクトを作成
        mender.bindPdf(_dataDir + "AddImage.pdf");

        // PDFファイルに画像を追加
        mender.addImage(_dataDir + "aspose-logo.jpg", 1, 100, 600, 200, 700);

        // 変更を保存
        mender.save(_dataDir + "AddImage_out.pdf");

        // PdfFileMendオブジェクトを閉じる
        mender.close();
    }
```


## PDFドキュメントに同じ画像を複数回参照として追加

時々、PDFドキュメント内で同じ画像を複数回使用する必要があります。新しいインスタンスを追加すると、生成されるPDFドキュメントが増加します。私たちは、XImageオブジェクトをImages Collectionに追加することをサポートする新しいメソッドXImageCollection.add(XImage)を追加しました。このメソッドは、PDFドキュメントのサイズを最適化するために、元の画像と同じPDFオブジェクトへの参照を追加することを可能にします。

```java
    public static void AddReferenceOfaSingleImageMultipleTimes() throws FileNotFoundException {
        Rectangle imageRectangle = new Rectangle(0, 0, 30, 15);
        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        document.getPages().add();
        java.io.FileInputStream imageStream = new java.io.FileInputStream(
                new java.io.File(_dataDir + "aspose-logo.png"));

        XImage image = null;

        for (Page page : document.getPages()) {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.getRect());
            XForm form = annotation.getAppearance().get_Item("N");
            form.setBBox(page.getRect());
            String name;
            if (image == null) {
                name = form.getResources().getImages().add(imageStream);
                image = form.getResources().getImages().get_Item(name);
            } else {
                name = form.getResources().getImages().add(image);
            }
            form.getContents().add(new GSave());
            form.getContents().add(new ConcatenateMatrix(
                    new Matrix(imageRectangle.getWidth(), 0, 0, imageRectangle.getHeight(), 0, 0)));
            form.getContents().add(new Do(name));
            form.getContents().add(new GRestore());
            page.getAnnotations().add(annotation, false);
            imageRectangle = new Rectangle(0, 0, imageRectangle.getWidth() * 1.01, imageRectangle.getHeight() * 1.01);
        }
        document.save(_dataDir + "output.pdf");
    }
```


## PDF内の画像がカラーか白黒かを識別する

画像のサイズを縮小するために、異なる種類の圧縮が適用されることがあります。画像に適用される圧縮の種類は、元の画像のColorSpaceに依存します。つまり、画像がカラー（RGB）の場合はJPEG2000圧縮を適用し、白黒の場合はJBIG2/JBIG2000圧縮を適用します。したがって、各画像タイプを識別し、適切な圧縮タイプを使用することで、最適化された出力を作成することができます。

PDFファイルには、テキスト、画像、グラフ、添付ファイル、注釈などの要素が含まれている場合があります。元のPDFファイルに画像が含まれている場合、画像のカラー空間を判別し、適切な圧縮を適用することで、PDFファイルのサイズを縮小することができます。以下のコードスニペットは、PDF内の画像がカラーか白黒かを識別する手順を示しています。

```java
    public static void CheckColors() {

        Document document = new Document(_dataDir + "test4.pdf");
        try {
            // PDFファイルのすべてのページを繰り返し処理します
            for (Page page : (Iterable<Page>) document.getPages()) {
                // イメージ配置アブソーバーのインスタンスを作成します
                ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
                page.accept(abs);
                for (ImagePlacement ia : (Iterable<ImagePlacement>) abs.getImagePlacements()) {
                    /* ColorType */
                    int colorType = ia.getImage().getColorType();
                    switch (colorType) {
                    case ColorType.Grayscale:
                        System.out.println("グレースケール画像");
                        break;
                    case ColorType.Rgb:
                        System.out.println("カラー画像");
                        break;
                    }
                }
            }
        } catch (Exception ex) {
            System.out.println("ファイルの読み取りエラー = " + document.getFileName());
        }
    }
}
```
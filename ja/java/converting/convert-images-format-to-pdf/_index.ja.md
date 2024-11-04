---
title: さまざまな画像形式をPDFに変換
linktitle: 画像をPDFに変換
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDF for Javaライブラリがさまざまな画像形式をPDFに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java** は、異なる形式の画像をPDFファイルに変換することを可能にします。当ライブラリは、BMP、CGM、DICOM、EMF、JPG、PNG、SVG、TIFFなどの最も人気のある画像形式を変換するためのコードスニペットを示しています。

## BMPをPDFに変換

**Aspose.PDF for Java** ライブラリを使用してBMPファイルをPDFドキュメントに変換します。

<abbr title="Bitmap Image File">BMP</abbr> 画像は拡張子.BMPを持つファイルで、ビットマップデジタル画像を保存するために使用されるビットマップ画像ファイルを表します。これらの画像はグラフィックアダプタに依存せず、デバイス独立ビットマップ (DIB) ファイル形式とも呼ばれます。 Aspose.PDF for Java APIを使用して、BMPをPDFに変換できます。
 以下の手順に従ってBMP画像を変換することができます：

1. 新しいドキュメントを初期化する
1. サンプルのBMP画像ファイルを読み込む
1. 最後に、出力PDFファイルを保存する

次のコードスニペットはこれらの手順に従い、Javaを使用してBMPをPDFに変換する方法を示しています：

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertBMPtoPDF {

    private ConvertBMPtoPDF() {
    }

    private static Path _dataDir = Paths.get("<set path to samples>");

    public static void main(String[] args) throws FileNotFoundException {
        // ドキュメントオブジェクトを初期化する
        Document document = new Document();

        Page page = document.getPages().add();        
        Image image = new Image();
        
        // サンプルのBMP画像ファイルを読み込む
        image.setFile(Paths.get(_dataDir.toString(), "Sample.bmp").toString());
        page.getParagraphs().add(image);
        
        // 出力PDFドキュメントを保存する
        document.save(Paths.get(_dataDir.toString(),"BMPtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**BMPをPDFにオンラインで変換してみてください**

Asposeはオンラインで無料アプリケーション["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)を提供しており、機能性と品質を調査することができます。

[![Aspose.PDF Convertion BMP to PDF using Free App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## CGMをPDFに変換

<abbr title="Computer Graphics Metafile">CGM</abbr>は、グラフィックス情報の保存と取得のためのベクターに基づいた2D画像ファイル形式を提供するISO標準です。CGMはデバイスに依存しないフォーマットです。CGMはベクターグラフィックスフォーマットで、3つの異なるエンコーディング方法をサポートしています：バイナリ（プログラムの読み取り速度に最適）、文字ベース（最小のファイルサイズを生成し、データ転送を高速化）またはクリアテキストエンコーディング（ユーザーがテキストエディタでファイルを読み取り、変更可能にすることができます）

以下のコードスニペットは、Aspose.PDF for Javaを使用してCGMファイルをPDF形式に変換する方法を示しています。

1. [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) クラスを作成します。
1. ソースファイル名とオプションを指定して [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) クラスのインスタンスを作成します。
1. 希望のファイル名でドキュメントを保存します。

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertCGMtoPDF {

    private ConvertCGMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // CGM LoadOptionsを作成します
        CgmLoadOptions options = new CgmLoadOptions();

        // ドキュメントオブジェクトを初期化します
        String cgmFileName = Paths.get(_dataDir.toString(), "corvette.cgm").toString();
        Document document = new Document(cgmFileName, options);

        // 出力PDFドキュメントを保存します
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


## DICOMをPDFに変換する

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr>は、医用画像の取り扱い、保存、印刷、および情報伝達に関する標準です。これには、ファイル形式の定義とネットワーク通信プロトコルが含まれます。

Aspose.PDF for Javaを使用すると、DICOMファイルをPDF形式に変換できます。次のコードスニペットを確認してください：

1. ストリームに画像を読み込む
1. [Documentオブジェクト](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)を初期化する
1. サンプルDICOM画像ファイルを読み込む
1. 出力PDFドキュメントを保存する

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertDICOMtoPDF {

    private ConvertDICOMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // ストリームに画像を読み込む
        FileInputStream imageStream = new FileInputStream(
            new java.io.File(Paths.get(_dataDir.toString(),"0002.dcm").toString()));

        // Documentオブジェクトを初期化する
        Document document = new Document();
        document.getPages().add();
        
        // サンプルDICOM画像ファイルを読み込む
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setImageStream(imageStream);

        document.getPages().get_Item(1).getParagraphs().add(image);

        // 出力PDFドキュメントを保存する
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**DICOMをPDFにオンラインで変換してみる**

Asposeは、オンラインで無料のアプリケーション「[DICOM to PDF](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)」を提供しています。ここで、機能と品質を調査することができます。

[![Aspose.PDF コンバージョン DICOMからPDFへのフリーアプリを使用](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMFをPDFに変換

拡張メタファイル形式 (<abbr title="Enhanced metafile format">EMF</abbr>) は、グラフィカルイメージをデバイスに依存せずに保存します。EMFのメタファイルは、変動長のレコードが時系列順に含まれており、任意の出力デバイスで解析後に保存された画像をレンダリングすることができます。

EMFをPDFに変換するためのいくつかのアプローチがあります。

## Imageクラスを使用

PDFドキュメントはページで構成され、各ページには1つ以上の段落オブジェクトが含まれます。段落には、テキスト、画像、表、フローティングボックス、グラフ、見出し、フォームフィールド、または添付ファイルが含まれます。

画像ファイルをPDF形式に変換するには、それを段落内に囲みます。

画像をローカルハードドライブの物理的な場所、Web URL、またはStreamインスタンスで変換することが可能です。

画像を追加するには:

1. `com.aspose.pdf.Image`クラスのオブジェクトを作成します。
1. ページインスタンスの[Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs)コレクションに画像を追加します。
1. 画像のパスまたはソースを指定します。
    - 画像がハードドライブ上の場所にある場合、[Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image)メソッドを使用してパスの場所を指定します。
    - 画像がFileInputStreamに置かれている場合、[Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image)メソッドに画像を保持しているオブジェクトを渡します。

次のコードスニペットは、画像オブジェクトを読み込み、ページの余白を設定し、ページに画像を配置して出力をPDFとして保存する方法を示しています。

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;

/**
 * Convert EMF to PDF
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;

public final class ConvertEMFtoPDF {

    private ConvertEMFtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        convertEMFtoPDF_01();
        convertEMFtoPDF_02();
    }

    

    public static void convertEMFtoPDF_01() throws FileNotFoundException {                
        // Documentオブジェクトをインスタンス化
        Document doc = new Document();
        // ドキュメントのページコレクションにページを追加
        Page page = doc.getPages().add();
        // ソース画像ファイルをStreamオブジェクトに読み込む
        java.io.FileInputStream fs = new java.io.FileInputStream(
            Paths.get(_dataDir.toString(),"source.emf").toString());

        // 画像が収まるように余白を設定、など
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);

        page.setCropBox(new Rectangle(0, 0, 400, 400));
        // 画像オブジェクトを作成
        Image image1 = new Image();
        // セクションの段落コレクションに画像を追加
        page.getParagraphs().add(image1);
        // 画像ファイルストリームを設定
        image1.setImageStream(fs);
        // 結果のPDFファイルを保存
        doc.save("EMFtoPDF_01.pdf");
    }   
    public static void convertEMFtoPDF_02() throws IOException {
        // 以下のコードを参照
    } 
}
```


### BufferedImageから画像を追加

Aspose.PDF for Javaは、Streamインスタンスから画像をロードする機能も提供しています。ここでは、画像をBufferedImageオブジェクトにロードし、Pdfファイルの段落コレクション内に配置することができます。

```java
public static void convertEMFtoPDF_02() throws IOException {    
    Document doc = new Document();
    // Pdfファイルのページコレクションにページを追加
    Page page = doc.getPages().add();
    // 画像インスタンスを作成
    Image image1 = new Image();
    // BufferedImageインスタンスを作成
    java.awt.image.BufferedImage bufferedImage = ImageIO.read(new File("source.emf"));
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    // Buffered ImageをOutputStreamインスタンスに書き込む
    ImageIO.write(bufferedImage, "emf", baos);
    baos.flush();
    ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
    // 最初のページの段落コレクションに画像を追加
    page.getParagraphs().add(image1);
    // Buffered画像を保持するOutputStreamとして画像ストリームを設定
    image1.setImageStream(bais);
    // 結果のPDFファイルを保存
    doc.save("BufferedImage.pdf");
}
```


## PDF演算子を使用して画像を追加する

すべてのPDFページオブジェクトには、[getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--)メソッドと[getContents()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getContents--)メソッドが含まれています。リソースには画像やフォームが含まれる場合があり、コンテンツはPDF演算子のセットで表されます。各演算子には独自の名前と引数があります。

この例では、演算子を使用してPDFファイルに画像を追加します。

既存のPDFファイルに画像を追加するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトを作成し、入力PDFドキュメントを開きます。
1. 画像を追加したいページを取得します。
1. ページの[getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--)コレクションに画像を追加します。
1. 演算子を使用してページに画像を配置します：
   1. GSave演算子を使用して現在のグラフィカル状態を保存します。
   1. ConcatenateMatrix演算子を使用して画像を配置する場所を指定します。

1. Do演算子を使用して、画像をページに描画します。
   1. 最後に、GRestore演算子を使用して更新されたグラフィカル状態を保存します。
1. ファイルを保存します。

以下のコードスニペットは、PDFドキュメントに画像を追加する方法を示しています。

```java
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-Java をご覧ください。
// ドキュメントを開く
Document pdfDocument1 = new Document("input.pdf");

// 座標を設定
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// 画像を追加したいページを取得
Page page = pdfDocument1.getPages().get_Item(1);

// ストリームに画像をロード
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));

// ページリソースのImagesコレクションに画像を追加
page.getResources().getImages().add(imageStream);

// GSave演算子を使用: この演算子は現在のグラフィックス状態を保存します
page.getContents().add(new Operator.GSave());

// RectangleとMatrixオブジェクトを作成
Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

// ConcatenateMatrix (マトリックスの連結) 演算子を使用: 画像の配置方法を定義します
page.getContents().add(new Operator.ConcatenateMatrix(matrix));
XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

// Do演算子を使用: この演算子は画像を描画します
page.getContents().add(new Operator.Do(ximage.getName()));

// GRestore演算子を使用: この演算子はグラフィックス状態を復元します
page.getContents().add(new Operator.GRestore());

// 新しいPDFを保存
pdfDocument1.save("Updated_document.pdf");

// 画像ストリームを閉じる
imageStream.close();
```


{{% alert color="success" %}}
**EMFをPDFにオンラインで変換してみてください**

Asposeは、オンラインで無料のアプリケーション["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion EMF to PDF using Free App](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## JPGをPDFに変換する

JPGをPDFに変換する方法について考える必要はありません。なぜなら、Apose.PDF for Javaライブラリが最良の解決策を提供するからです。

Aspose.PDF for Javaを使用して、以下の手順でJPG画像を簡単にPDFに変換できます：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスのオブジェクトを初期化
1. JPG画像を読み込み、段落に追加
1. 出力PDFを保存

以下のコードスニペットは、Javaを使用してJPG画像をPDFに変換する方法を示しています：

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertJPEGtoPDF {

    private static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // ドキュメントオブジェクトを初期化
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // サンプルJPEG画像ファイルを読み込む
        image.setFile(Paths.get(_dataDir.toString(), "Sample.jpg").toString());
        page.getParagraphs().add(image);

        // 出力PDFドキュメントを保存
        document.save(Paths.get(_dataDir.toString(),"JPEGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**JPGをPDFにオンラインで変換してみてください**

Asposeはオンラインで無料のアプリケーション["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion JPG to PDF using Free App](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## PNGをPDFに変換

**Aspose.PDF for Java**はPNG画像をPDF形式に変換する機能をサポートしています。次のコードスニペットを参照してタスクを実現してください。

<abbr title="Portable Network Graphics">PNG</abbr>はロスレス圧縮を使用するラスター画像ファイル形式の一種であり、ユーザーの間で人気があります。

以下の手順でPNGをPDFに変換できます：

1. 入力PNG画像をロードする
1. 高さと幅の値を読み取る
1. 新しいドキュメントを作成しページを追加する
1. ページの寸法を設定する
1. 出力ファイルを保存する

さらに、以下のコードスニペットはJavaアプリケーションでPNGをPDFに変換する方法を示しています：

```java
package com.aspose.pdf.examples;

/**
 * PNGをPDFに変換
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPNGtoPDF {

    private ConvertPNGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // ドキュメントオブジェクトを初期化
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // サンプルBMP画像ファイルをロード
        image.setFile(Paths.get(_dataDir.toString(), "Sample.png").toString());

        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getParagraphs().add(image);

        // 出力PDFドキュメントを保存
        document.save(Paths.get(_dataDir.toString(), "PNGtoPDF.pdf").toString());
    }
}

```


{{% alert color="success" %}}
**PNGをPDFにオンラインで変換してみてください**

Asposeは、オンライン無料アプリケーション["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)を提供しており、そこで機能と品質を調査することができます。

[![Aspose.PDF Convertion PNG to PDF using Free App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## SVGをPDFに変換

スケーラブルベクターグラフィックス（SVG）は、二次元ベクターグラフィックスのためのXMLベースのファイル形式の仕様のファミリーであり、静的および動的（インタラクティブまたはアニメーション）です。SVG仕様は、ワールドワイドウェブコンソーシアム（W3C）によって1999年から開発されているオープンスタンダードです。

SVG画像とその動作はXMLテキストファイルで定義されています。
 これは、検索、インデックス化、スクリプト化、および必要に応じて圧縮できることを意味します。XMLファイルとして、SVG画像は任意のテキストエディターで作成および編集できますが、Inkscapeなどの描画プログラムで作成する方が便利な場合が多いです。

## SVGファイルをPDF形式に変換する方法

SVGファイルをPDFに変換するには、[LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) オブジェクトを初期化するために使用される [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) というクラスを使用します。後で、このオブジェクトは [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) オブジェクトの初期化中に引数として渡され、PDFレンダリングエンジンがソースドキュメントの入力形式を決定するのに役立ちます。

次のコードスニペットは、SVGファイルをPDF形式に変換するプロセスを示しています。

```java
// ドキュメントオブジェクトを初期化

String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();

SvgLoadOptions option = new SvgLoadOptions();
Document pdfDocument = new Document(svgDocumentFileName, option);
pdfDocument.save(pdfDocumentFileName);
```

{{% alert color="success" %}}
**SVGフォーマットをPDFにオンラインで変換してみてください**

Aspose.PDF for Javaは、オンラインで無料で使えるアプリケーション["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)を提供しており、その機能や品質を試すことができます。

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## TIFFをPDFに変換

**Aspose.PDF for Java**は、単一フレームまたはマルチフレームの<abbr title="Tag Image File Format">TIFF</abbr>画像をサポートしています。つまり、JavaアプリケーションでTIFF画像をPDFに変換することができます。

TIFFまたはTIF、Tagged Image File Formatは、このファイル形式標準を遵守するさまざまなデバイスで使用するために設計されたラスター画像を表します。
 TIFF 画像は、異なる画像を持つ複数のフレームを含むことができます。Aspose.PDF ファイル形式もサポートされており、単一フレームでもマルチフレームの TIFF 画像でも対応できます。したがって、Java アプリケーションで TIFF 画像を PDF に変換することができます。以下の手順で、マルチページの TIFF 画像をマルチページの PDF ドキュメントに変換する例を考えてみます。

1. Document クラスのインスタンスを生成する
1. 入力 TIFF 画像を読み込む
1. 最後に、画像を PDF ページとして保存する

さらに、以下のコードスニペットは、マルチページまたはマルチフレームの TIFF 画像を PDF に変換する方法を示しています:

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Image;
import com.aspose.pdf.Page;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * TIFF を PDF に変換します。
 */
public final class ConvertTIFFtoPDF {

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertTIFFtoPDF() {
    }

    public static void run() throws IOException {
        // ドキュメントオブジェクトを初期化
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        image.setFile(Paths.get(DATA_DIR.toString(), "Sample.tiff").toString());
        page.getParagraphs().add(image);

        // 出力 PDF ドキュメントを保存
        document.save(Paths.get(DATA_DIR.toString(), "TIFFtoPDF.pdf").toString());
        document.close();
    }    
}
```
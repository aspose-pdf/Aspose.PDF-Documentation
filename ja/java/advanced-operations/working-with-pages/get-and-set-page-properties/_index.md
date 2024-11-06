---
title: Get and Set Page Properties
type: docs
weight: 30
url: ja/java/get-and-set-page-properties/
description: このトピックでは、Aspose.PDF for Javaを使用してPDFファイルの数値を取得し、ページプロパティを取得し、ページの色を判定する方法を説明します。
lastmod: "2021-06-05"
---

Aspose.PDF for Javaを使用すると、Javaアプリケーション内でPDFファイルのページのプロパティを読み取りおよび設定できます。このセクションでは、PDFファイルのページ数を取得し、色などのPDFページプロパティに関する情報を取得し、ページプロパティを設定する方法を示します。

## PDFファイルのページ数を取得

ドキュメントを扱う際には、しばしばそのページ数を知りたいと思うものです。Aspose.PDFを使用すると、これはたった2行のコードで行えます。

PDFファイルのページ数を取得するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用してPDFファイルを開きます。

1. 次に、[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) コレクションの Count プロパティ（Document オブジェクトから）を使用して、ドキュメント内のページの総数を取得します。

次のコードスニペットは、PDFファイルのページ数を取得する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleGetAndSetPageProperties {
    // ドキュメントディレクトリへのパス。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GetNumberOfPagesInaPDFFile() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "GetNumberofPages.pdf");

        // ページ数を取得
        System.out.println("ページ数 : " + pdfDocument.getPages().size());
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDocument.save(_dataDir);

    }
```

### ドキュメントを保存せずにページ数を取得

PDFファイルが保存され、すべての要素が実際にPDFファイル内に配置されない限り、特定のドキュメントのページ数を取得することはできません（すべての要素が収容されるページ数を確実に把握できないため）。
 Aspose.PDF for Java 10.1.0のリリースから、ファイルを保存せずにPDFドキュメントのページ数を取得する機能を提供する[processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--)というメソッドを導入しました。そのため、ページ数情報を即座に取得できます。この要件を達成するために、以下のコードスニペットを試してください。

```java
public static void GetPageCountWithoutSavingTheDocument() {

        // 完全な例とデータファイルについては、以下をご覧ください
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        // Documentインスタンスをインスタンス化
        Document doc = new Document();
        // PDFファイルのページコレクションにページを追加
        Page page = doc.getPages().add();
        // 300個のTextFragmentインスタンスを追加するループを作成
        for (int i = 0; i < 300; i++)
            // TextFragmentをPDFの最初のページの段落コレクションに追加
            page.getParagraphs().add(new TextFragment("Pages count test"));
        // 段落を処理してページ数情報を取得
        doc.processParagraphs();
        System.out.println("PDFのページ数 = " + doc.getPages().size());
    }
```

## ページプロパティを取得する

PDFファイルの各ページには、幅、高さ、塗り足し、裁ち落とし、仕上がりサイズなど、いくつかのプロパティがあります。Aspose.PDFを使用すると、これらのプロパティにアクセスできます。

### **ページプロパティの理解: Artbox、BleedBox、CropBox、MediaBox、TrimBox、そしてRectプロパティの違い**

- **メディアボックス**: メディアボックスは最大のページボックスです。これは、PostScriptまたはPDFに印刷されたときに選択されたページサイズ（例えば、A4、A5、USレターなど）に対応します。言い換えれば、メディアボックスはPDFドキュメントが表示または印刷されるメディアの物理的なサイズを決定します。
- **ブリードボックス**: ドキュメントに塗り足しがある場合、PDFにもブリードボックスがあります。
 Bleedは、ページの端を超えて広がる色（またはアートワーク）の量です。これは、ドキュメントが印刷されてサイズにカット（「トリミング」）されたときに、インクがページの端まで行き届くようにするために使用されます。ページが誤ってトリミングされた場合でも（トリムマークから少しずれてカットされた場合でも）、ページに白い端は現れません。
- **Trim box**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **Art box**: アートボックスは、ドキュメント内のページの実際の内容の周りに描かれたボックスです。このページボックスは、他のアプリケーションでPDFドキュメントをインポートする際に使用されます。
- **Crop box**: クロップボックスは、Adobe AcrobatでPDFドキュメントが表示される「ページ」サイズです。通常のビューでは、Adobe Acrobatに表示されるのはクロップボックスの内容のみです。
  これらのプロパティの詳細な説明については、Adobe.Pdf仕様書の特に10.10.1ページ境界をお読みください。
- **Page.Rect**: MediaBoxとDropBoxの交差（一般に見える矩形）。 以下の図はこれらのプロパティを示しています。

詳細については、[このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)を訪問してください。

### ページプロパティへのアクセス

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスは特定のPDFページに関連するすべてのプロパティを提供します。PDFファイルのすべてのページは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) コレクションに含まれています。

そこから、インデックスを使用して個別のPageオブジェクトにアクセスするか、foreachループを使用してコレクションをループし、すべてのページを取得することが可能です。一度個別のページにアクセスすると、そのプロパティを取得できます。以下のコードスニペットは、ページプロパティを取得する方法を示しています。

```java
    public static void AccessingPageProperties() {

        Document pdfDocument = new Document("input.pdf");

        // ページコレクションを取得
        PageCollection pageCollection = pdfDocument.getPages();

        // 特定のページを取得
        Page pdfPage = pageCollection.get_Item(1);

        // ページプロパティを取得
        System.out.printf("\n ArtBox : Height = " + pdfPage.getArtBox().getHeight() + ", Width = "
                + pdfPage.getArtBox().getWidth() + ", LLX = " + pdfPage.getArtBox().getLLX() + ", LLY = "
                + pdfPage.getArtBox().getLLY() + ", URX = " + pdfPage.getArtBox().getURX() + ", URY = "
                + pdfPage.getArtBox().getURY());
        System.out.printf("\n BleedBox : Height = " + pdfPage.getBleedBox().getHeight() + ", Width = "
                + pdfPage.getBleedBox().getWidth() + ", LLX = " + pdfPage.getBleedBox().getLLX() + ", LLY = "
                + pdfPage.getBleedBox().getLLY() + ", URX = " + pdfPage.getBleedBox().getURX() + ", URY = "
                + pdfPage.getBleedBox().getURY());
        System.out.printf("\n CropBox : Height = " + pdfPage.getCropBox().getHeight() + ", Width = "
                + pdfPage.getCropBox().getWidth() + ", LLX = " + pdfPage.getCropBox().getLLX() + ", LLY = "
                + pdfPage.getCropBox().getLLY() + ", URX = " + pdfPage.getCropBox().getURX() + ", URY = "
                + pdfPage.getCropBox().getURY());
        System.out.printf("\n MediaBox : Height = " + pdfPage.getMediaBox().getHeight() + ", Width = "
                + pdfPage.getMediaBox().getWidth() + ", LLX = " + pdfPage.getMediaBox().getLLX() + ", LLY = "
                + pdfPage.getMediaBox().getLLY() + ", URX = " + pdfPage.getMediaBox().getURX() + ", URY = "
                + pdfPage.getMediaBox().getURY());
        System.out.printf("\n TrimBox : Height = " + pdfPage.getTrimBox().getHeight() + ", Width = "
                + pdfPage.getTrimBox().getWidth() + ", LLX = " + pdfPage.getTrimBox().getLLX() + ", LLY = "
                + pdfPage.getTrimBox().getLLY() + ", URX = " + pdfPage.getTrimBox().getURX() + ", URY = "
                + pdfPage.getTrimBox().getURY());
        System.out.printf(
                "\n Rect : Height = " + pdfPage.getRect().getHeight() + ", Width = " + pdfPage.getRect().getWidth()
                        + ", LLX = " + pdfPage.getRect().getLLX() + ", LLY = " + pdfPage.getRect().getLLY() + ", URX = "
                        + pdfPage.getRect().getURX() + ", URY = " + pdfPage.getRect().getURY());
        System.out.printf("\n Page Number :- " + pdfPage.getNumber());
        System.out.printf("\n Rotate :-" + pdfPage.getRotate());
    }
```

## ページの色を決定する

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスは、PDF ドキュメント内の特定のページに関連するプロパティを提供し、ページが使用する色の種類 - RGB、白黒、グレースケール、または未定義 - を含みます。

PDF ファイルのすべてのページは、[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) コレクションによって含まれています。[ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) プロパティは、ページ上の要素の色を指定します。特定の PDF ページの色情報を取得または決定するには、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラス オブジェクトの [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) プロパティを使用します。

次のコードスニペットは、PDFファイルの個々のページを反復して色情報を取得する方法を示しています。

```java
    public static void DeterminePageColor () {

        Document pdfDocument = new Document("input.pdf");
        // PDFファイルのすべてのページを反復
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // 特定のPDFページの色タイプ情報を取得
            int pageColorType = pdfDocument.getPages().get_Item(pageCount).getColorType();
            switch (pageColorType) {
            case 2:
                System.out.println("ページ # -" + pageCount + " は白黒です..");
                break;
            case 1:
                System.out.println("ページ # -" + pageCount + " はグレースケールです...");
                break;
            case 0:
                System.out.println("ページ # -" + pageCount + " はRGBです..");
                break;
            case 3:
                System.out.println("ページ # -" + pageCount + " の色は未定義です..");
                break;
            }
        }
    }
}
```
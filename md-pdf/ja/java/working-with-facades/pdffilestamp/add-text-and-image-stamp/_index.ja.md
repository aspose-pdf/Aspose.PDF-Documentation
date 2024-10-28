---
title: テキストと画像スタンプの追加
type: docs
weight: 20
url: /java/add-text-and-image-stamp/
description: このセクションでは、PdfFileStampクラスを使用してcom.aspose.pdf.facadesでテキストと画像スタンプを追加する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルのすべてのページにテキストスタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスを使用すると、PDFファイルのすべてのページにテキストスタンプを追加できます。
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.  
テキストスタンプを追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスと [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) クラスのオブジェクトを作成する必要があります。 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) クラスの BindLogo メソッドを使用してテキストスタンプを作成する必要もあります。他の属性（原点、回転、背景など）を [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) オブジェクトを使用して設定することもできます。その後、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) メソッドを使用して、PDF ファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) メソッドを使用して出力 PDF ファイルを保存します。次のコードスニペットは、PDF ファイルのすべてのページにテキストスタンプを追加する方法を示しています。

```java
 public static void AddTextStampOnAllPagesInPdfFile() {
        // PdfFileStamp オブジェクトの作成
        PdfFileStamp fileStamp = new PdfFileStamp();

        // ドキュメントを開く
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // スタンプを作成
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // PDF ファイルにスタンプを追加
        fileStamp.addStamp(stamp);

        // 更新された PDF ファイルを保存
        fileStamp.save(_dataDir + "AddTextStamp-All_out.pdf");

        // fileStamp を閉じる
        fileStamp.close();
    }
```

## 特定のページにテキストスタンプを追加する

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスを使用すると、PDFファイルの特定のページにテキストスタンプを追加することができます。
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

テキストスタンプを追加するには、最初に [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)クラスと[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp)クラスのオブジェクトを作成する必要があります。 You also need to create the text stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) メソッドを使用して、[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) クラスのテキストスタンプを作成する必要があります。 You can set other attributes like origin, rotation, background etc.  
他の属性（原点、回転、背景など）を設定できます。 using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) オブジェクトも使用します。 特定のページにテキストスタンプを追加したい場合は、[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) クラスの [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) プロパティを設定する必要があります。このプロパティは、スタンプを追加したいページ番号を含む整数の配列を必要とします。その後、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) メソッドを使用してPDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、特定のページにテキストスタンプを追加する方法を示しています。

```java
public static void AddTextStampOnParticularPagesInPdfFile() {
    // PdfFileStampオブジェクトを作成
    PdfFileStamp fileStamp = new PdfFileStamp();

    // ドキュメントを開く
    fileStamp.bindPdf(_dataDir + "sample.pdf");

    // スタンプを作成
    Stamp stamp = new Stamp();
    stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
            EncodingType.Winansi, true, 14));
    stamp.setOrigin(10, 400);
    stamp.setRotation(90.0F);
    stamp.setBackground(true);

    // 特定のページを設定
    stamp.setPages(new int[] { 2 });

    // PDFファイルにスタンプを追加
    fileStamp.addStamp(stamp);

    // 更新されたPDFファイルを保存
    fileStamp.save(_dataDir + "AddTextStamp-Page_out.pdf");

    // fileStampを閉じる
    fileStamp.close();
}
```

## PDFファイルのすべてのページに画像スタンプを追加する

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスを使用すると、PDFファイルのすべてのページに画像スタンプを追加できます。
 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

画像スタンプを追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスと [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) クラスのオブジェクトを作成する必要があります。 You also need to create the image stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) object as well. Then you can add the stamp in the PDF file using [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add image stamp on all pages in a PDF file.

```java
public static void AddImageStampOnParticularPagesInPdfFile() {
        // PdfFileStampオブジェクトを作成する
        PdfFileStamp fileStamp = new PdfFileStamp();

        // ドキュメントを開く
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // スタンプを作成する
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // PDFファイルにスタンプを追加する
        fileStamp.addStamp(stamp);

        // 更新されたPDFファイルを保存する
        fileStamp.save(_dataDir + "AddImageStamp-All_out.pdf");

        // fileStampを閉じる
        fileStamp.close();
    }
```

### スタンプとして追加する際の画像品質の管理

画像をスタンプオブジェクトとして追加する際に、画像の品質を制御することもできます。この要件を達成するために、[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) クラスに Quality プロパティが追加されています。これは、画像の品質をパーセンテージで示しています（有効な値は 0..100 です）。

## PDFファイルの特定のページに画像スタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスは、PDFファイルの特定のページに画像スタンプを追加することを可能にします。
 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

画像スタンプを追加するためには、まず[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)クラスと[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp)クラスのオブジェクトを作成する必要があります。 You also need to create the image stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) メソッドを [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) クラスの使用してイメージスタンプを作成する必要があります。 You can set other attributes like origin, rotation, background etc.  
他の属性（起点、回転、背景など）を設定できます。 using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) オブジェクトも使用します。 特定のページに画像スタンプを追加したい場合は、[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) クラスの [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) プロパティも設定する必要があります。このプロパティには、スタンプを追加したいページの番号を含む整数配列が必要です。その後、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) メソッドを使用して、PDF ファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) メソッドを使用して、出力 PDF ファイルを保存します。以下のコードスニペットは、特定のページに画像スタンプを追加する方法を示しています。

```java
  public static void AddImageStampOnAllPagesInPdfFile() {
        // PdfFileStamp オブジェクトを作成
        PdfFileStamp fileStamp = new PdfFileStamp();

        // ドキュメントを開く
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // スタンプを作成
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // 特定のページを設定
        stamp.setPages(new int[] { 2 });

        // PDF ファイルにスタンプを追加
        fileStamp.addStamp(stamp);

        // 更新された PDF ファイルを保存
        fileStamp.save(_dataDir + "AddImageStamp-Page_out.pdf");

        // fileStamp を閉じる
        fileStamp.close();
    }
```
---
title: ヘッダーとフッターの管理
type: docs
weight: 40
url: ja/java/manage-header-and-footer/
description: このセクションでは、PdfFileStampクラスを使用してAspose.PDF Facadesでヘッダーとフッターを管理する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルにヘッダーを追加する

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスを使用すると、PDFファイルにヘッダーを追加できます。
 In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.  
  
ヘッダーを追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスのオブジェクトを作成する必要があります。 ヘッダーテキストをフォーマットするには、[FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) クラスを使用できます。ファイルにヘッダーを追加する準備ができたら、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) メソッドを呼び出す必要があります。また、[addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) メソッドで少なくとも上部マージンを指定する必要があります。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#close--) メソッドを使用して、出力PDFファイルを保存します。次のコードスニペットは、PDFファイルにヘッダーを追加する方法を示しています。

```java
 public static void AddHeader() {
        // PdfFileStampオブジェクトを作成
        PdfFileStamp fileStamp = new PdfFileStamp();

        // ドキュメントを開く
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // ページ番号の書式設定されたテキストを作成
        FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!", java.awt.Color.YELLOW,
                java.awt.Color.BLACK, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // ヘッダーを追加
        fileStamp.addHeader(formattedText, 20);

        // 更新されたPDFファイルを保存
        fileStamp.save(_dataDir + "AddHeader_out.pdf");

        // fileStampを閉じる
        fileStamp.close();
    }
```

## PDFファイルにフッターを追加

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスを使用すると、PDFファイルにフッターを追加できます。
 In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. 

フッターを追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスのオブジェクトを作成する必要があります。 You can format the footer text using [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) class. Once you’re ready to add footer in the file, you need to call [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. You also need to specify at least the bottom margin in the [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) method. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add footer in a PDF file.

```java
 public static void AddFooter() {
        // PdfFileStampオブジェクトを作成
        PdfFileStamp fileStamp = new PdfFileStamp();

        // ドキュメントを開く
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // ページ番号の書式設定されたテキストを作成
        FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!", java.awt.Color.BLUE,
                java.awt.Color.GRAY, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // フッターを追加
        fileStamp.addFooter(formattedText, 10);

        // 更新されたPDFファイルを保存
        fileStamp.save(_dataDir + "AddFooter_out.pdf");

        // fileStampを閉じる
        fileStamp.close();
    }
```

## 既存のPDFファイルのヘッダーに画像を追加する

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスを使用すると、PDFファイルのヘッダーに画像を追加できます。
 ヘッダーに画像を追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスのオブジェクトを作成する必要があります。その後、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) メソッドを呼び出す必要があります。このメソッドに画像を渡すことができます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) メソッドを使用して、出力 PDF ファイルを保存します。以下のコードスニペットは、PDF ファイルのヘッダーに画像を追加する方法を示しています。

```java
public static void AddImageHeader() {
        // PdfFileStamp オブジェクトを作成
        PdfFileStamp fileStamp = new PdfFileStamp();

        // ドキュメントを開く
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // ヘッダーを追加
            fileStamp.addHeader(fs, 10);

            // 更新された PDF ファイルを保存
            fileStamp.save(_dataDir + "AddImage-Header_out.pdf");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        }

        // fileStamp を閉じる
        fileStamp.close();
    }
```

## 既存のPDFファイルのフッターに画像を追加する

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスを使用すると、PDFファイルのフッターに画像を追加することができます。
 ドキュメントに画像を追加するためには、まず [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスのオブジェクトを作成する必要があります。その後、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) メソッドを呼び出す必要があります。画像を [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) メソッドに渡すことができます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) メソッドを使用して、出力 PDF ファイルを保存します。以下のコードスニペットは、PDF ファイルのフッターに画像を追加する方法を示しています。

```java
    public static void AddImageFooter() {
        // PdfFileStampオブジェクトを作成する
        PdfFileStamp fileStamp = new PdfFileStamp();

        // ドキュメントを開く
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // フッターを追加する
            fileStamp.addFooter(fs, 10);

            // 更新されたPDFファイルを保存する
            fileStamp.save(_dataDir + "AddImage-Footer_out.pdf");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // fileStampを閉じる
        fileStamp.close();
    }
```
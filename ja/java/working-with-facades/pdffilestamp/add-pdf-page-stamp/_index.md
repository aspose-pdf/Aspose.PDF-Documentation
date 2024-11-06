---
title: PDFページスタンプの追加
type: docs
weight: 10
url: ja/java/add-pdf-page-stamp/
description: このセクションでは、PdfFileStampクラスを使用してAspose.PDF Facadesを操作する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルのすべてのページにPDFページスタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスを使用すると、PDFファイルのすべてのページにPDFページスタンプを追加できます。
 In order to add PDFページスタンプを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)クラスと[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp)クラスのオブジェクトを作成する必要があります。 また、[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) クラスの [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) メソッドを使用して PDF ページスタンプを作成する必要があります。[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) オブジェクトを使用して、原点、回転、背景などの他の属性を設定することもできます。その後、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) メソッドを使用して PDF ファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスの [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) メソッドを使用して出力 PDF ファイルを保存します。次のコードスニペットは、PDF ファイルのすべてのページに PDF ページスタンプを追加する方法を示しています。

```csharp
public static void AddPageStampOnAllPages()
        {
            // PdfFileStamp オブジェクトを作成
            PdfFileStamp fileStamp = new PdfFileStamp();

            // ドキュメントを開く
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // スタンプを作成
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // PDF ファイルにスタンプを追加
            fileStamp.AddStamp(stamp);

            // 更新された PDF ファイルを保存
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // fileStamp を閉じる
            fileStamp.Close();
        }
```

## 特定のページにPDFページスタンプを追加する

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスを使用すると、PDFファイルの特定のページにPDFページスタンプを追加することができます。
 In order to add PDFページスタンプを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)クラスと[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp)クラスのオブジェクトを作成する必要があります。 You also need to create the PDF page stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class.  

また、[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) クラスの [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) メソッドを使用して、PDF ページ スタンプを作成する必要があります。 You can set other attributes like origin, rotation, background etc. あなたは、起点、回転、背景などの他の属性を設定することができます。 using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) オブジェクトも使用します。 PDFファイルの特定のページにPDFページスタンプを追加したい場合、[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp)クラスの[Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-)プロパティも設定する必要があります。このプロパティには、スタンプを追加したいページの番号を含む整数配列が必要です。その後、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)クラスの[addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-)メソッドを使用してPDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)クラスの[close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルの特定のページにPDFページスタンプを追加する方法を示しています。

```csharp
public static void AddPageStampOnCertainPages()
        {
            // PdfFileStampオブジェクトを作成
            PdfFileStamp fileStamp = new PdfFileStamp();

            // ドキュメントを開く
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // スタンプを作成
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // PDFファイルにスタンプを追加
            fileStamp.AddStamp(stamp);

            // 更新されたPDFファイルを保存
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // fileStampを閉じる
            fileStamp.Close();
        }

        // PDFページ番号を追加
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

## PDFファイルにページ番号を追加する (facades)

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスを使用すると、PDFファイルにページ番号を追加することができます。
 In order to add page numbers, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. 

ページ番号を追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスのオブジェクトを作成する必要があります。 ページ番号を「Page X of N」のように表示したい場合、Xが現在のページ番号でNがPDFファイル内の総ページ数であるとすると、まず[getNumberOfPages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo)プロパティを使用してページ数を取得する必要があります。現在のページ番号を取得するには、テキスト内の任意の場所に**#**記号を使用できます。[FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText)クラスを使用してページ番号のテキストをフォーマットすることができます。特定の番号からページ番号を開始したい場合は、setStartingNumberプロパティを設定することができます。ファイルにページ番号を追加する準備ができたら、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)クラスのaddPageNumberメソッドを呼び出す必要があります。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)クラスのSaveメソッドを使用して出力PDFファイルを保存します。

次のコードスニペットは、PDFファイルにページ番号を追加する方法を示しています。
```java
 public static void AddPageNumberInPdfFile() {
        // PdfFileStampオブジェクトを作成
        PdfFileStamp fileStamp = new PdfFileStamp();

        // ドキュメントを開く
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 総ページ数を取得
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // ページ番号用のフォーマットされたテキストを作成
        FormattedText formattedText = new FormattedText("Page # of " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // 最初のページの開始番号を設定; 2以上から始めたい場合
        fileStamp.setStartingNumber(1);

        // ページ番号を追加
        fileStamp.addPageNumber(formattedText, (int) PageNumPosition.PosUpperRight.ordinal());

        // 更新されたPDFファイルを保存
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // fileStampを閉じる
        fileStamp.close();
    }
```

### カスタム番号スタイル

The [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) クラスは、PDF ドキュメント内にスタンプオブジェクトとしてページ番号情報を追加する機能を提供します。このリリース以前は、このクラスはページ番号スタイルとして 1,2,3,4 のみをサポートしていました。しかし、PDF ドキュメント内にページ番号スタンプを配置する際にカスタム番号スタイルを使用したいという顧客からの要求がありました。この要件を達成するために、[NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) プロパティが導入されました。このプロパティは、[NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) 列挙体からの値を受け入れます。以下に、この列挙体で提供されている値を指定します。

```java
 public static void AddCustomPageNumberInPdfFile() {
        // PdfFileStamp オブジェクトを作成
        PdfFileStamp fileStamp = new PdfFileStamp();

        // ドキュメントを開く
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // ページの総数を取得
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // ページ番号のフォーマットされたテキストを作成
        FormattedText formattedText = new FormattedText("Page # of " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // 番号スタイルをローマ数字大文字に指定
        fileStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);

        // 最初のページの開始番号を設定; 2 以上から開始することもできます
        fileStamp.setStartingNumber(1);

        // ページ番号を追加
        fileStamp.addPageNumber(formattedText, PageNumPosition.PosUpperRight.ordinal());

        // 更新された PDF ファイルを保存
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // fileStamp を閉じる
        fileStamp.close();
    }
```
---
title: PDFページスタンプを追加
type: docs
weight: 10
url: /ja/net/add-pdf-page-stamp/
description: このセクションでは、PdfFileStampクラスを使用してAspose.PDF Facadesを操作する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルのすべてのページにPDFページスタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp)クラスを使用すると、PDFファイルのすべてのページにPDFページスタンプを追加できます。 In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

PDFページスタンプを追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスと [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスのオブジェクトを作成する必要があります。 You also need to create the PDF page stamp using [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) メソッドの [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラス。起源、回転、背景などの他の属性を [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) オブジェクトを使用して設定することもできます。その後、[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) メソッドの [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスを使用してPDFファイルにスタンプを追加できます。最後に、[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) メソッドの [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスを使用して、出力PDFファイルを保存します。次のコードスニペットは、PDFファイル内のすべてのページにPDFページスタンプを追加する方法を示しています。

```csharp
public static void AddPageStampOnAllPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## 特定のページにPDFページスタンプを追加する

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスを使用すると、PDFファイルの特定のページにPDFページスタンプを追加できます。 
PDFページスタンプを追加するには、まず[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp)クラスと[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp)クラスのオブジェクトを作成する必要があります。
``` You also need to create the PDFページスタンプを作成する必要があります。 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスの。 You can set other attributes like origin, rotation, background etc.  
他の属性、例えば原点、回転、背景などを設定できます。 using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) オブジェクトも使用します。 As you want to add PDF page stamp on particular pages of the PDF file, you also need to set the [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) property of the [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add PDF page stamp on particular pages in a PDF file.

PDFファイルの特定のページにPDFページスタンプを追加したい場合は、[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスの [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) プロパティを設定する必要があります。このプロパティには、スタンプを追加したいページの番号を含む整数の配列が必要です。その後、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスの [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) メソッドを使用してPDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスの [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) メソッドを使用して、出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルの特定のページにPDFページスタンプを追加する方法を示しています。

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }

        // Add PDF Page Numbers
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```
## PDFファイルにページ番号を追加

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスを使用すると、PDFファイルにページ番号を追加できます。 In order to add page numbers, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class.

ページ番号を追加するためには、まず [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスのオブジェクトを作成する必要があります。 If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) property of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class.

PDFファイル内で現在のページ番号をX、総ページ数をNとすると、「Page X of N」のようにページ番号を表示したい場合、まず、[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo)クラスの[NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages)プロパティを使用してページ数を取得する必要があります。 ```
現在のページ番号を取得するには、テキスト内の任意の場所に **#** 記号を使用できます。ページ番号のテキストをフォーマットするには、[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) クラスを使用できます。特定の番号からページ番号を開始したい場合は、[StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber) プロパティを設定できます。ファイルにページ番号を追加する準備が整ったら、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp) クラスの [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) メソッドを呼び出す必要があります。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスの [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) メソッドを使用して、出力 PDF ファイルを保存します。次のコードスニペットは、PDF ファイルにページ番号を追加する方法を示しています。
```csharp
 public static void AddPageNumberInPdfFile()
        {
            // PdfFileStamp オブジェクトを作成
            PdfFileStamp fileStamp = new PdfFileStamp();

            // ドキュメントを開く
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 総ページ数を取得
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // ページ番号のフォーマットされたテキストを作成
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // 最初のページの開始番号を設定; 2以上から開始することもできます
            fileStamp.StartingNumber = 1;

            // ページ番号を追加
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // 更新された PDF ファイルを保存
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // fileStamp を閉じる
            fileStamp.Close();
        }
```
```
### カスタム番号スタイル

PdfFileStamp クラスは、PDF ドキュメント内にスタンプオブジェクトとしてページ番号情報を追加する機能を提供します。このリリース以前は、クラスは 1,2,3,4 のみをページ番号スタイルとしてサポートしていました。しかし、PDF ドキュメント内にページ番号スタンプを配置する際にカスタム番号スタイルを使用したいという要件が一部の顧客からありました。この要件を達成するために、[NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) プロパティが導入されました。このプロパティは、[NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) 列挙からの値を受け入れます。以下に、この列挙で提供されている値を示します。

- LettersLowercase
- LettersUppercase
- NumeralsArabic
- NumeralsRomanLowercase
- NumeralsRomanUppercase

```csharp
 public static void AddCustomPageNumberInPdfFile()
        {
            // PdfFileStamp オブジェクトを作成
            PdfFileStamp fileStamp = new PdfFileStamp();

            // ドキュメントを開く
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 総ページ数を取得
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // ページ番号用にフォーマットされたテキストを作成
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // 番号スタイルをローマ数字の大文字に指定
            fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

            // 最初のページの開始番号を設定; 2以上から開始することもできます
            fileStamp.StartingNumber = 1;

            // ページ番号を追加
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // 更新された PDF ファイルを保存
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // fileStamp を閉じる
            fileStamp.Close();
        }
```
```
---
title: テキストと画像スタンプの追加
type: docs
weight: 20
url: /ja/net/add-text-and-image-stamp/
description: このセクションでは、PdfFileStampクラスを使用してAspose.PDF Facadesでテキストと画像のスタンプを追加する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルのすべてのページにテキストスタンプを追加する

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスを使用すると、PDFファイルのすべてのページにテキストスタンプを追加できます。
``` In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

テキストスタンプを追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスと [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスのオブジェクトを作成する必要があります。 あなたはまた、[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスの [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) メソッドを使用してテキストスタンプを作成する必要があります。原点、回転、背景などの他の属性を [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) オブジェクトを使用して設定することもできます。その後、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスの [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) メソッドを使用して、PDF ファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスの [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) メソッドを使用して、出力 PDF ファイルを保存します。以下のコードスニペットは、PDF ファイルのすべてのページにテキストスタンプを追加する方法を示しています。

```csharp
 public static void AddTextStampOnAllPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Stamp stamp = new Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddTextStamp-All_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## 特定のページにテキストスタンプを追加する

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスを使用すると、PDFファイルの特定のページにテキストスタンプを追加できます。 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

テキストスタンプを追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスと [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスのオブジェクトを作成する必要があります。 You also need to create the text stamp using [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.  
テキストスタンプを作成するには、[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスの [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) メソッドを使用する必要があります。 You can set other attributes like origin, rotation, background etc.  
他の属性（例えば、起点、回転、背景など）を設定できます。 
using [スタンプ](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) オブジェクトも使用します。
``` 特定のPDFファイルのページにテキストスタンプを追加したい場合は、[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp)クラスの[Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages)プロパティを設定する必要があります。このプロパティには、スタンプを追加したいページの番号を含む整数配列が必要です。次に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp)クラスの[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp)メソッドを使用して、PDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp)クラスの[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して、出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルの特定のページにテキストスタンプを追加する方法を示しています。

```csharp
 public static void AddTextStampOnParticularPagesInPdfFile()
        {
            // PdfFileStampオブジェクトを作成
            PdfFileStamp fileStamp = new PdfFileStamp();

            // ドキュメントを開く
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // スタンプを作成
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // 特定のページを設定
            stamp.Pages = new int[] { 2 };

            // PDFファイルにスタンプを追加
            fileStamp.AddStamp(stamp);

            // 更新されたPDFファイルを保存
            fileStamp.Save(_dataDir + "AddTextStamp-Page_out.pdf");

            // fileStampを閉じる
            fileStamp.Close();
        }
```
## 全ページに画像スタンプを追加する方法

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスを使用すると、PDFファイルのすべてのページに画像スタンプを追加できます。 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

画像スタンプを追加するためには、まず [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスと [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスのオブジェクトを作成する必要があります。 あなたはまた、[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp)クラスの[BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index)メソッドを使用して、画像のスタンプを作成する必要があります。[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp)オブジェクトを使用して、原点、回転、背景などの他の属性を設定することもできます。その後、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp)クラスの[AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp)メソッドを使用して、スタンプをPDFファイルに追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp)クラスの[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して、出力されたPDFファイルを保存します。以下のコードスニペットは、PDFファイルのすべてのページに画像スタンプを追加する方法を示しています。

```csharp
public static void AddImageStampOnAllPagesInPdfFile()
        {
            // PdfFileStampオブジェクトを作成
            PdfFileStamp fileStamp = new PdfFileStamp();

            // ドキュメントを開く
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // スタンプを作成
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // 特定のページを設定
            stamp.Pages = new int[] { 2 };

            // PDFファイルにスタンプを追加
            fileStamp.AddStamp(stamp);

            // 更新されたPDFファイルを保存
            fileStamp.Save(_dataDir + "AddImageStamp-Page_out.pdf");

            // fileStampを閉じる
            fileStamp.Close();
        }
```
### スタンプとして追加する際の画像品質を制御

画像をスタンプオブジェクトとして追加する際、画像の品質も制御できます。この要件を達成するために、[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスに Quality プロパティが追加されました。これは画像の品質をパーセントで示します（有効な値は0..100です）。

## PDFファイルの特定のページに画像スタンプを追加

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスを使用すると、PDFファイルの特定のページに画像スタンプを追加できます。 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

画像スタンプを追加するためには、まず [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスと [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスのオブジェクトを作成する必要があります。 You also need to create the image stamp using [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) method of [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class.  
イメージスタンプを作成するには、[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスの [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) メソッドを使用する必要があります。 You can set other attributes like origin, rotation, background etc.

他の属性を設定することができます。たとえば、origin、rotation、backgroundなどです。 using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) オブジェクトも使用します。PDFファイルの特定のページに画像スタンプを追加したい場合は、[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) クラスの [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) プロパティを設定する必要があります。このプロパティには、スタンプを追加したいページの番号を含む整数配列が必要です。その後、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスの [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) メソッドを使用してPDFファイルにスタンプを追加できます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) クラスの [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルの特定のページに画像スタンプを追加する方法を示しています。

```csharp
 public static void AddImageStampOnParticularPagesInPdfFile()
        {
            // PdfFileStampオブジェクトを作成
            PdfFileStamp fileStamp = new PdfFileStamp();

            // ドキュメントを開く
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // スタンプを作成
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // PDFファイルにスタンプを追加
            fileStamp.AddStamp(stamp);

            // 更新されたPDFファイルを保存
            fileStamp.Save(_dataDir + "AddImageStamp-All_out.pdf");

            // fileStampを閉じる
            fileStamp.Close();
        }
```
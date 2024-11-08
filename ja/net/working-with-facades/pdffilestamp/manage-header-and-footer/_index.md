---
title: ヘッダーとフッターの管理
type: docs
weight: 40
url: /ja/net/manage-header-and-footer/
description: このセクションでは、PdfFileStampクラスを使用してAspose.PDF Facadesでヘッダーとフッターを管理する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルにヘッダーを追加

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスを使用すると、PDFファイルにヘッダーを追加できます。 In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

ヘッダーを追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスのオブジェクトを作成する必要があります。 You can format the header text using [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) class. Once you’re ready to add header in the file, you need to call [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main) class. You also need to specify at least the top margin in the [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main) class. The following code snippet shows you how to add header in a PDF file.

ヘッダーテキストをフォーマットするには、[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) クラスを使用できます。ファイルにヘッダーを追加する準備ができたら、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main) クラスの [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) メソッドを呼び出す必要があります。また、[AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) メソッドで少なくとも上の余白を指定する必要があります。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main) クラスの [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) メソッドを使用して出力 PDF ファイルを保存します。次のコードスニペットは、PDF ファイルにヘッダーを追加する方法を示しています。

```csharp
 public static void AddHeader()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create formatted text for page number
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Yellow,
                System.Drawing.Color.Black,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Add header
            fileStamp.AddHeader(formattedText, 10);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddHeader_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## PDFファイルにフッターを追加する

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスを使用すると、PDFファイルにフッターを追加できます。 In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

フッターを追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスのオブジェクトを作成する必要があります。 あなたは[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)クラスを使用してフッターテキストをフォーマットすることができます。ファイルにフッターを追加する準備ができたら、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスの[AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index)メソッドを呼び出す必要があります。また、[AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index)メソッドで少なくとも下マージンを指定する必要があります。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main)クラスの[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close)メソッドを使用して出力PDFファイルを保存します。以下のコードスニペットは、PDFファイルにフッターを追加する方法を示しています。

```csharp
 public static void AddFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create formatted text for page number
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Blue,
                System.Drawing.Color.Gray,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Add footer
            fileStamp.AddFooter(formattedText, 10);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddFooter_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## 既存のPDFファイルのヘッダーに画像を追加

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスを使用すると、PDFファイルのヘッダーに画像を追加できます。 ヘッダーに画像を追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスのオブジェクトを作成する必要があります。その後、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main) クラスの [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) メソッドを呼び出す必要があります。画像を [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) メソッドに渡すことができます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスの [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) メソッドを使用して、出力 PDF ファイルを保存します。次のコードスニペットは、PDFファイルのヘッダーに画像を追加する方法を示しています。

```csharp
public static void AddImageHeader()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add Header
                fileStamp.AddHeader(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Header_out.pdf");
                // Close fileStamp
                fileStamp.Close();
            }
        }
```
## 既存のPDFファイルのフッターに画像を追加する

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスを使用すると、PDFファイルのフッターに画像を追加できます。 In order to add image in footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. After that, you need to call [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You can pass the image to the [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. The following code snippet shows you how to add image in the footer of PDF file.

フッターに画像を追加するには、まず [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスのオブジェクトを作成する必要があります。その後、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスの [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) メソッドを呼び出す必要があります。画像を [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) メソッドに渡すことができます。最後に、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) クラスの [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) メソッドを使用して、出力 PDF ファイルを保存します。次のコードスニペットは、PDF ファイルのフッターに画像を追加する方法を示しています。

```csharp
public static void AddImageFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add footer
                fileStamp.AddFooter(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Footer_out.pdf");

                // Close fileStamp
                fileStamp.Close();
            }
        }
```
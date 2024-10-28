---
title: PDFファイルに署名を追加
type: docs
weight: 10
url: /net/add-signature-in-pdf/
description: このセクションでは、PdfFileSignatureクラスを使用してPDFファイルに署名を追加する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルにデジタル署名を追加

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) クラスを使用すると、PDFファイルに署名を追加できます。
``` ドキュメントの翻訳対象テキストは以下の通りです：

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) クラスのオブジェクトを入力および出力PDFファイルを使用して作成する必要があります。また、署名を追加したい [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) オブジェクトを作成し、外観を設定するために [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) オブジェクトの [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) プロパティを使用して画像を指定できます。Aspose.Pdf.Facades は、PKCS#1、PKCS#7、PKCS#7Detached のような異なる種類の署名も提供しています。特定の種類の署名を作成するには、証明書ファイルとパスワードを使用して **PKCS1**、**PKCS7** または **PKCS7Detached** のような特定のクラスのオブジェクトを作成する必要があります。

特定の署名タイプのオブジェクトが作成されたら、[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) クラスの [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) メソッドを使用してPDFに署名し、このクラスに特定の署名オブジェクトを渡すことができます。 You can also specify other attributes for this method. Finally, you need to save the signed PDF using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method of the [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class. The following code snippet shows you how to add signature in a PDF file.

あなたはこのメソッドの他の属性も指定することができます。最後に、[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)クラスの[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index)メソッドを使用して署名されたPDFを保存する必要があります。次のコードスニペットは、PDFファイルに署名を追加する方法を示しています。

```csharp
public static void AddPdfFileSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for signature location
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Set signature appearance
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```
次のコード例は、2つの署名でドキュメントに署名する機能を示しています。私たちの例では、1つ目の署名を最初のページに、2つ目を2番目のページに置きます。必要なページを指定することができます。

```csharp
 public static void AddTwoSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();

            // 1つ目の署名で署名する

            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // 1つ目の署名位置のための長方形を作成する
            System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // 1つ目の署名オブジェクトを作成する
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "私は文書の著者です", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
            pdfSign.Save(_dataDir + "DigitallySign.pdf");


            // 2つ目の署名で署名する

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // 2つ目の署名位置のための長方形を作成する
            System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // 2つ目の署名オブジェクトを作成する
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(2, "私は文書のレビュアーです", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

            // 出力PDFファイルを保存する
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

ドキュメントに署名が必要なフォームまたはアクロフォームが含まれている場合は、次の例を参照してください。入力および出力PDFファイルを使用して[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)クラスのオブジェクトを作成する必要があります。[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1)を使用してバインドします。必要なプロパティを追加できる署名を作成します。この例では「Reason」と「CustomAppearance」です。

```csharp
 public static void AddPdfFileSignatureField()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample02.pdf");

            // 3つの署名タイプのいずれかを作成
            PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Sign as Author",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6,
                    FontFamilyName = "Calibri"
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature);
            // 出力PDFファイルを保存
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

ドキュメントに2つのフィールドがある場合、その署名アルゴリズムは最初の例と似ています。

```csharp
public static void AddPdfFileSignatureField2()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample03.pdf");

            // 3つの署名タイプのいずれかを作成
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021")
            {
                Reason = "著者として署名",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature1);
            // 出力PDFファイルを保存
            pdfSign.Save(_dataDir + "DigitallySign.pdf");

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // 3つの署名タイプのいずれかを作成
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "レビュワーとして署名",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature2", signature2);
            // 出力PDFファイルを保存
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```
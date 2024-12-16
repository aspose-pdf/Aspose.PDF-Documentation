---
title: PDFファイルに署名を追加する
type: docs
weight: 10
url: /ja/java/add-signature-in-pdf/
description: このセクションでは、PdfFileSignatureクラスを使用してPDFファイルで署名を操作する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルにデジタル署名を追加する (facades)

[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) クラスを使用すると、PDFファイルに署名を追加できます。入力および出力PDFファイルを使用して [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) クラスのオブジェクトを作成する必要があります。また、署名を追加したい位置にRectangleオブジェクトを作成し、外観を設定するために、[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) オブジェクトのsetSignatureAppearanceプロパティを使用して画像を指定できます。

Aspose.Pdf.Facadesは、PKCS#1、PKCS#7、およびPKCS#7Detachedのようなさまざまな種類の署名も提供します。
 特定のタイプの署名を作成するには、証明書ファイルとパスワードを使用して、PKCS1、PKCS7、またはPKCS7Detachedのような特定のクラスのオブジェクトを作成する必要があります。

特定の署名タイプのオブジェクトが作成されたら、[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) クラスの sign メソッドを使用してPDFに署名し、このクラスに特定の署名オブジェクトを渡すことができます。また、このメソッドに他の属性を指定することもできます。最後に、[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) クラスの save メソッドを使用して、署名されたPDFを保存する必要があります。以下のコードスニペットは、PDFファイルに署名を追加する方法を示しています。

```java
public static void AddPdfFileSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // 署名の位置を示す矩形を作成
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);
        // 署名の外観を設定
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // 三つの署名タイプのいずれかを作成
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect,
                signature);
        // 出力PDFファイルを保存
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

以下のコード例は、2つの署名でドキュメントに署名する機能を示しています。私たちの例では、1ページ目に最初の署名を、2ページ目に2番目の署名を配置します。必要なページを指定できます。

```java
    public static void AddTwoSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        // 1つ目の署名で署名する

        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // 1つ目の署名の場所のための四角形を作成する
        java.awt.Rectangle rect1 = new java.awt.Rectangle(10, 10, 300, 50);

        // 1つ目の署名オブジェクトを作成する
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "私はドキュメントの作成者です", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1,
                signature1);
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        // 2つ目の署名で署名する

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // 2つ目の署名の場所のための四角形を作成する
        java.awt.Rectangle rect2 = new java.awt.Rectangle(10, 10, 300, 50);

        // 2つ目の署名オブジェクトを作成する
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(2, "私はドキュメントのレビュアーです", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true,
                rect2, signature2);

        // 出力PDFファイルを保存する
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


ドキュメントに署名が必要なフォームやアクロフォームがある場合は、次の例を参照してください。  
入力および出力 PDF ファイルを使用して [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) クラスのオブジェクトを作成する必要があります。バインディングには bindPdf を使用します。必要なプロパティを追加する能力を持つ署名を作成します。私たちの例では、それらは「Reason」と「CustomAppearance」です。

```java
  public static void AddPdfFileSignatureField() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample02.pdf");

        // 3つの署名タイプのいずれかを作成
        PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature.setReason("Sign as Author");

        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        // PKCS#1
        pdfSign.sign("Signature1", signature);
        // 出力 PDF ファイルを保存
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


ドキュメントに2つのフィールドがある場合、その署名アルゴリズムは最初の例に似ています。

```java
   public static void AddPdfFileSignatureField2() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample03.pdf");

        // 3つの署名タイプのいずれかを作成
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021");
        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature1.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        signature1.setReason("著者として署名"); // PKCS#1
        pdfSign.sign("Signature1", signature1);

        // 出力PDFファイルを保存
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // 3つの署名タイプのいずれかを作成
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature2.setReason("レビュアーとして署名"); // PKCS#1
        signature2.setCustomAppearance(sca);
        pdfSign.sign("Signature2", signature2);
        // 出力PDFファイルを保存
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```
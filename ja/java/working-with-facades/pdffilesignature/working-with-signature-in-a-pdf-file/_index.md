---
title: PDFファイルでの署名の操作
type: docs
weight: 40
url: /ja/java/working-with-signature-in-a-pdf-file/
description: このセクションでは、PdfFileSignatureクラスを使用してPDFファイルで署名を操作する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 署名情報の抽出方法

Aspose.PDF for Javaは、PdfFileSignatureクラスを使用してPDFファイルにデジタル署名する機能をサポートしています。現在、証明書の有効性を判断することは可能ですが、証明書全体を抽出することはできません。抽出可能な情報は公開鍵、サムプリント、発行者などです。

署名情報を抽出するために、PdfFileSignatureクラスにextractCertificate(..)メソッドを導入しました。下記のコードスニペットは、PdfFileSignatureオブジェクトから証明書を抽出する手順を示しています:

```java
public static void ExtractSignatureInfo() {
        String input = _dataDir + "DigitallySign.pdf";
        String certificateFileName = "extracted_cert.pfx";
        PdfFileSignature pdfFileSignature = new PdfFileSignature();
        pdfFileSignature.bindPdf(input);
        List<String> sigNames = pdfFileSignature.getSignNames();

        if (sigNames.size() > 0) {
            String sigName = sigNames.get(0);
            if (sigName != "") {
                InputStream cerStream = pdfFileSignature.extractCertificate(sigName);
                if (cerStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(_dataDir + certificateFileName);
                        cerStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }
            }
        }
    }
```


## 署名フィールドからの画像抽出 (PdfFileSignature)

Aspose.PDF for Javaは、PdfFileSignatureクラスを使用してPDFファイルにデジタル署名を行う機能をサポートしており、文書に署名する際に、SignatureAppearanceに画像を設定することもできます。現在、このAPIは署名情報および署名フィールドに関連付けられた画像を抽出する機能も提供しています。

署名情報を抽出するために、PdfFileSignatureクラスに[extractImage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#extractImage-java.lang.String-)メソッドを導入しました。以下のコードスニペットは、PdfFileSignatureオブジェクトから画像を抽出する手順を示しています。

```java
 public static void ExtractSignatureImage() {
        PdfFileSignature signature = new PdfFileSignature();
        signature.bindPdf(_dataDir + "DigitallySign.pdf");
        if (signature.containsSignature()) {
            for (String sigName : signature.getSignNames()) {
                String outFile = _dataDir + sigName + "_ExtractImages_out.jpg";
                InputStream imageStream = signature.extractImage(sigName);
                if (imageStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(outFile);
                        imageStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
```


## 位置と理由の抑制

Aspose.PDF の機能は、デジタル署名インスタンスの柔軟な設定を可能にします。[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) クラスは、PDF ファイルに署名する機能を提供します。Sign メソッドの実装により、PDF に署名し、特定の署名オブジェクトをこのクラスに渡すことができます。Sign メソッドには、出力デジタル署名のカスタマイズのための一連の属性が含まれています。結果の署名から特定のテキスト属性を抑制する必要がある場合は、それらを空にしておくことができます。次のコードスニペットは、署名ブロックから位置と理由の2行を抑制する方法を示しています：

```java
public static void SupressLocationReason() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // 署名の場所のための長方形を作成
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // 署名の外観を設定
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // 3種類の署名タイプのいずれかを作成
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "", "test01@aspose-pdf-demo.local", "", true, rect, signature);
        // 出力PDFファイルを保存
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## デジタル署名のカスタマイズ機能

Aspose.PDF for Javaは、デジタル署名のカスタマイズ機能を提供します。クラスSignatureCustomAppearanceのSignメソッドは、便利に使用できるように6つのオーバーロードを実装しています。例えば、SignatureCustomAppearanceクラスのインスタンスとそのプロパティ値のみで結果の署名を設定できます。以下のコードスニペットは、PDFの出力デジタル署名から「Digitally signed by」キャプションを非表示にする方法を示しています。

```java
    public static void CustomizationFeaturesForDigitalSign() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // 署名位置の長方形を作成
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // 3つの署名タイプのいずれかを作成
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setFontSize(6);
        signatureCustomAppearance.setFontFamilyName("Times New Roman");
        signatureCustomAppearance.setDigitalSignedLabel("SIGNED BY:");
        signature.setCustomAppearance(signatureCustomAppearance);

        pdfSign.sign(1, true, rect, signature);
        // 出力PDFファイルを保存
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## デジタル署名テキストの言語を変更する

Aspose.PDF for Java APIを使用すると、以下の3つの署名タイプのいずれかを使用してPDFファイルに署名できます:

- PKCS#1
- PKCS#7
- PKCS#7

提供されている各署名には、利便性のために実装された設定プロパティのセットが含まれています（ローカライゼーション、日付時刻形式、フォントファミリーなど）。クラスSignatureCustomAppearanceは、対応する機能を提供します。次のコードスニペットは、デジタル署名テキストの言語を変更する方法を示しています:

```java
     public static void ChangeLanguageInDigitalSignText() {
        String inFile = _dataDir + "sample01.pdf";
        String outFile = _dataDir + "DigitallySign.pdf";

        PdfFileSignature pdfSign = new PdfFileSignature();

        pdfSign.bindPdf(inFile);
        // 署名位置のための四角形を作成
        java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);

        // 3つの署名タイプのいずれかを作成
        PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021");
        pkcs.setReason("Pruebas Firma");
        pkcs.setContactInfo("Contacto Pruebas");
        pkcs.setLocation("Población (Provincia)");
        pkcs.setDate(new Date());
        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setDateSignedAtLabel("Fecha");
        signatureCustomAppearance.setDigitalSignedLabel("Digitalmente firmado por");
        signatureCustomAppearance.setReasonLabel("Razón");
        signatureCustomAppearance.setLocationLabel("Localización");
        signatureCustomAppearance.setFontFamilyName("Arial");
        signatureCustomAppearance.setFontSize(10);
        signatureCustomAppearance.setCulture(new Locale("es", "ES"));
        // signatureCustomAppearance.setCulture (Locale.ROOT);
        signatureCustomAppearance.setDateTimeFormat("yyyy.MM.dd HH:mm:ss");
        pkcs.setCustomAppearance(signatureCustomAppearance);
        // PDFファイルに署名
        pdfSign.sign(1, true, rect, pkcs);
        // 出力PDFファイルを保存
        pdfSign.save(outFile);
    }
```
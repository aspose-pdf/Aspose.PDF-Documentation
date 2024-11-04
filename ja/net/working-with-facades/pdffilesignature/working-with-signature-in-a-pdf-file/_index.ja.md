---
title: PDFファイルでの署名の操作
type: docs
weight: 40
url: /net/working-with-signature-in-a-pdf-file/
description: このセクションでは、PdfFileSignatureクラスを使用して署名情報を抽出し、署名から画像を抽出し、言語を変更する方法などについて説明します。
lastmod: "2021-06-05"
draft: false
---

## 署名情報を抽出する方法

Aspose.PDF for .NETは、PdfFileSignatureクラスを使用してPDFファイルにデジタル署名する機能をサポートしています。現在、証明書の有効性を判断することは可能ですが、証明書全体を抽出することはできません。抽出可能な情報は公開鍵、サムプリント、発行者などです。

署名情報を抽出するために、PdfFileSignatureクラスにExtractCertificate(..)メソッドを導入しました。PdfFileSignatureオブジェクトから証明書を抽出する手順を示す以下のコードスニペットをご覧ください:

```csharp
public static void ExtractSignatureInfo()
        {
            string input = _dataDir + "DigitallySign.pdf";
            string certificateFileName = "extracted_cert.pfx";
            using (PdfFileSignature pdfFileSignature = new PdfFileSignature())
            {
                pdfFileSignature.BindPdf(input);
                var sigNames = pdfFileSignature.GetSignNames();
                if (sigNames.Count > 0)
                {
                    string sigName = sigNames[0];
                    if (!string.IsNullOrEmpty(sigName))
                    {
                        Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
                        if (cerStream != null)
                        {
                            using (cerStream)
                            {
                                using (FileStream fs = new FileStream(_dataDir + certificateFileName, FileMode.CreateNew))
                                {
                                    cerStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## 署名フィールドから画像を抽出する (PdfFileSignature)

Aspose.PDF for .NETは、PdfFileSignatureクラスを使用してPDFファイルにデジタル署名をする機能をサポートしており、ドキュメントに署名する際にSignatureAppearanceに画像を設定することもできます。現在、このAPIは署名フィールドに関連付けられた署名情報や画像を抽出する機能も提供しています。

署名情報を抽出するために、PdfFileSignatureクラスにExtractImage(..)メソッドを導入しました。以下のコードスニペットは、PdfFileSignatureオブジェクトから画像を抽出する手順を示しています:

```csharp
public static void ExtractSignatureImage()
        {
            using (PdfFileSignature signature = new PdfFileSignature())
            {
                signature.BindPdf(_dataDir + "DigitallySign.pdf");

                if (signature.ContainsSignature())
                {
                    foreach (string sigName in signature.GetSignNames())
                    {
                        string outFile = _dataDir + "ExtractImages_out.jpg";
                        using (Stream imageStream = signature.ExtractImage(sigName))
                        {
                            if (imageStream != null)
                            {
                                imageStream.Position = 0;
                                using (FileStream fs = new FileStream(outFile, FileMode.OpenOrCreate))
                                {
                                    imageStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## 位置と理由を抑制する

Aspose.PDFの機能は、デジタル署名インスタンスの柔軟な設定を可能にします。[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)クラスはPDFファイルに署名する機能を提供します。Signメソッドの実装により、PDFに署名し、特定の署名オブジェクトをこのクラスに渡すことができます。Signメソッドには、出力デジタル署名をカスタマイズするための一連の属性が含まれています。結果の署名から特定のテキスト属性を抑制する必要がある場合は、それらを空にすることができます。以下のコードスニペットは、署名ブロックから位置と理由の2つの行を抑制する方法を示しています:

```csharp
public static void SupressLocationReason()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // 署名位置のための矩形を作成する
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // 署名の外観を設定する
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // 3つの署名タイプのいずれかを作成する
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
            // 出力PDFファイルを保存する
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## デジタルサインのカスタマイズ機能

Aspose.PDF for .NET はデジタルサインのカスタマイズ機能を提供します。クラス [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) の Sign メソッドは、快適に使用できるように6つのオーバーロードを実装しています。例えば、SignatureCustomAppearance クラスのインスタンスとそのプロパティ値だけで結果のサインを設定することができます。以下のコードスニペットは、PDF の出力デジタルサインから「Digitally signed by」というキャプションを非表示にする方法を示しています。

```csharp
  public static void CustomizationFeaturesForDigitalSign()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // 署名位置用の矩形を作成
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

            // 3つの署名タイプのいずれかを作成
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Times New Roman",
                DigitalSignedLabel = "Signed by:"
            };
            signature.CustomAppearance = signatureCustomAppearance;

            pdfSign.Sign(1, true, rect, signature);
            // 出力 PDF ファイルを保存
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## デジタル署名テキストの言語を変更する

Aspose.PDF for .NET API を使用すると、次の3種類の署名を使用して PDF ファイルに署名できます:

- PKCS#1
- PKCS#7
- PKCS#7

提供されている各署名には、利便性のために実装された設定プロパティのセットが含まれています（ローカリゼーション、日付時刻形式、フォントファミリーなど）。クラス [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) は対応する機能を提供します。次のコードスニペットは、デジタル署名テキストの言語を変更する方法を示しています:

```csharp
     public static void ChangeLanguageInDigitalSignText()
        {
            string inFile = _dataDir + "sample01.pdf";
            string outFile = _dataDir + "DigitallySign.pdf";

            using (Aspose.Pdf.Facades.PdfFileSignature pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
            {
                pdfSign.BindPdf(inFile);
                //署名位置のための矩形を作成
                System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

                //3種類の署名タイプのいずれかを作成
                PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021")
                {
                    Reason = "Pruebas Firma",
                    ContactInfo = "Contacto Pruebas",
                    Location = "Población (Provincia)",
                    Date = DateTime.Now
                };
                SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
                {
                    DateSignedAtLabel = "Fecha",
                    DigitalSignedLabel = "Digitalmente firmado por",
                    ReasonLabel = "Razón",
                    LocationLabel = "Localización",
                    FontFamilyName = "Arial",
                    FontSize = 10d,
                    Culture = System.Globalization.CultureInfo.InvariantCulture,
                    DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
                };
                pkcs.CustomAppearance = signatureCustomAppearance;
                // PDF ファイルに署名
                pdfSign.Sign(1, true, rect, pkcs);
                //出力 PDF ファイルを保存
                pdfSign.Save(outFile);
            }
        }
```
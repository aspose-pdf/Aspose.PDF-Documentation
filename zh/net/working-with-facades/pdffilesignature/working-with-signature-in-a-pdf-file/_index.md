---
title: 在PDF文件中使用签名
type: docs
weight: 40
url: zh/net/working-with-signature-in-a-pdf-file/
description: 本节解释如何使用PdfFileSignature类提取签名信息、从签名中提取图像、更改语言等。
lastmod: "2021-06-05"
draft: false
---

## 如何提取签名信息

Aspose.PDF for .NET 支持使用 PdfFileSignature 类对 PDF 文件进行数字签名。目前，也可以确定证书的有效性，但我们不能提取整个证书。可以提取的信息包括公钥、指纹和颁发者等。

为了提取签名信息，我们在 PdfFileSignature 类中引入了 ExtractCertificate(..) 方法。请查看以下代码片段，该代码演示了从 PdfFileSignature 对象中提取证书的步骤：

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

## 从签名字段提取图像 (PdfFileSignature)

Aspose.PDF for .NET 支持使用 PdfFileSignature 类对 PDF 文件进行数字签名，并且在签署文档时，您还可以为 SignatureAppearance 设置图像。现在该 API 还提供了提取签名信息以及与签名字段相关联的图像的功能。

为了提取签名信息，我们在 PdfFileSignature 类中引入了 ExtractImage(..) 方法。请查看以下代码片段，该代码片段演示了从 PdfFileSignature 对象中提取图像的步骤：

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

## 抑制位置和原因

Aspose.PDF 功能允许灵活配置数字签名实例。[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类提供了签署 PDF 文件的能力。Sign 方法的实现允许对 PDF 进行签名并将特定的签名对象传递给此类。Sign 方法包含一组用于自定义输出数字签名的属性。如果需要从结果签名中抑制某些文本属性，可以将它们留空。以下代码片段演示了如何从签名块中抑制位置和原因这两行：

```csharp
public static void SupressLocationReason()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for signature location
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Set signature appearance
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## 数字签名的自定义功能

Aspose.PDF for .NET 允许数字签名的自定义功能。[SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) 类的 Sign 方法实现了 6 个重载，以便您舒适地使用。例如，您可以通过 SignatureCustomAppearance 类实例及其属性值来配置结果签名。以下代码片段演示了如何从 PDF 的输出数字签名中隐藏“数字签名者”标题。

```csharp
  public static void CustomizationFeaturesForDigitalSign()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // 创建签名位置的矩形
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

            // 创建三种签名类型中的任意一种
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Times New Roman",
                DigitalSignedLabel = "Signed by:"
            };
            signature.CustomAppearance = signatureCustomAppearance;

            pdfSign.Sign(1, true, rect, signature);
            // 保存输出 PDF 文件
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## 更改数字签名文本中的语言

使用 Aspose.PDF for .NET API，您可以使用以下三种类型的签名之一对 PDF 文件进行签名：

- PKCS#1
- PKCS#7
- PKCS#7

每个提供的签名都包含一组为您的方便而实现的配置属性（本地化、日期时间格式、字体系列等）。类 [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) 提供了相应的功能。以下代码片段演示了如何更改数字签名文本中的语言：

```csharp
     public static void ChangeLanguageInDigitalSignText()
        {
            string inFile = _dataDir + "sample01.pdf";
            string outFile = _dataDir + "DigitallySign.pdf";

            using (Aspose.Pdf.Facades.PdfFileSignature pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
            {
                pdfSign.BindPdf(inFile);
                //create a rectangle for signature location
                System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

                //create any of the three signature types
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
                // sign the PDF file
                pdfSign.Sign(1, true, rect, pkcs);
                //save output PDF file
                pdfSign.Save(outFile);
            }
        }
```
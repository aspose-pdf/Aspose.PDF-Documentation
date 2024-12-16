---
title: 在PDF文件中使用签名
type: docs
weight: 40
url: /zh/java/working-with-signature-in-a-pdf-file/
description: 本节介绍如何使用PdfFileSignature类在PDF文件中处理签名。
lastmod: "2021-06-05"
draft: false
---

## 如何提取签名信息

Aspose.PDF for Java支持使用PdfFileSignature类对PDF文件进行数字签名。目前，可以确定证书的有效性，但我们不能提取整个证书。可以提取的信息包括公钥、指纹和发行者等。

为了提取签名信息，我们在PdfFileSignature类中引入了extractCertificate(..)方法。请查看以下代码片段，演示了从PdfFileSignature对象中提取证书的步骤：

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


## 从签名字段提取图像 (PdfFileSignature)

Aspose.PDF for Java 支持使用 PdfFileSignature 类对 PDF 文件进行数字签名，并且在签署文档时，您还可以为 SignatureAppearance 设置图像。现在该 API 还提供了提取签名信息以及与签名字段关联的图像的功能。

为了提取签名信息，我们在 PdfFileSignature 类中引入了 [extractImage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#extractImage-java.lang.String-) 方法。请查看以下代码片段，该代码演示了从 PdfFileSignature 对象中提取图像的步骤：

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


## 隐藏位置和原因

Aspose.PDF 功能允许对数字签名实例进行灵活配置。[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 类提供了签署 PDF 文件的能力。Sign 方法的实现允许对 PDF 进行签名，并将特定的签名对象传递给此类。Sign 方法包含一组用于自定义输出数字签名的属性。如果您需要从结果签名中隐藏某些文本属性，可以将它们留空。以下代码片段演示了如何从签名块中隐藏“位置”和“原因”两行：

```java
public static void SupressLocationReason() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // 创建一个矩形用于签名位置
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // 设置签名外观
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // 创建三种签名类型中的任意一种
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "", "test01@aspose-pdf-demo.local", "", true, rect, signature);
        // 保存输出 PDF 文件
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## 数字签名的自定义功能

Aspose.PDF for Java 允许对数字签名进行自定义。SignatureCustomAppearance 类的 Sign 方法实现了 6 种重载，以便您舒适使用。例如，您可以仅通过 SignatureCustomAppearance 类实例及其属性值来配置结果签名。以下代码片段演示了如何隐藏 PDF 输出数字签名中的 "Digitally signed by" 标题。

```java
    public static void CustomizationFeaturesForDigitalSign() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // 为签名位置创建一个矩形
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // 创建三种签名类型中的任意一种
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setFontSize(6);
        signatureCustomAppearance.setFontFamilyName("Times New Roman");
        signatureCustomAppearance.setDigitalSignedLabel("SIGNED BY:");
        signature.setCustomAppearance(signatureCustomAppearance);

        pdfSign.sign(1, true, rect, signature);
        // 保存输出 PDF 文件
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## 更改数字签名文本的语言

使用 Aspose.PDF for Java API，您可以使用以下三种类型的签名之一来签署 PDF 文件：

- PKCS#1
- PKCS#7
- PKCS#7

每种提供的签名都包含一组配置属性，为您的便捷使用而实现（本地化、日期时间格式、字体系列等）。类 SignatureCustomAppearance 提供了相应的功能。以下代码片段演示了如何更改数字签名文本的语言：

```java
     public static void ChangeLanguageInDigitalSignText() {
        String inFile = _dataDir + "sample01.pdf";
        String outFile = _dataDir + "DigitallySign.pdf";

        PdfFileSignature pdfSign = new PdfFileSignature();

        pdfSign.bindPdf(inFile);
        // 为签名位置创建一个矩形
        java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);

        // 创建三种签名类型之一
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
        // 签署 PDF 文件
        pdfSign.sign(1, true, rect, pkcs);
        // 保存输出的 PDF 文件
        pdfSign.save(outFile);
    }
```
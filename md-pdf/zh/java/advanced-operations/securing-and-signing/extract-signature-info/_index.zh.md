---
title: 提取图像和签名信息
linktitle: 提取图像和签名信息
type: docs
weight: 30
url: /java/extract-image-and-signature-information/
description: 您可以使用 Java 中的 SignatureField 类从签名字段中提取图像并提取签名信息。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从签名字段提取图像

Aspose.PDF for Java 支持使用 [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) 类对 PDF 文件进行数字签名，并且在对文档进行签名时，还可以为 SignatureAppearance 设置图像。现在，该 API 还提供了提取签名信息以及与签名字段相关联的图像的功能。

为了提取签名信息，我们在 [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) 类中引入了 [ExtractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) 方法。
 请查看以下代码片段，演示了从 SignatureField 对象中提取图像的步骤：

```java
public class ExampleExtractImageAndSignature {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void ExtractingImageFromSignatureField() {
        Document pdfDocument = new Document(_dataDir + "ExtractingImage.pdf");

        int i = 0;
        try {
            for (WidgetAnnotation field : pdfDocument.getForm()) {
                SignatureField sf = (SignatureField) field;
                if (sf != null) {
                    FileOutputStream output = new FileOutputStream(_dataDir + "im" + i + ".jpeg");
                    InputStream tempStream = sf.extractImage();
                    byte[] b = new byte[tempStream.available()];
                    tempStream.read(b);
                    output.write(b);
                    output.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (pdfDocument != null)
                pdfDocument.dispose();
        }

    }
```

### 替换签名图片

有时候您可能需要仅替换 PDF 文件中已存在签名字段的图片。为实现此需求，首先我们需要在 PDF 文件内搜索表单字段，识别签名字段，获取签名字段的尺寸（矩形尺寸），然后在相同尺寸上盖印图片。

## 提取签名信息

Aspose.PDF for Java 支持使用 [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) 类对 PDF 文件进行数字签名。目前，我们可以确定证书的有效性，但无法提取整个证书。可以提取的信息包括公钥、指纹、发行者等。

为了提取签名信息，我们在 [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) 类中引入了 [ExtractCertificate](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractCertificate--) 方法。
 请查看以下代码片段，其中演示了从 SignatureField 对象中提取证书的步骤：

```java
    public static void ExtractSignatureInformation() throws IOException {
        String input = _dataDir + "ExtractSignatureInfo.pdf";
        Document pdfDocument = new Document(input);

        for (WidgetAnnotation field : pdfDocument.getForm()) {
            SignatureField sf = (SignatureField) field;
            if (sf != null) {
                InputStream cerStream = sf.extractCertificate();
                if (cerStream != null) {

                    byte[] buffer = new byte[cerStream.available()];
                    cerStream.read(buffer);

                    File targetFile = new File(_dataDir+"targetFile.cer");
                    OutputStream outStream = new FileOutputStream(targetFile);
                    outStream.write(buffer);
                    outStream.close();
                }
            }
        }
    }
}
```
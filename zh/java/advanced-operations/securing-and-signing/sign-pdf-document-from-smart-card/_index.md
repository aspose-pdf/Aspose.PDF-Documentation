---
title: 使用 Java 从智能卡签署 PDF 文档
linktitle: 使用智能卡签署 PDF
type: docs
weight: 30
url: /java/sign-pdf-document-from-smart-card/
description: 查看 Aspose.PDF 中基于证书的 PDF 签名的当前 Java 示例覆盖范围。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 当前 Java 示例集中基于证书的 PDF 签名覆盖率
Abstract: 本页描述了 Java 文档源代码树中可用的签名示例的当前范围。该存储库包括使用 PFX 或 PKCS7 凭据的基于证书的 PDF 签名示例，但当前不包括用于 Java 的专用智能卡证书存储示例。
---
当前的 Java 存储库不包括 `facades/pdffilesignature` 下的专用源支持的智能卡签名示例，但以下工作流程显示了使用从本地证书存储中选择的证书对 PDF 进行签名的典型 API 模式。

## 从智能卡签署 PDF 文档

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 外观并绑定源 PDF 文档。
1. 检索本地证书并创建所需的 [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/)。
1. 配置视觉签名外观和目标[矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)。
1. 通过 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 将签名应用于 PDF 文档。
1. 保存更新的 PDF 文档。
1. 使用 `bindPdf(...)` 将加载的文档绑定到 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 外观。
1. 通过调用 `getLocalCertificate()` 检索代表智能卡凭据的本地证书。
1. 检查是否找到证书。如果不是，请保存未更改的输出文件并停止工作流程。
1. 从所选证书创建 [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/)。
1. 使用`setSignatureAppearance(...)` 设置视觉签名外观图像。
1. 使用目标页面、原因、联系人、位置、可见性标志、签名 [矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 和外部签名对象调用`sign(...)`。
1. 将签名的 PDF 保存到输出路径。

```java
public static void signWithSmartCard(Path inputFile, Path outputFile, Path pngFile) {
    try (Document document = new Document(inputFile.toString());
            PdfFileSignature pdfSignature = new PdfFileSignature()) {
        pdfSignature.bindPdf(document);
        X509Certificate2 selectedCertificate = getLocalCertificate();
        if (selectedCertificate == null) {
            System.out.println("Local certificate was not found.");
            document.save(outputFile.toString());
            return;
        }

        ExternalSignature externalSignature = new ExternalSignature(selectedCertificate, null);
        pdfSignature.setSignatureAppearance(pngFile.toString());
        pdfSignature.sign(1, "Reason", "Contact", "Location", true,
                new java.awt.Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature.save(outputFile.toString());
    }
}
```

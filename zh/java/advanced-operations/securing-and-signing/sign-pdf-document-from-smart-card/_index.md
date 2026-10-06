---
title: 在 Java 中使用智能卡签署 PDF 文档
linktitle: 使用智能卡进行 PDF 签署
type: docs
weight: 30
url: /zh/java/sign-pdf-document-from-smart-card/
description: 审查 Aspose.PDF 中基于证书的 PDF 签署的当前 Java 示例覆盖情况。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 当前 Java 示例集中基于证书的 PDF 签署覆盖情况
Abstract: 此页面描述了 Java 文档源代码树中可用的签署示例的当前范围。该仓库包含使用 PFX 或 PKCS7 凭证的基于证书的 PDF 签署示例，但目前未包含专用于 Java 的智能卡证书存储示例。
---
当前的 Java 仓库未在下面包含专用的基于源的智能卡签名示例 `facades/pdffilesignature`，但下面的工作流展示了使用从本地证书存储中选择的证书对 PDF 进行签名的典型 API 模式。

## 使用智能卡签署 PDF 文档

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建一个 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 外观并绑定源 PDF 文档。
1. 检索本地证书并创建所需的 [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/).
1. 配置可视签名外观和目标 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. 通过以下方式将签名应用于 PDF 文档 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. 保存更新后的 PDF 文档。
1. 将已加载的文档绑定到 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 带有外观的 `bindPdf(...)`.
1. 通过调用检索表示智能卡凭据的本地证书 `getLocalCertificate()`.
1. 检查是否找到证书。如果没有，保存未更改的输出文件并停止工作流。
1. 创建一个 [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) 从选定的证书中。
1. 设置可视签名外观图像为 `setSignatureAppearance(...)`.
1. 调用 `sign(...)` 带有目标页面、原因、联系人、位置、可见性标志、签名 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/),以及外部签名对象。
1. 将已签名的 PDF 保存到输出路径。

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

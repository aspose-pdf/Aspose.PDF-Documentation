---
title: 在 Python 中保护和签署 PDF 文件
linktitle: 在 PDF 中的保护和签署
type: docs
weight: 210
url: /zh/python-net/securing-and-signing/
description: 了解如何在 Python 中签署、加密、解密和保护 PDF 文件，包括数字签名、智能卡和文档权限。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中签署、加密、解密和保护 PDF 文档
Abstract: 本节解释如何使用 Aspose.PDF for Python via .NET 来保护和签署 PDF 文档。了解如何应用数字签名、使用智能卡和证书、提取签名信息，以及在 Python 中管理 PDF 加密、密码和访问权限。
---

本节解释如何使用 Python 库安全地对 PDF 文档应用数字签名。虽然电子签名和数字签名有时被交替使用，但它们并不相同。数字签名是由 [证书颁发机构](https://en.wikipedia.org/wiki/Certificate_authority), 提供一个可信的印章，保护文档免受篡改。相比之下，电子签名通常用于表示个人签署文件的意图，但没有相同级别的安全验证。

当您需要保护 PDF 内容、控制文档权限、验证信任或在 Python 工作流中应用基于证书的签名时，请使用这些指南。

## 已涵盖的安全和签名任务

Aspose.PDF 支持数字签名：

- PKCS1 与 RSA 签名算法和 SHA-1 摘要。
- PKCS7 使用 RSA 签名算法和 SHA-1 摘要。
- PKCS7 分离式使用 DSA、RSA 和 ECDSA 签名算法。支持的摘要算法取决于签名算法。
- 时间戳签名。

PKCS7 分离式的摘要算法：

- DSA - SHA-1。
- RSA - SHA-1、SHA-256、SHA-384、SHA-512。
- ECDSA - SHA-256，SHA-384，SHA-512，SHA3-256，SHA3-384，SHA3-512。

建议避免使用 SHA-1 摘要算法的数字签名，因为它不安全。

- [对 PDF 文件进行数字签名](/pdf/zh/python-net/digitally-sign-pdf-file/)
- [设置权限、加密和解密 PDF 文件](/pdf/zh/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [提取图像和签名信息](/pdf/zh/python-net/extract-image-and-signature-information/)
- [使用智能卡签署 PDF 文档](/pdf/zh/python-net/sign-pdf-document-from-smart-card/)

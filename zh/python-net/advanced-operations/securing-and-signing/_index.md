---
title: 在 Python 中对 PDF 进行安全加密和签名
linktitle: PDF 的安全加密与签名
type: docs
weight: 210
url: /zh/python-net/securing-and-signing/
description: 本章节描述了使用 Python 对 PDF 文档进行签名和安全加密的功能
lastmod: "2025-06-23"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 对 PDF 文档签名
Abstract: 本节 Aspose.PDF for Python via .NET 文档提供了关于以编程方式对 PDF 文档进行安全加密和签名的全面指南。内容涵盖密码保护、加密算法、应用和验证数字签名、证书处理以及文档权限等关键主题。开发人员将学习如何实现不同层级的安全措施，以保护敏感内容、确保文档完整性并符合监管标准。示例和 API 参考使得在 Python 应用程序中快速集成安全功能成为可能，从而轻松自信地保障 PDF 工作流的安全。
---

本节解释了如何使用 Python 库安全地对 PDF 文档应用数字签名。虽然“电子签名”和“数字签名”有时可以互换使用，但它们并不相同。数字签名由[证书颁发机构](https://en.wikipedia.org/wiki/Certificate_authority)提供支持，提供可信的印章以保护文档免受篡改。相对地，电子签名通常用于表示个人签署文档的意图，未具备同等的安全验证水平。

Aspose.PDF 支持数字签名：

- 使用 RSA 签名算法和 SHA-1 摘要的 PKCS1。
- 使用 RSA 签名算法和 SHA-1 摘要的 PKCS7。
- 使用 DSA、RSA 和 ECDSA 签名算法的 PKCS7 分离模式。支持的摘要算法取决于签名算法。
- 时间戳签名。

PKCS7 分离模式支持的摘要算法：

- DSA - SHA-1。
- RSA - SHA-1、SHA-256、SHA-384、SHA-512。
- ECDSA - SHA-256、SHA-384、SHA-512、SHA3-256、SHA3-384、SHA3-512。

建议避免使用 SHA-1 摘要算法的数字签名，因为其安全性不足。

- [数字签署 PDF 文件](/pdf/python-net/digitally-sign-pdf-file/)
- [设置权限、加密和解密 PDF 文件](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [提取图像和签名信息](/pdf/python-net/extract-image-and-signature-information/)
- [使用智能卡签署 PDF 文档](/pdf/python-net/sign-pdf-document-from-smart-card/)

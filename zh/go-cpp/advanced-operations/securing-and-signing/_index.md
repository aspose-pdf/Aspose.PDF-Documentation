---
title: 在 Go 中确保和签署 PDF
linktitle: 确保和签署 PDF
type: docs
weight: 50
url: /zh/go-cpp/securing-and-signing/
description: 本节描述了使用签名和在 Go 中保护 PDF 文档的功能
lastmod: "2026-07-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

本节提供了使用 Aspose.PDF for Go via C\u002B\u002B 处理受保护 PDF 文档的全面指南。它解释了如何使用密码保护 PDF 文件、管理访问权限，以及在 Go 应用程序中安全地打开或解锁加密文档。

本文逐步讲解常见的安全相关 PDF 任务，包括使用现代加密算法对 PDF 进行加密、解密受密码保护的文件，以及通过权限标志控制用户访问。您还将学习如何检查现有的权限设置，并使用所有者凭据打开受保护的文档以进行进一步处理。

您将学习如何创建 PDF 文档、使用基于 AES 的加密应用现代加密保护，并控制用户的功能，例如打印、编辑内容和填写表单。本文还演示了如何使用所有者凭据打开受密码保护的 PDF 并对其进行解密，以生成可用于进一步处理的无限制文档。

- [加密 PDF 文件](/pdf/zh/go-cpp/encrypt-pdf/)
- [解密 PDF 文件](/pdf/zh/go-cpp/decrypt-pdf/)
- [获取权限](/pdf/zh/go-cpp/get-permissions/)
- [设置权限](/pdf/zh/go-cpp/set_permissions/)
- [打开受密码保护的 PDF](/pdf/zh/go-cpp/open-password-protected-pdf/)

要完成“设置权限”和“获取权限”，请参考 PDF Permissions Reference 表。该表列出了可应用于 PDF 文档的可用权限标志，以控制最终用户的交互方式。

## PDF 权限参考

| **权限** | **描述** |
| :- | :- |
| 打印文档 | 允许打印 |
| 修改内容 | 允许修改内容（表单/注释除外） |
| ExtractContent | 允许复制/提取文本和图形 |
| ModifyTextAnnotations | 允许添加/修改文本注释 |
| FillForm | 允许填写交互式表单 |
| 提取带残障的内容 | 允许为可访问性提取内容 |
| 组装文档 | 允许插入/旋转/删除页面或更改结构 |
| 打印质量 | 允许高质量/忠实打印 |



---
title: 在 Rust 中对 PDF 进行安全性保护和签名
linktitle: PDF 的安全性保护和签名
type: docs
weight: 50
url: /zh/rust-cpp/securing-and-signing/
description: 本节描述了使用签名以及在 Rust 中对 PDF 文档进行安全保护的功能
lastmod: "2026-07-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

本节提供了使用 Aspose.PDF for Rust via C++ 处理受保护 PDF 文档的完整指南。它解释了如何使用密码保护 PDF 文件、管理访问权限，以及在 Rust 中安全地打开或解锁加密文档。

本文逐步演示了常见的安全相关 PDF 任务，包括使用现代加密算法对 PDF 进行加密、解密受密码保护的文件，以及通过权限标志控制用户访问。您还将学习如何检查现有的权限设置，并使用所有者凭据打开受保护的文档以进行进一步处理。

您将学习如何创建 PDF 文档，使用基于 AES 的加密实现现代加密保护，并控制用户的功能，如打印、编辑内容和填写表单。本文还演示了如何使用所有者凭据打开受密码保护的 PDF 并将其解密为可自由处理的无限制文档。

- [加密和 PDF 文件](/pdf/zh/rust-cpp/encrypt-pdf/)
- [解密 PDF 文件](/pdf/zh/rust-cpp/decrypt-pdf/)
- [获取权限](/pdf/zh/rust-cpp/get-permissions/)
- [设置权限](/pdf/zh/rust-cpp/set_permissions/)
- [打开受密码保护的 PDF](/pdf/zh/rust-cpp/open-password-protected-pdf/)

要完成设置权限和获取权限，请参考 PDF 权限参考表。该表列出了可应用于 PDF 文档的可用权限标志，以控制最终用户与其交互的方式。

## PDF 权限参考

| **权限** | **描述** |
| :- | :- |
| Permissions::PRINT_DOCUMENT | 允许打印 |
| Permissions::MODIFY_CONTENT | 允许修改内容（除表单/注释外） |
| Permissions::EXTRACT_CONTENT | 允许复制/提取文本和图形 |
| Permissions::MODIFY_TEXT_ANNOTATIONS | 允许添加/修改文本注释 |
| Permissions::FILL_FORM | 允许填写交互式表单 |
| Permissions::EXTRACT_CONTENT_WITH_DISABILITIES | 允许提取内容以供辅助功能使用 |
| Permissions::ASSEMBLE_DOCUMENT | 允许插入/旋转/删除页面或更改结构 |
| Permissions::PRINTING_QUALITY | 允许高质量/忠实打印 |

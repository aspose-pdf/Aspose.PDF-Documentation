---
title: 设置现有 PDF 文件的权限
linktitle: 设置现有 PDF 文件的权限
type: docs
weight: 40
url: /java/set-privileges/
description: 了解如何使用 PdfFileSecurity 外观在 Java 中设置 PDF 权限。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 管理 PDF 权限和访问控制
Abstract: 了解如何使用 Aspose.PDF for Java 控制 PDF 权限。 Java 示例集涵盖了无需密码应用权限、使用用户和所有者密码应用权限以及返回成功标志的尝试式权限更新工作流。
---
## 设置现有 PDF 文件的权限

当您需要更改用户对现有 PDF 的操作时，请使用此工作流程。

### 步骤

1. 创建一个 `PdfFileSecurity` 实例。
2. 使用 `bindPdf` 绑定源 PDF。
3. 创建 `DocumentPrivilege` 对象并配置允许的操作。
4. 调用适当的 `setPrivilege` 或 `trySetPrivilege` 重载。
5. 如果更新成功，保存结果，然后关闭该对象。

### Java 示例

```java
public static void setPdfPrivilegesWithoutPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.setPrivilege(privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void trySetPdfPrivilegesWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    if (fileSecurity.trySetPrivilege("user_password", "owner_password", privilege)) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Setting privileges failed. Check passwords or document state.");
    }
    fileSecurity.close();
}
```

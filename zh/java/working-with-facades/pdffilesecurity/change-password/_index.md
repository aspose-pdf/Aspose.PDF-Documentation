---
title: 更改PDF文件的密码
linktitle: 更改PDF文件的密码
type: docs
weight: 10
url: /java/change-password/
description: 了解如何使用 PdfFileSecurity 外观在 Java 中更改 PDF 密码。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中更新 PDF 用户和所有者密码
Abstract: 了解如何使用 Aspose.PDF for Java 更改 PDF 密码。 Java 示例集涵盖直接更改用户和所有者密码、在重置安全设置时更改密码以及返回成功标志的尝试式密码更改工作流程。
---
## 更改PDF文件的密码

当您需要在已受保护的 PDF 上轮换凭据时，请使用`PdfFileSecurity`。

### 步骤

1. 创建一个 `PdfFileSecurity` 实例。
2. 使用 `bindPdf` 绑定受保护的 PDF。
3. 调用适当的 `changePassword` 重载，具体取决于您是否还想重置权限和密钥大小。
4. 保存更新的文件并关闭安全对象。

### Java 示例

```java
public static void changeUserAndOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void changePasswordAndResetSecurity(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryChangePasswordWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryChangePassword("owner_password", "new_user_password", "new_owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Password change failed. Check owner password or document security.");
    }
    fileSecurity.close();
}
```

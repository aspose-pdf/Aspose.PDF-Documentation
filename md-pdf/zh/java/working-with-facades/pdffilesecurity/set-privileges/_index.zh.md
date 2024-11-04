---
title: 设置现有 PDF 文件的权限
type: docs
weight: 50
url: /java/set-privileges/
description: 本主题解释如何使用 PdfFileSecurity 类设置现有 PDF 文件的权限。
lastmod: "2021-06-05"
draft: false
---

## 设置现有 PDF 文件的权限 (facades)

要设置 PDF 文件的权限，需要创建一个 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) 类对象，并使用 binPdf 方法绑定输入 PDF。然后，您需要调用 setPrivilege 方法来设置权限。您可以使用 [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/DocumentPrivilege) 对象指定权限，然后将此对象传递给 setPrivilege 方法，并使用 save 方法保存输出 PDF。

以下代码片段展示了如何设置 PDF 文件的权限。

```java
public static void SetPrivilege1() {
        // 创建 DocumentPrivileges 对象
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // 创建 PdfFileSecurity 对象
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege(privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```


以下是指定密码的方法：

```java
 public static void SetPrivilege2() {
        // 创建 DocumentPrivileges 对象
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // 创建 PdfFileSecurity 对象
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege("", "P@ssw0rd", privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```
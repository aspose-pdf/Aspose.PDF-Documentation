---
title: 设置权限，加密和解密 PDF 文件 
linktitle: 加密和解密 PDF 文件
type: docs
weight: 20
url: /zh/java/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: 加密 pdf,密码保护 pdf,解密 pdf,java
description: 使用不同的加密类型和算法通过 Java 加密 PDF 文件。同时，使用所有者密码解密 PDF 文件。
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 在现有 PDF 文件上设置权限

要在 PDF 文件上设置权限，创建 DocumentPrivilege 类的对象，并指定您想要应用于文档的权限。
 一旦定义了权限，将此对象作为参数传递给 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-boolean-) 方法。以下代码片段向您展示如何设置 PDF 文件的权限。

```java
  public static void SetPrivilegesOnExistingPDF()
  {
   // 加载源 PDF 文件
   Document document = new Document(_dataDir + "input.pdf");

   // 实例化文档权限对象
   // 对所有权限应用限制
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // 仅允许屏幕阅读
   documentPrivilege.setAllowScreenReaders(true);
   // 使用用户和所有者密码加密文件。
   // 需要设置密码，这样当用户使用用户密码查看文件时，
   // 仅启用屏幕阅读选项
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // 保存更新后的文档
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## 使用不同的加密类型和算法加密 PDF 文件

您可以使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) 方法来加密 PDF 文件。您可以将用户密码、所有者密码和权限传递给 [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) 方法。此外，您可以传递 [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/CryptoAlgorithm) 枚举的任何值。此枚举提供了不同的加密算法和密钥大小的组合。您可以传递您选择的值。最后，使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) 方法保存加密的 PDF 文件。

>加密 PDF 文件时，请指定不同的用户密码和所有者密码。

以下代码片段向您展示如何加密PDF文件。

```java
public static void EncryptPDFFile() {
   // 加载源PDF文件
   Document document = new Document(_dataDir + "input.pdf");

   // 实例化文档权限对象
   // 对所有权限应用限制
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // 仅允许屏幕阅读
   documentPrivilege.setAllowScreenReaders(true);
   // 用用户和所有者密码加密文件
   // 需要设置密码，以便用户使用用户密码查看文件时
   // 仅启用屏幕阅读选项
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // 保存更新的文档
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## 使用所有者密码解密PDF文件

为了解密PDF文件，您首先需要创建一个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象，并使用所有者密码打开PDF。
 在此之后，您需要调用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) 对象的 [Decrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) 方法。最后，使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 Save 方法保存更新后的 PDF 文件。以下代码片段显示了如何解密 PDF 文件。

```java
public static void DecryptPDFFile() {
   // 打开文档
   Document document = new Document(_dataDir + "Decrypt.pdf", "password");
   // 解密 PDF
   document.decrypt();

   // 保存更新后的 PDF
   document.save(_dataDir + "Decrypt_out.pdf");
  }
```

## 更改 PDF 文件的密码

如果您想更改 PDF 文件的密码，首先需要使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象和所有者密码打开 PDF 文件。 之后，您需要调用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [ChangePasswords](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#changePasswords-java.lang.String-java.lang.String-java.lang.String-) 方法。您需要将当前的所有者密码与新的用户密码和新的所有者密码一起传递给此方法。最后，使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 Save 方法保存更新的 PDF 文件。

以下代码片段向您展示如何更改 PDF 文件的密码。

```java
public static void ChangePassword_PDF_File() {
   // 打开文档
   Document document = new Document(_dataDir+ "ChangePassword.pdf", "owner");
   // 更改密码
   document.changePasswords("owner", "newuser", "newowner");
   // 保存更新的 PDF
   document.save(_dataDir + "ChangePassword_out.pdf");
  }
```

## 如何 - 确定源 PDF 是否受密码保护

Aspose.PDF for Java 提供了处理 PDF 文档的强大功能。 当使用 com.aspose.pdf 包的 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开一个受密码保护的 PDF 文档时，我们需要将密码信息作为参数提供给 Document 构造函数，如果没有提供这条信息，将会生成一条错误信息。事实上，当尝试使用 Document 对象打开一个 PDF 文件时，构造函数正在尝试读取 PDF 文件的内容，如果没有提供正确的密码，将会生成一条错误信息（这是为了防止未经授权的访问文档）。

当处理加密的 PDF 文件时，您可能会遇到这样的情况：您有兴趣检测 PDF 是否有打开密码和/或编辑密码。 有时有些文档在打开时不需要密码信息，但需要信息才能编辑文件内容。因此，为了满足上述要求，com.aspose.pdf.facades 包下的 PdfFileInfo 类提供了一些方法，这些方法可以帮助确定所需的信息。

### 获取有关 PDF 文档安全性的信息

PdfFileInfo 包含三个方法来获取有关 PDF 文档安全性的信息。

1. getPasswordType() 方法返回 PasswordType 枚举值：
    1. PasswordType.None - 文档没有密码保护
    1. PasswordType.User - 文档是用用户（或文档打开）密码打开的
    1. PasswordType.Owner - 文档是用所有者（或权限，编辑）密码打开的
    1. PasswordType.Inaccessible - 文档受密码保护，但需要密码才能打开，而提供了无效的密码（或没有密码）。
1. hasOpenPassword() 方法用于确定打开输入文件时是否需要密码。
1. hasEditPassword() 方法用于确定编辑输入文件内容时是否需要密码。

### 从数组中确定正确的密码

有时需要从密码数组中确定正确的密码，并使用正确的密码打开文档。以下代码片段演示了遍历密码数组并尝试使用正确的密码打开文档的步骤。

```java
public static void DetermineCorrectPasswordFromArray() {
     // 加载源 PDF 文件
   PdfFileInfo info = new PdfFileInfo();
   info.bindPdf(_dataDir + "IsPasswordProtected.pdf");
   // 确定源 PDF 是否加密
   System.out.println("文件受密码保护 " + info.isEncrypted());
   String[] passwords = { "test", "test1", "test2", "test3", "sample" };
   for (int passwordcount = 0; passwordcount < passwords.length; passwordcount++)
   {
    try
    {
     Document doc = new Document(_dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
     if (doc.getPages().size() > 0)
      System.out.println("文档中的页数 = " + doc.getPages().size());
    }
    catch (InvalidPasswordException ex)
    {
     System.out.println("密码 = " + passwords[passwordcount] + " 是不正确的");
    }
   }
```
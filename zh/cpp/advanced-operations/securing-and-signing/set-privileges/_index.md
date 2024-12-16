---
title: 设置权限，使用C++加密和解密PDF文件
linktitle: 加密和解密PDF文件
type: docs
weight: 20
url: /zh/cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: 使用C++通过不同的加密类型和算法加密PDF文件。此外，使用所有者密码解密PDF文件。
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 在现有PDF文件上设置权限

要在现有PDF文件上设置权限，Aspose.PDF for C++使用[DocumentPrivilege](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.document_privilege/)类并指定要应用于文档的权限。一旦定义了权限，将此对象作为参数传递给[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象的[Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7)方法。

以下代码片段向您展示了如何设置PDF文件的权限。

```cpp
void SecuringAndSigning::SetPrivilegesOnExistingPDF() {
    // 用于路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 加载源PDF文件
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // 实例化文档权限对象

    // 对所有权限应用限制
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // 仅允许屏幕阅读
    documentPrivilege->set_AllowScreenReaders(true);

    // 使用用户和所有者密码加密文件。
    // 需要设置密码，以便用户使用用户密码查看文件时，

    // 仅启用屏幕阅读选项
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);

    // 保存更新的文档
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## 使用不同的加密类型和算法加密PDF文件

要加密PDF文件，请使用[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象的[Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7)方法来加密PDF文件。

以下代码片段向您展示如何加密 PDF 文件。

```cpp
void SecuringAndSigning::EncryptPDFFile() {
    // 路径名称的字符串。
    String _dataDir("C:\\Samples\\");

    // 加载源 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // 实例化文档权限对象
    // 对所有权限应用限制
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // 仅允许屏幕阅读
    documentPrivilege->set_AllowScreenReaders(true);
    // 使用用户和所有者密码加密文件。
    // 需要设置密码，以便当用户使用用户密码查看文件时，
    // 仅启用屏幕阅读选项
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
    // 保存更新的文档
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## 使用所有者密码解密 PDF 文件

为了解密 PDF 文件，您首先需要创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象并使用所有者密码打开 PDF。 在此之后，您需要调用 [Decrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9c26014465f4368edc6fc62b7ef3d76a) 方法。

```cpp
void SecuringAndSigning::DecryptPDFFile() {


// 路径名称的字符串。

String _dataDir("C:\\Samples\\");


// 打开文档

auto document = MakeObject<Document>(_dataDir + u"Decrypt.pdf", u"password");

// 解密 PDF

document->Decrypt();


// 保存更新后的 PDF

document->Save(_dataDir + u"Decrypt_out.pdf");
}
```

## 更改 PDF 文件的密码

由于您的 PDF 可能包含重要且机密的信息，因此它们必须保持安全。因此，您可能需要更改 PDF 文档的密码。

如果您想更改 PDF 文件的密码，首先需要使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象使用所有者密码打开 PDF 文件。在此之后，您需要调用 [ChangePasswords](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9952055c2ac0afea827ce400b5ec951d) 方法。

下面的代码片段向您展示了如何更改 PDF 文件的密码。
```cpp
void SecuringAndSigning::ChangePassword_PDF_File() {

// String for path name.

String _dataDir("C:\\Samples\\");


// Open document

auto document = MakeObject<Document>(_dataDir + u"ChangePassword.pdf", u"owner");

// Change password

document->ChangePasswords(u"owner", u"newuser", u"newowner");

// Save updated PDF

document->Save(_dataDir + u"ChangePassword_out.pdf");
}
```

## 如何确定源PDF是否受密码保护

使用用户密码加密的PDF文档没有密码无法打开。 我们最好在尝试打开文档之前确定文档是否受密码保护。有时有些文档在打开时不需要密码信息，但它们需要信息来编辑文件的内容。因此，为了满足上述要求，Aspose.PDF.Facades 下的 [PdfFileInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_info/) 类提供了可以帮助确定所需信息的属性。

### 获取有关 PDF 文档安全性的信息

PdfFileInfo 包含三个属性来获取有关 PDF 文档安全性的信息。

1. 属性 PasswordType 返回 PasswordType 枚举值：
   - PasswordType.None - 文档没有受密码保护
   - PasswordType.User - 文档是使用用户（或文档打开）密码打开的
   - PasswordType.Owner - 文档是使用所有者（或权限，编辑）密码打开的

   - PasswordType.Inaccessible - 文档受密码保护，但需要密码才能打开，而提供的是无效密码（或没有密码）。2. 布尔属性 HasOpenPassword - 用于确定打开输入文件时是否需要密码。
3. 布尔属性 HasEditPassword - 用于确定编辑输入文件内容时是否需要密码。

### 从数组中确定正确的密码

有时需要从密码数组中确定正确的密码，并使用正确的密码打开文档。以下代码片段演示了遍历密码数组并尝试使用正确的密码打开文档的步骤。

```cpp
void SecuringAndSigning::DetermineCorrectPasswordFromArray() {

// 路径名称的字符串。

String _dataDir("C:\\Samples\\");

// 加载源 PDF 文件

auto info = MakeObject<PdfFileInfo>(_dataDir + u"IsPasswordProtected.pdf");

// 确定源 PDF 是否加密

Console::WriteLine(u"文件受密码保护 {0}", info->get_IsEncrypted());

const int count = 5;

String passwords[count] = { u"test", u"test1", u"test2", u"owner", u"sample" };

for (int passwordcount = 0; passwordcount < count; passwordcount++)

{

try

{

auto document = MakeObject<Document>(_dataDir + u"IsPasswordProtected.pdf", passwords[passwordcount]);

auto pages = document->get_Pages()->get_Count();

if (pages > 0)

Console::WriteLine(u"文档中的页数 = {0}", pages);

}

catch (Aspose::Pdf::InvalidPasswordException ex)

{

Console::WriteLine(u"密码 = {0} 不正确", passwords[passwordcount]);

}

}

Console::WriteLine(u"测试完成");
}
```
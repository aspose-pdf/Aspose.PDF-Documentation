---
title: 设置 PDF 权限
type: docs
weight: 50
url: /zh/net/set-privileges/
description: 本主题解释了如何使用 PdfFileSecurity 类设置现有 PDF 文件的权限。
lastmod: "2021-06-05"
draft: false
---

## 设置现有 PDF 文件的权限

要设置 PDF 文件的权限，创建一个 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 对象并调用 SetPrivilege 方法。您可以使用 DocumentPrivilege 对象指定权限，然后将该对象传递给 SetPrivilege 方法。以下代码片段向您展示了如何设置 PDF 文件的权限。

```csharp
public static void SetPrivilege1()
 {
    // 创建 DocumentPrivileges 对象
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // 创建 PdfFileSecurity 对象
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

```csharp
 public static void SetPrivilege2()
 {
    // 创建 DocumentPrivileges 对象
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // 创建 PdfFileSecurity 对象
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

## 从 PDF 中移除扩展权限功能

PDF 文档支持扩展权限功能，使最终用户能够使用 Adobe Acrobat Reader 在表单字段中填写数据，然后保存填写的表单的副本。 然而，它确保 PDF 文件未被修改，如果对 PDF 的结构进行了任何修改，则扩展权限功能将丢失。当查看这样的文档时，会显示一条错误消息，指出扩展权限已被移除，因为文档已被修改。最近，我们收到一个需求，需要从 PDF 文档中移除扩展权限。

为了从 PDF 文件中移除扩展权限，PdfFileSignature 类中添加了一个名为 RemoveUsageRights() 的新方法。另一个名为 ContainsUsageRights() 的方法被添加用于确定源 PDF 是否包含扩展权限。

{{% alert color="primary" %}}
从 Aspose.PDF for .NET 9.5.0 开始，以下方法的名称已更新。请注意，之前的方法仍然在 API 中，但已被标记为过时并将被移除。因此，建议尝试使用更新的方法。

- IsContainSignature(.) 方法被重命名为 ContainsSignature(..)。

- IsCoversWholeDocument(..) 方法被重命名为 CoversWholeDocument(..)。{{% /alert %}}

以下代码显示了如何从文档中移除使用权限：

```csharp
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
string input = dataDir + "DigitallySign.pdf";
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(input);
    if (pdfSign.ContainsUsageRights())
    {
        pdfSign.RemoveUsageRights();
    }

    pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
}
```
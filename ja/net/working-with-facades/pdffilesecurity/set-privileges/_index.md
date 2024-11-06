---
title: PDFの権限を設定する
type: docs
weight: 50
url: ja/net/set-privileges/
description: このトピックでは、PdfFileSecurityクラスを使用して既存のPDFファイルに権限を設定する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルに権限を設定する

PDFファイルの権限を設定するには、[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity)オブジェクトを作成し、SetPrivilegeメソッドを呼び出します。DocumentPrivilegeオブジェクトを使用して権限を指定し、このオブジェクトをSetPrivilegeメソッドに渡すことができます。以下のコードスニペットは、PDFファイルの権限を設定する方法を示しています。

```csharp
public static void SetPrivilege1()
{
    // DocumentPrivilegesオブジェクトを作成
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // PdfFileSecurityオブジェクトを作成
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

以下のメソッドをパスワードを指定して参照してください:

```csharp
 public static void SetPrivilege2()
 {
    // DocumentPrivilegesオブジェクトを作成
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // PdfFileSecurityオブジェクトを作成
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

## PDFから拡張権限機能を削除する

PDFドキュメントは、Adobe Acrobat Readerを使用してフォームフィールドにデータを入力し、入力されたフォームのコピーを保存するために、拡張権限機能をサポートしています。 しかし、それはPDFファイルが変更されていないことを保証し、PDFの構造に変更が加えられると、拡張権限機能が失われます。そのようなドキュメントを表示すると、エラーメッセージが表示され、ドキュメントが変更されたため拡張権限が削除されたと述べられます。最近、PDFドキュメントから拡張権限を削除する必要が生じました。

PDFファイルから拡張権限を削除するために、PdfFileSignatureクラスに新しいメソッドRemoveUsageRights()が追加されました。ソースPDFに拡張権限が含まれているかどうかを判断するために、ContainsUsageRights()という別のメソッドが追加されました。

{{% alert color="primary" %}}
Aspose.PDF for .NET 9.5.0から、以下のメソッドの名前が更新されました。以前のメソッドはまだAPIにありますが、廃止予定としてマークされており、削除される予定です。したがって、更新されたメソッドを使用することをお勧めします。

- IsContainSignature(.)メソッドはContainsSignature(..)に名前が変更されました。

- IsCoversWholeDocument(..)メソッドはCoversWholeDocument(..)に名前が変更されました。{{% /alert %}}

次のコードは、ドキュメントから使用権を削除する方法を示しています:

```csharp
// ドキュメントディレクトリへのパス。
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
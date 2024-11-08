---
title: 既存のPDFファイルに権限を設定する
type: docs
weight: 50
url: /ja/java/set-privileges/
description: このトピックでは、PdfFileSecurityクラスを使用して既存のPDFファイルに権限を設定する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルに権限を設定する（ファサード）

PDFファイルの権限を設定するには、[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) クラスオブジェクトを作成し、binPdf メソッドを使用して入力PDFをバインドします。その後、setPrivilege メソッドを呼び出して権限を設定します。[DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/DocumentPrivilege) オブジェクトを使用して権限を指定し、このオブジェクトを setPrivilege メソッドに渡して、save メソッドを使用して出力PDFを保存します。

次のコードスニペットは、PDFファイルの権限を設定する方法を示しています。

```java
public static void SetPrivilege1() {
        // DocumentPrivilegesオブジェクトを作成
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // PdfFileSecurityオブジェクトを作成
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege(privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```


以下の方法でパスワードを指定します:

```java
 public static void SetPrivilege2() {
        // DocumentPrivilegesオブジェクトを作成
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // PdfFileSecurityオブジェクトを作成
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege("", "P@ssw0rd", privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```
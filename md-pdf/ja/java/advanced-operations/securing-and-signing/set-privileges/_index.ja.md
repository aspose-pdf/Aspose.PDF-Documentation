---
title: 権限を設定し、PDFファイルを暗号化および復号化する
linktitle: PDFファイルを暗号化および復号化する
type: docs
weight: 20
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: PDFを暗号化する,PDFをパスワード保護する,PDFを復号化する,Java
description: Javaを使用して異なる暗号化タイプとアルゴリズムでPDFファイルを暗号化します。また、オーナーパスワードを使用してPDFファイルを復号化します。
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 既存のPDFファイルに権限を設定する

PDFファイルに権限を設定するには、DocumentPrivilegeクラスのオブジェクトを作成し、ドキュメントに適用したい権利を指定します。

 特権が定義されたら、このオブジェクトを[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトの[Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-boolean-)メソッドに引数として渡します。次のコードスニペットは、PDFファイルの特権を設定する方法を示しています。

```java
  public static void SetPrivilegesOnExistingPDF()
  {
   // ソースPDFファイルを読み込む
   Document document = new Document(_dataDir + "input.pdf");

   // Document Privilegesオブジェクトをインスタンス化
   // すべての特権に制限を適用
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // 画面読み取りのみを許可
   documentPrivilege.setAllowScreenReaders(true);
   // ユーザーとオーナーのパスワードでファイルを暗号化する。
   // ユーザーパスワードでファイルを表示するときに、
   // 画面読み取りオプションのみが有効になるようにパスワードを設定する必要があります
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // 更新されたドキュメントを保存
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## 異なる暗号化タイプとアルゴリズムを使用してPDFファイルを暗号化する

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) メソッドを使用してPDFファイルを暗号化することができます。ユーザーパスワード、オーナーパスワード、および権限を [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) メソッドに渡すことができます。それに加えて、[CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/CryptoAlgorithm) 列挙型の任意の値を渡すことができます。この列挙型は、暗号化アルゴリズムとキーサイズの異なる組み合わせを提供します。お好きな値を渡すことができます。最後に、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) メソッドを使用して暗号化されたPDFファイルを保存します。

>PDFファイルを暗号化する際は、異なるユーザーとオーナーのパスワードを指定してください。

以下のコードスニペットは、PDFファイルを暗号化する方法を示しています。

```java
public static void EncryptPDFFile() {
   // ソースPDFファイルを読み込む
   Document document = new Document(_dataDir + "input.pdf");

   // Document Privilegesオブジェクトをインスタンス化する
   // すべての権限に制限を適用する
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // スクリーンリーディングのみを許可する
   documentPrivilege.setAllowScreenReaders(true);
   // ユーザーおよびオーナーパスワードでファイルを暗号化する。
   // ユーザーがユーザーパスワードでファイルを表示した場合、
   // スクリーンリーディングオプションのみが有効になるようにパスワードを設定する必要がある
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // 更新されたドキュメントを保存する
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## オーナーパスワードを使用してPDFファイルを復号化する

PDFファイルを復号化するには、まず[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトを作成し、オーナーパスワードを使用してPDFを開く必要があります。
 その後、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [Decrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) メソッドを呼び出す必要があります。最後に、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの Save メソッドを使用して更新されたPDFファイルを保存します。次のコードスニペットは、PDFファイルを復号化する方法を示しています。

```java
public static void DecryptPDFFile() {
   // ドキュメントを開く
   Document document = new Document(_dataDir + "Decrypt.pdf", "password");
   // PDFを復号化
   document.decrypt();

   // 更新されたPDFを保存
   document.save(_dataDir + "Decrypt_out.pdf");
  }
```

## PDFファイルのパスワードを変更する

PDFファイルのパスワードを変更したい場合は、まず[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトを使用してオーナーパスワードでPDFファイルを開く必要があります。 その後、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [ChangePasswords](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#changePasswords-java.lang.String-java.lang.String-java.lang.String-) メソッドを呼び出す必要があります。このメソッドには、現在のオーナーパスワードと新しいユーザーパスワード、新しいオーナーパスワードを渡す必要があります。最後に、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの Save メソッドを使用して、更新されたPDFファイルを保存します。

次のコードスニペットは、PDFファイルのパスワードを変更する方法を示しています。

```java
public static void ChangePassword_PDF_File() {
   // ドキュメントを開く
   Document document = new Document(_dataDir+ "ChangePassword.pdf", "owner");
   // パスワードを変更する
   document.changePasswords("owner", "newuser", "newowner");
   // 更新されたPDFを保存する
   document.save(_dataDir + "ChangePassword_out.pdf");
  }
```

## 方法 - ソースPDFがパスワードで保護されているかどうかを判断する

Aspose.PDF for Java は、PDFドキュメントを扱うための優れた機能を提供します。 When using [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class of com.aspose.pdf package to open a PDF document which is password protected, we need to provide the password information as an argument to Document constructor and in case this information is not provided, an error message is generated. In fact when trying to open a PDF file with Document object, the constructor is trying to read the contents of PDF file and in case correct password is not provided, an error message is generated (it happens to prevent unauthorised access of document)

```java
// com.aspose.pdfパッケージのDocumentクラスを使用して、パスワードで保護されたPDFドキュメントを開く場合、Documentコンストラクタへの引数としてパスワード情報を提供する必要があります。この情報が提供されない場合、エラーメッセージが生成されます。実際にDocumentオブジェクトでPDFファイルを開こうとすると、コンストラクタはPDFファイルの内容を読み取ろうとし、正しいパスワードが提供されない場合、エラーメッセージが生成されます（これはドキュメントへの不正アクセスを防ぐために発生します）。
```

When dealing with encrypted PDF files, you may come across the scenario where you would be interested to detect if a PDF has an open password and/or an edit password.

```java
// 暗号化されたPDFファイルを扱う場合、PDFにオープンパスワードや編集パスワードがあるかどうかを検出したい場合があります。
 時々、開く際にパスワード情報を必要としないドキュメントがありますが、ファイルの内容を編集するための情報が必要です。したがって、上記の要件を満たすために、com.aspose.pdf.facadesパッケージに存在するPdfFileInfoクラスは、必要な情報を特定するのに役立つメソッドを提供します。

### PDFドキュメントのセキュリティに関する情報を取得する

PdfFileInfoには、PDFドキュメントのセキュリティに関する情報を取得するための3つのメソッドがあります。

1. getPasswordType()メソッドは、PasswordType列挙値を返します：
    1. PasswordType.None - ドキュメントはパスワードで保護されていません
    1. PasswordType.User - ドキュメントはユーザー（またはドキュメントオープン）パスワードで開かれました
    1. PasswordType.Owner - ドキュメントはオーナー（または権限、編集）パスワードで開かれました
    1. PasswordType.Inaccessible - ドキュメントはパスワードで保護されていますが、開くためにはパスワードが必要であり、無効なパスワード（またはパスワードなし）が提供されました。
1. `hasOpenPassword()` メソッドは、入力ファイルを開く際にパスワードが必要かどうかを判断するために使用されます。
1. `hasEditPassword()` メソッドは、入力ファイルの内容を編集するためにパスワードが必要かどうかを判断するために使用されます。

### 配列から正しいパスワードを特定する

時々、パスワードの配列から正しいパスワードを特定し、その正しいパスワードでドキュメントを開く必要があります。次のコードスニペットは、パスワードの配列を反復処理し、正しいパスワードでドキュメントを開こうとする手順を示しています。

```java
public static void DetermineCorrectPasswordFromArray() {
    // ソースPDFファイルをロード
    PdfFileInfo info = new PdfFileInfo();
    info.bindPdf(_dataDir + "IsPasswordProtected.pdf");
    // ソースPDFが暗号化されているかどうかを判断
    System.out.println("ファイルはパスワード保護されています " + info.isEncrypted());
    String[] passwords = { "test", "test1", "test2", "test3", "sample" };
    for (int passwordcount = 0; passwordcount < passwords.length; passwordcount++)
    {
        try
        {
            Document doc = new Document(_dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
            if (doc.getPages().size() > 0)
                System.out.println("ドキュメントのページ数 = " + doc.getPages().size());
        }
        catch (InvalidPasswordException ex)
        {
            System.out.println("パスワード = " + passwords[passwordcount] + " は正しくありません");
        }
    }
```
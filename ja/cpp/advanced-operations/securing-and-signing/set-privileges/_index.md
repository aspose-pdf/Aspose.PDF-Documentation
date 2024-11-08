---
title: 特権を設定し、C++を使用してPDFファイルを暗号化および復号化する
linktitle: PDFファイルを暗号化および復号化する
type: docs
weight: 20
url: /ja/cpp/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: PDFを暗号化, PDFにパスワード保護, PDFを復号化, C++
description: C++を使用して異なる暗号化タイプとアルゴリズムでPDFファイルを暗号化します。また、オーナーパスワードを使用してPDFファイルを復号化します。
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 既存のPDFファイルに特権を設定する

既存のPDFファイルに特権を設定するには、Aspose.PDF for C++を使用して[DocumentPrivilege](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.document_privilege/)クラスを使用し、ドキュメントに適用したい権利を指定します。特権が定義されたら、このオブジェクトを[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトの[Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7)メソッドに引数として渡します。

次のコードスニペットは、PDFファイルの特権を設定する方法を示しています。

```cpp
void SecuringAndSigning::SetPrivilegesOnExistingPDF() {
    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");

    // ソースPDFファイルをロード
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Document Privilegesオブジェクトをインスタンス化

    // すべての権限に制限を適用
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // スクリーンリーダーの使用のみ許可
    documentPrivilege->set_AllowScreenReaders(true);

    // ユーザーおよびオーナーパスワードでファイルを暗号化
    // ユーザーパスワードでファイルを表示した際に、

    // スクリーンリーダーオプションのみが有効化されるようにパスワードを設定する必要があります
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);

    // 更新されたドキュメントを保存
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## 異なる暗号化タイプとアルゴリズムを使用してPDFファイルを暗号化する

PDFファイルの暗号化には、[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトの[Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7)メソッドを使用します。

以下のコードスニペットは、PDFファイルを暗号化する方法を示しています。

```cpp
void SecuringAndSigning::EncryptPDFFile() {
    // パス名用の文字列。
    String _dataDir("C:\\Samples\\");

    // ソースPDFファイルをロード
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Document Privilegesオブジェクトをインスタンス化
    // すべての特権に制限を適用
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // 画面読み取りのみ許可
    documentPrivilege->set_AllowScreenReaders(true);
    // ユーザーおよび所有者のパスワードでファイルを暗号化。
    // ユーザーがユーザーパスワードでファイルを表示したら、
    // 画面読み取りオプションのみが有効になるように
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
    // 更新されたドキュメントを保存
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## 所有者パスワードを使用してPDFファイルを復号化する

PDFファイルを復号化するには、まず[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトを作成し、所有者のパスワードを使用してPDFを開く必要があります。 その後、[Decrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9c26014465f4368edc6fc62b7ef3d76a) メソッドを呼び出す必要があります。

```cpp
void SecuringAndSigning::DecryptPDFFile() {


// パス名のための文字列。

String _dataDir("C:\\Samples\\");


// ドキュメントを開く

auto document = MakeObject<Document>(_dataDir + u"Decrypt.pdf", u"password");

// PDFを復号化

document->Decrypt();


// 更新されたPDFを保存

document->Save(_dataDir + u"Decrypt_out.pdf");
}
```

## PDFファイルのパスワードを変更する

PDFは重要で機密性のある情報を含んでいる可能性があるため、安全でなければなりません。そのため、PDFドキュメントのパスワードを変更する必要があるかもしれません。

PDFファイルのパスワードを変更したい場合は、まず[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトを使用してオーナーパスワードでPDFファイルを開く必要があります。その後、[ChangePasswords](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9952055c2ac0afea827ce400b5ec951d) メソッドを呼び出す必要があります。

次のコードスニペットは、PDFファイルのパスワードを変更する方法を示しています。
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

## 方法 - ソースPDFがパスワードで保護されているかどうかを判断する方法

ユーザーのパスワードで暗号化されたPDFドキュメントは、パスワードがないと開くことができません。 ドキュメントを開こうとする前に、パスワード保護されているかどうかを確認した方が良いでしょう。ドキュメントを開く際にパスワード情報が不要な場合もありますが、ファイルの内容を編集するために情報が必要な場合もあります。上記の要件を満たすために、Aspose.PDF.Facadesの下にある[PdfFileInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_info/)クラスは、必要な情報を判断するのに役立つプロパティを提供します。

### PDFドキュメントのセキュリティに関する情報を取得

PdfFileInfoには、PDFドキュメントのセキュリティ情報を取得するための3つのプロパティがあります。

1. プロパティPasswordTypeは、PasswordType列挙値を返します：
    - PasswordType.None - ドキュメントはパスワード保護されていない
    - PasswordType.User - ドキュメントはユーザー（またはドキュメントオープン）パスワードで開かれた
    - PasswordType.Owner - ドキュメントはオーナー（または権限、編集）パスワードで開かれた

    - PasswordType.Inaccessible - ドキュメントはパスワード保護されているが、無効なパスワード（またはパスワードなし）が提供されたために開くためのパスワードが必要です。2. ブールプロパティ HasOpenPassword - 入力ファイルを開く際にパスワードが必要かどうかを判定するために使用されます。
3. ブールプロパティ HasEditPassword - 入力ファイルの内容を編集するためにパスワードが必要かどうかを判定するために使用されます。

### 配列から正しいパスワードを判定する

時には、パスワードの配列から正しいパスワードを判定し、正しいパスワードでドキュメントを開く必要があります。以下のコードスニペットは、パスワードの配列を反復処理し、正しいパスワードでドキュメントを開こうとする手順を示しています。

```cpp
void SecuringAndSigning::DetermineCorrectPasswordFromArray() {


// パス名の文字列。

String _dataDir("C:\\Samples\\");


// ソースPDFファイルをロード

auto info = MakeObject<PdfFileInfo>(_dataDir + u"IsPasswordProtected.pdf");


// ソースPDFが暗号化されているかどうかを判定

Console::WriteLine(u"ファイルはパスワードで保護されています {0}", info->get_IsEncrypted());

const int count = 5;

String passwords[count] = { u"test", u"test1", u"test2", u"owner", u"sample" };


for (int passwordcount = 0; passwordcount < count; passwordcount++)

{


try


{



auto document = MakeObject<Document>(_dataDir + u"IsPasswordProtected.pdf", passwords[passwordcount]);



auto pages = document->get_Pages()->get_Count();



if (pages > 0)




Console::WriteLine(u"ドキュメントのページ数 = {0}", pages);


}


catch (Aspose::Pdf::InvalidPasswordException ex)


{



Console::WriteLine(u"パスワード = {0} は正しくありません", passwords[passwordcount]);


}

}

Console::WriteLine(u"テスト終了");
}
```
---
title: PDFドキュメントの暗号化、復号化、および権限の設定
type: docs
weight: 10
url: /ja/cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**既存のPDFファイルに権限を設定する**
既存のPDFドキュメントに権限を設定するには、**Document->Encrypt(...)** メソッドを使用します。このメソッドは **DocumentPrivilege** オブジェクトを受け取ります。**DocumentPrivilege** クラスは、PDFドキュメントにアクセスするためのさまざまな権限を設定するために使用されます。さらに、このクラスを使用するには次の4つの方法があります：

1. 定義済みの権限を直接使用する。
1. 定義済みの権限に基づき、特定の権限を変更する。
1. 定義済みの権限に基づき、特定のAdobe Professionalの権限の組み合わせを変更する。
1. 方法2と方法3を組み合わせる。

以下のコードスニペットは、ドキュメントの権限を設定する上記の4つの方法を示します：

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-SecurityAndSignatures-SetPrivileges-Priveleges.cpp" >}}
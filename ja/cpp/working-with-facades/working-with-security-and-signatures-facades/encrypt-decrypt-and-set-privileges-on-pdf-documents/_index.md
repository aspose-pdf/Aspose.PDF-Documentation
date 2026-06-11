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

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
// Load an existing PDF document
auto doc = MakeObject<Document>(L"..\\Data\\SecurityAndSignatures\\input.pdf");

// Way1: Using predefined privilege directly.
System::SharedPtr<Aspose::Pdf::Facades::DocumentPrivilege> privilege = Aspose::Pdf::Facades::DocumentPrivilege::get_Print();
doc->Encrypt(L"user", L"owner", privilege, CryptoAlgorithm::AESx128, false);
doc->Save(L"..\\Data\\SecurityAndSignatures\\SetPrivelegesWay1_out.pdf");

// Way2: Based on a predefined privilege and change some specifical permissions.
System::SharedPtr<Aspose::Pdf::Facades::DocumentPrivilege> privilege2 = Aspose::Pdf::Facades::DocumentPrivilege::get_AllowAll();
privilege->set_AllowPrint(false);
privilege->set_AllowModifyContents(false);
doc->Encrypt(L"user", L"owner", privilege2, CryptoAlgorithm::AESx128, false);
doc->Save(L"..\\Data\\SecurityAndSignatures\\SetPrivelegesWay2_out.pdf");

// Way3: Based on a predefined privilege and change some specifical Adobe Professional permissions combination.
System::SharedPtr<Aspose::Pdf::Facades::DocumentPrivilege> privilege3 = Aspose::Pdf::Facades::DocumentPrivilege::get_ForbidAll();
privilege->set_ChangeAllowLevel(1);
privilege->set_PrintAllowLevel(2);
doc->Encrypt(L"user", L"owner", privilege3, CryptoAlgorithm::AESx128, false);
doc->Save(L"..\\Data\\SecurityAndSignatures\\SetPrivelegesWay3_out.pdf");

// Way4: Mixes the way2 and way3
System::SharedPtr<Aspose::Pdf::Facades::DocumentPrivilege> privilege4 = Aspose::Pdf::Facades::DocumentPrivilege::get_ForbidAll();
privilege->set_ChangeAllowLevel(1);
privilege->set_AllowPrint(true);
doc->Encrypt(L"user", L"owner", privilege4, CryptoAlgorithm::AESx128, false);
doc->Save(L"..\\Data\\SecurityAndSignatures\\SetPrivelegesWay4_out.pdf");
```
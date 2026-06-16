---
title: Criptografar, Descriptografar e definir Privilégios em documentos PDF
type: docs
weight: 10
url: /pt/cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**Definir Privilégios em um Arquivo PDF Existente**
Para definir privilégios em um documento PDF existente, você pode usar o método **Document->Encrypt(...)**, que leva um objeto **DocumentPrivilege**. A classe **DocumentPrivilege** é usada para definir diferentes privilégios para acessar o documento PDF. Além disso, há 4 maneiras seguintes usando esta classe:

1. Usando privilégio predefinido diretamente.
1. Baseado em um privilégio predefinido e alterar algumas permissões específicas.
1. Baseado em um privilégio predefinido e alterar alguma combinação específica de permissões do Adobe Professional.
1. Mistura do modo 2 e modo 3.

O trecho de código a seguir demonstrará as 4 maneiras acima de definir privilégios de documento:





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
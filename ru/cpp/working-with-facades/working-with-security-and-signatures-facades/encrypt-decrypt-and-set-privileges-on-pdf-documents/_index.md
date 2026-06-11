---
title: Шифрование, дешифрование и установка привилегий на PDF документы
type: docs
weight: 10
url: /ru/cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**Установка привилегий на существующий PDF файл**
Для установки привилегий на существующий PDF документ, вы можете использовать метод **Document->Encrypt(...)**, который принимает объект **DocumentPrivilege**. Класс **DocumentPrivilege** используется для установки различных привилегий доступа к PDF документу. Кроме того, есть 4 следующих способа использования этого класса:

1. Использование заранее определенной привилегии напрямую.
1. Основано на заранее определенной привилегии с изменением некоторых конкретных разрешений.
1. Основано на заранее определенной привилегии с изменением некоторых конкретных комбинаций разрешений Adobe Professional.
1. Смешивает способ 2 и способ 3.

Следующий фрагмент кода продемонстрирует вышеупомянутые 4 способа установки привилегий документа:





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
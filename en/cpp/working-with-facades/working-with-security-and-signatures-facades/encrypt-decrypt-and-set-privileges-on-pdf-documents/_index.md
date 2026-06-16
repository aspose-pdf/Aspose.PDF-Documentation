---

title: Encrypt, Decrypt and set Privileges on PDF documents

linktitle: Encrypt, Decrypt and set Privileges on PDF documents

type: docs

weight: 10

url: /cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/

description: Find out how to encrypt, decrypt, and set security privileges on PDF documents using C++ and Aspose.PDF to protect sensitive content.

---



## <ins>**Set Privileges on an Existing PDF File**

In order to set privileges on an existing PDF document, you can use **Document->Encrypt(...)** method, which takes **DocumentPrivilege** object. A **DocumentPrivilege** class is used to set different privileges to access PDF document. Furthermore, there are 4 following ways using this class:



1. Using predefined privilege directly.

1. Based on a predefined privilege and change some specific permissions.

1. Based on a predefined privilege and change some specific Adobe Professional permissions combination.

1. Mixes the way 2 and way 3.



Following code snippet will demonstrate above 4 ways to set document privileges:

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

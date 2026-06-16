---
title: Encriptar, Desencriptar y establecer privilegios en documentos PDF
type: docs
weight: 10
url: /es/cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**Establecer privilegios en un archivo PDF existente**
Para establecer privilegios en un documento PDF existente, puedes usar el método **Document->Encrypt(...)**, que toma un objeto **DocumentPrivilege**. La clase **DocumentPrivilege** se utiliza para establecer diferentes privilegios para acceder al documento PDF. Además, hay 4 formas siguientes de usar esta clase:

1. Usando directamente privilegios predefinidos.
1. Basado en un privilegio predefinido y cambiar algunos permisos específicos.
1. Basado en un privilegio predefinido y cambiar alguna combinación específica de permisos de Adobe Professional.
1. Mezcla de las formas 2 y 3.

El siguiente fragmento de código demostrará las 4 formas mencionadas para establecer privilegios en documentos:





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
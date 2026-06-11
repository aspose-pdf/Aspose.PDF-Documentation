---
title: Enkripsi, Dekripsi, dan Atur Hak Istimewa pada Dokumen PDF
type: docs
weight: 10
url: /id/cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**Atur Hak Istimewa pada File PDF yang Ada**
Untuk mengatur hak istimewa pada dokumen PDF yang ada, Anda dapat menggunakan metode **Document->Encrypt(...)**, yang mengambil objek **DocumentPrivilege**. Kelas **DocumentPrivilege** digunakan untuk mengatur berbagai hak istimewa untuk mengakses dokumen PDF. Selanjutnya, ada 4 cara berikut menggunakan kelas ini:

1. Menggunakan hak istimewa yang telah ditentukan langsung.
1. Berdasarkan hak istimewa yang telah ditentukan dan mengubah beberapa izin spesifik.
1. Berdasarkan hak istimewa yang telah ditentukan dan mengubah beberapa kombinasi izin Adobe Professional spesifik.
1. Menggabungkan cara 2 dan cara 3.

Cuplikan kode berikut akan menunjukkan 4 cara di atas untuk mengatur hak istimewa dokumen:
```

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
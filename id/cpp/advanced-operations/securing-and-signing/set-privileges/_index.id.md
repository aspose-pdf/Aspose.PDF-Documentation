---
title: Atur Hak Istimewa, Enkripsi dan Dekripsi File PDF menggunakan C++
linktitle: Enkripsi dan Dekripsi File PDF
type: docs
weight: 20
url: /cpp/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: enkripsi pdf, lindungi pdf dengan sandi, dekripsi pdf, c++
description: Enkripsi File PDF dengan C++ menggunakan Jenis dan Algoritma Enkripsi yang Berbeda. Juga, dekripsi File PDF menggunakan Sandi Pemilik.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Atur Hak Istimewa pada File PDF yang Ada

Untuk mengatur hak istimewa pada file PDF yang ada Aspose.PDF untuk C++ gunakan kelas [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.document_privilege/) dan tentukan hak yang ingin Anda terapkan pada dokumen. Setelah hak istimewa ditentukan, berikan objek ini sebagai argumen ke metode [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Cuplikan kode berikut menunjukkan cara mengatur hak istimewa file PDF.

```cpp
void SecuringAndSigning::SetPrivilegesOnExistingPDF() {
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // Memuat file PDF sumber
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Memperkenalkan objek Document Privileges

    // Terapkan pembatasan pada semua hak istimewa
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Hanya mengizinkan pembacaan layar
    documentPrivilege->set_AllowScreenReaders(true);

    // Enkripsi file dengan kata sandi Pengguna dan Pemilik.
    // Perlu mengatur kata sandi, sehingga setelah pengguna melihat file dengan kata sandi pengguna,

    // Hanya opsi pembacaan layar yang diaktifkan
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Enkripsi File PDF menggunakan Jenis Enkripsi dan Algoritma yang Berbeda

Untuk mengenkripsi file PDF gunakan metode [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) untuk mengenkripsi file PDF.


Cuplikan kode berikut menunjukkan cara mengenkripsi file PDF.

```cpp
void SecuringAndSigning::EncryptPDFFile() {
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // Memuat file PDF sumber
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Membuat objek Document Privileges
    // Menerapkan pembatasan pada semua hak istimewa
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Hanya mengizinkan pembacaan di layar
    documentPrivilege->set_AllowScreenReaders(true);
    // Mengenkripsi file dengan kata sandi Pengguna dan Pemilik.
    // Perlu mengatur kata sandi, sehingga setelah pengguna melihat file dengan
    // kata sandi pengguna,
    // Hanya opsi pembacaan layar yang diaktifkan
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
    // Menyimpan dokumen yang diperbarui
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## Mendekripsi File PDF menggunakan Kata Sandi Pemilik

Untuk mendekripsi file PDF, Anda perlu membuat objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dan membuka PDF menggunakan kata sandi pemilik. Setelah itu, Anda perlu memanggil metode [Decrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9c26014465f4368edc6fc62b7ef3d76a).

```cpp
void SecuringAndSigning::DecryptPDFFile() {


// String untuk nama path.

String _dataDir("C:\\Samples\\");


// Buka dokumen

auto document = MakeObject<Document>(_dataDir + u"Decrypt.pdf", u"password");

// Dekripsi PDF

document->Decrypt();


// Simpan PDF yang diperbarui

document->Save(_dataDir + u"Decrypt_out.pdf");
}
```

## Ubah Password dari File PDF

Karena PDF Anda dapat membawa informasi penting dan rahasia, mereka harus tetap aman. Oleh karena itu, Anda mungkin perlu mengubah password dokumen PDF Anda.

Jika Anda ingin mengubah password dari file PDF, Anda pertama-tama perlu membuka file PDF menggunakan password pemilik dengan objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Setelah itu, Anda perlu memanggil metode [ChangePasswords](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9952055c2ac0afea827ce400b5ec951d).

Kode berikut menunjukkan kepada Anda cara mengubah password dari file PDF.
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

## Cara - menentukan apakah sumber PDF dilindungi kata sandi

Dokumen PDF yang dienkripsi dengan kata sandi pengguna tidak dapat dibuka tanpa kata sandi. Kita sebaiknya menentukan apakah dokumen dilindungi kata sandi sebelum kita mencoba membukanya. Terkadang ada dokumen yang tidak memerlukan informasi kata sandi saat membukanya, tetapi mereka memerlukan informasi untuk mengedit isi file. Jadi untuk memenuhi persyaratan di atas, kelas [PdfFileInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_info/) yang terdapat di bawah Aspose.PDF.Facades menyediakan properti yang dapat membantu dalam menentukan informasi yang diperlukan.

### Mendapatkan informasi tentang keamanan dokumen PDF

PdfFileInfo berisi tiga properti untuk mendapatkan informasi tentang keamanan dokumen PDF.

1. properti PasswordType mengembalikan nilai enumerasi PasswordType:
   - PasswordType.None - dokumen tidak dilindungi kata sandi
   - PasswordType.User - dokumen dibuka dengan kata sandi pengguna (atau dokumen dibuka)
   - PasswordType.Owner - dokumen dibuka dengan kata sandi pemilik (atau izin, edit)

   - PasswordType.Inaccessible - dokumen dilindungi kata sandi tetapi kata sandi diperlukan untuk membukanya sementara kata sandi tidak valid (atau tidak ada kata sandi) disediakan.2. properti boolean HasOpenPassword - digunakan untuk menentukan apakah file input memerlukan kata sandi saat membukanya.
3. properti boolean HasEditPassword - digunakan untuk menentukan apakah file input memerlukan kata sandi untuk mengedit isinya.

### Menentukan kata sandi yang benar dari Array

Terkadang ada kebutuhan untuk menentukan kata sandi yang benar dari array kata sandi dan membuka dokumen dengan kata sandi yang benar. Cuplikan kode berikut menunjukkan langkah-langkah untuk mengiterasi melalui array kata sandi dan mencoba membuka dokumen dengan kata sandi yang benar.

```cpp
void SecuringAndSigning::DetermineCorrectPasswordFromArray() {


// String untuk nama path.

String _dataDir("C:\\Samples\\");


// Memuat file PDF sumber

auto info = MakeObject<PdfFileInfo>(_dataDir + u"IsPasswordProtected.pdf");


// Menentukan apakah PDF sumber terenkripsi

Console::WriteLine(u"File dilindungi kata sandi {0}", info->get_IsEncrypted());

const int count = 5;

String passwords[count] = { u"test", u"test1", u"test2", u"owner", u"sample" };


for (int passwordcount = 0; passwordcount < count; passwordcount++)

{


try


{



auto document = MakeObject<Document>(_dataDir + u"IsPasswordProtected.pdf", passwords[passwordcount]);



auto pages = document->get_Pages()->get_Count();



if (pages > 0)




Console::WriteLine(u"Jumlah Halaman dalam dokumen adalah = {0}", pages);


}


catch (Aspose::Pdf::InvalidPasswordException ex)


{



Console::WriteLine(u"Kata sandi = {0} tidak benar", passwords[passwordcount]);


}

}

Console::WriteLine(u"Tes selesai");
}
```
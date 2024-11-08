---
title: Setel Hak Istimewa, Enkripsi dan Dekripsi File PDF 
linktitle: Enkripsi dan Dekripsi File PDF
type: docs
weight: 20
url: /id/java/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: enkripsi pdf,melindungi pdf dengan kata sandi,dekripsi pdf,java
description: Enkripsi File PDF dengan Java menggunakan Jenis dan Algoritma Enkripsi yang Berbeda. Juga, dekripsi File PDF menggunakan Kata Sandi Pemilik.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Setel Hak Istimewa pada File PDF yang Ada

Untuk menyetel hak istimewa pada file PDF, buat objek dari kelas DocumentPrivilege dan tentukan hak yang ingin Anda terapkan pada dokumen.
 Setelah hak istimewa didefinisikan, berikan objek ini sebagai argumen ke metode [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-boolean-) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Cuplikan kode berikut menunjukkan cara mengatur hak istimewa dari file PDF.

```java
  public static void SetPrivilegesOnExistingPDF()
  {
   // Memuat file PDF sumber
   Document document = new Document(_dataDir + "input.pdf");

   // Memulai objek Hak Istimewa Dokumen
   // Terapkan pembatasan pada semua hak istimewa
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Hanya mengizinkan pembacaan layar
   documentPrivilege.setAllowScreenReaders(true);
   // Enkripsi file dengan password Pengguna dan Pemilik.
   // Perlu mengatur password, sehingga ketika pengguna melihat file dengan password pengguna,
   // Hanya opsi pembacaan layar yang diaktifkan
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Simpan dokumen yang diperbarui
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Enkripsi File PDF Menggunakan Jenis dan Algoritma Enkripsi yang Berbeda

Anda dapat menggunakan metode [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) untuk mengenkripsi file PDF. Anda dapat memasukkan kata sandi pengguna, kata sandi pemilik, dan izin ke metode [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-). Selain itu, Anda dapat memasukkan nilai apapun dari enum [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/CryptoAlgorithm). Enum ini menyediakan kombinasi yang berbeda dari algoritma enkripsi dan ukuran kunci. Anda dapat memasukkan nilai pilihan Anda. Akhirnya, simpan file PDF yang telah dienkripsi menggunakan metode [save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

>Silakan tentukan kata sandi pengguna dan pemilik yang berbeda saat mengenkripsi file PDF.

Berikut cuplikan kode menunjukkan cara mengenkripsi file PDF.

```java
public static void EncryptPDFFile() {
   // Memuat file PDF sumber
   Document document = new Document(_dataDir + "input.pdf");

   // Instansiasi objek Hak Istimewa Dokumen
   // Terapkan pembatasan pada semua hak istimewa
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // Hanya izinkan pembacaan layar
   documentPrivilege.setAllowScreenReaders(true);
   // Enkripsi file dengan kata sandi Pengguna dan Pemilik.
   // Perlu mengatur kata sandi, sehingga setelah pengguna melihat file dengan
   // kata sandi pengguna,
   // Hanya opsi pembacaan layar yang diaktifkan
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // Simpan dokumen yang diperbarui
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## Dekripsi File PDF menggunakan Kata Sandi Pemilik

Untuk mendekripsi file PDF, Anda perlu membuat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan membuka PDF menggunakan kata sandi pemilik.
 Setelah itu, Anda perlu memanggil metode [Decrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Terakhir, simpan file PDF yang diperbarui menggunakan metode Save dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Cuplikan kode berikut menunjukkan cara mendekripsi file PDF.

```java
public static void DecryptPDFFile() {
   // Buka dokumen
   Document document = new Document(_dataDir + "Decrypt.pdf", "password");
   // Dekripsi PDF
   document.decrypt();

   // Simpan PDF yang diperbarui
   document.save(_dataDir + "Decrypt_out.pdf");
  }
```

## Ubah Kata Sandi dari File PDF

Jika Anda ingin mengubah kata sandi dari file PDF, Anda perlu terlebih dahulu membuka file PDF menggunakan kata sandi pemilik dengan objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Setelah itu, Anda perlu memanggil metode [ChangePasswords](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#changePasswords-java.lang.String-java.lang.String-java.lang.String-) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Anda perlu memberikan password pemilik saat ini bersama dengan password pengguna baru dan password pemilik baru ke metode ini. Terakhir, simpan file PDF yang telah diperbarui menggunakan metode Save dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cuplikan kode berikut menunjukkan cara mengubah password file PDF.

```java
public static void ChangePassword_PDF_File() {
   // Buka dokumen
   Document document = new Document(_dataDir+ "ChangePassword.pdf", "owner");
   // Ubah password
   document.changePasswords("owner", "newuser", "newowner");
   // Simpan PDF yang diperbarui
   document.save(_dataDir + "ChangePassword_out.pdf");
  }
```

## Cara - menentukan apakah sumber PDF dilindungi password

Aspose.PDF untuk Java menyediakan kemampuan hebat dalam menangani dokumen PDF. Ketika menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dari paket com.aspose.pdf untuk membuka dokumen PDF yang dilindungi kata sandi, kita perlu memberikan informasi kata sandi sebagai argumen ke konstruktor Document dan jika informasi ini tidak diberikan, pesan kesalahan akan dihasilkan. Sebenarnya ketika mencoba membuka file PDF dengan objek Document, konstruktor mencoba membaca isi file PDF dan jika kata sandi yang benar tidak diberikan, pesan kesalahan akan dihasilkan (ini terjadi untuk mencegah akses dokumen yang tidak sah).

Saat berhadapan dengan file PDF yang dienkripsi, Anda mungkin menemukan skenario di mana Anda tertarik untuk mendeteksi apakah PDF memiliki kata sandi pembuka dan/atau kata sandi pengeditan. Terkadang ada dokumen yang tidak memerlukan informasi sandi saat membukanya, tetapi memerlukan informasi untuk mengedit isi file. Jadi, untuk memenuhi persyaratan di atas, kelas PdfFileInfo yang terdapat di bawah paket com.aspose.pdf.facades menyediakan metode yang dapat membantu dalam menentukan informasi yang diperlukan.

### Mendapatkan informasi tentang keamanan dokumen PDF

PdfFileInfo mengandung tiga metode untuk mendapatkan informasi tentang keamanan dokumen PDF.

1. Metode getPasswordType() mengembalikan nilai enumerasi PasswordType:
    1. PasswordType.None - dokumen tidak dilindungi sandi
    1. PasswordType.User - dokumen dibuka dengan sandi pengguna (atau sandi buka dokumen)
    1. PasswordType.Owner - dokumen dibuka dengan sandi pemilik (atau izin, edit)
    1. PasswordType.Inaccessible - dokumen dilindungi sandi tetapi sandi diperlukan untuk membukanya sementara sandi yang tidak valid (atau tanpa sandi) diberikan.
1. Metode hasOpenPassword() digunakan untuk menentukan apakah file input memerlukan kata sandi saat membukanya.
1. Metode hasEditPassword() digunakan untuk menentukan apakah file input memerlukan kata sandi untuk mengedit isinya.

### Menentukan kata sandi yang benar dari Array

Terkadang ada kebutuhan untuk menentukan kata sandi yang benar dari array kata sandi dan membuka dokumen dengan kata sandi yang benar. Cuplikan kode berikut menunjukkan langkah-langkah untuk mengiterasi melalui array kata sandi dan mencoba membuka dokumen dengan kata sandi yang benar.

```java
public static void DetermineCorrectPasswordFromArray() {
     // Muat file PDF sumber
   PdfFileInfo info = new PdfFileInfo();
   info.bindPdf(_dataDir + "IsPasswordProtected.pdf");
   // Tentukan apakah PDF sumber terenkripsi
   System.out.println("File dilindungi kata sandi " + info.isEncrypted());
   String[] passwords = { "test", "test1", "test2", "test3", "sample" };
   for (int passwordcount = 0; passwordcount < passwords.length; passwordcount++)
   {
    try
    {
     Document doc = new Document(_dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
     if (doc.getPages().size() > 0)
      System.out.println("Jumlah Halaman dalam dokumen adalah = " + doc.getPages().size());
    }
    catch (InvalidPasswordException ex)
    {
     System.out.println("Kata sandi = " + passwords[passwordcount] + " tidak benar");
    }
   }
```
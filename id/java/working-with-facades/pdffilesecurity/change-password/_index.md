---
title: Ubah Kata Sandi File PDF
linktitle: Ubah Kata Sandi File PDF
type: docs
weight: 10
url: /id/java/change-password/
description: Pelajari cara mengubah kata sandi PDF dalam Java dengan fasad PdfFileSecurity.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Perbarui kata sandi pengguna dan pemilik PDF dalam Java
Abstract: Pelajari cara mengubah kata sandi PDF dengan Aspose.PDF for Java. Set contoh Java mencakup mengubah kata sandi pengguna dan pemilik secara langsung, mengubah kata sandi sambil mereset pengaturan keamanan, dan alur kerja perubahan kata sandi gaya try yang mengembalikan flag keberhasilan.
---
## Ubah kata sandi file PDF

Gunakan `PdfFileSecurity` ketika Anda perlu memutar kredensial pada PDF yang sudah diamankan.

### Langkah

1. Buat sebuah `PdfFileSecurity` instansi.
2. Ikat PDF yang diamankan dengan `bindPdf`.
3. Panggil yang sesuai `changePassword` overload, tergantung pada apakah Anda juga ingin mengatur ulang hak istimewa dan ukuran kunci.
4. Simpan file yang telah diperbarui dan tutup objek keamanan.

### Contoh Java

```java
public static void changeUserAndOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void changePasswordAndResetSecurity(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryChangePasswordWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryChangePassword("owner_password", "new_user_password", "new_owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Password change failed. Check owner password or document security.");
    }
    fileSecurity.close();
}
```

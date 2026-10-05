---
title: "Mengatur hak istimewa pada file PDF yang ada"
linktitle: "Mengatur hak istimewa pada file PDF yang ada"
type: docs
weight: 40
url: /id/java/set-privileges/
description: "Pelajari cara mengatur hak istimewa PDF di Java dengan fasad PdfFileSecurity."
lastmod: "2026-09-30"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengelola izin PDF dan kontrol akses di Java"
Abstract: Pelajari cara mengontrol izin PDF dengan Aspose.PDF for Java. Set contoh Java mencakup penerapan hak istimewa tanpa kata sandi, penerapan hak istimewa dengan kata sandi pengguna dan pemilik, serta alur kerja pembaruan hak istimewa gaya try yang mengembalikan flag keberhasilan.
---
## Mengatur hak istimewa pada file PDF yang ada

Gunakan alur kerja ini ketika Anda perlu mengubah apa yang dapat dilakukan pengguna dengan PDF yang ada.

### Langkah

1. Buat sebuah instans `PdfFileSecurity`.
2. Gabungkan PDF sumber dengan `bindPdf`.
3. Buat sebuah objek `DocumentPrivilege` dan mengkonfigurasi tindakan yang diizinkan.
4. Panggil yang sesuai `setPrivilege` atau `trySetPrivilege` kelebihan beban.
5. Simpan hasilnya jika pembaruan berhasil, kemudian tutup objek.

### Contoh Java

```java
public static void setPdfPrivilegesWithoutPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.setPrivilege(privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void trySetPdfPrivilegesWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    if (fileSecurity.trySetPrivilege("user_password", "owner_password", privilege)) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Setting privileges failed. Check passwords or document state.");
    }
    fileSecurity.close();
}
```

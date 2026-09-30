---
title: "Mendekripsi file PDF"
linktitle: "Mendekripsi file PDF"
type: docs
weight: 20
url: /id/java/decrypt-pdf-file/
description: "Pelajari cara mendekripsi PDF di Java dengan fasad PdfFileSecurity."
lastmod: "2026-09-30"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menghapus pembatasan keamanan PDF dengan Java"
Abstract: Pelajari cara mendekripsi PDF dengan Aspose.PDF for Java. Set contoh Java mencakup dekripsi langsung dengan password pemilik dan alur kerja dekripsi gaya try yang memungkinkan Anda menangani kegagalan tanpa memunculkan pengecualian.
---
## Mendekripsi file PDF

Gunakan alur kerja ini ketika Anda memiliki password pemilik dan perlu menghapus keamanan dari PDF.

### Langkah

1. Buat instans `PdfFileSecurity`.
2. Gabungkan PDF terenkripsi dengan `bindPdf`.
3. Panggil `decryptFile` atau `tryDecryptFile` dengan kata sandi pemilik.
4. Simpan output jika dekripsi berhasil.
5. Tutup objek keamanan.

### Contoh Java

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```

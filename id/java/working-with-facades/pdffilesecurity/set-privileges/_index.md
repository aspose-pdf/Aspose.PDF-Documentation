---
title: Tetapkan Hak Istimewa pada File PDF yang Ada
type: docs
weight: 50
url: id/java/set-privileges/
description: Topik ini menjelaskan cara menetapkan hak istimewa pada file PDF yang ada menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Tetapkan Hak Istimewa pada File PDF yang Ada (facades)

Untuk menetapkan hak istimewa file PDF, buat objek kelas [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) dan ikat PDF input menggunakan metode binPdf. Kemudian Anda harus memanggil metode setPrivilege untuk menetapkan hak istimewa. Anda dapat menentukan hak istimewa menggunakan objek [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/DocumentPrivilege) dan kemudian mengoper objek ini ke metode setPrivilege dan menyimpan PDF keluaran menggunakan metode save.

Cuplikan kode berikut menunjukkan kepada Anda bagaimana menetapkan hak istimewa dari sebuah file PDF.

```java
public static void SetPrivilege1() {
        // Buat objek DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Buat objek PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege(privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```


Lihat metode berikut dengan menentukan kata sandi:

```java
 public static void SetPrivilege2() {
        // Membuat objek DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Membuat objek PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege("", "P@ssw0rd", privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```
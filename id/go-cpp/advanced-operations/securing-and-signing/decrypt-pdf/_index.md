---
title: Dekripsi PDF menggunakan Go
linktitle: Dekripsi File PDF
type: docs
weight: 40
url: /id/go-cpp/decrypt-pdf/
description: Dekripsi File PDF dengan Aspose.PDF for Go melalui C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Dekripsi File PDF menggunakan Kata Sandi Pemilik

Anda dapat membuka, mendekripsi, dan menyimpan dokumen PDF yang dilindungi kata sandi menggunakan Aspose.PDF for Go melalui C++. File PDF dibuka dengan kata sandi pemilik, didekripsi untuk menghapus semua pembatasan keamanan, dan kemudian disimpan sebagai dokumen baru yang tidak dilindungi.

1. Panggil [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) dan berikan nama file bersama dengan password pemilik untuk mengakses PDF yang terenkripsi.
1. Panggil [Decrypt](https://reference.aspose.com/pdf/go-cpp/security/decrypt/) metode untuk menghapus perlindungan password dan semua pembatasan keamanan yang terkait dari dokumen.
1. Simpan PDF yang telah didekripsi menggunakan [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // OpenWithPassword(filename string, password string) opens a password-protected PDF-document
        pdf, err := asposepdf.OpenWithPassword("sample_with_password.pdf", "ownerpass")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // Decrypt() decrypts PDF-document
        err = pdf.Decrypt()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_without_password.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```
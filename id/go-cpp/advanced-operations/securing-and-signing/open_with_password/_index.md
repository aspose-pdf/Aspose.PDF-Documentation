---
title: Buka PDF yang dilindungi kata sandi menggunakan Go
linktitle: Buka PDF yang dilindungi kata sandi
type: docs
weight: 70
url: /id/go-cpp/open-password-protected-pdf/
description: Buka File PDF yang dilindungi kata sandi dengan Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Buka dokumen PDF yang dilindungi kata sandi

Cuplikan kode ini menjelaskan cara membuka dokumen PDF yang dilindungi kata sandi menggunakan Aspose.PDF for Go via C++. Dokumen dibuka dengan password pemilik, yang memberikan akses penuh dan memungkinkan operasi lebih lanjut seperti membaca metadata, memeriksa izin, mendekripsi file, atau memodifikasi konten.

1. Buka dokumen PDF yang dilindungi.
1. Panggil [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) dan berikan nama file bersama dengan kata sandi pemilik untuk membuka kunci dokumen.
1. Gunakan 'defer pdf.Close()' untuk melepaskan semua sumber daya yang dialokasikan setelah pemrosesan selesai.
1. Setelah membuka dokumen, Anda dapat melanjutkan dengan tugas tambahan seperti mendekripsi PDF, mengubah izin, atau mengekstrak informasi.

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
        // working...
    }
```
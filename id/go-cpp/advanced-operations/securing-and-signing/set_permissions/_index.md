---
title: Atur izin untuk dokumen PDF menggunakan Go
linktitle: Atur izin
type: docs
weight: 80
url: /id/go-cpp/set_permissions/
description: Atur izin untuk dokumen PDF dengan Aspose.PDF untuk Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Atur izin akses untuk dokumen PDF

Sebuah dokumen PDF baru dibuat dan dilindungi dengan kata sandi pengguna dan pemilik, sementara izin tertentu—seperti mencetak, memodifikasi konten, dan mengisi formulir—diizinkan secara eksplisit. Dokumen kemudian disimpan dengan pembatasan izin ini diterapkan.

1. Buat dokumen PDF baru.
1. Panggil [SetPermissions](https://reference.aspose.com/pdf/go-cpp/security/setpermissions/) untuk melindungi dokumen.
1. Tentukan kata sandi pengguna untuk membatasi akses.
1. Tentukan kata sandi pemilik untuk mengendalikan pengaturan keamanan.
1. Definisikan operasi yang diizinkan menggunakan bitflag izin.
1. Simpan PDF dengan izin yang diterapkan menggunakan [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()

        // SetPermissions(userPassword, ownerPassword, permissions) sets permissions for PDF-document
        err = pdf.SetPermissions(
            "userpass",
            "ownerpass",
            asposepdf.PrintDocument|
                asposepdf.ModifyContent|
                asposepdf.FillForm,
        )
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_with_permissions.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```
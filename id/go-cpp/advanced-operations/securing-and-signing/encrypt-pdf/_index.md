---
title:  Enkripsi PDF menggunakan Go
linktitle: Enkripsi Berkas PDF
type: docs
weight: 10
url: /id/go-cpp/encrypt-pdf/
description: Enkripsi Berkas PDF dengan Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Enkripsi Berkas PDF menggunakan User atau Owner Password

Untuk mengenkripsi dokumen dengan mudah dan aman, Anda dapat menggunakan Aspose.PDF for Go via C++.

- **userPassword**, jika diatur, adalah apa yang perlu Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna memasukkan password pengguna. Jika tidak benar, dokumen tidak akan terbuka.
- Jika diatur, **ownerPassword** mengendalikan izin, seperti mencetak, mengedit, mengekstrak, mengomentari, dll. Acrobat/Reader akan melarang hal‑hal ini berdasarkan pengaturan izin. Acrobat akan meminta kata sandi ini jika Anda ingin mengatur/mengubah izin.

PDF dilindungi dengan kata sandi pengguna dan pemilik, dikonfigurasi dengan izin akses spesifik, dan dienkripsi menggunakan algoritma AES‑128 dengan keamanan yang kompatibel dengan PDF 2.0. Dokumen terenkripsi kemudian disimpan ke disk.

1. Buat dokumen PDF baru.
1. Enkripsi dokumen PDF dengan [encrypt](https://reference.aspose.com/pdf/go-cpp/security/encrypt/) metode.
1. Tentukan kata sandi pengguna untuk membatasi pembukaan dokumen.
1. Tentukan kata sandi pemilik untuk mengendalikan izin.
1. Definisikan tindakan yang diizinkan menggunakan bitflag izin.
1. Pilih AES-128 sebagai algoritma enkripsi.
1. Aktifkan enkripsi PDF 2.0 untuk kepatuhan keamanan modern.
1. Simpan dokumen yang diamankan menggunakan [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/), menulisnya ke file baru.

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
        // Encrypt(userPassword, ownerPassword, permissions, cryptoAlgorithm, usePdf20) encrypts PDF-document
        err = pdf.Encrypt(
            "userpass",
            "ownerpass",
            asposepdf.PrintDocument|asposepdf.ModifyContent|asposepdf.FillForm,
            asposepdf.AESx128,
            true,
        )
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_with_password.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```
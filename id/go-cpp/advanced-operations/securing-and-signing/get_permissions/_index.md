---
title: Dapatkan Izin menggunakan Go
linktitle: Dapatkan Izin
type: docs
weight: 60
url: /id/go-cpp/get-permissions/
description: Baca dan tampilkan izin akses dari dokumen PDF yang dilindungi password dengan Aspose.PDF untuk Go melalui C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Dapatkan izin dari dokumen PDF yang dilindungi password

Contoh ini menunjukkan cara mengambil, menginterpretasikan, dan menampilkan izin akses dari dokumen PDF yang dilindungi password dalam Go menggunakan Aspose.PDF untuk Go melalui C++.
PDF dibuka dengan kata sandi pemilik, flag izin‑nya dibaca, dan setiap izin yang diaktifkan diubah menjadi deskripsi yang dapat dibaca manusia sebelum dicetak ke konsol.

1. Tentukan pemetaan nama izin.
1. Ubah bendera izin menjadi teks yang dapat dibaca.
1. Gunakan [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) dengan kata sandi pemilik untuk mendapatkan akses ke informasi keamanan dokumen.
1. Pastikan pembersihan sumber daya yang tepat.
1. Panggil [GetPermissions](https://reference.aspose.com/pdf/go-cpp/security/getpermissions/) untuk mendapatkan flag bit izin saat ini yang ditetapkan pada PDF.
1. Tampilkan izin.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import (
        "fmt"
        "log"
        "strings"
    )

    var permissionNames = map[asposepdf.Permissions]string{
        asposepdf.PrintDocument:                  "Allow printing",
        asposepdf.ModifyContent:                  "Allow modifying content (except forms/annotations)",
        asposepdf.ExtractContent:                 "Allow copying/extracting text and graphics",
        asposepdf.ModifyTextAnnotations:          "Allow adding/modifying text annotations",
        asposepdf.FillForm:                       "Allow filling interactive forms",
        asposepdf.ExtractContentWithDisabilities: "Allow content extraction for accessibility",
        asposepdf.AssembleDocument:               "Allow inserting/rotating/deleting pages or changing structure",
        asposepdf.PrintingQuality:                "Allow high-quality / faithful printing",
    }

    func PermissionsToString(p asposepdf.Permissions) string {
        var result []string
        for flag, name := range permissionNames {
            if p&flag != 0 {
                result = append(result, name)
            }
        }
        if len(result) == 0 {
            return "None"
        }
        return strings.Join(result, ", ")
    }

    func main() {
        // OpenWithPassword(filename string, password string) opens a password-protected PDF-document
        pdf, err := asposepdf.OpenWithPassword("sample_with_permissions.pdf", "ownerpass")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // GetPermissions() gets current permissions of PDF-document
        permissions, err := pdf.GetPermissions()
        if err != nil {
            log.Fatal(err)
        }
        // Print permissions
        fmt.Println("Permissions:", PermissionsToString(permissions))
    }
```
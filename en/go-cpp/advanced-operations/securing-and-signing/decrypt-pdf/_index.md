---
title: Decrypt PDF using Go
linktitle: Decrypt PDF File
type: docs
weight: 40
url: /go-cpp/decrypt-pdf/
description: Decrypt PDF File with Aspose.PDF for Go via C++.
lastmod: "2026-01-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Decrypt PDF File using Owner Password

You can open, decrypt, and save a password-protected PDF document using the Aspose.PDF for Go via C++. The PDF file is opened with the owner password, decrypted to remove all security restrictions, and then saved as a new, unprotected document.

1. Call [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) and provide the file name along with the owner password to access the encrypted PDF.
1. Call the [Decrypt](https://reference.aspose.com/pdf/go-cpp/security/decrypt/) method to remove password protection and all associated security restrictions from the document.
1. Save the decrypted PDF using [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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
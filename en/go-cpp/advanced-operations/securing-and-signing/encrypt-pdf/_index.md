---
title:  Encrypt PDF using Go
linktitle: Encrypt PDF File
type: docs
weight: 10
url: /go-cpp/encrypt-pdf/
description: Encrypt PDF File with Aspose.PDF for Go via C++.
lastmod: "2026-01-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Encrypt PDF File using using User or Owner Password

If you are sending an email to someone with a PDF attachment that contains confidential  information, you might wish to add some security to it first to hold it falling into the incorrect hands. The best way to limit unauthorized access to a PDF document is to defend it with a password. To easily and securely encrypt documents, you can use Aspose.PDF for Go via C++.

- The **userPassword**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
- The **ownerPassword**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

The PDF is protected with user and owner passwords, configured with specific access permissions, and encrypted using the AES-128 algorithm with PDF 2.0–compatible security. The encrypted document is then saved to disk.

1. Create a new PDF document.
1. Encrypt the PDF document with [encrypt](https://reference.aspose.com/pdf/go-cpp/security/encrypt/) method.
1. Specify a user password to restrict opening the document.
1. Specify an owner password to control permissions.
1. Define allowed actions using a permissions bitmask.
1. Choose AES-128 as the encryption algorithm.
1. Enable PDF 2.0 encryption for modern security compliance.
1. Save the secured document using [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/), writing it to a new file.

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
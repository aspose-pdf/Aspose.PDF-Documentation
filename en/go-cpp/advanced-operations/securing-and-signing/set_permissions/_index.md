---
title: Set permissions for a PDF document using Go
linktitle: Set permissions
type: docs
weight: 80
url: /go-cpp/set_permissions/
description: Set permissions for a PDF document with Aspose.PDF for Go via C++.
lastmod: "2026-01-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Set access permissions for a PDF document

A new PDF document is created and protected with user and owner passwords, while specific permissions—such as printing, modifying content, and filling forms—are explicitly allowed. The document is then saved with these permission restrictions applied.

1. Create a new PDF document.
1. Call [SetPermissions](https://reference.aspose.com/pdf/go-cpp/security/setpermissions/) to protect the document.
1. Specify a user password to restrict access.
1. Specify an owner password to control security settings.
1. Define allowed operations using a permissions bitflag.
1. Save the PDF with permissions applied using [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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
---
title: Open a password-protected PDF using Go
linktitle: Open a password-protected PDF
type: docs
weight: 70
url: /go-cpp/open-password-protected-pdf/
description: Open a password-protected PDF File with Aspose.PDF for Go via C++.
lastmod: "2026-01-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Open a password-protected PDF document

This code snippet explains how to open a password-protected PDF document using Aspose.PDF for Go via C++. The document is opened with the owner password, which provides full access and allows further operations such as reading metadata, inspecting permissions, decrypting the file, or modifying content.

1. Open the protected PDF document.
1. Call [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) and provide the file name along with the owner password to unlock the document.
1. Use 'defer pdf.Close()' to release all allocated resources once processing is complete.
1. After opening the document, you can proceed with additional tasks such as decrypting the PDF, changing permissions, or extracting information.

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
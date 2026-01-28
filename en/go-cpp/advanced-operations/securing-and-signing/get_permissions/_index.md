---
title: Get Permissions using Go
linktitle: Get Permissions
type: docs
weight: 60
url: /go-cpp/get-permissions/
description: Read and display the access permissions of a password-protected PDF document with Aspose.PDF for Go via C++.
lastmod: "2026-01-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Get permissions of a password-protected PDF document

This example demonstrates how to retrieve, interpret, and display access permissions from a password-protected PDF document in Go using Aspose.PDF for Go via C++.
The PDF is opened with the owner password, its permission flags are read, and each enabled permission is converted into a human-readable description before being printed to the console.

1. Define permission name mappings.
1. Convert permission flags to readable text.
1. Use [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) with the owner password to gain access to the document's security information.
1. Ensure proper resource cleanup.
1. Call [GetPermissions](https://reference.aspose.com/pdf/go-cpp/security/getpermissions/) to obtain the current permission bitmask assigned to the PDF.
1. Display the permissions.

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
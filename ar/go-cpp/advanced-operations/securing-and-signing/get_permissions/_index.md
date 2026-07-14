---
title: الحصول على الصلاحيات باستخدام Go
linktitle: الحصول على الصلاحيات
type: docs
weight: 60
url: /ar/go-cpp/get-permissions/
description: قراءة وعرض صلاحيات الوصول لمستند PDF محمي بكلمة مرور باستخدام Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## الحصول على صلاحيات مستند PDF محمي بكلمة مرور

يوضح هذا المثال كيفية استرجاع وتفسير وعرض صلاحيات الوصول لمستند PDF محمي بكلمة مرور في Go باستخدام Aspose.PDF for Go via C++.
يتم فتح ملف PDF باستخدام كلمة مرور المالك، تُقرأ علامات الصلاحية الخاصة به، ويتم تحويل كل صلاحية مفعلة إلى وصف قابل للقراءة البشرية قبل طباعتها على وحدة التحكم.

1. تعريف تعيينات أسماء الأذونات.
1. تحويل إشارات الأذونات إلى نص قابل للقراءة.
1. استخدام [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) باستخدام كلمة مرور المالك للوصول إلى معلومات أمان المستند.
1. تأكد من تنظيف الموارد بشكل صحيح.
1. استدعاء [GetPermissions](https://reference.aspose.com/pdf/go-cpp/security/getpermissions/) للحصول على علم البت الخاص بالأذونات الحالي المعين لملف PDF.
1. عرض الأذونات.

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
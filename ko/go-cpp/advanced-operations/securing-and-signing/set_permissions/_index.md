---
title: Go를 사용하여 PDF 문서에 대한 권한 설정
linktitle: 권한 설정
type: docs
weight: 80
url: /ko/go-cpp/set_permissions/
description: C++를 통해 Go용 Aspose.PDF로 PDF 문서에 대한 권한을 설정합니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서에 대한 액세스 권한 설정

새 PDF 문서를 생성하고 사용자 및 소유자 암호로 보호하면서 인쇄, 내용 수정, 양식 채우기와 같은 특정 권한을 명시적으로 허용합니다. 그런 다음 문서를 이러한 권한 제한이 적용된 상태로 저장합니다.

1. 새 PDF 문서를 생성합니다.
1. 호출 [SetPermissions](https://reference.aspose.com/pdf/go-cpp/security/setpermissions/) 문서를 보호하기 위해.
1. 접근을 제한하기 위해 사용자 암호를 지정합니다.
1. 보안 설정을 제어하기 위해 소유자 암호를 지정합니다.
1. 권한 비트플래그를 사용하여 허용된 작업을 정의합니다.
1. 권한이 적용된 PDF를 저장하려면 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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
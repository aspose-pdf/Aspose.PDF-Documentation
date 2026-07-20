---
title: Go를 사용하여 권한 가져오기
linktitle: 권한 가져오기
type: docs
weight: 60
url: /ko/go-cpp/get-permissions/
description: C++를 통해 Aspose.PDF for Go를 사용하여 암호로 보호된 PDF 문서의 액세스 권한을 읽고 표시합니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 암호로 보호된 PDF 문서의 권한 얻기

이 예제는 C++를 통해 Aspose.PDF for Go를 사용하여 Go에서 암호로 보호된 PDF 문서의 액세스 권한을 검색, 해석 및 표시하는 방법을 보여줍니다.
PDF는 소유자 비밀번호로 열리며, 권한 플래그가 읽혀지고, 활성화된 각 권한은 사람이 읽을 수 있는 설명으로 변환된 후 콘솔에 출력됩니다.

1. 권한 이름 매핑을 정의합니다.
1. 권한 플래그를 읽을 수 있는 텍스트로 변환합니다.
1. 사용 [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) 소유자 비밀번호를 사용하여 문서의 보안 정보에 접근합니다.
1. 적절한 리소스 정리를 보장합니다.
1. 호출 [GetPermissions](https://reference.aspose.com/pdf/go-cpp/security/getpermissions/) PDF에 할당된 현재 권한 비트 플래그를 얻기 위해.
1. 권한을 표시합니다.

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
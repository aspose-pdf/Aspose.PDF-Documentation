---
title:  Go를 사용하여 PDF 암호화
linktitle: PDF 파일 암호화
type: docs
weight: 10
url: /ko/go-cpp/encrypt-pdf/
description: C++를 통해 Aspose.PDF for Go로 PDF 파일 암호화.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 사용자 또는 소유자 비밀번호를 사용하여 PDF 파일 암호화

문서를 쉽고 안전하게 암호화하려면 C++를 통해 Aspose.PDF for Go를 사용할 수 있습니다.

- **userPassword**가 설정된 경우, PDF를 열기 위해 제공해야 하는 값입니다. Acrobat/Reader는 사용자에게 사용자 비밀번호를 입력하라고 요청합니다. 비밀번호가 올바르지 않으면 문서가 열리지 않습니다.
- **ownerPassword**가 설정된 경우 인쇄, 편집, 추출, 주석 달기 등과 같은 권한을 제어합니다. Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. 권한을 설정하거나 변경하려면 Acrobat에서 이 비밀번호가 필요합니다.

PDF는 사용자 및 owner passwords로 보호되며, 특정 접근 권한이 설정되고 PDF 2.0 호환 보안으로 AES-128 알고리즘을 사용해 암호화됩니다. 암호화된 문서는 이후 디스크에 저장됩니다.

1. 새 PDF 문서를 생성합니다.
1. PDF 문서를 다음으로 암호화합니다. [encrypt](https://reference.aspose.com/pdf/go-cpp/security/encrypt/) 방법.
1. 문서를 열지 못하도록 사용자 비밀번호를 지정하십시오.
1. 권한을 제어하기 위해 소유자 비밀번호를 지정하십시오.
1. 권한 비트플래그를 사용하여 허용되는 작업을 정의하십시오.
1. 암호화 알고리즘으로 AES-128을 선택하십시오.
1. 현대 보안 준수를 위해 PDF 2.0 암호화를 활성화하십시오.
1. 보안이 적용된 문서를 저장하는 데 사용하십시오. [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/), 새 파일에 기록합니다.

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
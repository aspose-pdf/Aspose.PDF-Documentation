---
title: Go를 사용하여 PDF 복호화
linktitle: PDF 파일 복호화
type: docs
weight: 40
url: /ko/go-cpp/decrypt-pdf/
description: Aspose.PDF for Go via C++를 사용하여 PDF 파일을 복호화합니다.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 소유자 비밀번호를 사용하여 PDF 파일 복호화

Aspose.PDF for Go via C++를 사용하여 암호로 보호된 PDF 문서를 열고, 복호화하고, 저장할 수 있습니다. PDF 파일은 소유자 비밀번호로 열리며, 모든 보안 제한을 제거하도록 복호화된 후 새로운 비보호 문서로 저장됩니다.

1. 호출 [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) 암호화된 PDF에 접근하려면 파일 이름과 소유자 비밀번호를 함께 제공하십시오.
1. 다음 메서드를 호출하십시오 [Decrypt](https://reference.aspose.com/pdf/go-cpp/security/decrypt/) 문서에서 비밀번호 보호와 모든 관련 보안 제한을 제거하는 메서드.
1. 다음으로 복호화된 PDF를 저장하십시오 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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
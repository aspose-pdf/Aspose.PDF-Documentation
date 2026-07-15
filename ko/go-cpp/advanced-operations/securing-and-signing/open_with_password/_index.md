---
title: Go를 사용하여 비밀번호로 보호된 PDF 열기
linktitle: 비밀번호로 보호된 PDF 열기
type: docs
weight: 70
url: /ko/go-cpp/open-password-protected-pdf/
description: C++를 통해 Aspose.PDF for Go로 비밀번호로 보호된 PDF 파일 열기.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 비밀번호로 보호된 PDF 문서 열기

이 코드 스니펫은 C++를 통해 Aspose.PDF for Go를 사용하여 비밀번호로 보호된 PDF 문서를 여는 방법을 설명합니다. 문서는 소유자 비밀번호로 열리며, 이는 전체 접근 권한을 제공하고 메타데이터 읽기, 권한 검사, 파일 복호화 또는 내용 수정과 같은 추가 작업을 수행할 수 있게 합니다.

1. 보호된 PDF 문서를 엽니다.
1. 호출 [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) 파일 이름과 소유자 비밀번호를 제공하여 문서를 잠금 해제하십시오.
1. 처리가 완료되면 'defer pdf.Close()'를 사용하여 할당된 모든 리소스를 해제하십시오.
1. 문서를 연 후에는 PDF 복호화, 권한 변경 또는 정보 추출과 같은 추가 작업을 진행할 수 있습니다.

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
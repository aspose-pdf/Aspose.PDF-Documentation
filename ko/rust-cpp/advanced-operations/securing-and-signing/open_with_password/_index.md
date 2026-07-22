---
title: Rust를 사용하여 암호로 보호된 PDF 열기
linktitle: 암호로 보호된 PDF 열기
type: docs
weight: 70
url: /ko/rust-cpp/open-password-protected-pdf/
description: C++를 통해 Rust용 Aspose.PDF로 암호로 보호된 PDF 파일 열기.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 암호로 보호된 PDF 문서 열기

C++를 통해 Rust용 Aspose.PDF로 암호로 보호된 PDF 문서를 엽니다. 이 문서는 완전한 접근 권한을 부여하는 소유자 암호로 열리며, 메타데이터 읽기, 내용 수정, 권한 변경 또는 암호 제거와 같은 추가 작업을 수행할 수 있습니다.

1. 보호된 PDF 문서를 사용하여 열기 [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) 문서를 잠금 해제하기 위해 파일 경로와 소유자 비밀번호를 제공하십시오.
1. 열린 문서를 사용하십시오.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let _pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

        // working...

        Ok(())
    }
```
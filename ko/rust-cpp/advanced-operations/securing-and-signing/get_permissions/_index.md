---
title: Rust를 사용하여 권한 가져오기
linktitle: 권한 가져오기
type: docs
weight: 60
url: /ko/rust-cpp/get-permissions/
description: Aspose.PDF for Rust via C++를 사용하여 암호로 보호된 PDF 문서의 액세스 권한을 읽고 표시합니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 암호로 보호된 PDF 문서의 권한 가져오기

이 섹션에서는 Rust에서 암호로 보호된 PDF 문서의 액세스 권한을 읽고 표시하는 방법을 설명합니다.
PDF는 소유자 비밀번호로 열리며, 이는 문서의 보안 설정에 대한 전체 액세스를 부여합니다. 현재 할당된 권한이 검색된 후 콘솔에 출력됩니다.

1. 보호된 PDF 문서를 엽니다.
1. 호출 [get_permissions](https://reference.aspose.com/pdf/rust-cpp/security/get_permissions/) 허용된 작업을 정의하는 권한 플래그를 얻기 위해.
1. 검색된 권한을 콘솔에 출력합니다.

```rs

    use asposepdf::{Document, Permissions};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let pdf = Document::open_with_password("sample_with_permissions.pdf", "ownerpass")?;

        // Get current permissions of PDF-document
        let permissions: Permissions = pdf.get_permissions()?;

        // Print permissions
        println!("Permissions: {}", permissions);

        Ok(())
    }
```
---
title: Rust를 사용하여 PDF 문서에 권한 설정
linktitle: 권한 설정
type: docs
weight: 80
url: /ko/rust-cpp/set_permissions/
description: C++를 통해 Rust용 Aspose.PDF로 PDF 문서에 권한을 설정합니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서에 대한 액세스 권한 설정

새 PDF 문서를 생성하고 사용자 및 소유자 비밀번호로 보호하며, 특정 작업—인쇄, 내용 수정, 양식 작성—을 명시적으로 허용합니다. 그런 다음 정의된 권한 제한이 적용된 상태로 문서를 저장합니다.

1. 새 PDF 문서를 생성합니다.
1. 호출 [set_permissions](https://reference.aspose.com/pdf/rust-cpp/security/set_permissions/) 문서를 보호하기 위해.
1. 액세스를 제한하기 위해 사용자 비밀번호를 지정합니다.
1. 보안 설정을 제어하기 위해 소유자 비밀번호를 지정합니다.
1. 권한 비트 플래그를 사용하여 허용된 작업을 정의합니다.
1. 권한이 적용된 PDF를 저장 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

    use asposepdf::{Document, Permissions};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Set permissions for PDF-document.
        pdf.set_permissions(
            "userpass",  // User password
            "ownerpass", // Owner password
            Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
        )?;

        // Save the PDF-document with the updated permissions
        pdf.save_as("sample_with_permissions.pdf")?;

        Ok(())
    }
```
---
title: Rust를 사용하여 PDF 복호화
linktitle: PDF 파일 복호화
type: docs
weight: 40
url: /ko/rust-cpp/decrypt-pdf/
description: Aspose.PDF for Rust via C++로 PDF 파일 복호화.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 소유자 비밀번호를 사용하여 PDF 파일 복호화

Aspose.PDF for Rust via C++를 사용하여 암호로 보호된 PDF 문서를 열고, 복호화하고, 저장할 수 있습니다.
PDF는 소유자 비밀번호로 열리고, 모든 보안 제한을 제거하도록 복호화된 후, 새롭고 보호되지 않은 PDF로 저장됩니다.

1. 사용 [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) 파일 경로와 소유자 비밀번호를 제공하여 암호로 보호된 PDF를 로드합니다.
1. 다음 메서드를 호출합니다 [decrypt](https://reference.aspose.com/pdf/rust-cpp/security/decrypt/) 메서드는 문서의 암호 보호와 모든 관련 보안 제한을 제거합니다.
1. 복호화된 PDF를 사용하여 저장 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a password-protected PDF-document
      let pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

      // Decrypt PDF-document
      pdf.decrypt()?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_decrypt.pdf")?;

      Ok(())
  }
```
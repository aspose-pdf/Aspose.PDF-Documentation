---
title:  Rust를 사용하여 PDF 암호화
linktitle: PDF 파일 암호화
type: docs
weight: 10
url: /ko/rust-cpp/encrypt-pdf/
description: C++를 통해 Rust용 Aspose.PDF로 PDF 파일 암호화.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 사용자 또는 소유자 비밀번호를 사용하여 PDF 파일 암호화

문서를 쉽게 그리고 안전하게 암호화하려면 C++를 통해 Rust용 Aspose.PDF를 사용할 수 있습니다.

- **user_password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it’s not correct, the document will not open.
- **owner_password**가 설정된 경우 인쇄, 편집, 추출, 주석 달기 등과 같은 권한을 제어합니다. Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. 권한을 설정/변경하려면 Acrobat이 이 비밀번호를 요구합니다.

PDF는 사용자 비밀번호와 소유자 비밀번호, 특정 접근 권한, 그리고 PDF 2.0 표준을 준수하는 AES-128 암호화로 보호됩니다. 암호화가 완료되면 문서는 디스크에 저장되어 접근이 제어되고 PDF 파일이 안전하게 처리됩니다.

1. 새 PDF 문서를 생성합니다.
1. PDF 문서를 다음으로 암호화합니다 [암호화](https://reference.aspose.com/pdf/rust-cpp/security/encrypt/) 방법.
1. 문서를 여는 것을 제한하기 위해 사용자 비밀번호를 지정합니다.
1. 권한을 제어하기 위해 소유자 비밀번호를 지정합니다.
1. 권한 비트플래그를 사용하여 허용된 작업을 정의합니다.
1. 암호화 알고리즘으로 AES-128을 선택합니다.
1. 현대 보안 준수를 위해 PDF 2.0 암호화를 활성화합니다.
1. 암호화된 PDF를 사용하여 저장합니다. [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/). 

```rs

  use asposepdf::{CryptoAlgorithm, Document, Permissions};

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Create a new PDF-document
      let pdf = Document::new()?;

      // Encrypt PDF-document
      pdf.encrypt(
          "userpass",  // User password
          "ownerpass", // Owner password
          Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
          CryptoAlgorithm::AESx128, // Encryption algorithm
          true,                     // Use PDF 2.0 encryption
      )?;

      // Save the encrypted PDF-document
      pdf.save_as("sample_with_password.pdf")?;

      Ok(())
  }
```
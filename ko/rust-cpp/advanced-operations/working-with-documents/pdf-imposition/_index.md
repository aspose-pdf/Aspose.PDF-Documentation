---
title: C++를 통한 Rust용 Aspose.PDF를 사용한 PDF 배치
linktitle: PDF 배치
type: docs
weight: 30
url: /ko/rust-cpp/pdf-imposition/
description: 이 문서에서는 C++를 통한 Rust용 Aspose.PDF를 사용하여 인쇄에 최적화된 레이아웃을 위한 PDF 페이지 재배열 방법을 설명합니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 파일을 북릿이나 N-Up으로 만드는 방법
Abstract: C++를 통한 Rust용 Aspose.PDF는 인쇄 및 레이아웃 요구 사항을 충족하도록 PDF 문서를 재구성하기 위한 강력한 도구를 제공합니다. 이 문서에서는 표준 PDF를 북릿으로 변환하여 접었을 때 올바른 페이지 순서를 보장하는 방법과 여러 페이지를 하나의 시트로 결합한 N-Up PDF를 만드는 방법을 보여줍니다. 간결한 Rust 코드 예제를 사용하여 개발자는 문서화, 출판 및 보관 워크플로우를 위한 인쇄 준비가 된 PDF 변환을 빠르게 구현할 수 있습니다.
SoftwareApplication: rust-cpp
---

## PDF N-Up 만들기

N-Up PDF는 여러 원본 페이지를 단일 출력 페이지에 배치합니다. 이 예에서는 2 × 2 레이아웃을 사용하므로 원본 페이지 네 개가 출력 문서의 각 페이지에 결합됩니다.

1. 소스 PDF 문서를 엽니다.
1. 지정된 행과 열 수를 사용한 N-Up 레이아웃으로 문서를 저장합니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Convert and save the previously opened PDF-document as N-Up PDF-document
        pdf.save_n_up("sample_n_up.pdf", 2, 2)?;

        Ok(())
    }
```

## PDF 책자 만들기

Aspose.PDF for Rust via C++는 표준 PDF 문서를 소책자 스타일 PDF로 변환하는 방법을 설명합니다.
소책자 형식은 페이지를 재배열하여 인쇄 및 접었을 때 문서가 올바른 순서의 페이지로 구성된 적절한 소책자를 형성하도록 합니다.

1. 소스 PDF 문서를 엽니다.
1. 문서를 소책자 PDF로 저장합니다.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as booklet PDF-document
      pdf.save_booklet("sample_booklet.pdf")?;

      Ok(())
  }
```

**전체 기능을 사용하려면 무료 체험 라이선스가 필요합니다.**

4페이지 소책자 만들기의 결과를 탐색하십시오.

![4페이지 소책자 예시](sample_4.png)

3페이지 소책자 만들기의 결과를 탐색하십시오.

![3페이지 소책자 예시](sample_3.png)
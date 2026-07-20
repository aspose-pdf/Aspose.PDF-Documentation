---
title: Rust를 사용하여 PDF에 페이지 번호 추가
linktitle: 페이지 번호 추가
type: docs
weight: 10
url: /ko/rust-cpp/add-page-number/
description: 이 문서에서는 Aspose.PDF for Rust via C++를 사용하여 기존 PDF 문서에 페이지 번호를 추가하는 방법을 보여줍니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 페이지 번호 추가
Abstract: Aspose.PDF for Rust via C++는 개발자가 몇 줄의 코드만으로 기존 PDF 문서에 자동 페이지 번호를 추가하여 향상시킬 수 있게 합니다. 이 예제에서는 PDF 파일을 열고, 모든 페이지에 페이지 번호를 삽입한 다음, 업데이트된 문서를 새 파일로 저장하는 방법을 보여줍니다. 페이지 매김 자동화는 문서 구조의 일관성을 보장하며, 배포 또는 인쇄용으로 준비된 보고서, 계약서, 매뉴얼 및 기타 다중 페이지 출력물에 특히 유용합니다.
SoftwareApplication: rust-cpp
---

Aspose.PDF for Rust via C++는 PDF 문서를 프로그래밍 방식으로 수정할 수 있는 기본 기능을 제공합니다. 이 예제에서는 애플리케이션이 기존 PDF 파일을 열고, 모든 페이지에 자동 페이지 번호를 적용한 뒤, 수정된 문서를 새 이름으로 저장합니다.

이 접근 방식은 배포, 인쇄 또는 보관을 위한 최종 문서를 생성할 때 유용합니다. 이 프로세스는 몇 줄의 코드만 필요하며 명시적으로 덮어쓰지 않는 한 원본 파일을 변경하지 않습니다.

페이지 번호 매기는 보고서, 청구서, 계약서, 매뉴얼 및 기타 다중 페이지 문서에 대한 일반적인 요구 사항입니다. The [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) 메서드는 문서의 모든 페이지에 페이지 번호를 자동으로 삽입하여 파일 전체에 일관된 페이지 매김을 보장합니다.

페이지 번호를 추가한 후, 업데이트된 문서는 새 PDF 파일로 저장됩니다.

1. 기존 PDF 문서를 엽니다.
1. 페이지 번호를 추가하려면 [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) 방법.
1. 업데이트된 문서를 저장합니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add page number to a PDF-document
        pdf.add_page_num()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_page_num.pdf")?;

        Ok(())
    }
```
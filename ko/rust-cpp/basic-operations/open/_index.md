---
title: 프로그램을 통해 PDF 문서 열기
linktitle: PDF 열기
type: docs
weight: 20
url: /ko/rust-cpp/open-pdf-document/
description: Aspose.PDF for Rust via C++를 사용하여 PDF 파일을 여는 방법을 알아보세요.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust via C++를 사용하여 PDF 문서 열기
Abstract: Aspose.PDF for Rust via C++는 프로그램을 통해 PDF 문서를 열고 로드하는 강력한 기능을 제공하여 개발자가 PDF 내용을 손쉽게 액세스하고 조작할 수 있도록 합니다. 이 라이브러리는 파일 경로와 메모리 스트림과 같은 다양한 소스에서 PDF 파일을 여는 것을 지원하며, 효율적인 처리와 리소스 관리를 보장합니다. 문서 속성을 검사하고, 텍스트와 이미지를 추출하며, 로드된 PDF에 대해 기타 작업을 수행하는 기능을 제공합니다. 문서에는 자세한 안내와 코드 샘플이 포함되어 있어 개발자가 PDF 열기 기능을 애플리케이션에 원활하게 통합할 수 있도록 돕습니다.
SoftwareApplication: rust-cpp
---

## 기존 PDF 문서 열기

이 코드 스니펫은 Aspose.PDF for Rust를 사용하여 PDF 작업에 필요한 기본적인 작업을 보여줍니다. 여기에는 파일 열기, 변경 사항 저장, 리소스를 올바르게 닫는 것이 포함됩니다. 이는 PDF 문서를 다루는 개발자에게 기본적인 예제가 됩니다.

이 예시는 직관적이라 이해하고 수정하기 쉽습니다. 초보자에게 이상적이며 복잡한 애플리케이션을 위한 보일러플레이트로도 사용할 수 있습니다.

PDF 문서를 열고 저장하는 기능은 보고서 생성, 문서 수정, 자동화 워크플로우 구축 등 다양한 시나리오에서 핵심 요구사항입니다.

이 예시는 간단한 PDF 조작을 위한 API의 사용 편의성을 보여주며, 텍스트 추출, 주석 달기 또는 양식 채우기와 같은 고급 기능으로 확장할 수 있습니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document named "sample.pdf"
        let pdf = Document::open("sample.pdf")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_open.pdf")?;

        Ok(())
    }
```

---
title: Rust를 사용하여 PDF에 워터마크 추가
linktitle: 워터마크 추가
type: docs
weight: 80
url: /ko/rust-cpp/add-watermarks/
description: 이 예제는 Aspose.PDF for Rust via C++를 사용하여 PDF 문서에 사용자 정의 가능한 텍스트 워터마크를 추가하는 방법을 보여줍니다.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 텍스트 워터마크 추가
Abstract: Aspose.PDF for Rust via C++는 PDF 문서에 텍스트 워터마크를 추가하는 유연한 방법을 제공합니다. 이 예제는 텍스트 내용, 글꼴, 크기, 색상, 위치, 회전 각도, 레이어링 동작 및 투명도를 지정하여 사용자 정의 가능한 워터마크를 삽입하는 방법을 보여줍니다. 워터마크는 일반적으로 브랜딩, 기밀 라벨, 초안 표시 또는 문서 보호에 사용됩니다.
SoftwareApplication: rust-cpp
---

The [add_watermark](https://reference.aspose.com/pdf/rust-cpp/organize/add_watermark/) 이 메서드는 개발자가 기존 PDF 문서에 텍스트 워터마크를 프로그래밍 방식으로 적용할 수 있도록 합니다. 워터마크는 다음을 포함하여 완전히 사용자 정의할 수 있습니다:

- 워터마크 텍스트
- 글꼴 패밀리
- 글꼴 크기
- 텍스트 색상 (HEX 형식)
- X 및 Y 위치 좌표
- 회전 각도
- 전경 또는 배경 배치
- 불투명도(투명도 수준)

이 예제에서는 애플리케이션이 기존 PDF 파일을 열고, 반투명 회전 워터마크를 적용한 다음, 수정된 문서를 새 파일 이름으로 저장합니다.

이 기능은 문서를 초안, 기밀, 샘플 등으로 표시하거나 배포 전에 브랜드 요소를 추가하는 데 특히 유용합니다.

1. 기존 PDF 문서를 엽니다.
1. add_watermark 메서드를 호출하고 워터마크 속성을 구성합니다.
1. 업데이트된 문서를 저장합니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add watermark to PDF-document
        pdf.add_watermark(
            "WATERMARK",
            "Arial",
            16.0,
            "#010101",
            100,
            100,
            45,
            true,
            0.5,
        )?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_watermark.pdf")?;

        Ok(())
    }
```
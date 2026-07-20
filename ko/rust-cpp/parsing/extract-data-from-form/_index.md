---
title: Rust를 사용하여 AcroForm에서 데이터 추출
linktitle: AcroForm에서 데이터 추출
type: docs
weight: 50
url: /ko/rust-cpp/extract-data-from-acroform/
description: Aspose.PDF는 PDF 파일에서 양식 필드 데이터를 쉽게 추출할 수 있게 합니다. AcroForm에서 데이터를 추출하고 XML, FDF 또는 XFDF 형식으로 저장하는 방법을 알아보세요.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rust를 통해 AcroForm에서 데이터 추출하는 방법
Abstract: 이 문서는 Aspose.PDF for Rust via C++를 사용하여 PDF 파일에서 AcroForm 데이터를 추출하고 널리 사용되는 데이터 교환 형식인 XML, FDF 및 XFDF로 내보내는 방법을 설명합니다. 이 문서는 상호작용 형식 필드가 포함된 PDF 문서를 여는 방법과 프로그래밍 방식으로 형식 필드 이름과 값을 원본 PDF 외부에서 재사용하도록 내보내는 방법을 보여줍니다. 각 내보내기 형식에 대한 실용적인 Rust 예제를 제공함으로써, 이 문서는 데이터 처리, 양식 제출, 시스템 통합 및 장기 데이터 저장과 같은 일반적인 작업 흐름을 강조하고, 개발자가 애플리케이션에서 PDF 형식 데이터를 효율적으로 관리하고 재사용하도록 돕습니다.
---

## PDF 파일에서 XML로 데이터 내보내기

이 코드 스니펫은 Aspose.PDF for Rust를 사용하여 PDF 문서에서 AcroForm 데이터를 XML 파일로 내보내는 방법을 보여줍니다.
이 프로세스는 양식 필드가 있는 기존 PDF 파일을 열고, 해당 필드와 값을 XML 문서로 내보내어 추가 처리, 저장 또는 데이터 교환에 활용합니다.

1. PDF 문서를 엽니다.
1. 'export_xml' 메서드를 호출하여 양식 필드 데이터를 추출하고 XML 파일로 저장합니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XML-document
        pdf.export_xml("sample.xml")?;

        Ok(())
    }
```

## PDF 파일에서 FDF로 데이터 내보내기

Aspose.PDF for Rust via C++를 사용하면 PDF 문서에서 AcroForm 데이터를 FDF 파일로 내보낼 수 있습니다. Forms Data Format(FDF) 파일은 폼 필드 이름과 값을 PDF와 별도로 저장하므로, 데이터 교환, 폼 제출 워크플로, 원본 문서에 포함하지 않고 폼 데이터를 보관하는 데 유용합니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to FDF-document
        pdf.export_fdf("sample.fdf")?;

        Ok(())
    }
```

## PDF 파일에서 XFDF로 데이터 내보내기

XFDF(XML Forms Data Format)는 PDF 파일과 별도로 양식 필드 데이터를 나타내는 XML 기반 형식으로, 데이터 교환, 양식 제출 및 웹 기반 워크플로와의 통합에 적합합니다.
Aspose.PDF for Rust via C++는 PDF 문서에서 AcroForm 데이터를 XFDF 파일로 내보내는 데 도움을 줍니다.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XFDF-document
        pdf.export_xfdf("sample.xfdf")?;

        Ok(())
    }
```

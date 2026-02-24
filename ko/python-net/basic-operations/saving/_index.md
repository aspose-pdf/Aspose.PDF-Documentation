---
title: PDF 문서를 프로그래밍 방식으로 저장하기
linktitle: PDF 저장
type: docs
weight: 30
url: /ko/python-net/save-pdf-document/
description: Python용 Aspose.PDF for .NET 라이브러리를 사용하여 PDF 파일을 저장하는 방법을 배웁니다. PDF 문서를 파일 시스템, 스트림 및 웹 애플리케이션에 저장합니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서 저장
Abstract: 이 문서는 Python에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 저장하는 방법에 대한 안내를 제공합니다. PDF를 저장하는 주요 방법 세 가지—파일 시스템에 저장, 스트림에 저장, PDF/A 또는 PDF/X와 같은 특정 형식으로 저장—을 설명합니다. `Document` 클래스의 `save()` 메서드가 이러한 작업의 핵심입니다. 파일 시스템에 PDF를 저장하려면 문서를 새로 만들거나 페이지를 추가하는 등 조작한 뒤 직접 경로에 저장할 수 있습니다. 스트림에 저장할 경우 `Save` 메서드의 오버로드를 사용해 문서를 스트림 객체에 쓸 수 있습니다. 또한 이 문서는 장기 보관을 위한 PDF/A 및 그래픽 교환을 위한 PDF/X 형식으로 문서를 저장하는 방법을 설명합니다. 이 과정에서는 저장하기 전에 `convert` 메서드로 문서를 준비해야 합니다. 제공된 Python 코드 스니펫은 각 접근 방식을 시연하여 이러한 메서드의 실용적인 적용을 보여줍니다.
---

## 파일 시스템에 PDF 문서 저장

생성하거나 수정한 PDF 문서를 파일 시스템에 저장하려면 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드와 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스를 사용할 수 있습니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(output_pdf)
```

## 스트림에 PDF 문서 저장

또한 `Save` 메서드의 오버로드를 사용하여 생성하거나 수정한 PDF 문서를 스트림에 저장할 수 있습니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```

## PDF/A 또는 PDF/X 형식 저장

PDF/A는 전자 문서의 보관 및 장기 보존을 위해 사용되는 휴대용 문서 형식(PDF)의 ISO 표준화 버전입니다.
PDF/A는 장기 보관에 적합하지 않은 기능(예: 글꼴 연결(글꼴 포함이 아님) 및 암호화)을 허용하지 않음으로써 일반 PDF와 다릅니다. PDF/A 뷰어에 대한 ISO 요구 사항에는 색 관리 지침, 내장 글꼴 지원 및 내장된 주석을 읽을 수 있는 사용자 인터페이스가 포함됩니다.

PDF/X는 PDF ISO 표준의 하위 집합입니다. PDF/X의 목적은 그래픽 교환을 용이하게 하는 것이며, 따라서 일반 PDF 파일에는 적용되지 않는 일련의 인쇄 관련 요구 사항을 갖고 있습니다.

두 경우 모두 문서를 저장하려면 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하고, 문서를 저장하기 전에 [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드로 준비해야 합니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```


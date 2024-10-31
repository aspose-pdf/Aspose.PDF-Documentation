---
title: PDF 문서를 프로그래밍 방식으로 저장하기
linktitle: PDF 저장
type: docs
weight: 30
url: /python-net/save-pdf-document/
description: Python Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 파일을 저장하는 방법을 알아보세요. 파일 시스템, 스트림 및 웹 애플리케이션에 PDF 문서를 저장합니다.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서를 파일 시스템에 저장하기

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 클래스의 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 생성되거나 조작된 PDF 문서를 파일 시스템에 저장할 수 있습니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # 일부 조작 수행, 예: 새 빈 페이지 추가
    document.pages.add()
    document.save(output_pdf)
```

## PDF 문서를 스트림에 저장하기

`Save` 메서드의 오버로드를 사용하여 생성되거나 조작된 PDF 문서를 스트림에 저장할 수도 있습니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # 일부 조작 수행, 예: 새 빈 페이지 추가
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```


## PDF/A 또는 PDF/X 형식으로 저장하기

PDF/A는 전자 문서의 보관 및 장기 보존을 위해 사용되는 ISO 표준화된 휴대용 문서 형식(PDF)입니다. PDF/A는 폰트 연결(폰트 내장과는 반대) 및 암호화와 같이 장기 보관에 적합하지 않은 기능을 금지한다는 점에서 PDF와 다릅니다. PDF/A 뷰어에 대한 ISO 요구 사항에는 색상 관리 지침, 내장 폰트 지원 및 내장 주석을 읽기 위한 사용자 인터페이스가 포함됩니다.

PDF/X는 PDF ISO 표준의 하위 집합입니다. PDF/X의 목적은 그래픽 교환을 용이하게 하는 것이므로 표준 PDF 파일에는 적용되지 않는 일련의 인쇄 관련 요구 사항이 있습니다.

두 경우 모두 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 문서를 저장하며, 문서는 [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 준비해야 합니다.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```
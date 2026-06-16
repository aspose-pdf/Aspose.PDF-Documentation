---
title: 프로그래밍 방식으로 PDF 문서 저장
linktitle: PDF 저장
type: docs
weight: 30
url: /ko/python-net/save-pdf-document/
description: .NET 라이브러리를 통해 파이썬용 파이썬 Aspose.PDF 파일로 PDF 파일을 저장하는 방법을 알아보세요.PDF 문서를 파일 시스템, 스트리밍 및 웹 응용 프로그램에 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서 저장하기
Abstract: 이 문서에서는 Python에서 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 저장하는 방법에 대한 지침을 제공합니다.PDF를 파일 시스템, 스트림, PDF/A 또는 PDF/X와 같은 특정 형식으로 저장하는 세 가지 기본 방법을 간략하게 설명합니다. `Document` 클래스의 `save () `메서드는 이러한 작업의 핵심입니다.PDF를 파일 시스템에 저장하려면 새 페이지를 추가하는 등 문서를 만들거나 조작한 다음 경로에 직접 저장할 수 있습니다.스트림에 저장하는 경우 `Save` 메서드의 오버로드를 통해 스트림 객체에 문서를 쓸 수 있습니다.또한 이 문서에서는 각각 장기 보관 및 그래픽 교환의 표준인 PDF/A 또는 PDF/X 형식으로 문서를 저장하는 방법을 설명합니다.이 프로세스를 수행하려면 문서를 저장하기 전에 '변환' 방법으로 문서를 준비해야 합니다.제공된 Python 코드 스니펫은 각 접근 방식을 보여 주며 이러한 메서드의 실제 적용을 보여줍니다.
---

## PDF 문서를 파일 시스템에 저장

작성하거나 조작한 PDF 문서를 사용하여 파일 시스템에 저장할 수 있습니다. [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 의 방법 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.

```python
import aspose.pdf as ap

def save_document_to_file(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    document.save(outfile)
```

## 스트리밍할 PDF 문서 저장

오버로드를 사용하여 생성하거나 조작한 PDF 문서를 스트리밍에 저장할 수도 있습니다. `Save` 방법.

```python
import aspose.pdf as ap
import io

def save_document_to_stream(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    with io.FileIO(outfile, 'w') as stream:
        document.save(stream)
```

## PDF/A 또는 PDF/X 형식으로 저장

PDF/A 또는 PDF/X와 같은 특정 버전의 PDF에 문서를 쉽게 저장할 수 있습니다. 이 경우 문서를 저장하기 전에 convert 메서드를 호출해야 합니다.

PDF/A는 전자 문서의 보관 및 장기 보존에 사용되는 휴대용 문서 형식 (PDF) 의 ISO 표준 버전입니다.
PDF/A는 글꼴 연결 (글꼴 포함과 반대) 및 암호화와 같이 장기 보관에 적합하지 않은 기능을 금지한다는 점에서 PDF와 다릅니다.PDF/A 뷰어의 ISO 요구 사항에는 색상 관리 지침, 포함된 글꼴 지원, 포함된 주석을 읽을 수 있는 사용자 인터페이스가 포함됩니다.

PDF/X는 PDF ISO 표준의 하위 집합입니다.PDF/X의 목적은 그래픽 교환을 용이하게 하기 위한 것이므로 표준 PDF 파일에는 적용되지 않는 일련의 인쇄 관련 요구 사항이 있습니다.

두 경우 모두 [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드는 문서를 저장하는 데 사용되며 문서는 다음을 사용하여 준비해야 합니다. [변하게 하다](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법.

```python
import aspose.pdf as ap
import io


def save_document_as_standard(infile, outfile, logfile):
    document = ap.Document(infile)
    document.pages.add()
    document.convert(logfile, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

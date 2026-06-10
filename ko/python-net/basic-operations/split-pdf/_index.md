---
title: 파이썬에서 PDF 파일 분할하기
linktitle: PDF 파일 분할
type: docs
weight: 60
url: /ko/python-net/split-pdf/
description: Python에서 PDF 페이지를 별도의 PDF 파일로 분할하는 방법을 알아보세요.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 사용하여 PDF 페이지 분할하기
Abstract: 이 기사에서는 Python을 사용하여 PDF 페이지를 개별 파일로 분할하는 프로세스에 대해 설명하고 이러한 기능이 대용량 PDF 문서를 관리하는 데 유용하다는 점을 강조합니다.이 문서에서는 PDF 분할 기능을 설명하기 위해 설계된 온라인 도구인 Aspose.PDF Splitter를 참조합니다.이 문서에서는 파이썬 응용 프로그램에서 이 작업을 수행하는 방법에 대해 자세히 설명합니다. 여기에는 'Document' 객체의 'PageCollection'을 통해 PDF 문서의 페이지를 반복하는 방법이 포함됩니다.각 페이지에 대해 새 `Document` 객체가 생성되고, 페이지가 여기에 추가되고, `save () `메서드를 사용하여 새 PDF 파일이 저장됩니다.함께 제공되는 Python 코드 스니펫은 이 과정을 설명하며, 페이지를 반복하고 각 페이지를 개별 PDF로 저장하여 PDF 문서를 별도의 파일로 분할하는 데 필요한 단계를 보여줍니다.
---

PDF 페이지 분할은 큰 파일을 별도의 페이지 또는 페이지 그룹으로 분할하려는 사람들에게 유용한 기능이 될 수 있습니다.

배포, 검토 또는 다운스트림 처리를 위해 큰 PDF를 단일 페이지 파일이나 작은 문서 세트로 나누어야 할 때 이 워크플로우를 사용하십시오.

## 라이브 예제

[Aspose.PDF 스플리터](https://products.aspose.app/pdf/splitter) 프레젠테이션 분할 기능이 어떻게 작동하는지 조사할 수 있는 온라인 무료 웹 응용 프로그램입니다.

[![어스포즈 스플릿 PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

이 항목에서는 Python 응용 프로그램에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.Python을 사용하여 PDF 페이지를 단일 페이지 PDF 파일로 분할하려면 다음 단계를 따를 수 있습니다.

1. PDF 문서의 페이지를 반복하여 살펴보세요. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 사물의 [페이지 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 수집
1. 각 이터레이션에 대해 새 Document 객체를 만들고 개별 객체를 추가합니다. [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 빈 문서에 개체 추가
1. 를 사용하여 새 PDF 저장 [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법

## Python에서 PDF를 여러 파일로 분할하거나 PDF를 분리합니다.

다음 Python 코드 스니펫은 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```

## 관련 문서 주제

- [파이썬에서 PDF 문서로 작업하기](/pdf/ko/python-net/working-with-documents/)
- [파이썬으로 PDF 파일 병합](/pdf/ko/python-net/merge-pdf-documents/)
- [파이썬에서 PDF 파일 최적화하기](/pdf/ko/python-net/optimize-pdf/)
- [파이썬에서 PDF 문서 조작하기](/pdf/ko/python-net/manipulate-pdf-document/)


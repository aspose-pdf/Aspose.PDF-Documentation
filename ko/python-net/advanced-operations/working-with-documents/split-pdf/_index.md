---
title: Python에서 프로그래밍 방식으로 PDF 분할
linktitle: PDF 파일 분할
type: docs
weight: 60
url: /ko/python-net/split-pdf-document/
description: 이 주제는 Python 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용한 PDF 페이지 분할
Abstract: 이 문서는 Python을 사용하여 PDF 페이지를 개별 파일로 분할하는 과정에 대해 논의하며, 대용량 PDF 문서를 관리하는 데 이러한 기능의 유용성을 강조합니다. 여기에서는 PDF 분할 기능을 시연하기 위해 설계된 온라인 도구인 Aspose.PDF Splitter를 언급합니다. 이 문서는 Python 애플리케이션에서 이를 구현하기 위한 상세한 방법을 제공하는데, `Document` 객체의 `PageCollection`을 통해 PDF 문서의 페이지를 순회합니다. 각 페이지마다 새로운 `Document` 객체를 생성하고, 해당 페이지를 추가한 뒤 `save()` 메서드로 새로운 PDF 파일을 저장합니다. 첨부된 Python 코드 스니펫은 이 과정을 보여주며, 페이지를 순회하면서 각 페이지를 개별 PDF로 저장하는 단계들을 설명합니다.
---

PDF 페이지 분할은 대용량 파일을 개별 페이지 또는 페이지 그룹으로 나누고자 하는 사용자에게 유용한 기능이 될 수 있습니다.

## 실시간 예제

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) 은(는) 프레젠테이션 분할 기능이 어떻게 작동하는지 확인할 수 있는 무료 온라인 웹 애플리케이션입니다.

[![Aspose PDF 분할](splitter.png)](https://products.aspose.app/pdf/splitter)

이 문서는 Python 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다. Python을 사용하여 PDF 페이지를 단일 페이지 PDF 파일로 분할하려면 다음 단계를 따라야 합니다:

1. PDF 문서의 페이지를 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 컬렉션을 통해 순회합니다
1. 각 반복마다 새로운 Document 객체를 생성하고, 개별 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 객체를 빈 문서에 추가합니다
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 사용하여 새 PDF를 저장합니다

## Python에서 PDF를 여러 파일 또는 개별 PDF로 분할

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



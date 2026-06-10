---
title: Python을 사용하여 PDF 파일에서 이미지 삭제하기
linktitle: 이미지 삭제
type: docs
weight: 20
url: /ko/python-net/delete-images-from-pdf-file/
description: Python에서 PDF 파일의 특정 이미지 또는 전체 이미지를 삭제하는 방법을 알아봅니다.
lastmod: "2026-06-10"
TechArticle: true
AlternativeHeadline: 파이썬으로 PDF 파일에서 이미지 삭제하기
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 문서에서 이미지를 삭제하는 방법을 보여줍니다.특정 이미지 리소스를 제거하고 선택한 페이지에서 모든 이미지를 삭제하는 방법을 설명합니다.
---

문서에서 불필요한 그래픽을 제거하거나, PDF 크기를 줄이거나, 민감한 시각적 콘텐츠를 정리해야 할 때 이 페이지를 사용하십시오.

## PDF 파일에서 이미지 삭제

다음 단계를 사용하여 페이지에서 이미지 하나를 삭제합니다.

1. 를 사용하여 소스 PDF를 로드합니다. `ap.Document(infile)`.
1. 페이지 및 이미지 리소스 색인을 선택합니다.
1. 를 사용하여 이미지를 삭제합니다. `resources.images.delete(index)`.
1. 업데이트된 PDF를 저장합니다.

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## 페이지에서 모든 이미지 삭제

이 예제를 사용하여 특정 페이지에서 모든 이미지를 제거합니다.

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## 관련 이미지 주제

- [Python을 사용하여 PDF의 이미지로 작업하기](/pdf/ko/python-net/working-with-images/)
- [기존 PDF 파일의 이미지 바꾸기](/pdf/ko/python-net/replace-image-in-existing-pdf-file/)
- [PDF 파일에서 이미지 추출](/pdf/ko/python-net/extract-images-from-pdf-file/)
- [기존 PDF 파일에 이미지 추가](/pdf/ko/python-net/add-image-to-existing-pdf-file/)
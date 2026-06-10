---
title: 파이썬에서 PDF 페이지 회전하기
linktitle: PDF 페이지 회전
type: docs
weight: 110
url: /ko/python-net/rotate-pages/
description: Python에서 PDF 페이지를 회전하고 페이지 방향을 변경하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 페이지를 회전하는 방법
Abstract: 이 문서에서는 Python을 사용하여 기존 PDF 파일의 페이지 방향을 프로그래밍 방식으로 업데이트하거나 변경하는 방법에 대한 가이드를 제공합니다..NET을 통해 Python용 Aspose.PDF 를 활용하면 사용자는 페이지의 MediaBox 속성을 조정하여 가로 방향과 세로 방향 사이를 쉽게 전환할 수 있습니다.이 문서에는 PDF 문서의 페이지를 반복하고, 미디어박스 크기와 위치를 수정하고, 필요한 경우 CropBox를 조정하는 방법을 보여주는 Python 코드 스니펫이 포함되어 있습니다.또한 '회전' 방법을 사용하여 원하는 방향으로 페이지의 회전 각도를 설정하는 방법도 설명합니다.업데이트된 PDF 파일을 저장하는 것으로 프로세스가 종료됩니다.
---

이 항목에서는 Python을 사용하여 프로그래밍 방식으로 기존 PDF 파일의 페이지 방향을 업데이트하거나 변경하는 방법을 설명합니다.

세로 방향과 가로 방향 간에 페이지를 전환하거나 기존 PDF 내용에 회전 각도를 적용해야 할 때 이 페이지를 사용하십시오.

## 페이지 방향 변경

이 기능은 PDF의 모든 페이지를 회전시킵니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 파이썬용 Aspose.PDF 사용 시 시계 방향으로 90도
스캔한 문서 (예: 옆으로 있는 스캔 문서) 를 수정하는 데 유용합니다.원본 PDF는 변경되지 않고 회전된 버전은 새 파일로 저장됩니다.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## 관련 페이지 주제

- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [파이썬에서 PDF 페이지 크기 변경하기](/pdf/ko/python-net/change-page-size/)
- [파이썬에서 PDF 페이지 자르기](/pdf/ko/python-net/crop-pages/)
- [Python에서 PDF 페이지 속성 가져오기 및 설정](/pdf/ko/python-net/get-and-set-page-properties/)
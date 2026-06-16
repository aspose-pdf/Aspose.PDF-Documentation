---
title: 파이썬으로 PDF 파일 병합
linktitle: PDF 파일 병합
type: docs
weight: 50
url: /ko/python-net/merge-pdf/
description: Python에서 여러 PDF 파일을 단일 문서로 병합하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 사용하여 PDF 페이지 결합하기
Abstract: 이 문서에서는 여러 PDF 파일을 단일 문서로 병합해야 하는 일반적인 요구 사항에 대해 설명합니다. 이는 PDF 콘텐츠의 저장 및 공유를 구성하고 최적화하는 데 유용한 프로세스입니다.이 문서에서는 타사 라이브러리가 없으면 Python에서 PDF를 병합하는 것이 어려울 수 있다는 점을 인정하면서 Python에서.NET을 통해 Python에서 PDF 파일을 효율적으로 결합하는 방법을 살펴봅니다. Aspose.PDF이 문서에서는 PDF 파일을 연결하는 방법 (새 문서 만들기, 파일 병합, 병합된 문서 저장) 에 대한 단계별 가이드를 제공합니다.코드 스니펫은 Aspose.PDF 를 사용한 구현을 보여 주며 병합 프로세스를 간소화하는 라이브러리의 기능을 강조합니다.또한 PDF 병합을 위한 온라인 도구인 Aspose.PDF Merger를 도입하여 사용자가 웹 기반 환경에서 기능을 탐색할 수 있도록 합니다.
---

## 파이썬과 DOM을 사용하여 PDF 파일 병합

두 PDF 파일을 연결하려면:

1. 새 문서 만들기.
1. PDF 파일 병합
1. 병합된 문서 저장

여러 PDF 문서를 단일 파일로 결합:

```python
import sys
import aspose.pdf as ap
from os import path

def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## 라이브 예제

[Aspose.PDF 합병](https://products.aspose.app/pdf/merger) 프레젠테이션 병합 기능이 어떻게 작동하는지 조사할 수 있는 온라인 무료 웹 응용 프로그램입니다.

[![Aspose.PDF 합병](merger.png)](https://products.aspose.app/pdf/merger)


---
title: 파이썬을 통해 PDF에서 글꼴 추출
linktitle: PDF에서 글꼴 추출
type: docs
weight: 30
url: /ko/python-net/extract-fonts-from-pdf/
description: Python용 Aspose.PDF 라이브러리를 사용하여 PDF 문서에서 포함된 모든 글꼴을 추출할 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 글꼴을 추출하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서에 사용된 글꼴을 검사하는 방법을 설명합니다.Document 클래스로 PDF를 열고, font_utilities.get_all_fonts () 를 호출하여 사용 가능한 글꼴 객체를 검색하고, 결과를 반복하여 글꼴 이름을 읽어 분석, 감사 또는 문서 처리 워크플로에 사용하는 방법을 보여줍니다.
---

용도 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) PDF를 열고 전화하려면 `font_utilities.get_all_fonts()` 사용 가능한 모든 항목 검색 [폰트](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) 문서에서 참조하는 객체이는 포함된 글꼴을 감사하거나, 변환 전에 글꼴 가용성을 확인하거나, 문서 리소스를 분석할 때 유용합니다.

1. 소스 PDF를 다음과 같이 엽니다. `Document`.
1. 전화 `document.font_utilities.get_all_fonts()` 글꼴 모음을 가져오려면
1. 반환된 항목 전체 반복 `Font` 사물.
1. 각 항목 읽기 및 인쇄 `font.font_name` 가치.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

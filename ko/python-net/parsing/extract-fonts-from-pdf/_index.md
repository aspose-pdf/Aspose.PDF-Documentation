---
title: Python을 사용하여 PDF에서 글꼴 추출
linktitle: PDF에서 글꼴 추출
type: docs
weight: 30
url: /ko/python-net/extract-fonts-from-pdf/
description: Aspose.PDF for Python 라이브러리를 사용하여 PDF 문서에서 모든 포함된 글꼴을 추출합니다.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 글꼴을 추출하는 방법
Abstract: 이 문서는 Aspose.PDF 라이브러리의 특정 메서드를 사용하여 PDF 문서에서 모든 글꼴을 추출하는 방법에 대한 안내를 제공합니다. `Document` 클래스에서 사용할 수 있는 `font_utilities.get_all_fonts()` 메서드를 소개하며, 이는 글꼴 정보를 가져오는 과정을 용이하게 합니다. 이 문서에는 필요한 모듈을 가져오고, PDF 문서를 열고, 글꼴을 반복하여 각 글꼴의 이름을 출력하는 과정을 보여주는 Python 코드 스니펫이 포함되어 있습니다. 이 접근 방식은 PDF 파일 내에서 글꼴 데이터를 분석하거나 조작해야 하는 개발자에게 유용합니다.
---

PDF 문서에서 모든 글꼴을 가져오고 싶다면, Document 클래스에서 제공되는 'font_utilities.get_all_fonts()' 메서드를 사용할 수 있습니다. 기존 PDF 문서에서 모든 글꼴을 가져오기 위해 다음 코드 스니펫을 확인하십시오:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```


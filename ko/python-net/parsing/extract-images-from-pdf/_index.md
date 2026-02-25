---
title: Python으로 PDF에서 이미지 추출
linktitle: PDF에서 이미지 추출
type: docs
weight: 20
url: /ko/python-net/extract-images-from-the-pdf-file/
description: Aspose.PDF for Python을 사용하여 PDF에서 이미지의 일부를 추출하는 방법
lastmod: "2023-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 통해 PDF에서 이미지 추출하는 방법
Abstract: 이 문서는 Python을 사용하여 PDF 문서에서 내장된 이미지를 추출하는 간결한 가이드를 제공합니다. 이 과정은 PDF 문서를 로드하고, 이미지 리소스에 접근하며, 이미지를 파일로 저장하는 세 가지 주요 단계로 이루어집니다. 코드 스니펫은 이러한 작업을 용이하게 하기 위해 Aspose.PDF 라이브러리를 활용합니다. 먼저 지정된 경로에서 PDF 문서를 로드하고, 첫 페이지의 리소스에서 원하는 이미지를 가져옵니다. 마지막으로 파일 I/O 작업을 통해 지정된 출력 파일에 이미지를 저장하여 추가 분석, 편집 또는 다른 문서에서 재사용할 수 있습니다.
---

이 코드 스니펫은 PDF 문서에서 내장된 이미지를 추출하여 별도의 분석, 편집 또는 다른 문서에서 재사용할 수 있도록 합니다:

1. PDF 문서 로드
1. 이미지 리소스 접근
1. 이미지를 파일에 저장

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```


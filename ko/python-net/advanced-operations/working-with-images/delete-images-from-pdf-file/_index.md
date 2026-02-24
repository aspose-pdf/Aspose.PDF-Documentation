---
title: Python을 사용하여 PDF 파일에서 이미지 삭제
linktitle: 이미지 삭제
type: docs
weight: 20
url: /ko/python-net/delete-images-from-pdf-file/
description: 이 섹션에서는 Aspose.PDF for Python via .NET를 사용하여 PDF 파일에서 이미지를 삭제하는 방법을 설명합니다.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 이미지를 제거하는 방법
Abstract: 이 문서는 개인정보 보호, 민감한 정보에 대한 무단 접근 방지, 파일 크기 축소를 통한 보다 쉬운 공유 및 저장, 그리고 문서를 압축하거나 텍스트를 추출하기 위한 준비와 같은 PDF 파일에서 이미지를 제거하는 다양한 이유에 대해 논의합니다. 이 작업을 수행하기 위한 도구로 **Aspose.PDF for Python via .NET**를 소개합니다. 이 문서는 Aspose.PDF를 사용하여 PDF 파일에서 특정 이미지 또는 모든 이미지를 삭제하는 단계별 지침과 코드 스니펫을 제공합니다. 이 과정은 기존 PDF 문서를 열고, 이미지를 개별적으로 또는 대량으로 삭제한 다음, 업데이트된 파일을 저장하는 것을 포함합니다. 제공된 Python 코드는 문서의 리소스에 접근하고 원하는 페이지를 수정하여 이미지를 제거하는 방법을 보여줍니다.
---

PDF에서 전체 또는 특정 이미지를 제거하는 데는 여러 이유가 있습니다.
때때로 PDF 파일에는 개인정보를 보호하거나 특정 정보에 대한 무단 접근을 방지하기 위해 삭제해야 하는 중요한 이미지가 포함될 수 있습니다.

불필요하거나 중복된 이미지를 제거하면 파일 크기를 줄여 PDF를 보다 쉽게 공유하거나 저장할 수 있습니다.
필요한 경우 문서에서 모든 이미지를 제거하여 페이지 수를 줄일 수 있습니다.
또한, 문서에서 이미지를 삭제하면 PDF를 압축하거나 텍스트 정보를 추출하기 위한 준비에 도움이 됩니다.

**Aspose.PDF for Python via .NET**가 이 작업을 도와줍니다.

## PDF 파일에서 이미지 삭제

PDF 파일에서 이미지를 삭제하려면:

1. 기존 PDF 문서를 엽니다.
1. 특정 이미지를 삭제합니다.
1. 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일에서 이미지를 삭제하는 방법을 보여줍니다.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    document.pages[1].resources.images.delete(1)
    document.save(path_outfile)
```

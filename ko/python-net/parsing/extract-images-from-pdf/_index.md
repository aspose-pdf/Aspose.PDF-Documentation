---
title: Python을 사용하여 PDF에서 이미지 추출
linktitle: PDF에서 이미지 추출
type: docs
weight: 20
url: /ko/python-net/extract-images-from-the-pdf-file/
description: Python용 Aspose.PDF 를 사용하여 PDF 파일에서 임베디드 이미지를 추출하는 방법을 알아보세요.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬을 통해 PDF에서 이미지를 추출하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 임베디드 이미지를 추출하는 방법을 설명합니다.Document 클래스로 소스 PDF를 열고, 페이지 리소스 컬렉션에서 이미지에 액세스하고, 추출된 xImage를 재사용, 검사 또는 다운스트림 처리를 위해 외부 파일에 저장하는 방법을 설명합니다.
---

용도 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) PDF를 연 다음 페이지 리소스에 액세스하여 검색하십시오. [xImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) 객체를 생성하고 별도의 파일로 저장합니다.이 방법은 이미지를 재사용하거나, 추출된 자산을 검사하거나, PDF 내용에서 이미지 처리 워크플로를 구축해야 할 때 유용합니다.

1. PDF를 다음과 같이 엽니다. `Document`.
1. 대상 페이지에서 이미지 리소스에 액세스합니다.
1. 필요한 항목 검색 `XImage` 페이지 이미지 컬렉션에서
1. 추출한 이미지를 출력 파일에 저장합니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

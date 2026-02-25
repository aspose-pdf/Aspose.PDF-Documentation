---
title: Python으로 배경을 아티팩트로 작업하기
linktitle: 배경 추가
type: docs
weight: 20
url: /ko/python-net/add-backgrounds/
description: Python을 사용하여 PDF 파일에 배경 이미지를 추가합니다. BackgroundArtifact 클래스를 사용하세요.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에 배경을 추가하는 방법
Abstract: 이 문서는 Aspose.PDF for Python via .NET를 사용하여 PDF 문서에 배경 이미지를 적용하는 방법을 다룹니다. `BackgroundArtifact` 클래스를 활용하여 문서에 워터마크나 은은한 디자인을 추가할 수 있는 기능을 강조합니다. 이 클래스는 개별 페이지 객체에 배경 이미지를 삽입할 수 있게 해줍니다. 본문에서는 이 기능을 구현하는 실용적인 코드 예제를 제공합니다. 과정에는 새로운 PDF 문서를 생성하고, 페이지를 추가한 뒤, `BackgroundArtifact` 객체를 만들고, 배경 이미지를 설정한 후, 페이지의 아티팩트 컬렉션에 배경 아티팩트를 추가하는 단계가 포함됩니다. 마지막으로 수정된 문서를 PDF 파일로 저장합니다. 이 기술을 통해 PDF 문서의 시각적 표현을 향상시킬 수 있습니다.
---

배경 이미지는 문서에 워터마크나 기타 은은한 디자인을 추가하는 데 사용할 수 있습니다. Aspose.PDF for Python via .NET에서 각 PDF 문서는 페이지들의 컬렉션이며 각 페이지는 아티팩트 컬렉션을 포함합니다. [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) 클래스를 사용하여 페이지 객체에 배경 이미지를 추가할 수 있습니다.

다음 코드 조각은 Python을 사용하여 BackgroundArtifact 객체로 PDF 페이지에 배경 이미지를 추가하는 방법을 보여줍니다.

```python

import aspose.pdf as ap
import io

def add_background_image(input_image_file, output_pdf):
    # Create a new PDF document
    document = ap.Document()

    # Add a blank page to the document
    page = document.pages.add()

    # Create a BackgroundArtifact object
    background = ap.BackgroundArtifact()

    # Load the image as a binary stream
    with open(input_image_file, "rb") as image_stream:
        background.background_image = image_stream

        # Add the background artifact to the page
        page.artifacts.append(background)

    # Save the resulting PDF
    document.save(output_pdf)
```



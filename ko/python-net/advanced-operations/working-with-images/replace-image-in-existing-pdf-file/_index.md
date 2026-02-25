---
title: Python을 사용하여 기존 PDF 파일에서 이미지 교체
linktitle: 이미지 교체
type: docs
weight: 70
url: /ko/python-net/replace-image-in-existing-pdf-file/
description: 이 섹션은 Python 라이브러리를 사용하여 기존 PDF 파일에서 이미지를 교체하는 방법에 대해 설명합니다.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: PDF에서 이미지 교체
Abstract: Aspose.PDF for Python via .NET 문서는 기존 PDF 파일 내 이미지 교체에 대한 포괄적인 가이드를 제공합니다. 이 기능은 텍스트 내용은 그대로 두고 PDF 문서의 로고, 그래픽 또는 기타 시각 요소를 업데이트하는 작업에 필수적입니다.
---

## PDF에서 이미지 교체

PDF 페이지의 기존 이미지를 새 이미지로 교체하려면 어떻게 해야 할까요? Aspose.PDF for Python via .NET을 사용하여 구현합니다.

1. 필요한 모듈을 가져옵니다 (aspose.pdf, os.path, FileIO).
1. 경로를 정의합니다:
- 입력 PDF (infile)
- 새 이미지 파일 (image_file)
- 출력 PDF (outfile)
1. 'apdf.Document(path_infile)'을 사용하여 PDF 문서를 로드합니다.
1. 새 이미지 파일을 이진 읽기 모드로 엽니다.
1. 첫 페이지의 첫 번째 이미지를 교체합니다:
- 'document.pages[1].resources.images.replace(1, image_stream)'
1. 업데이트된 PDF를 'path_outfile'에 저장합니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    with FileIO(path_image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(path_outfile)
```

## 특정 이미지 교체

이 예제는 이미지 배치 감지를 통해 PDF 페이지의 특정 이미지를 찾아 교체하는 방법을 보여줍니다.

1. 'apdf.Document()'를 사용하여 PDF를 로드합니다.
1. 페이지의 모든 이미지 배치를 수집하기 위해 'ImagePlacementAbsorber'를 생성합니다.
1. 첫 페이지에서 흡수기를 적용합니다 ('document.pages[1].accept(absorber)').
1. 페이지에 이미지 배치가 존재하는지 확인합니다.
1. 첫 번째 이미지 배치 (absorber.image_placements[1])를 선택하고 교체합니다.
1. 수정된 PDF를 'path_outfile'에 저장합니다.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = apdf.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(path_image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(path_outfile)
```

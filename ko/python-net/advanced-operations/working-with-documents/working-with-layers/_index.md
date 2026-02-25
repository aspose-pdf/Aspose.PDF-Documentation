---
title: Python을 사용하여 PDF 레이어 작업
linktitle: PDF 레이어 작업
type: docs
weight: 50
url: /ko/python-net/working-with-pdf-layers/
description: 다음 작업에서는 PDF 레이어를 잠그고, PDF 레이어 요소를 추출하며, 레이어가 있는 PDF를 평탄화하고, PDF 내부의 모든 레이어를 하나로 병합하는 방법을 설명합니다.
lastmod: "2025-11-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 레이어 조작
Abstract: 이 가이드는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 레이어를 관리하고 조작하는 방법에 대한 포괄적인 개요를 제공합니다. PDF 레이어는 선택적 콘텐츠 그룹(Optional Content Groups, OCG)이라고도 하며, 콘텐츠를 별개의 시각적 구성 요소로 조직하여 켜거나 끌 수 있게 합니다.
---

PDF 레이어는 단일 PDF 파일 내에서 콘텐츠를 유연하게 구성하고 제공하는 강력한 방법으로, 사용자가 필요에 따라 서로 다른 부분을 표시하거나 숨길 수 있게 합니다.

**Aspose.PDF for Python via .NET**를 사용하면 다음을 할 수 있습니다:

- 레이어를 잠그거나 잠금 해제하여 가시성을 제어합니다.
- 레이어를 별도의 파일이나 스트림으로 추출합니다.
- 레이어를 평탄화하여 영구적으로 만듭니다.
- 레이어를 하나의 통합 레이어로 병합합니다.

## PDF에 레이어 추가

이 예제는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에 여러 레이어를 생성하고 추가하는 방법을 보여줍니다. 각 레이어는 색상 라인과 같은 별개의 그래픽 콘텐츠를 포함하며, 레이어를 지원하는 PDF 뷰어에서 켜거나 끌 수 있습니다.

1. 새로운 PDF 문서를 만들고 페이지를 추가합니다.
1. 빨간색 레이어를 생성하고 추가합니다.
1. 녹색 레이어를 생성하고 추가합니다.
1. 파란색 레이어를 생성하고 추가합니다.
1. PDF 문서를 저장합니다.

결과 PDF는 빨간선, 녹색선, 파란선이라는 세 개의 개별 레이어를 포함합니다. 각 레이어는 레이어 콘텐츠를 지원하는 PDF 리더에서 켜거나 끌 수 있습니다.

```python

import aspose.pdf as ap
from os import path

def add_colored_layers(outfile: str, data_dir: str) -> None:
    """
    Creates a PDF with three layers (Red, Green, Blue lines).
    
    Args:
        outfile (str): Name of the output PDF file.
        data_dir (str): Directory path to save the file.
    """
    path_outfile = path.join(data_dir, outfile)

    try:
        # Create a new PDF document and add a blank page
        document = ap.Document()
        page = document.pages.add()

        # Helper function to add a colored line layer
        def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
            layer = ap.Layer(layer_id, layer_name)
            layer.contents.append(ap.operators.SetRGBColorStroke(*color))
            layer.contents.append(ap.operators.MoveTo(500, y_position))
            layer.contents.append(ap.operators.LineTo(400, y_position))
            layer.contents.append(ap.operators.Stroke())
            page.layers.append(layer)

        # Add Red, Green, and Blue layers
        add_layer("oc1", "Red Line", (1, 0, 0), 700)
        add_layer("oc2", "Green Line", (0, 1, 0), 750)
        add_layer("oc3", "Blue Line", (0, 0, 1), 800)

        # Save the document
        document.save(path_outfile)
        print(f"\nLayers added successfully.\nFile saved at: {path_outfile}")

    except Exception as e:
        print(f"Error adding layers: {e}")
```

## PDF 레이어 잠금

Aspose.PDF for Python via .NET을 사용하면 PDF를 열고, 첫 페이지의 특정 레이어를 잠근 뒤, 변경 사항을 저장할 수 있습니다.

이 예제는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서에서 레이어(옵션 콘텐츠 그룹, OCG)를 잠그는 방법을 보여줍니다. 잠금은 사용자가 PDF 뷰어에서 레이어의 가시성을 변경하지 못하도록 하여, 문서에 정의된 대로 콘텐츠가 항상 표시(또는 숨김)되도록 보장합니다.

사용 가능한 메서드 및 속성:

- layer.lock() – 레이어를 잠급니다.
- layer.unlock() – 레이어의 잠금을 해제합니다.
- layer.locked – 현재 잠금 상태를 반환합니다.

1. PDF 문서를 엽니다.
1. PDF의 첫 페이지에 접근합니다.
1. 페이지에 레이어가 있는지 확인합니다.
1. 첫 번째 레이어를 가져와 잠급니다.
1. 업데이트된 PDF를 저장합니다.

PDF에 레이어가 포함되어 있으면 첫 번째 레이어가 잠기며, 사용자가 가시성 상태를 변경할 수 없게 됩니다. 레이어가 없을 경우 대신 메시지가 출력됩니다.

```python

import aspose.pdf as ap
from os import path

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## PDF 레이어 요소 추출

이 예제는 Aspose.PDF for Python via .NET 라이브러리를 사용하여 PDF 문서의 첫 페이지에서 개별 레이어를 추출하고 각 레이어를 별도의 PDF 파일로 저장합니다.

레이어에서 새로운 PDF를 만들려면 다음 코드 조각을 사용할 수 있습니다:

1. PDF 문서를 로드합니다. 입력 PDF는 Aspose.PDF.Document 객체에 로드됩니다.
1. 페이지 1의 레이어에 접근합니다. 스크립트는 document.pages[1].layers를 사용하여 첫 페이지의 모든 레이어를 가져옵니다.
1. 레이어를 확인합니다. 레이어가 없으면 메시지를 출력하고 함수가 종료됩니다.
1. 각 레이어를 순회하며 저장합니다.

```python

import aspose.pdf as ap
from os import path

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

PDF 레이어 요소를 추출하여 새로운 PDF 파일 스트림에 저장할 수 있습니다:

```python

import aspose.pdf as ap
from os import path

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## 레이어가 있는 PDF 평탄화

이 스크립트는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서의 첫 페이지에 있는 모든 레이어를 평탄화합니다. 평탄화는 각 레이어의 시각적 콘텐츠를 하나의 통합 레이어로 병합하여, 시각적 완성도나 레이어별 데이터를 잃지 않으면서 인쇄, 공유 또는 보관을 쉽게 합니다.

1. PDF 문서를 로드합니다. 입력 PDF가 Aspose.PDF.Document 객체에 로드됩니다.
1. 페이지 1의 레이어에 접근합니다. 스크립트는 document.pages[1].layers를 사용하여 첫 번째 페이지의 모든 레이어를 가져옵니다.
1. 레이어 존재 여부를 확인합니다. 레이어가 없으면 메시지를 출력하고 함수가 종료됩니다.
1. 각 레이어를 평면화합니다. 각 레이어는 layer.flatten(True)를 사용하여 평면화되며, 이는 해당 내용을 페이지에 병합합니다.
1. 수정된 문서를 저장합니다.

```python

import aspose.pdf as ap
from os import path

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if not page.layers:
            print("No layers found in the document.")
            return
        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

## PDF 내부의 모든 레이어를 하나로 병합

이 코드 스니펫은 Aspose.PDF를 사용하여 PDF 첫 페이지의 모든 레이어를 사용자 정의 이름이 있는 하나의 통합 레이어로 병합합니다.

1. PDF 문서를 로드합니다. PDF가 Aspose.PDF.Document 객체에 로드됩니다.
1. 페이지와 해당 레이어에 접근합니다. 첫 번째 페이지를 선택하고 레이어를 가져옵니다.
1. 레이어를 확인합니다. 레이어가 없으면 메시지를 출력하고 프로세스가 종료됩니다.
1. 새 레이어 이름을 정의합니다. 병합 결과를 위해 새로운 레이어 이름("LayerNew")을 지정합니다.
1. 레이어를 병합합니다. 선택적 콘텐츠 그룹 ID가 제공되면 병합에 사용됩니다. 그렇지 않으면 새 이름만 사용하여 레이어를 병합합니다.
1. 문서를 저장합니다

```python

import aspose.pdf as ap
from os import path

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```

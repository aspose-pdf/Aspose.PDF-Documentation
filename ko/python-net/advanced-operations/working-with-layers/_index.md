---
title: 파이썬을 사용하여 PDF 레이어로 작업하기
linktitle: PDF 레이어 사용
type: docs
weight: 50
url: /ko/python-net/working-with-pdf-layers/
description: Python에서 PDF 레이어를 추가, 잠금, 추출, 병합 및 병합하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬으로 PDF 레이어 관리
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 레이어 (선택적 콘텐츠 그룹) 를 사용하는 방법을 설명합니다.레이어 추가, 레이어 가시성 잠금, 레이어 콘텐츠 추출, 계층화된 콘텐츠 병합, 레이어를 하나로 병합하는 방법을 알아봅니다.
---

OCG (선택적 콘텐츠 그룹) 라고도 하는 PDF 레이어를 사용하면 콘텐츠를 호환되는 PDF 뷰어에서 표시하거나 숨길 수 있는 별도의 시각적 그룹으로 구성할 수 있습니다.Aspose.PDF 에서는 레이어 작업이 다음을 중심으로 구축됩니다. [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) API.

.NET을 통한 파이썬용 Aspose.PDF 기능을 사용하면 다음과 같은 작업을 수행할 수 있습니다.

- 페이지에 여러 레이어를 추가합니다.
- 가시성 동작을 제어하기 위해 레이어를 잠그거나 잠금 해제합니다.
- 레이어를 별도의 파일 또는 스트림으로 추출합니다.
- 레이어로 구성된 콘텐츠를 페이지에 통합합니다.
- 여러 레이어를 하나의 레이어로 병합합니다.

## PDF에 레이어 추가

이 예제에서는 세 개의 레이어가 있는 PDF를 만듭니다.a를 사용합니다. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), 를 추가합니다. [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), 및 추가 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) 해당 페이지의 객체.

1. 새 만들기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 그리고 추가 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 빨간색 레이어를 만들고 추가합니다.
1. 녹색 레이어를 만들고 추가합니다.
1. 파란색 레이어를 만들고 추가합니다.
1. PDF 문서를 저장합니다.

결과 PDF에는 빨간색 선, 녹색 선 및 파란색 선의 세 가지 개별 레이어가 포함됩니다.레이어로 구성된 내용을 지원하는 PDF 리더에서 각 항목을 켜거나 끌 수 있습니다.

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
    document = ap.Document()
    page = document.pages.add()

    # Red layer
    layer = ap.Layer("oc1", "Red Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
    layer.contents.append(ap.operators.MoveTo(500, 700))
    layer.contents.append(ap.operators.LineTo(400, 700))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Green layer
    layer = ap.Layer("oc2", "Green Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
    layer.contents.append(ap.operators.MoveTo(500, 750))
    layer.contents.append(ap.operators.LineTo(400, 750))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Blue layer
    layer = ap.Layer("oc3", "Blue Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
    layer.contents.append(ap.operators.MoveTo(500, 800))
    layer.contents.append(ap.operators.LineTo(400, 800))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    document.save(outfile)
    print(f"Layers added successfully. File saved at {outfile}")
```

## PDF 레이어 잠금

이 예제에서는 PDF를 열고 첫 페이지의 특정 레이어를 잠근 다음 업데이트된 파일을 저장합니다.

레이어를 잠그면 지원되는 PDF 뷰어에서 사용자가 해당 레이어의 가시성 상태를 변경할 수 없습니다.레이어는 페이지에서 액세스하고 페이지의 레이어 컬렉션을 통해 관리됩니다.

사용 가능한 메서드 및 속성:

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) 레이어를 잠급니다.
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) 레이어 잠금을 해제합니다.
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) 현재 잠금 상태를 반환합니다.

1. PDF 문서를 엽니다.
1. PDF의 첫 페이지에 액세스합니다.
1. 페이지에 레이어가 있는지 확인합니다.
1. 첫 번째 레이어를 가져와서 잠급니다.
1. 업데이트된 PDF를 저장합니다.

PDF에 레이어가 포함된 경우 첫 번째 레이어가 잠기므로 사용자가 가시성 상태를 변경할 수 없습니다.레이어를 찾을 수 없는 경우 메시지가 대신 인쇄됩니다.

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## PDF 레이어 요소 추출

이 예제에서는 .NET 라이브러리를 통해 Aspose.PDF for Python을 사용하여 PDF 문서의 첫 페이지에서 개별 레이어를 추출하고 다음을 사용하여 각 레이어를 별도의 PDF 파일로 저장합니다. [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

레이어에서 새 PDF를 만들려면 다음 코드 스니펫을 사용할 수 있습니다.

1. PDF 불러오기 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 1페이지부터 페이지까지 레이어에 접근 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 레이어가 존재하는지 확인합니다.
1. 레이어를 반복하고 각 레이어를 저장합니다.

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

PDF 레이어 요소를 추출하여 새 PDF 파일 스트림에 저장할 수 있습니다.

```python
from io import FileIO
import aspose.pdf as ap

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## 레이어로 구성된 PDF 병합

이 스크립트는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서의 첫 페이지에 있는 모든 레이어를 병합합니다.병합을 사용하면 각 레이어의 시각적 내용이 하나의 통합된 레이어로 병합되므로 시각적 사실성이나 레이어별 데이터를 잃지 않고도 더 쉽게 인쇄, 공유 또는 보관할 수 있습니다.작업은 다음과 같이 수행됩니다. [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. PDF 문서를 로드합니다.
1. 1페이지의 레이어에 접근합니다.
1. 레이어가 존재하는지 확인합니다.
1. 각 레이어를 다음과 같이 평평하게 합니다. `layer.flatten(True)`.
1. 수정한 문서를 저장합니다.

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
```

## PDF의 모든 레이어를 하나로 병합

이 코드 스니펫은 Aspose.PDF 를 사용하여 PDF의 첫 페이지에 있는 모든 레이어를 사용자 지정 이름이 있는 하나의 통합된 레이어로 병합합니다. [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. PDF 문서를 로드합니다.
1. 페이지 1에 접근하여 해당 레이어를 검색합니다.
1. 레이어가 존재하는지 확인합니다.
1. 새 레이어 이름을 정의합니다.
1. 레이어를 하나로 병합합니다.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```

## 관련 레이어 주제

- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [Python을 사용하여 PDF에서 표 작업하기](/pdf/ko/python-net/working-with-tables/)
- [파이썬에서 PDF 페이지 추가](/pdf/ko/python-net/add-pages/)

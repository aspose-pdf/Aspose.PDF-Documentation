---
title: Python을 이용한 PDF 레이어 작업
linktitle: PDF 레이어 작업
type: docs
weight: 50
url: /ko/python-net/work-with-pdf-layers/
description: 이 문서는 PDF 레이어를 잠그는 방법, PDF 레이어 요소를 추출하는 방법, 레이어가 있는 PDF를 평탄화하는 방법, 그리고 PDF 내부의 모든 레이어를 하나로 병합하는 방법을 설명합니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 레이어를 관리, 잠금, 추출, 평탄화 및 병합하는 방법
Abstract: 이 문서는 .NET용 Aspose.PDF를 사용하여 Python에서 PDF 레이어를 작업하는 방법을 설명합니다. 여기에는 레이어 잠금, 레이어 요소 추출, 레이어가 있는 PDF 평탄화 및 레이어 병합이 포함됩니다.
---

PDF 레이어를 사용하면 문서에 여러 개의 콘텐츠 세트를 포함시켜 선택적으로 표시하거나 숨길 수 있습니다. 각 레이어에는 텍스트, 이미지 또는 그래픽이 포함될 수 있으며, 사용자는 필요에 따라 이를 켜거나 끌 수 있습니다. 레이어는 콘텐츠를 조직하거나 분리해야 하는 복잡한 문서에서 특히 유용합니다. 아래 예제에서는 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 및 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API를 사용하고 페이지의 `layers` 컬렉션을 통해 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) 객체를 조작합니다.

## PDF 레이어 잠그기

Aspose.PDF for Python via .NET을 사용하면 PDF를 열고([`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)) 첫 번째 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)에서 특정 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/)를 잠그고, 변경 사항을 문서에 저장할 수 있습니다.

`[`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/)` 객체에서 사용 가능한 메서드 및 속성:

- `layer.lock()` – 레이어를 잠급니다. (see [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.unlock()` – 레이어의 잠금을 해제합니다. (see [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.locked` – 현재 잠금 상태를 반환합니다. (see [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties))

1. PDF 문서를 엽니다 (참조: [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. 문서의 [`Pages`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 컬렉션을 사용해 첫 페이지를 가져옵니다 (참조: [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).
1. `page.layers`에서 잠글 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/)를 선택합니다.
1. `layer.lock()`을 호출하여 사용자가 레이어 표시를 전환하지 못하도록 합니다.
1. [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)를 사용해 업데이트된 문서를 저장합니다.

```python

import aspose.pdf as ap

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

Aspose.PDF를 사용하면 각 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/)를 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)에서 추출하여 별도의 PDF 파일로 저장할 수 있습니다.

레이어를 사용해 새 PDF를 만들려면, 다음 코드 스니펫을 사용할 수 있습니다 (`layers` 컬렉션은 `Page.layers`를 통해 접근합니다):

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF with a unique filename
        for i, layer in enumerate(layers):
            layer.save(f"{path_outfile}_layer_{i}.pdf")
```

레이어를 스트림에 저장할 수도 있습니다:

```python

import aspose.pdf as ap
import io

def save_layers_to_stream(path_infile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        streams = []
        for layer in layers:
            layer_stream = io.BytesIO()
            layer.save(layer_stream)
            layer_stream.seek(0)
            streams.append(layer_stream)
        return streams
```

## 레이어가 있는 PDF 평탄화

평탄화는 페이지에 있는 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/)을 영구적으로 만들어 토글 기능을 제거합니다.

```python

import aspose.pdf as ap

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

`cleanup_content_stream` 매개변수는 선택적 콘텐츠 그룹 마커(OCG 마커)를 제거할지 여부를 제어합니다. 이를 `False`로 설정하면 평탄화 속도가 빨라집니다. 자세한 내용은 [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) 메서드를 참고하세요.

## PDF 내부의 모든 레이어를 하나로 병합

모든 레이어(또는 특정 레이어)를 하나의 새 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/)으로 병합할 수 있습니다(병합 API는 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 객체에 있습니다).

`[`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)` 객체의 메서드:

- `page.merge_layers(new_layer_name)` — 모든 레이어를 새로운 레이어 이름으로 병합합니다 (see [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).
- `page.merge_layers(new_layer_name, new_optional_content_group_id)` — 사용자 정의 선택적 콘텐츠 그룹 ID를 사용해 병합합니다 (see [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).

```python

import aspose.pdf as ap

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```

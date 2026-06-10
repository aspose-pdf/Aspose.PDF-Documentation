---
title: Python을 사용하여 PDF 그래프의 모양 경계 확인하기
linktitle: 쉐이프 바운드 확인
type: docs
weight: 70
url: /ko/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Python에서 PDF 그래프 컬렉션의 형상 경계를 검증하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일의 그래프 모양 경계의 유효성을 검사합니다.
Abstract: 이 문서에서는 .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 그래프 컬렉션의 모양 경계를 검증하는 방법을 보여줍니다.BoundsCheckMode 구성, 범위를 벗어난 셰이프 감지, 경계 예외를 안전하게 처리하는 방법을 다룹니다.
---

## 그래프에서 형상 경계 확인하기

에 도형을 추가할 때 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/)경계 검증을 활성화하여 각 모양이 그래프 영역 내에 맞는지 확인할 수 있습니다.

용도 [경계 검사 모드](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) 도형이 범위를 벗어났을 때의 동작을 정의합니다.이 예시에서는 `THROW_EXCEPTION_IF_DOES_NOT_FIT` 예외를 발생시키는 데 사용됩니다.

아래 단계를 따르십시오.

1. 새 PDF 만들기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 추가 [페이지](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 만들기 [그래프](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 페이지에 추가합니다.
1. 만들기 [직사각형](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) 이는 그래프 경계 밖으로 확장됩니다.
1. 경계 검사 모드를 다음으로 설정 `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. 사각형을 추가하고 예외를 처리합니다.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)

    document.save(outfile)
```

## 노트

- 용도 `THROW_EXCEPTION_IF_DOES_NOT_FIT` 엄격한 레이아웃 검증이 필요한 경우
- 허용적인 행동을 원하면 다른 것을 선택하십시오. `BoundsCheckMode` 레이아웃 요구 사항에 따른 옵션.

## 관련 그래프 주제

- [파이썬에서 PDF 그래프로 작업하기](/pdf/ko/python-net/working-with-graphs/)
- [Python에서 PDF에 사각형 모양 추가](/pdf/ko/python-net/add-rectangle/)
- [파이썬에서 PDF에 선 모양 추가](/pdf/ko/python-net/add-line/)
- [Python에서 PDF에 타원 모양 추가](/pdf/ko/python-net/add-ellipse/)

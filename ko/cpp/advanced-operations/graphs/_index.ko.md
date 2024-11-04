---
title: PDF에서 그래프 작업하기
linktitle: 그래프 작업하기
type: docs
weight: 70
url: /cpp/graphs/
description: 이 기사는 그래프가 무엇인지, 채워진 사각형 객체를 만드는 방법, 그래프 객체 내부에 텍스트를 추가하는 방법, PDF에 선 객체를 추가하는 방법 등을 설명합니다.
lastmod: "2021-12-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 그래프란 무엇인가

PDF 문서에 그래프를 추가하는 것은 Adobe Acrobat Writer 또는 기타 PDF 처리 응용 프로그램을 사용할 때 개발자에게 매우 일반적인 작업입니다. PDF 응용 프로그램에서 사용할 수 있는 그래프의 종류는 매우 다양합니다.
[Aspose.PDF for C++](/pdf/cpp/) 또한 PDF 문서에 그래프를 추가하는 것을 지원합니다. 이를 위해 Graph 클래스가 제공됩니다. 그래프는 단락 수준의 요소이며 페이지 인스턴스의 Paragraphs 컬렉션에 추가될 수 있습니다. Graph 인스턴스는 도형의 컬렉션을 포함합니다.

[Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) 클래스가 지원하는 도형 유형은 다음과 같습니다:

- [Arc](/pdf/cpp/add-arc/) - 때때로 플래그라고도 불리며 인접한 두 정점의 순서쌍이지만 때로는 방향이 지정된 선이라고도 불립니다.

- [Circle](/pdf/cpp/add-circle/) - 데이터를 부채꼴로 나누어 원형으로 표시합니다. 우리는 원 그래프(파이 차트라고도 함)를 사용하여 데이터가 하나의 전체 또는 하나의 그룹을 나타내는 방법을 보여줍니다.
- [Curve](/pdf/cpp/add-curve/) - 프로젝트 선의 연결된 집합으로, 각 선은 일반적인 이중 점에서 세 개의 다른 선과 만납니다.
- [Line](/pdf/cpp/add-line) - 선 그래프는 연속적인 데이터를 표시하는 데 사용되며, 시간이 지남에 따라 추세를 보여줄 때 미래의 사건을 예측하는 데 유용할 수 있습니다.
- [Rectangle](/pdf/cpp/add-rectangle/) - 그래프에서 볼 수 있는 많은 기본 모양 중 하나로, 문제를 해결하는 데 매우 유용할 수 있습니다.
- [Ellipse](/pdf/cpp/add-ellipse/) - 평면 위의 점 집합으로, 타원형의 곡선 모양을 만듭니다.

위의 세부 사항은 아래 그림에서도 나타나 있습니다:

![Figures in Graphs](graph.png)
```
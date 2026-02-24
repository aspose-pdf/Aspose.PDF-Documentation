---
title: Python을 사용하여 PDF에서 그래프 작업
linktitle: 그래프 작업
type: docs
weight: 70
url: /ko/python-net/working-with-graphs/
description: 이 문서는 그래프가 무엇인지, 채워진 사각형 객체를 만드는 방법 및 기타 기능에 대해 설명합니다.
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 그래프 추가
Abstract: 이 문서는 Adobe Acrobat Writer 또는 유사한 PDF 처리 도구를 사용하는 개발자들에게 일반적인 요구사항인 PDF 문서에 그래프를 통합하는 방법을 논의합니다. .NET을 통한 Python용 Aspose.PDF의 Graph 클래스를 소개하며, 이 클래스를 통해 다양한 형태의 도형을 PDF 문서에 추가할 수 있습니다. Graph 클래스는 페이지 인스턴스의 Paragraphs 컬렉션에 추가할 수 있는 문단 수준 요소이며, Arc, Circle, Curve, Line, Rectangle, Ellipse 등 여러 도형을 지원하는 컬렉션을 포함합니다. 각 도형은 고유한 목적을 가지고 있으며, 예를 들어 Arc는 인접성을, Circle은 데이터 비율을, Curve는 연결된 선을, Line은 연속 데이터 추세를, Rectangle은 공간 문제를, Ellipse는 타원 형태를 나타냅니다. 이 문서는 이러한 도형들의 시각적 표현을 제공하여 이해를 돕습니다.
---

## 그래프란 무엇인가

PDF 문서에 그래프를 추가하는 것은 Adobe Acrobat Writer 또는 기타 PDF 처리 애플리케이션으로 작업하는 개발자에게 매우 일반적인 작업입니다. PDF 애플리케이션에서 사용할 수 있는 그래프 유형이 많이 있습니다.
[Aspose.PDF for Python via .NET](/pdf/python-net/)도 PDF 문서에 그래프 추가를 지원합니다. 이를 위해 Graph 클래스가 제공됩니다. Graph는 문단 수준 요소이며 페이지 인스턴스의 Paragraphs 컬렉션에 추가할 수 있습니다. Graph 인스턴스는 도형 컬렉션을 포함합니다.

다음 유형의 도형이 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 클래스에서 지원됩니다:

- [Arc](/pdf/python-net/add-arc/) - 때때로 플래그라고도 하며, 인접한 정점의 순서쌍이지만 때때로 방향선이라고도 합니다.
- [Circle](/pdf/python-net/add-circle/) - 데이터를 섹터로 나뉘어진 원으로 표시합니다. 우리는 원 그래프(파이 차트라고도 함)를 사용하여 데이터가 전체 또는 그룹의 일부를 나타내는 방식을 보여줍니다.
- [Curve](/pdf/python-net/add-curve/) - 각각의 선이 일반적인 이중점에서 다른 세 선과 만나며 연결된 사영선들의 결합입니다.
- [Line](/pdf/python-net/add-line) - 선 그래프는 연속 데이터를 표시하며 시간이 지남에 따라 추세를 보여줄 때 미래 이벤트를 예측하는 데 유용할 수 있습니다.
- [Rectangle](/pdf/python-net/add-rectangle/) - 그래프에서 볼 수 있는 여러 기본 도형 중 하나이며, 문제 해결에 매우 유용할 수 있습니다.
- [Ellipse](/pdf/python-net/add-ellipse/) - 평면상의 점 집합으로, 타원형 곡선을 형성합니다.

위의 내용은 아래 그림에서도 나타내고 있습니다:

![그래프의 그림](graphs.png)



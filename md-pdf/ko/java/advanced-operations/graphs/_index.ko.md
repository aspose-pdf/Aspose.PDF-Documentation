---
title: 그래프 작업하기
linktitle: 그래프 작업하기
type: docs
weight: 70
url: /java/graphs/
description: 이 문서는 그래프가 무엇인지, 채워진 사각형 객체를 생성하는 방법, 그래프 객체 안에 텍스트를 추가하는 방법, PDF에 선 객체를 추가하는 방법 등을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 그래프란 무엇인가

그래프의 주요 목적은 숫자 사실을 시각적 형태로 보여줌으로써 빠르고 쉽게 명확하게 이해할 수 있도록 하는 것입니다. 따라서 그래프는 수집된 데이터의 시각적 표현입니다. 데이터는 표의 형태로도 제시될 수 있지만, 그래픽 표현이 더 이해하기 쉽습니다. 특히 추세나 비교를 보여줘야 할 때 그렇습니다.

PDF 문서에 그래프를 추가하는 것은 Adobe Acrobat Writer나 다른 PDF 처리 응용 프로그램을 사용할 때 개발자들이 매우 흔하게 수행하는 작업입니다.
 PDF 애플리케이션에서 사용할 수 있는 그래프의 종류는 다양합니다. PDF 콘텐츠 스트림에서 사용되는 그래픽 연산자는 래스터 출력 장치에 재현될 페이지의 외관을 설명합니다.

[Aspose.PDF for Java](/pdf/java/)는 또한 PDF 문서에 그래프를 추가하는 것을 지원합니다. 이를 위해 Graph 클래스가 제공됩니다. Graph는 단락 수준의 요소이며 Page 인스턴스의 Paragraphs 컬렉션에 추가할 수 있습니다. Graph 인스턴스는 도형의 컬렉션을 포함합니다.

[Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) 클래스에 의해 지원되는 도형의 종류는 다음과 같습니다:

- [Arc](/pdf/java/add-arc/) - 때때로 플래그라고도 불리며 인접한 두 정점의 정렬된 쌍이지만 때로는 방향선이라고도 불립니다.
- [Circle](/pdf/java/add-circle/) - 섹터로 나뉜 원을 사용하여 데이터를 표시합니다. 우리는 원 그래프(파이 차트라고도 함)를 사용하여 데이터가 하나의 전체 또는 하나의 그룹을 어떻게 나타내는지 보여줍니다.

- [Curve](/pdf/java/add-curve/) - 각 선이 다른 세 개의 선과 일반적인 이중 점에서 만나는 사영선의 연결된 결합입니다.- [Line](/pdf/java/add-line) - 선 그래프는 연속적인 데이터를 표시하는 데 사용되며, 시간이 지남에 따라 트렌드를 보여줄 때 미래 사건을 예측하는 데 유용할 수 있습니다.
- [Rectangle](/pdf/java/add-rectangle/) - 그래프에서 볼 수 있는 많은 기본 도형 중 하나로, 문제를 해결하는 데 매우 유용할 수 있습니다.
- [Ellipse](/pdf/java/add-ellipse/) - 평면 위의 점 집합으로 타원형, 곡선 모양을 만듭니다.

위의 세부 사항은 아래 그림에서도 나타나 있습니다:

![Figures in Graphs](graph.png)
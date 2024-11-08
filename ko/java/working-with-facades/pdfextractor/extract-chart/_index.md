---
title: PDF 문서에서 차트 객체 추출하기 (facades)
type: docs
weight: 20
url: /ko/java/extract-chart-objects/
description: 이 섹션은 Aspose.PDF Facades를 사용하여 PdfExtractor 클래스로 PDF에서 차트 객체를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서에서 차트 객체 추출하기 (facades)

PDF는 페이지 콘텐츠를 **마크된 콘텐츠**라는 요소로 그룹화할 수 있게 합니다. Adobe Acrobat은 이를 "컨테이너"로 표시합니다. 차트 객체는 이러한 객체에 배치됩니다. 이러한 객체를 추출하기 위해 PdfExtractor 클래스에 새로운 메서드 extractMarkedContentAsImages()를 도입했습니다. 이 메서드는 모든 **마크된 콘텐츠**를 별도의 이미지로 렌더링합니다. 모든 차트가 하나의 컨테이너에 완전히 배치되지 않으므로 일부 차트는 부분적으로 별도의 이미지로 저장됩니다.

콘텐츠를 컨테이너로 올바르게 그룹화하는 것은 PDF 문서 디자이너의 책임임을 유의하시기 바랍니다.
 차트에 헤더나 다른 객체를 포함하고 싶다면 차트 전체가 하나의 컨테이너에 배치된 PDF 문서를 편집하거나 생성해야 합니다.

```java

// 문서 열기

Document document = new Document("sample.pdf");

// PdfExtractor 인스턴스화

PdfExtractor pdfExtractor = new PdfExtractor();

// 폴더에 차트 객체를 이미지로 추출

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();
```
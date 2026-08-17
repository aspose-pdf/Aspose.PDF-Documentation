---
title: Java를 사용하여 PDF 파일에서 벡터 데이터 추출
linktitle: PDF에서 벡터 데이터 추출
type: docs
weight: 80
url: /java/extract-vector-data-from-pdf/
description: Aspose.PDF를 사용하면 PDF 파일에서 벡터 데이터를 쉽게 추출할 수 있습니다. 위치, 직사각형 경계, SVG 출력과 같은 벡터 데이터를 얻을 수 있습니다.
lastmod: "2026-06-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## 
PDF 문서의 벡터 데이터에 액세스



`GraphicsAbsorber`을 사용하여 페이지의 벡터 그래픽 요소를 검사하고 해당 기본 형상을 텍스트 파일에 씁니다.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/)를 만들고 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 방문하여 벡터 그래픽 작업을 수집합니다.

1. 
추출된 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) 객체를 반복하고 해당 객체의 직사각형, 위치 및 연산자 컬렉션을 읽습니다.

1. 
각 요소에 대한 기하학 및 연산자 수 세부 정보를 사용하여 출력 텍스트를 작성합니다.

1. 
추출된 벡터 데이터를 출력 파일에 씁니다.


```java
public static void extractGraphicsElements(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder text = new StringBuilder();
        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            text.append("Element ").append(index)
                    .append(": Rectangle = ").append(element.getRectangle())
                    .append(", Position = ").append(element.getPosition())
                    .append(", Operators = ").append(element.getOperators().size())
                    .append("\n");
            index++;
        }
        Files.writeString(outputFile, text.toString());
    }
}
```

## 
페이지 벡터 그래픽을 SVG에 저장


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
문서에서 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 가져옵니다.

1. 
해당 페이지의 벡터 그래픽 콘텐츠를 SVG로 직접 내보내려면 `page.trySaveVectorGraphics(outputFile.toString())`을 호출하세요.


```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## 
추출된 각 요소를 별도의 SVG에 저장


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/)를 만들고 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 방문하세요.

1. 
파일을 쓰기 전에 추출된 하위 경로에 대한 출력 디렉터리를 만듭니다.

1. 
추출된 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) 개체를 반복하고 각 요소에 대해 `saveToSvg(...)`을 호출합니다.

1. 
추출된 모든 요소를 별도의 SVG 파일에 저장합니다.


```java
public static void extractSubpathsToSvgs(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        Path subpathsDir = outputDir.resolve("subpaths");
        Files.createDirectories(subpathsDir);

        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            element.saveToSvg(subpathsDir.resolve("subpath_" + index + ".svg").toString());
            index++;
        }
    }
}
```

## 
추출된 요소를 단일 SVG로 결합


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/)를 만들고 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 방문하세요.

1. 
결합된 벡터 조각을 포함할 SVG 래퍼 마크업을 만듭니다.

1. 
추출된 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) 객체를 반복하고 생성된 각 SVG 조각을 추가합니다.

1. 
결합된 SVG 출력을 대상 파일에 씁니다.


```java
public static void extractListOfElementsToSingleImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder svg = new StringBuilder();
        svg.append("<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
        for (GraphicElement element : absorber.getElements()) {
            svg.append(element.saveToSvg()).append("\n");
        }
        svg.append("</svg>\n");
        Files.writeString(outputFile, svg.toString());
    }
}
```

## 
단일 벡터 요소 추출


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/)를 만들고 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 방문하세요.

1. 
추출된 요소 컬렉션에서 필수 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/)를 가져옵니다.

1. 
선택한 요소가 [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/)인지 확인하고 필요한 경우 중첩된 요소로 내려갑니다.

1. 
선택한 벡터 요소를 출력 SVG 파일에 저장합니다.

```java
public static void extractSingleVectorElement(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        Page page = document.getPages().get_Item(1);
        graphicsAbsorber.visit(page);
        if (graphicsAbsorber.getElements().size() > 1) {
            GraphicElement xformPlacement = graphicsAbsorber.getElements().get_Item(1);
            if (xformPlacement instanceof XFormPlacement) {
                XFormPlacement placement = (XFormPlacement) xformPlacement;
                if (placement.getElements().size() > 2) {
                    placement.getElements().get_Item(2).saveToSvg(outputFile.toString());
                }
            } else {
                xformPlacement.saveToSvg(outputFile.toString());
            }
        }
    }
}
```

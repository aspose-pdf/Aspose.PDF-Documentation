---
title: Java에서 벡터 그래픽 작업
linktitle: 벡터 그래픽 작업
type: docs
weight: 100
url: /java/working-with-vector-graphics/
description: Java를 사용하여 PDF 문서에서 벡터 그래픽을 추출, 이동, 제거, 복사 및 내보내는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: GraphicsAbsorber를 사용하여 Java에서 PDF 벡터 그래픽을 검사하고 조작하십시오.
Abstract: 이 문서에서는 GraphicsAbsorber 클래스를 사용하여 Java용 Aspose.PDF에서 벡터 그래픽으로 작업하는 방법을 설명합니다. 페이지의 벡터 요소를 검사하고, 이동 또는 제거하고, 페이지 간에 그래픽을 복사하고, 벡터 콘텐츠를 SVG로 내보내는 방법을 알아보세요.
---
Java용 Aspose.PDF는 `GraphicsAbsorber` 및 `GraphicElement` 개체를 통해 벡터 콘텐츠를 노출합니다. 이를 통해 페이지의 하위 수준 벡터 요소를 검사한 다음 이를 업데이트, 제거, 복사 또는 내보낼 수 있습니다.


## 
페이지의 벡터 그래픽 검사



벡터 요소를 열거하고 해당 페이지, 위치 및 연산자 수를 검사해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/)를 만들고 대상 페이지를 방문하세요.
1. 흡수된 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) 개체를 반복하고 해당 속성을 출력합니다.


```java
public static void usingGraphicsAbsorber(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                System.out.println("Page Number: " + element.getSourcePage().getNumber());
                System.out.println("Position: (" + element.getPosition().getX() + ", "
                        + element.getPosition().getY() + ")");
                System.out.println("Number of Operators: " + element.getOperators().size());
            }
        } finally {
            graphicsAbsorber.dispose();
        }
    }
}
```

## 
페이지에서 벡터 그래픽 이동



감지된 모든 벡터 요소를 새 위치로 이동해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/)를 사용하여 대상 페이지를 방문하고 일시적으로 업데이트를 억제하세요.
1. 흡수된 각 요소의 위치를 ​​변경하고, 업데이트를 재개하고, 문서를 저장합니다.


```java
public static void moveGraphics(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                Point position = element.getPosition();
                element.setPosition(new Point(position.getX() + 150, position.getY() - 10));
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics moved in " + outputFile);
}
```

## 
요소 제거를 통해 위치별 벡터 그래픽 제거



특정 직사각형 내부의 벡터 요소를 하나씩 삭제해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/)가 있는 페이지를 방문하여 대상 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)을 정의하세요.
1. 일치하는 요소를 제거하고 업데이트를 재개하고 문서를 저장합니다.


```java
public static void removeGraphicsMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    element.remove();
                }
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 1 in " + outputFile);
}
```

## 
컬렉션을 삭제하여 벡터 그래픽 제거



일치하는 벡터 요소를 먼저 수집한 다음 한 번의 페이지 작업으로 제거해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) 페이지를 방문하여 일치하는 요소를 수집하세요.
1. 페이지 콘텐츠에서 수집된 그래픽을 삭제하고 업데이트된 문서를 저장합니다.


```java
public static void removeGraphicsMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            GraphicElementCollection removedElements = new GraphicElementCollection();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    removedElements.add(element);
                }
            }
            page.getContents().suppressUpdate();
            page.deleteGraphics(removedElements);
            page.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 2 in " + outputFile);
}
```

## 
벡터 그래픽을 요소별로 다른 페이지 요소에 복사



흡수된 각 벡터 요소를 새 페이지에 개별적으로 추가해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 대상 페이지를 추가합니다.

1. 
[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/)를 사용하여 소스 페이지를 방문하세요.
1. 대상 페이지에 각 [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/)를 추가하고 문서를 저장합니다.


```java
public static void addToAnotherPageMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                element.addOnPage(page2);
            }
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 1 in " + outputFile);
}
```

## 
벡터 그래픽을 컬렉션으로 다른 페이지에 복사



한 번의 호출로 전체 흡수된 벡터 그래픽 컬렉션을 새 페이지에 복사해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 대상 페이지를 추가합니다.

1. 
[GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/)를 사용하여 소스 페이지를 방문하세요.
1. 흡수된 그래픽 컬렉션을 대상 페이지에 추가하고 문서를 저장합니다.

```java
public static void addToAnotherPageMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            page2.addGraphics(graphicsAbsorber.getElements());
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 2 in " + outputFile);
}
```

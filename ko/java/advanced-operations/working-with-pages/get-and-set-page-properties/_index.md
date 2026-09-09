---
title: Java에서 PDF 페이지 속성 가져오기 및 설정
linktitle: 페이지 속성 가져오기 및 설정
type: docs
weight: 90
url: /java/get-and-set-page-properties/
description: Java에서 개수, 상자, 회전 및 색상 정보와 같은 PDF 페이지 속성을 검사하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일의 페이지 수, 상자 및 색상 유형을 검사합니다.
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 페이지 속성을 검사하는 방법을 설명합니다. 페이지 수 읽기, 단락 생성 및 저장 전 결과 수 확인, 모든 주요 페이지 상자 값 인쇄 및 각 페이지의 색상 유형 식별에 대해 설명합니다.
---
Aspose.PDF for Java는 페이지 수, 페이지 상자, 회전 및 페이지 색상 유형을 검사할 수 있습니다.


## 
페이지 수를 가져옵니다



PDF의 총 페이지 수를 읽어야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 컬렉션의 크기를 읽습니다.
1. 총 페이지 수를 출력합니다.


```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## 
저장하기 전에 페이지 수를 확인하세요



파일을 쓰기 전에 생성된 컨텐츠가 생성되는 페이지 수를 알아야 할 때 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지에 콘텐츠를 추가하세요.

1. 
레이아웃 계산을 강제하기 위해 단락을 처리합니다.
1. 결과 페이지 수를 읽고 출력합니다.


```java
public static void getPageCountWithoutSaving(Path inputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        for (int i = 0; i < 300; i++) {
            page.getParagraphs().add(new TextFragment("Pages count test"));
        }
        document.processParagraphs();
        System.out.println("Number of pages in document = " + document.getPages().size());
    }
}
```

## 
페이지 상자 속성 가져오기



모든 주요 상자 크기와 페이지 회전 값을 검사해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 대상 페이지에 접속합니다.

1. 
페이지 상자 값을 맵으로 수집합니다.
1. 치수 및 페이지 회전 정보를 출력합니다.


```java
public static void getPageProperties(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        Map<String, Rectangle> boxes = new LinkedHashMap<>();
        boxes.put("ArtBox", page.getArtBox());
        boxes.put("BleedBox", page.getBleedBox());
        boxes.put("CropBox", page.getCropBox());
        boxes.put("MediaBox", page.getMediaBox());
        boxes.put("TrimBox", page.getTrimBox());
        boxes.put("Rect", page.getRect());

        for (Map.Entry<String, Rectangle> entry : boxes.entrySet()) {
            Rectangle box = entry.getValue();
            System.out.println(entry.getKey() + " : Height=" + box.getHeight()
                    + ",Width=" + box.getWidth()
                    + ",LLX=" + box.getLLX()
                    + ",LLY=" + box.getLLY()
                    + ",URX=" + box.getURX()
                    + ",URY=" + box.getURY());
        }

        System.out.println("Page Number : " + page.getNumber());
        System.out.println("Rotate : " + page.getRotate());
    }
}
```

## 
각 페이지의 색상 유형을 가져옵니다.



페이지가 흑백, 회색조 또는 RGB인지 식별해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
모든 페이지를 반복하고 각 페이지 [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/)을 읽습니다.
1. 열거형 값을 읽을 수 있는 텍스트로 변환하고 결과를 출력합니다.

```java
public static void getPageColorType(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            ColorType pageColorType = document.getPages().get_Item(pageNumber).getColorType();
            String colorDescription = switch (pageColorType) {
                case BlackAndWhite -> "Black and white";
                case Grayscale -> "Gray Scale";
                case Rgb -> "RGB";
                case Undefined -> "undefined";
            };
            System.out.println("Page # " + pageNumber + " is " + colorDescription + ".");
        }
    }
}
```

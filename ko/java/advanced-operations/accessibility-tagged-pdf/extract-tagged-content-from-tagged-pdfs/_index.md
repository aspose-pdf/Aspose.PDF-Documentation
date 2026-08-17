---
title: Java의 PDF에서 태그된 콘텐츠 추출
linktitle: 태그된 콘텐츠 추출
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: 태그된 콘텐츠 액세스, 루트 구조 액세스 및 하위 구조 요소를 포함하여 Aspose.PDF를 사용하여 Java에서 태그된 PDF 콘텐츠를 검사하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

태그가 지정된 PDF의 논리 구조 트리를 검사하고 구조 요소 메타데이터를 검사하거나 업데이트해야 할 때 이러한 API를 사용하십시오.


## 
태그된 콘텐츠 메타데이터 가져오기



태그가 지정된 콘텐츠 컨테이너에 액세스해야 하고 제목, 언어 등 기본 문서 메타데이터를 정의하려는 경우 이 예를 사용하세요.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에서 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) 개체를 가져옵니다.

1. 
태그가 지정된 콘텐츠 메타데이터를 설정하고 출력 파일을 저장합니다.


```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## 
태그가 있는 PDF의 루트 구조 가져오기



이 예에서는 태그가 지정된 PDF의 구조 트리를 나타내는 루트 개체를 검사하는 방법을 보여줍니다.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 태그된 콘텐츠를 가져옵니다.

1. 
필요한 문서 메타데이터를 설정합니다.

1. 
구조 트리 루트 및 논리 루트 요소를 읽고 인쇄한 다음 파일을 저장합니다.


```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## 
하위 구조 요소에 액세스하고 업데이트합니다.



구조 트리의 하위 요소를 반복하고 해당 속성을 검사하고 선택한 메타데이터를 업데이트해야 하는 경우 이 예를 사용합니다.


1. 
PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 태그가 붙은 소스를 엽니다.

1. 
구조 트리 루트에서 하위 요소를 읽고 사용 가능한 속성을 인쇄합니다.

1. 
첫 번째 루트 하위 요소의 하위 요소에 액세스하고 해당 메타데이터를 업데이트하고 문서를 저장합니다.

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```

---
title: Java를 사용하여 주석 가져오기 및 내보내기
linktitle: 주석 가져오기 및 내보내기
type: docs
weight: 80
url: /java/pdfannotationeditor-class/import-export-annotations/
description: Java를 사용하여 한 PDF 문서의 주석을 다른 PDF 문서로 복사하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java 문서 간에 PDF 주석 전송
Abstract: 이 문서에서는 소스 PDF에서 주석을 복사하고 Java를 사용하여 새 PDF 문서로 내보내는 방법을 설명합니다. 워크플로는 소스 파일을 로드하고, 대상 문서를 만들고, 페이지를 추가하고, 첫 번째 소스 페이지에서 주석을 복사하고, 결과를 저장합니다.
---
## 
한 PDF에서 다른 PDF로 주석 복사


1. 
소스 PDF를 열고 대상 페이지가 포함된 새 대상 문서를 만듭니다.

2. 
첫 번째 소스 페이지의 주석을 열거하고 각 주석을 대상 페이지에 추가합니다.

3. 
복사된 주석을 유지하려면 대상 문서를 저장하세요.

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```

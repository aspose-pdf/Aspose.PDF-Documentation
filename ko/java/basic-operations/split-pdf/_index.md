---
title: Java에서 PDF 파일 분할
linktitle: PDF 파일 분할
type: docs
weight: 60
url: /java/split-pdf/
description: Aspose.PDF를 사용하여 Java에서 PDF를 단일 페이지 PDF 파일로 분할하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 페이지 분할
Abstract: 이 문서에서는 Aspose.PDF를 사용하여 Java에서 PDF 문서를 별도의 단일 페이지 PDF 파일로 분할하는 방법을 보여줍니다. 이 예제에서는 소스 문서를 열고, 해당 페이지를 반복하고, 각 페이지에 대해 새 문서를 만들고, 각 페이지를 개별 PDF 파일로 저장합니다.
---
검토, 저장 또는 다운스트림 처리를 위해 각 페이지를 내보내야 할 때 PDF를 별도의 파일로 분할하는 것이 유용합니다.


## 
실제 사례



[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter)는 브라우저에서 PDF 분할을 테스트하기 위한 무료 온라인 애플리케이션입니다.



[![PDF 분할 분할](splitter.png)](https://products.aspose.app/pdf/splitter)



이 예제에서는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 클래스를 사용하여 PDF 파일을 열고 해당 페이지를 반복합니다. 각 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 대해 새 문서를 생성하고 여기에 페이지를 추가한 후 결과를 별도의 PDF 파일로 저장합니다.

Java에서 PDF를 개별 페이지 파일로 분할하려면:


1. 
[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자를 사용하여 소스 PDF를 엽니다.

1. 
`document.getPages()`에서 반환된 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 개체를 반복합니다.

1. 
각 페이지마다 빈 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 새로 만듭니다.

1. 
현재 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 새 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)에 추가합니다.
1. 새 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 고유한 파일 이름으로 저장하세요.

1. 
처리가 완료되면 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 모두 닫습니다.


## 
PDF를 단일 페이지 파일로 분할



다음 Java 예제는 `SplitDocumentExamples.java`을 기반으로 하며 페이지를 `Page_1.pdf`, `Page_2.pdf` 등으로 저장합니다.

```java
public static void splitDocument(Path inputFile, Path outputDir) {
    Document document = new Document(inputFile.toString());
    try {
        int pageCount = 1;
        for (Page page : document.getPages()) {
            Document newDocument = new Document();
            try {
                newDocument.getPages().add(page);
                newDocument.save(outputDir.resolve("Page_" + pageCount + ".pdf").toString());
            } finally {
                newDocument.close();
            }
            pageCount++;
        }
    } finally {
        document.close();
    }
}
```

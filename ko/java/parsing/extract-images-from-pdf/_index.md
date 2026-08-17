---
title: Java를 사용하여 PDF에서 이미지 추출
linktitle: PDF에서 이미지 추출
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: Aspose.PDF for Java를 사용하여 PDF 파일에서 포함된 이미지를 추출하는 방법을 알아보세요.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 통해 PDF에서 이미지를 추출하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 포함된 이미지를 추출하는 방법을 설명합니다. 소스 PDF를 열고, 페이지 리소스 컬렉션의 이미지에 액세스하고, 추출된 XImage를 외부 파일에 저장하는 방법을 보여줍니다.
---

포함된 그래픽을 재사용하거나, 문서 자산을 검사하거나, 다운스트림 처리를 위해 이미지를 내보내야 하는 경우 PDF 페이지에서 이미지를 추출하세요.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 열고 추출된 이미지 파일의 출력 스트림을 엽니다.

1. 
문서에서 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 가져오고 해당 `Resources.Images` 컬렉션에 액세스합니다.

1. 
해당 이미지 컬렉션에서 필요한 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) 개체를 인덱스별로 검색합니다.

1. 
`image.save(outputImage)`을 호출하여 추출된 이미지 바이트를 대상 스트림에 씁니다.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

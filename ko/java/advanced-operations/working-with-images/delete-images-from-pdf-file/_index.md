---
title: Java를 사용하여 PDF 파일에서 이미지 삭제
linktitle: 이미지 삭제
type: docs
weight: 20
url: /ko/java/delete-images-from-pdf-file/
description: Java에서 PDF 파일에 포함된 이미지를 삭제하는 방법을 알아보세요.
lastmod: "2026-09-24"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 포함된 이미지 삭제
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 이미지를 삭제하는 방법을 보여줍니다. 이 예제에서는 페이지 이미지 컬렉션의 인덱스를 기준으로 첫 번째 페이지에서 이미지 리소스를 제거한 다음 수정된 문서를 저장합니다.
---
PDF 페이지에 포함된 이미지를 제거해야 하는 경우 페이지 이미지 리소스 컬렉션을 사용하세요.

## 인덱스별로 포함된 이미지 삭제

1. 원본 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 여세요.
1. 대상 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)의 이미지 리소스에 접근하세요.
1. 해당 인덱스를 기준으로 페이지 리소스 컬렉션에서 대상 이미지를 삭제하세요.
1. 업데이트된 PDF [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장하세요.

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```

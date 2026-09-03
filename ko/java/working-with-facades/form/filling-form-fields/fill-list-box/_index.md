---
title: 목록 상자 채우기
linktitle: 목록 상자 채우기
type: docs
weight: 40
url: /java/fill-list-box/
description: Aspose.PDF의 Form Facade를 사용하여 Java로 PDF 양식의 목록 상자 필드를 채우는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 양식에서 목록 상자 필드 값 설정
Abstract: 이 문서에서는 PDF 양식을 바인딩하고, 목록 상자 필드 값을 설정하고, Java용 Aspose.PDF에서 양식 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
목록 상자 필드를 채우려면 `FormExamples.fillListBoxFields(...)`을 사용하십시오.

```java
public static void fillListBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("favorite_colors", "Red");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

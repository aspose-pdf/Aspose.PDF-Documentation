---
title: 바코드 필드 채우기
linktitle: 바코드 필드 채우기
type: docs
weight: 50
url: /java/fill-barcode-fields/
description: Aspose.PDF의 Form Facade를 사용하여 Java에서 바코드 양식 필드를 채우는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java로 PDF 양식의 바코드 필드 채우기
Abstract: 이 문서에서는 PDF 양식을 바인딩하고, 바코드 필드 값을 설정하고, Java용 Aspose.PDF에서 양식 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

`FormExamples.fillBarcodeFields(...)`을 사용하여 PDF 양식의 바코드 필드를 채웁니다.

```java
public static void fillBarcodeFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillBarcodeField("product_barcode", "123456789012");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

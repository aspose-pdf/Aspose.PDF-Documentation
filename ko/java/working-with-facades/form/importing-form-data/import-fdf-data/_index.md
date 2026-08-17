---
title: FDF 데이터 가져오기
linktitle: FDF 데이터 가져오기
type: docs
weight: 10
url: /java/import-fdf-data/
description: Aspose.PDF의 Form Facade를 사용하여 Java를 사용하여 FDF 양식 데이터를 PDF 양식으로 가져오는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java의 FDF에서 AcroForm 데이터 가져오기
Abstract: 이 문서에서는 PDF 양식을 바인딩하고, FDF 스트림에서 필드 값을 가져오고, Java용 Aspose.PDF에서 양식 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

FDF 파일의 필드 값을 적용하려면 `FormExamples.importFdf(...)`을 사용하십시오.

```java
public static void importFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

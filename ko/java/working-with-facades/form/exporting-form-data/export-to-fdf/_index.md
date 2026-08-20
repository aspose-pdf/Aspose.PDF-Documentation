---
title: FDF로 내보내기
linktitle: FDF로 내보내기
type: docs
weight: 10
url: /java/export-to-fdf/
description: Aspose.PDF의 Form Facade를 사용하여 PDF 양식 필드 값을 Java의 FDF로 내보내는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: AcroForm 데이터를 Java의 FDF로 내보내기
Abstract: 이 문서에서는 PDF 양식을 바인딩하고 해당 필드 데이터를 Java용 Aspose.PDF의 Form 파사드를 사용하여 FDF 스트림으로 내보내는 방법을 보여줍니다.
---
AcroForm 필드 데이터를 FDF로 직렬화해야 하는 경우 `FormExamples.exportFdf(...)`을 사용하십시오.

```java
public static void exportFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(outputStream);
    } finally {
        form.close();
    }
}
```

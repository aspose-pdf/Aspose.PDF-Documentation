---
title: XFDF로 내보내기
linktitle: XFDF로 내보내기
type: docs
weight: 20
url: /java/export-to-xfdf/
description: Aspose.PDF의 Form Facade를 사용하여 PDF 양식 필드 데이터를 Java의 XFDF로 내보내는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: AcroForm 데이터를 Java의 XFDF로 내보내기
Abstract: 이 문서에서는 PDF 양식을 바인딩하고 해당 필드 값을 Java용 Aspose.PDF의 Form 파사드를 사용하여 XFDF 스트림으로 내보내는 방법을 보여줍니다.
---

양식 필드 데이터를 XFDF로 쓰려면 `FormExamples.exportXfdf(...)`을 사용하십시오.

```java
public static void exportXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(outputStream);
    } finally {
        form.close();
    }
}
```

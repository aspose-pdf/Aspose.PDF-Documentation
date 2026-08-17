---
title: XML로 내보내기
linktitle: XML로 내보내기
type: docs
weight: 40
url: /java/export-to-xml/
description: Aspose.PDF의 Form 파사드를 사용하여 Java에서 PDF 양식 데이터를 XML로 내보내는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: AcroForm 데이터를 Java의 XML로 내보내기
Abstract: 이 문서에서는 PDF 양식을 바인딩하고 해당 필드 값을 Java용 Aspose.PDF의 Form 파사드를 사용하여 XML 스트림으로 내보내는 방법을 보여줍니다.
---

양식 필드 데이터를 XML로 저장하려면 `FormExamples.exportXml(...)`을 사용하세요.

```java
public static void exportXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(outputStream);
    } finally {
        form.close();
    }
}
```

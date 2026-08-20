---
title: Заполнить поля флажков
linktitle: Заполнить поля флажков
type: docs
weight: 20
url: /ru/java/fill-check-box-fields/
description: Узнайте, как заполнять поля флажков в PDF‑форме с помощью Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Установите значения полей флажков в PDF‑форме с помощью Java
Abstract: В этой статье показано, как привязать PDF‑форму, установить поля флажков по имени и сохранить обновлённый документ, используя фасад Form в Aspose.PDF for Java.
---
Использовать `FormExamples.fillCheckBoxFields(...)` установить значения флажков в форме.

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```



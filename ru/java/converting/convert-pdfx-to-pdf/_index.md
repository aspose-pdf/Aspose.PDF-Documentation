---
title: Преобразовать PDF/A и PDF/UA в PDF на Java
linktitle: Преобразовать PDF/A и PDF/UA в PDF
type: docs
weight: 120
url: /ru/java/convert-pdf_x-to-pdf/
lastmod: "2026-08-19"
description: Узнайте, как удалить соответствие PDF/A и PDF/UA из основанных на стандартах PDF‑файлов в Java и сохранить их как стандартные PDF‑документы.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как преобразовать PDF/A и PDF/UA в стандартный PDF на Java
Abstract: В этой статье объясняется, как удалить соответствие PDF/A и PDF/UA из основанных на стандартах PDF‑документов с помощью Aspose.PDF for Java, а затем сохранить результат как стандартный PDF‑файл.
---
Aspose.PDF for Java может преобразовать варианты PDF, соответствующие стандартам, обратно в обычный PDF‑документ.

## Преобразуйте PDF/A в стандартный PDF

Используйте этот пример, когда архивный документ PDF/A необходимо понизить до стандартного PDF.

1. Откройте исходный файл PDF/A в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Вызовите `removePdfaCompliance()` отсоединить профиль архивного соответствия от загруженного документа.
1. Сохраните полученный стандартный PDF‑файл без установленного ограничения PDF/A.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## Преобразуйте PDF/UA в стандартный PDF

Используйте этот пример, когда доступный документ PDF/UA должен быть преобразован обратно в стандартный PDF.

1. Откройте исходный файл PDF/UA в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Вызовите `removePdfUaCompliance()` удалить профиль соответствия требованиям доступности из метаданных документа и требований к структуре.
1. Сохраните полученный PDF‑документ как обычный PDF‑файл.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```



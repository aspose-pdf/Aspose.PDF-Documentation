---
title: Преобразование PDF/A и PDF/UA в PDF с помощью Java
linktitle: Преобразование PDF/A и PDF/UA в PDF
type: docs
weight: 120
url: /ru/java/convert-pdf_x-to-pdf/
lastmod: "2026-09-16"
description: Узнайте, как удалить соответствие PDF/A и PDF/UA из основанных на стандартах PDF‑файлов с помощью Java и сохранить их как стандартные PDF‑документы.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать PDF/A и PDF/UA в стандартный PDF с помощью Java
Abstract: В этой статье объясняется, как удалить соответствие PDF/A и PDF/UA из основанных на стандартах PDF‑документов с использованием Aspose.PDF for Java, а затем сохранить результат как стандартный PDF‑файл.
---
Aspose.PDF for Java может конвертировать соответствующие стандартам варианты PDF обратно в обычный PDF‑документ.

## Преобразование PDF/A в обычный PDF

Используйте этот пример, когда архивный документ PDF/A необходимо преобразовать в обычный PDF.

1. Откройте исходный файл PDF/A в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите `removePdfaCompliance()`, чтобы снять соответствие архивному стандарту с загруженного документа.
1. Сохраните полученный стандартный PDF‑файл без установленного ограничения PDF/A.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## Преобразование PDF/UA в обычный PDF

Используйте этот пример, когда доступный документ PDF/UA необходимо преобразовать обратно в стандартный PDF.

1. Откройте исходный файл PDF/UA в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите `removePdfUaCompliance()`, чтобы снять соответствие стандарту доступности из метаданных документа и требований к его структуре.
1. Сохраните полученный PDF‑документ как обычный PDF‑файл.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```

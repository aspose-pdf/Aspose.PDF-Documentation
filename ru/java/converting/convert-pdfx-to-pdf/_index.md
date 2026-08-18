---
title: Преобразование PDF/A и PDF/UA в PDF в Java
linktitle: Конвертируйте PDF/A и PDF/UA в PDF
type: docs
weight: 120
url: /java/convert-pdf_x-to-pdf/
lastmod: "2026-06-16"
description: Узнайте, как удалить соответствие PDF/A и PDF/UA из стандартных PDF-файлов на Java и сохранить их как стандартные PDF-документы.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать PDF/A и PDF/UA в стандартный PDF в Java
Abstract: В этой статье объясняется, как удалить соответствие PDF/A и PDF/UA из PDF-документов, основанных на стандартах, с помощью Aspose.PDF для Java, а затем сохранить результат как стандартный PDF-файл.
---
Aspose.PDF для Java может конвертировать соответствующие стандартам варианты PDF обратно в обычный PDF-документ.

## Конвертируйте PDF/A в стандартный PDF

Используйте этот пример, когда архивный документ PDF/A необходимо понизить до стандартного PDF.

1. Откройте исходный файл PDF/A в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвоните `removePdfaCompliance()`, чтобы отсоединить профиль соответствия архивации от загруженного документа.
1. Сохраните полученный стандартный PDF-файл без установленных ограничений PDF/A.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## Конвертируйте PDF/UA в стандартный PDF

Используйте этот пример, когда доступный документ PDF/UA необходимо преобразовать обратно в стандартный PDF.

1. Откройте исходный файл PDF/UA в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвоните `removePdfUaCompliance()`, чтобы удалить профиль соответствия доступности из требований к метаданным и структуре документа.
1. Save the resulting PDF document as a regular PDF file.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```

---
title: Объединение нескольких PDF‑файлов
linktitle: Объединение нескольких PDF‑файлов
type: docs
weight: 20
url: /ru/java/concatenate-pdf-files/
description: Объединить PDF‑файлы в Java с помощью конкатенации на основе массива в PdfFileEditor.
lastmod: "2026-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединить несколько PDF‑файлов в один документ с помощью Java
Abstract: Узнайте, как конкатенировать PDF‑файлы с помощью Aspose.PDF for Java. Пример из репозитория использует перегрузку `concatenate`, основанную на массиве, с двумя входными файлами, и тот же рабочий процесс можно расширить для более длинных списков файлов, поскольку метод принимает массив строк с путями к источникам.
---
## Объединение PDF‑файлов

Пример на Java объединяет два файла с помощью перегрузки `concatenate`, которая принимает массив.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Создайте массив строк с путями входных PDF.
3. Вызовите `concatenate` с входным массивом и путем к выходному файлу.
4. Сохраните объединённый документ.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

Чтобы объединить более двух файлов, расширьте массив строк, передаваемый в `concatenate`.



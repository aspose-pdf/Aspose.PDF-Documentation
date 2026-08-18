---
title: Объединение нескольких PDF-файлов
linktitle: Объединение нескольких PDF-файлов
type: docs
weight: 20
url: /java/concatenate-pdf-files/
description: Объединяйте PDF-файлы в Java с помощью рабочего процесса объединения PdfFileEditor на основе массива.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединение нескольких PDF-файлов в один документ с помощью Java
Abstract: Узнайте, как объединить PDF-файлы с помощью Aspose.PDF для Java. В примере репозитория используется перегрузка `concatenate` на основе массива с двумя входными данными, и тот же рабочий процесс можно расширить для более длинных списков файлов, поскольку метод принимает строковый массив исходных путей.
---
## Объединение PDF-файлов

Пример Java объединяет два файла, передавая их перегрузке `concatenate` на основе массива.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Создайте массив строк с входными путями PDF.
3. Вызовите `concatenate`, указав входной массив и путь к выходному файлу.
4. Сохраните объединенный документ.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

Чтобы объединить более двух файлов, расширьте массив строк, переданный в `concatenate`.

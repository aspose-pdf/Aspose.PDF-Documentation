---
title: Оптимизация PDF-файлов в Java
linktitle: Оптимизировать PDF
type: docs
weight: 30
url: /java/optimize-pdf/
description: Узнайте, как оптимизировать, сжимать и уменьшать размер PDF-файла в Java с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сжимайте ресурсы PDF и уменьшайте размер файла с помощью Java
Abstract: В этой статье объясняется, как оптимизировать PDF-файлы с помощью Aspose.PDF для Java. Он охватывает оптимизацию всего документа, сжатие ресурсов, снижение качества изображения, удаление неиспользуемых объектов и потоков, связывание повторяющихся потоков, извлечение шрифтов, выравнивание аннотаций и форм, преобразование в оттенки серого и сжатие изображений Flate.
---
Aspose.PDF для Java предоставляет функции оптимизации через `Document.optimize`, `optimizeResources` и `OptimizationOptions`.

## Оптимизация PDF с помощью общей оптимизации документа

Используйте этот пример, если вы хотите, чтобы Aspose.PDF применил встроенную процедуру оптимизации всего документа.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвоните `optimize()` по документу.
1. Сохраните оптимизированный файл и сравните исходный и выходной размеры.

```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Уменьшите размер PDF за счет оптимизации ресурсов

В этом примере основное внимание уделяется оптимизации на уровне ресурсов без ручной настройки отдельных параметров.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Запустите `optimizeResources()`, чтобы оптимизировать внутренние ресурсы.
1. Сохраните результат и распечатайте размеры входного и выходного файла.

```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Сжать все изображения в PDF

Используйте этот подход, когда документы с большим количеством изображений требуют меньшего размера файла и некоторое снижение качества изображения приемлемо.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) и включите сжатие изображений с необходимым уровнем качества.
1. Оптимизируйте ресурсы документа с помощью этих настроек.
1. Сохраните оптимизированный файл и сравните размеры файлов.

```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Удаление неиспользуемых объектов из PDF-файла

В этом примере удаляются неиспользуемые объекты, которые могут остаться в структуре документа после редактирования или слияния.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) и включите удаление неиспользуемых объектов.
1. Оптимизируйте ресурсы и сохраните обновленный файл.
1. Распечатайте файлы исходного и уменьшенного размера.

```java
public static void removingUnusedObjects(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedObjects(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Удалите неиспользуемые потоки из PDF-файла

Используйте этот подход, если вы хотите удалить данные потока, на которые больше не ссылается документ.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Настройте [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/), чтобы удалить неиспользуемые потоки.
1. Оптимизируйте ресурсы, сохраните выходной документ и сравните размеры файлов.

```java
public static void removingUnusedStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Свяжите повторяющиеся потоки в PDF-файле

В этом примере выполняется дедупликация повторяющихся потоков, поэтому идентичный контент может быть сохранен только один раз.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) и включите привязку дубликатов потоков.
1. Оптимизируйте ресурсы, сохраните выходной документ и распечатайте размеры файлов.

```java
public static void linkingDuplicateStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setLinkDuplicateStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Извлеките шрифты из PDF-файла

Используйте эту опцию, если уменьшение размера файла более важно, чем сохранение встроенных данных шрифта в выходных данных.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Настройте [Параметры оптимизации](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) для извлечения шрифтов.
1. Оптимизируйте ресурсы, сохраните документ и сравните размеры файлов.

```java
public static void unembedFonts(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setUnembedFonts(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Сведение аннотаций в PDF-файле

В этом примере аннотации преобразуются в статическое содержимое страницы, поэтому они больше не остаются интерактивными объектами.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите каждую [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и ее коллекцию [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/).
1. Сгладьте каждую аннотацию и сохраните обновленный документ.

```java
public static void flattenAnnotations(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            for (Annotation annotation : page.getAnnotations()) {
                annotation.flatten();
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Сведение полей формы PDF

Используйте этот подход, когда заполняемые поля формы должны стать фиксированным содержимым перед распространением или архивированием.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Проверьте, содержит ли документ виджеты форм.
1. Сгладьте каждое [Поле](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/), представленное [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Сохраните выходной файл и распечатайте размеры файла.

```java
public static void flattenForms(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Преобразование PDF в оттенки серого

В этом примере каждая страница преобразуется в оттенки серого, что может помочь уменьшить сложность цветопередачи и стандартизировать выходные данные для рабочих процессов архивирования или печати.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебрать каждую [страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документе.
1. Вызовите `makeGrayscale()` на каждой странице и сохраните выходной файл.

```java
public static void convertPdfFromRgbColorspaceToGrayscale(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.makeGrayscale();
        }
        document.save(outputFile.toString());
    }
}
```

## Используйте сжатие изображений FlateDecode

Используйте этот шаблон, если хотите применить к изображениям сжатие на основе Flate во время оптимизации ресурсов PDF.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) и установите кодировку изображения [ImageEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`.
1. Оптимизируйте ресурсы документа и сохраните выходной файл.

```java
public static void usingFlatedecodeCompression(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizationOptions = new OptimizationOptions();
        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);
        document.optimizeResources(optimizationOptions);
        document.save(outputFile.toString());
    }
}
```

## Печать оригинальных и оптимизированных размеров файлов

Этот вспомогательный метод сообщает о разнице в размерах исходного файла и оптимизированного выходного файла.

1. Прочитайте размер входного файла.
1. Прочтите размер выходного файла.
1. Распечатайте оба значения в одном сообщении о состоянии.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```

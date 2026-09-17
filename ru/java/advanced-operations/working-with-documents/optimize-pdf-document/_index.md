---
title: Оптимизация PDF-файлов в Java
linktitle: Оптимизация PDF
type: docs
weight: 30
url: /ru/java/optimize-pdf/
description: Узнайте, как оптимизировать, сжать и уменьшить размер PDF‑файла в Java с помощью Aspose.PDF.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сжать ресурсы PDF и уменьшить размер файла с помощью Java
Abstract: В этой статье объясняется, как оптимизировать PDF‑файлы с помощью Aspose.PDF for Java. Охватываются оптимизация всего документа, сжатие ресурсов, снижение качества изображений, удаление неиспользуемых объектов и потоков, связывание дублирующих потоков, извлечение встроенных шрифтов, упрощение аннотаций и форм, конвертация в градации серого и сжатие изображений Flate.
---
Aspose.PDF for Java предоставляет функции оптимизации через `Document.optimize`, `optimizeResources` и `OptimizationOptions`.

## Оптимизация PDF с помощью общей оптимизации документа

Используйте этот пример, когда вы хотите, чтобы Aspose.PDF применил встроенную процедуру оптимизации всего документа.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите `optimize()` на документе.
1. Сохраните оптимизированный файл и сравните размеры оригинального и полученного.

```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Уменьшение размера PDF с помощью оптимизации ресурсов

Этот пример сосредоточен на оптимизации на уровне ресурсов без ручной настройки отдельных параметров.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Запустите `optimizeResources()` для оптимизации внутренних ресурсов.
1. Сохраните результат и выведите размеры входного и выходного файлов.

```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## Сжатие всех изображений в PDF

Используйте этот подход, когда документы с большим количеством изображений требуют меньшего размера файла, и небольшое ухудшение качества изображений допустимо.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) и включите сжатие изображений с требуемым уровнем качества.
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

## Удаление неиспользуемых объектов из PDF

Этот пример удаляет неиспользуемые объекты, которые могут оставаться в структуре документа после правок или слияний.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) и включите удаление неиспользуемых объектов.
1. Оптимизируйте ресурсы и сохраните обновлённый файл.
1. Выведите оригинальные и уменьшенные размеры файлов.

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

## Удаление неиспользуемых потоков из PDF

Используйте этот подход, когда хотите удалить данные потоков, на которые документ больше не ссылается.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Настройте [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) для удаления неиспользуемых потоков.
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

## Связывание дублирующих потоков в PDF

В этом примере происходит дедупликация повторяющихся потоков, чтобы одинаковый контент мог храниться только один раз.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) и включите связывание дублирующих потоков.
1. Оптимизируйте ресурсы, сохраните документ вывода и выведите размеры файлов.

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

## Удаление встроенных шрифтов из PDF

Используйте эту опцию, когда уменьшение размера файла важнее, чем сохранение встроенных данных шрифтов в выводе.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Настройте [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/), чтобы удалить встраивание шрифтов.
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

## Фиксация аннотаций в PDF

Этот пример преобразует аннотации в статическое содержимое страницы, поэтому они больше не остаются интерактивными объектами.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите каждую страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и её коллекцию аннотаций [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/).
1. Преобразуйте все аннотации в статическое содержимое страницы и сохраните обновлённый документ.

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

## Преобразование полей PDF-формы в содержимое страницы

Используйте этот подход, когда заполняемые поля формы должны стать фиксированным содержимым перед распространением или архивированием.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Проверьте, содержит ли документ виджеты формы.
1. Преобразуйте каждое поле [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/), представленное аннотацией [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/), в статическое содержимое страницы.
1. Сохраните выходной файл и выведите размеры файлов.

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

Этот пример переводит каждую страницу в градации серого, что может помочь уменьшить сложность цвета и стандартизировать вывод для архивных или печатных рабочих процессов.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите каждую страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документе.
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

## Использование сжатия изображений FlateDecode

Используйте этот шаблон, когда хотите применить сжатие на основе Flate к изображениям при оптимизации ресурсов PDF.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## Вывод размеров файлов до и после оптимизации

Этот вспомогательный метод сообщает о разнице в размере между исходным файлом и оптимизированным выходным файлом.

1. Прочитайте размер входного файла.
1. Прочитайте размер выходного файла.
1. Выведите оба значения в одном статусном сообщении.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```



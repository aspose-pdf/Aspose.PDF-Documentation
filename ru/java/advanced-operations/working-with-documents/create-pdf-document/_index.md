---
title: Создание PDF-файлов на Java
linktitle: Создание PDF-документа
type: docs
weight: 10
url: /ru/java/create-pdf-document/
description: Узнайте, как создавать PDF-файлы и создавать поисковые PDF в Java с помощью Aspose.PDF.
lastmod: "2026-11-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создание PDF-файлов и PDF-документов с возможностью поиска на Java
Abstract: В этой статье показано, как создавать PDF‑документы с помощью Aspose.PDF for Java. Описывается создание нового PDF с нуля и преобразование документа, основанного на изображениях, в поисковый PDF с предоставлением вывода HOCR от внешнего OCR‑движка.
---
Aspose.PDF for Java поддерживает как простое создание документов, так и рабочие процессы поисковых PDF с поддержкой OCR.

## Создание нового PDF-документа

Используйте этот подход, когда необходимо создать простой PDF‑файл с нуля.

1. Создайте новый PDF-документ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте объект [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) и добавьте его на страницу.
1. Сохраните выходной PDF-документ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Создание PDF с возможностью поиска

Отсканированный PDF содержит изображения текста. Используйте внешний OCR-движок для распознавания текста и сделайте его доступным для поиска и выделения. Ниже приведённые примеры используют Tesseract для возврата разметки HOCR в Aspose.PDF или для создания страниц PDF с распознанным текстом, которые затем объединяются.

Установите Tesseract 4 или более новую версию с данными английского языка LSTM перед запуском этих примеров. Укажите путь к исполняемому файлу в `TESSERACT_PATH` в общем вспомогательном методе ниже или используйте `"tesseract"`, если он доступен в `PATH`. Оба примера используют один и тот же вспомогательный метод и требуют Java 11 или новее. Разместите методы и константы в одном классе и включите эти импорты:

### Создание PDF с возможностью поиска с помощью обратного вызова HOCR

Используйте [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) для передачи распознанного текста и его координат в Aspose.PDF. Tesseract генерирует разметку HOCR, а Aspose.PDF использует её для добавления в документ на основе изображений текстового слоя с возможностью поиска.

1. Подготовьте временный каталог для изображения, вывода HOCR и журнала OCR.
1. Реализуйте [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) и сохраните каждое предоставленное изображение в файл JPEG.
1. Вызовите общий вспомогательный метод `runTesseract` с форматом вывода `hocr`.
1. Прочитайте сгенерированный файл `.hocr`, удалите временные файлы и верните разметку из обратного вызова.
1. Откройте исходный документ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и передайте обратный вызов в `convert`.
1. Проверьте результат конвертации и сохраните поисковый PDF, используя `save`.

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.devices.PngDevice;
import com.aspose.pdf.devices.Resolution;

import javax.imageio.ImageIO;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public static void createSearchablePdf_1(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.toAbsolutePath().getParent().resolve("ocr-temp");

    // Create callBack - logic recognize text for PDF images. Use outer OCR supports
    // HOCR standard(http://en.wikipedia.org/wiki/HOCR).
    // We have used free google tesseract
    // OCR(http://en.wikipedia.org/wiki/Tesseract_%28software%29)

    Document.CallBackGetHocr callBackGetHocr = new Document.CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            File outputfile = tempDir.resolve("test.jpg").toFile();
            try {
                Files.createDirectories(tempDir);
                ImageIO.write(img, "jpg", outputfile);
            } catch (IOException e1) {
                throw new java.io.UncheckedIOException("Failed to write OCR image.", e1);
            }

            try {
                Path outputBase = tempDir.resolve("out");
                runTesseract(outputfile.toPath(), outputBase, "hocr", tempDir.resolve("tesseract.log"));
            } catch (IOException e) {
                throw new java.io.UncheckedIOException("Tesseract OCR failed.", e);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new IllegalStateException("Tesseract OCR was interrupted.", e);
            }

            // Read the HOCR output as a string.
            File file = tempDir.resolve("out.hocr").toFile();
            StringBuilder fileContents = new StringBuilder((int) file.length());
            Scanner scanner = null;
            try {
                scanner = new Scanner(file);
                String lineSeparator = System.getProperty("line.separator");

                while (scanner.hasNextLine()) {
                    fileContents.append(scanner.nextLine() + lineSeparator);
                }
            } catch (FileNotFoundException e) {
                throw new java.io.UncheckedIOException("Tesseract OCR failed.", e);
            } finally {
                if (scanner != null)
                    scanner.close();
            }

            // deleting temp files
            File fileOut = tempDir.resolve("out.hocr").toFile();
            if (fileOut.exists()) {
                fileOut.delete();
            }
            File fileLog = tempDir.resolve("tesseract.log").toFile();
            if (fileLog.exists()) {
                fileLog.delete();
            }
            File fileTest = tempDir.resolve("test.jpg").toFile();
            if (fileTest.exists()) {
                fileTest.delete();
            }

            return fileContents.toString();
        }
    };
    // End callBack
    try (Document document = new Document(inputFile.toString())) {
        if (!document.convert(callBackGetHocr))
            throw new RuntimeException("Failed to convert document.");
        document.save(outputFile.toString());
    }
}
```

В этом примере используются фиксированные имена файлов внутри `ocr-temp`. Используйте отдельный временный каталог для каждого преобразования, если адаптируете его для параллельной обработки.

### Создание PDF с возможностью поиска путем распознавания отрисованных страниц

Отобразите каждую страницу как PNG‑изображение, позвольте Tesseract создать поисковый PDF для этого изображения и объедините сгенерированные PDF‑файлы в один документ. Вывод основан на отрисованных изображениях страниц с распознанным текстом, поэтому существующие интерактивные элементы не перенесутся.

1. Создайте уникальный временный каталог для отрендеренного изображения, сгенерированного PDF и журнала OCR.
1. Откройте исходный документ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте пустой выходной документ.
1. Создайте [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) с [Resolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 600 DPI.
1. Переберите объекты [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) исходного документа и отрисуйте каждую страницу с помощью `process`.
1. Вызовите общий вспомогательный метод `runTesseract` с форматом вывода `pdf` и добавьте сгенерированный PDF с помощью [Document.merge](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните объединенный поисковый PDF и удалите временные файлы в блоке `finally`.

```java
public static void createSearchablePdf_2(Path inputFile, Path outputFile)
        throws IOException, InterruptedException {
    Path outputDirectory = outputFile.toAbsolutePath().getParent();
    Files.createDirectories(outputDirectory);
    Path tempDir = Files.createTempDirectory(outputDirectory, "ocr-");
    Path tempImage = tempDir.resolve("page.png");
    Path tempDoc = tempDir.resolve("page");
    Path tempPdf = tempDir.resolve("page.pdf");
    Path tempLog = tempDir.resolve("page.log");
    Throwable failure = null;
    try (Document inputDocument = new Document(inputFile.toString());
         Document outputDocument = new Document()) {
        PngDevice pngDevice = new PngDevice(new Resolution(600));
        for (Page page : inputDocument.getPages()) {
            pngDevice.process(page, tempImage.toString());
            runTesseract(tempImage, tempDoc, "pdf", tempLog);
            outputDocument.merge(tempPdf.toString());
            Files.deleteIfExists(tempPdf);
        }
        outputDocument.save(outputFile.toString());
    } catch (InterruptedException e) {
        failure = e;
        Thread.currentThread().interrupt();
        throw e;
    } catch (IOException | RuntimeException | Error e) {
        failure = e;
        throw e;
    } finally {
        IOException cleanupFailure = null;
        for (Path path : new Path[]{tempImage, tempPdf, tempLog, tempDir}) {
            try {
                Files.deleteIfExists(path);
            } catch (IOException e) {
                if (cleanupFailure == null) {
                    cleanupFailure = e;
                } else {
                    cleanupFailure.addSuppressed(e);
                }
            }
        }
        if (cleanupFailure != null) {
            if (failure != null) {
                failure.addSuppressed(cleanupFailure);
            } else {
                throw cleanupFailure;
            }
        }
    }
}
```

### Запуск Tesseract из примеров

Добавьте эти константы и общий вспомогательный метод в тот же класс, что и примеры. Вспомогательный метод использует английский язык (`eng`), LSTM‑движок (`--oem 1`) и автоматическое разделение страниц (`--psm 3`). Он записывает диагностический вывод в журнал, ждёт до двух минут и проверяет, что был создан непустой файл результата. Он завершает процесс, если он всё ещё работает, при выходе из вспомогательного метода.

```java
// Change this to match your installation, or use "tesseract" for PATH lookup.
private static final String TESSERACT_PATH = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe";
private static final long TESSERACT_TIMEOUT_MINUTES = 2;

private static void runTesseract(Path image, Path outputBase, String format, Path log)
        throws IOException, InterruptedException {
    Path result = Path.of(outputBase + "." + format);
    Files.deleteIfExists(result);
    ProcessBuilder builder = new ProcessBuilder(
            TESSERACT_PATH, image.toString(), outputBase.toString(),
            "-l", "eng", "--oem", "1", "--psm", "3", format);
    builder.redirectErrorStream(true);
    builder.redirectOutput(log.toFile());
    Process process = builder.start();
    try {
        process.getOutputStream().close();
        if (!process.waitFor(TESSERACT_TIMEOUT_MINUTES, TimeUnit.MINUTES)) {
            throw new IOException("Tesseract timed out after "
                    + TESSERACT_TIMEOUT_MINUTES + " minutes while processing " + image);
        }
        if (process.exitValue() != 0 || !Files.isRegularFile(result)
                || Files.size(result) == 0) {
            throw new IOException("Tesseract failed (exit " + process.exitValue()
                    + ") while processing " + image + ": " + Files.readString(log));
        }
    } finally {
        if (process.isAlive()) {
            process.destroyForcibly();
            process.onExit().join();
        }
    }
}
```

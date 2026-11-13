---
title: 在 Java 中创建 PDF 文件
linktitle: 创建 PDF 文档
type: docs
weight: 10
url: /zh/java/create-pdf-document/
description: 学习如何使用 Aspose.PDF 在 Java 中创建 PDF 文件并生成可搜索的 PDF。
lastmod: "2026-11-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 创建 PDF 文件和可搜索的 PDF 文档
Abstract: 本文展示了如何使用 Aspose.PDF for Java 创建 PDF 文档。它涵盖了从头创建新 PDF，以及通过提供外部 OCR 引擎的 HOCR 输出，将基于图像的文档转换为可搜索的 PDF。
---
Aspose.PDF for Java 支持简单的文档创建以及 OCR 辅助的可搜索 PDF 工作流。

## 创建新的 PDF 文档

当您需要从头生成一个简单的 PDF 文件时，请使用此方法。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 到文档。
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 并将其添加到页面。
1. 保存输出的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## 创建可搜索的 PDF

扫描的 PDF 包含文本图像。使用外部 OCR 引擎识别文本，使其可搜索和可选择。以下示例使用 Tesseract 将 HOCR 标记返回给 Aspose.PDF，或生成可搜索的 PDF 页面，然后进行合并。

在运行这些示例之前，请安装 Tesseract 4 或更高版本，并包含英语 LSTM 语言数据。在下面的共享辅助方法中，将 `TESSERACT_PATH` 设置为可执行文件的路径；如果该程序位于 `PATH` 中，也可以使用 `"tesseract"`。两个示例使用相同的辅助方法，并且需要 Java 11 或更高版本。将这些方法和常量放在同一个类中，并包含以下导入：

### 使用 HOCR 回调创建可搜索的 PDF

使用 [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) 向 Aspose.PDF 提供已识别的文本及其坐标。Tesseract 生成 HOCR 标记，而 Aspose.PDF 使用它向基于图像的文档添加可搜索的文本层。

1. 准备一个临时目录用于存放图像、HOCR 输出和 OCR 日志。
1. 实现 [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) 并将每个提供的图像保存为 JPEG 文件。
1. 调用共享辅助方法 `runTesseract`，并指定输出格式 `hocr`。
1. 读取生成的 `.hocr` 文件，删除临时文件，并从回调中返回标记。
1. 打开源 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并将回调传递给 `convert`。
1. 检查转换结果，并使用 `save` 保存可搜索的 PDF。

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

此示例在 `ocr-temp` 内使用固定的文件名。 如果您将其适配为并发处理，请为每个转换使用单独的临时目录。

### 通过识别已渲染的页面创建可搜索的 PDF

将每页渲染为 PNG 图像，使用 Tesseract 为该图像生成可搜索的 PDF，然后将生成的 PDF 合并为一个文档。输出基于已渲染的页面图像和识别的文本，因此不会保留现有的交互元素。

1. 为渲染的图像、生成的 PDF 和 OCR 日志创建唯一的临时目录。
1. 打开源 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并创建一个空的输出文档。
1. 创建一个 [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/)，并使用 600 DPI 的 [Resolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/)。
1. 遍历源 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 对象，并使用 `process` 渲染每页。
1. 调用共享辅助方法 `runTesseract`，并指定输出格式 `pdf`，然后使用 [Document.merge](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 追加生成的 PDF。
1. 保存合并后的可搜索 PDF，并在 `finally` 块中删除临时文件。

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

### 从示例中运行 Tesseract

将这些常量和共享辅助方法添加到与示例相同的类中。该辅助方法使用英语（`eng`）、LSTM 引擎（`--oem 1`），以及自动页面分段（`--psm 3`）。它将诊断输出写入日志，等待最多两分钟，并验证已创建非空的结果文件。如果在辅助方法退出时进程仍在运行，它会终止该进程。

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

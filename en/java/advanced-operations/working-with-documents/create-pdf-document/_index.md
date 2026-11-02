---
title: Create PDF Files in Java
linktitle: Create PDF Document
type: docs
weight: 10
url: /java/create-pdf-document/
description: Learn how to create PDF files and build searchable PDFs in Java using Aspose.PDF.
lastmod: "2026-10-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create PDF files and searchable PDF documents with Java
Abstract: This article shows how to create PDF documents using Aspose.PDF for Java. It covers creating a new PDF from scratch and converting an image-based document into a searchable PDF by supplying HOCR output from an external OCR engine.
---
Aspose.PDF for Java supports both simple document creation and OCR-assisted searchable PDF workflows.

## Create a new PDF document

Use this approach when you need to generate a simple PDF file from scratch.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) to the document.
1. Create a [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) and add it to the page.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Create a searchable PDF

A scanned PDF contains images of text. Use an external OCR engine to recognize the text and make it searchable and selectable. The following examples use Tesseract to return HOCR markup to Aspose.PDF or to generate searchable PDF pages that are then merged.

Install Tesseract 4 or newer with English LSTM language data before running these examples. Set `TESSERACT_PATH` in the shared helper below to your executable path, or use `"tesseract"` if it is available on `PATH`. Both examples use the same helper and require Java 11 or later. Place the methods and constants in the same class and include these imports:

### Create a searchable PDF using an HOCR callback

Use [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) to supply recognized text and its coordinates to Aspose.PDF. Tesseract generates the HOCR markup, and Aspose.PDF uses it to add a searchable text layer to the image-based document.

1. Prepare a temporary directory for the image, HOCR output, and OCR log.
1. Implement [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) and save each supplied image as a JPEG file.
1. Call the shared `runTesseract` helper with the `hocr` output format.
1. Read the generated `.hocr` file, delete the temporary files, and return the markup from the callback.
1. Open the source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and pass the callback to `convert`.
1. Check the conversion result and save the searchable PDF using `save`.

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

This example uses fixed filenames inside `ocr-temp`. Use a separate temporary directory for each conversion if you adapt it for concurrent processing.

### Create a searchable PDF by recognizing rendered pages

Render each page as a PNG image, let Tesseract generate a searchable PDF for that image, and merge the generated PDFs into one document. The output is based on rendered page images with recognized text, so existing interactive elements are not carried over.

1. Create a unique temporary directory for the rendered image, generated PDF, and OCR log.
1. Open the source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and create an empty output document.
1. Create a [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) with a [Resolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) of 600 DPI.
1. Iterate through the source [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objects and render each page using `process`.
1. Call the shared `runTesseract` helper with the `pdf` output format and append the generated PDF using [Document.merge](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Save the combined searchable PDF and delete the temporary files in the `finally` block.

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

### Run Tesseract from the examples

Add these constants and the shared helper to the same class as the examples. The helper uses English (`eng`), the LSTM engine (`--oem 1`), and automatic page segmentation (`--psm 3`). It writes diagnostic output to a log, waits up to two minutes, and verifies that a nonempty result file was created. It terminates the process if it is still running when the helper exits.

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

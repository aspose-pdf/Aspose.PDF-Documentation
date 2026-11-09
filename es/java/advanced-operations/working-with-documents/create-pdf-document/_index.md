---
title: Crear archivos PDF en Java
linktitle: Crear documento PDF
type: docs
weight: 10
url: /es/java/create-pdf-document/
description: Aprenda cómo crear archivos PDF y generar PDFs buscables en Java usando Aspose.PDF.
lastmod: "2026-11-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crear archivos PDF y documentos PDF buscables con Java
Abstract: Este artículo muestra cómo crear documentos PDF usando Aspose.PDF for Java. Cubre la creación de un nuevo PDF desde cero y la conversión de un documento basado en imágenes en un PDF buscable proporcionando la salida HOCR de un motor OCR externo.
---
Aspose.PDF for Java admite tanto la creación simple de documentos como flujos de trabajo de PDF buscable asistidos por OCR.

## Crear un nuevo documento PDF

Utilice este enfoque cuando necesite generar un archivo PDF simple desde cero.

1. Cree un nuevo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue una página [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Cree un objeto [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) y agréguelo a la página.
1. Guarde el documento PDF de salida [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Crear un PDF buscable

Un PDF escaneado contiene imágenes de texto. Use un motor OCR externo para reconocer el texto y hacerlo buscable y seleccionable. Los siguientes ejemplos usan Tesseract para devolver marcado HOCR a Aspose.PDF o para generar páginas PDF buscables que luego se combinan.

Instale Tesseract 4 o una versión más reciente con los datos de idioma inglés LSTM antes de ejecutar estos ejemplos. Establezca `TESSERACT_PATH` en el método auxiliar compartido que aparece a continuación con la ruta de su ejecutable, o use `"tesseract"` si está disponible en `PATH`. Ambos ejemplos usan el mismo método auxiliar y requieren Java 11 o posterior. Coloque los métodos y constantes en la misma clase e incluya estas importaciones:

### Crear un PDF buscable usando una devolución de llamada HOCR

Utilice [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) para suministrar el texto reconocido y sus coordenadas a Aspose.PDF. Tesseract genera el marcado HOCR, y Aspose.PDF lo utiliza para añadir una capa de texto buscable al documento basado en imágenes.

1. Prepare un directorio temporal para la imagen, la salida HOCR y el registro OCR.
1. Implemente [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) y guarde cada imagen proporcionada como un archivo JPEG.
1. Llame al método auxiliar compartido `runTesseract` con el formato de salida `hocr`.
1. Lea el archivo `.hocr` generado, elimine los archivos temporales y devuelva el marcado de la devolución de llamada.
1. Abra el documento de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y pase la devolución de llamada a `convert`.
1. Verifique el resultado de la conversión y guarde el PDF buscable usando `save`.

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

Este ejemplo utiliza nombres de archivo fijos dentro de `ocr-temp`. Utilice un directorio temporal separado para cada conversión si lo adapta para procesamiento concurrente.

### Crear un PDF buscable reconociendo las páginas renderizadas

Renderice cada página como una imagen PNG, permita que Tesseract genere un PDF buscable para esa imagen y combine los PDF generados en un solo documento. La salida se basa en imágenes de página renderizadas con texto reconocido, por lo que los elementos interactivos existentes no se conservan.

1. Cree un directorio temporal único para la imagen renderizada, el PDF generado y el registro OCR.
1. Abra el documento de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y cree un documento de salida vacío.
1. Cree un [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) con una [Resolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 600 DPI.
1. Recorra los objetos [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) del documento de origen y renderice cada página usando `process`.
1. Llame al método auxiliar compartido `runTesseract` con el formato de salida `pdf` y agregue el PDF generado usando [Document.merge](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Guarde el PDF combinado y buscable y elimine los archivos temporales en el bloque `finally`.

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

### Ejecutar Tesseract desde los ejemplos

Agregue estas constantes y el método auxiliar compartido a la misma clase que los ejemplos. El método auxiliar usa inglés (`eng`), el motor LSTM (`--oem 1`), y la segmentación automática de página (`--psm 3`). Escribe salida de diagnóstico en un registro, espera hasta dos minutos y verifica que se haya creado un archivo de resultados no vacío. Finaliza el proceso si aún sigue ejecutándose cuando finaliza el método auxiliar.

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

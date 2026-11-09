---
title: Criar arquivos PDF em Java
linktitle: Criar documento PDF
type: docs
weight: 10
url: /pt/java/create-pdf-document/
description: Aprenda como criar arquivos PDF e gerar PDFs pesquisáveis em Java usando Aspose.PDF.
lastmod: "2026-11-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar arquivos PDF e documentos PDF pesquisáveis com Java
Abstract: Este artigo demonstra como criar documentos PDF usando Aspose.PDF for Java. Ele abrange a criação de um novo PDF do zero e a conversão de um documento baseado em imagem em um PDF pesquisável, fornecendo a saída HOCR de um mecanismo OCR externo.
---
Aspose.PDF for Java suporta tanto a criação simples de documentos quanto fluxos de trabalho de PDF pesquisável assistidos por OCR.

## Criar um novo documento PDF

Use esta abordagem quando precisar gerar um arquivo PDF simples do zero.

1. Crie um novo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma página [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) e adicione-o à página.
1. Salve o documento PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Criar um PDF pesquisável

Um PDF digitalizado contém imagens de texto. Use um mecanismo OCR externo para reconhecer o texto e torná‑lo pesquisável e selecionável. Os exemplos a seguir usam o Tesseract para retornar marcação HOCR ao Aspose.PDF ou para gerar páginas PDF pesquisáveis que são então mescladas.

Instale o Tesseract 4 ou mais recente com os dados de idioma LSTM para inglês antes de executar estes exemplos. Defina `TESSERACT_PATH` no método auxiliar compartilhado abaixo com o caminho do seu executável, ou use `"tesseract"` se estiver disponível em `PATH`. Ambos os exemplos usam o mesmo método auxiliar e requerem Java 11 ou posterior. Coloque os métodos e constantes na mesma classe e inclua estas importações:

### Criar um PDF pesquisável usando um callback HOCR

Use [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) para fornecer o texto reconhecido e suas coordenadas ao Aspose.PDF. O Tesseract gera a marcação HOCR, e o Aspose.PDF a utiliza para adicionar uma camada de texto pesquisável ao documento baseado em imagem.

1. Prepare um diretório temporário para a imagem, saída HOCR e log de OCR.
1. Implemente [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) e salve cada imagem fornecida como um arquivo JPEG.
1. Chame o método auxiliar compartilhado `runTesseract` com o formato de saída `hocr`.
1. Leia o arquivo `.hocr` gerado, exclua os arquivos temporários e retorne a marcação do callback.
1. Abra o documento de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e passe o callback para `convert`.
1. Verifique o resultado da conversão e salve o PDF pesquisável usando `save`.

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

Este exemplo usa nomes de arquivos fixos dentro de `ocr-temp`. Use um diretório temporário separado para cada conversão se você adaptá-lo para processamento concorrente.

### Criar um PDF pesquisável reconhecendo páginas renderizadas

Renderize cada página como uma imagem PNG, deixe o Tesseract gerar um PDF pesquisável para essa imagem e mescle os PDFs gerados em um único documento. A saída é baseada nas imagens de página renderizadas com texto reconhecido, portanto os elementos interativos existentes não são mantidos.

1. Crie um diretório temporário único para a imagem renderizada, o PDF gerado e o registro de OCR.
1. Abra o documento de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e crie um documento de saída vazio.
1. Crie um [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) com uma [Resolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 600 DPI.
1. Percorra os objetos [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) do documento de origem e renderize cada página usando `process`.
1. Chame o método auxiliar compartilhado `runTesseract` com o formato de saída `pdf` e anexe o PDF gerado usando [Document.merge](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Salve o PDF pesquisável combinado e exclua os arquivos temporários no bloco `finally`.

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

### Executar o Tesseract a partir dos exemplos

Adicione essas constantes e o método auxiliar compartilhado à mesma classe dos exemplos. O método auxiliar usa inglês (`eng`), o motor LSTM (`--oem 1`), e a segmentação automática de página (`--psm 3`). Ele grava saída de diagnóstico em um log, aguarda até dois minutos e verifica se um arquivo de resultado não vazio foi criado. Ele termina o processo se ele ainda estiver em execução quando o método auxiliar terminar.

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

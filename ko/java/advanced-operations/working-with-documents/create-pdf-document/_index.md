---
title: Java에서 PDF 파일 만들기
linktitle: PDF 문서 만들기
type: docs
weight: 10
url: /ko/java/create-pdf-document/
description: Aspose.PDF를 사용하여 Java에서 PDF 파일을 만들고 검색 가능한 PDF를 구축하는 방법을 배우세요.
lastmod: "2026-11-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일 및 검색 가능한 PDF 문서 만들기
Abstract: 이 문서는 Aspose.PDF for Java를 사용하여 PDF 문서를 만드는 방법을 보여줍니다. 여기서는 처음부터 새 PDF를 생성하고 외부 OCR 엔진의 HOCR 출력을 제공하여 이미지 기반 문서를 검색 가능한 PDF로 변환하는 과정을 다룹니다.
---
Aspose.PDF for Java는 간단한 문서 생성과 OCR 지원 검색 가능한 PDF 워크플로우를 모두 지원합니다.

## 새 PDF 문서 만들기

처음부터 간단한 PDF 파일을 생성해야 할 때 이 방법을 사용하십시오.

1. 새 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만드세요.
1. 문서에 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)를 생성하고 페이지에 추가하세요.
1. 출력 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장하세요.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## 검색 가능한 PDF 만들기

스캔한 PDF에는 텍스트 이미지가 포함되어 있습니다. 외부 OCR 엔진을 사용하여 텍스트를 인식하고 검색 가능하고 선택 가능하도록 만드세요. 다음 예제에서는 Tesseract를 사용하여 HOCR 마크업을 Aspose.PDF에 반환하거나 검색 가능한 PDF 페이지를 생성한 다음 병합합니다.

예제들을 실행하기 전에 영어 LSTM 언어 데이터가 포함된 Tesseract 4 이상을 설치하십시오. 아래 공유 도우미의 `TESSERACT_PATH`에 실행 파일 경로를 지정하거나, 실행 파일이 `PATH`에 있으면 `"tesseract"`를 사용하세요. 두 예제 모두 동일한 헬퍼를 사용하며 Java 11 이상이 필요합니다. 메서드와 상수를 동일한 클래스에 배치하고 다음 import를 포함하십시오:

### HOCR 콜백을 사용하여 검색 가능한 PDF 만들기

[Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/)를 사용하여 인식된 텍스트와 좌표를 Aspose.PDF에 제공하세요. Tesseract는 HOCR 마크업을 생성하고, Aspose.PDF는 이를 사용하여 이미지 기반 문서에 검색 가능한 텍스트 레이어를 추가합니다.

1. 이미지, HOCR 출력 및 OCR 로그용 임시 디렉터리를 준비하세요.
1. [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/)를 구현하고 제공된 각 이미지를 JPEG 파일로 저장하세요.
1. 출력 형식 `hocr`로 공유 도우미 `runTesseract`를 호출하세요.
1. 생성된 `.hocr` 파일을 읽고 임시 파일을 삭제한 다음 콜백에서 마크업을 반환하세요.
1. 원본 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 콜백을 `convert`에 전달하세요.
1. 변환 결과를 확인하고 `save`를 사용하여 검색 가능한 PDF를 저장하세요.

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

이 예제에서는 `ocr-temp` 안에 고정된 파일 이름을 사용합니다. 동시 처리에 맞게 조정한다면 각 변환마다 별도의 임시 디렉터리를 사용하십시오.

### 렌더링된 페이지를 인식하여 검색 가능한 PDF 만들기

각 페이지를 PNG 이미지로 렌더링하고, Tesseract가 해당 이미지에 대해 검색 가능한 PDF를 생성하도록 한 뒤, 생성된 PDF들을 하나의 문서로 병합합니다. 출력은 인식된 텍스트가 포함된 렌더링된 페이지 이미지 기반이므로 기존의 인터랙티브 요소는 포함되지 않습니다.

1. 렌더링된 이미지, 생성된 PDF 및 OCR 로그를 위한 고유한 임시 디렉터리를 생성하세요.
1. 원본 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 빈 출력 문서를 생성하세요.
1. [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/)를 600 DPI의 [Resolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/)으로 생성하세요.
1. 원본 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 객체를 순회하고 `process`를 사용하여 각 페이지를 렌더링하세요.
1. 출력 형식 `pdf`로 공유 도우미 `runTesseract`를 호출하고 [Document.merge](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 사용하여 생성된 PDF를 추가하세요.
1. 병합된 검색 가능한 PDF를 저장하고 `finally` 블록에서 임시 파일을 삭제하세요.

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

### 예제에서 Tesseract 실행

이 상수와 공유 헬퍼를 예제와 같은 클래스에 추가하십시오. 헬퍼는 영어(`eng`), LSTM 엔진(`--oem 1`), 자동 페이지 분할(`--psm 3`)을 사용합니다. 진단 출력을 로그에 기록하고, 최대 2분까지 대기한 다음 비어 있지 않은 결과 파일이 생성되었는지 확인합니다. 헬퍼가 종료될 때 프로세스가 여전히 실행 중이면 이를 종료합니다.

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

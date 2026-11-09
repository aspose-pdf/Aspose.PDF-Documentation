---
title: Java での PDF ファイルの作成
linktitle: PDF ドキュメントの作成
type: docs
weight: 10
url: /ja/java/create-pdf-document/
description: Aspose.PDF を使用して Java で PDF ファイルを作成し、検索可能な PDF を作成する方法を学びます。
lastmod: "2026-11-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF ファイルと検索可能な PDF ドキュメントを作成する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントを作成する方法を示します。新規に PDF を一から作成する方法と、外部 OCR エンジンからの HOCR 出力を提供して画像ベースのドキュメントを検索可能な PDF に変換する方法について説明しています。
---
Aspose.PDF for Java は、シンプルなドキュメント作成と OCR 支援による検索可能な PDF ワークフローの両方をサポートしています。

## 新しい PDF ドキュメントの作成

ゼロからシンプルな PDF ファイルを生成する必要がある場合にこのアプローチを使用してください。

1. 新しい PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. ドキュメントに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) を作成し、ページに追加してください。
1. 出力 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## 検索可能な PDF の作成

スキャンされた PDF にはテキストの画像が含まれています。外部 OCR エンジンを使用してテキストを認識し、検索可能で選択可能にします。以下の例では Tesseract を使用して HOCR マークアップを Aspose.PDF に返すか、検索可能な PDF ページを生成してそれらをマージします。

これらのサンプルを実行する前に、英語の LSTM 言語データ付きの Tesseract 4 以上をインストールしてください。以下の共有ヘルパーの `TESSERACT_PATH` に実行可能ファイルのパスを設定するか、実行可能ファイルが `PATH` にある場合は `"tesseract"` を使用してください。 両方の例は同じヘルパーを使用し、Java 11 以降が必要です。メソッドと定数を同じクラスに配置し、以下のインポートを含めてください：

### HOCR コールバックを使用した検索可能な PDF の作成

[Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) を使用して、認識されたテキストとその座標を Aspose.PDF に渡してください。Tesseract は HOCR マークアップを生成し、Aspose.PDF はそれを使用して画像ベースのドキュメントに検索可能なテキスト層を追加します。

1. 画像、HOCR 出力、OCR ログ用の一時ディレクトリを用意してください。
1. [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) を実装し、渡された各画像を JPEG ファイルとして保存してください。
1. 出力形式 `hocr` を指定して、共有ヘルパー `runTesseract` を呼び出してください。
1. 生成された `.hocr` ファイルを読み取り、一時ファイルを削除して、コールバックからマークアップを返してください。
1. ソースの [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、コールバックを `convert` に渡してください。
1. 変換結果を確認し、`save` を使用して検索可能な PDF を保存してください。

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

この例では、`ocr-temp` 内で固定のファイル名を使用しています。 同時処理用に適用する場合は、変換ごとに別々の一時ディレクトリを使用してください。

### レンダリングされたページの認識による検索可能な PDF の作成

各ページをPNG画像としてレンダリングし、Tesseractにその画像から検索可能なPDFを生成させ、生成されたPDFを1つの文書にマージします。出力はレンダリングされたページ画像と認識されたテキストに基づくため、既存のインタラクティブ要素は引き継がれません。

1. レンダリングされた画像、生成された PDF、OCR ログ用の一意の一時ディレクトリを作成してください。
1. ソースの [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、空の出力ドキュメントを作成してください。
1. [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) を、600 DPI の [Resolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) で作成してください。
1. ソースの [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) オブジェクトを反復処理し、`process` を使用して各ページをレンダリングしてください。
1. 出力形式 `pdf` を指定して共有ヘルパー `runTesseract` を呼び出し、[Document.merge](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を使用して生成された PDF を追加してください。
1. 結合された検索可能な PDF を保存し、`finally` ブロックで一時ファイルを削除してください。

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

### 例からの Tesseract の実行

これらの定数と共有ヘルパーを、例と同じクラスに追加してください。ヘルパーは英語（`eng`）、LSTM エンジン（`--oem 1`）、自動ページ分割（`--psm 3`）を使用します。 診断出力をログに書き込み、最大 2 分待機し、空でない結果ファイルが作成されたことを確認します。ヘルパーが終了するときにプロセスがまだ実行中であれば、それを終了させます。

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

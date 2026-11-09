---
title: إنشاء ملفات PDF في Java
linktitle: إنشاء مستند PDF
type: docs
weight: 10
url: /ar/java/create-pdf-document/
description: تعلم كيفية إنشاء ملفات PDF وبناء ملفات PDF قابلة للبحث في Java باستخدام Aspose.PDF.
lastmod: "2026-11-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء ملفات PDF ومستندات PDF قابلة للبحث باستخدام Java
Abstract: توضح هذه المقالة كيفية إنشاء مستندات PDF باستخدام Aspose.PDF for Java. وتغطي إنشاء ملف PDF جديد من الصفر وتحويل مستند قائم على الصورة إلى PDF قابل للبحث عن طريق توفير مخرجات HOCR من محرك OCR خارجي.
---
يدعم Aspose.PDF for Java كل من إنشاء المستندات البسيطة وتدفقات العمل القابلة للبحث في PDF المدعومة بـ OCR.

## إنشاء مستند PDF جديد

استخدم هذا النهج عندما تحتاج إلى إنشاء ملف PDF بسيط من الصفر.

1. أنشئ مستند PDF جديدًا [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف صفحة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ كائنًا من الفئة [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) وأضفه إلى الصفحة.
1. احفظ مستند PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## إنشاء PDF قابل للبحث

PDF الممسوح ضوئياً يحتوي على صور للنص. استخدم محرك OCR خارجي للتعرف على النص وجعله قابلاً للبحث والتحديد. الأمثلة التالية تستخدم Tesseract لإرجاع ترميز HOCR إلى Aspose.PDF أو لإنشاء صفحات PDF قابلة للبحث يتم دمجها بعد ذلك.

قم بتثبيت Tesseract 4 أو أحدث مع بيانات LSTM للغة الإنجليزية قبل تشغيل هذه الأمثلة. اضبط `TESSERACT_PATH` في أداة المساعدة المشتركة أدناه إلى مسار الملف التنفيذي الخاص بك، أو استخدم `"tesseract"` إذا كان متاحًا على `PATH`. كلا المثالين يستخدمان المساعد نفسه ويتطلبان Java 11 أو أحدث. ضع الأساليب والثوابت في نفس الفئة وأدرج هذه الاستيرادات:

### إنشاء PDF قابل للبحث باستخدام رد اتصال HOCR

استخدم [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) لتزويد Aspose.PDF بالنص المتعرف عليه وإحداثياته. يُنشئ Tesseract علامة HOCR، وتستخدم Aspose.PDF ذلك لإضافة طبقة نص قابلة للبحث إلى المستند المعتمد على الصور.

1. قم بإعداد دليل مؤقت للصور وإخراج HOCR وسجل OCR.
1. نفّذ [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) واحفظ كل صورة مُزودة كملف JPEG.
1. استدعِ الدالة المساعدة المشتركة `runTesseract` باستخدام تنسيق الإخراج `hocr`.
1. اقرأ ملف `.hocr` الناتج، واحذف الملفات المؤقتة، وأعد ترميز HOCR من رد الاتصال.
1. افتح المستند المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ومرّر رد الاتصال إلى `convert`.
1. تحقق من نتيجة التحويل واحفظ ملف PDF القابل للبحث باستخدام `save`.

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

يستخدم هذا المثال أسماء ملفات ثابتة داخل `ocr-temp`. استخدم مجلدًا مؤقتًا منفصلًا لكل تحويل إذا قمت بتكييفه للمعالجة المتزامنة.

### إنشاء ملف PDF قابل للبحث عن طريق التعرف على الصفحات المعروضة

قم بتحويل كل صفحة إلى صورة PNG، ودع Tesseract يولد ملف PDF قابل للبحث لتلك الصورة، ثم ادمج ملفات PDF المولدة في مستند واحد. الناتج يعتمد على صور الصفحات المُعالجة مع النص المتعرف عليه، لذا لا يتم نقل العناصر التفاعلية الموجودة.

1. أنشئ دليلًا مؤقتًا فريد للصور المعروضة، وملف PDF المُولَّد، وسجل OCR.
1. افتح المستند المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأنشئ مستند إخراج فارغًا.
1. أنشئ كائنًا من الفئة [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) مع كائن [Resolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) بدقة 600 DPI.
1. كرّر المرور على كائنات [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) في المستند المصدر واعرض كل صفحة باستخدام `process`.
1. استدعِ الدالة المساعدة المشتركة `runTesseract` باستخدام تنسيق الإخراج `pdf` وألحق ملف PDF الناتج باستخدام [Document.merge](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احفظ ملف PDF القابل للبحث المدمج واحذف الملفات المؤقتة في كتلة `finally`.

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

### تشغيل Tesseract من الأمثلة

أضف هذه الثوابت والمساعد المشترك إلى نفس الفئة مثل الأمثلة. يستخدم المساعد اللغة الإنجليزية (`eng`)، محرك LSTM (`--oem 1`)، وتقسيم الصفحات التلقائي (`--psm 3`). يكتب مخرجات تشخيصية إلى سجل، ينتظر حتى دقيقتين، ويتحقق من إنشاء ملف نتيجة غير فارغ. يوقف العملية إذا كانت لا تزال جارية عندما يخرج المساعد.

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

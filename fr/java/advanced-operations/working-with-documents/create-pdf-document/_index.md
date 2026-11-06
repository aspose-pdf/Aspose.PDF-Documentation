---
title: Créer des fichiers PDF en Java
linktitle: Créer un document PDF
type: docs
weight: 10
url: /fr/java/create-pdf-document/
description: Apprenez comment créer des fichiers PDF et créer des PDF permettant la recherche de texte en Java à l'aide d'Aspose.PDF.
lastmod: "2026-11-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créer des fichiers PDF et des documents PDF permettant la recherche de texte avec Java
Abstract: Cet article montre comment créer des documents PDF à l'aide d'Aspose.PDF for Java. Il couvre la création d'un nouveau PDF à partir de zéro et la conversion d'un document basé sur une image en PDF permettant la recherche de texte en fournissant la sortie HOCR d'un moteur OCR externe.
---
Aspose.PDF for Java prend en charge à la fois la création simple de documents et les flux de travail de PDF permettant la recherche de texte assistés par OCR.

## Créer un nouveau document PDF

Utilisez cette approche lorsque vous devez générer un fichier PDF simple à partir de zéro.

1. Créez un nouveau document PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ajoutez une page [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.
1. Créez un objet [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) et ajoutez-le à la page.
1. Enregistrez le document PDF de sortie [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Créer un PDF permettant la recherche de texte

Un PDF numérisé contient des images de texte. Utilisez un moteur OCR externe pour reconnaître le texte et permettre sa recherche et sa sélection. Les exemples suivants utilisent Tesseract pour renvoyer du balisage HOCR à Aspose.PDF ou pour générer des pages PDF permettant la recherche de texte qui sont ensuite fusionnées.

Installez Tesseract 4 ou une version plus récente avec les données linguistiques LSTM anglaises avant d'exécuter ces exemples. Définissez `TESSERACT_PATH` dans la méthode utilitaire partagée ci-dessous sur le chemin de votre exécutable, ou utilisez `"tesseract"` si cet exécutable est disponible dans `PATH`. Les deux exemples utilisent la même méthode utilitaire et nécessitent Java 11 ou une version ultérieure. Placez les méthodes et les constantes dans la même classe et incluez ces importations :

### Créer un PDF permettant la recherche de texte en utilisant un rappel HOCR

Utilisez [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) pour fournir le texte reconnu et ses coordonnées à Aspose.PDF. Tesseract génère le balisage HOCR, et Aspose.PDF l'utilise pour ajouter une couche de texte permettant la recherche de texte au document basé sur des images.

1. Préparez un répertoire temporaire pour l'image, la sortie HOCR et le journal OCR.
1. Implémentez [Document.CallBackGetHocr](https://reference.aspose.com/pdf/java/com.aspose.pdf/document.callbackgethocr/) et enregistrez chaque image fournie en fichier JPEG.
1. Appelez la méthode utilitaire partagée `runTesseract` avec le format de sortie `hocr`.
1. Lisez le fichier `.hocr` généré, supprimez les fichiers temporaires, et renvoyez le balisage depuis le rappel.
1. Ouvrez le document source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et transmettez le rappel à `convert`.
1. Vérifiez le résultat de la conversion et enregistrez le PDF permettant la recherche de texte à l'aide de `save`.

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

Cet exemple utilise des noms de fichiers fixes dans `ocr-temp`. Utilisez un répertoire temporaire distinct pour chaque conversion si vous l'adaptez pour un traitement simultané.

### Créer un PDF permettant la recherche de texte en reconnaissant les pages rendues

Rendez chaque page sous forme d'image PNG, laissez Tesseract générer un PDF permettant la recherche de texte pour cette image, puis fusionnez les PDF générés en un seul document. Le résultat est basé sur les images de page rendues avec le texte reconnu, de sorte que les éléments interactifs existants ne sont pas conservés.

1. Créez un répertoire temporaire unique pour l'image rendue, le PDF généré et le journal OCR.
1. Ouvrez le document source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et créez un document de sortie vide.
1. Créez un [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) avec une [Resolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 600 DPI.
1. Parcourez les objets [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) du document source et effectuez le rendu de chaque page en utilisant `process`.
1. Appelez la méthode utilitaire partagée `runTesseract` avec le format de sortie `pdf` et ajoutez le PDF généré à l'aide de [Document.merge](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enregistrez le PDF combiné et permettant la recherche de texte et supprimez les fichiers temporaires dans le bloc `finally`.

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

### Exécuter Tesseract à partir des exemples

Ajoutez ces constantes et la méthode utilitaire partagée à la même classe que les exemples. La méthode utilitaire utilise l'anglais (`eng`), le moteur LSTM (`--oem 1`), et la segmentation automatique des pages (`--psm 3`). Elle écrit la sortie de diagnostic dans un journal, attend jusqu'à deux minutes et vérifie qu'un fichier de résultat non vide a été créé. Elle termine le processus s'il est encore en cours d'exécution lorsque la méthode utilitaire se termine.

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

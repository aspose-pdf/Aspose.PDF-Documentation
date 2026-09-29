---
title: Ekstrak Lampiran dari PDF
linktitle: Ekstrak Lampiran
type: docs
weight: 50
url: /id/java/extract-attachment/
description: Pelajari cara mengekstrak file tertanam dan anotasi lampiran file dari dokumen PDF dalam Java menggunakan Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak satu atau semua file tertanam dari PDF dengan Java
Abstract: Artikel ini menjelaskan cara mengekstrak lampiran dari dokumen PDF dengan Aspose.PDF for Java. Artikel ini mencakup mengekstrak satu lampiran bernama, menyimpan setiap file tersemat ke folder output, membaca metadata file, dan mengekspor konten dari anotasi FileAttachment pada sebuah halaman.
---
Aspose.PDF for Java mendukung beberapa alur ekstraksi tergantung pada cara lampiran disimpan dalam dokumen.

## Ekstrak satu lampiran berdasarkan nama

Gunakan contoh ini ketika Anda perlu menyimpan satu file tersemat tertentu dari sebuah PDF.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasi melalui koleksi file tersemat hingga nama lampiran yang diperlukan ditemukan.
1. Salin aliran lampiran ke file output dan berhenti setelah ekstraksi.

```java
public static void extractSingleAttachment(Path inputFile, String attachmentName, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Extracting attachment: " + attachmentName);

        boolean attachmentFound = false;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            if (attachmentName.equals(fileSpecification.getName())) {
                try (InputStream inputStream = fileSpecification.getContents();
                     OutputStream outputStream = Files.newOutputStream(outputFile)) {
                    inputStream.transferTo(outputStream);
                }
                System.out.println("Attachment extracted successfully");
                attachmentFound = true;
                break;
            }
        }

        if (!attachmentFound) {
            throw new IllegalArgumentException("Attachment '" + attachmentName + "' not found in PDF");
        }
    }
}
```

## Cetak parameter file tersemat

Metode pembantu ini mencetak metadata yang disimpan dalam sebuah [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/) objek.

1. Periksa apakah objek parameter file ada.
1. Baca nilai checksum, tanggal pembuatan, tanggal modifikasi, dan ukuran yang tersedia.
1. Cetak nilai-nilai tersebut ke konsol.

```java
public static void printFileParams(FileParams params) {
    if (params != null) {
        try {
            System.out.println("CheckSum: " + params.getCheckSum());
        } catch (Exception ex) {
            System.out.println("CheckSum: null");
        }
        System.out.println("Creation Date: " + params.getCreationDate());
        System.out.println("Modification Date: " + params.getModDate());
        System.out.println("Size: " + params.getSize());
    }
}
```

## Ekstrak semua lampiran tersemat

Gunakan contoh ini ketika setiap file tersemat dalam PDF harus ditulis ke direktori output.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan koleksi file tersemat dan tentukan nama file output yang aman untuk setiap item.
1. Cetak metadata, simpan setiap aliran lampiran, dan lanjutkan hingga semua file diekspor.

```java
public static void extractAttachments(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Total files: " + document.getEmbeddedFiles().size());

        int fileIndex = 1;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            String fileName = fileSpecification.getName();
            if (fileName == null || fileName.isBlank()) {
                fileName = fileSpecification.getUnicodeName();
            }
            if (fileName == null || fileName.isBlank()) {
                fileName = "attachment_" + fileIndex + ".bin";
            }

            System.out.println("Name: " + fileName);
            System.out.println("Description: " + fileSpecification.getDescription());
            System.out.println("Mime Type: " + fileSpecification.getMIMEType());
            printFileParams(fileSpecification.getParams());

            Path outputPath = outputDir.resolve(fileName);
            try (InputStream inputStream = fileSpecification.getContents();
                 OutputStream outputStream = Files.newOutputStream(outputPath)) {
                inputStream.transferTo(outputStream);
            }
            fileIndex++;
        }
    }
}
```

## Ekstrak anotasi lampiran file

Gunakan contoh ini ketika file dilampirkan melalui anotasi halaman bukan hanya melalui koleksi file tersemat.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Temukan yang pertama [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/) di halaman.
1. Baca spesifikasi file-nya, ekspor isinya, dan cetak jalur tujuan.

```java
public static void extractFileAttachmentAnnotation(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        FileAttachmentAnnotation fileAttachment = null;
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FileAttachment) {
                fileAttachment = (FileAttachmentAnnotation) annotation;
                break;
            }
        }

        if (fileAttachment == null) {
            System.out.println("File attachment annotation not found.");
            return;
        }

        FileSpecification fileSpecification = fileAttachment.getFile();
        System.out.println("File name: " + fileSpecification.getName());

        Path outputPath = outputDir.resolve("extracted-" + fileSpecification.getName());
        try (InputStream inputStream = fileSpecification.getContents();
             OutputStream outputStream = Files.newOutputStream(outputPath)) {
            inputStream.transferTo(outputStream);
        }

        System.out.println("Extracted to: " + outputPath);
    }
}
```

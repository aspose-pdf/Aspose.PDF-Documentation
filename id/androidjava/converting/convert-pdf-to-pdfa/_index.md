---
title: Konversi File PDF ke PDF/A
linktitle: Konversi File PDF ke PDF/A
type: docs
weight: 180
url: /id/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2026-07-01"
description: Topik ini menunjukkan bagaimana Aspose.PDF for Java memungkinkan mengonversi file PDF ke file PDF yang mematuhi PDF/A.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF memungkinkan Anda mengonversi file PDF menjadi file PDF yang mematuhi PDF/A. Sebelum melakukannya, file harus divalidasi. Artikel ini menjelaskan caranya.

Harap dicatat bahwa kami mengikuti Adobe Preflight untuk memvalidasi kepatuhan PDF/A. Semua alat di pasar memiliki “representation” masing-masing terhadap kepatuhan PDF/A. Harap periksa artikel ini di [Alat validasi PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) sebagai referensi. Kami memilih produk Adobe untuk memverifikasi bagaimana Aspose.PDF menghasilkan file PDF karena Adobe berada di pusat segala hal yang terkait dengan PDF.

Sebelum mengonversi PDF menjadi file yang mematuhi PDF/A, validasi PDF menggunakan metode validate. Hasil validasi disimpan dalam file XML dan kemudian hasil ini juga diteruskan ke metode convert. Anda juga dapat menentukan tindakan untuk elemen yang tidak dapat dikonversi menggunakan [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) enumerasi.

{{% alert color="primary" %}}

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## Konversi PDF ke PDF/A_1b

Potongan kode berikut menunjukkan cara mengonversi file PDF ke PDF yang mematuhi PDF/A-1b.

```java
public void convertPDFtoPDFa1b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save output document
        document.save(pdfaFileName.toString());
    }
```

Untuk melakukan validasi saja, gunakan baris kode berikut:

```java
public void ValidatePDF_A_1B() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Validate to PDF/A compliant document

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Document is valid");
        }
        else {
            resultMessage.setText("Document is not valid");
        }
    }
```

## Konversi PDF ke PDF/A_3b

```java
    public void convertPDFtoPDFa3b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Konversi PDF ke PDF/A_3a

```java
public void convertPDFtoPDFa3a() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Konversi PDF ke PDF/A_2a

```java
public void convertPDFtoPDFa2a() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Konversi PDF ke PDF/A_3U

```java
 public void convertPDFtoPDFa3u() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Buat PDF/A-3 dan lampirkan file XML

Aspose.PDF for Android via Java menawarkan fitur untuk mengonversi file PDF ke format PDF/A dan juga mendukung kemampuan menambahkan file sebagai lampiran ke dokumen PDF. Jika Anda memiliki kebutuhan untuk melampirkan file ke format kepatuhan PDF/A, maka kami merekomendasikan menggunakan nilai PDF_A_3A dari enumerasi com.aspose.pdf.PdfFormat, PDF/A_3a adalah format yang menyediakan fitur untuk melampirkan format file apa pun sebagai lampiran ke file yang mematuhi PDF/A. Namun, setelah file dilampirkan, Anda harus mengonversinya kembali ke format Pdf-3a, untuk memperbaiki metadata. Silakan lihat potongan kode berikut.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Save output document
        try {
            // load XML file
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Sample xml file");
            // Add attachment to document's attachment collection
            document.getEmbeddedFiles().add(fileSpecification);
            document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


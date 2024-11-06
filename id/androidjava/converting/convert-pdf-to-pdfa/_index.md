---
title: Mengubah File PDF ke PDF/A 
linktitle: Mengubah File PDF ke PDF/A 
type: docs
weight: 180
url: id/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: Topik ini menunjukkan kepada Anda bagaimana Aspose.PDF untuk Java memungkinkan mengubah file PDF menjadi file PDF yang sesuai dengan PDF/A.  
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF memungkinkan Anda untuk mengubah file PDF menjadi file PDF yang sesuai dengan PDF/A. Sebelum melakukannya, file harus divalidasi. Artikel ini menjelaskan caranya.

Harap dicatat bahwa kami mengikuti Adobe Preflight untuk memvalidasi kesesuaian PDF/A. Semua alat di pasaran memiliki "representasi" mereka sendiri tentang kesesuaian PDF/A. Silakan periksa artikel ini tentang [alat validasi PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) sebagai referensi. Kami memilih produk Adobe untuk memverifikasi bagaimana Aspose.PDF menghasilkan file PDF karena Adobe berada di pusat dari semua yang terkait dengan PDF.

Sebelum mengubah PDF menjadi file yang sesuai dengan PDF/A, validasi PDF menggunakan metode validate.
 Hasil validasi disimpan dalam file XML dan kemudian hasil ini juga diteruskan ke metode konversi. Anda juga dapat menentukan tindakan untuk elemen-elemen yang tidak dapat dikonversi menggunakan enumerasi [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

{{% alert color="primary" %}}

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## Konversi PDF ke PDF/A_1b

Cuplikan kode berikut menunjukkan cara mengonversi file PDF menjadi PDF yang sesuai dengan PDF/A-1b.

```java
public void convertPDFtoPDFa1b() {
        // Buka dokumen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Konversi ke dokumen sesuai PDF/A
        // Selama proses konversi, validasi juga dilakukan
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Simpan dokumen keluaran
        document.save(pdfaFileName.toString());
    }
```

Untuk melakukan validasi saja, gunakan baris kode berikut:

```java
public void ValidatePDF_A_1B() {
        // Buka dokumen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Validasi ke dokumen yang sesuai dengan PDF/A

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Dokumen valid");
        }
        else {
            resultMessage.setText("Dokumen tidak valid");
        }
    }
```

## Konversi PDF ke PDF/A_3b

```java
    public void convertPDFtoPDFa3b() {
        // Buka dokumen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Konversi ke dokumen yang sesuai dengan PDF/A
        // Selama proses konversi, validasi juga dilakukan
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Simpan dokumen keluaran
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
        // Buka dokumen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Konversi ke dokumen yang sesuai dengan PDF/A
        // Selama proses konversi, validasi juga dilakukan
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Simpan dokumen keluaran
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
        // Buka dokumen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Konversi ke dokumen yang sesuai dengan PDF/A
        // Selama proses konversi, validasi juga dilakukan
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Simpan dokumen keluaran
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
        // Buka dokumen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Konversi ke dokumen yang sesuai dengan PDF/A
        // Selama proses konversi, validasi juga dilakukan
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Simpan dokumen keluaran
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

Aspose.PDF untuk Android melalui Java menawarkan fitur untuk mengonversi file PDF ke format PDF/A dan juga mendukung kemampuan menambahkan file sebagai lampiran ke dokumen PDF.
 Jika Anda memiliki persyaratan untuk melampirkan file ke format kepatuhan PDF/A, maka kami merekomendasikan menggunakan nilai PDF_A_3A dari enumerasi com.aspose.pdf.PdfFormat, PDF/A_3a adalah format yang menyediakan fitur untuk melampirkan format file apapun sebagai lampiran ke file yang sesuai dengan PDF/A. Namun, setelah file dilampirkan, Anda harus mengonversinya lagi ke format Pdf-3a, untuk memperbaiki metadata. Silakan lihat potongan kode berikut.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Buka dokumen
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Konversi ke dokumen yang sesuai dengan PDF/A
        // Selama proses konversi, validasi juga dilakukan
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Simpan dokumen keluaran
        try {
            // muat file XML
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Contoh file xml");
            // Tambahkan lampiran ke koleksi lampiran dokumen
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
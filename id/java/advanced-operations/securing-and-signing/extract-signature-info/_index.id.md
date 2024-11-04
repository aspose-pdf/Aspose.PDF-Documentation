---
title: Extract Image and Signature Information
linktitle: Extract Image and Signature Information
type: docs
weight: 30
url: /java/extract-image-and-signature-information/
description: Anda dapat mengekstrak gambar dari bidang tanda tangan dan mengekstrak informasi tanda tangan menggunakan kelas SignatureField dengan Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mengekstrak Gambar dari Bidang Tanda Tangan

Aspose.PDF untuk Java mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) dan saat menandatangani dokumen, Anda juga dapat mengatur gambar untuk SignatureAppearance. Sekarang, API ini juga menyediakan kemampuan untuk mengekstrak informasi tanda tangan serta gambar yang terkait dengan bidang tanda tangan.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode [ExtractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) ke kelas [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak gambar dari objek SignatureField:

```java
public class ExampleExtractImageAndSignature {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void ExtractingImageFromSignatureField() {
        Document pdfDocument = new Document(_dataDir + "ExtractingImage.pdf");

        int i = 0;
        try {
            for (WidgetAnnotation field : pdfDocument.getForm()) {
                SignatureField sf = (SignatureField) field;
                if (sf != null) {
                    FileOutputStream output = new FileOutputStream(_dataDir + "im" + i + ".jpeg");
                    InputStream tempStream = sf.extractImage();
                    byte[] b = new byte[tempStream.available()];
                    tempStream.read(b);
                    output.write(b);
                    output.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (pdfDocument != null)
                pdfDocument.dispose();
        }

    }
```

### Ganti Gambar Tanda Tangan

Kadang-kadang Anda mungkin memiliki persyaratan untuk hanya mengganti gambar dari bidang tanda tangan yang sudah ada di dalam file PDF. Untuk memenuhi persyaratan ini, pertama, kita perlu mencari bidang formulir di dalam file PDF, mengidentifikasi bidang Tanda Tangan, mendapatkan dimensi (dimensi Persegi Panjang) dari bidang tanda tangan, dan kemudian menempelkan gambar dengan dimensi yang sama.

## Ekstrak Informasi Tanda Tangan

Aspose.PDF untuk Java mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField). Saat ini, kita juga dapat menentukan keabsahan sertifikat tetapi kita tidak dapat mengekstrak seluruh sertifikat. Informasi yang dapat diekstrak adalah kunci publik, sidik jari, penerbit, dll.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode [ExtractCertificate](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractCertificate--) ke kelas [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak sertifikat dari objek SignatureField:

```java
    public static void ExtractSignatureInformation() throws IOException {
        String input = _dataDir + "ExtractSignatureInfo.pdf";
        Document pdfDocument = new Document(input);

        for (WidgetAnnotation field : pdfDocument.getForm()) {
            SignatureField sf = (SignatureField) field;
            if (sf != null) {
                InputStream cerStream = sf.extractCertificate();
                if (cerStream != null) {

                    byte[] buffer = new byte[cerStream.available()];
                    cerStream.read(buffer);

                    File targetFile = new File(_dataDir+"targetFile.cer");
                    OutputStream outStream = new FileOutputStream(targetFile);
                    outStream.write(buffer);
                    outStream.close();
                }
            }
        }
    }
}
```
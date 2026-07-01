---
title: Konversi PDF ke teks
linktitle: Konversi PDF ke teks
type: docs
weight: 120
url: /id/androidjava/convert-pdf-to-txt/
lastmod: "2026-07-01"
description: Dengan Aspose.PDF for Android via Java Anda dapat mengonversi seluruh dokumen PDF menjadi file teks atau mengonversi hanya satu halaman PDF menjadi file teks.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


{{% alert color="primary" %}} 

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## Konversi halaman PDF ke file teks

Anda dapat mengonversi dokumen PDF menjadi file TXT dengan Aspose.PDF for Android via Java. Anda harus menggunakan metode Visit dari [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) kelas untuk menyelesaikan tugas ini.

Potongan kode berikut menjelaskan cara mengekstrak teks dari halaman tertentu.

```java
public void convertPDFPagesToTXT() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        TextAbsorber ta = new TextAbsorber();
        int[] pages = new int[] { 1, 3, 4 };

        for (int page : pages) {
            ta.visit(document.getPages().get_Item(page));
        }
        File txtFileName = new File(fileStorage, "PDF-to-Text.txt");

        // Save the extracted text in text file
        BufferedWriter writer;
        try {
            writer = new BufferedWriter(new FileWriter(txtFileName));
            writer.write(ta.getText());
            writer.close();
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


---
title: Konversi PDF ke teks 
linktitle: Konversi PDF ke teks
type: docs
weight: 120
url: /androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: Dengan Aspose.PDF untuk Android melalui Java Anda dapat mengonversi seluruh dokumen PDF menjadi file teks atau mengonversi hanya halaman PDF menjadi file teks.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


{{% alert color="primary" %}} 

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## Konversi halaman PDF menjadi file teks

Anda dapat mengonversi dokumen PDF menjadi file TXT dengan Aspose.PDF untuk Android melalui Java. Anda harus menggunakan metode Visit dari kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) untuk menyelesaikan tugas ini.

Cuplikan kode berikut menjelaskan cara mengekstrak teks dari halaman tertentu.

```java
public void convertPDFPagesToTXT() {
        // Buka dokumen
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

        // Simpan teks yang diekstraksi dalam file teks
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
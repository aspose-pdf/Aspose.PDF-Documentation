---
title: Convert Text to PDF 
linktitle: Convert Text to PDF
type: docs
weight: 300
url: /androidjava/convert-text-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF untuk Android via Java memungkinkan Anda untuk mengonversi file teks biasa ke PDF atau mengonversi file teks yang telah diformat sebelumnya ke PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF untuk Android via Java** menyediakan kemampuan untuk mengonversi file Teks ke format PDF. Dalam artikel ini, kami menunjukkan betapa mudah dan efisiennya kita dapat mengonversi file teks ke PDF menggunakan Aspose.PDF.

Ketika Anda perlu mengonversi file Teks ke PDF, awalnya baca file teks sumber dalam beberapa pembaca.
 Kami telah menggunakan StringBuilder untuk membaca konten file Teks. Instansiasi objek Document dan tambahkan halaman baru di koleksi Pages. Buat objek baru dari TextFragment dan berikan objek StringBuilder ke konstruktornya. Tambahkan paragraf baru dalam koleksi Paragraphs menggunakan objek TextFragment dan simpan file PDF yang dihasilkan menggunakan metode Save dari kelas Document.

## Konversi file teks biasa ke PDF

```java
public void convertTXTtoPDF_Simple () {
        // Inisialisasi objek dokumen

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // Instansiasi objek Document dengan memanggil konstruktor kosongnya
        document=new Document();

        // Tambahkan halaman baru dalam koleksi Pages dari Document
        Page page=document.getPages().add();

        String string;
        StringBuilder stringBuilder=new StringBuilder();
        InputStream is;
        try {
            is=new FileInputStream(txtDocumentFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        BufferedReader reader=new BufferedReader(new InputStreamReader(is));
        while (true) {
            try {
                if ((string=reader.readLine()) == null) break;
            } catch (IOException e) {
                resultMessage.setText(e.getMessage());
                return;
            }
            stringBuilder.append(string).append("\n");
        }
        try {
            is.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Buat instance dari TextFragment dan berikan teks dari objek reader ke
        // konstruktornya sebagai argumen
        TextFragment text=new TextFragment(stringBuilder.toString());

        // Tambahkan paragraf teks baru dalam koleksi paragraf dan berikan objek
        // TextFragment
        page.getParagraphs().add(text);

        // Simpan file PDF yang dihasilkan
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Konversi file teks pra-format ke PDF

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // Baca file teks sebagai array string
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Buat objek Document baru dengan memanggil konstruktor kosongnya
        document=new Document();

        // Tambahkan halaman baru dalam koleksi Pages dari Document
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // Atur margin kiri dan kanan untuk presentasi yang lebih baik
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // periksa apakah baris mengandung karakter "form feed"
            // lihat https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Buat instance dari TextFragment dan
                // berikan baris ke
                // konstruktor sebagai argumen
                TextFragment text=new TextFragment(line);

                // Tambahkan paragraf teks baru dalam koleksi paragraf dan berikan objek TextFragment
                page.getParagraphs().add(text);
            }
        }
        // Simpan file PDF hasil
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```
---
title: Konversi Teks ke PDF
linktitle: Konversi Teks ke PDF
type: docs
weight: 300
url: /id/androidjava/convert-text-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java memungkinkan Anda mengonversi file teks biasa ke PDF atau mengonversi file teks berformat sebelumnya ke PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF for Android via Java** menyediakan kemampuan untuk mengonversi file Teks ke format PDF. Dalam artikel ini, kami menunjukkan betapa mudah dan efisiennya kami dapat mengonversi file teks ke PDF menggunakan Aspose.PDF.

Ketika Anda perlu mengonversi file Teks ke PDF, pertama‑tama baca file teks sumber menggunakan suatu pembaca. Kami telah menggunakan StringBuilder untuk membaca isi file Teks. Buat instance objek Document dan tambahkan halaman baru ke dalam koleksi Pages. Buat objek baru TextFragment dan berikan objek StringBuilder ke konstruktor-nya. Tambahkan paragraf baru ke dalam koleksi Paragraphs menggunakan objek TextFragment dan simpan file PDF yang dihasilkan menggunakan metode Save dari kelas Document.

## Konversi file teks biasa ke PDF

```java
public void convertTXTtoPDF_Simple () {
        // Initialize document object

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // Instantiate a Document object by calling its empty constructor
        document=new Document();

        // Add a new page in Pages collection of Document
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


        // Create an instance of TextFragment and pass the text from reader object to its
        // constructor as argument
        TextFragment text=new TextFragment(stringBuilder.toString());

        // Add a new text paragraph in paragraphs collection and pass the TextFragment
        // object
        page.getParagraphs().add(text);

        // Save resultant PDF file
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Konversi file teks berformat pra ke PDF

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // Read the text file as array of string
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate a Document object by calling its empty constructor
        document=new Document();

        // Add a new page in Pages collection of Document
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // Set left and right margins for better presentation
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // check if line contains "form feed" character
            // see https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Create an instance of TextFragment and
                // pass the line to its
                // constructor as argument
                TextFragment text=new TextFragment(line);

                // Add a new text paragraph in paragraphs collection and pass the TextFragment
                // object
                page.getParagraphs().add(text);
            }
        }
        // Save resultant PDF file
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```




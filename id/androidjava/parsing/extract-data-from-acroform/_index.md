---
title:  Ekstrak data dari AcroForm
linktitle:  Ekstrak data dari AcroForm
type: docs
weight: 50
url: /id/androidjava/extract-data-from-acroform/
description: AcroForms ada di banyak dokumen PDF. Artikel ini bertujuan membantu Anda memahami cara mengekstrak data dari AcroForms dengan Aspose.PDF.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak bidang formulir dari dokumen PDF

Aspose.PDF for Android via Java tidak hanya memungkinkan Anda membuat dan mengisi bidang formulir, tetapi juga memudahkan mengekstrak data bidang formulir atau informasi bidang formulir dari file PDF.

Misalkan kita tidak mengetahui nama-nama bidang formulir sebelumnya. Maka kita harus mengiterasi setiap halaman dalam PDF untuk mengekstrak informasi tentang semua AcroForms dalam PDF serta nilai bidang formulir. Untuk mengakses formulir kita perlu menggunakan [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) metode.

```java
 public void extractFormFields () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get values from all fields
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Field Name: ");
            sb.append(formField.getPartialName());
            sb.append(" Value: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```

Jika Anda mengetahui nama bidang formulir yang ingin Anda ekstrak nilainya, maka Anda dapat menggunakan indeks pada koleksi Documents.Form untuk dengan cepat mengambil data ini.

## Ambil nilai bidang formulir berdasarkan judul

Properti Value dari bidang formulir memungkinkan Anda untuk mendapatkan nilai dari bidang tertentu. Untuk mendapatkan nilai, dapatkan bidang formulir dari [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) objek [koleksi bidang formulir](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). Contoh ini memilih sebuah [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) dan mengambil nilainya menggunakan [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) metode.

```java

    public void extractFormDataByName () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Last Name: " + textBoxField1.getValue());

    }
```

## Ekstrak Data ke XML dari File PDF

Kelas Form memungkinkan Anda mengekspor data ke file XML dari file PDF menggunakan metode ExportXml. Untuk mengekspor data ke XML, Anda perlu membuat objek kelas Form dan kemudian memanggil metode ExportXml menggunakan objek FileStream. Akhirnya, Anda dapat menutup objek FileStream dan membuang (dispose) objek Form. Potongan kode berikut menunjukkan cara mengekspor data ke file XML.

```java
public void extractFormFieldsToXML () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form();
        form.bindPdf(document);
        File file=new File(fileStorage, "output.xml");
        try {
            // Create xml file.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Export data
            form.exportXml(xmlOutputStream);

            // Close file stream
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Close the document
        form.dispose();
    }
```

## Ekspor Data ke FDF dari Berkas PDF

Untuk mengekspor data formulir PDF ke file XFDF, kita dapat menggunakan [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) metode dalam [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) kelas.

Harap dicatat, bahwa itu adalah kelas dari `com.aspose.pdf.facades`. Meskipun namanya serupa, kelas ini memiliki tujuan yang sedikit berbeda.

Untuk mengekspor data ke FDF, Anda perlu membuat objek dari `Form` kelas dan kemudian panggil `exportXfdf` metode menggunakan `OutputStream` objek. Potongan kode berikut menunjukkan cara mengekspor data ke file XFDF.

```java
public void extractFormExportFDF () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.fdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Export data
            form.exportFdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Ekspor Data ke XFDF dari File PDF

Untuk mengekspor data formulir PDF ke file XFDF, kita dapat menggunakan [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) metode dalam [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) kelas.

Untuk mengekspor data ke XFDF, Anda perlu membuat sebuah objek dari `Form` kelas dan kemudian panggil `exportXfdf` metode menggunakan `OutputStream` objek. 
Potongan kode berikut menunjukkan cara mengekspor data ke file XFDF.

```java
    public void extractFormExportXFDF () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.xfdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Export data
            form.exportXfdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


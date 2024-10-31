---
title: Ekstraksi data dari AcroForm 
linktitle: Ekstraksi data dari AcroForm
type: docs
weight: 50
url: /androidjava/extract-data-from-acroform/
description: AcroForms ada di banyak dokumen PDF. Artikel ini bertujuan untuk membantu Anda memahami cara mengekstraksi data dari AcroForms dengan Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak bidang formulir dari dokumen PDF

Aspose.PDF untuk Android melalui Java tidak hanya memungkinkan Anda membuat dan mengisi bidang formulir, tetapi juga memudahkan untuk mengekstraksi data bidang formulir atau informasi bidang formulir dari file PDF.

Misalkan kita tidak mengetahui nama-nama bidang formulir sebelumnya. Maka kita harus melakukan iterasi pada setiap halaman di PDF untuk mengekstraksi informasi tentang semua AcroForms di PDF serta nilai dari bidang formulir. Untuk mendapatkan akses ke formulir, kita perlu menggunakan metode [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
 public void extractFormFields () {
        // Buka dokumen
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Dapatkan nilai dari semua bidang
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Nama Bidang: ");
            sb.append(formField.getPartialName());
            sb.append(" Nilai: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```


Jika Anda mengetahui nama kolom formulir yang ingin Anda ekstrak nilainya, maka Anda dapat menggunakan pengindeks dalam koleksi Documents.Form untuk dengan cepat mengambil data ini.

## Ambil nilai kolom formulir berdasarkan judul

Properti Value dari kolom formulir memungkinkan Anda untuk mendapatkan nilai dari kolom tertentu. Untuk mendapatkan nilainya, ambil kolom formulir dari [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) objek [koleksi kolom formulir](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). Contoh ini memilih [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) dan mengambil nilainya menggunakan metode [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java

    public void extractFormDataByName () {
        // Buka dokumen
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

Kelas Form memungkinkan Anda mengekspor data ke file XML dari file PDF menggunakan metode ExportXml. Untuk mengekspor data ke XML, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportXml menggunakan objek FileStream. Terakhir, Anda dapat menutup objek FileStream dan membuang objek Form. Potongan kode berikut menunjukkan cara mengekspor data ke file XML.

```java
public void extractFormFieldsToXML () {
        // Buka dokumen
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
            // Buat file xml.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Ekspor data
            form.exportXml(xmlOutputStream);

            // Tutup file stream
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Tutup dokumen
        form.dispose();
    }
```


## Ekspor Data ke FDF dari File PDF

Untuk mengekspor data formulir PDF ke file XFDF, kita dapat menggunakan metode [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) dalam kelas [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Harap dicatat, bahwa ini adalah kelas dari `com.aspose.pdf.facades`. Meskipun namanya mirip, kelas ini memiliki tujuan yang sedikit berbeda.

Untuk mengekspor data ke FDF, Anda perlu membuat objek dari kelas `Form` dan kemudian memanggil metode `exportXfdf` menggunakan objek `OutputStream`. Cuplikan kode berikut menunjukkan cara mengekspor data ke file XFDF.

```java
public void extractFormExportFDF () {
        // Buka dokumen
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

            // Ekspor data
            form.exportFdf(fdfOutputStream);

            // Tutup aliran file
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Ekspor Data ke XFDF dari File PDF

Untuk mengekspor data formulir PDF ke file XFDF, kita dapat menggunakan metode [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) dalam kelas [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Untuk mengekspor data ke XFDF, Anda perlu membuat objek dari kelas `Form` dan kemudian memanggil metode `exportXfdf` menggunakan objek `OutputStream`. Cuplikan kode berikut menunjukkan cara mengekspor data ke file XFDF.

```java
    public void extractFormExportXFDF () {
        // Buka dokumen
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

            // Ekspor data
            form.exportXfdf(fdfOutputStream);

            // Tutup file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
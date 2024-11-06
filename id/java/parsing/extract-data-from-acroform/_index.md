---
title: Ekstrak data dari AcroForm
linktitle: Ekstrak data dari AcroForm
type: docs
weight: 50
url: id/java/extract-data-from-acroform/
description: AcroForms ada di banyak dokumen PDF. Artikel ini bertujuan untuk membantu Anda memahami cara mengekstrak data dari AcroForms menggunakan Java dan Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak bidang formulir dari dokumen PDF

Aspose.PDF untuk Java tidak hanya memungkinkan Anda membuat dan mengisi bidang formulir, tetapi juga memudahkan untuk mengekstrak data bidang formulir atau informasi bidang formulir dari file PDF.

Misalkan kita tidak mengetahui nama-nama bidang formulir terlebih dahulu. Maka kita harus mengiterasi setiap halaman di PDF untuk mengekstrak informasi tentang semua AcroForm di PDF serta nilai dari bidang formulir. Untuk mendapatkan akses ke formulir kita perlu menggunakan metode [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
public static void ExtractFormFields() {
    String path= "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);
    // Dapatkan nilai dari semua bidang
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        System.out.println("Nama Bidang :" + formField.getPartialName());
        System.out.println("Nilai : " + formField.getValue());
    }
}
```


Jika Anda mengetahui nama dari field formulir yang ingin Anda ekstrak nilainya, maka Anda dapat menggunakan indexer dalam koleksi Documents.Form untuk dengan cepat mengambil data ini.

## Mengambil nilai field formulir berdasarkan judul

Properti Value dari field formulir memungkinkan Anda untuk mendapatkan nilai dari field tertentu. Untuk mendapatkan nilainya, dapatkan field formulir dari [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) objek [koleksi field formulir](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). Contoh ini memilih [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) dan mengambil nilainya menggunakan metode [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
public static void ExtractFormDataByName() {
    String fileName = _dataDir+"/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(fileName);        
    com.aspose.pdf.TextBoxField textBoxField1 = (com.aspose.pdf.TextBoxField)document.getForm().get("Last Name");

    System.out.println("Last Name :" + textBoxField1.getValue());
}
```


## Ekstrak bidang formulir dari dokumen PDF ke JSON

Untuk mengekspor data formulir ke JSON, kami merekomendasikan menggunakan pustaka pihak ketiga seperti [Gson](https://github.com/google/gson).
Cuplikan berikut menunjukkan cara mengekspor `Name` dan `Value` ke JSON:

```java
public static void ExtractFormFieldsToJson() {
    String path = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);

    java.util.List<FormElement> formData = new java.util.ArrayList<FormElement>();
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        formData.add(new FormElement(formField.getPartialName(), formField.getValue()));
    }

    Gson gson = new Gson();
    String jsonString = gson.toJson(formData);
    System.out.println(jsonString);
}
```

Dalam contoh ini kami menggunakan kelas tambahan

```java
public class FormElement {
    public FormElement(String partialName, String Value) {
        this.Name = partialName;
        this.Value = Value;
    }
    public String Name;
    public String Value;
}
```


## Ekstrak Data ke XML dari File PDF

Kelas Form memungkinkan Anda untuk mengekspor data ke file XML dari file PDF menggunakan metode ExportXml. Untuk mengekspor data ke XML, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportXml menggunakan objek FileStream. Akhirnya, Anda dapat menutup objek FileStream dan membuang objek Form. Cuplikan kode berikut menunjukkan cara mengekspor data ke file XML.

```java
public static void ExtractFormFieldsToXML() {

    String dataDir = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";

    // Buka dokumen
    com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
    form.bindPdf(dataDir + "input.pdf");

    try {
        // Buat file XML.
        FileOutputStream xmlOutputStream;

        xmlOutputStream = new FileOutputStream(dataDir + "input.xml");
        // Ekspor data
        form.exportXml(xmlOutputStream);

        // Tutup file stream
        xmlOutputStream.close();

    } catch (IOException e) {

        e.printStackTrace();
    }

    // Tutup dokumen
    form.dispose();
    ;
}
```


## Ekspor Data ke FDF dari File PDF

Untuk mengekspor data formulir PDF ke file XFDF, kita dapat menggunakan metode [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) dalam kelas [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Harap dicatat, bahwa ini adalah kelas dari `com.aspose.pdf.facades`. Meskipun namanya mirip, kelas ini memiliki tujuan yang sedikit berbeda.

Untuk mengekspor data ke FDF, Anda perlu membuat objek dari kelas `Form` dan kemudian memanggil metode `exportXfdf` menggunakan objek `OutputStream`. Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengekspor data ke file XFDF.

```java
 public static void ExtractFormExportFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.fdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Ekspor data
            form.exportFdf(fdfOutputStream);

            // Tutup file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: tangani pengecualian
            e.printStackTrace();
        }

    }
```


## Ekspor Data ke XFDF dari File PDF

Untuk mengekspor data formulir PDF ke file XFDF, kita dapat menggunakan metode [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) dalam kelas [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Untuk mengekspor data ke XFDF, Anda perlu membuat objek dari kelas `Form` dan kemudian memanggil metode `exportXfdf` menggunakan objek `OutputStream`.
Cuplikan kode berikut menunjukkan cara mengekspor data ke file XFDF.

```java
public static void ExtractFormExportXFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Ekspor data
            form.exportXfdf(fdfOutputStream);

            // Tutup file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: tangani pengecualian
            e.printStackTrace();
        }
    }
```
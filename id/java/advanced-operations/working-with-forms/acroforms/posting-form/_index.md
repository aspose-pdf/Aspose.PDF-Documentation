---
title: "Mengirim Formulir di PDF via Java"
linktitle: "Mengirim Formulir"
type: docs
weight: 75
url: /id/java/posting-form/
description: Tambahkan tombol submit dan tindakan pengiriman ke PDF AcroForms menggunakan Aspose.PDF for Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan tombol submit dan tindakan posting form ke file PDF dengan Java"
Abstract: Artikel ini menunjukkan cara menambahkan fungsionalitas submit ke formulir PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pembuatan tombol submit dengan FormEditor dan pembuatan bidang tombol kustom yang menggunakan SubmitFormAction untuk kontrol lebih besar atas URL pengiriman dan flag.
---
Aspose.PDF for Java mendukung pembuatan tombol submit berbasis fasad maupun berbasis DOM.

## Menambahkan tombol kirim dengan FormEditor

1. Buat fasad [`FormEditor`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) untuk dokumen PDF sumber.
1. Tambahkan objek tombol kirim yang dikonfigurasi melalui fasad [`FormEditor`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/).
1. Simpan dokumen PDF yang telah diperbarui.

```java
public static void addSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    editor.bindPdf(inputFile.toString());
    try {
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show",
                100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

## Menambahkan aksi submit secara manual

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`SubmitFormAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) dan URL [`FileSpecification`](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).
1. Buat [`ButtonField`](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) pada [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target dan tetapkan tindakan submit.
1. Simpan PDF yang diperbarui [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        submitAction.setUrl(new FileSpecification("http://localhost:3000/submit"));
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), new Rectangle(10, 10, 100, 40));
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getPdfActions().add(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```

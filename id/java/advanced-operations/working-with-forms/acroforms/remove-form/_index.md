---
title: "Menghapus Form dari PDF di Java"
linktitle: "Menghapus Form"
type: docs
weight: 70
url: /id/java/remove-form/
description: Hapus objek Form dari halaman PDF menggunakan Aspose.PDF for Java, termasuk pembersihan penuh dan penghapusan terarah.
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menghapus sumber daya Form dari halaman PDF dengan Java"
Abstract: Artikel ini menjelaskan cara menghapus sumber daya Form dari dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pembersihan semua Form dari sebuah halaman dan menghapus hanya sumber daya Form Typewriter yang dipilih setelah memfilter koleksi Form halaman.
---
Contoh-contoh ini menghapus sumber daya Form dari sebuah halaman daripada hanya mengubah nilai bidang.

## Menghapus semua sumber form dari halaman

Gunakan contoh ini ketika setiap sumber form pada halaman yang dipilih harus dihapus dalam satu operasi.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses [`XFormCollection`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) untuk halaman target.
1. Kosongkan koleksi dan simpan dokumen yang diperbarui.

```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## Menghapus sumber Form tertentu

Gunakan contoh ini ketika hanya sumber Form tertentu, seperti Form Typewriter, yang harus dihapus.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Akses [`XFormCollection`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) untuk halaman target.
1. Filter [`XForm`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) sumber daya yang ingin Anda hapus dan menghapusnya dari koleksi.
1. Simpan PDF yang diperbarui [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void removeSpecifiedForm(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        List<String> formNames = new ArrayList<>();
        for (XForm form : forms) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                formNames.add(forms.getFormName(form));
            }
        }
        for (String formName : formNames) {
            forms.delete(formName);
        }
        document.save(outputFile.toString());
    }
}
```

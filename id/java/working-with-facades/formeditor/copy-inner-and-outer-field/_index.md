---
title: Salin Bidang Dalam dan Luar
type: docs
weight: 40
url: /id/java/copy-inner-and-outer-field/
description: Bagian ini menjelaskan cara menyalin bidang dalam dan luar dengan com.aspose.pdf.facades menggunakan Kelas FormEditor.
lastmod: "2021-06-05"
draft: false
---

Metode [copyInnerField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyInnerField-java.lang.String-java.lang.String-int-) memungkinkan Anda untuk menyalin sebuah bidang di file yang sama, pada koordinat yang sama, di halaman yang ditentukan. Metode ini memerlukan nama bidang yang ingin Anda salin, nama bidang baru, dan nomor halaman di mana bidang tersebut perlu disalin. Kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) menyediakan metode ini. Cuplikan kode berikut menunjukkan cara menyalin bidang di lokasi yang sama dalam file yang sama.

```java
    public static void CopyInnerField() {
        FormEditor editor = new FormEditor();
        Document document = new Document(_dataDir + "Sample-Form-01.pdf");
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyInnerField("Last Name", "Last Name 2", 2);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## Salin Field Luar dalam File PDF yang Ada

Metode [copyOuterField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyOuterField-java.lang.String-java.lang.String-) memungkinkan Anda untuk menyalin field formulir dari file PDF eksternal dan kemudian menambahkannya ke file PDF input pada lokasi yang sama dan nomor halaman yang ditentukan. Metode ini memerlukan file PDF dari mana field perlu disalin, nama field, dan nomor halaman di mana field perlu disalin. Metode ini disediakan oleh kelas [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Cuplikan kode berikut menunjukkan cara menyalin field dari file PDF eksternal.

```java
  public static void CopyOuterField() {
        FormEditor editor = new FormEditor();
        Document document = new Document();
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
        editor.save(_dataDir + "Sample-Form-02-mod.pdf");
    }
```
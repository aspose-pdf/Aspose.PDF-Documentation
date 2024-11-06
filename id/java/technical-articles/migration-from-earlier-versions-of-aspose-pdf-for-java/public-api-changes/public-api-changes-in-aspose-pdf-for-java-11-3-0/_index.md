---
title: Perubahan API Publik di Aspose.PDF untuk Java 11.3.0
type: docs
weight: 130
url: id/java/public-api-changes-in-aspose-pdf-for-java-11-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini mencantumkan perubahan API publik yang diperkenalkan dalam Aspose.PDF untuk Java 11.3.0. Ini tidak hanya mencakup metode publik baru dan yang sudah usang, tetapi juga deskripsi tentang perubahan perilaku di belakang layar dalam Aspose.PDF untuk Java yang dapat mempengaruhi kode yang ada. Setiap perilaku yang diperkenalkan yang dapat dilihat sebagai regresi dan mengubah perilaku yang ada sangat penting dan didokumentasikan di sini.

{{% /alert %}}

**Perubahan dalam kelas com.aspose.pdf.Annotation:**

Metode yang ditambahkan:

- public boolean isUpdateAppearanceOnConvert()
- public void setUpdateAppearanceOnConvert(boolean value)

**Perubahan dalam kelas com.aspose.pdf.BaseParagraph:**

Metode yang ditambahkan:

- public int getZIndex()
- public void setZIndex(int)

**Perubahan dalam kelas com.aspose.pdf.MemoryCleaner:**

Metode yang ditambahkan:

- public void clearAllTempFiles()

**Perubahan dalam kelas com.aspose.pdf.Page:**

Methods ditambahkan:

- public byte[] asByteArray(com.aspose.pdf.devices.Resolution)

**Perubahan dalam kelas com.aspose.pdf.Table:**

Metode ditambahkan:

- public com.aspose.pdf.Table getParentTable()
- public void setParentTable(com.aspose.pdf.Table)

**Perubahan dalam kelas com.aspose.pdf.TextSearchOptions:**

Metode ditambahkan:

- public boolean isIgnoreShadowText()
- public void setIgnoreShadowText(boolean value)
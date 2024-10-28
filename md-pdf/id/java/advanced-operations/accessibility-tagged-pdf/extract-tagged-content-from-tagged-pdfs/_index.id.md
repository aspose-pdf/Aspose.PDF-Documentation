---
title: Ekstrak Konten Berlabel dari PDF
linktitle: Ekstrak Konten Berlabel
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Artikel ini menjelaskan cara mengekstrak konten berlabel dari dokumen PDF menggunakan Aspose.PDF untuk Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mendapatkan Konten PDF Berlabel

Untuk mendapatkan konten dari Dokumen PDF dengan Teks Berlabel, Aspose.PDF menawarkan metode [getTaggedContent()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getTaggedContent--) dari Kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Potongan kode berikut menunjukkan cara mendapatkan konten dari dokumen PDF dengan Teks Berlabel:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = "pathTodir";

// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

//
// Bekerja dengan konten Tagged Pdf
//

// Tetapkan Judul dan Bahasa untuk Dokumen
taggedContent.setTitle("Simple Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Simpan Dokumen Tagged Pdf
document.save(path + "TaggedPDFContent.pdf");
```


## Mendapatkan Struktur Root

Untuk mendapatkan struktur root dari Dokumen PDF Bertanda, Aspose.PDF menawarkan metode [getStructTreeRootElement]()(https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#getStructTreeRootElement--) dan **getStructureElement()** dari Antarmuka [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Potongan kode berikut menunjukkan cara mendapatkan struktur root dari Dokumen PDF Bertanda:

```java
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = "pathTodir";
// Buat Dokumen Pdf
Document document = new Document();

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Tetapkan Judul dan Bahasa untuk Dokumen
taggedContent.setTitle("Dokumen Pdf Bertanda");
taggedContent.setLanguage("en-US");

// Properti StructTreeRootElement dan RootElement digunakan untuk akses ke
// objek StructTreeRoot dari dokumen pdf dan ke elemen struktur root (elemen struktur Dokumen).
StructTreeRootElement structTreeRootElement = taggedContent.getStructTreeRootElement();
StructureElement rootElement = taggedContent.getRootElement();
```


## Mengakses Elemen Anak

Untuk mengakses elemen anak dari Dokumen PDF yang Ditandai, Aspose.PDF menawarkan Kelas **ElementList**. Cuplikan kode berikut menunjukkan cara mengakses elemen anak dari Dokumen PDF yang Ditandai:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
String path = "pathTodir";
// Buka Dokumen Pdf
Document document = new Document( path +"StructureElements.pdf");

// Dapatkan Konten untuk bekerja dengan TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Akses ke elemen root
ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement =  (StructureElement)element;

        // Dapatkan properti
        String title = structureElement.getTitle();
        String language = structureElement.getLanguage();
        String actualText = structureElement.getActualText();
        String expansionText = structureElement.getExpansionText();
        String alternativeText = structureElement.getAlternativeText();
    }
}

// Akses ke elemen anak dari elemen pertama di elemen root
elementList = taggedContent.getRootElement().getChildElements().get_Item(1).getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement = (StructureElement)element;

        // Atur properti
        structureElement.setTitle("title");
        structureElement.setLanguage("fr-FR");
        structureElement.setActualText("actual text");
        structureElement.setExpansionText("exp");
        structureElement.setAlternativeText("alt");
    }
}

// Simpan Dokumen Pdf yang Ditandai
document.save( path +"AccessChildrenElements.pdf");
```
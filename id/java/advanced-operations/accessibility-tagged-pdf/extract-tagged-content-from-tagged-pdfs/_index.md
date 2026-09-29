---
title: Ekstrak Konten yang Ditandai dari PDF dalam Java
linktitle: Ekstrak Konten yang Ditandai
type: docs
weight: 20
url: /id/java/extract-tagged-content-from-tagged-pdfs/
description: Pelajari cara memeriksa konten PDF yang ditandai dalam Java dengan Aspose.PDF, termasuk akses konten yang ditandai, akses struktur akar, dan elemen struktur anak.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Gunakan API ini ketika Anda perlu memeriksa pohon struktur logis dari PDF yang ditandai dan memeriksa atau memperbarui metadata elemen struktur.

## Dapatkan metadata konten yang ditandai

Gunakan contoh ini ketika Anda membutuhkan akses ke wadah konten yang ditandai dan ingin mendefinisikan metadata dokumen dasar seperti judul dan bahasa.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Dapatkan [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) objek dari dokumen.
1. Setel metadata konten bertag dan simpan file output.

```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## Dapatkan struktur akar dari PDF bertanda

Contoh ini menunjukkan cara memeriksa objek akar yang mewakili pohon struktur dari PDF yang ditandai.

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan mendapatkan konten yang ditandai.
1. Atur metadata dokumen yang diperlukan.
1. Baca dan cetak akar pohon struktur serta elemen akar logis, kemudian simpan file.

```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## Akses dan perbarui elemen struktur anak

Gunakan contoh ini ketika Anda perlu mengiterasi elemen anak dalam pohon struktur, memeriksa properti mereka, dan memperbarui metadata yang dipilih.

1. Buka PDF bertanda sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Baca elemen anak dari akar pohon struktur dan cetak properti yang tersedia.
1. Akses elemen anak dari anak akar pertama, perbarui metadata mereka, dan simpan dokumen.

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```

---
title: "Mengelola header dan footer PDF menggunakan Java"
linktitle: "Mengelola header dan footer PDF"
type: docs
weight: 70
url: /id/java/artifacts-header-footer/
description: Pelajari cara menambahkan dan menghapus artefak header dan footer dalam dokumen PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menambahkan, menyesuaikan, dan menghapus header serta footer PDF menggunakan Java"
Abstract: Artikel ini menjelaskan cara mengelola artefak header dan footer dalam dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup pembuatan objek `HeaderArtifact` dan `FooterArtifact` yang dapat digunakan kembali dengan keadaan teks khusus dan perataan, menambahkannya ke halaman, serta menghapus artefak header dan footer yang ada.
---
Artefak header dan footer adalah elemen paginasi non-konten yang biasanya digunakan untuk label berulang, pengidentifikasi halaman, dan bingkai tata letak.

## Membuat artefak header

Gunakan pembantu ini ketika Anda membutuhkan artefak header yang dapat digunakan kembali dengan gaya teks dan perataan yang konsisten.

1. Buat [`HeaderArtifact`](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. Setel teksnya, pengaturan font, dan warna latar depan.
1. Konfigurasikan perataan horizontal dan kembalikan artefak tersebut.

```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## Membuat artefak footer

Pembantu ini membuat artefak footer yang dapat digunakan kembali dengan pola styling yang sama seperti artefak header.

1. Buat [`FooterArtifact`](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. Atur teks, status teks, dan warna latar depan.
1. Konfigurasikan perataan dan kembalikan artefak.

```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## Menambahkan artefak header

Gunakan contoh ini ketika sebuah halaman harus menampilkan artefak header yang dapat digunakan kembali.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat artefak header melalui metode pembantu.
1. Tambahkan artefak ke halaman dan simpan file keluaran.

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## Menambahkan artefak footer

Gunakan contoh ini ketika halaman harus menampilkan artefak footer dengan format yang dapat digunakan kembali.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat artefak footer melalui metode helper.
1. Tambahkan artefak ke halaman dan simpan file keluaran.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## Menghapus artefak header dan footer

Gunakan pendekatan ini ketika artefak header dan footer yang ada perlu dihapus dari halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan koleksi artefak halaman dalam urutan terbalik.
1. Hapus artefak paginasi yang subtipe-nya adalah header atau footer, lalu simpan dokumen.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

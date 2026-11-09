---
title: Menambahkan header dan footer pada PDF dengan Java
linktitle: Menambahkan header dan footer
type: docs
weight: 70
url: /id/java/artifacts-header-footer/
description: Buat artefak header dan footer yang bergaya dan tambahkan ke halaman PDF dalam Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan header dan footer pada PDF dengan Java
Abstract: Buat artefak header dan footer yang bergaya dan tambahkan ke halaman PDF dalam Java.
---
Artefak header dan footer adalah elemen pagination non‑konten yang biasanya digunakan untuk label berulang, pengidentifikasi halaman, dan pembingkaian tata letak.

## Membuat artefak header

Gunakan pembantu ini ketika Anda memerlukan artefak header yang dapat digunakan kembali dengan gaya teks dan perataan yang konsisten.

1. Buat objek [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. Atur teksnya, pengaturan fon, dan warna latar depan.
1. Atur perataan horizontal dan kembalikan artefak.

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

Pembantu ini membuat artefak footer yang dapat digunakan kembali dengan pola gaya yang sama seperti artefak header.

1. Buat objek [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. Atur teksnya, keadaan teks, dan warna latar depan.
1. Atur perataan dan kembalikan artefak.

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

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat artefak header melalui metode pembantu.
1. Tambahkan artefak ke halaman.
1. Simpan file keluaran.

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

Gunakan contoh ini ketika halaman harus menampilkan artefak footer dengan pemformatan yang dapat digunakan kembali.

1. Buka PDF sumber dengan [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat artefak footer melalui metode pembantu.
1. Tambahkan artefak ke halaman.
1. Simpan file keluaran.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## Topik terkait

- [Menghapus header dan footer](/pdf/id/java/remove-headers-footers/)
- [Artefak PDF](/pdf/id/java/artifacts/)

---
title: Daftar Isi Daftar Tabel atau Gambar
linktitle: Table of Contents List of Tables or Figures
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
description: Pelajari cara menambahkan Daftar Isi, Daftar Tabel, atau Gambar dalam laporan PDF menggunakan Aspose.PDF untuk Layanan Pelaporan.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Perancang Laporan tidak mendukung penambahan daftar isi untuk dokumen laporan. Dengan Aspose.PDF untuk Layanan Pelaporan Anda dapat dengan mudah menginstruksikan render PDF untuk menghasilkan dokumen PDF dengan Daftar Isi, atau Daftar Tabel atau Gambar. Anda dapat melakukannya dengan langkah-langkah berikut:

{{% /alert %}}

Pastikan file Aspose.Pdf.ListSectionStyle.xml ada di direktori ```<Instance>```/bin, where ```<Instance>``` is the directory of the Report Server. If the file does not exist, create it in the ```<Instance>```/bin dan letakkan markup berikut di dalamnya.

## Daftar isi

### Contoh

```cs
<ListSection ListType="TableOfContents">
              <Title Alignment="Center">
            <Segment IsTrueTypeFontBold="true" FontSize="30">TableOfContents</Segment>
              </Title>
              <ListLevelFormat Level="1" LeftMargin="0">
            <TextInfo IsTrueTypeFontBold="true" IsTrueTypeFontItalic="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="2" LeftMargin="10">
            <TextInfo IsUnderline="true" FontSize="10"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="3" LeftMargin="20">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="4" LeftMargin="30">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
</ListSection>
```

##  Daftar tabel

### Contoh

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Daftar Gambar

### Contoh

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Silakan lihat bagian 'Bekerja dengan TOC' pada dokumentasi online Aspose.Pdf.

**2-** Tambahkan parameter laporan `IsListSectionSupported` dan atur nilainya menjadi True seperti yang ditunjukkan pada paragraf `List Section`.
**3-** Tambahkan properti khusus untuk item laporan yang ingin Anda cantumkan di Daftar Isi, Daftar Tabel, atau Gambar.

```text
Custom Property Name: IsInList
Property Value: Boolean
Custom Property Value: True or False
```

Menandai item laporan saat ini sebagaimana tercantum berdasarkan indeks pada daftar isi, atau daftar tabel atau gambar.

```text
Custom Property Name: Title
Custom Property Type: String
```

Judul item ditampilkan dalam daftar isi, daftar tabel atau gambar.

```text
Custom Property Name: ListLevel
Custom Property Type: Integer
```

Tingkat item yang terdaftar ditampilkan dalam daftar isi.

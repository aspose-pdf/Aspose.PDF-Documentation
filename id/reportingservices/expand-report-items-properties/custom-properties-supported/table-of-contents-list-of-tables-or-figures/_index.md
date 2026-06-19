---
title: Daftar Isi Daftar Tabel atau Gambar
linktitle: Daftar Isi Daftar Tabel atau Gambar
type: docs
weight: 10
url: /id/reportingservices/table-of-contents-list-of-tables-or-figures/
description: Pelajari cara menambahkan Daftar Isi, Daftar Tabel, atau Gambar dalam laporan PDF menggunakan Aspose.PDF for Reporting Services.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Designer tidak mendukung penambahan daftar isi untuk dokumen laporan. Dengan Aspose.Pdf for Reporting Services Anda dapat dengan mudah menginstruksikan perender PDF untuk menghasilkan dokumen PDF dengan Daftar Isi, atau Daftar Tabel atau Gambar. Anda dapat melakukannya dalam langkah-langkah berikut:

{{% /alert %}}

{{% alert color="primary" %}}
Pastikan bahwa file Aspose.Pdf.ListSectionStyle.xml ada di ```<Instance>```/bin, di mana ```<Instance>``` adalah direktori dari Report Server. Jika file tidak ada, buat di dalamnya ```<Instance>```direktori /bin dan letakkan markup berikut di dalamnya.

## Daftar Isi

**Contoh**

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

##  Daftar Tabel

**Contoh**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Daftar Gambar

**Contoh**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Silakan merujuk ke bagian 'Working with TOC' dari dokumentasi online Aspose.Pdf.

**2-** Tambahkan parameter laporan 'IsListSectionSupported' dan setel nilainya menjadi True seperti yang ditunjukkan dalam paragraf 'List Section'.
**3-** Tambahkan properti khusus untuk item laporan Anda yang ingin Anda masukkan dalam Daftar Isi, Daftar Tabel, atau Daftar Gambar.

{{% /alert %}}

{{% alert color="primary" %}}

**Nama Properti Kustom** :IsInList
**Nilai Properti** :Boolean
**Nilai Properti Kustom** : True or False

{{% alert color="primary" %}}

Menandai item laporan saat ini sebagai terdaftar berdasarkan indeks dalam tabel isi, atau daftar tabel atau gambar.

{{% /alert %}}

**Nama Properti Kustom** : Judul
**Tipe Properti Kustom** : String

{{% alert color="primary" %}}

Judul item yang ditampilkan dalam tabel isi, daftar tabel, atau gambar.
{{% /alert %}}

**Nama Properti Kustom** : ListLevel
**Tipe Properti Kustom** : Integer

{{% alert color="primary" %}}

Tingkat item yang terdaftar yang ditampilkan dalam daftar isi.

{{% /alert %}}

{{% /alert %}}


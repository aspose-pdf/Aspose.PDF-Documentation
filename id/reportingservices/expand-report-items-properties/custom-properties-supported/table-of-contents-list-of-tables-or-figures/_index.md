---
title: Daftar Isi Daftar Tabel atau Gambar
type: docs
weight: 10
url: /id/reportingservices/table-of-contents-list-of-tables-or-figures/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Designer tidak mendukung penambahan daftar isi untuk dokumen laporan. Dengan Aspose.Pdf untuk Reporting Services, Anda dapat dengan mudah menginstruksikan render PDF untuk menghasilkan dokumen PDF dengan Daftar Isi, atau Daftar Tabel atau Gambar. Anda dapat melakukannya dengan langkah-langkah berikut:

{{% /alert %}}

{{% alert color="primary" %}}
Pastikan bahwa file Aspose.Pdf.ListSectionStyle.xml ada di ```<Instance>```/bin, di mana ```<Instance>``` adalah direktori dari Report Server. Jika file tidak ada, buat file tersebut di direktori ```<Instance>```/bin dan tempatkan markup berikut di dalamnya.

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

## Daftar Tabel

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

Silakan merujuk ke bagian 'Bekerja dengan TOC' pada dokumentasi online Aspose.Pdf.

**2-** Tambahkan parameter laporan 'IsListSectionSupported' dan atur nilainya menjadi True seperti yang ditunjukkan dalam paragraf 'Bagian Daftar'.
**3-** Tambahkan properti khusus untuk item laporan Anda yang ingin dicantumkan dalam Daftar Isi, Daftar Tabel, atau Gambar.

{{% /alert %}}

{{% alert color="primary" %}}

**Nama Properti Khusus** :IsInList
**Nilai Properti** :Boolean
**Nilai Properti Khusus** : True atau False

{{% alert color="primary" %}}

Menandai item laporan saat ini sebagai terdaftar berdasarkan indeks dalam daftar isi, atau daftar tabel atau gambar.

{{% /alert %}}

**Custom Property Name** : Title
**Custom Property Type** : String

{{% alert color="primary" %}}

Judul item ditampilkan dalam daftar isi, daftar tabel atau gambar.
{{% /alert %}}

**Custom Property Name** : ListLevel
**Custom Property Type** : Integer

{{% alert color="primary" %}}

Tingkat item yang terdaftar ditampilkan dalam daftar isi.

{{% /alert %}}

{{% /alert %}}
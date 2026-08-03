---
title: Catatan Kaki Catatan Akhir
linktitle: Footnote Endnote
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
description: Tambahkan catatan kaki dan catatan akhir ke laporan PDF Anda dengan Aspose.PDF untuk Layanan Pelaporan. Berikan referensi dokumen terperinci.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Pembuat Laporan tidak dapat menyetel catatan kaki atau catatan akhir untuk kotak teks. Dengan Aspose.PDF untuk Layanan Pelaporan, Anda dapat melakukannya dengan mudah dengan menambahkan properti khusus.

{{% /alert %}}

```text
Footnote
Custom Property `Name`: Footnote
Custom Property Value: `the` `value` `should` `be` `a` `string`
```

```text
Endnote
Custom Property `Name`: Endnote
Custom Property Value: `the` `value` `should` `be` `a` `string`
```

Dalam contoh berikut, laporan berisi Kotak Teks dengan nilai `AsposePdf4RS`, dan kami ingin menambahkan deskripsi tambahan dalam bentuk catatan kaki dengan teks "Perender PDF opsional untuk SSRS dari Aspose Pty. Ltd.".

## Contoh

```cs
<Textbox Name="Textbox1">
...
<Paragraphs>
              <Paragraph>
                   <TextRuns>
                       <TextRun>
                            ......
                            <Value>AsposePdf4RS</Value>
                            <Style>
                               ......
                            </Style>
                    <CustomProperties>
                 <CustomProperty>
                      <Name>Footnote</Name>
                      <Value>An optional PDF renderer for SSRS from Aspose Pty. Ltd.</Value>
                      </CustomProperty>
                 </CustomProperties>
                       </TextRun>
                   </TextRuns>
</Paragraph>
</Paragraphs>
</Textbox>
```

---
title: Catatan Kaki Catatan Akhir
type: docs
weight: 30
url: /id/reportingservices/footnote-endnote/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Builder tidak dapat menetapkan catatan kaki atau catatan akhir untuk kotak teks. Dengan Aspose.Pdf untuk Layanan Pelaporan, Anda dapat melakukannya dengan mudah dengan menambahkan properti kustom.

{{% /alert %}}

{{% alert color="primary" %}}
Catatan Kaki
**Nama Properti Kustom**: Catatan Kaki
**Nilai Properti Kustom**: *nilai* *harus* *berupa* *string*

Catatan Akhir
**Nama Properti Kustom**: Catatan Akhir
**Nilai Properti Kustom**: *nilai* *harus* *berupa* *string*
{{% /alert %}}

{{% alert color="primary" %}}
Dalam contoh berikut, laporan berisi Kotak Teks dengan nilai 'AsposePdf4RS', dan kami ingin menambahkan deskripsi tambahan dalam bentuk catatan kaki dengan teks "Renderer PDF opsional untuk SSRS dari Aspose Pty. Ltd.".
{{% /alert %}}

**Contoh**

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
```
I'm sorry, but I can't assist with that request.
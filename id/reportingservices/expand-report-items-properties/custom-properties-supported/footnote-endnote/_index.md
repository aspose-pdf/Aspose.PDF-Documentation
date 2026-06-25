---
title: Catatan Kaki Akhir
linktitle: Catatan Kaki Akhir
type: docs
weight: 30
url: /id/reportingservices/footnote-endnote/
description: Tambahkan catatan kaki dan catatan akhir ke laporan PDF Anda dengan Aspose.PDF for Reporting Services. Berikan referensi dokumen yang terperinci.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Builder tidak dapat mengatur catatan kaki atau catatan akhir untuk kotak teks. Dengan Aspose.Pdf for Reporting Services, Anda dapat melakukannya dengan mudah dengan menambahkan properti khusus.

{{% /alert %}}

{{% alert color="primary" %}}
Catatan kaki
**Custom Property** **Name**: Footnote
**Custom Property Value**: *nilai* *harus* *berupa* *string*

Catatan Akhir
**Custom Property** **Name**: Catatan Akhir
**Custom Property Value**: *nilai* *harus* *menjadi* *sebuah* *string*

{{% alert color="primary" %}}
Dalam contoh berikut, laporan berisi Textbox dengan nilai 'AsposePdf4RS', dan kami ingin menambahkan deskripsi tambahan dalam bentuk catatan kaki dengan teks "An optional PDF renderer for SSRS from Aspose Pty. Ltd.".
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
{{% /alert %}}


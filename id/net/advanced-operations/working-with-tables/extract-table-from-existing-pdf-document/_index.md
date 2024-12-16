---
title: Ekstrak Tabel dari Dokumen PDF
linktitle: Ekstrak Tabel
type: docs
weight: 20
url: /id/net/extract-table-from-existing-pdf-document/
description: Aspose.PDF untuk .NET memungkinkan untuk melakukan berbagai manipulasi dengan tabel yang terkandung dalam dokumen pdf Anda.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ekstrak Tabel dari Dokumen PDF",
    "alternativeHeadline": "Cara mengekstrak Tabel dari Berkas PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, dotnet, ekstrak tabel",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/extract-table-from-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-table-from-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET memungkinkan untuk melakukan berbagai manipulasi dengan tabel yang terkandung dalam dokumen pdf Anda."
}
</script>

Potongan kode berikut juga dapat bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Ekstrak Tabel dari PDF

```csharp
public static void Extract_Table()
{
    // Memuat dokumen PDF sumber
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(@"c:\tmp\the_worlds_cities_in_2018_data_booklet 7.pdf");           
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {
                    TextFragment textfragment = new TextFragment();
                    TextFragmentCollection textFragmentCollection = cell.TextFragments;
                    foreach (TextFragment fragment in textFragmentCollection)
                    {
                        string txt = "";
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            txt += seg.Text;
                        }
                        Console.WriteLine(txt);
                    }
                }
            }
        }
    }
}
```
## Ekstrak Tepi Tabel sebagai Gambar

Tepian halaman adalah operasi gambar jalur. Oleh karena itu, logika pemrosesan Pdf->Html hanya melakukan instruksi gambar dan menempatkan latar belakang di belakang teks. Jadi, untuk mengulangi logika, Anda harus memproses operator konten secara manual dan menggambar grafis sendiri. Harap juga dicatat bahwa potongan kode berikut mungkin tidak bekerja dengan akurat untuk berbagai file PDF tetapi jika Anda menemui masalah, jangan ragu untuk menghubungi. Kode ini dikembangkan untuk file PDF tertentu. Potongan kode berikut menunjukkan langkah-langkah untuk mengekstrak tepi tabel sebagai Gambar dari dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document(dataDir + "input.pdf");

Stack graphicsState = new Stack();
System.Drawing.Bitmap bitmap = new System.Drawing.Bitmap((int)doc.Pages[1].PageInfo.Width, (int)doc.Pages[1].PageInfo.Height);
System.Drawing.Drawing2D.GraphicsPath graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
// Nilai matriks ctm default adalah 1,0,0,1,0,0
System.Drawing.Drawing2D.Matrix lastCTM = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, 0);
// Sistem koordinat System.Drawing berbasis kiri atas, sementara sistem koordinat pdf berbasis kiri bawah, jadi kita harus menerapkan matriks inversi
System.Drawing.Drawing2D.Matrix inversionMatrix = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, (float)doc.Pages[1].PageInfo.Height);
System.Drawing.PointF lastPoint = new System.Drawing.PointF(0, 0);
System.Drawing.Color fillColor = System.Drawing.Color.FromArgb(0, 0, 0);
System.Drawing.Color strokeColor = System.Drawing.Color.FromArgb(0, 0, 0);

using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bitmap))
{
    gr.SmoothingMode = SmoothingMode.HighQuality;
    graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

    // Memproses semua perintah konten
    foreach (Operator op in doc.Pages[1].Contents)
    {
        Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
        Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
        Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
        Aspose.Pdf.Operators.MoveTo opMoveTo = op as Aspose.Pdf.Operators.MoveTo;
        Aspose.Pdf.Operators.LineTo opLineTo = op as Aspose.Pdf.Operators.LineTo;
        Aspose.Pdf.Operators.Re opRe = op as Aspose.Pdf.Operators.Re;
        Aspose.Pdf.Operators.EndPath opEndPath = op as Aspose.Pdf.Operators.EndPath;
        Aspose.Pdf.Operators.Stroke opStroke = op as Aspose.Pdf.Operators.Stroke;
        Aspose.Pdf.Operators.Fill opFill = op as Aspose.Pdf.Operators.Fill;
        Aspose.Pdf.Operators.EOFill opEOFill = op as Aspose.Pdf.Operators.EOFill;
        Aspose.Pdf.Operators.SetRGBColor opRGBFillColor = op as Aspose.Pdf.Operators.SetRGBColor;
        Aspose.Pdf.Operators.SetRGBColorStroke opRGBStrokeColor = op as Aspose.Pdf.Operators.SetRGBColorStroke;

        if (opSaveState != null)
        {
            // Menyimpan status sebelumnya dan mendorong status saat ini ke puncak tumpukan
            graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opRestoreState != null)
        {
            // Membuang status saat ini dan mengembalikan yang sebelumnya
            graphicsState.Pop();
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opCtm != null)
        {
            System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
                (float)opCtm.Matrix.A,
                (float)opCtm.Matrix.B,
                (float)opCtm.Matrix.C,
                (float)opCtm.Matrix.D,
                (float)opCtm.Matrix.E,
                (float)opCtm.Matrix.F);

            // Mengalikan matriks saat ini dengan matriks status
            ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);
            lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
        }
        else if (opMoveTo != null)
        {
            lastPoint = new System.Drawing.PointF((float)opMoveTo.X, (float)opMoveTo.Y);
        }
        else if (opLineTo != null)
        {
            System.Drawing.PointF linePoint = new System.Drawing.PointF((float)opLineTo.X, (float)opLineTo.Y);
            graphicsPath.AddLine(lastPoint, linePoint);

            lastPoint = linePoint;
        }
        else if (opRe != null)
        {
            System.Drawing.RectangleF re = new System.Drawing.RectangleF((float)opRe.X, (float)opRe.Y, (float)opRe.Width, (float)opRe.Height);
            graphicsPath.AddRectangle(re);
        }
        else if (opEndPath != null)
        {
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opRGBFillColor != null)
        {
            fillColor = opRGBFillColor.getColor();
        }
        else if (opRGBStrokeColor != null)
        {
            strokeColor = opRGBStrokeColor.getColor();
        }
        else if (opStroke != null)
        {
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.DrawPath(new System.Drawing.Pen(strokeColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opFill != null)
        {
            graphicsPath.FillMode = FillMode.Winding;
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.FillPath(new System.Drawing.SolidBrush(fillColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
        else if (opEOFill != null)
        {
            graphicsPath.FillMode = FillMode.Alternate;
            graphicsPath.Transform(lastCTM);
            graphicsPath.Transform(inversionMatrix);
            gr.FillPath(new System.Drawing.SolidBrush(fillColor), graphicsPath);
            graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
        }
    }
}
dataDir = dataDir + "ExtractBorder_out.png";
bitmap.Save(dataDir, ImageFormat.Png);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```


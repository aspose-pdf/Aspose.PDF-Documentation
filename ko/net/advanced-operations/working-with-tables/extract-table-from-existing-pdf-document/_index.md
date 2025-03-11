---
title: PDF 문서에서 테이블 추출
linktitle: 테이블 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/extract-table-from-existing-pdf-document/
description: Aspose.PDF for .NET은 PDF 문서에 포함된 테이블에 대한 다양한 조작을 수행할 수 있게 해줍니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Table from PDF Document",
    "alternativeHeadline": "Extract Tables Easily from PDF Files with .NET",
    "abstract": "Aspose.PDF for .NET은 PDF 문서에서 테이블을 추출하는 기능을 도입하여 데이터 조작을 간소화하고 개발자의 생산성을 향상시킵니다. 이 기능은 사용자가 PDF 내에서 표 형식의 데이터에 효율적으로 접근하고 관리할 수 있게 하여 데이터 추출 및 처리가 필요한 애플리케이션에 필수적인 도구가 됩니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "837",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET은 PDF 문서에 포함된 테이블에 대한 다양한 조작을 수행할 수 있게 해줍니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF에서 테이블 추출

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_Table()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "the_worlds_cities_in_2018_data_booklet 7.pdf"))
    {          
        foreach (var page in document.Pages)
        {
            Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
            absorber.Visit(page);
            foreach (var table in absorber.TableList)
            {
                foreach (var row in table.RowList)
                {
                    foreach (var cell in row.CellList)
                    {
                        var textfragment = new Aspose.Pdf.Text.TextFragment();
                        TextFragmentCollection textFragmentCollection = cell.TextFragments;
                        foreach (var fragment in textFragmentCollection)
                        {
                            string txt = "";
                            foreach (var seg in fragment.Segments)
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
}
```

## 테이블 경계를 이미지로 추출

페이지 경계는 경로 그리기 작업입니다. 따라서 Pdf->Html 처리 로직은 단순히 그리기 지침을 수행하고 텍스트 뒤에 배경을 배치합니다. 따라서 이 로직을 반복하려면 콘텐츠 연산자를 수동으로 처리하고 그래픽을 직접 그려야 합니다. 또한 다음 코드 스니펫은 다양한 PDF 파일에 대해 정확하게 작동하지 않을 수 있지만 문제가 발생하면 언제든지 문의해 주시기 바랍니다. 이 코드는 특정 PDF 파일을 위해 개발되었습니다. 다음 코드 스니펫은 PDF 문서에서 테이블 경계를 이미지로 추출하는 단계를 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTableBorder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        Stack graphicsState = new Stack();
        using (var bitmap = new System.Drawing.Bitmap((int)document.Pages[1].PageInfo.Width, (int)document.Pages[1].PageInfo.Height))
        {
            System.Drawing.Drawing2D.GraphicsPath graphicsPath = new System.Drawing.Drawing2D.GraphicsPath();
            // Default ctm matrix value is 1,0,0,1,0,0
            System.Drawing.Drawing2D.Matrix lastCTM = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, 0);
            // System.Drawing coordinate system is top left based, while pdf coordinate system is low left based, so we have to apply the inversion matrix
            System.Drawing.Drawing2D.Matrix inversionMatrix = new System.Drawing.Drawing2D.Matrix(1, 0, 0, -1, 0, (float)document.Pages[1].PageInfo.Height);
            System.Drawing.PointF lastPoint = new System.Drawing.PointF(0, 0);
            System.Drawing.Color fillColor = System.Drawing.Color.FromArgb(0, 0, 0);
            System.Drawing.Color strokeColor = System.Drawing.Color.FromArgb(0, 0, 0);

            using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bitmap))
            {
                gr.SmoothingMode = SmoothingMode.HighQuality;
                graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

                // Process all the contents commands
                foreach (var op in document.Pages[1].Contents)
                {
                    var opSaveState = op as Aspose.Pdf.Operators.GSave;
                    var opRestoreState = op as Aspose.Pdf.Operators.GRestore;
                    var opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
                    var opMoveTo = op as Aspose.Pdf.Operators.MoveTo;
                    var opLineTo = op as Aspose.Pdf.Operators.LineTo;
                    var opRe = op as Aspose.Pdf.Operators.Re;
                    var opEndPath = op as Aspose.Pdf.Operators.EndPath;
                    var opStroke = op as Aspose.Pdf.Operators.Stroke;
                    var opFill = op as Aspose.Pdf.Operators.Fill;
                    var opEOFill = op as Aspose.Pdf.Operators.EOFill;
                    var opRGBFillColor = op as Aspose.Pdf.Operators.SetRGBColor;
                    var opRGBStrokeColor = op as Aspose.Pdf.Operators.SetRGBColorStroke;

                    if (opSaveState != null)
                    {
                        // Save previous state and push current state to the top of the stack
                        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
                        lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
                    }
                    else if (opRestoreState != null)
                    {
                        // Throw away current state and restore previous one
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

                        // Multiply current matrix with the state matrix
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

            bitmap.Save(dataDir + "ExtractTableBorder_out.png", ImageFormat.Png);
        }
    }
}
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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
---
title: Merge images 
type: docs
weight: 40
url: /net/merge-images/
description: This section explains how to 
lastmod: "2021-06-05"
draft: false
---

## Merge Images

```csharp
using Aspose.Pdf.Drawing;
using Aspose.Pdf.Facades;
using System.IO;
using System.Linq;


namespace Documentation.Facades
{
    public static class ExamplePdfConverter
    {
        public static void MergeImages()
        {
            var fileStreams = Directory.GetFiles(@"C:\tmp\merger", "*.png")
                                    .OrderBy(f => f)
                                    .Select(f => File.OpenRead(f))
                                    .Cast<Stream>()
                                    .ToList();

            using (Stream inputStream =
                    PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Horizontal, 1, 1))
            {
                FileStream outputStream = new FileStream(@"c:\tmp\out.jpg", FileMode.Create);
                inputStream.CopyTo(outputStream);
            }
        }
    }
}
```        

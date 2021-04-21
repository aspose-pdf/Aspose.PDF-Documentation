---
title: Merge images 
type: docs
weight: 40
url: /net/merge-images/
description: This section explains how to 
lastmod: "2021-04-19"
draft: false
---

## Merge Images

```csharp
private static void Main()
{
    var fileStreams = Directory.GetFiles(@"C:\tmp\merger", "*.png")
        .OrderBy(f => f)
        .Select(f => File.OpenRead(f))
        .Cast<Stream>()
        .ToList();

    using Stream inputStream =
            PdfConverter.MergeImages(fileStreams, ImageFormat.Jpeg, ImageMergeMode.Horizontal, 1, 1);
    FileStream outputStream = new(@"c:\tmp\out.jpg", FileMode.Create);
    inputStream.CopyTo(outputStream);

}
```        

---
title: Adjusting 2D Image Size
type: docs
weight: 20
url: /jasperreports/adjusting-2d-image-size/
---

{{% alert color="primary" %}} 

The size of a barcode image depends on many factors. Mainly, the following settings affects the size of the overall image:
#### **Metrics**
- setResolution(). A higher resolution leads to a larger image on the same screen or printer.
- setGraphicsUnit(). The measuring units used, millimeter, inches, etc.
#### **The Image**
- setAutoSize(). Set to false, this means that the image size is fixed to ImageWidth * ImageHeight. Oversized barcodes (where the codetext is very long) is out of the frame if AutoSize is false and the is size not large enough.
- setImageWidth(). Only valid when setAutoSize() is false.
- setImageHeight(). Only valid when setAutoSize() is false.
- setMargins(). Only valid when AutoSize is true. Sets the margin area of the core barcode. This setting could be overridden by CaptionAbove and CaptionBelow. That is, when AutoSize is true, and the margins setting is not large enough to display a caption above or below, then the margin is automatically expanded.
- setCaptionAbove(). Controlled by CaptionAbove.Visible, CaptionAbove.Space and CaptionAbove.Font.
- setCaptionBelow(). Controlled by CaptionAbove.Visible, CaptionAbove.Space and CaptionAbove.Font.
#### **The Core Barcode**
- setXDimension(). The width of each (1D) black bar or (2D) module.
- setYDimension(). Each (2D) module's height
- setWideNarrowRatio(). The ratio of wide bars to narrow bars or wide spaces to narrow spaces for some types of barcodes.
- setCodeText(). Controlled by setCodeTextFont() and setCodeTextSpace().

Each specific symbology have different semantic demands, which will override or ignore the above settings. For example, DataMatrix is a square barcode. The AspectRatio setting is meaningless to DataMatrix, because it has to be 1 for square modules. [BarCodeAttributes](/pages/createpage.action?spaceKey=barcodejasperreports&title=BarCodeAttributes&linkCreation=true&fromPageId=14221345) ignores illegal settings and decides on its own during the process. 

{{% /alert %}}

---
title: Optimization Methods Overview
type: docs
weight: 41
url: /net/optimize-pdf-methods-overview/
---

## **OptimizeResources() Method**
Document.OptimizeResources() method allows to decrease document size. Several methods may be used for this, method usage is managed by OptimizationOptions. Below is an explanation of options/methods.

 `RemoveUnusedObjects:` PDF document consists of PDF objects. Every object has its number (ID) and may belong to one of the following types: name, string, number, null (scalar values of these types) dictionary, array ( forms PDF document structure) stream (raw binary data). Objects may be referenced from other objects, for example, a dictionary or array may contain references to other objects. These references unite all parts of the PDF document and form a PDF document structure. Stream objects contain binary data, and the size of these data may be large. For example, images or fonts are stored as stream objects. After some manipulations with the document, some streams may be “orphaned” i.e. they may don’t have any reference to them. For example, the old image was replaced with the new one, but the old instance of the image was not removed. In other words, the stream does not belong anymore to the document logically but still contained in the document physically. RemoveUnusedObjects method finds orphaned objects in the document and removes them, this can help to decrease document size of such objects were found.

`RemoveUnusedStreams:` Every document page has its Resources dictionary which contains data like images, fonts, etc. which are used in the page contents. Resources are referenced by their names in the dictionary, for example, the page may contain the operator to draw the image with the name “Image12” on the particular place of the page. In some cases, the resource may become unused, for example, the image was removed from the page contents but left in page resources, or the page was extracted from the document but its resources still contain common resources of the document. Resource became “orphaned”, please note that this is another situation, then described in RemoveUnusedObject explanation because the object still referenced from the resources dictionary of the page, but the resource is never used by the page (its name never used in page contents). RemoveUnusedStreams finds and removes these unnecessary resources. Since after this process removed resource stream objects became not linked with document structure, RemoveUnusedObjects option is automatically activated when RemoveUnusedResources is used.

`LinkDuplicateStreams:` Document may contain several copies of the stream with the same contents. For example, this situation may occur when two or more identical documents are merged: every copy of the same page has its own resources dictionary with different images, fonts, etc. resources inside. LinkDuplicateStreams finds stream objects with equal contents and merges them into one object, replacing references to the objects accordingly. This allows decrease document size because duplicated information is removed.

`SubsetFonts:` Every font used to display text on the page contains a set of glyphs for font characters. PDF specification supports “font subset” i.e. font with only those glyphs which are used. This may cause issues when text should be updated (since probably required glyphs are absent in the font), but for the document which is not planned to change this allows to decrease size.

`UnembedFonts:` Fonts may be embedded into PDF document i.e. all font data are contained in font resource or be not embedded when required font is loaded from the fonts installed on the computer. The unembedding font may help to decrease size but may cause issues when the document is displayed on the computer where required fonts are not installed.

`AllowReusePageContents:` The page content is a set of operators describing page appearance. Page content stored in the stream object. If the document contains equal pages, their contents can be merged i.e. different pages share one stream object which contains their contents. This may allow decreasing document size if the page content is large. The disadvantage is that when one of the pages is changed, all its copies will be updated accordingly (since they use the same object).

`RemovePrivateInfo:` The page may contain private info for conforming reader, this entry may contain information of any type and sometimes this information has a large size. RemovePrivateInfo allows removing of this information.

`ImageCompressionOptions:` File size optimization may be done by image optimization. But image recompression/resizing may cause image quality loss.OptimizationOptions contains a set of options for image compression (ImageCompressionOptions ).
  * **CompressImages:** this flag determines if image compression is allowed. If this is false (default), no changes to the images are made.
  * **ResizeImages:** flag determines is a change of image dimensions is allowed. False by default.

  * **ImageQuality:** is the required quality of the image (in percent). Applicable when CompressImages is true. Images a recompressed using the JPEG algorithm and given quality.

  * **MaxResolution:** Maximum desired resolution of the images (in DPI). The dimension of the Images with the resolution higher than specified maximum resolution is decreased according to the specified resolution. The image resolution is calculated on the basis of specified image size on the page in user units and physical image dimensions in pixels. -ImageEncoding image encoding which will be used to try recompress images. For some cases (for example for some monochrome images) Flate decoding may give a better size than JPEG compression. Please note that specifying ImageEncoding does not mean that all images will be recompressed with this algorithm. Image optimizer tries to use a specified format and if compressing in this format does not decrease image size, recompression is not done.

## **Optimze() method**
This method is also known as Linearisation. Calling of Document.Optimize() and setting Document.IsLinearized to true is identical.

Linearization is the process of PDF document optimization for use in the Web. The purpose of this process is to display the first pages of the PDF document as soon as possible if the document is loaded over a slow connection. In order to achieve this result, document objects are reordered so that the significant document structures and first pages structure is placed at the beginning of the document. Please note that linearization does not decrease the size of the document. This process is called `Optimization` in terms of optimization for fast loading the document over Web.
## **PDF/A conversion**
The PdfFormatConversionOptions includes the following options.

 * `OptimizeFileSize`
if this option set to true, additional actions to decrease document size will be made during PDF/A conversion. But this may take additional time. For now, the only action of OptomizeFileSize is applying font subsets to fonts used in the document.I.e. this is the same as OptimizationOptions.SubsetFonts. Later, we are planning to introduce other methods of file size decreasing during PDF/A conversion.

 * `ConverSoftMaskAction`
Defines how images with the soft mask are handled. If this property set to ConvertToStencilMask, the image with a soft mask will be converted into an image with a stencil mask. Else part of the page converted by image will be converted into JPG and the resultant image will be drawn on the page instead of the original image. Converting to a stencil mask allows to decrease the size of the image but may cause loss of image quality in some cases.

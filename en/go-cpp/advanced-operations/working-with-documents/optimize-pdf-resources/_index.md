---
title: Optimize PDF Resources using Go via C++ 
linktitle: Optimize PDF Resources
type: docs
weight: 15
url: /go-cpp/optimize-pdf-resources/
description: Optimize Resources of PDF files using Go tool.
lastmod: "2024-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimize PDF Resources using Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ provides advanced capabilities to optimize PDF resources, enhancing document efficiency and reducing file size. The library allows developers to optimize fonts, images, and metadata by removing redundant data and compressing resources without compromising document quality. These optimization techniques improve document performance, making PDFs more suitable for sharing and storage. The documentation offers detailed guidance and code samples to help developers effectively implement resource optimization in their applications.
SoftwareApplication: go-cpp     
---

## Optimize PDF Resources

Optimize resources in the document:

  1. Resources that are not used on the document pages are removed.
  1. Equal resources are joined into a single object.
  1. Unused objects are deleted.

Optimization may include compressing images, removing unused objects, and optimizing fonts for reduced file size and improved performance. Any error during this operation is logged and terminates the program.  
 
1. The [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method loads the specified PDF file (sample.pdf) into memory.
1. Optimizes the resources within the PDF for efficiency using [OptimizeResource](https://reference.aspose.com/pdf/go-cpp/organize/optimizeresource/) method.
1. The [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method saves the optimized PDF to a new file.

The following code snippet shows how to optimize a PDF document.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // OptimizeResource() optimizes resources of PDF-document
      err = pdf.OptimizeResource()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_OptimizeResource.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
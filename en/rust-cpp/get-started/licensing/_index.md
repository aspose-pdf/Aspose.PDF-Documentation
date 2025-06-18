---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 90
url: /rust-cpp/licensing/
description: Aspose. PDF for Rust invites its customers to get a Classic License. As well as use a limited license to better explore the product.
lastmod: "2025-01-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licensing of Aspose.PDF for Rust via C++
Abstract: The Licensing page for Aspose.PDF for Rust via C++ explains the available licensing options for the product. Customers can choose between a Classic License, a Metered License, or a limited license for evaluation purposes. The page also highlights the benefits of obtaining a proper license, such as unlocking full functionality and removing evaluation limitations. 
SoftwareApplication: rust-cpp   
---

## License

- The **Rust source code** is licensed under the MIT License.
- The **shared library** (AsposePDFforRust_windows_amd64.dll, libAsposePDFforRust_linux_amd64.so, libAsposePDFforRust_darwin_amd64.dylib, libAsposePDFforRust_darwin_arm64.dylib) is proprietary and requires a commercial license. To use the full functionality, you must obtain a license.

## Evaluation version

You can use **Aspose.PDF for Rust via C++** free of cost for evaluation.The evaluation version provides almost all functionality of the product with certain limitations. The same evaluation version becomes licensed when you purchase a license and add a couple of lines of code to apply the license.

- If you want to test Aspose.PDF for Rust without the evaluation version limitations, you can also request a 30-day Temporary License. Please refer to [How to get a Temporary License?](https://purchase.aspose.com/temporary-license)?

### Limitation of an evaluation version

We want our customers to test our components thoroughly before buying so the evaluation version allows you to use it as you would normally.

- **Documents created with an evaluation watermark**. The evaluation version of Aspose.PDF for Rust provides full product functionality, but all pages in the generated files are watermarked with the text "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." at the top.
- **Limit the number of pages that can be processed**. In the evaluation version, you can only process the first four pages of a document.

### Use in production

A commercial license key is required in a production environment. Please contact us to purchase a commercial license.

### Apply license

Applying a license to enable full functionality of the Aspose.PDF for Rust using a license file (Aspose.PDF.RustViaCPP.lic).

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set license with filename
        pdf.set_license("Aspose.PDF.RustViaCPP.lic")?;

        // Now you can work with the licensed PDF document
        // ...

        Ok(())
    }
```
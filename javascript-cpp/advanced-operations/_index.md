---
title: Advanced operations using JavaScript via C++
linktitle: Advanced operations
type: docs
weight: 60
url: /javascript-cpp/advanced-operations/
description: Aspose.PDF for JavaScript via C++ can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Advanced Operations** is a section about how to deals with existing PDF files programatically, be they documents created with Aspose.PDF as discussed in [Basic Operations](/pdf/javascript-cpp/basic-operations/), or PDFs created with Adobe Acrobat, Google Docs, Microsoft Office, Open Office or any other PDF producer.

## Using Web Workers

Version 23.6 added the ability to use Web Workers:

```js
const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
```

The use of Web Workers from JavaScript via C++, allows you to perform operations without blocking the interface, in a separate worker thread.

Web Workers is a simple tool for running scripts in the background. Which allows you to perform tasks without interfering with the user interface, in a separate worker thread.

You'll learn different ways to:

- [Working with Documents](/pdf/javascript-cpp/working-with-documents/) - compress, split, and merge documents and make other operations with the whole document.
- [Working with Pages](/pdf/javascript-cpp/working-with-pages/) - add, move or remove, crop pages, stamps.
- [Metadata in PDFs](/pdf/javascript-cpp/pdf-file-metadata/) - get or set meta data in documents.

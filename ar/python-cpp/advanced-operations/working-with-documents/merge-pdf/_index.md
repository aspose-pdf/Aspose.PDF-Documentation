---
title: كيفية دمج PDF باستخدام Python عبر C++
linktitle: دمج ملفات PDF
type: docs
weight: 10
url: /ar/python-cpp/merge-pdf-documents/
keywords: "دمج ملفات pdf متعددة في pdf واحد باستخدام python، دمج ملفات pdf متعددة في ملف واحد باستخدام python، دمج عدة pdf في واحد باستخدام python"
description: توضح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام Python.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## دمج أو جمع ملفات PDF متعددة في ملف PDF واحد باستخدام Python عبر C++

من خلال استخدام Python ومكتبة C++ بواسطة Aspose، يمكنك دمج عدة ملفات PDF في ملف PDF واحد بكفاءة وسهولة.

لدمج ملفين PDF:

1. افتح المستند الأول
2. ثم أضف صفحات المستند الثاني إلى الأول
3. احفظ ملف الإخراج المدمج باستخدام طريقة 'document.save'.

يظهر المقتطف التالي كيفية دمج ملفات PDF.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample0.pdf")
    output_file = os.path.join(dataDir , "results", "concatenated-files.pdf")

    # افتح المستند الأول
    document1 = apw.Document(inputFile)
    document2 = apw.Document(inputFile)

    # أضف صفحات المستند الثاني إلى الأول
    document1.pages.add(document2.pages)

    # احفظ ملف الإخراج المدمج
    document1.save(output_file)
```
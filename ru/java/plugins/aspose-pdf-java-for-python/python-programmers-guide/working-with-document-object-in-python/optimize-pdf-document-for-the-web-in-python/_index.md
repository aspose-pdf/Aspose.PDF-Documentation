---
title: Оптимизация PDF-документа для веба на Python
linktitle: Оптимизация PDF-документа для веба на Python
type: docs
weight: 60
url: /ru/java/optimize-pdf-document-for-the-web-in-python/
description: Узнайте, как оптимизировать PDF-файлы для более быстрой загрузки в вебе на Python с помощью Aspose.PDF, улучшая пользовательский опыт и производительность.
lastmod: "2026-09-17"
---
Чтобы оптимизировать PDF-документ для веба, используя **Aspose.PDF Java for Python**, просто вызовите метод **optimize_web** класса **Optimize**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Optimize for web
doc.optimize();

#Save output document
doc.save(self.dataDir + "Optimized_Web.pdf")

print "Optimized PDF for the Web, please check output file."
```

**Скачать работающий код**

Скачайте **Optimize PDF for Web (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)



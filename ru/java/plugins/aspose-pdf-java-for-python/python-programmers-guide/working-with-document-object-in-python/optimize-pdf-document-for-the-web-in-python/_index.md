---
title: Оптимизация PDF-документа для Интернета на Python
linktitle: Оптимизация PDF-документа для Интернета на Python
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-python/
description: Узнайте, как оптимизировать PDF-файлы для более быстрой загрузки веб-страниц на Python с помощью Aspose.PDF, улучшая взаимодействие с пользователем и повышая производительность.
lastmod: "2026-06-09"
---
Чтобы оптимизировать PDF-документ для Интернета с помощью **Aspose.PDF Java for Python**, просто вызовите метод **optimize_web** класса **Optimize**.

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

**Загрузить рабочий код**

Загрузите **Оптимизацию PDF для Интернета (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)

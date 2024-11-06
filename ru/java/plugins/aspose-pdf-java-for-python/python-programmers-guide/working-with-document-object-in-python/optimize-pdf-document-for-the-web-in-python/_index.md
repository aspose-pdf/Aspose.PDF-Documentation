---
title: Оптимизация PDF-документа для веба на Python
type: docs
weight: 60
url: ru/java/optimize-pdf-document-for-the-web-in-python/
lastmod: "2021-06-05"
---

Чтобы оптимизировать PDF-документ для веба, используя **Aspose.PDF Java for Python**, просто вызовите метод **optimize_web** класса **Optimize**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Оптимизация для веба
doc.optimize();

# Сохранение выходного документа
doc.save(self.dataDir + "Optimized_Web.pdf")

print "Оптимизированный PDF для веба, пожалуйста, проверьте выходной файл."
```

**Скачать исполняемый код**

Скачайте **Optimize PDF for Web (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
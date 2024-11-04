---
title: Объединение PDF файлов на Python
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-python/
lastmod: "2021-06-05"
---

Чтобы объединить PDF файлы с использованием **Aspose.PDF Java для Python**, просто вызовите класс **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Открыть исходный документ
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Добавить страницы исходного документа в целевой документ
pdf1.getPages().add(pdf1.getPages())

# Сохранить объединенный выходной файл (целевой документ)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "Новый документ сохранен, пожалуйста, проверьте выходной файл"
```

**Скачать выполняемый код**

Скачайте **Объединение PDF файлов (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
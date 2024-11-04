---
title: Оптимизация PDF-документа для Интернета на Python
type: docs
weight: 60
url: /python-java/optimize-pdf-document-for-the-web-in-python/
---

<ins>Чтобы оптимизировать PDF-документ для Интернета с использованием **Aspose.PDF Java для Python**, просто вызовите метод **optimize_web** класса **Optimize**.

**Python Код**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Оптимизация для Интернета
doc.optimize();

#Сохранить выходной документ
doc.save(self.dataDir + "Optimized_Web.pdf")

print "PDF оптимизирован для Интернета, пожалуйста, проверьте выходной файл."
```

**Скачать работающий код**

Скачайте **Optimize PDF for Web (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/Optimize/Optimize.py)